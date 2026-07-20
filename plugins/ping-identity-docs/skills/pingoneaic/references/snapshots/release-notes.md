---
title: Akamai Account Protector node
description: Use the Akamai Account Protector node to inject the Akamai risk score into an Advanced Identity Cloud authentication journey
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/akamai-acc-protect-node
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/akamai-acc-protect-node.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  compatibility: Compatibility
  inputs: Inputs
  dependencies: Dependencies
  akamai-acc-prot-setup: Configure Akamai Account Protector
  enable_account_protector_on_the_akamai_edge: Enable Account Protector on the Akamai Edge
  add_the_username_parameter_to_akamai_account_protector: Add the username parameter to Akamai Account Protector
  configuration: Configuration
  outputs: Outputs
  example: Example
---

# Akamai Account Protector node

Use the Akamai Account Protector node to inject the Akamai risk score into your authentication journey. When the Akamai Account Protector feature is enabled for your application, the Akamai Edge service provides the risk score in the HTTP header. Learn more in the [Akamai Account Protector](https://techdocs.akamai.com/cloud-security/docs/account-protector) documentation.

## Compatibility

| Product                               | Compatible? |
| ------------------------------------- | ----------- |
| Advanced Identity Cloud               | Yes         |
| PingAM (self-managed)                 | Yes         |
| Ping Identity Platform (self-managed) | Yes         |

## Inputs

This node retrieves user risk data from the Akamai-User-Risk HTTP request header.

## Dependencies

You must set up [Akamai Account Protector](https://www.akamai.com/resources/product-brief/account-protector) and enable it in your web application before using the Akamai Account Protector node.

### Configure Akamai Account Protector

Akamai Account Protector detects malicious activities and assigns risk scores to requests. To inject the akamai-user-risk header, follow these steps:

#### Enable Account Protector on the Akamai Edge

1. Log in to Akamai Control Center.

2. Navigate to Security Configuration and select your existing security policy or create a new one.

3. Enable Account Protector under Bot Management settings.

4. Ensure that risk scoring is enabled and that Akamai adds the akamai-user-risk HTTP header.

##### Add the username parameter to Akamai Account Protector

1. In the Akamai Control Center, create an API Definition to PingOne AIC's hostname.

2. Add an API Resource with the following:

   * **Name:** Authenticate

   * **Path:** `/am/json/realms/root/realms/alpha/authenticate`

3. Check the `POST` method and set the request parameters. For example:

   ![akamai acc prot set par](../_images/akamai-acc-prot-set-par.png)

4. Similarly, set the response parameters.

   > **Collapse: The sample JSON/XML Schema script used in this node.**
   >
   > ```
   > {
   >   "requestBody": {
   >     "content": {
   >       "application/json": {
   >         "schema": {
   >           "type": "object",
   >           "required": [
   >             "callbacks"
   >           ],
   >           "properties": {
   >             "callbacks": {
   >               "type": "array",
   >               "items": {
   >                 "type": "object",
   >                 "properties": {
   >                   "input": {
   >                     "type": "array",
   >                     "items": {
   >                       "type": "object",
   >                       "properties": {
   >                         "name": {
   >                           "type": "string"
   >                         }
   >                       }
   >                     }
   >                   }
   >                 }
   >               },
   >               "description": "callbacks"
   >             }
   >           }
   >         }
   >       },
   >       "application/xml": {
   >         "schema": {
   >           "type": "object",
   >           "required": [
   >             "callbacks"
   >           ],
   >           "properties": {
   >             "callbacks": {
   >               "type": "array",
   >               "items": {
   >                 "type": "object",
   >                 "properties": {
   >                   "input": {
   >                     "type": "array",
   >                     "items": {
   >                       "type": "object",
   >                       "properties": {
   >                         "name": {
   >                           "type": "array",
   >                           "items": {
   >                             "type": "string"
   >                           },
   >                           "maxItems": 1
   >                         }
   >                       }
   >                     }
   >                   }
   >                 }
   >               },
   >               "description": "callbacks"
   >             }
   >           },
   >           "xml": {
   >             "name": "root"
   >           }
   >         }
   >       }
   >     },
   >     "required": true
   >   }
   > }
   > ```

## Configuration

| Property                           | Usage                                                                                                                                                                                                 |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| High Risk Threshold                | The maximum user risk score for a high risk assessment. Scores above medium assessment and up to this value are categorized as high risk. Scores above this value are categorized as a critical risk. |
| Medium Risk Threshold              | The maximum user risk score for a medium risk assessment. Scores between the the Low Risk Threshold and this value are categorized as medium risk.                                                    |
| Low Risk Threshold                 | The maximum user risk score for a low risk assessment. Scores up to this value are categorized as low risk.                                                                                           |
| Save Akamai Header to Shared State | If selected, the node writes the Akamai-User-Risk header value to the shared state.                                                                                                                   |

## Outputs

By default, this node writes the Akamai-User-Risk HTTP request header value to the transient state. If Save Akamai Header to Shared State is selected, then the value is stored in shared state.

## Example

The following example journey illustrates the use of Akamai Account Protector node.

![Journey using Akamai Account Protector node](../_images/akamai-account-protector-journey.png)

The inner journey shown above is contained in an outer journey which performs user authentication and collects the username to the Akamai Account Protector node. The Akamai Account Protector node parses the Akamai-User-Risk HTTP request header and extracts the user risk score. Based on the risk score, the authentication journey progresses through the appropriate outcome.

---

---
title: CLEAR ID Verification node
description: Use the CLEAR ID Verification node to integrate identity verification into an Advanced Identity Cloud authentication journey
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/auth-node-clear
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/auth-node-clear.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  compatibility: Compatibility
  inputs: Inputs
  dependencies: Dependencies
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  troubleshooting: Troubleshooting
  example: Example
---

# CLEAR ID Verification node

Use the CLEAR ID Verification node to integrate [CLEAR verification](https://docs.clearme.com/docs/web-app) in your authentication journey.

## Compatibility

| Product                               | Compatible? |
| ------------------------------------- | ----------- |
| Advanced Identity Cloud               | Yes         |
| PingAM (self-managed)                 | Yes         |
| Ping Identity Platform (self-managed) | Yes         |

## Inputs

None. This node doesn't read shared state data.

## Dependencies

To use this node, you must have access to a CLEAR Verified tenant. Learn more about [setting up a CLEAR tenant](https://docs.clearme.com/docs/web-app#configure-your-first-project).

## Configuration

| Property            | Usage                                                                                                                                               |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| CLEAR API Key       | Environment API Key for CLEAR.                                                                                                                      |
| CLEAR Project ID    | Google Cloud administrator's private key.                                                                                                           |
| Key ID              | The tenant ID for the CLEAR project used for integration.                                                                                           |
| Redirect URL        | The target URL for redirection after verification.                                                                                                  |
| Use Secure Endpoint | If this toggle is enabled, the node uses the secure endpoint to retrieve user verification results; otherwise, the node uses the standard endpoint. |

## Outputs

The ID Verification results are stored in the `verificationResults` shared state attribute. An example of data is provided [here](https://docs.clearme.com/docs/web-app#endpoint-overview).

## Outcomes

* `Continue`

  Successfully authenticated the user.

* `Error`

  An error message is output to the shared state.

## Troubleshooting

If this node logged an error, review the log messages for the transaction and contact [CLEAR support](https://www.clearme.com/support) for further troubleshooting.

## Example

The example journey shows the following:

* The journey starts with user registration.

* CLEAR ID Verification node verifies the user credentials.

* The [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) is a scripted decision node extracts the document number from the CLEAR verification response stored in shared state and stores it on the user object.

![auth node clear journey](../_images/auth-node-clear-journey.png)

---

---
title: Configure a DCR onboarding flow
description: Use Dynamic Client Registration to automatically onboard OAuth 2.0 clients as AI agents in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/ai-agents-configure-dcr-onboarding-flow
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/ai-agents-configure-dcr-onboarding-flow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configure-the-oauth-2-abbr-provider-service-dcr: "Task 1: Configure the OAuth 2.0 provider service"
  task_2_create_and_register_a_dcr_script: "Task 2: Create and register a DCR script"
  register-and-configure-a-dynamic-client: "Task 3: Register and configure a dynamic client"
  get-a-dynamic-client-access-token: "Task 4: Get a dynamic client access token"
---

# Configure a DCR onboarding flow

To streamline the onboarding of OAuth 2.0 clients, Advanced Identity Cloud supports Dynamic Client Registration (DCR), which allows for the automated creation and configuration of dynamic clients without manual intervention.

In addition to the standard DCR endpoint (`/register`), Advanced Identity Cloud provides an AI agent-specific DCR endpoint (`/aiagent/register`) for onboarding AI agents as dynamic clients, enabling your AI-driven solutions to programmatically register and obtain credentials for secure access to applications on behalf of end users.

What is Dynamic Client Registration (DCR)?

Dynamic Client Registration (DCR) is an OAuth 2.0 extension that allows *dynamic clients* to be programmatically registered with an authorization server at runtime without manual administrative intervention. Instead of a static setup, dynamic clients send their own metadata (including names and authorized redirect URLs) directly to a dedicated registration endpoint to obtain unique credentials. This process is essential for scaling high-velocity environments where numerous individual client instances require distinct identities for secure tracking and lifecycle management.

DCR is a key component of Model Context Protocol (MCP) authorization, where MCP clients such as AI assistants and IDEs need to interact securely with MCP servers that host data and tools. DCR allows these MCP clients to be dynamically onboarded with appropriate access permissions and security settings, enabling seamless and secure interactions in AI-driven solutions.

## Task 1: Configure the OAuth 2.0 provider service

Configure the OAuth 2.0 provider service to support the grant types needed for the DCR onboarding flow:

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Services.

2. Click the OAuth2 Provider service, then click the Advanced tab:

   1. In the Grant Types field, select the Client Credentials grant type, if it isn't already selected.

   2. In the Client Registration Scope Allowlist field, select the scopes that AI-driven solutions can request when they use the DCR onboarding flow to onboard AI agents.

3. Click the Client Dynamic Registration tab:

   * Select the Allow Open Dynamic Client Registration checkbox, if it isn't already selected.

4. Click Save Changes.

## Task 2: Create and register a DCR script

Create a DCR script to configure the settings for AI agents onboarded as dynamic clients.

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Scripts.

2. Click [icon: add, set=material, size=inline] New Script.

3. In the New Script page:

   1. Enter a Name for the script, such as `AI Agent Dynamic Client Registration Script`.

   2. In the Script Type drop-down list, select `OAuth2 Dynamic Client Registration`.

   3. Click Create.

4. In the script editor:

   1. (Optional) Enter a Description for the script, such as `Script to configure AI agent access settings during dynamic client registration`.

   2. In the Script field, enter the following script:

      ```javascript
      if (operation === "CREATE" && clientIdentity.isAIAgent()) {
        clientIdentity.setAttribute("providerOverridesEnabled", ["true"]); (1)
        clientIdentity.setAttribute("statelessTokensEnabled", ["true"]); (2)
        clientIdentity.setAttribute("acceptAudienceParametersInTokenExchangeRequests", ["true"]); (3)

        clientIdentity.setAttribute("AgentType", clientIdentity.getAttributeValues("AgentType")); (4)
        clientIdentity.setAttribute("aiAgentIdentityUid", clientIdentity.getAttributeValues("aiAgentIdentityUid")); (4)

        clientIdentity.store(); (5)
      }
      ```

      |       |                                                                                                                                                                                                                                                                                                                                       |
      | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | **1** | `providerOverridesEnabled` is required to enable client-specific customization for the dynamic client's OAuth 2.0 settings.                                                                                                                                                                                                           |
      | **2** | `statelessTokensEnabled` is required to enable stateless token issuance for the dynamic client. This allows the AI-agent dynamic client to receive self-contained tokens that don't require Advanced Identity Cloud to look up token metadata in the database for each validation, which is ideal for high-scale AI-driven solutions. |
      | **3** | `acceptAudienceParametersInTokenExchangeRequests` is required to allow the AI-agent dynamic client to specify audience values in token exchange requests, which is important for ensuring that the access tokens it obtains are properly scoped for the intended target applications.                                                 |
      | **4** | The script also copies the `AgentType` and `aiAgentIdentityUid` attributes back to the client. This is a required step for dynamic clients created via the `/aiagent/register` endpoint.                                                                                                                                              |
      | **5** | `clientIdentity.store()` saves the changes made to the client's attributes.                                                                                                                                                                                                                                                           |

   3. Click Save Changes.

5. Go to Native Consoles > Access Management > Services > OAuth2 Provider.

6. Click the Client Dynamic Registration tab, then in the Dynamic Client Registration Script drop-down list, select the DCR script you just created.

7. Click Save Changes.

## Task 3: Register and configure a dynamic client

1. Use the AI agent-specific DCR endpoint (`/aiagent/register`) to register a dynamic client.

   |   |                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `/aiagent/register` endpoint doesn't support setting the client ID in the request payload. The `client_id` is automatically generated by Advanced Identity Cloud for AI agents registered as dynamic clients. |

   ```shell
   $ curl \
   --request POST 'https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/<realm>/aiagent/register' \(1)(2)
   --header 'Content-Type: application/json' \
   --data '{(3)
       "grant_types": ["client_credentials"],
       "response_types": ["token"],
       "redirect_uris": <dynamic-client-redirect-uris>,(4)
       "scopes": <dynamic-client-scopes>,(5)
       "client_name": <dynamic-client-name>,(6)
       "token_endpoint_auth_method": "client_secret_post"(7)
   }'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                                                                                                                                                                                       |
   > | **2** | Replace \<realm> with either `alpha` or `bravo`.                                                                                                                                                                                                                                                                                                                                                                                           |
   > | **3** | The JSON payload contains the metadata needed to onboard a dynamic client.                                                                                                                                                                                                                                                                                                                                                                 |
   > | **4** | Replace \<dynamic-client-redirect-uris> with a JSON array of one or more absolute URLs for the dynamic client you want to onboard. For example, `["https://example.com/callback"]`. The URLs you set in `redirect_uris` act as a secure allowlist, identifying the only authorized endpoints where the authorization server can send sensitive response data, such as authorization codes or tokens, upon successful end user interaction. |
   > | **5** | Replace \<dynamic-client-scopes> with a JSON array of one or more scopes that the dynamic client can request. For example, `["data-read", "data-write"]`.                                                                                                                                                                                                                                                                                  |
   > | **6** | Replace \<dynamic-client-name> with a human-readable name for the dynamic client you want to onboard. For example, `Retail Chatbot` or `Workforce Assistant`. This name is used to identify the dynamic client to end users on consent screens and to tenant administrators within the Advanced Identity Cloud admin console.                                                                                                              |
   > | **7** | The `token_endpoint_auth_method` parameter defines how the dynamic client authenticates when requesting an access token. By setting this to `client_secret_post`, the client identifies as a confidential client that will provide its `client_id` and `client_secret` directly within the HTTP POST request body.                                                                                                                         |

   ```json
   {
       ...
       "providerOverridesEnabled": true,
       ...
       "client_id": "ab9da93d-e9ad-40ca-ba43-3be6eb63af3c", (1)
       ...
       "client_secret": "zhYjm03cS9…​ayPVIwZsgQ", (1)
       ...
       "grant_types": [
           "client_credentials"
       ],
       ...
       "redirect_uris": [
           "https://example.com/callback"
       ],
       ...
       "scopes": [
           "data-read",
           "data-write"
       ],
       ...
       "response_types": [
           "token"
       ]
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                                                                                                                                                                       |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Note the `client_id` and `client_secret` values. These are the credentials for the dynamic client you just onboarded. You'll use these credentials in the next task to authenticate the dynamic client and obtain access tokens for it to access applications on behalf of end users. |

2. (Optional) Configure an application policy for the dynamic client. Learn more in [Create AI agent application policies](ai-agents-ui.html#create-ai-agent-application-policies).

## Task 4: Get a dynamic client access token

1. Get an access token for the dynamic client using the Client Credentials grant type:

   ```shell
   $ curl \
   --request POST 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token' \(1)
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'grant_type=client_credentials' \(2)
   --data-urlencode 'client_id=<dynamic-client-client-id>' \(3)
   --data-urlencode 'client_secret=<dynamic-client-client-secret>' \(4)
   --data-urlencode 'scope=<dynamic-client-scopes>'(5)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                             |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                        |
   > | **2** | The `grant_type` for this request is `client_credentials`, which represents the Client Credentials grant type.                                              |
   > | **3** | Replace \<dynamic-client-client-id> with the client ID of the dynamic client you registered in task 3. For example, `ab9da93d-e9ad-40ca-ba43-3be6eb63af3c`. |
   > | **4** | Replace \<dynamic-client-client-secret> with the client secret of the dynamic client.                                                                       |
   > | **5** | Replace \<dynamic-client-scopes> with some or all of the scopes you assigned to the dynamic client. For example, `data-read`.                               |

   ```json
   {
       "access_token": "eyJ0eXAiOi...l2Yz6xCHHu0", (1)
       "scope": "data-read",
       "token_type": "Bearer",
       "expires_in": 3599
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                |
   > | ----- | ------------------------------------------------------------------------------ |
   > | **1** | The `access_token` value in the response is the dynamic client's access token. |

2. Introspect the dynamic client's access token to verify the claims contain expected values:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/tokeninfo' \(1)
   --data-urlencode 'access_token=<dynamic-client-access-token>'(2)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                            |
   > | ----- | ---------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                       |
   > | **2** | Replace \<dynamic-client-access-token> with the dynamic client's access token from the response in step 2. |

   ```json
   {
       "sub": "ab9da93d-e9ad-40ca-ba43-3be6eb63af3ca", (1)
       "cts": "OAUTH2_STATELESS_GRANT",
       "auditTrackingId": "a910ad63-6b82-48d9-935c-52e962266243-289468",
       "subname": "ab9da93d-e9ad-40ca-ba43-3be6eb63af3c",
       "iss": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha",
       "tokenName": "access_token",
       "token_type": "Bearer",
       "data-read": "",
       "authGrantId": "Br5_jYrhYK...iohBrU2hs4",
       "client_id": "ab9da93d-e9ad-40ca-ba43-3be6eb63af3c",
       "access_token": "eyJ0eXAiOi...4Pmh8fD2c4",
       "aud": "ab9da93d-e9ad-40ca-ba43-3be6eb63af3c", (2)
       "nbf": 1778768831,
       "grant_type": "client_credentials",
       "scope": [
           "data-read" (3)
       ],
       :...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                                                                |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | The `sub` claim represents the subject of the token, which in this case is the dynamic client itself, identified by its client ID.                                             |
   > | **2** | The `aud` claim represents the audience of the token, which in this case is the client ID of the dynamic client, indicating that the token is intended for use by that client. |
   > | **3** | The `scope` claim contains the scopes that the dynamic client can access.                                                                                                      |

---

---
title: "Configure an \"on behalf of\" authentication flow for AI agents"
description: Configure an OAuth 2.0 token-exchange flow so an AI agent can act on behalf of an end user in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/ai-agents-configure-on-behalf-of-authentication-flow
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/ai-agents-configure-on-behalf-of-authentication-flow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configure-the-oauth-2-abbr-provider-service: "Task 1: Configure the OAuth 2.0 provider service"
  create-and-configure-a-custom-oauth2-application: "Task 2: Create and configure a custom OAuth 2.0 application"
  create-a-custom-oauth2-application: "Task 2.1: Create a custom OAuth 2.0 application"
  configure-a-custom-oauth2-application: "Task 2.2: Configure a custom OAuth 2.0 application"
  create-and-configure-an-ai-agent: "Task 3: Create and configure an AI agent"
  create-an-ai-agent: "Task 3.1: Create an AI agent"
  configure-an-ai-agent: "Task 3.2: Configure an AI agent"
  test-the-authentication-flow: "Task 4: Test the authentication flow"
  get-an-end-user-access-token: "Task 4.1: Get an end user access token"
  get-an-ai-agent-access-token: "Task 4.2: Get an AI agent access token"
---

# Configure an "on behalf of" authentication flow for AI agents

The "on behalf of" flow allows an AI agent to perform actions on behalf of an end user, which is useful for securing the actions of digital assistants.

The following instructions use an example scenario of a digital assistant AI agent that performs actions on behalf of end users in a web application. The AI agent needs to access to the web application to perform actions such as retrieving data, creating or updating records, and performing administrative tasks.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For ease of understanding, this example uses a simple [Resource owner password credentials grant](../../am-oauth2/oauth2-ropc-grant.html) (ROPC) to obtain an access token for the end user, which is then exchanged for a new access token that represents the AI agent acting on behalf of the end user. In production environments, use a more secure flow, such as the [Authorization code grant](../../am-oauth2/oauth2-authz-grant.html). |

## Task 1: Configure the OAuth 2.0 provider service

Configure the OAuth 2.0 provider service to support the grant types needed for the "on behalf of" authentication flow:

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Services.

2. Click the OAuth2 Provider service, then click the Advanced tab:

   * In the Grant Types field, select the Resource Owner Password Credentials and Token Exchange grant types, if they aren't already selected.

3. Click Save Changes.

## Task 2: Create and configure a custom OAuth 2.0 application

Create and configure a custom OAuth 2.0 application with a confidential client type to act as a resource that the AI agent can access on behalf of end users.

### Task 2.1: Create a custom OAuth 2.0 application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, then click [icon: add, set=material, size=inline] Custom Application.

2. In the Add a Custom Application modal:

   1. Click OIDC - OpenId Connect, then click Next.

   2. Click Web, then click Next.

3. In the Application Details modal:

   1. Enter a name for the application. For example, `Digital Assistant Web App`.

   2. Select one or more application Owners.

   3. Click Next.

4. In the Web Settings modal:

   1. Enter a Client ID for the application using only alphanumeric characters, dashes, or underscores. For example, `digital-assistant-web-app`.

   2. Enter a Client Secret and make a note of it, as you won't be able to view it again after creating the application.

   3. Click Create Application.

5. Follow the instructions in [Configure a custom OAuth 2.0 application](#configure-a-custom-oauth2-application) to configure the application you created.

### Task 2.2: Configure a custom OAuth 2.0 application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications.

2. Review the Applications page to find the application you want to configure, then click it.

3. Click the Sign On tab to configure the application's OAuth 2.0 client:

   1. In the Grant Types field, select Resource Owner Password Credentials to add it to the existing grant types.

   2. In the Scopes field, enter the scopes that the application needs to access resources. For example, `openid`, `read-data`, `write-data`, and `admin-action`.

   3. Click Show Advanced Settings to display a vertical tab menu, then click the Authentication vertical tab.

   4. In the Token Endpoint Authentication Method field, select `client_secret_post`.

   5. Click Save.

## Task 3: Create and configure an AI agent

Create and configure an AI agent that can access the custom OAuth 2.0 application on behalf of end users using the token exchange grant type.

### Task 3.1: Create an AI agent

1. Follow the instructions in [Create an AI agent](ai-agents-ui.html#create-an-ai-agent). An example name for the AI agent is `Digital Assistant AI Agent`, and an example client ID is `digital-assistant-ai-agent`.

2. Follow the instructions in [Configure an AI agent](#configure-an-ai-agent) to configure the AI agent you created.

### Task 3.2: Configure an AI agent

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the AI agent you want to configure, then click it.

3. Click the Access tab to configure the agent's OAuth 2.0 client:

   1. Click Show Advanced Settings to display a vertical tab menu.

   2. Click the Advanced vertical tab:

      1. In the Grant Types field, enter `urn:ietf:params:oauth:grant-type:token-exchange`.

      2. In the Token Endpoint Authentication Method field, select `client_secret_post`.

   3. Click the OAuth Provider Overrides tab:

      1. Select the Enable OAuth2 Provider Overrides checkbox.

      2. Select the Use Client-Side Access & Refresh Tokens checkbox.

      3. Select the Accept Audience Parameters in Token Exchange Requests checkbox.

4. Click the Applications tab:

   1. Click [icon: add, set=material, size=inline] Add Application.

   2. In the Resource field, select the custom OAuth 2.0 application you created in the previous task.

   3. Click Save.

   4. In the Subjects field, select users that the AI agent will act on behalf of or in the Subject Groups field, select groups of users that the AI agent will act on behalf of.

   5. In the Permissions field, choose one of the following approaches:

      * To limit the scopes the AI agent can request, select specific scopes. For example, `read-data`. This approach is recommended for "on behalf of" operations where the AI agent only needs access to a limited set of permissions.

      * To allow the AI agent to request any or all of the scopes that are assigned to the custom OAuth 2.0 application, select all scopes in this field or leave it empty. This approach might be suitable for "human-in-the-loop" workflows, where end users are required to explicitly approve high-risk or sensitive operations.

      You can also enter custom scope values that aren't in the drop-down list by typing them into the field.

   6. Click Save.

## Task 4: Test the authentication flow

Run a series of commands to get an access token for an end user and then exchange it for a new access token that represents an AI agent acting on behalf of the end user.

### Task 4.1: Get an end user access token

1. [Create a user account](../../identities/manage-identities.html#create_a_user_profile) for the end user that the AI agent will act on behalf of, if one doesn't already exist.

2. Get an access token for the end user using the Resource Owner Password Credentials grant type:

   ```shell
   $ curl \
   --request POST 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token' \(1)
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'grant_type=password' \(2)
   --data-urlencode 'username=<end-user-username>' \(3)
   --data-urlencode 'password=<end-user-password>' \(4)
   --data-urlencode 'client_id=<oauth2-app-client-id>' \(5)
   --data-urlencode 'client_secret=<oauth2-app-client-secret>' \(6)
   --data-urlencode 'scope=<application-scopes>'(7)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                         |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                    |
   > | **2** | The `grant_type` for this request is `password`, which represents the Resource Owner Password Credentials grant type.                                   |
   > | **3** | Replace \<end-user-username> with the username of the end user that the AI agent will act on behalf of. For example, `barbara.jensen`.                  |
   > | **4** | Replace \<end-user-password> with the password of the end user.                                                                                         |
   > | **5** | Replace \<oauth2-app-client-id> with the client ID of the custom OAuth 2.0 application you created in task 2. For example, `digital-assistant-web-app`. |
   > | **6** | Replace \<oauth2-app-client-secret> with the client secret of the custom OAuth 2.0 application.                                                         |
   > | **7** | Replace \<application-scopes> with some or all of the scopes you assigned to the custom OAuth 2.0 application. For example, `openid`.                   |

   ```json
   {
       "access_token": "eyJ0eXAiOi...nbCv_gODEw", (1)
       "refresh_token": "eyJ0eXAiOi...1HXGCc8z0s",
       "scope": "openid",
       "token_type": "Bearer",
       "expires_in": 3599
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                          |
   > | ----- | ------------------------------------------------------------------------ |
   > | **1** | The `access_token` value in the response is the end user's access token. |

3. Introspect the end user's access token to verify the claims contain expected values:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/tokeninfo' \(1)
   --data-urlencode 'access_token=<end-user-access-token>'(2)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                |
   > | ----- | ---------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                           |
   > | **2** | Replace \<end-user-access-token> with the end-user's access token from the response in step 2. |

   ```json
   {
       "sub": "2199ef22-7927-4ecf-8345-ee58df8f6328", (1)
       "cts": "OAUTH2_STATELESS_GRANT",
       "auth_level": 0,
       "auditTrackingId": "c6e32020-37ea-4e5c-af49-e66d81f13edd-179589",
       "openid": "",
       "subname": "2199ef22-7927-4ecf-8345-ee58df8f6328",
       "iss": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha",
       "tokenName": "access_token",
       "token_type": "Bearer",
       "authGrantId": "VWbXE2oH-5...3A1NQXnaVI",
       "client_id": "digital-assistant-web-app",
       "access_token": "eyJ0eXAiOi...nbCv_gODEw",
       "aud": "digital-assistant-web-app",  (2)
       "nbf": 1778083229,
       "grant_type": "password",
       "scope": [
           "openid"  (3)
       ],
       ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                                                 |
   > | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `sub` claim contains the end user's UUID, which indicates that the token represents the end user.                                                           |
   > | **2** | The `aud` claim contains the client ID of the custom OAuth 2.0 application, which indicates that the intended audience of this access token is the application. |
   > | **3** | The `scope` claim contains the application scopes that the end user can access.                                                                                 |

### Task 4.2: Get an AI agent access token

1. Use the Token Exchange grant type to exchange the end user's access token for a new AI agent access token that the AI agent can use to access the custom OAuth 2.0 application on behalf of the end user:

   ```shell
   $ curl \
   --request POST 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token' \(1)
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \(2)
   --data-urlencode 'subject_token=<end-user-access-token>' \(3)
   --data-urlencode 'subject_token_type=urn:ietf:params:oauth:token-type:access_token' \
   --data-urlencode 'client_id=<ai-agent-client-id>' \(4)
   --data-urlencode 'client_secret=<ai-agent-client-secret>' \(5)
   --data-urlencode 'audience=<oauth2-app-client-id>' \(6)
   --data-urlencode 'scope=<ai-agent-scopes>'(7)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                                                                                                                                            |
   > | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                       |
   > | **2** | The `grant_type` for this request is `urn:ietf:params:oauth:grant-type:token-exchange`, which represents the Token Exchange grant type.                                                                                                                                    |
   > | **3** | Replace \<end-user-access-token> with the end user's access token.                                                                                                                                                                                                         |
   > | **4** | Replace \<ai-agent-client-id> with the client ID of the AI agent you created in task 3. For example, `digital-assistant-ai-agent`.                                                                                                                                         |
   > | **5** | Replace \<ai-agent-client-secret> with the client secret of the AI agent.                                                                                                                                                                                                  |
   > | **6** | Replace \<oauth2-app-client-id> with the client ID of the custom OAuth 2.0 application. For example, `digital-assistant-web-app`. Setting this as the `audience` indicates that the AI agent intends to access the custom OAuth 2.0 application on behalf of the end user. |
   > | **7** | Replace \<ai-agent-scopes> with some or all of the scopes that you assigned to the AI agent in task 3.2, step 5e. For example, `read-data`.                                                                                                                                |

   ```json
   {
       "access_token": "eyJ0eXAiOi...7-SnU_UoYg", (1)
       "refresh_token": null,
       "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
       "scope": "read-data",
       "token_type": "Bearer",
       "expires_in": 3599
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                               |
   > | ----- | --------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `access_token` value in the response is can be used by the AI agent to access the custom OAuth 2.0 application on behalf of the end user. |

2. Introspect the AI agent's access token to verify the claims contain expected values:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/tokeninfo' \(1)
   --data-urlencode 'access_token=<ai-agent-access-token>'(2)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                |
   > | ----- | ---------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                           |
   > | **2** | Replace \<ai-agent-access-token> with the ai-agent's access token from the response in step 1. |

   ```json
   {
       "sub": "2199ef22-7927-4ecf-8345-ee58df8f6328", (1)
       "cts": "OAUTH2_STATELESS_GRANT",
       "auth_level": 0,
       "auditTrackingId": "c6e32020-37ea-4e5c-af49-e66d81f13edd-179625",
       "subname": "2199ef22-7927-4ecf-8345-ee58df8f6328",
       "iss": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha",
       "tokenName": "access_token",
       "token_type": "Bearer",
       "authGrantId": "EUoCJS8Fs0...JXD3fbH5o",
       "client_id": "digital-assistant-ai-agent",
       "access_token": "eyJ0eXAiOi...7-SnU_UoYg",
       "aud": [
           "digital-assistant-ai-agent", (2)
           "digital-assistant-web-app" (2)
       ],
       "nbf": 1778083245,
       "act": {
           "sub": "digital-assistant-ai-agent" (3)
       },
       "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
       "scope": [
           "read-data" (4)
       ],
       "auth_time": 1778083229,
       ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                                                                                     |
   > | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `sub` claim contains the end user's UUID, which indicates that the token represents the end user.                                                                                               |
   > | **2** | The `aud` claim contains the client ID of the AI agent and the custom OAuth 2.0 application, which indicates that the intended audience of this access token is both the agent and the application. |
   > | **3** | The `act` claim contains a `sub` claim with the AI agent's client ID, which indicates that the AI agent is acting on behalf of the end user.                                                        |
   > | **4** | The `scope` claim contains the scopes that the AI agent can access.                                                                                                                                 |

---

---
title: Configure an autonomous AI agent flow
description: The autonomous AI agent flow lets an AI agent act independently, without requiring an end user to be present. The agent obtains its own access token using the Client Credentials grant type and then exchanges it for a scoped token that it can use to access a specific application. This is useful for automated pipelines, background tasks, and other scenarios where an AI agent acts on its own behalf rather than on behalf of an end user.
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/ai-agents-configure-autonomous-agent-flow
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/ai-agents-configure-autonomous-agent-flow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  configure-the-oauth-2-abbr-provider-service: "Task 1: Configure the OAuth 2.0 provider service"
  create-and-configure-a-custom-oauth2-application: "Task 2: Create and configure a custom OAuth 2.0 application"
  create-a-custom-oauth2-application: "Task 2.1: Create a custom OAuth 2.0 application"
  configure-a-custom-oauth2-application: "Task 2.2: Configure a custom OAuth 2.0 application"
  create-and-configure-an-ai-agent: "Task 3: Create and configure an AI agent"
  create-an-ai-agent: "Task 3.1: Create an AI agent"
  configure-an-ai-agent: "Task 3.2: Configure an AI agent"
  test-the-authentication-flow: "Task 4: Test the authentication flow"
  get-an-ai-agent-access-token: "Task 4.1: Get an AI agent access token"
  exchange-agent-token-for-application-access: "Task 4.2: Exchange the AI agent token for application access"
---

# Configure an autonomous AI agent flow

The autonomous AI agent flow lets an AI agent act independently, without requiring an end user to be present. The agent obtains its own access token using the Client Credentials grant type and then exchanges it for a scoped token that it can use to access a specific application. This is useful for automated pipelines, background tasks, and other scenarios where an AI agent acts on its own behalf rather than on behalf of an end user.

The following instructions use an example scenario of an AI agent that analyzes a web server's access logs for bot traffic. The AI agent needs to access the web server's logs API autonomously, to read and search the logs for indicators of bot traffic.

## Task 1: Configure the OAuth 2.0 provider service

Configure the OAuth 2.0 provider service to support the grant types needed for the autonomous agent flow:

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Services.

2. Click the OAuth2 Provider service, then click the Advanced tab:

   * In the Grant Types field, select the Client Credentials and Token Exchange grant types, if they aren't already selected.

3. Click Save Changes.

## Task 2: Create and configure a custom OAuth 2.0 application

Create and configure a custom OAuth 2.0 application with a confidential client type to act as a resource that the AI agent can access autonomously.

### Task 2.1: Create a custom OAuth 2.0 application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, then click [icon: add, set=material, size=inline] Custom Application.

2. In the Add a Custom Application modal:

   1. Click OIDC - OpenId Connect, then click Next.

   2. Click Service, then click Next.

3. In the Application Details modal:

   1. Enter a name for the application. For example, `Web Server Logs API App`.

   2. Select one or more application Owners.

   3. Click Next.

4. In the Service Settings modal:

   1. Enter a Client ID for the application using only alphanumeric characters, dashes, or underscores. For example, `web-server-logs-api-app`.

   2. Enter a Client Secret and make a note of it, as you won't be able to view it again after creating the application.

   3. Click Create Application.

5. Follow the instructions in [Configure a custom OAuth 2.0 application](#configure-a-custom-oauth2-application) to configure the application you created.

### Task 2.2: Configure a custom OAuth 2.0 application

1. In the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications.

2. Review the Applications page to find the application you want to configure, then click it.

3. Click the Sign On tab to configure the application's OAuth 2.0 client:

   1. In the Scopes field, enter the scopes that the application needs to access resources. For example, `logs-read` and `logs-search`.

   2. Click Save.

## Task 3: Create and configure an AI agent

Create and configure an AI agent that can autonomously access the custom OAuth 2.0 application.

### Task 3.1: Create an AI agent

1. Follow the instructions in [Create an AI agent](ai-agents-ui.html#create-an-ai-agent). An example name for the AI agent is `Bot Traffic Analyzer Agent`, and an example client ID is `bot-traffic-analyzer-agent`.

2. Follow the instructions in [Configure an AI agent](#configure-an-ai-agent) to configure the AI agent you created.

### Task 3.2: Configure an AI agent

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the AI agent you want to configure, then click it.

3. Click the Access tab to configure the agent's OAuth 2.0 client:

   1. Click Show Advanced Settings to display a vertical tab menu. The Core vertical tab is selected by default.

   2. In the Scopes field, enter the scopes the agent needs for basic operations. For example, `monitor-system`.

   3. Click the Advanced vertical tab:

      1. In the Grant Types field, enter `urn:ietf:params:oauth:grant-type:token-exchange` and `client_credentials`.

      2. In the Token Endpoint Authentication Method field, select `client_secret_post`.

   4. Click the OAuth Provider Overrides vertical tab:

      1. Select the Enable OAuth2 Provider Overrides checkbox.

      2. Select the Use Client-Side Access & Refresh Tokens checkbox.

      3. Select the Accept Audience Parameters in Token Exchange Requests checkbox.

4. Click the Applications tab:

   1. Click [icon: add, set=material, size=inline] Add Application.

   2. In the Resource field, select the custom OAuth 2.0 application you created in the previous task.

   3. Click Save.

   4. Leave the Subjects and Subject Groups fields empty, because the AI agent acts autonomously rather than on behalf of a specific user.

   5. In the Permissions field, choose one of the following approaches:

      * To limit the scopes the AI agent can request, select specific scopes. For example, `logs-read` and `logs-search`. This approach is recommended when you want to apply least privilege to the agent's access.

      * To allow the AI agent to request any or all of the scopes assigned to the custom OAuth 2.0 application, select all scopes or leave the field empty.

   6. Click Save.

## Task 4: Test the authentication flow

Run a series of commands to get an access token for the AI agent and then exchange it for a scoped token the agent can use to access the custom OAuth 2.0 application autonomously.

### Task 4.1: Get an AI agent access token

1. Get an access token for the AI agent using the Client Credentials grant type:

   ```shell
   $ curl \
   --request POST 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token' \(1)
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'grant_type=client_credentials' \(2)
   --data-urlencode 'client_id=<ai-agent-client-id>' \(3)
   --data-urlencode 'client_secret=<ai-agent-client-secret>' \(4)
   --data-urlencode 'scope=<ai-agent-scopes>'(5)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                    |
   > | ----- | ---------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                               |
   > | **2** | The `grant_type` for this request is `client_credentials`, which represents the Client Credentials grant type.                     |
   > | **3** | Replace \<ai-agent-client-id> with the client ID of the AI agent you created in task 3. For example, `bot-traffic-analyzer-agent`. |
   > | **4** | Replace \<ai-agent-client-secret> with the client secret of the AI agent.                                                          |
   > | **5** | Replace \<ai-agent-scopes> with one or more of the scopes you assigned to the AI agent. For example, `monitor-system`.             |

   ```json
   {
       "access_token": "eyJ0eXAiOi...jARmOdTatY", (1)
       "scope": "monitor-system",
       "token_type": "Bearer",
       "expires_in": 3599
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                          |
   > | ----- | ------------------------------------------------------------------------ |
   > | **1** | The `access_token` value in the response is the AI agent's access token. |

2. Introspect the AI agent's access token to verify the claims contain the expected values:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/tokeninfo' \(1)
   --data-urlencode 'access_token=<ai-agent-access-token>'(2)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                |
   > | ----- | ---------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                           |
   > | **2** | Replace \<ai-agent-access-token> with the AI agent's access token from the response in step 1. |

   ```json
   {
       "sub": "bot-traffic-analyzer", (1)
       "cts": "OAUTH2_STATELESS_GRANT",
       "auditTrackingId": "a910ad63-6b82-48d9-935c-52e962266243-276314",
       "subname": "bot-traffic-analyzer",
       "iss": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha",
       "tokenName": "access_token",
       "token_type": "Bearer",
       "authGrantId": "C3ca_i8hU6...ODXFTX-cEc",
       "client_id": "bot-traffic-analyzer",
       "access_token": "eyJ0eXAiOi...jARmOdTatY",
       "aud": "bot-traffic-analyzer", (2)
       "nbf": 1778764699,
       "grant_type": "client_credentials",
       "scope": [
           "monitor-system" (3)
       ],
       ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                  |
   > | ----- | -------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `sub` claim contains the AI agent's client ID, which indicates that the token represents the agent.                          |
   > | **2** | The `aud` claim contains the AI agent's client ID, which indicates that the intended audience of this access token is the agent. |
   > | **3** | The `scope` claim contains the scopes that the AI agent can access.                                                              |

### Task 4.2: Exchange the AI agent token for application access

1. Use the Token Exchange grant type to exchange the AI agent's access token for a new token scoped to the custom OAuth 2.0 application:

   ```shell
   $ curl \
   --request POST 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/access_token' \(1)
   --header 'Content-Type: application/x-www-form-urlencoded' \
   --data-urlencode 'grant_type=urn:ietf:params:oauth:grant-type:token-exchange' \(2)
   --data-urlencode 'subject_token=<ai-agent-access-token>' \(3)
   --data-urlencode 'subject_token_type=urn:ietf:params:oauth:token-type:access_token' \
   --data-urlencode 'client_id=<ai-agent-client-id>' \(4)
   --data-urlencode 'client_secret=<ai-agent-client-secret>' \(5)
   --data-urlencode 'audience=<oauth2-app-client-id>' \(6)
   --data-urlencode 'scope=<exchanged-scopes>'(7)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                                                                                                                                                  |
   > | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                             |
   > | **2** | The `grant_type` for this request is `urn:ietf:params:oauth:grant-type:token-exchange`, which represents the Token Exchange grant type.                                                                                                                                          |
   > | **3** | Replace \<ai-agent-access-token> with the AI agent's access token from task 4.1.                                                                                                                                                                                                 |
   > | **4** | Replace \<ai-agent-client-id> with the client ID of the AI agent. For example, `bot-traffic-analyzer-agent`.                                                                                                                                                                     |
   > | **5** | Replace \<ai-agent-client-secret> with the client secret of the AI agent.                                                                                                                                                                                                        |
   > | **6** | Replace \<oauth2-app-client-id> with the client ID of the custom OAuth 2.0 application. For example, `web-server-logs-api-app`. Setting this as the `audience` indicates that the AI agent intends to use the exchanged access token to access the custom OAuth 2.0 application. |
   > | **7** | Replace \<exchanged-scopes> with the scopes that the AI agent needs to access the application. For example, `logs-read logs-search`.                                                                                                                                             |

   ```json
   {
       "access_token": "eyJ0eXAiOi...83ZuC6fSnw", (1)
       "refresh_token": null,
       "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
       "scope": "logs-read logs-search",
       "token_type": "Bearer",
       "expires_in": 3599
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                                 |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `access_token` value in the response is the scoped token that the AI agent can use to access the custom OAuth 2.0 application autonomously. |

2. Introspect the exchanged token to verify the claims contain expected values:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/tokeninfo' \(1)
   --data-urlencode 'access_token=<exchanged-access-token>'(2)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                |
   > | ----- | ---------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                           |
   > | **2** | Replace \<exchanged-access-token> with the exchanged access token from the response in step 1. |

   ```json
   {
       "sub": "bot-traffic-analyzer", (1)
       "cts": "OAUTH2_STATELESS_GRANT",
       "auditTrackingId": "a910ad63-6b82-48d9-935c-52e962266243-285038",
       "subname": "bot-traffic-analyzer",
       "iss": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha",
       "tokenName": "access_token",
       "token_type": "Bearer",
       "authGrantId": "wnqUfLhio1...i38m44oycg",
       "client_id": "bot-traffic-analyzer",
       "access_token": "eyJ0eXAiOi...83ZuC6fSnw",
       "aud": [
           "bot-traffic-analyzer", (2)
           "access-log-api" (2)
       ],
       "nbf": 1778767385,
       "act": {
           "sub": "bot-traffic-analyzer" (3)
       },
       "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
       "scope": [
           "logs-search", (4)
           "logs-read" (4)
       ],
       ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                                                                                                          |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | The `sub` claim contains the AI agent's client ID, which indicates that the token represents the agent acting autonomously.                                                                                              |
   > | **2** | The `aud` claim contains the client ID of the AI agent and the custom OAuth 2.0 application, which indicates that the intended audience of this access token is both the agent and the application.                      |
   > | **3** | The `act` claim also contains the AI agent's client ID. In an autonomous flow, both `sub` and `act` are the agent's identity, in contrast to the "on behalf of" flow where `sub` is the end user and `act` is the agent. |
   > | **4** | The `scope` claim contains the scopes that the AI agent can access on the application.                                                                                                                                   |

---

---
title: Enable the AI agents feature
description: Enable the AI agents feature for Advanced Identity Cloud sandbox tenants created before March 2026 using the environment API
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/ai-agents-enable
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/ai-agents-enable.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Enable the AI agents feature

The AI agents feature is enabled by default for sandbox tenants created on or after March 31, 2026. For sandbox tenants created before that date, you can enable the AI agents feature using the following steps:

1. Check if the feature is already enabled by looking for the [icon: smart_toy, set=material, size=inline] AI Agents menu item in the left navigation menu of either realm in the Advanced Identity Cloud admin console. If the menu item is displayed, you can skip the rest of the steps.

2. Check that your sandbox tenant supports application management using the [Application management migration FAQ](../../product-information/migration-dependent-features/application-management-migration-faq.html). If your tenant doesn't support application management, contact your Ping Identity representative.

3. Check that your sandbox tenant has groups enabled using the [Group identity migration FAQ](../../product-information/migration-dependent-features/group-identity-migration-faq.html). If your tenant doesn't have groups enabled, follow the feature enablement instructions in [Group management](../../idm-objects/groups.html).

4. Enable the AI agents feature:

   1. [Get an access token](../../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with the `fr:am:*` and `fr:idm:*` scopes.

   2. Make a POST request to the `/environment/aiagent?_action=enable` endpoint to enable the feature:

      ```shell
      $ curl \
      --request POST 'https://<tenant-env-fqdn>/environment/aiagent?_action=enable' \(1)
      --header 'Authorization: Bearer <access-token>'(2)
      ```

      |       |                                                                      |
      | ----- | -------------------------------------------------------------------- |
      | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
      | **2** | Replace \<access-token> with the access token created in step 1.     |

   3. Examine the HTTP status code of the response:

      * If the response has a `200` HTTP status code, the enablement request was successful.

        It can take up to 10 minutes for the AI agents feature to be fully enabled and accessible in the Advanced Identity Cloud admin console. Every few minutes, reload the Advanced Identity Cloud admin console in your browser, then verify if the AI agents feature is enabled by checking for the [icon: smart_toy, set=material, size=inline] AI Agents menu item in the left navigation menu of either realm.

      * If the response has a `500` HTTP status code, the enablement request failed:

        1. Double-check that your tenant environment meets the prerequisites in steps 2 and 3, and if necessary, repeat step 4 to try enabling the feature again.

        2. If you still can't access the feature, open a support case with Ping Identity support:

           > **Collapse: Show support guidance**
           >
           > 1. Go to <https://support.pingidentity.com>.
           >
           > 2. Click Create a case.
           >
           > 3. Follow the steps in the case submission wizard by selecting your account and contract and answering questions about your tenant environments.
           >
           > 4. On the Please answer the following questions to help us understand the issue you're facing page, enter the following details, and then click Next:
           >
           >    | Field                                                | Value                                                  |
           >    | ---------------------------------------------------- | ------------------------------------------------------ |
           >    | What product family is experiencing the issue?       | Select PingOne Advanced Identity Cloud                 |
           >    | What specific product is experiencing the issue?     | Select Configuration                                   |
           >    | What version of the product are you using?           | Select NA                                              |
           >    | What Hostname(s) or Tenant ID(s) does this apply to? | Enter the of FQDN for your sandbox tenant environment. |
           >
           > 5. On the Tell us about the issue page, enter the following details, and then click Next:
           >
           >    | Field                                      | Value                                                                                                                                                                                                                                                                                                                                                                    |
           >    | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
           >    | Provide a descriptive title for your issue | Enter `Unable to enable AI agents feature`                                                                                                                                                                                                                                                                                                                               |
           >    | Describe the issue below                   | Enter one of the follwing descriptions based on the HTTP status code you received in step 4:\* `Received a 500 HTTP status code when making a POST request to the /environment/aiagent?_action=enable endpoint.`\* `Received a 200 HTTP status code when making a POST request to the /environment/aiagent?_action=enable endpoint, but still can't access the feature.` |
           >
           > 6. Click Submit.
           >
           > 7. Wait for Ping Identity support to respond to your case with next steps for troubleshooting the issue.

---

---
title: Google Chrome Device Trust node
description: Use the Google Chrome Device Trust node to establish device trust with Chrome Enterprise in an Advanced Identity Cloud journey
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/auth-node-chrome-trust
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/auth-node-chrome-trust.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  compatibility: Compatibility
  inputs: Inputs
  dependencies: Dependencies
  set-pg: Set up PingGateway
  about_pinggateway_routes: About PingGateway routes
  set-sdn: Set up Scripted Decision node
  configuration: Configuration
  outputs: Outputs
  outcomes: Outcomes
  troubleshooting: Troubleshooting
  example: Example
---

# Google Chrome Device Trust node

Use the Google Chrome Device Trust node to establish device trust with [Chrome Enterprise](https://cloud.google.com/blog/products/chrome-enterprise/establish-device-trust-chrome-enterprise-and-ping-identity).

## Compatibility

| Product                               | Compatible? |
| ------------------------------------- | ----------- |
| Advanced Identity Cloud               | Yes         |
| PingAM (self-managed)                 | Yes         |
| Ping Identity Platform (self-managed) | Yes         |

## Inputs

This node reads the `challengeresponse` property from the journey state. This property is populated by a Scripted Decision node that retrieves the value from PingGateway.

## Dependencies

This node requires:

* [PingGateway must be installed and configured](#set-pg).

* [A Scripted Decision node be configured in the journey for redirection](#set-sdn).

### Set up PingGateway

1. Install PingGateway as indicated in the [Quick Install Guide](https://docs.pingidentity.com/pinggateway/latest/getting-started/preface.html).

2. Configure the `admin.json` file to run PingGateway on ports 9090 / 9443. Learn more about [starting up PingGateway with custom settings](https://docs.pingidentity.com/pinggateway/latest/installation-guide/start-stop.html#starting-options).

   If 9443 is for HTTPS, then readers need to configure PingGateway for server-side HTTPS. Learn more in [Configure PingGateway for TLS](https://docs.pingidentity.com/pinggateway/latest/installation-guide/securing-connections.html#server-side-tls).

3. Download the [generate\_challenge.json](https://github.com/ForgeRock/tntp-google-chrome-device-trust/blob/main/gateway/generate_challenge.json) and [challengeresponse.json](https://github.com/ForgeRock/tntp-google-chrome-device-trust/blob/main/gateway/challengeresponse.json) JSON route files.

4. Store the two JSON route files in your `routes` directory, for example:

   * $HOME/.openig/config/routes (on Mac or Linx) or

   * %appdata%\OpenIG\config\routes (on Windows).

5. Download and store the [getChallenge.groovy](https://github.com/ForgeRock/tntp-google-chrome-device-trust/blob/main/gateway/getChallenge.groovy) Groovy script file in your `groovy` directory, for example:

   * $HOME/.openig/scripts/groovy (on Mac or Linux), or

   * %appdata%\OpenIG\scripts\groovy (on Windows).

     If you do not have the `groovy` directory, create one.

#### About PingGateway routes

The `generate_challenge.json` route executes the `getChallenge.groovy` Groovy script to perform the following tasks:

1. Make an `HTTP POST` request to the Google Chrome Verified Access API to generate the challenge.

2. Get the challenge from the API response.

3. Set the challenge as the value of the x-verified-access-challenge custom HTTP response header.

   Google Chrome recognizes the custom HTTP response header and uses the challenge value to calculate a challenge-response.

4. Finally, Google Chrome creates a new custom HTTP request header, x-verified-access-challenge, and sets the challenge-response as the header value.

The `generate_challenge.json` route redirects the user to the `challengeresponse.json` route to perform these tasks:

1. Get the challenge-response from the request headers.

2. Set the challenge-response value in the query parameter of the redirect URL as the `challengeresponse` key.

3. Redirect back to Advanced Identity Cloud.

### Set up Scripted Decision node

This node requires a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) earlier in the journey to redirect the end user to PingGateway to generate and retrieve the `challengeresponse`.

1. Configure a Script Decision node. The following is an example script used in the Script Decision node.

   > **Collapse: Example Script Decision Node redirect script.**
   >
   > ```
   > try {
   >   var redirectMethod = "GET";
   >   var redirectUrl = "https://ig.example.com:9443/pinggateway-route-name";
   >   if (!requestParameters.get("challengeresponse")) {
   >     callbacksBuilder.redirectCallback(redirectUrl, {}, redirectMethod, true);
   >   } else {
   >     var challenge = requestParameters.get("challengeresponse");
   >     nodeState.putShared("x-verified-access-challenge", challenge);
   >     action.goTo("true");
   >   }
   >
   > } catch (error) {
   >   nodeState.putShared("errorMessage", error.toString());
   >   action.goTo('false').withErrorMessage(error);
   > }
   > ```
   >
   > * The above script uses the Next Generation Script Engine.
   >
   > * The `challengeresponse` parameter must be in the redirect to Advanced Identity Cloud as a query parameter from PingGateway.
   >
   > * The Google Chrome Device Trust node retrieves the `challengeresponse` value from the request parameters.

## Configuration

| Property                 | Usage                                                                    |
| ------------------------ | ------------------------------------------------------------------------ |
| API Key                  | The Google Cloud API key.                                                |
| Private Key              | Google Cloud administrator credential's private key.                     |
| Key ID                   | The credential used to verify the authenticity and integrity of the JWT. |
| Credentials Client Email | The email ID of the client with Google Cloud administrator credentials.  |

## Outputs

The node writes the Chrome Device Trust signals to transient state.

## Outcomes

* `Continue`

  Successfully authenticated the user.

* `Error`

  The journey follows this outcome path if the node is unable to obtain the device trust signals.

## Troubleshooting

If this node logged an error, review the log messages for the transaction to find the reason for the exception. Review the GCP configuration for the Chrome Enterprise Device Trust node and contact Google Support for further information.

## Example

![auth node chrome journey](../_images/auth-node-chrome-journey.png)

The example journey shows the following:

* A user logs in.

* The Chrome Device Trust Headers node, a Scripted Decision node, redirects to PingGateway to handle the Google Chrome challenge-response process.

* PingGateway generates the challenge, retrieves the challenge response, and sets it as a request parameter before redirecting back to the journey.

* The Google Chrome Device Trust node uses the challenge response to retrieve Chrome Device Trust signals, storing them in transient state.

* The Check Disk Encryption node, another Scripted Decision node, determines if the `diskEncryption` signal is disabled or enabled and makes an informed access decision.

  > **Collapse: The sample script used in this node.**
  >
  > ```
  > var diskEncrypted = nodeState.get("deviceSignals").get("diskEncryption");
  >
  > if(diskEncrypted === "DISK_ENCRYPTION_DISABLED") {
  >     outcome = "true"
  > } else {
  >     outcome = "false"
  > }
  > ```

---

---
title: Manage AI agents using the admin console
description: Create, configure, and manage AI agents and their application policies using the Advanced Identity Cloud admin console
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel/ai-agents-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel/ai-agents-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  create-an-ai-agent: Create an AI agent
  update-an-ai-agent: Update an AI agent
  update-an-ai-agents-basic-settings-or-custom-attributes: Update an AI agent's basic settings or custom attributes
  update-an-ai-agents-access-settings: Update an AI agent's access settings
  create-ai-agent-application-policies: Create AI agent application policies
  update-ai-agent-application-policies: Update AI agent application policies
  delete-an-ai-agent: Delete an AI agent
---

# Manage AI agents using the admin console

You can find background information on AI agents in PingOne Advanced Identity Cloud in [Secure your AI-driven solutions using AI agents](ai-agents.html).

## Create an AI agent

To create a new AI agent:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Click [icon: add, set=material, size=inline] Add AI Agent.

3. In the Add new AI Agent modal:

   1. Enter a descriptive Name for the AI agent. For example, "Retail Chatbot" or "Workforce Assistant".

   2. Enter a Client ID for the AI agent using only alphanumeric characters, dashes, or underscores. For example, "retail-chatbot" or "workforce-assistant".

      |   |                                                                                   |
      | - | --------------------------------------------------------------------------------- |
      |   | Once you enter a client ID and save the AI agent, the client ID can't be changed. |

   3. (Optional) Enter a Client Secret:

      * If you don't enter a value for the client secret, you can enter it later using the AI agent's Access tab.

      * If you do enter a value, make a note of it, as you won't be able to view it again after creating the AI agent.

   4. (Optional) Click Use Secret Store for secrets, then enter a Secret Label Identifier.

      * If you don't enter a value, you can enter it later using the AI agent's Access tab.

      * If you do enter a value, after saving the AI agent you must also create an ESV secret and map it to a secret label with the format `am.applications.oauth2.client.<identifier>.secret`. For example, if you enter `retail-chatbot-secret` as the secret label identifier, you must create an ESV secret and map it to the secret label `am.applications.oauth2.client.retail-chatbot-secret.secret`. Learn more in [Secret labels with identifiers](../../tenants/esvs-signing-encryption.html#secret-labels-with-identifiers).

   5. Click Save.

4. Complete the new AI agent's configuration using the instructions in [Update an AI agent](#update-an-ai-agent).

## Update an AI agent

To update an AI agent, use the following instructions:

* [Update an AI agent's basic settings or custom attributes](#update-an-ai-agents-basic-settings-or-custom-attributes)

* [Update an AI agent's access settings](#update-an-ai-agents-access-settings)

* Manage an AI agent's application policies:

  * [Create AI agent application policies](#create-ai-agent-application-policies)

  * [Update AI agent application policies](#update-ai-agent-application-policies)

### Update an AI agent's basic settings or custom attributes

To view or edit an AI agent's basic settings or custom attributes:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the AI agent you want to edit, then click it.

3. Click the Overview tab:

   1. (Optional) Edit the AI agent's Name. The name should be a descriptive label for the AI agent, such as "Retail Chatbot" or "Workforce Assistant".

   2. (Optional) Enter a Description for the AI agent. The description should provide additional context about the AI agent's purpose or functionality, such as "A chatbot that helps retail customers navigate products and answer questions" or "A workforce assistant that helps employees access enterprise tools and resources".

   3. (Optional) Select one or more Agent Owners for the AI agent. Agent owners are symbolic owners that can be used for visibility within your organization, but don't have any functional permissions or privileges related to the AI agent.

   4. (Optional) Click Show advanced settings, then enter one or more Custom attributes. Custom attributes are key-value pairs that let you add additional metadata to the AI agent. For example, you could add `status` and `state` attributes to track the AI agent's lifecycle.

      You can enter custom attributes in two ways:

      * **Basic editor**: Use Name and Value fields to enter custom attributes one at a time. You can click the add button ([icon: add, set=material, size=inline]) to add additional custom attributes as needed and click the remove button ([icon: remove, set=material, size=inline]) to remove any custom attributes you no longer need.

        ![AI agent custom attributes basic editor showing two custom attributes: 'status': 'active' and 'state': 'awaiting-approval'](../_images/ai-agent-custom-attributes-basic-editor.png)

      * **Advanced editor**: Use a JSON editor to directly manage the underlying JSON object that stores the custom attributes. To switch to the JSON editor, click Use advanced editor. You can switch back to the basic editor at any time by clicking Use basic editor.

        ![AI agent custom attributes advanced editor showing a JSON object with two key-value pairs: 'status': 'active' and 'state': 'awaiting-approval'](../_images/ai-agent-custom-attributes-advanced-editor.png)

4. Click Save.

### Update an AI agent's access settings

To view or edit an AI agent's OAuth 2.0 settings:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the AI agent you want to edit, then click it.

3. Click the Access tab.

4. Review the AI agent's Client ID and Client Secret fields:

   * The Client ID is a read-only field and can't be modified.

   * The Client Secret is a read-only, masked field.

5. (Optional) To add, update, or reset the Client Secret:

   1. Click the Reset button to the right of the Client Secret field.

   2. In the Reset Client Secret modal, enter a New Client Secret field. Make a note of the new secret, as you won't be able to view it again after clicking Save.

   3. Click Save.

6. (Optional) Click Use Secret Store for secrets, then enter a Secret Label Identifier. If you enter a value, after saving the AI agent you must also create an ESV secret and map it to a secret label with the format `am.applications.oauth2.client.<identifier>.secret`. For example, if you enter `retail-chatbot-secret` as the secret label identifier, you must create an ESV secret and map it to the secret label `am.applications.oauth2.client.retail-chatbot-secret.secret`. Learn more in [Secret labels with identifiers](../../tenants/esvs-signing-encryption.html#secret-labels-with-identifiers).

7. (Optional) Click Show advanced settings and update the OAuth 2.0 client profile settings as needed. The settings are listed in step 4 of [Create a client profile](https://docs.pingidentity.com/pingam/8/am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

8. Click Save.

### Create AI agent application policies

You can create application policies for an AI agent to specify which applications the AI agent can access, which end users or groups of end users the AI agent can act on behalf of when accessing those applications, and which OAuth 2.0 scopes the AI agent can use when accessing those applications.

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the AI agent you want to edit, then click it.

3. Click the Applications tab.

4. Click [icon: add, set=material, size=inline] Add Application.

5. In the Add new Application modal:

   1. Select an application from the Resources drop-down list. To create an application to select here, refer to [Application management](../../app-management/applications.html).

   2. (Optional) Enter a Description for the application policy. The description should provide additional context about the application policy. For example:

      * "Allows the retail chatbot to access the product catalog on behalf of customers to help them find products and answer questions"

      * "Allows the workforce assistant to access Salesforce on behalf of employees".

   3. (Optional) In the Acting On Behalf Of section, use one or both of the Subjects and Subject Groups drop-down lists to select which individual users (subjects) or groups of users (subject groups) the AI agent can act on behalf of when accessing the application. For example:

      * For a retail chatbot, you could specify a `Privilege Member` customer group to allow the AI agent to act on behalf of any user in that group.

      * For a workforce assistant, you could specify `Sales Support` and `Customer Service` employee groups to allow the AI agent to act on behalf of any user in that group.

      To create users or groups to select here, refer to [Manage identities](../../identities/manage-identities.html).

   4. (Optional) In the Permissions section, use the Permissions field to select or enter scopes:

      * You can select specific scopes from the drop-down list. The scopes in this list come from the application you select in the Resources field.

      * You can also enter custom scope values that aren't in the drop-down list by typing them into the field.

      When selecting scopes, you should choose only the scopes that are necessary for the AI agent to perform its intended functions when accessing the application, following the principle of least privilege. In particular, you should avoid selecting any high-risk or sensitive scopes that would allow the AI agent to perform actions that could be destructive or have significant consequences if misused, such as deleting data or managing user accounts. For example:

      * For a retail chatbot accessing a product catalog application, you might only select read-only scopes that allow the AI agent to view product information on behalf of customers, but not any write scopes that would allow the AI agent to modify or delete product information. Additionally, you might want to select scopes that allow the AI agent to add a product to a customer's shopping cart on their behalf, but avoid any scopes that would allow the AI agent to complete a purchase on the customer's behalf without their explicit approval.

      * For a workforce assistant accessing Salesforce, you might select a mix of read and write scopes that allow the AI agent to view and update customer information on behalf of employees, but avoid any high-risk scopes that would allow the AI agent to delete customer information or manage user accounts.

      To create scopes to select here, in the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, select the application you want to create scopes for, click the Sign On tab, then enter scope values in the Scopes field.

   5. Click Save.

6. Repeat steps 5 and 6 to create additional application policies for the AI agent as needed.

### Update AI agent application policies

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the AI agent you want to edit, then click it.

3. Click the Applications tab.

4. Review the application policies to find the policy you want to update.

5. To update an application policy:

   1. Click the application policy.

   2. In the Edit Application modal, follow the instructions in step 6 of [Create AI agent application policies](#create-ai-agent-application-policies).

6. To revoke an application policy:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Revoking an application policy immediately removes the AI agent's access to the associated application, which could cause disruptions if the AI agent is actively performing tasks on behalf of end users when you revoke the policy. Before revoking an application policy, make sure to review the AI agent's activity and audit logs to understand its recent actions and ensure that revoking the policy won't cause unintended consequences for your end users or your organization's AI-driven solutions. |

   1. Click the application policy's ellipsis icon ([icon: more_horiz, set=material, size=inline]), then click [icon: delete, set=material, size=inline] Revoke.

## Delete an AI agent

Before deleting an AI agent, make sure to review the AI agent's activity and audit logs to understand its recent actions and ensure that it's not still in use by any of your organization's AI-driven solutions.

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. (Optional) To delete an AI agent from the AI Agents page:

   1. Click the AI agent's ellipsis icon ([icon: more_horiz, set=material, size=inline]), then click [icon: delete, set=material, size=inline] Delete.

   2. In the Delete AI Agent? modal, click Delete.

3. (Optional) To delete an AI agent from the AI agent's own page:

   1. Click the AI agent.

   2. Click Delete Agent.

   3. In the Delete Agent? modal, click Delete.

---

---
title: Rapid channel changelog
description: Advanced Identity Cloud rapid channel changelog tracking the latest features, enhancements, and fixes deployed to sandbox environments
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel-changelog
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel-changelog.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["product-information:coming-soon.adoc"]
section_ids:
  july_2026: July 2026
  16_jul_2026: 16 Jul 2026
  enhancements: Enhancements
  fixes: Fixes
  08_jul_2026: 08 Jul 2026
  enhancements_2: Enhancements
  fixes_2: Fixes
  june_2026: June 2026
  15_jun_2026: 15 Jun 2026
  4_june_2026: 4 June 2026
  key_features: Key features
  enhancements_3: Enhancements
  fixes_3: Fixes
  april_2026: April 2026
  28_apr_2026: 28 Apr 2026
  changed_functionality: Changed functionality
  17_apr_2026: 17 Apr 2026
  enhancements_4: Enhancements
  14_apr_2026_rev1: 14 Apr 2026
  key_features_2: Key features
  enhancements_5: Enhancements
  fixes_4: Fixes
  09_apr_2026: 09 Apr 2026
  enhancements_6: Enhancements
  fixes_5: Fixes
  march_2026: March 2026
  30_mar_2026: 30 Mar 2026
  key_features_3: Key features
  fixes_6: Fixes
  24_mar_2026: 24 Mar 2026
  key_features_4: Key features
  enhancements_7: Enhancements
  fixes_7: Fixes
  23_mar_2026: 23 Mar 2026
  18_mar_2026: 18 Mar 2026
  key_features_5: Key features
  enhancements_8: Enhancements
  fixes_8: Fixes
  february_2026: February 2026
  27_feb_2026: 27 Feb 2026
  19_feb_2026: 19 Feb 2026
  fixes_9: Fixes
  changed_functionality_2: Changed functionality
  18_feb_2026: 18 Feb 2026
  enhancements_9: Enhancements
  fixes_10: Fixes
  17_feb_2025: 17 Feb 2025
  reversions: Reversions
  16_feb_2026: 16 Feb 2026
  fixes_11: Fixes
  13_feb_2026: 13 Feb 2026
  enhancements_10: Enhancements
  fixes_12: Fixes
  12_feb_2026: 12 Feb 2026
  enhancements_11: Enhancements
  fixes_13: Fixes
  09_feb_2026: 09 Feb 2026
  06_feb_2026: 06 Feb 2026
  enhancements_12: Enhancements
  fixes_14: Fixes
  changed_functionality_3: Changed functionality
  03_feb_2026: 03 Feb 2026
  enhancements_13: Enhancements
  fixes_15: Fixes
  january_2026: January 2026
  28_jan_2026: 28 Jan 2026
  fixes_16: Fixes
  27_jan_2026: 27 Jan 2026
  enhancements_14: Enhancements
  fixes_17: Fixes
  26_jan_2026: 26 Jan 2026
  23_jan_2026: 23 Jan 2026
  enhancements_15: Enhancements
  20_jan_2026: 20 Jan 2026
  14_jan_2026: 14 Jan 2026
  fixes_18: Fixes
  05_jan_2026: 05 Jan 2026
  fixes_19: Fixes
  december_2025: December 2025
  20_dec_2025: 20 Dec 2025
  17_dec_2025: 17 Dec 2025
  key_features_6: Key features
  enhancements_16: Enhancements
  fixes_20: Fixes
  15_dec_2025: 15 Dec 2025
  10_dec_2025: 10 Dec 2025
  enhancements_17: Enhancements
  fixes_21: Fixes
  november_2025: November 2025
  17_nov_2025: 17 Nov 2025
  enhancements_18: Enhancements
  fixes_22: Fixes
  changed_functionality_4: Changed functionality
  14_nov_2025: 14 Nov 2025
  12_nov_2025: 12 Nov 2025
  10_nov_2025: 10 Nov 2025
  05_nov_2025: 05 Nov 2025
  october_2025: October 2025
  31_oct_2025: 31 Oct 2025
  enhancements_19: Enhancements
  27_oct_2025: 27 Oct 2025
  enhancements_20: Enhancements
  fixes_23: Fixes
  24_oct_2025: 24 Oct 2025
  22_oct_2025: 22 Oct 2025
  20_oct_2025: 20 Oct 2025
  17_oct_2025: 17 Oct 2025
  16_oct_2025: 16 Oct 2025
  enhancements_21: Enhancements
  15_oct_2025: 15 Oct 2025
  08_oct_2025: 08 Oct 2025
  fixes_24: Fixes
  03_oct_2025: 03 Oct 2025
  september_2025: September 2025
  29_sept_2025: 29 Sept 2025
  26_sept_2025: 26 Sept 2025
  key_features_7: Key features
  enhancements_22: Enhancements
  fixes_25: Fixes
  25_sept_2025: 25 Sept 2025
  key_features_8: Key features
  enhancements_23: Enhancements
  fixes_26: Fixes
  19_sept_2025: 19 Sept 2025
  16_sept_2025_v2: 16 Sept 2025
  enhancements_24: Enhancements
  fixes_27: Fixes
  04_sept_2025: 04 Sept 2025
  03_sept_2025: 03 Sept 2025
  01_sept_2025: 01 Sept 2025
  key_features_9: Key features
  enhancements_25: Enhancements
  fixes_28: Fixes
  august_2025: August 2025
  29_aug_2025: 29 Aug 2025
  enhancements_26: Enhancements
  fixes_29: Fixes
  log_event_exporter_26_aug_2025: 26 Aug 2025
  key_features_10: Key features
  19_aug_2025_supplementary: 19 Aug 2025
  fixes_30: Fixes
  18_aug_2025: 18 Aug 2025
  enhancements_27: Enhancements
  15_aug_2025: 15 Aug 2025
  enhancements_28: Enhancements
  fixes_31: Fixes
  12_aug_2025: 12 Aug 2025
  07_aug_2025: 07 Aug 2025
  fixes_32: Fixes
  06_aug_2025: 06 Aug 2025
  enhancements_29: Enhancements
  july_2025: July 2025
  31_jul_2025: 31 Jul 2025
  fixes_33: Fixes
  30_jul_2025: 30 Jul 2025
  29_jul_2025: 29 Jul 2025
  28_jul_2025: 28 Jul 2025
  24_jul_2025: 24 Jul 2025
  23_jul_2025: 23 Jul 2025
  22_jul_2025: 22 Jul 2025
  21_jul_2025: 21 Jul 2025
  18_jul_2025: 18 Jul 2025
  key_features_11: Key features
  enhancements_30: Enhancements
  fixes_34: Fixes
  17_jul_2025: 17 Jul 2025
  16_jul_2025: 16 Jul 2025
  key_features_12: Key features
  14_jul_2025: 14 Jul 2025
  fixes_35: Fixes
  01_jul_2025: 01 Jul 2025
  key_features_13: Key features
  enhancements_31: Enhancements
  fixes_36: Fixes
  removed: Removed
  june_2025: June 2025
  30_june_2025: 30 June 2025
  reversions_2: Reversions
  25_jun_2025: 25 Jun 2025
  fixes_37: Fixes
  24_jun_2025: 24 Jun 2025
  23_jun_2025: 23 Jun 2025
  enhancements_32: Enhancements
  fixes_38: Fixes
  18_jun_2025: 18 Jun 2025
  enhancements_33: Enhancements
  fixes_39: Fixes
  16_jun_2025: 16 Jun 2025
  13_jun_2025: 13 Jun 2025
  10_jun_2025: 10 Jun 2025
  enhancements_34: Enhancements
  fixes_40: Fixes
  06_jun_2025_supplementary: 06 Jun 2025
  enhancements_35: Enhancements
  fixes_41: Fixes
  06_jun_2025: 06 Jun 2025
  fixes_42: Fixes
  04_jun_2025: 04 Jun 2025
  03_jun_2025: 03 Jun 2025
  02_jun_2025: 02 Jun 2025
  may_2025: May 2025
  30_may_2025: 30 May 2025
  key_features_14: Key features
  enhancements_36: Enhancements
  fixes_43: Fixes
  23_may_2025: 23 May 2025
  enhancements_37: Enhancements
  fixes_44: Fixes
  22_may_2025: 22 May 2025
  21_may_2025: 21 May 2025
  fixes_45: Fixes
  15_may_2025: 15 May 2025
  13_may_2025: 13 May 2025
  12_may_2025: 12 May 2025
  enhancements_38: Enhancements
  09_may_2025: 09 May 2025
  08_may_2025: 08 May 2025
  enhancements_39: Enhancements
  06_may_2025: 06 May 2025
  05_may_2025: 05 May 2025
  fixes_46: Fixes
  02_may_2025: 02 May 2025
---

# Rapid channel changelog

Subscribe to get automatic updates. Learn more in [Track rapid channel releases](release-process.html#track-rapid-channel-releases).

For release notes published before May 2025, refer to the [Rapid channel changelog archive](rapid-channel-changelog-archive.html).

## July 2026

### 16 Jul 2026

**Version 22773.0**

#### Enhancements

* FRAAS-33591: The promotions API now returns report metadata ordered by creation date, with the most recent first.

* IAM-3954, IAM-10782: Improved accessibility of numeric input fields and list fields throughout the admin console.

* IAM-10610: You can now mark parameters in custom reports as optional, giving you more flexibility when running reports.

* IAM-10764: Journey annotation notes now display multi-line formatting in view mode, matching how they appear when editing.

* IAM-10917: The deferred release environment message displayed in a modal during promotions now uses clearer language and explains that updating your production release version during promotion is standard practice.

#### Fixes

* FRAAS-32040: Fixed a deadlock where the `/environment/startup` endpoint became unresponsive when Advanced Identity Cloud services failed to start because of bad configuration.

* IAM-6882: Fixed an issue where the admin console displayed the incorrect product name.

* IAM-7788: Fixed an issue where the Next Generation scripts editor displayed unpublished environment secrets and variables.

* IAM-8343: Fixed an issue where the delete button for ESVs was not disabled for tenant auditors.

* IAM-10686: Fixed an issue where navigation labels in the hosted pages editor wrapped inconsistently compared to the hosted account pages.

* IAM-10728: Fixed a pagination issue where organization administrators with a limited user scope saw a `no users found` error after navigating past the last page of the user list.

* IAM-10780: Fixed an issue where exporting a journey containing a Device Profile node with a custom matching script did not include the script, causing import failures.

* IAM-10812: Fixed an issue where the edit icon in the Inner Tree Node and Scripted Decision Node opened an intermediate list instead of navigating directly to the linked resource.

* OPENAM-28030: Journey name validation rules in the access management backend are now consistent with those in the access management native console and the Advanced Identity Cloud admin console.

* OPENAM-28291: Fixed an issue where Page nodes using both a CAPTCHA node and live password validation could fail because the CAPTCHA token was reused on repeated validation requests. The fix is now available in Page node v3, which ensures that nodes with validation enabled generate a new CAPTCHA token for each validation request.

### 08 Jul 2026

**Version 22555.0**

#### Enhancements

* AME-34566: The **Evaluator Version** selector is now available in the Advanced Identity Cloud admin console for all remaining next-generation script types, including OIDC node, Social Provider Handler node, OAuth2 scripts, and Policy Condition scripts.

* FRAAS-33086: You can now migrate user accounts from the deprecated PKCS5S2 password hashing scheme to a more secure algorithm.

* IAM-2333: The **Identities** page now displays an **Account Status** column showing whether each user account is **Active** or **Inactive**.

* IAM-3671, IAM-9388, IAM-10148, IAM-10174, IAM-10548: Improved accessibility across hosted journey pages and the admin console, including context-sensitive page titles, form field labels, and `aria-describedby` attributes for the Attribute Collector node.

* IAM-8200: You can now use an environment secret or variable (ESV) to configure the from address for email providers.

* IAM-9628: Proxy Connect enabled tenants can now manage Proxy Connect configuration directly in the Advanced Identity Cloud admin console, without using the API.

* IAM-10069: Hosted journey pages now display hCaptcha text and challenges in the end user's configured locale.

* IAM-10536, IAM-10553, IAM-10558, IAM-10559: Improved color contrast for active UI components across multiple areas of the admin console to meet accessibility standards.

* IAM-10595: Updated the column picker component for consistent behavior across data tables in the admin console and hosted account pages.

* IAM-10596, IAM-10597, IAM-10598: Column visibility preferences for data tables in the admin console and hosted account pages are now customizable and saved between sessions.

* IAM-10641: The **AI Agents** page now displays an **Enable AI Agents** button when the feature has not yet been enabled.

* IAM-10796: Super administrators can now configure the redirect URI to use a custom domain when setting up federated administrator access.

* IAM-10952: The **Identities** page now displays a loading spinner while identity data is being fetched.

* OPENAM-27489: You can now create and edit social identity providers in the Advanced Identity Cloud admin console.

* OPENAM-27492: You can now configure self-service journey mappings directly in the Advanced Identity Cloud admin console.

* PF-39499\[[1](#_footnotedef_1 "View footnote.")]: Microsoft 365 SSO applications now use the selected **UPN Attribute Name** setting for WS-Trust username authentication. Existing applications must be resaved for this change to take effect.

#### Fixes

* FRAAS-31319: Fixed an issue where log streaming relied on the `source` field for the original log source, which can conflict with Splunk's reserved `source` field. Splunk log streaming now includes `stream_source` to preserve the original Advanced Identity Cloud log source.

* IAM-4875: Fixed an issue where ESV values couldn't be entered as the well-known endpoint URL when setting up Microsoft Entra ID as a federation IdP.

* IAM-5457: Fixed an issue where using an ESV in the **Password Policy** view caused the page to freeze.

* IAM-6374: Fixed an issue where journeys could be imported even when their referenced ESVs were not published.

* IAM-8313: Fixed an issue where setting a managed object property to nullable caused it to disappear from the **Password Policy** attribute validation list.

* IAM-10593: Fixed a layout issue on the **Journeys** page where journey counts for category tags were obscured for locales with longer words.

* IAM-10776: Fixed an issue where the stored username was overwritten with an OTP value when **Remember Me** was enabled during MFA sign-on.

* IAM-10833: Fixed an issue where the admin console incorrectly displayed "Rollback in progress" during a standard environment promotion.

* IAM-10836: Fixed a regression where `TextOutputCallback` messages containing custom HTML were rendered with unexpected line breaks.

## June 2026

### 15 Jun 2026

**Version 22293.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 4 June 2026

**Version 22170.0**

#### Key features

* Identity Governance role LCM (IGA-4265)\[[3](#_footnotedef_3 "View footnote.")]

  The new role lifecycle management (LCM) feature lets designated end users create, update, and delete roles on behalf of others without full administrative access. All changes are submitted as workflow-driven requests, maintaining governance and security while delegating role management to business owners.

* Identity Governance for AI agents (IGA-4223)\[[3](#_footnotedef_3 "View footnote.")]

  Agent Governance lets you detect, onboard, and govern AI agents the same way you govern human identities, accounts, and roles. This brings them under the governance umbrella alongside human identities.

  Find more information in [Agent Governance](../identity-governance/administration/iga-agent-governance.html) and [Agent Governance: custodian and reviewer tasks](../identity-governance/end-user/iga-agent-governance-enduser.html).

#### Enhancements

* AME-33781: Advanced Identity Cloud now supports the [WebAuthn conditional UI](../am-authentication/authn-mfa-webauthn.html#webauthn-conditional-ui), also known as passkey autofill. This lets your end users sign in with a passkey if they've previously saved one in their browser.

* IAM-1478: Autofill is now disabled for fields on pages where you add identities.

* IAM-4646: Tenant administrators registered through federation no longer have the option to update their username and password on the sign-on screen.

* IAM-9608: You can now assign an authorization policy to a SAML or OIDC application. This lets you restrict who can access an application to a subset of end users who have authenticated through a specific journey.

* IAM-9937: The [SaaS REST](../app-management/applications/saas-rest.html) and [SaaS REST (connector server)](../app-management/applications/saas-rest-rcs.html) applications now let you add filter policies to object types when you configure provisioning. Adding filters at the API level reduces network overhead, boosts synchronization performance, and prevents unwanted data from entering your identity pipeline.

* IAM-10132: The Advanced Identity Cloud admin console is now fully accessible using keyboard controls.

* IAM-10810: The PingOne worker service now lets you configure the connection to PingOne using a credential JWT.

* OPENAM-26335: The [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) now lets you suppress the display of the verification code in the PingOne Verify web UI.

* OPENAM-27540: You can now configure a trusted CA certificate for each OAuth 2.0 client using the `tls_client_auth` authentication method, instead of relying only on realm-wide CAs.

* IAM-8699: Advanced Identity Cloud now supports [node versioning](../journeys/node-versions.html). When we make changes to a node in the future, we'll create a new version of the node.

  This release introduces new node versions for the following nodes:

  | Node                                                                                                            | Description of change                                                                                                                                |
  | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)                                       | Adds support for standalone nodes within a Page node. Standalone nodes are self-contained and can be included after the final multiple outcome node. |
  | [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)             | Adds an option to prepopulate the username if it's available in the shared state.                                                                    |
  | [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) | Adds support for the WebAuthn conditional UI, also known as passkey autofill, and removes the ability to return the challenge as JavaScript.         |
  | [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)     | Removes the ability to return the challenge as JavaScript.                                                                                           |

  Other node versioning changes include:

  * Resource version `3.0` for `authenticationtrees` REST endpoint

    We've added a version-aware `3.0` resource to the `realm-config/authentication/authenticationtrees` endpoint. When sending a request to this endpoint, set the `Accept-API-Version` header to `protocol=2.1,resource=3.0`.

    Resource versions 1.0 and 2.0 are deprecated.

  * Versioned node endpoints

    The `realm-config/authentication/authenticationtrees/nodes` endpoint is now versioned. Specify the version of the node in the request URL, for example: `https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/nodes/UsernameCollectorNode/2.0`.

    Versionless node endpoints are deprecated.

  * Audit logging

    The node version is logged in the [am-authentication](../tenants/audit-debug-log-sources.html#am-sources) source under the `AM-NODE-LOGIN-COMPLETED` event for node versions greater than `1.0`.

#### Fixes

* AME-34254: Added support for next-generation SAML SP account mapper scripts to the Advanced Identity Cloud admin console.

* FRAAS-29198: Fixed an issue where promotions that failed due to the encrypted secrets verification check were not listing the configuration paths that needed updating.

* IAM-5003: Fixed an issue where changing the locale on the terms and conditions creation page didn't change the text in the editor.

* IAM-9751: Fixed an accessibility issue where the VoiceOver screen reader was not vocalizing UI text correctly.

* IAM-10040: Fixed an issue where the browser was incorrectly using autofill if a KBA Definition Node was within a Page node. The issue prevented use of tab and arrow functionality for that node.

* IGA-4139: Updated the access filter component in the IGA access graph to accept dynamic filter options. This lets you use different UI components to customize the available filter options, based on context.

* IGA-4275: Fixed a pagination issue in the Direct Reports view by removing sortable columns and default sort from the Direct Reports and Delegates pages.

* OPENAM-26359: Added a new configuration option, Enable Rich Authorization Requests with RCS, to the `OAuth2 Provider` service. This resolves an issue with remote consent where authorize requests with `authorization_details` would fail with an `invalid_request` error if an RCS was not configured.

## April 2026

### 28 Apr 2026

**Version 21659.0**

#### Changed functionality

* Graceful shutdown of identity management services (OPENIDM-19536)

  **What changed?** When an identity management service instance shuts down, it now drains in-flight HTTP traffic before exiting. In-flight responses include a `Connection: close` header that signals clients to close persistent (keep-alive) connections.

  **Why it matters?** Previously, integrations that held long-lived connections through a connection pool sent a request over a connection to an instance that had already shut down, which resulted in transient `404` responses or connection errors. With this change, compliant HTTP clients close affected connections and reconnect on the next request, which eliminates those transient failures during routine restarts and upgrades.

  **What you need to do?** Nothing, in most cases. Standard HTTP client libraries and connection pools honor the `Connection: close` header, by default. If you maintain a custom HTTP client or have explicitly disabled connection-close handling, verify that your client respects `HTTP/1.1` connection-close semantics.

### 17 Apr 2026

**Version 21531.0**

#### Enhancements

* New binding for next-generation SP adapter scripts (OPENAM-26050)

  A new `authnRequestHelper` binding has been added for next-generation SP adapter scripts. This binding lets you retrieve and modify the destination property of the `AuthnRequest`.

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | This entry was revised on 29 April 2026 as OPENAM-26050 was inadvertently excluded from the changelog. |

### 14 Apr 2026

**Version 21478.0**

#### Key features

* Snowflake connector (OPENIDM-21957)

  The [Snowflake connector](https://docs.pingidentity.com/openicf/connector-reference/snowflake.html) is now bundled with Advanced Identity Cloud. This new connector allows you to manage users, grant and revoke roles and database roles, and synchronize data between Advanced Identity Cloud and Snowflake.

  Learn more about the [1.5.20.33 Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html#1_5_20_33_connectors).

* Identity Governance Access Modeling\[[3](#_footnotedef_3 "View footnote.")] (IGA-3696)

  Advanced Identity Cloud Identity Governance introduces a new feature called Access Modeling (role mining) that analyzes existing user-to-entitlement assignments to discover potential access roles that reflect how people use access in your environment. Using advanced machine learning, it examines current roles and entitlements across your access landscape to propose new role candidates and suggest changes to existing ones.

  Access Modeling is an Advanced Identity Cloud add-on capability that integrates with the Identity Governance add-on capability.

#### Enhancements

* IAM-1715: Improve messaging on back button for 404 pages in the Advanced Identity Cloud admin console.

* IAM-3829: You can now perform dry-run promotions in the Advanced Identity Cloud admin console.

* IAM-3834: Distinguish between dry-run and actual promotions in the promotion report in the Advanced Identity Cloud admin console.

* IAM-8149, IAM-8275, IAM-8988: Added the following configuration options to the Advanced Identity Cloud admin console when you create or edit a journey:

  * `Override authenticated session timeout`, `Maximum Session Time`, and `Maximum Idle Time`

  * `Transactional Only`

  * `No Session`

  Previously, these settings could only be configured over REST.

* IAM-8972: You can now configure managed objects and relationships in the Advanced Identity Cloud admin console.

* IAM-9819\[[4](#_footnotedef_4 "View footnote.")]: Added the ability to export custom reports.

* IAM-9822: You can now perform promotion rollbacks in the Advanced Identity Cloud admin console.

* IAM-9903\[[4](#_footnotedef_4 "View footnote.")]: Added the ability to import custom reports.

* IAM-9960: Added a wider scope to the monitoring search feature by being able to search on `/payload/message` and just `/payload` in cases where the monitoring record's payload is a string.

* OPENIDM-22009: All connectors included with Advanced Identity Cloud were upgraded. Learn more in [1.5.20.34 Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html#1_5_20_34_connectors).

* IGA-4036: Added the ability to add and remove members of an entitlement directly from the entitlement LCM users tab.

#### Fixes

* IAM-1907: Fixed an issue where custom endpoint search showed an incorrect message.

* IAM-2537: Fixed an issue where non-dashboard URLs didn't show a 404 page.

* IAM-2615: Fixed an issue where border radius settings affected the hosted pages editor preview.

* IAM-3453: Fixed styling issues with the back button.

* IAM-5439: Fixed an issue where an ESV couldn't be updated after its last value was deleted.

* IAM-7502: Fixed an issue where the color in the `Card Input Border Focus Color` hosted pages setting wasn't applied to the search field in the **My Applications** hosted account page.

* IAM-9475: Fixed an issue in the hosted journey pages where a journey was allowed to continue in the event of a password mismatch when a message node was on the same page.

* IAM-9752: Fixed an issue where VoiceOver gestures didn't work on drop-down lists.

* IAM-9842: Fixed an issue where VoiceOver didn't announce text for some page elements.

* IAM-9936: Fixed an issue with the query operation in the SaaS REST application where setting the type select field prevented the method select field from being cleared, and the other way around.

* IAM-9952: Fixed an issue where the table header for the action column was empty on several pages in the hosted account pages.

* IAM-9958: Fixed an issue where the table header for the action column was empty on several pages in the Advanced Identity Cloud admin console.

* IAM-10056: Fixed an issue on the **Auth Scripts** page where the modal body failed to load after clicking **[icon: add, set=material, size=inline] New Script**.

### 09 Apr 2026

**Version 21386.0**

#### Enhancements

* FRAAS-31357: You can now use the `/environment/aiagent?_action=enable` endpoint to simplify the process of enabling the AI Agents feature in your sandbox environments. Learn more in [Enable the AI agents feature](rapid-channel/ai-agents-enable.html).

* IGA-4247\[[3](#_footnotedef_3 "View footnote.")]: Added two new log sources, `iga-api` and `jas`, to improve Identity Governance monitoring:

  * The `iga-api` log source captures Identity Governance events related to API requests, certifications, segregation of duties (SOD), events, glossary, and lifecycle management (LCM).

  * The `jas` log source captures events from the Java API Service (JAS), including receipt, republishing, and processing of identity management audit messages, as well as logging of entity creation and updates with success and failure tracking.

#### Fixes

* FRAAS-31613: Fixed an issue where password policy updates weren't properly replicating to the datastore in mutable environments.

## March 2026

### 30 Mar 2026

**Version 21182.0**

#### Key features

* Identity for AI (IAM-9357)

  You can now use *AI agents* to secure your organization's AI-driven solutions. AI agents are specialized OAuth 2.0 clients that are onboarded with their own identities. They can securely perform tasks on behalf of end users through a delegated token exchange process, ensuring distinct accountability and granular access control.

  You can use AI agents to securely build digital assistants that operate on behalf of end users, such as a chatbot on a retail website helping a user navigate products, or an internal workforce assistant acting on behalf of an employee to access enterprise tools like Salesforce.

  Learn more about AI agents in [Secure your AI-driven solutions using AI agents](rapid-channel/ai-agents.html).

#### Fixes

* FRAAS-31318: Fixed an issue where setting certain special characters in an ESV prevented the ESV from being interpreted correctly.

### 24 Mar 2026

**Version 21083.0**

#### Key features

* Partial support for Rich Authorization Requests (RAR) (AME-28325)

  The `/authorize` and `/par` endpoints now optionally accept the `authorization_details` parameter from the RAR (Rich Authorization Requests) specification RFC 9396, allowing clients to specify fine-grained authorization requirements.

* App Policy Decision node (AME-30063)

  A new [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) is a specialized policy node that lets you enforce OIDC and SAML application access policies in journeys. You can use the node to filter access by group, organization, and more.

* Support for audience parameter in token exchange (AME-33970)

  A client can now specify audience parameters in OAuth 2.0 Token Exchange requests. These parameters can be allowlisted and, if valid, are included in the audience claim of the resulting token.

* Next-generation scripted JWT operations (OPENAM-25836)

  The `jwtValidator` and `jwtAssertion` bindings are now available in all next-generation scripts.

#### Enhancements

* AME-33573: Next-generation scripts now include `utils.base64url.encode()` and `utils.base64url.decodeToBytes()` for Base64URL encoding and decoding.

* AME-33971: Added a new Save and Test Connection button to the PingOne worker configuration screen allowing you to validate the connection.

* AME-33973: You can now configure the PingOne Worker Service connection using a credential JWT.

* AME-34248: You can now use next-generation scripts in the Social Provider Handler node to transform normalized profile data into identities or managed users.

* AME-34249: You can now use next-generation scripts in the OIDC ID Token Validator node. The `jwtClaims` binding now behaves as a native JavaScript object.

* AME-34540: You can now specify autocomplete attributes for username nodes.

* OPENAM-21474: A new `Minimum max_age for Authorize Requests` property is now available in the advanced OIDC settings of the OAuth 2.0 provider service.

* OPENAM-23610: The default value for the Return challenge as JavaScript (Legacy) property on the WebAuthn Authentication and WebAuthn Registration nodes is now not enabled. Ping Identity recommends that you keep this setting.

* OPENAM-24523: You can now dynamically modify the scopes of a refresh token during the refresh flow with the new next-generation scope validation script binding, `scopeValidatorHelper`, and its method, `inheritAccessTokenScopesOnRefresh()`. This is useful when scope validation scripts alter access token scopes and you need the refresh token to inherit those changes.

* OPENAM-25901: Next-generation OAuth 2.0 scope validation scripts now have access to the `availableScopes` binding, which lists all scopes configured for the client. A new `throwInvalidScope()` method is also available to simplify error handling.

#### Fixes

* AME-34216, AME-34398: When using an SSO token as the subject for a policy with an `IDM user` environment condition, it now correctly resolves to the IDM `_id` instead of the user's AM universal ID.

  You can temporarily revert this behavior by setting the ESV `esv.am.policy.condition.idm.universalId` to `true` to let you update policies to use another property.

* AME-34329: By default, parallel updates can no longer be made for CTS sessions. You can revert this behavior by setting the ESV `esv.cts.use.etag.assertion.on.updates` to `false`.

### 23 Mar 2026

**Version 21076.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 18 Mar 2026

**Version 21027.0**

#### Key features

* Policy Decision node (AME-28779)

  A new [Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/policy-decision.html) lets you evaluate an authorization policy against resources within an authentication journey.

* Backchannel Notification node (AME-32579)

  Introduced a new [Backchannel Notification node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-notification.html) that allows a backchannel journey to send real-time status updates to the main authentication journey.

#### Enhancements

* FRAAS-28387: Invites for Advanced Identity Cloud tenant registration now use a one-time passcode (OTP) instead of a magic link. This change prevents email scanners from accidentally invalidating single-use links.

* AME-29745: Improved the certificate validation process in the Certificate Collector and Certificate Validation nodes. By default, Advanced Identity Cloud collects the \_first certificate in a certificate chain (the user certificate). You can now create an ESV named `esv-am-nodes-certificatechain-validation-enforced` and set its value to `true` to collect the chain of certificates.

* AME-33851: You can now use next-generation scripts for social identity provider transformation scripts.

* OPENAM-25329: The PingOne Protect Initialize node now includes an `Additional Signals SDK Initialization Options` attribute. This allows you to configure options that aren't already defined in the node. The `PingOneProtectInitializeCallback` has been updated with new fields to support this.

* OPENAM-25677: The `PingOneProtectInitializeCallback` now includes a `universalDeviceIdentification` field, which replaces the deprecated `enableTrust` field. The `enableTrust` field is still returned for backward compatibility.

#### Fixes

* IGA-4186\[[3](#_footnotedef_3 "View footnote.")]: Fixed an Identity Governance issue where the end-user UI did not correctly sort and paginate large user populations, improving responsiveness for large datasets.

* OPENAM-22698: Fixed a bug that caused duplicate URIs in WS-Federation responses.

## February 2026

### 27 Feb 2026

**Version 20814.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 19 Feb 2026

**Version 20712.0**

#### Fixes

* OPENIDM-21493: You can now cancel a clustered reconciliation even when a route associated with the source or target system is unavailable.

#### Changed functionality

* OPENIDM-21718: The `maxQueueSize` for [queued synchronization](../idm-synchronization/chap-implicit-live-sync.html#queued-sync) now defaults to `1000` and can't be configured to a value higher than `1000` or lower than `100`. The previous default was `20000`.

  The `pageSize` still defaults to `100`, but now can't be configured to a value higher than `100` or lower than `10`. If the configured `pageSize` is greater than `maxQueueSize / 10`, Advanced Identity Cloud uses `maxQueueSize / 10` for the page size.

  If you have any configuration outside of these bounds, Advanced Identity Cloud automatically adjusts the values to the nearest bound.

### 18 Feb 2026

**Versions 20698.0, 20705.0**

#### Enhancements

* AME-34191: You can now override the HTTP binding used to redirect users to the SAML error page. To do this, configure an [ESV variable](../tenants/esvs.html#variables) named `esv-global-saml-error-page-http-binding` and set its value to `HTTP-POST` or `HTTP-Redirect`. If you don't set this variable, Advanced Identity Cloud uses the default value of `HTTP-POST`.

* IAM-6546: End users now have more options to manage their devices in the hosted account pages. For each device, they can view when it was last used for sign on, view when it was added, edit its name, and delete it.

* IAM-9672: In the advanced sync **Mapping** tab, if no properties have been mapped, it now shows a more accurate description of the target and source identity objects whose properties can be mapped.

#### Fixes

* IAM-6640: Fixed an issue in the hosted pages theme preview where clicking **Edit Personal Info** opened two instances of the modal.

* IAM-8221: Fixed an issue in the terms & conditions live preview where interactive elements weren't disabled.

* IAM-9620\[[3](#_footnotedef_3 "View footnote.")]: Fixed an Identity Governance issue where clicking **Save** in the certification template creation wizard didn't disable the button after submission, which could result in the creation of unintended duplicate templates.

* IAM-9786: Fixed an issue where ESV placeholders manually entered into a field were always treated as strings, regardless of whether they were an array, list, or string.

* IAM-9886: Fixed a display issue on the **Reports Run History** tab where the pop-up menu items weren't displayed correctly.

### 17 Feb 2025

#### Reversions

**Versions 20552.0, 20554.0**

All identity management (`OPENIDM`) changes associated with this release have been withdrawn. This affects the following changelog entry:

* [06 Feb 2025](#06_feb_2026)

### 16 Feb 2026

**Version 20679.0**

#### Fixes

* OPENAM-25779: Deletion of the `samlApplication` object is now deferred for unsuccessful authentication journeys so that the object is still available for subsequent sign-on attempts in the same session.

### 13 Feb 2026

**Version 20645.0**

#### Enhancements

* The following OAuth 2.0 scripts can now use the next-generation scripting engine, which gives them access to common bindings such as `utils` and `openidm`:

  * AME-33228: OIDC claims

  * AME-33846: Scripted JWT validator

  * AME-33847: Scope validation

  * AME-33848: Authorize endpoint data provider

  * AME-33849: Scope evaluation

  * AME-33850: May act

* The following SAML 2.0 scripts can now use the next-generation scripting engine, which gives them access to common bindings such as `utils` and `openidm`:

  * AME-32919: SP adapter

  * AME-32920: IDP adapter

  * AME-32921: IDP attribute mapper

* AME-32969: You can now make sure the `samlApplication` binding is available for all SAML flows by enabling the application context in the hosted IdP or remote SP entity configuration. Previously this was only added in certain situations such as when using an application journey or IdP-initiated integrated mode.

* AME-32997: Added an `Allow Retry` option to the Backchannel Initialize node that lets end users retry a failed backchannel authentication journey.

* AME-33430: You can now include remote consent agent credentials in a `Basic Authentication` header for pushed consent requests.

* AME-33930: A new `testConnection` action on the `realm-config/services/pingOneWorkerService/workers/pingone-worker-service-name` endpoint lets you test the connection from Advanced Identity Cloud to PingOne.

* AME-33939: A new `listLatestNodeDefinitions` action on the `realm-config/authentication/authenticationtrees/nodes` endpoint provides a list of node definitions for the *latest* version of each node.

  This action combines the responses from the following separate actions into a single response:

  * `getAllTypes` action on the `realm-config/authentication/authenticationtrees/nodes` endpoint

  * `schema`, `template` and `listOutcomes` actions on the `realm-config/authentication/authenticationtrees/nodes/node-name` endpoint

* FRAAS-29084: Custom domains are now restricted to a maximum of 63 characters in the Advanced Identity Cloud admin console. This restriction has always existed on the system backend.

* OPENAM-22125: A new Proxy Configuration tab in the Http Client Service configuration lets you use separate proxy configurations per HTTP Client instance.

* OPENAM-24476: Added `java.util.zip` classes to the allowlist for the Scripted Decision node scripting context.

* The following enhancements have been made to the nodes provided with Advanced Identity Cloud:

  * AME-33009: Enhanced the RADIUS Decision node to capture Vendor-Specific Attributes (VSA) returned by the RADIUS server during authentication.

  * Enhancements to the PingOne Protect Evaluation node:

    * AME-33807: Fixed an issue where a default value was sent for the flow subtype. Previously, the node would fall back to using the value configured in Authentication Flow Subtype or Authorization Flow Subtype. Now, if nothing is found in the node state, the node doesn't send a value to PingOne Protect.

    * OPENAM-24557: Added a configuration property that lets you specify a custom session ID in the node state.

    * OPENAM-24562: Added two configuration properties that let you include a custom browser cookie and any externally maintained `deviceId` in the request sent to PingOne.

    * OPENAM-25553: Added a configuration property that lets you include user group information as part of a risk evaluation.

  * The following nodes now let you set custom headers on journey success, failure, and error:

    * AME-33813: Set Success Details node

    * AME-33874: Set Failure Details node

    * AME-33873: Set Error Details node

  * OPENAM-24419: Added a new [RSA SecurID](https://docs.pingidentity.com/auth-node-ref/latest/rsa-securid.html) node. This node replaces the Marketplace RSA SecurID node, which is now deprecated.

  * OPENAM-24546: Removed certain unused and unsupported configuration properties from the PingOne Protect Initialize node and its associated callback (`PingOneProtectInitializeCallback`).

  * OPENAM-25372: Added a [JWT Password Replay](https://docs.pingidentity.com/auth-node-ref/latest/jwt-password-replay.html) node to secure the user's password within an encrypted JSON Web Token (JWT). This node is used by PingGateway and replaces the old Password Replay scripting functionality.

  * OPENAM-24401: The CAPTCHA node now prevents submission after expiry.

  * OPENAM-24489: The Device Binding and Device Signing Verifier nodes now let you specify a clock skew between the client device and AIC. This helps prevent binding failures caused by clocks being out of sync.

* OPENAM-25371: Added a configuration property to the PingOne Verify Evaluation node to enable automatic redirection to the journey after an end user completes verification (when using the `Redirect` delivery mode).

* OPENAM-25618: The new `locales` binding lets you return the localized version of a string from a translation map. It is available to next-generation Configuration Provider node, Journey Decision node, and Device Match node scripts.

#### Fixes

* AME-33653: Custom nodes now work with the Configuration Provider node.

* AME-33808: If Node State Attribute For User ID is provided in the PingOne Protect Evaluation node, but the corresponding attribute is missing from the node state, the node triggers the failure outcome rather than using the user ID associated with the AM identity.

* AME-34217: Added a version setting to the Configuration Provider node. This update provides the underlying infrastructure for a node versioning feature in an upcoming release.

* OPENAM-21881: Updated the Page node to remove `pageNodeCallbacks` from the shared state after the node completes.

* OPENAM-23918: Resolved a race condition in the OATH Registration node and OATH Device Storage node where recovery codes could potentially be lost.

* OPENAM-24065: Improved consistency for error responses across realms when processing illegal arguments. The `/authenticate` call now correctly returns a 400 (Bad Request) instead of a 500 (Internal Server Error) for invalid arguments.

* OPENAM-25406: Added an `identity.exists()` method to next-generation objects returned by `idRepository.getIdentity()`. This lets scripts verify an identity's existence in the identity store before further processing.

### 12 Feb 2026

**Version 20612.0**

#### Enhancements

* ANALYTICS-1383\[[4](#_footnotedef_4 "View footnote.")]: The new historical change report feature provides a complete audit trail of changes to your managed identities. It tracks all modifications to user profiles, roles, accounts, and applications. You can easily generate reports to see what changed, who made the change, and when it happened, which gives you clear insights for compliance and security monitoring.

#### Fixes

* ANALYTICS-1326\[[4](#_footnotedef_4 "View footnote.")]: Fixed an issue in custom reports caused by relationships between custom identities that contain multiple underscores.

* ANALYTICS-1367\[[4](#_footnotedef_4 "View footnote.")]: Fixed an issue in custom reports caused by IP addresses in journey events.

### 09 Feb 2026

**Versions 20575.0, 20577.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 06 Feb 2026

|   |                                                                                                                                       |
| - | ------------------------------------------------------------------------------------------------------------------------------------- |
|   | Identity management changes in this release have been reverted. All OPENIDM changes associated with this release have been withdrawn. |

**Versions 20552.0, 20554.0**

#### Enhancements

* OPENIDM-21472: When provisioning applications and using queued synchronization, changes to a user account now propagate to all associated accounts.

#### Fixes

* OPENAM-25702: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) again supports a Node State Attribute For Username setting. PingOne Protect risk evaluation calls can depend on the username.

* OPENIDM-21493: You can now cancel a clustered reconciliation even when a route associated with the source or target system is unavailable.

* OPENIDM-21776: The Advanced Identity Cloud identity management service now uses synchronous HTTP client requests to connect to external identity management, REST, and token introspection services. This change prevents connection closure exceptions from terminating reconciliation.

#### Changed functionality

* OPENIDM-21718: The `maxQueueSize` for [queued synchronization](../idm-synchronization/chap-implicit-live-sync.html#queued-sync) now defaults to `1000` and can't be configured to a value higher than `1000` or lower than `100`. The previous default was `20000`.

  The `pageSize` still defaults to `100`, but now can't be configured to a value higher than `100` or lower than `10`. If the configured `pageSize` is greater than `maxQueueSize / 10`, Advanced Identity Cloud uses `maxQueueSize / 10` for the page size.

  If you have any configuration outside of these bounds, Advanced Identity Cloud automatically adjusts the values to the nearest bound.

### 03 Feb 2026

**Version 20512.0**

#### Enhancements

* FRAAS-29829: Removed a reference to "PingOne Advanced Identity Cloud" from the `404 Not Found` error page.

#### Fixes

* AME-34034: Fixed an issue where omitting a shared secret label in the RADIUS Decision node caused Prometheus metrics to become unavailable.

## January 2026

### 28 Jan 2026

**Version 20408.0**

#### Fixes

* OPENAM-25707: Fixed [PingOneProtectInitializeCallback](../am-authentication/callbacks-interactive.html#PingOneProtectInitializeCallback) processing to prevent unwarranted HTTP 4xx and 5xx errors.

### 27 Jan 2026

**Version 20406.0**

#### Enhancements

* IAM-4464: Next-generation configuration provider scripts created through the journey editor now contain the default config for the selected node type.

* IAM-9709: Updated the journey editor to make fewer network calls when saving a journey that contains page nodes.

#### Fixes

* IAM-4345: Vertical tabs were missing a hover state.

* IAM-8033: Journey name field did not have a length check in place.

* IAM-8226: When importing a journey, if you skip the the download backup option but then return to it using the **Previous** link, it now completes the backup before offering the download.

* IAM-9590: The message shown in the hosted pages for an unauthorized access attempt is now correctly centered on a single page.

* IAM-9687: When you enter a valid ESV placeholder in the URL field of a bookmark application, the field is now immediately disabled and shows a delete icon to remove the placeholder.

* IAM-9803: The link to the access management native console from the Advanced Identity Cloud admin console now always correctly links to the Alpha or Bravo realm.

### 26 Jan 2026

**Version 20385.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 23 Jan 2026

**Version 20359.0**

#### Enhancements

* FRAAS-23284: RCS connections to Advanced Identity Cloud now have a default timeout value of `10000` (10 seconds) for new tenants. Existing tenants retain the default timeout value of `-1` (no timeout).

### 20 Jan 2026

**Version 20340.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 14 Jan 2026

**Version 20285.0**

#### Fixes

* OPENAM-25646: For backward compatibility, we've restored the following deprecated fields sent to PingOne Protect by the PingOne Protect Initialize node (in the `PingOneProtectInitializeCallback`):

  * `consoleLogEnabled`

  * `deviceAttributesIgnored`

  * `customHost`

  * `lazyMetadata`

  * `deviceKeyRsyncIntervals`

  * `disableHub`

  |   |                                                                                                                                                                                                   |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | These fields are deprecated and no longer supported in PingOne. This fix restores the fields but you should update your clients and scripts to remove the unsupported fields as soon as possible. |

### 05 Jan 2026

**Version 20185.0**

#### Fixes

* FRAAS-13233: AM script validation now ignores ESV placeholders in commented-out code.

## December 2025

### 20 Dec 2025

**Version 20133.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 17 Dec 2025

**Version 20090.0**

#### Key features

* AD Decision node to authenticate against Active Directory identity stores (AME-14959)

  The [AD Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ad-decision.html) verifies that the provided username and password exist in the specified Active Directory data store. The node also checks whether the user account is locked, disabled, or has expired.

* Cache management service (AME-32248, AME-32285)

  A new scripted cache management service lets you create and use caches in Scripted Decision nodes. This can improve performance for slow tasks, such as fetching access tokens for third party services that can be reused between journeys. The service has its own metrics.

  Find more information in [Cache script values](../am-scripting/cache-manager.html).

* SAML 2.0 SP account mapper (OPENAM-23986)

  A new SAML 2.0 SP account mapper script type enables dynamic modification of SAML assertion data before it's used to identify local users.

  Find more information in [SP account mapper](../am-saml2/custom-sp-account-mapper.html).

* Support for SAML 2.0 IdP-initiated flows in integrated mode (AME-29258)

  You can now configure the hosted SP to redirect to a journey when a response is received from the IdP.

  Use the new configuration option to check that the IdP entity ID in the incoming SAML assertion matches the IdP entity ID configured for the node.

  A new method has also been added to the `samlApplication` script binding that returns the assertion as a JSON map.

  Find more information in [Redirect to a journey on the hosted SP](../am-saml2/configure-providers.html#config-redirect-journey).

#### Enhancements

* AME-31153: Consent request data can now be pushed via backchannel.

* AME-31429: A new field on the remote consent agent lets you include properties from the resource owner's session as part of the consent request.

* AME-31846: Next-generation Config Provider Node scripts can now access the following additional scripted node bindings:

  * `callbacks`

  * `callbacksBuilder`

  * `jwtAssertion`

  * `jwtValidator`

  * `resumedFromSuspend`

  * `requestCookies`

  * `samlApplication`

  * `oauthApplication`

* AME-32064: The [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html) includes a new configuration option,`validateIdpEntityId`. When set to `true`, the node validates that the IdP entity ID from the SAML assertion is the same as the IdP entity ID configured on the node.

* AME-32970: You can now access the application context for \_all OAuth 2.0 / OIDC flows through the `oauthApplication` binding by setting `Enable Application Context` in the OAuth 2.0 provider or at the client level. Previously, you could only use this binding when using an application journey.

* IAM-8244: Adds support for bidirectional mappings in synchronization configuration.

* IAM-8497: Added a brand administrator role to the Advanced Identity Cloud admin console. Brand administrators only have access to change hosted pages themes.

* IAM-9484: Added ability to provide translation overrides for the Waiting Message field in the Polling Wait node and the Email Suspend Message field in the Email Suspend node. This lets you provide translations when the `PollingWaitCallback` or the `SuspendedTextOutputCallback` callbacks are added using scripts.

* OPENAM-23711: Adds a `Detect connection timeout` option to the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html). When enabled, connection timeouts from social identity providers result in the journey following the Timeout outcome.

* OPENAM-24059: Adds support for the `android-key` WebAuthn attestation format.

* OPENAM-24130: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) now lets you set the flow subtype that's sent to PingOne Protect.

* OPENAM-24137: You can now configure the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) to obtain biographic matching data from the node state.

* OPENAM-24350: Cryptographic keys can now be derived in next-generation scripts using the PBKDF2 algorithm.

* OPENAM-24548: The [PingOne ProtectInitialize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) now lets you obtain PingID Device Trust Agent attributes when going through a PingOne Protect flow.

* OPENAM-24552: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) now lets you send a target application name in addition to the existing target application ID, in the PingOne Protect evaluation request.

* OPENAM-24554: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) now lets you use targeted PingOne policies.

* OPENAM-24560: Removed the User Type and User Name fields from the PingOne Protect Evaluation node. The user type is always `EXTERNAL` and the user name is not applicable to external user types. Only the `User ID` is sent in the PingOne Protect evaluation request.

* OPENAM-24587: You can now configure Google Secret Manager key IDs (KIDs) as ESVs.

* OPENAM-25327: Next-generation OAuth 2.0 scripts can now access the `redirectUris` property on the `clientProperties` binding.

* OPENAM-25417: You can now configure the `SameSite` option for cookies in the [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/latest/set-persistent-cookie.html) and the [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/latest/persistent-cookie-decision.html).

* OPENAM-25418: The attestation `fmt` type is now included in the transient state data of the WebAuthn nodes.

#### Fixes

* AME-32307: Fixed an issue where end users weren't able to continue a PingOne Verify journey that requested a QR code if they didn't have a separate device to scan the code.

* AME-32513: Added the `suspend` action to [Custom nodes](../journeys/node-designer.html).

* IAM-8766: Fixed an issue with [mustRun](../am-authentication/configure-authentication-trees.html#enable-journey-completion) journeys and query parameters such as `forceAuth=true`, where end users were authenticated then immediately unauthenticated.

* IAM-9430: A warning is now displayed in the Advanced Identity Cloud admin console when a promotion would cause a deferred release tenant to be upgraded at the same time.

* OPENAM-20582: Lets you configure a list of accepted JWT issuers for OAuth 2.0 clients. These are now accepted in addition to the OAuth 2.0 client ID for private key JWT authentication.

* OPENAM-23929: Fixed a performance issue related to schema caching.

* OPENAM-24297: Fixed an issue where the PingOne Verify Evaluation node incorrectly returned a failure outcome when the PingOne environment timed out during the identity verification process. This could happen, for example, if an end user didn't engage with the QR code or selfie capture. The update correctly detects the `TRANSACTION_TIMED_OUT` status in PingOne responses and returns the timeout outcome, letting journeys handle timeouts distinctly from failures.

* OPENAM-24309: The PingOne Verify Evaluation node now supports a list of values in an attribute sent for biographic matching.

### 15 Dec 2025

**Versions 20039.0, 20042.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 10 Dec 2025

**Version 19974.0**

#### Enhancements

* FRAAS-28686: For log streaming, the `am-everything` and `idm-everything` sources now include sub-source information in the `source` and `extracted_source` fields.

  For example, `am-everything` returns logs containing the corresponding match in `am-access`, `am-activity`, `am-authentication`, `am-config`, `am-core`. This ensures that logs consolidated under `am-everything` are correctly identified and parsed by log analysis tools such as Splunk, retaining their original context.

#### Fixes

* FRAAS-29022: Streamed logs now correctly identify the application in the `source` field.

## November 2025

### 17 Nov 2025

**Version 19722.0**

#### Enhancements

* IAM-9395: Table columns are now resized uniformly across the Advanced Identity Cloud admin console.

* IAM-9516: The tenant administrator profile page now prompts for re-authentication when adding or removing an MFA device.

* OPENIDM-19400: New Prometheus metric for the availability of connector servers, for example:

  `idm_icf_connector_server_availability{name="system-id",type="connector-server-type",} 1.0`.

* OPENIDM-20341: Identity management scripts now natively support Base64 encoding using the `btoa` (encode) and `atob` (decode) [global script](../idm-scripting/scripting-func-engine.html#global-utility-functions) bindings.

* OPENIDM-20790: The `openidm/sync/mappings` endpoint now [supports paging](../idm-synchronization/mappings.html#sync-mapping-paging) using either offsets or cookies.

* OPENIDM-20933: Improved task scanner exception handling. If the task scanner encounters a task that results in an exception, it now aborts only that task and continues processing the remaining tasks. Previously, the scanner would abort the entire process when any task caused an exception.

* OPENIDM-20937: New provisioner metric `idm_icf_pending`. Includes all the same tags as `idm_icf*`.

* OPENIDM-21170: Metrics for router filters now use `router_filter` for the metric name and include a `name` tag to identify the specific filter.

* OPENIDM-21171: Metrics for managed identity script hooks now use `managed-script-hook` for the metric name, `object` to tag the identity object, and `script-hook` to tag the script hook.

* OPENIDM-21172: Metrics for custom endpoints now use the new `custom_endpoint` metric name and include a `name` tag based on the custom endpoint configuration name after the hyphen. For example, a custom endpoint configuration `endpoint-onboardCustomer.json` will generate metrics with a name tag/label of "onboardCustomer". The policy service makes use of an internal scripted endpoint based on the file `policy.js`, and its metric name is `policy-js`.

* OPENIDM-21233: The `openidm/health/ready` endpoint has been enhanced to include the number of waiting requests. A new set of metrics have been added to provide a historical accounting of IDM health.

#### Fixes

* IAM-9466: Annotation comments added to sub-nodes are now saved correctly.

* IAM-9496: The tooltip in journey comments now correctly displays the creator's name without overflow.

* IAM-9527: The theme logo now correctly uses the height specified in the theme.

* OPENICF-3277: The SaaS REST connector no longer throws a `NullPointerException` when attributes are missing in the request payload.

* OPENIDM-20525: The `cn` and `telephoneNumber` schema for `alpha_user` and `bravo_user` are now `scope: public` and `searchable: true`. This schema change applies to sandbox tenants created on or after November 17, 2025. Existing sandbox tenants are unchanged.

* OPENIDM-20863: Default values for multivalue mappings are now copied by value to prevent unintended mutations during runtime.

* OPENIDM-21421: Updating the configuration of an inactive provisioner no longer throws an `IllegalStateException`.

* OPENIDM-21454: Every failed record from a live sync is now stored in the dead-letter queue with a unique entry ID.

#### Changed functionality

* Default API version for unversioned requests (OPENIDM-21191)

  Previously, REST API requests without an `Accept-API-Version` header used the latest available API version for the resource. These unversioned requests now default to API version `1.0` for most endpoints. However, the `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

### 14 Nov 2025

**Version 19704.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 12 Nov 2025

**Version 19674.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 10 Nov 2025

**Version 19646.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 05 Nov 2025

**Version 19604.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

## October 2025

### 31 Oct 2025

**Versions 19567.0, 19573.0**

#### Enhancements

* IAM-9429: If your production environment is configured for deferred release, you can use the new `/environment/promotion/promote` endpoint to check if running a promotion will trigger a release upgrade.

### 27 Oct 2025

**Version 19521.0**

#### Enhancements

* IAM-1709: Exposed `useInPlaceholders` and `encoding` attributes when creating ESV secrets in the admin console.

* IAM-9312: Table columns are now resized uniformly across the following Advanced Identity Cloud admin console pages:

  * **Tenant settings**

  * **Scripts**

  * **Security**

  * **Terms & Conditions**

* IAM-9323: Added **Metadata** tab to user resource page to display properties such as `createDate` and `loginCount`.

#### Fixes

* IAM-9217: Fixed cron schedule validation for new jobs.

### 24 Oct 2025

**Version 19514.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 22 Oct 2025

**Version 19480.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 20 Oct 2025

**Version 19448.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 17 Oct 2025

**Version 19433.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 16 Oct 2025

**Version 19414.0**

#### Enhancements

* FRAAS-28370: Fixed an issue where requests to the `/monitoring/prometheus/am` and `/monitoring/prometheus/idm` endpoints occasionally didn't return timely responses.

### 15 Oct 2025

**Versions 19379.0, 19387.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 08 Oct 2025

**Version 19292.0**

#### Fixes

* AME-32979: The Core Token Service (CTS) now stores `AUTHENTICATION_WHITELIST` tokens with millisecond-level precision for the expiry timestamp. This minimizes contention in indexes.

### 03 Oct 2025

**Version 19259.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

## September 2025

### 29 Sept 2025

**Version 19190.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 26 Sept 2025

**Version 19173.0**

#### Key features

* Create custom authentication nodes (IAM-5759)

  Advanced Identity Cloud lets you create your own nodes to reuse common functionality in authentication journeys. Define properties and run custom server-side scripts in these nodes to dynamically set values and decide the outcome of journeys.

  Learn more in [Custom nodes](../journeys/node-designer.html).

#### Enhancements

* IAM-9000, IAM-9001: Added annotations and sticky notes to journeys to assist learning and collaboration.

* IAM-9237: Allow ESVs to be embedded in URL fields for federation IdPs. This lets you set up federation IdPs with fewer ESVs because you can define a single ESV containing a UUID shared by multiple URL fields.

* IAM-9246: Table columns are now resized uniformly across all table views.

#### Fixes

* IAM-9153: Password validation now works correctly when pasting a value that matches the existing value.

### 25 Sept 2025

**Version 19095.0**

#### Key features

* Mapping custom key IDs to secrets (AME-31380)

  You can now map custom `kid` header values for JWTs signed with the signing key to a specific ESV secret.

* Nodes to support backchannel authentication journeys (AME-31636 and AME-31635)

  The new [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html) and [Backchannel Status node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-status.html) let you implement backchannel authentication from within a journey.

* Next-generation OAuth 2.0 access token modification scripts (AME-31083)

  You can now create next-generation access token modification scripts that can use next-generation common bindings, such as `httpClient`, `openidm`, and `utils`.

* Ability to configure journeys as *transactional only* (\[.\_2025-10-14]#AME-31843)

  A transactional authentication journey only runs when Advanced Identity Cloud starts a transaction, which happens when Advanced Identity Cloud does one of the following:

  * Initializes [backchannel authentication](../am-authentication/backchannel-authentication.html) using either the `/authenticate/backchannel/initialize` endpoint or the [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html).

  * Runs a [SAML 2.0 app](../am-saml2/configure-providers.html#samlapp-journey) journey for a remote SP.

  * Runs an [OAuth 2.0 app](../am-oauth2/oauth2-register-client.html) journey when Advanced Identity Cloud is acting as an authorization server.

  * Enforces a [transactional authorization](../am-authorization/transactional-authorization.html) policy.

  You can only configure transactional authentication journeys using the REST API. Set the `transactionalOnly` property to `true` in the journey configuration.

* Journey binding for scripted nodes (OPENAM-23127)

  The new `journey` binding for scripted nodes lets you obtain details of the current journey, including inner or child journeys.

#### Enhancements

* AME-30984 and AME-30609: Enhanced authentication audit logging to include the SAML Identity Provider (IdP) and Service Provider (SP) entity IDs during SAML flows. This information lets you report on the SAML applications users are accessing, supporting analytics and dashboarding efforts.

* AME-30985: In SAML v2.0 single sign-on (SSO) flows, the JSON web token (JWT) created in the browser's session storage no longer expires.

  The time allowed to complete the SSO flow is now determined by the configurable [maximum duration](../am-authentication/suspended-auth.html#maximum-duration) of the journey session instead of the JWT expiration.

  Previously, the JWT expired when the cache was cleared.

* AME-31082 and SDKS-3681: Added support for device token refreshing to the Push Notification Service endpoint, enabling the reception of new tokens from mobile devices.

* AME-31379: You can now enforce the OAuth 2.0 request object processing rules that apply, regardless of the request type. Create an ESV named `esv.oauth2.provider.request.object.processing.enforced` and set its value to `true`. This setting forces Advanced Identity Cloud to use the specification set in the [Request Object Processing Specification](../am-reference/services-configuration.html#config-request-object-proc-spec) field of the OAuth 2.0 provider configuration for JWT requests.

* AME-31656 and AME-31468: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) has been enhanced to support dynamic risk policy IDs and target app IDs. To set the risk policy set ID dynamically, enable `Use Node State Attribute For Risk Policy Set ID` in the node configuration. To set the target app ID dynamically, enable `Use Node State Attribute For Target App ID` in the node configuration. This instructs the node to obtain these IDs from the node state.

* AME-31398: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) has been enhanced to support custom attributes. To specify custom attributes to be used in PingOne Protect for custom predictors, set the `Node State Attribute For Custom Attributes` in the node configuration. The node retrieves a map of custom attributes from the node state to be used in the evaluation request to PingOne Protect.

* AME-31487: Improvements to SAML v2.0 standalone mode include replacing legacy JSPs with URL endpoints.

  You can still invoke the JSPs because they're mapped to URLs for backward compatibility, but any customizations to these JSPs will be lost.

  The following URLs supersede SAML v2.0 JSPs:

  > **Collapse: URLs**
  >
  > | Old URL                                     | New URL               |
  > | ------------------------------------------- | --------------------- |
  > | `/saml2/jsp/exportmetadata.jsp`             | `/ExportSamlMetadata` |
  > | `/saml2/jsp/idpSingleLogoutInit.jsp`        | `/IDPSloInit`         |
  > | `/saml2/jsp/idpSingleLogoutRedirect.jsp`    | `/IDPSloRedirect`     |
  > | `/saml2/jsp/idpSingleLogoutPOST.jsp`        | `/IDPSloPOST`         |
  > | `/saml2/jsp/idpMNIRedirect.jsp`             | `/IDPMniRedirect`     |
  > | `/saml2/jsp/idpMNIRequestInit.jsp`          | `/IDPMniInit`         |
  > | `/saml2/jsp/idpSSOFederate.jsp`             | `/idpSSOFederate`     |
  > | `/saml2/jsp/spAssertionConsumer.jsp`        | `/Consumer`           |
  > | `/saml2/jsp/saml2AuthAssertionConsumer.jsp` | `/AuthConsumer`       |
  > | `/saml2/jsp/spSingleLogoutInit.jsp`         | `/SPSloInit`          |
  > | `/saml2/jsp/spSingleLogoutRedirect.jsp`     | `/SPSloRedirect`      |
  > | `/saml2/jsp/spSingleLogoutPOST.jsp`         | `/SPSloPOST`          |
  > | `/saml2/jsp/spMNIRedirect.jsp`              | `/SPMniRedirect`      |
  > | `/saml2/jsp/spMNIPOST.jsp`                  | `/SPMniPOST`          |
  > | `/saml2/jsp/spMNIRequestInit.jsp`           | `/SPMniInit`          |
  > | `/saml2/jsp/spSSOInit.jsp`                  | `/spssoinit`          |
  > | `/saml2/jsp/idpSSOInit.jsp`                 | `/idpssoinit`         |
  > | `/saml2/jsp/idpSSOFederate.jsp`             | `/idpSSOFederate`     |
  > | `/saml2/jsp/SA_IDP.jsp`                     | `/idpsaehandler`      |
  > | `/saml2/jsp/SA_SP.jsp`                      | `/spsaehandler`       |

* IAM-8236: The ability to edit journeys from the AM native admin console has been removed. Use the Advanced Identity Cloud admin console to edit journeys.

* OPENAM-20776: A new OIDC client configuration option, `Private Key JWT Audience`, lets you configure and override the audience (`aud`) claim of a Private Key JWT.

* OPENAM-21783: Improved token management for OAuth 2.0 client applications.

  This change resolves issues related to managing tokens issued to OAuth 2.0 clients that override the `Use Client-Side Access & Refresh Tokens` setting. Specifically: **The [/users/user/oauth2/applications](../am-oauth2/rest-api-oauth2-applications-endpoint.html) endpoint now correctly returns all tokens issued to clients. **Administrators can now successfully revoke any tokens issued to a client, as required.

* OPENAM-23051 and AME-31918: A new ESV, `esv.oauth2.request.object.restrictions.enforced` lets you enforce stricter adherence to the [PAR](https://www.rfc-editor.org/rfc/rfc9126.html) and [JAR](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2) specifications.

  Setting the value of this ESV to `true` enforces the following: **The authorization server ignores authorize parameters outside the `request_uri`. **When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

* OPENAM-23669: \_Full scopes (scopes ending in `*`) can now be used by service accounts in all cases where more specific scopes (for example, `:read`) are used.

* OPENAM-23710: The `httpClient` binding is now available to legacy SAML 2.0 IdP adapter scripts.

* OPENAM-23850: Enhanced the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) with an `Allow same device verification` option that lets end users continue verification on their current device.

* OPENAM-23867: The [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html) no longer logs credential failures as errors. It now logs them at the `info` level.

* OPENAM-24062: Added support for the `ECDSA` algorithm to the `utils.crypto.subtle` next-generation binding. This algorithm is supported for key generation, signing, and verification.

#### Fixes

* AME-31351 and AME-31471: Improvements to the Device Code flow mean that end users are now prompted to reauthenticate even when there's an existing session for must-run and app journeys.

* AME-31481: Validation around policy creation has been improved. If you're using the legacy "Policy" environment condition (or a custom environment condition), you'll need to add that to the list of allowed environment conditions for your policy set to create or update policies that use that condition type.

* OPENAM-20749: A new ESV, `esv-enable-oauth2-sync-refresh-token-issuer` causes a stateful OAuth 2.0 introspect response to overwrite the `iss` claim of the introspectable token. To enable this behavior, set this ESV to `false`.

  For compatibility reasons, the existing behavior in Advanced Identity Cloud is not changed by default.

* OPENAM-23770: Canceling a WebAuthn flow now results in a `Client Error` outcome, rather than an internal failure.

* OPENAM-24159: Fixed an issue that prevented multiple [Identity Assertion](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html) nodes from being used in a single journey.

### 19 Sept 2025

**Versions 19095.0, 19101.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 16 Sept 2025

**Version 19054.0**

#### Enhancements

* OPENAM-24486: Improved performance when creating large numbers of OAuth 2.0 clients simultaneously.

#### Fixes

* OPENDJ-11486: Fixed an exception caused when identity management queried for users with a filter containing wildcards and specific object classes.

### 04 Sept 2025

**Version 18897.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 03 Sept 2025

**Versions 18859.0, 18878.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 01 Sept 2025

**Version 18842.0**

#### Key features

* Reports API endpoints to import and export report templates# (ANALYTICS-1195\[[5](#_footnotedef_5 "View footnote.")])

  Added the ability to import and export report templates using reports API endpoints.

* Custom objects as data sources for reporting (ANALYTICS-582\[[5](#_footnotedef_5 "View footnote.")]\[[4](#_footnotedef_4 "View footnote.")])

  Custom objects can now be used as data sources for reporting. The system uses an object's configured title for the data source name, makes its properties available as attributes, and represents all object relationships.

#### Enhancements

* ANALYTICS-1165\[[5](#_footnotedef_5 "View footnote.")]: Added the capability to change a report name.

* IAM-7547: Access policy modal now validates IPv4 or IPv6 format for IP addresses.

* IAM-8922: The Advanced Identity Cloud admin console now accepts ESV placeholders for the following federation fields:

  * Application ID

  * Application Secret

  * Well-Known Endpoint

  * Authorization Endpoint

  * User Info Endpoint

  * Token Endpoint

  * Issuer

* IAM-8982\[[3](#_footnotedef_3 "View footnote.")]: Add event function for setting the query filter/select options of a select field.

* IAM-9066: Added **Tenant Auditor** option to Advanced Identity Cloud admin console federation groups claim.

* IAM-9099, IAM-9146, IAM-9167: Many table views now support column resizing and customization.

#### Fixes

* IAM-5488: Terms and Conditions now respects target attribute in anchor tags.

* IAM-6588: The Advanced Identity Cloud admin console now correctly displays journey status for journeys disabled and enabled using ESVs.

* IAM-8887: Prevent browsers auto-filling passwords in user registration journeys.

* IAM-8940: Managed identity number property now accepts float values.

* IAM-8956: Deselecting the **Personal Information** option now disables the section containing the user avatar in hosted account pages.

* IAM-9169: Fixed styling for responsive table layouts with sticky action column in **Identities** table views.

## August 2025

### 29 Aug 2025

**Version 18823.0**

#### Enhancements

* FRAAS-25919: You can now use the API to configure custom domains for the Advanced Identity Cloud admin console.

* OPENIDM-21372: Advanced Identity Cloud now prevents access to the identity repository endpoint, `/openidm/repo`. This prevents uncontrolled and potentially incompatible schema changes.

#### Fixes

* AME-32756: Fixed an issue with policy evaluation returning results from a stale policy index cache.

* FRAAS-26287: Advanced Identity Cloud now correctly authenticates the sender address for emails sent to Advanced Identity Cloud tenant administrators, `saas@pingidentity.com`.

* OPENDJ-11634: Advanced Identity Cloud now prevents searches with many results and no applicable index from overloading the system.

### 26 Aug 2025

**Version N/A**

#### Key features

* Log event exporter (FRAAS-19963)

  Advanced Identity Cloud now lets you export log event data to an external monitoring tool, such as an OpenTelemetry-compatible SIEM or Splunk. This helps you monitor events and troubleshoot issues in near real time.

  Learn more in [Stream logs to an external monitoring tool](../tenants/audit-debug-logs-push.html).

### 19 Aug 2025

**Version 18712.0**

#### Fixes

* OPENAM-24393: Fixed an issue where the InnerTreeEvaluator node failed for authentication journeys initially accessed using REST without an `authId`.

### 18 Aug 2025

**Version 18700.0**

#### Enhancements

* FRAAS-25547: The sender address for emails sent to Advanced Identity Cloud tenant administrators is now `saas@pingidentity.com`.

### 15 Aug 2025

**Versions 18678.0, 18684.0**

#### Enhancements

* OPENAM-24384: Added `javax.crypto.SecretKeyFactory`, `javax.crypto.spec.PBEKeySpec`, and `com.sun.crypto.provider.PBKDF2KeyImpl` classes to the allowlist for the `OAUTH2_ACCESS_TOKEN_MODIFICATION` scripting context.

#### Fixes

* FRAAS-25734: Exception stacktraces in access management and identity management logs are now truncated to approximately 300-400 lines.

### 12 Aug 2025

**Version 18623.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 07 Aug 2025

**Versions 18559.0, 18570.0**

#### Fixes

* FRAAS-25821\[[6](#_footnotedef_6 "View footnote.")]: Fixed an issue that prevented IP rules in the Proxy Connect add-on from being disabled.

* OPENAM-24159: Fixed an issue with Identity Assertion nodes failing if there are more than one in a journey.

### 06 Aug 2025

**Version 18550.0**

#### Enhancements

* FRAAS-24857: CNAME verification is no longer required when creating a custom domain.

* FRAAS-26063: You can now override the `samlErrorPageUrl`. To do so, configure an [ESV variable](../tenants/esvs.html#variables) named `esv-global-saml-error-page-url` and set its value to your SAML error page URL. If you don't set this variable, Advanced Identity Cloud uses the default value of `/saml2/jsp/saml2error.jsp`.

## July 2025

### 31 Jul 2025

**Version 18483.0**

#### Fixes

* IAM-9062: Hosted pages themes no longer continuously refresh when trying to set up or confirm two-factor authentication (2FA).

### 30 Jul 2025

**Version 18468.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 29 Jul 2025

**Version 18451.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 28 Jul 2025

**Versions 18435.0, 18444.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 24 Jul 2025

**Version 18395.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 23 Jul 2025

**Version 18382.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 22 Jul 2025

**Version 18368.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 21 Jul 2025

**Version 18347.0, 18351.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 18 Jul 2025

**Version 18331.0**

#### Key features

* Try In SDK button (IAM-8618)

  A **Try In SDK** button has been added to the **Details** page for Native / SPA applications. This lets developers quickly test SDKs with dynamic configuration code snippets.

* Custom WS-Fed applications (IAM-8261)

  You can now create custom WS-Fed\[[7](#_footnotedef_7 "View footnote.")] applications for single sign-on (SSO).

#### Enhancements

* FRAAS-25818: The built-in SMTP server in new tenants now has a limit of 10 emails per minute and a fixed email sender address with the format `noreply@<tenant-fqdn>`.

* IAM-7581: Text wrapping in table views has been improved for readability.

* IAM-8573: IDM now includes an endpoint to retrieve individual themes from the `/themerealm` configuration using either an `ID` or a `_queryFilter` by name. This improves performance and ensures reliable theme loading, even on slow networks.

* IAM-8610: When you create an SSO application for Microsoft 365, the application now generates a signing certificate, which you can download or rotate as needed.

* IAM-8633: You can now add, remove, and rearrange table columns for managed identities and application provisioning tables.

* IAM-8925\[[8](#_footnotedef_8 "View footnote.")]: In Identity Governance, you can now configure actions that trigger automatically when a form first loads or when a user changes the value of a specific field.

* IGA-3674\[[8](#_footnotedef_8 "View footnote.")]: A Wait node is now available for IGA workflows. This node pauses the workflow until a specified date and time, for example, if you need to seek approvals.

* IGA-3700\[[8](#_footnotedef_8 "View footnote.")]: Improved UI for suspended requests in table and request view.

* IGA-3742\[[8](#_footnotedef_8 "View footnote.")]: The form editor now includes icons in the list of fields in the left panel.

#### Fixes

* IAM-8789: Managed identity modals now correctly handle both single-value and array-based enum types.

* IAM-4397: Fixed an issue in the hosted journey pages where the prompt text for the Choice Collector node wasn't fully visible and the default option wasn't visible at all.

* IAM-8632: Fixed an issue where validation errors were incorrectly displayed for pre-populated fields.

* IAM-8871: The hosted account pages no longer freeze and throw an error when editing details if there are empty custom enum array values.

* IAM-8902: The application username field in SAML 2.0 NameID flows is now correctly set to `uid` instead of `username`.

### 17 Jul 2025

**Version 18311.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 16 Jul 2025

**Version 18295.0**

#### Key features

* Monitor log entries in the admin console (FRAAS-25665)

  Advanced Identity Cloud now provides a console for monitoring log entries in development and sandbox\[[9](#_footnotedef_9 "View footnote.")] environments. You can view, filter, and search log entries for specific log sources within a timeframe to quickly identify issues, track events, and ensure system security.

  |   |                                                                                                                                                                                                                             |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This is a [beta](../product-information/release-lifecycle.html#beta) feature and is limited to development and sandbox\[[9](#_footnotedef_9 "View footnote.")] environments. It's not available in production environments. |

### 14 Jul 2025

**Version 18274.0**

#### Fixes

* IAM-8933: Fixed an issue in the Advanced Identity Cloud admin console when creating or modifying identity objects with a required boolean property. You can now set the value of the required boolean property to `false`.

### 01 Jul 2025

**Version 18170.0**

#### Key features

* Policy binding for next-generation scripting (AME-26150)

  The next-generation `policy` binding lets you access the policy engine API and evaluate policies from within scripts. The `policy` binding works in a similar way to the [Request policy decisions for a specific resource](../am-authorization/rest-api-authz-policy-decisions.html#rest-api-authz-policy-decision-concrete) API call.

* Set Error Details node (AME-30968)

  The [Set Error Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-error-details.html) adds details to the JSON response when a journey ends in an error.

#### Enhancements

* AME-31372: An **Agent** journey is now available by default in both Alpha and Bravo realms. The `Agent` journey makes it easier to integrate with Ping Identity agents and gateways. It validates the agent credentials with an [Agent Data Store Decision](https://docs.pingidentity.com/auth-node-ref/latest/agent-data-store-decision.html) node.

* AME-30050: You can now enable a next-generation script in the AM native admin console native console to run after a Dynamic Client Registration request is processed.

* AME-30716: Removed `Failed to create SSO Token` from logs at warning level. To observe these warnings, increase the log level to debug.

* AME-30801: The [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html) now has an optional **Error Outcome** that lets you capture exception details if an exception occurs during the evaluation of the child journey.

* OPENAM-22467: Customers can now provide any value in the `typ` header in JWTs.

* Greater control over journey session duration and authenticated session timeouts:

  * OPENAM-23265: The [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html) now lets you customize the **Maximum Session Time** and **Maximum Idle Time** of the session granted at the end of the journey.

  * OPENAM-23290: The new [Update Journey Timeout node](https://docs.pingidentity.com/auth-node-ref/latest/update-journey-timeout.html) lets you update the timeout of the journey.

  * OPENAM-23291: The [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html) now lets you configure the **Suspend Duration** in minutes. This duration overrides existing global or realm settings.

  * OPENAM-23515: You can now set the suspend duration in next-generation scripted decision nodes when suspending the journey.

* OPENAM-23438: Following Webauthn Registration and Authentication, new information is added to the transient state.

* OPENAM-20709: On successful authentication, the [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) now adds the UUID of the device (`webauthnDeviceUuid`) and the name of the device (`webauthnDeviceName`) to the shared state. This lets you track the use of biometric authentication and the device used to authenticate.

#### Fixes

* AME-30969: If the **OIDC Claims Plugin Type** in the OAuth 2.0 provider is set to `SCRIPTED` but no script is selected, the `userinfo` endpoint now returns the `sub` claim, in compliance with the OIDC specification. Previously, the `userinfo` endpoint returned an empty JSON object. If you still require this behavior, set the `esv-scripting-legacynulloidcclaimsscriptbehaviour` ESV to `true`.

* OPENAM-20749: For server-side OAuth 2.0 tokens, the [/oauth2/introspect](../am-oauth2/oauth2-introspect-endpoint.html) response can now overwrite the `iss` claim of the introspectable token. To enable this behavior, set the `esv-enable-oauth2-sync-refresh-token-issuer` ESV to `false`.

* OPENAM-22928: When agents authenticate to Advanced Identity Cloud, the session created no longer expires.

* OPENAM-23334: You can now use the `mergeShared` and `mergeTransient` methods to add nested objects to `ObjectAttributes`.

* OPENAM-23519: Improved error handling during WebAuthn registration when the Android lock screen isn't enabled.

#### Removed

* Modules and chains (AME-30762)

  The legacy PingAM authentication mechanism using modules and chains is enabled by default in Advanced Identity Cloud but has never been supported. Modules and chains remain enabled but have been removed from the Advanced Identity Cloud admin console.

  Modules and chains will be removed entirely in the near future. If you're using them for authentication, you must migrate to nodes and trees as soon as possible.

  Advanced Identity Cloud provides default journeys that replace the corresponding *default* modules and chains. Any default authentication processes that relied on modules and chains are unaffected by their removal.

## June 2025

### 30 June 2025

#### Reversions

**Version 18094.0** has been reverted. All changes associated with this version have been withdrawn. This affects the following changelog entry:

* [25 Jun 2025](#25_jun_2025)

### 25 Jun 2025

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | This version has been reverted and all associated changes withdrawn. |

**Version 18094.0**

#### Fixes

* IAM-8314: Fixed an issue where setting ESVs in connector or provisioner configuration stops the Advanced Identity Cloud admin console from being able to update connectors or run a liveSync operation.

### 24 Jun 2025

**Version 18076.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 23 Jun 2025

**Version 18045.0**

#### Enhancements

* AME-31379: Setting the new ESV `esv-oauth2-provider-request-object-processing-enforced` to `true` now lets admins enforce which validation rules are applied when processing OAuth 2.0 request objects.

#### Fixes

* FRAAS-25226: Allow a higher threshold for large JSON log entries before splitting them into smaller plaintext log entries.

### 18 Jun 2025

**Version 17994.0**

#### Enhancements

* FRAAS-25437: Tenant administrators with the `tenant-auditor` role can now use federated access to authenticate to Advanced Identity Cloud.

* IAM-3441: Added pagination to all list views.

* IAM-7265: You can now right-click a node in the journey editor to access a context menu.

* IAM-7266: Added an action bar to the journey editor that lets you deselect or delete currently selected nodes.

* IAM-7580: Pages now span the full width of the screen, improving navigation and usability.

* IAM-8260: Advanced Identity Cloud now supports multiple WS-Fed applications\[[7](#_footnotedef_7 "View footnote.")].

* IAM-8640: The **Release Notes** link in **Tenant Settings** now opens the release notes for the tenant's specific version.

* IAM-8714\[[3](#_footnotedef_3 "View footnote.")]: You can now configure columns in the Identity Governance access review page.

* IAM-6820: The Email Suspend node now provides a drop-down list of available email templates.

* OPENIDM-21206\[[10](#_footnotedef_10 "View footnote.")]: Usernames and application names must now be unique, as enforced by the datastore.

#### Fixes

* IAM-7413: The reCAPTCHA Enterprise node is now fully supported.

* IAM-8489: Fixed an issue with the display of application logos in the hosted account pages.

* IAM-8770: Fixed an issue with the calendar icon position in date fields.

* IAM-8773: Fixed an issue where key actions such as realm login were blocked in older tenants with an unmodified original theme.

### 16 Jun 2025

**Version 17959.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 13 Jun 2025

**Versions 17949.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 10 Jun 2025

**Version 17889.0**

#### Enhancements

* ANALYTICS-868: The **Tenant Admin Activity** report has been changed to the **Tenant Admin Initiated Managed Objects Changes** report. The new report provides more detailed and business-friendly insights into changes made by tenant administrators:

  * Field names added, deleted, or modified.

  * Before and after values of changed attributes (if applicable).

  * Business-friendly entity name and entity type changes to custom attributes and custom objects.

#### Fixes

* OPENAM-21783: Improved token management for OAuth 2.0 clients that override the **Use Client-Side Access & Refresh Tokens** setting. The OAuth 2.0 applications endpoint now correctly shows all tokens issued to these clients. Additionally, administrators can now successfully revoke any of the tokens issued to these clients.

### 06 Jun 2025

**Version 17853.0**

#### Enhancements

* IAM-8405: You can now duplicate out-of-the-box reports.

* IAM-8591: Dynamic sorting for report results. You can now sort report results directly in the Advanced Identity Cloud admin console after running a report.

  |   |                                                                                                                                                                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | * Sorting is available only when the result set contains fewer than 10,000 rows.

  * Columns with complex data types (for example, JSON) can't be sorted.

  * Downloaded reports reflect the original data order, not the sorted view from the Advanced Identity Cloud admin console. |

#### Fixes

* FRAAS-25434: Fix issue causing source to sometimes be defined as `unknown` in `/monitoring/logs/*` endpoints.

### 06 Jun 2025

**Version 17836.0**

#### Fixes

* FRAAS-25269: The IDC.CLI OAuth 2.0 client is now deprecated in existing tenants and no longer provisioned in new tenants. Use a [service account](../tenants/service-accounts.html) instead.

### 04 Jun 2025

**Version 17825.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 03 Jun 2025

**Versions 17804.0, 17821.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 02 Jun 2025

**Version 17800.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

## May 2025

### 30 May 2025

**Version 17779.0**

#### Key features

* Tenant auditors (IAM-8086)

  Advanced Identity Cloud now lets you invite tenant auditors to access the Advanced Identity Cloud admin console. Tenant auditors can view settings, configuration, and data but cannot modify them.

* Tenant auditor role (FRAAS-24460)

  Advanced Identity Cloud now supports a tenant auditor role with read-only access to ancillary APIs.

  For new tenants, Advanced Identity Cloud doesn't support non-global realm user access and OAuth2 client access to the ESV API. Access is deprecated for existing tenants.

#### Enhancements

* FRAAS-25155: Increased log batching size to avoid truncation of large JSON log entries.

#### Fixes

* FRAAS-25142: Fixed a memory issue in the ESV service.

### 23 May 2025

**Versions 17709.0, 17713.0**

#### Enhancements

* FRAAS-25205: Consolidated `End User UI`, `Login UI`, `Administrator Registration UI`, and `Administrator UI` status page components into a single `Administrator UI` component as they were all reporting the same service.

* OPENIDM-15771: You can now set locales in identity management scripts with the [`_locale` parameter](../tenants/email-send.html#email-send-post-params).

* OPENIDM-17680: Advanced Identity Cloud now supports enumerations in string and number attributes of its identity schema. To make an attribute an enumeration, add `"enum" : [ "one", "two", "three" ]` to the attribute. Advanced Identity Cloud requires create and update privileges to use one of the enumerated values.

* OPENIDM-19918: You can now choose whether synchronization detects identity array changes using \_ordered or *unordered* comparisons. Set the [`comparison`](../idm-synchronization/chap-implicit-live-sync.html#array-comparison) configuration property in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings. Relationship and virtual property array fields default to unordered comparisons. All other fields default to ordered comparisons.

* OPENIDM-20023: RCS communication with Advanced Identity Cloud can now use stricter authorization. Learn more in [Secure RCS access](../idm-auth/authorization-and-roles.html#secure-openicf-access) and [Migration dependent features](../product-information/migration-dependent-features.html).

#### Fixes

* OPENIDM-20995: Fixed an issue that prevented error reports during certain operations on groups or users. For example, trying to remove a non-existing attribute or null value now correctly results in an exception message to the client if these operations are not supported by the target system.

### 22 May 2025

**Version 17692.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 21 May 2025

**Version 17680.0**

#### Fixes

* FRAAS-25256: Fixed an issue that was causing missing data in analytics dashboards.

* OPENIDM-20995: Fixed an issue that prevented error reports during certain operations on groups or users. For example trying to remove a non-existing attribute or null value now correctly results in an exception message to the client if these operations are not supported by the target system.

### 15 May 2025

**Versions 17600.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 13 May 2025

**Versions 17581.0, 17584.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 12 May 2025

**Version 17570.0**

#### Enhancements

* OPENAM-23218: Legacy SAML 2.0 IDP attribute mapper scripts now have access to the 'httpClient' binding.

* OPENAM-23710: Legacy SAML 2.0 IDP adapter scripts now have access to the 'httpClient' binding.

### 09 May 2025

**Version 17553.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 08 May 2025

**Versions 17546.0, 17549.0**

#### Enhancements

* ANALYTICS-1004\[[4](#_footnotedef_4 "View footnote.")]: Support for custom attributes and relationships in the organization entity for advanced reports.

### 06 May 2025

**Versions 17513.0, 17514.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

### 05 May 2025

**Version 17507.0**

#### Fixes

* FRAAS-24990: Fixed an issue where requests to the `/monitoring/logs` and `/monitoring/logs/tail` endpoints timed out after 15 seconds rather than the expected 60 seconds.

### 02 May 2025

**Version 17488.0**

No customer-facing features, enhancements, or fixes released.\[[2](#_footnotedef_2 "View footnote.")]

***

[1](#_footnoteref_1). Requires WS-Federation/WS-Trust, which is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). This release focuses on internal improvements and technical updates to enhance the overall stability, performance, and maintainability of the platform. While there are no direct customer-facing changes, these updates lay the groundwork for future feature releases and improvements.[3](#_footnoteref_3). This change applies to a feature only available in PingOne Identity Governance, which is an [add-on capability](../product-information/add-on-capabilities.html) and must be purchased separately.[4](#_footnoteref_4). This change applies to a feature only available in Advanced Reporting, which is an [add-on capability](../product-information/add-on-capabilities.html) and must be purchased separately.[5](#_footnoteref_5). This issue was added to the changelog on September 4, 2025.[6](#_footnoteref_6). Proxy Connect is an [add-on capability](../product-information/add-on-capabilities.html).[7](#_footnoteref_7). [WS-Federation/WS-Trust](../app-management/register-a-custom-application.html#sso-microsoft-365) is an [add-on capability](../product-information/add-on-capabilities.html).[8](#_footnoteref_8). IGA is an [add-on capability](../product-information/add-on-capabilities.html).[9](#_footnoteref_9). A [sandbox environment](../tenants/environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[10](#_footnoteref_10). This issue was released on June 18, 2025 but inadvertently excluded from the changelog.

---

---
title: Rapid channel changelog archive
description: Archive of Advanced Identity Cloud rapid channel release notes published before May 2025, listing features, enhancements, and fixes by date
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel-changelog-archive
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel-changelog-archive.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  2022: 2022
  2023: 2023
  2024: 2024
  2025: 2025
  28_apr_2025: 28 Apr 2025
  24_apr_2025: 24 Apr 2025
  23_apr_2025: 23 Apr 2025
  enhancements: Enhancements
  fixes: Fixes
  22_apr_2025: 22 Apr 2025
  17_apr_2025: 17 Apr 2025
  fixes_2: Fixes
  16_apr_2025: 16 Apr 2025
  15_apr_2025: 15 Apr 2025
  14_apr_2025: 14 Apr 2025
  11_apr_2025: 11 Apr 2025
  fixes_3: Fixes
  10_apr_2025: 10 Apr 2025
  fixes_4: Fixes
  09_apr_2025: 09 Apr 2025
  fixes_5: Fixes
  08_apr_2025: 08 Apr 2025
  enhancements_2: Enhancements
  02_apr_2025: 02 Apr 2025
  key_features: Key Features
  enhancements_3: Enhancements
  01_apr_2025: 01 Apr 2025
  31_mar_2025: 31 Mar 2025
  28_mar_2025: 28 Mar 2025
  enhancements_4: Enhancements
  27_mar_2025: 27 Mar 2025
  26_mar_2025: 26 Mar 2025
  enhancements_5: Enhancements
  25_mar_2025: 25 Mar 2025
  24_mar_2025: 24 Mar 2025
  21_mar_2025: 21 Mar 2025
  key_features_2: Key Features
  enhancements_6: Enhancements
  fixes_6: Fixes
  20_mar_2025: 20 Mar 2025
  19_mar_2025: 19 Mar 2025
  18_mar_2025: 18 Mar 2025
  17_mar_2025: 17 Mar 2025
  key_features_3: Key Features
  enhancements_7: Enhancements
  fixes_7: Fixes
  14_mar_2025: 14 Mar 2025
  13_mar_2025: 13 Mar 2025
  10_mar_2025: 10 Mar 2025
  06_mar_2025: 06 Mar 2025
  27_feb_2025: 27 Feb 2025
  key_features_4: Key Features
  enhancements_8: Enhancements
  fixes_8: Fixes
  26_feb_2025: 26 Feb 2025
  25_feb_2025: 25 Feb 2025
  24_feb_2025: 24 Feb 2025
  21_feb_2025: 21 Feb 2025
  20_feb_2025: 20 Feb 2025
  key_features_5: Key features
  enhancements_9: Enhancements
  fixes_9: Fixes
  17_feb_2025: 17 Feb 2025
  13_feb_2025: 13 Feb 2025
  12_feb_2025: 12 Feb 2025
  10_feb_2025: 10 Feb 2025
  07_feb_2025: 07 Feb 2025
  06_feb_2025: 06 Feb 2025
  fixes_10: Fixes
  04_feb_2025: 04 Feb 2025
  enhancements_10: Enhancements
  fixes_11: Fixes
  03_feb_2025: 03 Feb 2025
  fixes_12: Fixes
  31_jan_2025: 31 Jan 2025
  30_jan_2025: 30 Jan 2025
  29_jan_2025: 29 Jan 2025
  27_jan_2025: 27 Jan 2025
  24_jan_2025: 24 Jan 2025
  enhancements_11: Enhancements
  23_jan_2025: 23 Jan 2025
  22_jan_2025: 22 Jan 2025
  21_jan_2025: 21 Jan 2025
  20_jan_2025: 20 Jan 2025
  enhancements_12: Enhancements
  fixes_13: Fixes
  17_jan_2025: 17 Jan 2025
  15_jan_2025: 15 Jan 2025
  enhancements_13: Enhancements
  14_jan_2025: 14 Jan 2025
  13_jan_2025: 13 Jan 2025
  10_jan_2025: 10 Jan 2025
  enhancements_14: Enhancements
  fixes_14: Fixes
  08_jan_2025: 08 Jan 2025
  06_jan_2025: 06 Jan 2025
  03_jan_2025: 03 Jan 2025
  03_jan_2025_2: 03 Jan 2025
  key_features_6: Key features
  enhancements_15: Enhancements
  fixes_15: Fixes
  21_dec_2024: 21 Dec 2024
  19_dec_2024: 19 Dec 2024
  fixes_16: Fixes
  18_dec_2024: 18 Dec 2024
  enhancements_16: Enhancements
  17_dec_2024: 17 Dec 2024
  enhancements_17: Enhancements
  rev3_16_dec_2024: 16 Dec 2024
  key_features_7: Key features
  enhancements_18: Enhancements
  fixes_17: Fixes
  03_dec_2024: 03 Dec 2024
  reversions: Reversions
  02_dec_2024: 02 Dec 2024
  key_features_8: Key features
  enhancements_19: Enhancements
  fixes_18: Fixes
  reversion_26_nov_2024: 26 Nov 2024
  reversions_2: Reversions
  25_nov_2024: 25 Nov 2024
  enhancements_20: Enhancements
  21-nov-2024: 21 Nov 2024
  key_features_9: Key features
  20-nov-2024: 20 Nov 2024
  key_features_10: Key features
  enhancements_21: Enhancements
  fixes_19: Fixes
  20_nov_2024: 20 Nov 2024
  19_nov_2024: 19 Nov 2024
  18_nov_2024: 18 Nov 2024
  15_nov_2024: 15 Nov 2024
  14_nov_2024: 14 Nov 2024
  enhancements_22: Enhancements
  11_nov_2024: 11 Nov 2024
  08_nov_2024: 08 Nov 2024
  07_nov_2024: 07 Nov 2024
  06_nov_2024: 06 Nov 2024
  key_features_11: Key features
  enhancements_23: Enhancements
  fixes_20: Fixes
  05_nov_2024: 05 Nov 2024
  04_nov_2024: 04 Nov 2024
  01_nov_2024: 01 Nov 2024
  31_oct_2024: 31 Oct 2024
  30_oct_2024: 30 Oct 2024
  29_oct_2024: 29 Oct 2024
  enhancements_24: Enhancements
  fixes_21: Fixes
  28_oct_2024: 28 Oct 2024
  25_oct_2024: 25 Oct 2024
  23_oct_2024: 23 Oct 2024
  22_oct_2024: 22 Oct 2024
  17_oct_2024: 17 Oct 2024
  16_oct_2024: 16 Oct 2024
  15_oct_2024: 15 Oct 2024
  14_oct_2024: 14 Oct 2024
  enhancements_25: Enhancements
  fixes_22: Fixes
  10_oct_2024: 10 Oct 2024
  07_oct_2024: 07 Oct 2024
  enhancements_26: Enhancements
  01_oct_2024: 01 Oct 2024
  enhancements_27: Enhancements
  30_sept_2024: 30 Sept 2024
  27_sept_2024: 27 Sept 2024
  26_sept_2024: 26 Sept 2024
  25_sept_2024: 25 Sept 2024
  24_sept_2024: 24 Sept 2024
  23_sept_2024: 23 Sept 2024
  20_sept_2024: 20 Sept 2024
  key_features_12: Key features
  enhancements_28: Enhancements
  fixes_23: Fixes
  16_sept_2024: 16 Sept 2024
  key_features_13: Key features
  enhancements_29: Enhancements
  fixes_24: Fixes
  13_sept_2024: 13 Sept 2024
  key_features_14: Key features
  fixes_25: Fixes
  11_sept_2024: 11 Sept 2024
  10_sept_2024: 10 Sept 2024
  09_sept_2024: 09 Sept 2024
  key_features_15: Key features
  enhancements_30: Enhancements
  fixes_26: Fixes
  06_sept_2024: 06 Sept 2024
  05_sept_2024: 05 Sept 2024
  03_sept_2024: 03 Sept 2024
  02_sept_2024: 02 Sept 2024
  30_aug_2024: 30 Aug 2024
  fixes_27: Fixes
  29_aug_2024: 29 Aug 2024
  key_features_16: Key features
  enhancements_31: Enhancements
  fixes_28: Fixes
  27_aug_2024: 27 Aug 2024
  26_aug_2024: 26 Aug 2024
  22_aug_2024: 22 Aug 2024
  21_aug_2024: 21 Aug 2024
  key_features_17: Key features
  enhancements_32: Enhancements
  19_aug_2024: 19 Aug 2024
  16_aug_2024: 16 Aug 2024
  14_aug_2024: 14 Aug 2024
  13_aug_2024: 13 Aug 2024
  12_aug_2024: 12 Aug 2024
  09_aug_2024: 09 Aug 2024
  08_aug_2024: 08 Aug 2024
  07_aug_2024: 07 Aug 2024
  06_aug_2024: 06 Aug 2024
  05_aug_2024: 05 Aug 2024
  02_aug_2024: 02 Aug 2024
  enhancements_33: Enhancements
  fixes_29: Fixes
  25_jul_2024: 25 Jul 2024
  24_jul_2024: 24 Jul 2024
  23_jul_2024: 23 Jul 2024
  22_jul_2024: 22 Jul 2024
  19_jul_2024: 19 Jul 2024
  key_features_18: Key features
  enhancements_34: Enhancements
  fixes_30: Fixes
  18_jul_2024: 18 Jul 2024
  17_jul_2024: 17 Jul 2024
  16_jul_2024: 16 Jul 2024
  15_jul_2024: 15 Jul 2024
  12_jul_2024: 12 Jul 2024
  fixes_31: Fixes
  11_jul_2024: 11 Jul 2024
  10_jul_2024: 10 Jul 2024
  09_jul_2024: 09 Jul 2024
  08_jul_2024: 08 Jul 2024
  fixes_32: Fixes
  05_jul_2024: 05 Jul 2024
  03_jul_2024: 03 Jul 2024
  02_jul_2024: 02 Jul 2024
  fixes_33: Fixes
  01_jul_2024: 01 Jul 2024
  fixes_34: Fixes
  27_jun_2024: 27 Jun 2024
  key_features_19: Key features
  fixes_35: Fixes
  changed_functionality: Changed functionality
  26_jun_2024: 26 Jun 2024
  25_jun_2024: 25 Jun 2024
  24_jun_2024: 24 Jun 2024
  key_features_20: Key features
  enhancements_35: Enhancements
  fixes_36: Fixes
  18_jun_2024: 18 Jun 2024
  key_features_21: Key features
  fixes_37: Fixes
  17_jun_2024: 17 Jun 2024
  14_jun_2024: 14 Jun 2024
  13_jun_2024: 13 Jun 2024
  12_jun_2024: 12 Jun 2024
  key_features_22: Key features
  enhancements_36: Enhancements
  fixes_38: Fixes
  05_jun_2024: 05 Jun 2024
  enhancements_37: Enhancements
  04_jun_2024: 04 Jun 2024
  update_03_jun_2024: 03 Jun 2024
  fixes_39: Fixes
  03_jun_2024: 03 Jun 2024
  fixes_40: Fixes
  22_may_2024: 22 May 2024
  key_features_23: Key features
  enhancements_38: Enhancements
  21_may_2024: 21 May 2024
  enhancements_39: Enhancements
  20_may_2024: 20 May 2024
  key_features_24: Key features
  enhancements_40: Enhancements
  16_may_2024: 16 May 2024
  15_may_2024: 15 May 2024
  14_may_2024: 14 May 2024
  13_may_2024: 13 May 2024
  10_may_2024: 10 May 2024
  07_may_2024: 07 May 2024
  06_may_2024: 06 May 2024
  03_may_2024: 03 May 2024
  key_features_25: Key features
  enhancements_41: Enhancements
  fixes_41: Fixes
  01_may_2024: 01 May 2024
  30_apr_2024: 30 Apr 2024
  29_apr_2024: 29 Apr 2024
  26_apr_2024: 26 Apr 2024
  25_apr_2024: 25 Apr 2024
  24_apr_2024: 24 Apr 2024
  fixes_42: Fixes
  23_apr_2024: 23 Apr 2024
  22_apr_2024: 22 Apr 2024
  fixes_43: Fixes
  18_apr_2024: 18 Apr 2024
  fixes_44: Fixes
  17_apr_2024: 17 Apr 2024
  key_features_26: Key features
  enhancements_42: Enhancements
  fixes_45: Fixes
  rev1_12_apr_2024: 12 Apr 2024
  fixes_46: Fixes
  11_apr_2024: 11 Apr 2024
  enhancements_43: Enhancements
  09_apr_2024: 09 Apr 2024
  key_features_27: Key features
  08_apr_2024: 08 Apr 2024
  04_apr_2024: 04 Apr 2024
  02_apr_2024: 02 Apr 2024
  enhancements_44: Enhancements
  01_apr_2024: 01 Apr 2024
  29_mar_2024: 29 Mar 2024
  28_mar_2024: 28 Mar 2024
  27_mar_2024: 27 Mar 2024
  26_mar_2024: 26 Mar 2024
  key_features_28: Key features
  enhancements_45: Enhancements
  fixes_47: Fixes
  25_mar_2024: 25 Mar 2024
  22_mar_2024: 22 Mar 2024
  enhancements_46: Enhancements
  21_mar_2024: 21 Mar 2024
  key_features_29: Key features
  enhancements_47: Enhancements
  19_mar_2024: 19 Mar 2024
  18_mar_2024: 18 Mar 2024
  enhancements_48: Enhancements
  15_mar_2024: 15 Mar 2024
  key_features_30: Key features
  14_mar_2024: 14 Mar 2024
  13_mar_2024: 13 Mar 2024
  key_features_31: Key features
  enhancements_49: Enhancements
  08_mar_2024: 08 Mar 2024
  04_mar_2024: 04 Mar 2024
  02_mar_2024: 02 Mar 2024
  enhancements_50: Enhancements
  fixes_48: Fixes
  01_mar_2024: 01 Mar 2024
  29_feb_2024: 29 Feb 2024
  enhancements_51: Enhancements
  fixes_49: Fixes
  28_feb_2024: 28 Feb 2024
  enhancements_52: Enhancements
  15_feb_2024: 15 Feb 2024
  fixes_50: Fixes
  12_feb_2024: 12 Feb 2024
  enhancements_53: Enhancements
  07_feb_2024: 07 Feb 2024
  fixes_51: Fixes
  06_feb_2024: 06 Feb 2024
  fixes_52: Fixes
  25_jan_2024: 25 Jan 2024
  fixes_53: Fixes
  24_jan_2024: 24 Jan 2024
  enhancements_54: Enhancements
  fixes_54: Fixes
  23_jan_2024: 23 Jan 2024
  key_features_32: Key features
  22_jan_2024_supplementary: 22 Jan 2024 (supplementary)
  key_features_33: Key features
  enhancements_55: Enhancements
  fixes_55: Fixes
  22_jan_2024: 22 Jan 2024
  enhancements_56: Enhancements
  fixes_56: Fixes
  19_jan_2024: 19 Jan 2024
  key_features_34: Key features
  18_jan_2024: 18 Jan 2024
  key_features_35: Key features
  enhancements_57: Enhancements
  fixes_57: Fixes
  17_jan_2024: 17 Jan 2024
  fixes_58: Fixes
  09_jan_2024: 09 Jan 2024
  fixes_59: Fixes
  19_dec_2023: 19 Dec 2023
  key_features_36: Key features
  enhancements_58: Enhancements
  fixes_60: Fixes
  15_dec_2023: 15 Dec 2023
  fixes_61: Fixes
  12_dec_2023: 12 Dec 2023
  enhancements_59: Enhancements
  fixes_62: Fixes
  11_dec_2023: 11 Dec 2023
  fixes_63: Fixes
  30_nov_2023: 30 Nov 2023
  fixes_64: Fixes
  notices: Notices
  28_nov_2023: 28 Nov 2023
  key_features_37: Key features
  27_nov_2023: 27 Nov 2023
  enhancements_60: Enhancements
  fixes_65: Fixes
  17_nov_2023: 17 Nov 2023
  enhancements_61: Enhancements
  fixes_66: Fixes
  13_nov_2023: 13 Nov 2023
  fixes_67: Fixes
  31_oct_2023: 31 Oct 2023
  key_features_38: Key features
  enhancements_62: Enhancements
  fixes_68: Fixes
  19_oct_2023: 19 Oct 2023
  key_features_39: Key features
  16_oct_2023: 16 Oct 2023
  key_features_40: Key features
  enhancements_63: Enhancements
  fixes_69: Fixes
  13_oct_2023: 13 Oct 2023
  enhancements_64: Enhancements
  fixes_70: Fixes
  12_oct_2023: 12 Oct 2023
  key_features_41: Key features
  03_oct_2023: 03 Oct 2023
  fixes_71: Fixes
  25_sep_2023: 25 Sep 2023
  enhancements_65: Enhancements
  fixes_72: Fixes
  22_sep_2023: 22 Sep 2023
  fixes_73: Fixes
  20_sep_2023: 20 Sep 2023
  key_features_42: Key features
  enhancements_66: Enhancements
  fixes_74: Fixes
  19_sep_2023: 19 Sep 2023
  enhancements_67: Enhancements
  15_sep_2023: 15 Sep 2023
  key_features_43: Key features
  enhancements_68: Enhancements
  fixes_75: Fixes
  11_sep_2023: 11 Sep 2023
  enhancements_69: Enhancements
  fixes_76: Fixes
  06_sep_2023: 06 Sep 2023
  enhancements_70: Enhancements
  22_aug_2023: 22 Aug 2023
  key_features_44: Key features
  18_aug_2023: 18 Aug 2023
  key_features_45: Key features
  14_aug_2023: 14 Aug 2023
  fixes_77: Fixes
  09_aug_2023: 09 Aug 2023
  enhancements_71: Enhancements
  fixes_78: Fixes
  31_jul_2023: 31 Jul 2023
  enhancements_72: Enhancements
  fixes_79: Fixes
  25_jul_2023: 25 Jul 2023
  fixes_80: Fixes
  17_jul_2023: 17 Jul 2023
  fixes_81: Fixes
  13_jul_2023: 13 Jul 2023
  fixes_82: Fixes
  26_jun_2023: 26 Jun 2023
  fixes_83: Fixes
  22_jun_2023: 22 Jun 2023
  enhancements_73: Enhancements
  fixes_84: Fixes
  19_jun_2023: 19 Jun 2023
  enhancements_74: Enhancements
  16_jun_2023: 16 Jun 2023
  fixes_85: Fixes
  14_jun_2023: 14 Jun 2023
  key_features_46: Key features
  enhancements_75: Enhancements
  fixes_86: Fixes
  13_jun_2023: 13 Jun 2023
  fixes_87: Fixes
  08_jun_2023: 08 Jun 2023
  key_features_47: Key features
  fixes_88: Fixes
  05_jun_2023: 05 Jun 2023
  key_features_48: Key features
  fixes_89: Fixes
  30_may_2023: 30 May 2023
  key_features_49: Key features
  fixes_90: Fixes
  24_may_2023: 24 May 2023
  fixes_91: Fixes
  23_may_2023: 23 May 2023
  fixes_92: Fixes
  18_may_2023: 18 May 2023
  key_features_50: Key features
  enhancements_76: Enhancements
  17_may_2023: 17 May 2023
  fixes_93: Fixes
  15_may_2023: 15 May 2023
  fixes_94: Fixes
  05_may_2023: 05 May 2023
  fixes_95: Fixes
  04_may_2023: 04 May 2023
  fixes_96: Fixes
  03_may_2023: 03 May 2023
  fixes_97: Fixes
  26_apr_2023: 26 Apr 2023
  key_features_51: Key features
  resolved_issues: Resolved issues
  25_apr_2023: 25 Apr 2023
  resolved_issues_2: Resolved issues
  24_apr_2023: 24 Apr 2023
  key_features_52: Key features
  resolved_issues_3: Resolved issues
  12_apr_2023: 12 Apr 2023
  resolved_issues_4: Resolved issues
  06_apr_2023: 06 Apr 2023
  key_features_53: Key features
  resolved_issues_5: Resolved issues
  30_mar_2023: 30 Mar 2023
  key_features_54: Key features
  resolved_issues_6: Resolved issues
  29_mar_2023: 29 Mar 2023
  resolved_issues_7: Resolved issues
  27_mar_2023: 27 Mar 2023
  resolved_issues_8: Resolved issues
  20_mar_2023: 20 Mar 2023
  resolved_issues_9: Resolved issues
  17_mar_2023: 17 Mar 2023
  resolved_issues_10: Resolved issues
  16_mar_2023: 16 Mar 2023
  key_features_55: Key features
  resolved_issues_11: Resolved issues
  15_mar_2023: 15 Mar 2023
  resolved_issues_12: Resolved issues
  13_mar_2023: 13 Mar 2023
  resolved_issues_13: Resolved issues
  10_mar_2023: 10 Mar 2023
  key_features_56: Key features
  resolved_issues_14: Resolved issues
  08_mar_2023: 08 Mar 2023
  key_features_57: Key features
  resolved_issues_15: Resolved issues
  06_mar_2023: 06 Mar 2023
  resolved_issues_16: Resolved issues
  03_mar_2023: 03 Mar 2023
  key_features_58: Key features
  resolved_issues_17: Resolved issues
  01_mar_2023: 01 Mar 2023
  28_feb_2023: 28 Feb 2023
  resolved_issues_18: Resolved issues
  22_feb_2023: 22 Feb 2023
  resolved_issues_19: Resolved issues
  16_feb_2023: 16 Feb 2023
  resolved_issues_20: Resolved issues
  14_feb_2023: 14 Feb 2023
  key_features_59: Key features
  resolved_issues_21: Resolved issues
  13_feb_2023: 13 Feb 2023
  resolved_issues_22: Resolved issues
  09_feb_2023: 09 Feb 2023
  key_features_60: Key features
  resolved_issues_23: Resolved issues
  31_jan_2023: 31 Jan 2023
  resolved_issues_24: Resolved issues
  30_jan_2023: 30 Jan 2023
  resolved_issues_25: Resolved issues
  27_jan_2023: 27 Jan 2023
  resolved_issues_26: Resolved issues
  26_jan_2023: 26 Jan 2023
  resolved_issues_27: Resolved issues
  25_jan_2023: 25 Jan 2023
  key_features_61: Key features
  resolved_issues_28: Resolved issues
  13_jan_2023: 13 Jan 2023
  key_features_62: Key features
  resolved_issues_29: Resolved issues
  11_jan_2023: 11 Jan 2023
  resolved_issues_30: Resolved issues
  04_jan_2023: 04 Jan 2023
  resolved_issues_31: Resolved issues
  21_dec_2022: 21 Dec 2022
  resolved_issues_32: Resolved issues
  20_dec_2022: 20 Dec 2022
  key_features_63: Key features
  resolved_issues_33: Resolved issues
  16_dec_2022: 16 Dec 2022
  resolved_issues_34: Resolved issues
  15_dec_2022: 15 Dec 2022
  resolved_issues_35: Resolved issues
  09_dec_2022: 09 Dec 2022
  key_features_64: Key features
  resolved_issues_36: Resolved issues
  08_dec_2022: 08 Dec 2022
  resolved_issues_37: Resolved issues
  07_dec_2022: 07 Dec 2022
  resolved_issues_38: Resolved issues
  06_dec_2022: 06 Dec 2022
  key_features_65: Key features
  resolved_issues_39: Resolved issues
  29_nov_2022: 29 Nov 2022
  key_features_66: Key features
  resolved_issues_40: Resolved issues
  23_nov_2022: 23 Nov 2022
  resolved_issues_41: Resolved issues
  22_nov_2022: 22 Nov 2022
  resolved_issues_42: Resolved issues
  18_nov_2022: 18 Nov 2022
  resolved_issues_43: Resolved issues
  10_nov_2022: 10 Nov 2022
  resolved_issues_44: Resolved issues
  08_nov_2022: 08 Nov 2022
  key_features_67: Key features
  resolved_issues_45: Resolved issues
  02_nov_2022: 02 Nov 2022
  key_features_68: Key features
  resolved_issues_46: Resolved issues
  25_oct_2022: 25 Oct 2022
  key_features_69: Key features
  resolved_issues_47: Resolved issues
  19_oct_2022: 19 Oct 2022
  key_features_70: Key features
  resolved_issues_48: Resolved issues
  18_oct_2022: 18 Oct 2022
  resolved_issues_49: Resolved issues
  07_oct_2022: 07 Oct 2022
  resolved_issues_50: Resolved issues
  03_oct_2022: 03 Oct 2022
  resolved_issues_51: Resolved issues
  22_sep_2022: 22 Sep 2022
  resolved_issues_52: Resolved issues
  20_sep_2022: 20 Sep 2022
  resolved_issues_53: Resolved issues
---

# Rapid channel changelog archive

## 2025

### 28 Apr 2025

**Versions 17434.0, 17436.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Apr 2025

**Version 17395.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 23 Apr 2025

**Version 17384.0**

#### Enhancements

* IAM-987: Added support for [enums](../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to hosted account pages.

* IAM-1116: Added support for [enums](../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to the Advanced Identity Cloud admin console.

* IAM-2103: Added support for [enums](../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to hosted journey pages.

* IAM-6822: Added the ability to manage cookie domains in the Advanced Identity Cloud admin console.

* IAM-7412: Updated the password policy feature in the Advanced Identity Cloud admin console. Added the ability to specify a minimum substring length between 3 - 64 to use when validating passwords against user attribute values. The default is still 5 characters, but can now be reduced to as few as 3 characters to catch shorter string matches.

* IAM-7794\[[2](#_footnotedef_2 "View footnote.")]: Added support for using custom identity objects in the form builder.

* IAM-7919: Improved color contrast ratio of the **Delete Account** button text when focused.

* IAM-7934: Improved color contrast ratio of date fields when focused.

* IAM-7957: Improved color contrast ratio of the **Deselect** button text when focused.

* IAM-7966: Improved color contrast ratio of **In Progress** text.

* IAM-8016\[[2](#_footnotedef_2 "View footnote.")]: Allow form authors to specify a user filter when dynamic enums are selected.

* IAM-8085: Updated the **Add a Parameter** reports modal to use entity attributes for input.

#### Fixes

* FRAAS-15518: Fixed issue that prevented localization of **Session timed out** message in certain locales.

* IAM-5834: Fixed a double-encoding issue in the SAML app that affected IdP-initiated sign on.

* IAM-6796: Jobs are now prevented from being scheduled with frequencies that cause invalid date errors.

* IAM-7855: Fixed a typo in the help text returned when there are no results to display.

* IAM-8237: Corrected floating labels in the date picker in the hosted journey pages.

* IAM-8361: The **Save** button in the **Edit Bookmark** application is now inactive while checking if the ESV exists.

* IAM-8364: Fixed issues in SAML end-to-end scenarios.

* IAM-8378: Fixed an issue that stripped HTML elements from email templates.

* IAM-8403: Fixed border focus location and floating label issues in **Tag** fields.

* IAM-8434: Fixed an issue that prevented duplication of new themes that contain special characters.

### 22 Apr 2025

**Version 17363.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 17 Apr 2025

**Versions 17317.0**

#### Fixes

* FRAAS-24449: Enhanced the reliability of metrics collection under high-load conditions.

### 16 Apr 2025

**Versions 17283.0, 17299.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 15 Apr 2025

**Version 17269.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 14 Apr 2025

**Version 17255.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 11 Apr 2025

**Version 17238.0**

#### Fixes

* FRAAS-24631: Fixed a promotions issue where ESVs mapped to secret labels aren't identified as available in the upper environment.

### 10 Apr 2025

**Version 17210.0**

#### Fixes

* FRAAS-24648: Fixed an issue with loading ESVs with values containing leading blank spaces.

* IAM-7202: In the custom application modal, the native apps link now correctly points to the SDKs documentation.

### 09 Apr 2025

**Versions 17190.0, 17194.0**

#### Fixes

* FRAAS-24646: Fixed an issue where ESVs mapped to AM secret labels could block configuration promotions.

### 08 Apr 2025

**Versions 17178.0, 17186.0**

#### Enhancements

* OPENDJ-11175: The password validation mechanism has been enhanced to include checks for attribute values shorter than the `min-substring-length` (the default is 5).

  For example, if the password contains `Bob` for a user named Bob, the password is rejected, even if `min-substring-length` is set to 5.

### 02 Apr 2025

**Version 17111.0**

#### Key Features

* FRAAS-24546: Tenant-auditor role temporarily disabled in the Advanced Identity Cloud admin console.

#### Enhancements

* AME-31141: Multiple Java libraries added to SAML SP Adapter scripting allowlist.

### 01 Apr 2025

**Version 17106.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 31 Mar 2025

**Version 17090.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 28 Mar 2025

**Versions 17072.0, 17079.0**

#### Enhancements

* ANALYTICS-846: You can now select the attribute type and value for report entity attributes.

* ANALYTICS-983\[[3](#_footnotedef_3 "View footnote.")]: You can now use regular expression operators in Advanced Reporting.

### 27 Mar 2025

**Versions 17055.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 26 Mar 2025

**Versions 17041.0, 17046.0**

#### Enhancements

* OPENAM-23718: Added additional Java classes to the SAML 2.0 SP adapter scripting allowlist.

### 25 Mar 2025

**Version 17034.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Mar 2025

**Versions 17031.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 21 Mar 2025

#### Key Features

* Custom attributes for user entity in Advanced Reports (ANALYTICS-863)\[[3](#_footnotedef_3 "View footnote.")]\[[4](#_footnotedef_4 "View footnote.")]

  When a tenant administrator modifies the `users` identity object from the native console and adds a new custom attribute, the attribute is immediately available on the Create Report page. Administrators can use the custom attribute for their reports and filters.

  Learn more in [Custom attributes for user objects](../reports/use-cases/custom-attributes-for-user-in-advanced-reports.html).

#### Enhancements

* ANALYTICS-770\[[3](#_footnotedef_3 "View footnote.")]\[[4](#_footnotedef_4 "View footnote.")]: Add IN and CONTAINS operators for filtering in Advanced Reporting.

#### Fixes

* FRAAS-24435: Fixed an issue with the `pagedResultsCookie` that prevented some customers from retrieving logs.

### 20 Mar 2025

**Versions 17002.0, 17015.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 19 Mar 2025

**Versions 16981.0, 16989.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 18 Mar 2025

**Version 16955.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 17 Mar 2025

**Version 16940.0**

#### Key Features

* Tenant auditors (IAM-8086)

  Advanced Identity Cloud now lets you invite tenant auditors to access the Advanced Identity Cloud admin console. Tenant auditors can view settings, configuration, and data but cannot modify them.

#### Enhancements

* IAM-6996: Added the ability to create a specific OAuth 2.0 client when creating a connector server, rather than relying on the default **RCSClient**.

* IAM-7109: You can now use an ESV to set the **From Address** in the email provider configuration.

* IAM-7827/ANALYTICS-835\[[3](#_footnotedef_3 "View footnote.")]: In the analytics report editor in Advanced Reporting, you can now reorder columns by dragging and dropping them.

* IAM-7841/ANALYTICS-840\[[3](#_footnotedef_3 "View footnote.")]: The reports page in Advanced Reporting is now a list view with pagination and search.

* IAM-8321: In the journey editor, the node titles now wrap within the left nodes panel.

#### Fixes

* IAM-1504: User no longer needs to click the cancel button twice in some journey dialogs.

* IAM-8111: Schedules can no longer be disabled when running.

### 14 Mar 2025

**Version 16919.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 13 Mar 2025

**Version 16885.0, 16887.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 Mar 2025

**Version 16846.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 06 Mar 2025

**Version 16832.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 27 Feb 2025

**Version 16747.0**

#### Key Features

* Flow Control node (AME-30017)

  You can now randomly direct users down different journey paths. Learn more in [Flow Control node](https://docs.pingidentity.com/auth-node-ref/latest/flow-control.html).

* OIDC application journeys (AME-28650)

  You can now configure OAuth 2.0 / OIDC client applications to redirect authentication requests to a specified journey. Learn more in [Client application journeys](../am-oauth2/oauth2-register-client.html#oauth2app-journey).

#### Enhancements

* AME-27705: Extend the `utils` binding for all next-generation scripts to support low-level cryptographic operations. These operations include encryption, decryption, hashing, signing, verification, and key generation.

  Find more information in [Access utility functions](../am-scripting/script-bindings.html#common-utils).

* AME-28780: Added an IDM policy condition that can assert conditions against an IDM resource type such as user identities.

* AME-28954: Modified the import metadata endpoint to support updating signing and encryption certificates for existing SAML service providers (SPs) without requiring the deletion or recreation of SP configurations.

* AME-29307: You can now use DER-encoded certificates for OAuth 2.0 client authentication.

* AME-29810: The realm default authentication service can no longer be a journey with `mustRun` enabled. Also, `mustRun` can no longer be enabled on journeys that are set as the realm default authentication service.

* AME-29835: Configuration Provider Node scripts can now use the next-generation scripting engine, which gives them access to common bindings such as `openidm` and `httpClient`.

* AME-30076: New `getApplicationId()` method provides a consistent way to retrieve the application ID from both SAML and OAuth 2.0 applications.

#### Fixes

* AME-29504: The `scriptName` and `logger` bindings in library scripts referenced the same default script name and ID. Their previous behavior has now been restored by inheriting values from the referencing script.

* AME-29965: The Configuration Provider node now works with the Inner Tree Evaluator for nested inner journeys.

* AME-30377: The following two warning level log messages have been reduced to debug level because they're rarely useful and appear frequently, drowning out more useful log entries:

  * `No users have been identified.`

  * `Ignoring the new universal id as that is empty and the current universal id is already set.`

* OPENAM-22120: Back-channel logout tokens now include the `exp` claim.

* OPENAM-23077: The `access_token` endpoint now responds with the correct error code when the `code_verifier` isn't supplied (for example, `invalid_grant`).

### 26 Feb 2025

**Version 16726.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 25 Feb 2025

**Version 16713.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Feb 2025

**Version 16704.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 21 Feb 2025

**Version 16686.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 20 Feb 2025

**Version 16676.0**

#### Key features

* [Advanced sync](../app-management/provision-an-application.html) (IAM-8090)

  Many of the mapping synchronization features available in the IDM admin console are now exposed in the Advanced Sync tab when viewing an application. You can create additional mappings between applications or between applications and identity profiles.

#### Enhancements

* IAM-7967\[[2](#_footnotedef_2 "View footnote.")]: Added an image description for the approvals **Low Priority** icon.

* IAM-7977: Improved the font color contrast ratio of the email address displayed in Advanced Identity Cloud admin console user profiles.

* IAM-8053: The Advanced Identity Cloud end-user UI can now use `defaultText` value as a fallback value when the actual value of a field returns empty.

* OPENIDM-20139: Applications can now use `postAction` scripts for the `ONBOARD` action.

#### Fixes

* IAM-7719\[[2](#_footnotedef_2 "View footnote.")]: Users are now redirected back to the compliance **Policy Rules** tab after creating or editing a policy rule.

### 17 Feb 2025

**Version 16639.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 13 Feb 2025

**Version 16583.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 12 Feb 2025

**Version 16577.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 Feb 2025

**Version 16552.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 07 Feb 2025

**Version 16538.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 06 Feb 2025

**Version 16526.0**

#### Fixes

* FRAAS-23812: You can now deactivate the header ruleset after deactivating the IP ruleset when configuring Proxy Connect.

### 04 Feb 2025

**Version 16508.0**

#### Enhancements

* IAM-4692: Managed identity boolean fields now use a checkbox instead of a toggle.

* IAM-6581: [SAML 2.0 application journeys](../am-saml2/configure-providers.html#samlapp-journey) can now be configured in the Advanced Identity Cloud admin console.

* IAM-7248\[[2](#_footnotedef_2 "View footnote.")]: In IGA sources, the `displayName` and `logo` can now be obtained from the CDN.

* IAM-7874\[[2](#_footnotedef_2 "View footnote.")]: The **Governance > Requests > Settings** tab now lets you activate or deactivate Governance LCM.

#### Fixes

* IAM-1262: Clicking the **Toggle Sidebar** button now collapses the sidebar.

* IAM-5801: For applications that mandate a minimum page size, the page size selector on the **Data** tab and the **Reconciliation Results** tab has been removed.

### 03 Feb 2025

**Version 16492.0**

#### Fixes

* FRAAS-23780: Optimized network utilization to distribute workloads more effectively.

### 31 Jan 2025

**Versions 16460.0, 16466.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 30 Jan 2025

**Version 16450.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 29 Jan 2025

**Versions 16437.0, 16441.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 27 Jan 2025

**Version 16419.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Jan 2025

**Versions 16410.0, 16412.0**

#### Enhancements

* FRAAS-23002: Improvements to OATH support for MFA authenticators

  * Update the default OATH shared secret length from 32 to 40 for existing and new tenants so that tenant administrators can use Google Authenticator with MFA when signing on using their Advanced Identity Cloud native accounts.

  * Make the OATH shared secret length configurable (using a support request) to support other MFA authenticators.

### 23 Jan 2025

**Versions 16386.0, 16388.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 22 Jan 2025

**Versions 16368.0, 16376.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 21 Jan 2025

**Version 16355.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 20 Jan 2025

**Versions 16345.0, 16348.0**

#### Enhancements

* IAM-7454: The inbound mapping for all application templates and scripted application templates has now been configured to make fewer connector requests.

#### Fixes

* IAM-5242: The **Previous** link in the **New Script** modal now always shows the previous step.

* IAM-7799: Identity attributes with `Time` and `DateTime` format now trigger change events only when a change occurs.

### 17 Jan 2025

**Version 16330.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 15 Jan 2025

**Versions 16294.0, 16297.0**

#### Enhancements

* FRAAS-23375: You can now obtain the HTTP client location from the `X-Client-City` & `X-Client-City-Lat-Long` HTTP headers in Advanced Identity Cloud scripts and journeys.

  `X-Client-City` contains the name of the city from which the request originated, for example, `Mountain View` for Mountain View, California. There is no canonical list of valid values for this variable. The city names can contain US-ASCII letters, numbers, spaces, and the following characters: ``"!#$%&'*+-.^_`|~"``.

  `X-Client-City-Lat-Long` contains the latitude and longitude of the city from which the request originated, for example, `37.386051,-122.083851` for a request from Mountain View.

### 14 Jan 2025

**Versions 16276.0, 16278.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 13 Jan 2025

**Version 16256.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 Jan 2025

**Versions 16216.0, 16229.0**

#### Enhancements

* IAM-6833: Made existing synchronization tokens editable for incremental reconciliations.

* IAM-7223\[[2](#_footnotedef_2 "View footnote.")]: Added the ability to set user, role, organization, application, or entitlement objects to provide predefined values for select and multiselect fields in request forms.

#### Fixes

* IAM-5482: Password policy no longer allows **Password length** to be set as an empty string.

### 08 Jan 2025

**Version 16166.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 06 Jan 2025

**Version 16139.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 03 Jan 2025

**Version 16128.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 03 Jan 2025

**Version 15989.0**

#### Key features

* Reports for IGA data sources (ANALYTICS-571)\[[5](#_footnotedef_5 "View footnote.")]

  Advanced Reporting\[[6](#_footnotedef_6 "View footnote.")] now supports various IGA\[[7](#_footnotedef_7 "View footnote.")] data sources and relationships. This lets IGA administrators create customer-friendly report templates.

#### Enhancements

* ANALYTICS-459\[[5](#_footnotedef_5 "View footnote.")]: Report query data is now retained for 30 days for customers using OOTB reports and 90 days for customers with Advanced Reporting\[[6](#_footnotedef_6 "View footnote.")].

* ANALYTICS-495\[[5](#_footnotedef_5 "View footnote.")]: Replace `email` with `username` in **User Last Login** report.

* ANALYTICS-817\[[5](#_footnotedef_5 "View footnote.")]\[[3](#_footnotedef_3 "View footnote.")]: Report authors can now query on "Password Last Changed Time" for user entity.

* ANALYTICS-818\[[5](#_footnotedef_5 "View footnote.")]\[[3](#_footnotedef_3 "View footnote.")]: Report authors can now query on "Password Expiration Time" for user entity.

#### Fixes

* ANALYTICS-474\[[5](#_footnotedef_5 "View footnote.")]: The **User Journey Stats** report now provides aggregates by outcome in the report result when more than one outcome is selected.

* ANALYTICS-837\[[5](#_footnotedef_5 "View footnote.")]: The **User Count by Status** report now provides aggregates by status in the report result when more than one outcome is selected

* ANALYTICS-585\[[5](#_footnotedef_5 "View footnote.")]\[[3](#_footnotedef_3 "View footnote.")]: Remove **Report Admin** and **Report Owner** group selection when creating a new report.

## 2024

### 21 Dec 2024

**Version 16100.0**

### 19 Dec 2024

**Version 16070.0**

#### Fixes

* AME-29504: Fixed issue with script names not displaying in next-generation script logs.

### 18 Dec 2024

**Version 16056.0**

#### Enhancements

* OPENIDM-20542: Added a feature service named `am/2fa/profiles` to expose certain multi-factor attributes on `alpha` and `bravo` users.

### 17 Dec 2024

**Version 16028.0**

#### Enhancements

* OPENDJ-9287: The password validation mechanism has been enhanced to include checks for portions of attribute values within passwords. This improvement ensures that even partial matches between portions of passwords and portions of attribute values are identified and restricted, thereby enhancing security.

  For example, if the password is `abcdef` and the attribute value is `abcdef123`, the password is rejected. Similarly, if the password is `abcdefAZERTY` and the attribute value is `abcdef123`, the password is rejected.

### 16 Dec 2024

**Version 15989.0**

This release reintroduces many features, enhancements, and fixes previously present in reverted versions.

#### Key features

* [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html) (TNTP-183)

  Use this node to send a decision request to a specified decision endpoint in your PingOne Authorize environment.

* PingOne node improvements (SDKS-3468)

  * PingOne Create, Identify, and Delete Nodes

    The following PingOne nodes are now available:

    * [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html)

      Use the PingOne Identity Match node to identify if a user exists both in the user repository and in PingOne, using defined attributes.

    * [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html)

      Create new users in the PingOne platform using the PingOne Create User node. Create users based on an existing user's properties or choose to create the user anonymously. For example, when used in conjunction with PingOne Verify.

    * [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html)

      Delete users from the PingOne platform with the PingOne Delete User node.

  * PingOne Verify nodes

    Use the following PingOne Verify nodes in conjunction with the [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html), [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html), and [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html) to create a seamless verification process in your journey:

    * [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html)

      Leverage PingOne Verify to initiate or continue a verification transaction with the PingOne Verify Evaluation Node.

    * [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html)

      Determine the completion status of the most recent identity verification transaction for an end user.

      Use before the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) to determine the status of the verification process or after the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) using a script to evaluate the transaction.

      For example, you can evaluate if the transaction was completed using a passport and route your journey accordingly.

  |   |                                                                   |
  | - | ----------------------------------------------------------------- |
  |   | Use these nodes in place of the PingOne Verify Marketplace nodes. |

* reCAPTCHA Enterprise node (SDKS-3322)

  The [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html) node adds Google reCAPTCHA Enterprise support to your journeys.

* SAML application journeys (AME-27850)

  Added support for SAML application journeys with a new setting on the remote SP. Configure a specific authentication journey that always runs for users authenticating with your SAML 2.0 app, regardless of existing sessions or configured authentication context.

  Learn more in [Configure a SAML 2.0 application journey](../am-saml2/configure-providers.html#samlapp-journey).

* Set Failure Details node (AME-27871)

  Use the [Set Failure Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-failure-details.html) to configure a localized error message on journey failure. You can also configure extra details in the response body of the failure request.

* Set Success Details node (OPENAM-12335)

  Use the [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-success-details.html) to add additional details to the success response of a journey.

* UI support for managing certificates (IAM-5813)

  You can now use the Advanced Identity Cloud admin console to generate CSRs and upload SSL certificates in your tenant environments.

  Learn more in [Manage server certificates using the admin console](../realms/server-certificates-ui.html).

#### Enhancements

* AME-26050: You can now create Next-generation Policy Condition scripts that have access to all common bindings, such as `openidm` and `httpClient`. Additionally, some existing bindings have been wrapped to improve usability in scripts.

* AME-28228: OAuth 2.0 audit logs now include the OAuth 2.0 client ID and any journey associated with the client.

* AME-29009: When using the new FIDO Metadata Service, if you link to the FIDO metadata using a URL, Advanced Identity Cloud periodically downloads and updates the latest FIDO metadata based on the `nextUpdate` date specified in the downloaded data.

* AME-29093: Added configuration for integration with WebAuthn Metadata Services (such as the FIDO Metadata Service). This includes a realm-level WebAuthn Metadata service and a new FIDO Certification Level configuration attribute in the WebAuthn Registration Node.

* FRAAS-22321: You can now obtain the HTTP client location from the `X-Client-Region` HTTP header within your scripts and journeys. The `X-Client-Region` header contains the country (or region) associated with the client's IP address in the form of a Unicode CLDR region code, such as `US` or `FR`. For most countries, these codes correspond directly to ISO-3166-2 codes.

* FRAAS-23073: The SAML scripting adapter now lets scripts access `org.forgerock.http.protocol.*`.

* IAM-3323: You can now use XPath transformation functions with additional [Workday application template](../app-management/provision-an-application.html#provision-workday) attributes.

* IAM-4540: You can now change the border color of a selected input field in journey and end-user pages.

* IAM-6397: The Advanced Identity Cloud admin console now lets you page through the list of OAuth 2.0 client profiles.

* OPENAM-23109: During a WebAuthn registration flow, if Store data in transient state is enabled, the Authenticator Attestation Global Unique Identifier (AAGUID) is now added to the node state under the `webauthnData` key.

#### Fixes

* AME-28016: When an invalid redirect URI is provided to the `/par` endpoint, the URI mismatch error is now `redirect_uri_mismatch` instead of `invalid_request`.

* AME-28017: Advanced Identity Cloud now accepts the requested OAuth 2.0 endpoint as a valid JWT audience claim, as per [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519.html#section-4.1.3) and [RFC 9126](https://www.rfc-editor.org/rfc/rfc9126.html#section-2).

* AME-29170: On [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html) login failure, stack traces are now logged at `debug` level.

* AME-29965: The [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html) now works with the [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html) for nested inner journeys.

* IAM-1782: Long gateway and agent IDs no longer overflow in the Advanced Identity Cloud admin console.

* IAM-7523\[[2](#_footnotedef_2 "View footnote.")]: A user receiving a forwarded fulfillment task now has permission to approve or reject the task.

* IAM-7537\[[2](#_footnotedef_2 "View footnote.")]: Governance functionality is now only shown for the `alpha` realm.

* IAM-7689\[[2](#_footnotedef_2 "View footnote.")]: The Advanced Identity Cloud admin console now displays the Assigned To value in the task list for a user assigned to a role who receives a forwarded fulfillment task.

* OPENAM-18252: Journeys acting on multiple identities now successfully update `universalId` in the journey context during the authentication flow.

* OPENAM-20314: Added the ability to indicate whether an OIDC provider doesn't return a unique value for the `sub` claim.

* OPENAM-22966: Social IDPs now support NONE as a client authentication method. This option should be used if the provider doesn't require client authentication at the token endpoint.

### 03 Dec 2024

#### Reversions

**Versions 15824.0 and 15770.0** have been reverted. All changes associated with these versions have been withdrawn. This affects the following changelog entries:

* [02 Dec 2024](#02_dec_2024)

* [25 Nov 2024](#25_nov_2024)

### 02 Dec 2024

**Version 15824.0**

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | This version has been reverted and all associated changes withdrawn. |

This release reintroduces many features, enhancements, and fixes previously present in reverted versions.

#### Key features

* [PingOne Authorize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-authorize.html)

  Use this node to send a decision request to a specified decision endpoint in your PingOne Authorize environment.

* PingOne Create, Identify, and Delete Nodes

  The following PingOne nodes are now available:

  * [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html)

    Use the PingOne Identity Match node to identify if a user exists both in the user repository and in PingOne, using defined attributes.

  * [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html)

    Create new users in the PingOne platform using the PingOne Create User node. Create users based off of an existing user's properties or choose to create the user anonymously. For example, when used in conjunction with PingOne Verify.

  * [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html)

    Delete users from the PingOne platform with the PingOne Delete User node.

* PingOne Verify Nodes

  Use the following PingOne Verify nodes in conjunction with the [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html), [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html), and [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html) to create a seamless verification process in your journey:

  * [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html)

    Leverage PingOne Verify to initiate or continue a verification transaction with the PingOne Verify Evaluation Node.

  * [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html)

    Determine the completion status of the most recent identity verification transaction for an end user.

    Use before the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) to determine the status of the verification process or after the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) using a script to evaluate the transaction.

    For example, you can evaluate if the transaction was completed using a passport and route your journey accordingly.

  |   |                                                                   |
  | - | ----------------------------------------------------------------- |
  |   | Use these nodes in place of the PingOne Verify Marketplace nodes. |

* reCAPTCHA Enterprise node

  The [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html) node adds Google reCAPTCHA Enterprise support to your journeys.

* SAML application journeys (AME-27850)

  Added support for SAML application journeys with a new setting on the remote SP. Configure a specific authentication journey that always runs for users authenticating with your SAML 2.0 app, regardless of existing sessions or configured authentication context.

  Learn more in [Configure a SAML 2.0 application journey](../am-saml2/configure-providers.html#samlapp-journey).

* Set Failure Details node (AME-27871)

  Use the [Set Failure Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-failure-details.html) to configure a localized error message on journey failure. You can also configure extra details in the response body of the failure request.

* Set Success Details node (OPENAM-12335)

  Use the [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-success-details.html) to add additional details to the success response of a journey.

#### Enhancements

* AME-26050: You can now create Next-generation Policy Condition scripts that have access to all common bindings, such as `openidm` and `httpClient`. Additionally, some existing bindings have been wrapped to improve usability in scripts.

* AME-28228: OAuth 2.0 audit logs now include the OAuth 2.0 client ID and any journey associated with the client.

* AME-29009: When using the new FIDO Metadata Service, if you link to the FIDO metadata using a URL, Advanced Identity Cloud periodically downloads and updates the latest FIDO metadata based on the `nextUpdate` date specified in the downloaded data.

* AME-29093: Added configuration for integration with WebAuthn Metadata Services (such as the FIDO Metadata Service). This includes a realm-level WebAuthn Metadata service and a new FIDO Certification Level configuration attribute in the WebAuthn Registration Node.

* AME-29769: The Social Provider Handler node has a new configuration option, Store Tokens, that allows access and refresh tokens to be stored in the transient state.

* FRAAS-22321: You can now obtain the HTTP client location from the `X-Client-Region` HTTP header within your scripts and journeys. The `X-Client-Region` header contains the country (or region) associated with the client's IP address in the form of a Unicode CLDR region code, such as `US` or `FR`. For most countries, these codes correspond directly to ISO-3166-2 codes.

* IAM-3323: You can now use XPath transformation functions with additional [Workday application template](../app-management/provision-an-application.html#provision-workday) attributes.

* IAM-4540: You can now change the border color of a selected input field in journey and end-user pages.

* OPENAM-23109: During a WebAuthn registration flow, if Store data in transient state is enabled, the Authenticator Attestation Global Unique Identifier (AAGUID) is now added to the node state under the `webauthnData` key.

#### Fixes

* AME-28016: When an invalid redirect URI is provided to the `/par` endpoint, the URI mismatch error is now `redirect_uri_mismatch` instead of `invalid_request`.

* AME-28017: Advanced Identity Cloud now accepts the requested OAuth 2.0 endpoint as a valid JWT audience claim, as per [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519.html#section-4.1.3) and [RFC 9126](https://www.rfc-editor.org/rfc/rfc9126.html#section-2).

* AME-28906: The stack trace of an authentication exception generated on login failure is now logged only when `debug` level logging is enabled.

* AME-29170: On [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html) login failure, stack traces are now logged at `debug` level.

* IAM-7523\[[2](#_footnotedef_2 "View footnote.")]: A user receiving a forwarded fulfillment task now has permission to approve or reject the task.

* IAM-7537\[[2](#_footnotedef_2 "View footnote.")]: Governance functionality is now only shown for the `alpha` realm.

* OPENAM-18252: Journeys acting on multiple identities now successfully update `universalId` in the journey context during the authentication flow.

* OPENAM-20314: Added the ability to indicate whether an OIDC provider doesn't return a unique value for the `sub` claim.

* OPENAM-22966: Social IDPs now support `NONE` as a client authentication method. Use this option if the provider doesn't require client authentication at the token endpoint.

### 26 Nov 2024

#### Reversions

**Version 15726.0** has been reverted. All changes associated with that version have been withdrawn. This affects the following changelog entries:

* [21 Nov 2024](#21-nov-2024)

* [20 Nov 2024](#20-nov-2024)

### 25 Nov 2024

**Version 15770.0**

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | This version has been reverted and all associated changes withdrawn. |

#### Enhancements

* FRAAS-22321: You can now obtain the HTTP client location from the `X-Client-Region` HTTP header within your scripts and journeys. The `X-Client-Region` header contains the country (or region) associated with the client's IP address in the form of a Unicode CLDR region code, such as `US` or `FR`. For most countries, these codes correspond directly to ISO-3166-2 codes.

### 21 Nov 2024

**Version 15726.0 (supplementary)**

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | This version has been reverted and all associated changes withdrawn. |

#### Key features

* PingOne Create, Identify, and Delete Nodes \[[8](#_footnotedef_8 "View footnote.")]

  The following PingOne nodes are now available:

  * [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html)

    Use the PingOne Identity Match node to identify if a user exists both in the user repository as well as in PingOne, using defined attributes.

  * [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html)

    Create new users in the PingOne platform using the PingOne Create User node. Create users based off of an existing user's properties or choose to create the user anonymously. For example, when used in conjunction with PingOne Verify.

  * [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html)

    Delete users from the PingOne platform with the PingOne Delete User node.

* PingOne Verify Nodes \[[8](#_footnotedef_8 "View footnote.")]

  Use the following PingOne Verify nodes in conjunction with the [PingOne Identity Match node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-identity-match.html), [PingOne Create User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-create-user.html), and [PingOne Delete User node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-delete-user.html) to create a seamless verification process in your journey:

  * [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html)

    Leverage PingOne Verify to initiate or continue a verification transaction with the PingOne Verify Evaluation Node.

  * [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-completion-decision.html)

    Determine the completion status of the most recent identity verification transaction for an end user.

    Use before the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) to determine the status of the verification process, or after the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) using a script to evaluate the transaction.

    For example, you can evaluate if the transaction was completed using a passport and route your journey accordingly.

  |   |                                                                   |
  | - | ----------------------------------------------------------------- |
  |   | Use these nodes in place of the PingOne Verify Marketplace nodes. |

* reCAPTCHA Enterprise node \[[8](#_footnotedef_8 "View footnote.")]

  The [reCAPTCHA Enterprise node](https://docs.pingidentity.com/auth-node-ref/latest/recaptcha-enterprise.html) node adds Google reCAPTCHA Enterprise support to your journeys.

### 20 Nov 2024

**Version 15726.0**

|   |                                                                      |
| - | -------------------------------------------------------------------- |
|   | This version has been reverted and all associated changes withdrawn. |

#### Key features

* Set Success Details node (OPENAM-12335)

  Use the [Set Success Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-success-details.html) to add additional details to the success response of a journey.

* Set Failure Details node (AME-27871)

  Use the [Set Failure Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-failure-details.html) to configure a localized error message on journey failure. You can also configure extra details in the response body of the failure request.

#### Enhancements

* AME-29769: The Social Provider Handler node has a new configuration option, Store Tokens, that allows access and refresh tokens to be stored in the transient state.

* AME-29009: When using the new FIDO Metadata Service, if you link to the FIDO metadata using a URL, Advanced Identity Cloud periodically downloads and updates the latest FIDO metadata based upon the `nextUpdate` date specified in the downloaded data.

* AME-29093: Added configuration for integration with WebAuthn Metadata Services (such as the FIDO Metadata Service). This includes a realm-level WebAuthn Metadata service and a new FIDO Certification Level configuration attribute in the WebAuthn Registration Node.

* AME-26050: You can now create Next-generation Policy Condition scripts that have access to all common bindings, such as `openidm` and `httpClient`. Additionally, some existing bindings have been wrapped to improve usability in scripts.

* OPENAM-23109: During a WebAuthn registration flow, if Store data in transient state is enabled, the Authenticator Attestation Global Unique Identifier (AAGUID) is now added to the node state under the `webauthnData` key.

#### Fixes

* AME-28016: When an invalid redirect URI is provided to the `/par` endpoint, the URI mismatch error is now `redirect_uri_mismatch` instead of `invalid_request`.

* AME-28017: Advanced Identity Cloud now accepts the requested OAuth 2.0 endpoint as a valid JWT audience claim, as per [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519.html#section-4.1.3) and [RFC 9126](https://www.rfc-editor.org/rfc/rfc9126.html#section-2).

* AME-28906: The stack trace of an authentication exception generated on login failure is now logged only when `debug` level logging is enabled.

* AME-29170: On [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html) login failure, stack traces are now logged at `debug` level.

* OPENAM-18252: Journeys acting on multiple identities now successfully update `universalId` in the journey context during the authentication flow.

* OPENAM-22966: Social IDPs now support `NONE` as a client authentication method. Use this option if the provider doesn't require client authentication at the token endpoint.

* OPENAM-20314: Added the ability to indicate whether an OIDC provider doesn't return a unique value for the `sub` claim.

### 20 Nov 2024

**Version 15723.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 19 Nov 2024

**Versions 15711.0, 15715.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 18 Nov 2024

**Versions 15703.0, 15708.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 15 Nov 2024

**Versions 15687.0, 15696.0, 15699.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 14 Nov 2024

**Version 15682.0**

#### Enhancements

* OPENDJ-11012: Added support for Microsoft Identity Cloud PBKDF2-SHA512 password scheme in Advanced Identity Cloud.

### 11 Nov 2024

**Version 15618.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 08 Nov 2024

**Version 15611.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 07 Nov 2024

**Version 15601.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 06 Nov 2024

**Version 15572.0**

#### Key features

* Configure journey to always run\[[9](#_footnotedef_9 "View footnote.")] (AME-27848)

  Added a new setting for journeys to always run regardless of existing user sessions.

  Learn more in [Configure an authentication journey to always run](../am-authentication/auth-nodes-and-journeys.html#enable-journey-completion).

* SAML application journeys (AME-27850)

  Added support for SAML application journeys with a new setting on the remote SP. Configure a specific authentication journey that always runs for users authenticating with your SAML 2.0 app, regardless of existing sessions or configured authentication context.

  Learn more in [Configure a SAML 2.0 application journey](../am-saml2/configure-providers.html#samlapp-journey).

* SAML application script binding\[[9](#_footnotedef_9 "View footnote.")] (AME-28012)

  Added a new `samlApplication` binding for querying the SAML 2.0 authentication request properties and IdP and SP configuration attributes.

  Learn more in [Query SAML application and authentication request](../am-scripting/scripting-api-node.html#samlapp-binding).

* Suspend and resume journeys (OPENAM-21806)

  Next-generation decision node scripts can now use the new `action.suspend()` method to suspend the current authentication session and send a message to the user. Implement custom logic with the resume URI, for example, to send an email or SMS using the HTTP client service.

  Learn more in [Suspend and resume journeys](../am-scripting/scripting-api-node.html#scripting-api-node-suspend).

#### Enhancements

* AME-27074: Added a new `configProviderScript` action to each authentication node endpoint to generate a configuration provider template script, for example: `authentication/authenticationtrees/nodes/MessageNode?_action=configProviderScript`.

* AME-28258: Added a new "webAuthnExtensions" input to the WebAuthn Registration and Authentication nodes. This can be set via a Scripted Decision node. It is expected to contain a map of extension name to input. Output is currently not available.

* AME-28384: The outcome of a Scripted Decision node can now also be a `CharSequence` type.

* AME-28777: The refresh token grace period now applies to both client-side refresh tokens and server-side refresh tokens.

* AME-29157: Authentication nodes with limited possible outcomes are now available to the [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html), including:

  * [MFA Registration Options node](https://docs.pingidentity.com/auth-node-ref/latest/mfa-registration-options.html)

  * [OATH Token Verifier node](https://docs.pingidentity.com/auth-node-ref/latest/oath-token-verifier.html)

  * [Polling Wait node](https://docs.pingidentity.com/auth-node-ref/latest/polling-wait.html)

  * [Push Sender node](https://docs.pingidentity.com/auth-node-ref/latest/push-sender.html)

  * [Select Identity Provider node](https://docs.pingidentity.com/auth-node-ref/latest/select-identity-provider.html)

  * [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html)

  * [WebAuthn Device Storage node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-device-storage.html)

  * [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)

  The [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html), [Push Wait node](https://docs.pingidentity.com/auth-node-ref/latest/push-wait.html), and [Enable Device Management node](https://docs.pingidentity.com/auth-node-ref/latest/enable-device-management.html) nodes with fixed outcomes are also now available to the Configuration Provider node.

* OPENAM-22601: You can now use the next-generation script binding, `utils`, to generate secure random numbers.

* OPENAM-22811: NodeState has two new methods: `mergeShared(Map<String, Object>)` and `mergeTransient(Map<String, Object>)`. Use them to merge keys into the shared/transient state, including "objectAttributes" keys.

#### Fixes

* AME-25491: The Configuration Provider node script now correctly reads node state after an inner tree callback.

* AME-28786: Removed several unused UI properties from default social identity provider profiles.

* AME-29027: WebAuthN attestations containing a self-signed root CA are now rejected instead of silently removed.

* OPENAM-22465: Fixed error to return `invalid_resource_uri` when request\_uri client doesn't match request parameter client in PAR authorise request.

* OPENAM-22675: In next-generation scripting, you can now set a default name correctly when creating a NameCallback.

* OPENAM-22688: Fixed Page node localization to default to correct locale when the incoming `accepted-language` header doesn't match the node's language configuration.

### 05 Nov 2024

**Version 15570.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 04 Nov 2024

**Version 15559.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 01 Nov 2024

**Version 15551.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 31 Oct 2024

**Version 15532.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 30 Oct 2024

**Version 15508.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 29 Oct 2024

**Versions 15466.0, 15472.0**

#### Enhancements

* IAM-6388: Added the ability to specify that inner journeys can't be accessed directly.

* IAM-7185: The mapping tab for application provisioning now shows the inbound or outbound application type without needing to inspect a drop-down.

#### Fixes

* IAM-7415: When creating an assignment, the `_id` is now automatically generated instead of using the name specified.

### 28 Oct 2024

**Version 15453.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 25 Oct 2024

**Version 15434.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 23 Oct 2024

**Version 15399.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 22 Oct 2024

**Version 15374.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 17 Oct 2024

**Versions 15335.0, 15337.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 16 Oct 2024

**Versions 15321.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 15 Oct 2024

**Versions 15310.0, 15312.0**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 14 Oct 2024

**Version 15300.0**

#### Enhancements

* IAM-7187: Integration of SAP app template with IDM scripts.

* IAM-7243\[[2](#_footnotedef_2 "View footnote.")]: Added text field to utilities category in IGA access request forms.

#### Fixes

* IAM-7385: Unable to create user when required boolean property is set to false.

### 10 Oct 2024

**Version 15258.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 07 Oct 2024

**Version 15211.0**

#### Enhancements

FRAAS-22177: Renamed "Advanced Gateway" to "Proxy Connect" throughout Advanced Identity Cloud, including URLs, OpenID Connect scopes, autogenerated code snippets, and UI labels.

### 01 Oct 2024

**Versions 15154.0, 15158.0**

#### Enhancements

IAM-4753: Added a toggle to the application catalog to hide deprecated templates.

### 30 Sept 2024

**Versions 15136.0, 15139.0, 15143.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 27 Sept 2024

**Version 15124.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 26 Sept 2024

**Versions 15111.0, 15114.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 25 Sept 2024

**Versions 15084.0, 15096.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Sept 2024

**Version 15063.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 23 Sept 2024

**Version 15058.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 20 Sept 2024

**Versions 15044.0, 15052.0**

#### Key features

* Support for LINE as a social identity provider (AME-28672)

  You can now configure a social provider authentication with LINE Login when signing in from a browser. There is a separate configuration for authenticating from a mobile app.

  Learn more in [Social authentication](../self-service/social-registration.html).

* Identity Governance request and approval forms\[[2](#_footnotedef_2 "View footnote.")] (IAM-6358)

  Identity Governance now lets you create request and approval forms to make it easier for end users to request access to applications.

  Learn more in [Identity Governance forms](../identity-governance/administration/governance-forms.html).

#### Enhancements

* OPENAM-22666: The well-known endpoint is no longer required when configuring a social identity provider service. If it is not provided, Advanced Identity Cloud uses the client secret for signature verification.

#### Fixes

* FRAAS-16228: Promotions are now halted if the AM CORS service is disabled; the service is essential to the correct functioning of promotions.

### 16 Sept 2024

**Version 14975.0**

#### Key features

* Additional cloud connectors

  The following connectors are now bundled with Advanced Identity Cloud:

  * AWS IAM Identity Center Connector v1.5.20.23 (OPENIDM-20038)

  * Box Connector v1.5.20.23 (OPENIDM-20367)

  Learn more in the [ICF documentation](https://docs.pingidentity.com/openicf/index.html).

#### Enhancements

* OPENIDM-19698: Added ability to use wildcards in the `watchedFields` property.

#### Fixes

* OPENIDM-19336: Fixed an issue where delegated administrators couldn't add new users to their organization.

* OPENIDM-20238: Fixed an issue where clustered reconciliation can fail with "Expecting a Map or List" under specific circumstances.

### 13 Sept 2024

**Version 14962.0**

#### Key features

* Advanced Reporting\[[6](#_footnotedef_6 "View footnote.")] (ANALYTICS-763)

  Advanced Identity Cloud now offers Advanced Reporting to let you create custom reports on activity in your tenant environments. You can query a number of metrics to create useful reports for your company.

  Learn more in [Advanced Reporting](../reports/administration/advanced-reports.html).

#### Fixes

* FRAAS-21715: Environments can now be unlocked if configuration rollback fails because there are no promotions to roll back.

### 11 Sept 2024

**Version 14927.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 Sept 2024

**Versions 14912.0, 14920.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 09 Sept 2024

**Versions 14868.0, 14888.0**

#### Key features

* Scripted SAML 2.0 NameID values(AME-25921)

  The [NameID mapper script](../am-saml2/custom-nameid-mapper.html) lets you customize SAML 2.0 NameID values per application.

* Set State node (AME-26443)

  The [Set State node](https://docs.pingidentity.com/auth-node-ref/latest/set-state.html) lets you add attributes to the journey state.

* Http Client service (AME-27936)

  The new [Http Client service](../am-reference/services-configuration.html#realm-httpclient) lets you create named instances that you can reference from a next-generation script to make mTLS connections to external services.

  Learn more in [Access HTTP services](../am-scripting/script-bindings.html#httpclient-mtls).

* Enable Device Management node (SDKS-2919)

  The new [Enable Device Management node](https://docs.pingidentity.com/auth-node-ref/latest/enable-device-management.html) lets end users manage devices from their account.

#### Enhancements

* FRAAS-21728: Updated the cookie domain API to add default values for GET requests where cookie domain values haven't been overridden by a PUT request. The default values are derived from the existing tenant cookie domain configuration, so are backward compatible.

* AME-26594: Added secrets API binding to all next-generation script contexts.

* AME-27129: Added option to exclude client certificate from SAML hosted SP metadata.

* AME-27792: Added `AM-TREE-LOGIN-COMPLETED` audit log event that outputs a `result` of `FAILED`. when a journey ends with an error.

* AME-27839: Added the ability to specify connection and response timeouts for Http Client service instances.

* AME-28008: You can now disable certificate revocation checks, or all certificate checks entirely, on your Http Client service instances.

#### Fixes

* OPENAM-15410: Fixed an issue that prevented customization of claims if `profile` and `openid` scopes are requested.

* OPENAM-20609: Fixed inconsistent error message when generating access token using refresh token after changing username.

* OPENAM-21974: Adds an OAuth 2.0 client configuration for the new version of the LinkedIn provider.

* OPENAM-22298: Log unretrieved SP and IdP descriptors in SAML2 Authentication node.

### 06 Sept 2024

**Versions 14851.0, 14858.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 05 Sept 2024

**Version 14848.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 03 Sept 2024

**Version 14800.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 02 Sept 2024

**Version 14781.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 30 Aug 2024

**Versions 14761.0, 14767.0**

#### Fixes

* FRAAS-21713: The promotion process now retries getting an access token from the lower environment, preventing promotion failures.

### 29 Aug 2024

**Version 14741.0**

#### Key features

* DocuSign application template (IAM-6194)

  The [DocuSign application](../app-management/provision-an-application.html#provision-docusign) lets you manage DocuSign service accounts and synchronize DocuSign accounts and Advanced Identity Cloud identities.

#### Enhancements

* IAM-6493: The PingOne application template now supports specifying an LDAP gateway.

* IAM-6868: Added screen reader label to end-user access approval button.

* IAM-6870: Added screen reader label to end-user access request button.

* IAM-6880: Added a toggle in the hosted pages journey settings to disable the error heading fallback that displays if there is no heading in the page content. (FORGEROCK-1582)

#### Fixes

* IAM-7033: Unable to save user filter in AD/LDAP app template.

### 27 Aug 2024

**Version 14717.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 26 Aug 2024

**Version 14683.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 22 Aug 2024

**Version 14652.0, 14669.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 21 Aug 2024

**Version 14626.0**

#### Key features

* BeyondTrust application template (IAM-6492)

  The [BeyondTrust application](../app-management/provision-an-application.html#provision-beyondtrust) lets you manage and synchronize data from Advanced Identity Cloud to BeyondTrust.

#### Enhancements

* IAM-7011: Older app templates are no longer marked "deprecated".

### 19 Aug 2024

**Version 14592.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 16 Aug 2024

**Versions 14568.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 14 Aug 2024

**Versions 14530.0, 14538.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 13 Aug 2024

**Version 14516.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 12 Aug 2024

**Version 14467.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 09 Aug 2024

**Version 14465.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 08 Aug 2024

**Version 14454.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 07 Aug 2024

**Versions 14443.0, 14450.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 06 Aug 2024

**Version 14442.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 05 Aug 2024

**Versions 14425.0, 14432.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 02 Aug 2024

**Versions 14410.0, 14417.0**

#### Enhancements

* IAM-5233: Update SAP SuccessFactors app template to support connector version 1.5.20.22.

* IAM-6874: Update journey analytics to use hourly data.

#### Fixes

* FRAAS-21318: Promotion report now categorizes AM session service changes correctly.

### 25 Jul 2024

**Versions 14309.0, 14313.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Jul 2024

**Versions 14275.0, 14277.0, 14285.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 23 Jul 2024

**Versions 14257.0, 14260.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 22 Jul 2024

**Version 14238.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 19 Jul 2024

**Version 14225.0**

#### Key features

* Adobe Admin Console application template (IAM-6195)

  The [Advanced Identity Cloud Adobe Admin Console application](../app-management/app-catalog.html) lets you manage users, groups, and user group memberships between Adobe Admin Console and Advanced Identity Cloud.

#### Enhancements

* IAM-4279: Display available ESV placeholders in Decision Node script editor.

* IAM-4654: Enable creation of all script types in Advanced Identity Cloud admin console.

#### Fixes

* IAM-5356: Session logout warning not displaying when maximum idle time set to a higher value than maximum session time.

* IAM-6628: New draft option shouldn't exist for out-of-the-box workflows.

* IAM-6779: Pagination for list of apps not working when there are over 4000 apps.

### 18 Jul 2024

**Version 14199.0, 14213.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 17 Jul 2024

**Version 14175.0, 14187.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 16 Jul 2024

**Version 14160.0, 14165.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 15 Jul 2024

**Version 14149.0, 14150.0, 14156.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 12 Jul 2024

**Versions 14108.0, 14113.0**

#### Fixes

* FRAAS-20397: The promotion process now retries tagging the lower environment after a network interruption, preventing blocking promotion failures.

### 11 Jul 2024

**Versions 14100.0, 14101.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 Jul 2024

**Version 14093.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 09 Jul 2024

**Version 14069.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 08 Jul 2024

**Versions 14062.0, 14063.0**

#### Fixes

* FRAAS-20983: Promotion reports now list changes to the default OAuth 2.0 provider.

### 05 Jul 2024

**Versions 14046.0, 14047.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 03 Jul 2024

**Version 14018.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 02 Jul 2024

**Version 14013.0**

#### Fixes

* FRAAS-20970: The `/monitoring/logs` endpoint now returns an `X-Ratelimit-Limit` header with a fixed value of 60. Previously, the value was misleading due to the way it was calculated when scaling an environment's resources. The `X-Ratelimit-Remaining` header continues to report the number of requests that may be sent before receiving a rate limited response.

### 01 Jul 2024

**Versions 13982.0, 14004.0**

#### Fixes

* OPENIDM-18495: Disable sorting in the connector data tab in the IDM native admin console.

### 27 Jun 2024

**Versions 13964.0, 13966.0**

#### Key features

* Additional cloud connectors

  The following connectors are now bundled with Advanced Identity Cloud:

  * Adobe Admin Console connector (OPENIDM-19843)

  * DocuSign connector (OPENIDM-20190)

  For more information, refer to the [ICF documentation](https://docs.pingidentity.com/openicf/index.html).

#### Fixes

* OPENIDM-20142: Resolved a communication failure between Advanced Identity Cloud and RCS instances that could result in a prolonged failure to activate remote connectors.

#### Changed functionality

* OPENIDM-20178: You can't use scope private fields in query filters. For more information, refer to link:[Security Advisory #202402](https://backstage.pingidentity.com/knowledge/advisories/article/a95212747).

### 26 Jun 2024

**Versions 13953.0, 13956.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 25 Jun 2024

**Version 13945.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Jun 2024

**Versions 13937.0**

#### Key features

* Product name change for Identity Cloud (FRAAS-20178)

  To align ForgeRock products with Ping family names, ForgeRock Identity Cloud has been renamed to PingOne Advanced Identity Cloud. Name and logo changes have been updated throughout the user interfaces, and documentation updates will occur when the UI changes are released to the regular channel.

#### Enhancements

* IAM-4785: Synchronize only the modified properties on a target source during reconciliation of applications.

* IAM-5237\[[2](#_footnotedef_2 "View footnote.")]: Add ability for B2B business partners to certify access for their users using organizational-based certification.

* IAM-5487: Correlation rules moved to the top of the reconciliation settings page.

* IAM-5629\[[2](#_footnotedef_2 "View footnote.")]: Add ability to create scoping rules in Identity Governance.

* IAM-6231: Scripted Decision Node now updates the list of scripts when a script is added or edited.

* IAM-6544\[[2](#_footnotedef_2 "View footnote.")]: Add reviewer column to administrator list view of compliance violations.

#### Fixes

* IAM-6135: ESV values containing accents get corrupted by encoding process.

* IAM-6562: Label duplicated for OAuth 2.0 access token and ID token endpoints.

* IAM-6669\[[2](#_footnotedef_2 "View footnote.")]: Badge count of violations in end-user navigation doesn't update when an action is performed.

### 18 Jun 2024

**Versions 13896.0, 13900.0**

#### Key features

* PingOne Protect nodes\[[10](#_footnotedef_10 "View footnote.")] (TNTP-180)

  The new PingOne Protect nodes replace the deprecated PingOne Protect Marketplace nodes.

#### Fixes

* FRAAS-20604: Removed superfluous AM metrics related to token store internals:

  * `am_cts_connection_count`

  * `am_cts_connection_seconds`

  * `am_cts_connection_seconds_total`

  * `am_cts_connection_state`

  * `am_cts_reaper_cache_size`

  * `am_cts_reaper_deletion`

  * `am_cts_reaper_deletion_count`

  * `am_cts_reaper_deletion_total`

* FRAAS-20786: Fix promotion issue where an attempt was made to delete an already deleted application.

### 17 Jun 2024

**Version 13890.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 14 Jun 2024

**Version 13877.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 13 Jun 2024

**Version 13865.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 12 Jun 2024

**Version 13848.0**

#### Key features

* New utility binding available for scripting (AME-25519)

  You can now use a new utility binding in your scripts to access several common utility classes. For example, the utility binding includes classes for generating random UUIDs and for base64 encoding and decoding.

#### Enhancements

* AME-26199: Added the ability to set additional claims, including non-registered claims, during JWT assertion and generation, as per the specification.

* AME-26820: Provided library scripts with access to all common script bindings.

* AME-26993: Enhanced secret mapping for agents. Updating a secret label identifier value now causes any corresponding secret mapping for the previous identifier to also be updated, provided no other agent shares that secret mapping. If another agent shares the secret mapping, Advanced Identity Cloud creates a new secret mapping for the updated identifier and copies its aliases from the previously shared secret mapping.

* AME-27346: Renamed **Secret ID Identifier** to **Secret Label Identifier** in the SAML remote entity provider configuration.

* AME-27478: Renamed **Client ID Token Public Encryption Key** property to **ID Token Encryption Public Key** in the OAuth 2.0 client configuration.

* AME-27775: Added scripting thread pool metrics per script context.

* OPENAM-16564: Enabled next-generation scripts to access the cookies in incoming requests.

* OPENAM-21800: Added page node functionality to next-generation scripts.

* OPENAM-21933: Enabled auto-encoding of the `httpClient` form body in next-generation scripts.

#### Fixes

* FRAAS-19461: Fixed an issue where large audit logs could be missing from IGA events and processing.

* OPENAM-21748: Restored the missing `get` wrapper function for `HiddenValueCallback` in next-generation scripting.

* OPENAM-21864: Fixed an issue that prevented setting the tracking cookie to resume a journey after returning from a redirect flow.

* OPENAM-21897: Corrected inconsistent results from the policy `evaluateTree` endpoint.

* OPENAM-21951: Enabled setting of the `selectedIndex` property in a `ChoiceCallback` in next-generation scripts.

* OPENAM-22181: Corrected an issue with UMA `approve` and `approveAll` requests failing.

### 05 Jun 2024

**Version 13760.0**

#### Enhancements

* FRAAS-20048: Configuration promotions can now be rolled back using the API. An environment can be rolled back successively to revert as many previous promotion changes as needed.

  |   |                                                                                                                                                                                                         |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This feature can't be used in sandbox environments; a promotion or a rollback can only be run between development, UAT\[[11](#_footnotedef_11 "View footnote.")], staging, and production environments. |

### 04 Jun 2024

**Version 13741.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 03 Jun 2024

**Version 13731.0**

#### Fixes

* FRAAS-20154: ESVs with special characters are now correctly encoded. The workaround of double-encoding ESVs is no longer required.

### 03 Jun 2024

#### Fixes

* FRAAS-11180: Authentication session whitelisting is now enabled by default for new tenants\[[12](#_footnotedef_12 "View footnote.")]

* IAM-5593: Adding roles to certain objects no longer breaks readable titles\[[12](#_footnotedef_12 "View footnote.")]

* IAM-6537: Journey import now alerts users if they try to import a file containing missing references\[[12](#_footnotedef_12 "View footnote.")]

### 22 May 2024

**Versions 13570.0**

#### Key features

* Oracle E-Business Suite app template (IAM-6342)

  The [Oracle E-Business Suite (EBS) application](../app-management/provision-an-application.html#provision-ebs) lets you manage and synchronize accounts between EBS and Advanced Identity Cloud.

#### Enhancements

* IAM-6376: In the applications rules tab, you can now configure custom logic to perform specific actions, such as sending an email, when an account is successfully created or updated.

* IAM-6380: In the applications rules tab, you can now use the provisioning failure rule to configure custom logic to perform specific actions when provisioning fails.

### 21 May 2024

**Versions 13548.0, 13552.0, 13562.0**

#### Enhancements

* FRAAS-15404: When updating ESV secrets, the API saves a new secret version only when it differs from the previous value.

### 20 May 2024

**Version 13528.0**

#### Key features

* Improved promotion of applications (FRAAS-19241)

  It is now possible to promote applications via the API and not just the UI.

  Additionally, the provisional report has been improved to only show applications that have changed, rather than always show all applications in the report.

#### Enhancements

* FRAAS-19982: Configuration promotion now fails if Advanced Identity Cloud services do not restart successfully with the new configuration.

### 16 May 2024

**Version 13493.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 15 May 2024

**Versions 13477.0, 13482.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 14 May 2024

**Versions 13464.0, 13465.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 13 May 2024

**Versions 13445.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 May 2024

**Versions 13417.0, 13424.0, 13426.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 07 May 2024

**Versions 13361.0, 13359.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 06 May 2024

**Versions 13352.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 03 May 2024

#### Key features

* Webex application template (IAM-5234\[[13](#_footnotedef_13 "View footnote.")])

  The [Advanced Identity Cloud Webex application](../app-management/provision-an-application.html#provision-webex) lets you manage and synchronize data between Webex Control Hub and Advanced Identity Cloud.

* Epic EMP application template (IAM-2407)

  The [Epic EMP application](../app-management/provision-an-application.html#provision-epic-emp) lets you manage and synchronize data between Epic EMP and Advanced Identity Cloud.

#### Enhancements

* IAM-2653: Configure object properties with user-friendly display names.

* IAM-3857: Application list view displays enabled/disabled status of enterprise apps.

* IAM-5913\[[2](#_footnotedef_2 "View footnote.")]: Create custom access request workflows.

#### Fixes

* IAM-6264: Approval actions display in the UI even when they are not available due to permissions.

* IAM-6296: UI doesn't display paginated results on application data and recon tabs.

* IAM-6409: Logging out of UI generates malformed redirect realm URLs.

### 01 May 2024

**Versions 13317.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 30 Apr 2024

**Versions 13300.0, 13310.0, 13313.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 29 Apr 2024

**Version 13293.0, 13294.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 26 Apr 2024

**Version 13291.0, 13289.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 25 Apr 2024

**Version 13283.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Apr 2024

**Version 13281.0**

#### Fixes

* TNTP-166:

  * Add configuration options to P1 Verify Authentication nodes.

  * Verify code not visible when using QR option.

  * Set claim mapping only in shared state in P1 Proofing node.

### 23 Apr 2024

**Version 13277.0, 13265.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 22 Apr 2024

**Version 13239.0**

#### Fixes

* FRAAS-19593: The promotion API incorrectly reports as ready, resulting in a blocking promotion failure when trying to promote. (FORGEROCK-1319)

### 18 Apr 2024

**Version 13237.0**

#### Fixes

* OPENIDM-19879: Identity Management reconciliation service processes additional source query pages whenever a query returns a `pagedResultsCookie`.

* OPENIDM-19924: Unnecessary quotes not being removed from email addresses.

### 17 Apr 2024

**Version 13218.0**

#### Key features

* Event-based certification\[[2](#_footnotedef_2 "View footnote.")] (IAM-5148)

  Identity Governance now allows tenant administrators to configure certifications that are triggered by specific governance events, a process referred to as *event-based certification*. This method offers faster certification resolution compared to scheduled—​and often lengthy—​campaigns spanning weeks or months and involving numerous applications, intricate rules, and hundreds of reviewers.

  The event-based certifications feature kicks off an identity certification for the following events:

  * **User create**. Advanced Identity Cloud detects when a user account has been created.

  * **User modify**. Advanced Identity Cloud detects when an existing user account has been modified or updated.

  * **Attribute change**. Advanced Identity Cloud detects changes in the attributes of an existing user account.

  * **User delete/deactivate**. Advanced Identity Cloud detects if a user account has been deleted or deactivated.

  For more information, refer to [Certify access by event](../identity-governance/administration/event-certification-preface.html).

* Grant entitlements to users and roles\[[2](#_footnotedef_2 "View footnote.")] (IAM-5146)

  Identity Governance now allows tenant administrators to carry out more fine-grained entitlement grants for their user accounts. Tenant administrators can now:

  * Create a role and grant entitlements to the role.

  * Revoke entitlements in a role.

  * Grant entitlements to a user account.

  * Revoke entitlements from a user account.

  For more information, refer to [Entitlements](../identity-governance/administration/entitlements.html).

* Identity Assertion node (AME-26821)

  The new [Identity Assertion node](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html) provides a secure communication channel for authentication journeys to communicate directly with [PingGateway](../realms/gateways-agents.html).

* PingOne application template (IAM-5232)

  The PingOne application lets you manage and synchronize data between PingOne and Advanced Identity Cloud.

* Authenticate gateway and agent profiles with a shared secret (IAM-5833)

  The Advanced Identity Cloud admin console for gateways and agents now lets you authenticate with a shared secret instead of a password. Use this to set the label for the shared secret.

* Authenticate OAuth 2.0 applications with a shared secret (IAM-6028)

  The Advanced Identity Cloud admin console for OAuth 2.0 applications now lets you authenticate with a shared secret instead of a password. Use this to set the label for the shared secret.

#### Enhancements

* OPENAM-21031: The performance of Google KMS has been improved by the introduction of caching.

* AME-27126: A SAML SP can now authenticate to IDPs using mutual TLS (mTLS) when making an artifact resolution request.

* IAM-3199: HTML styling in the Message node journey editor allows you to left justify text.

#### Fixes

* FRAAS-19334: Failure to look up service account names following changes applied through the ESV API.

* IAM-5079\[[2](#_footnotedef_2 "View footnote.")]: End-user roles page sometimes shows role grants as conditional even when the grants are direct.

* IAM-5363\[[2](#_footnotedef_2 "View footnote.")]: Show the total number of approvals and access reviews in the inbox.

* IAM-5858\[[2](#_footnotedef_2 "View footnote.")]: Missing support for access request global configuration options.

* IAM-6138\[[2](#_footnotedef_2 "View footnote.")]: The governance events filter builder incorrectly validates `before` and `after` properties in the user created state.

* IAM-6176\[[2](#_footnotedef_2 "View footnote.")]: The end-user access request rejection is missing a justification message.

* IAM-6203\[[2](#_footnotedef_2 "View footnote.")]: The governance events filter doesn't use `after` temporal values for user created flows.

* IAM-6209: The Advanced Identity Cloud admin console navigation panel text appears when the panel is collapsed.

* OPENAM-21473: If you set the collection method of a Certificate Collector node to `REQUEST`, `HEADER`, or `EITHER`, and the certificate is not provided in the request or in the header, the node now returns a status of `Not collected`.

  |   |                                                                  |
  | - | ---------------------------------------------------------------- |
  |   | This node is currently not supported in Advanced Identity Cloud. |

* SDKS-2935: The [Device Binding node](https://docs.pingidentity.com/auth-node-ref/latest/device-binding.html) now gracefully handles the case of a user being set to `inactive`.

### 12 Apr 2024

**Version 13162.0**

#### Fixes

* FRAAS-19596: Configuration promotion report should include changes to realm authentication settings.

### 11 Apr 2024

**Version 13149.0**

#### Enhancements

* AME-26085: SAML 2.0 `NameID` mapping can be configured per SP

* AME-27133: "Secret ID" has been renamed to "Secret Label" for secret mappings

* The following services now support configuration using the Secrets API:

  * AME-16536: The OAuth 2.0 provider hash salt secret

  * AME-25885: The persistent cookie core authentication attribute

  * AME-26110: The client-side session signing key

  * AME-26134: The social provider service

  * AME-26441: The new CAPTCHA node (replaces the legacy CAPTCHA node)

  * AME-26442: The OIDC Token Validator node now lets you store the client secret in any type of secret store

  * AME-26633: The OAuth 2.0 client `clientJwtPublicKey`

  * AME-26637: The OAuth 2.0 client `idTokenPublicEncryptionKey`

  * AME-26639: OAuth 2.0 client mTLS self-signed certificates

  * AME-26668: The post authentication process (PAP) replay password

  * AME-26670: The web agents replay password key

  * AME-26998: The OAuth 2.0 client secret

* The following services now support rotation of secrets using secret versions:

  * AME-25988: The persistent cookie encryption secret

  * AME-26999: OAuth 2.0 client secrets

  * AME-27000: OAuth 2.0 client `clientJwtPublicKey`

  * AME-27001: OAuth 2.0 client mTLS self-signed certificates

### 09 Apr 2024

**Version 13122.0**

#### Key features

* PingOne Verify service node (TNTP-118)

  The [PingOne Verify service node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-service.html) lets you configure and use PingOne Verify nodes ([PingOne Verify Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-authn.html) and [PingOne Verify Proofing node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-proof.html)) in your authentication journeys.

### 08 Apr 2024

**Version 12666.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 04 Apr 2024

**Version 12589.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 02 Apr 2024

**Version 13009.0**

#### Enhancements

* FRAAS-19566: Add `_sortKeys` query parameter to ESV API

### 01 Apr 2024

**Version 12988.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 29 Mar 2024

**Versions 12974.0, 12960.0, 12957.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 28 Mar 2024

**Versions 12957.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 27 Mar 2024

**Versions 12957.0, 12934.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 26 Mar 2024

**Versions 12899.0**

#### Key features

* Social Provider Handler node\[[14](#_footnotedef_14 "View footnote.")] (OPENAM-20924)

  The new Social Provider Handler node adds an outcome to better handle interruptions in a social authentication journey after requesting profile information.

* Event-based certification\[[2](#_footnotedef_2 "View footnote.")] (IGA-2357)

  Identity Governance now allows tenant administrators to configure certifications that are triggered by specific governance events, a process referred to as *event-based certification*. This method offers faster certification resolution compared to scheduled—​and often lengthy—​campaigns spanning weeks or months and involving numerous applications, intricate rules, and hundreds of reviewers.

  The event-based certifications feature kicks off an identity certification for the following events:

  * **User create**. Advanced Identity Cloud detects when a user account has been created.

  * **User modify**. Advanced Identity Cloud detects when an existing user account has been modified or updated.

  * **Attribute change**. Advanced Identity Cloud detects changes in the attributes of an existing user account.

  * **User delete/deactivate**. Advanced Identity Cloud detects if a user account has been deleted or deactivated.

    For more information, refer to [Certify access by event](../identity-governance/administration/event-certification-preface.html).

* Grant entitlements to users and roles\[[2](#_footnotedef_2 "View footnote.")] (IAM-5146)

  Identity Governance now allows tenant administrators to carry out more fine-grained entitlement grants for their user accounts. Tenant administrators can now:

  * Create a role and grant entitlements to the role.

  * Revoke entitlements in a role.

  * Grant entitlements to a user account.

  * Revoke entitlements from a user account.

    For more information, refer to [Entitlements](../identity-governance/administration/entitlements.html).

#### Enhancements

* AME-26130\[[14](#_footnotedef_14 "View footnote.")]: Updated the PUSH Notification service to store access keys as a secret

* AME-25906\[[14](#_footnotedef_14 "View footnote.")]: Updated Identity Gateway agents to store credentials as a secret

* IAM-4585: Request and approvals page now shows the current and past approvers, their decisions, and the dates

* IAM-4968: Expose additional top-level parameters in the advanced section of mapping pages

* IAM-5769: Add grouping logic to journey node items

* IAM-5674: Target application can use ONBOARD action for FOUND situation

* IAM-5814: Allow fixed application usernames to be chosen for custom SAML apps

* OPENAM-21575\[[14](#_footnotedef_14 "View footnote.")]: Added `org.forgerock.json.jose.jwe.JweHeader` to the allowlist for Scripted Decision nodes

#### Fixes

* AME-25915\[[14](#_footnotedef_14 "View footnote.")]: Assertion consumer processing fails if NameID format not present in the assertion response

* IAM-3927\[[2](#_footnotedef_2 "View footnote.")]: Identity Governance now enforces mandatory comments (if configured) for revoke and allow exceptions

* IAM-4309: Access reviews no longer display the internal `lastSync` user attribute

* IAM-4762: Authoritative apps are now requestable

* IAM-4986: Platform UI can now determine whether to use a pagedResultsCookie or offset for paging results

* IAM-5076: "Abstain from action" option no longer displays when a campaign has expired

* IAM-5362: Marking a property as an authoritative app entitlement no longer causes target app config to be generated

* IAM-5413: Account deprovisioning now works in AD/LDAP after deleting a user identity

* IAM-5794: Border color of sign-in input fields in hosted pages can now be overridden in themes

* IAM-5875: Journey editor no longer orphans deleted nodes

### 25 Mar 2024

**Versions 12899.0, 12894.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 22 Mar 2024

**Version 12878.0**

#### Enhancements

* FRAAS-19414: You can now configure custom domains directly in all environments without needing to create ESVs or promote configurations. Existing custom domains will be migrated automatically.

### 21 Mar 2024

**Versions 12899.0, 12863.0, 12855.0**

#### Key features

* Additional cloud connectors

  The following connectors are now bundled with Advanced Identity Cloud:

  * Dropbox connector (OPENIDM-19838)

  * PingOne connector (OPENIDM-19736)

  * Webex connector (OPENIDM-19920)

  For more information, refer to the [ICF documentation](https://docs.pingidentity.com/openicf/index.html).

#### Enhancements

* OPENIDM-19921: The following connectors included with Advanced Identity Cloud were upgraded to 1.5.20.21:

  * Google Apps connector

  * Microsoft Graph API connector

  * AWS connector

  For details, refer to [1.5.20.21 Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html#1_5_20_21).

### 19 Mar 2024

**Versions 12820.0, 12815.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 18 Mar 2024

**Versions 12873.0, 12784.0**

#### Enhancements

* FRAAS-19341: ESV support for AES keys through the `base64aes` encoding type

  For more information, refer to [Encoding format](../tenants/esvs.html#encoding-format).

### 15 Mar 2024

**Versions 12754.0**

#### Key features

* PingOne Service (TNTP-148)

  Set up the [PingOne Service](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-service.html) in your Advanced Identity Cloud tenant so you can add Ping Identity nodes to your authentication journeys.

* PingOne nodes (TNTP-119)

  * [PingOne node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone.html)

    The [PingOne node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone.html) establishes trust between PingOne and Advanced Identity Cloud by leveraging a federated connection. Learn more in [PingOne node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone.html).

  * [PingOne DaVinci API node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html)

    The [PingOne DaVinci API node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html) lets an Advanced Identity Cloud journey trigger a PingOne DaVinci flow through the API integration method. Learn more in [PingOne DaVinci API node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-davinci.html).

* PingOne Protect nodes (TNTP-127)

  Ping Identity's PingOne Protect is a centralized identity threat protection service, for securing your digital assets against online fraud attempts.

  Learn more in [PingOne Protect > How it Works](https://www.pingidentity.com/en/platform/capabilities/threat-protection/pingone-protect.html#section-2-ea7ff059-06bb-4145-9585-4c923ddd435d).

### 14 Mar 2024

**Versions 12736.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 13 Mar 2024

**Version 12714.0**

#### Key features

* [HTTP Client node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/http-client.html) (TNTP-136)

  The [HTTP Client node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/http-client.html) lets you make HTTP(S) requests to APIs and services external to Advanced Identity Cloud from within a journey.

  Use the [HTTP Client node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/http-client.html) to simplify the integration with a broad range of external services by making direct HTTP(S) requests.

  For more information, refer to [HTTP Client node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/http-client.html).

#### Enhancements

* IAM-5602: Add functionality for viewing and deleting user's trusted devices in Advanced Identity Cloud admin console

### 08 Mar 2024

**Versions 12666.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 04 Mar 2024

**Versions 12589.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 02 Mar 2024

**Version 12580.0**

#### Enhancements

* The following services now support setting secrets using the secrets API rather than setting secrets in the service configuration:

  * AME-25709: AuthId signing key

  * AME-25907: Java agents

  * AME-25908: Web agents

  * AME-26014: Rotatable secrets for agents

  * AME-26301: SAML remote entities

  * AME-26241: OATH, Push, Web AuthN devices and the device binding, device ID, and Device profile services

* The following nodes now support setting their secrets using the secrets API rather than setting secrets in the node configuration:

  * AME-26117: OTP SMS Sender and OTP SMTP Sender nodes

  * AME-16535: Set Persistent Cookie node

* AME-26041: Enhanced handling of agents secret mappings – if you update or delete a secret label identifier, any corresponding secret mapping for the previous identifier is updated or deleted, provided no other agent shares that secret mapping

* AME-25434: New Request Header node lets you inject values into shared state based on request header values

* AME-26039: Added LDAP Affinity Level configuration option to the LDAP Decision node, to enable affinity-based load balancing for BIND requests

* OPENAM-21768: Added `org.forgerock.opendj.ldap.Rdn` and `org.forgerock.opendj.ldap.Dn` classes to the allowlist for all script contexts

#### Fixes

* AME-24760: Inner nodes of a PageNode don't independently audit node-login-complete events

* AME-26158: Exception thrown when generating a Signed JWT with no encryption within a next-gen script called by a Scripted Journey node

* OPENAM-17315: Scripts used to call 'response.getEntity()' in the past should now use 'response.getEntity().getString()' instead

* OPENAM-21856: Introspecting stateless token with IG/Web agents causes `OAuth2ChfException`

### 01 Mar 2024

**Versions 12560.0**

No customer-facing issues released.\[[1](#_footnotedef_1 "View footnote.")]

### 29 Feb 2024

**Version 12560.0**

#### Enhancements

* IAM-4257: Azure AD [app template](../app-management/provision-an-application.html#connectors_with_predefined_non_account_objects) updates

* IAM-4342: MSGraphAPI connector includes a new optional `licenseCacheExpiryTime` configuration property

* IAM-4892: Salesforce [app template](../app-management/provision-an-application.html#connectors_with_predefined_non_account_objects) updates

* IAM-4900: UI has been updated to show the Advanced Identity Cloud build number

* IAM-5033: Added new "Remember my username" checkbox to authentication trees

* IAM-5287: Updated username, password, and KBA heading size on the profile page to improve accessibility

* IAM-5334: Expose "Guarded String" as an object type property for Scripted Groovy, ScriptedREST, ScriptedSQL, CSV, Database table, and SCIM connectors

* IAM-5459: KBA answer field now contains question context

* IAM-5461: Custom errors sent as `TextOutputCallback.ERROR` are now rendered as primary login errors, improving screen reader accessibility feature

* IAM-5503: Rename Orchestrations to Workflows

* IAM-5563: Google Apps [app template](../app-management/provision-an-application.html#connectors_with_predefined_non_account_objects) updates

* IAM-5603: Create device details modal for managed user identities

* IAM-5606: Add "POWERED BY" metadata to marketplace nodes

* IAM-5748: Make "PingOne" a special case on the federation providers page

#### Fixes

* IAM-5598: Styled terms and conditions included in a journey causes authenticate calls to fail

* IAM-5611: Can't revoke custom apps from roles or edit them from the role view

* IAM-5641: Custom endpoints search returns endpoints created by other areas of the UI

* IAM-5692: Console errors when opening the Add user modal for Bravo realm

* IAM-5767: SAML SSO is not used when an application is saved from another tab after SSO setup

* IAM-5873: Hosted page may fail to match user locale

### 28 Feb 2024

**Version 12547.0**

#### Enhancements

* OPENIDM-19405: [Allow email addresses](../tenants/email-provider.html#international-email) to contain non-ASCII characters for supported SMTP providers

### 15 Feb 2024

#### Fixes

* FRAAS-18455: Prevent the latest version of a secret from being deleted

### 12 Feb 2024

#### Enhancements

* FRAAS-18788: Add AWS, GCP, and SAP S/4HANA connectors to Advanced Identity Cloud

### 07 Feb 2024

#### Fixes

* FRAAS-18693: Validation bug prevents use of the `base64encodedinlined` and `keyvaluelist` ESV expression types

### 06 Feb 2024

#### Fixes

* FRAAS-18414: Changes to an out-of-the-box journey can be incorrectly reported against both realms

### 25 Jan 2024

#### Fixes

* FRAAS-18526: Script library functionality can't be used in the UI in certain environments

### 24 Jan 2024

#### Enhancements

* OPENIDM-17878\[[15](#_footnotedef_15 "View footnote.")]: Allow access to operational attributes in the Advanced Identity Cloud data store

* OPENIDM-18645\[[15](#_footnotedef_15 "View footnote.")]: Add ESV support to `oauthProxy` script

#### Fixes

* OPENIDM-18743\[[15](#_footnotedef_15 "View footnote.")]: Attempts to use connectors fail with null pointer exceptions when `operationOptions` is defined in the provisioner configuration

### 23 Jan 2024

#### Key features

* iProov Authentication node (TNTP-131)

  The [iProov authentication](https://docs.pingidentity.com/auth-node-ref/latest/cloud/iproov.html) node integrates Advanced Identity Cloud authentication journeys with the [Genuine Presence Assurance](https://www.iproov.com/iproov-system/technology/genuine-presence-assurance) and [Liveness Assurance](https://www.iproov.com/iproov-system/technology/liveness-assurance) products from [iProov](https://www.iproov.com/).

### 22 Jan 2024 (supplementary)

#### Key features

* Fingerprint Profiler and Fingerprint Response nodes (TNTP-130)

  The [Fingerprint nodes](https://docs.pingidentity.com/auth-node-ref/latest/cloud/fingerprint.html) nodes let you integrate your Advanced Identity Cloud environment with the [Fingerprint platform](https://fingerprint.com/products/fingerprint-pro/) to help reduce fraud and improve customer experience.

#### Enhancements

* AME-25906: Add the ability to configure the password for authenticating to an Identity Gateway agent as an ESV secret

* AME-26130: Add the ability to configure the SNS access key secret for the push notification service to use an ESV secret

* OPENAM-21575: Add `org.forgerock.json.jose.jwe.JweHeader` to the class allowlist for Scripted Decision node

#### Fixes

* AME-25915: SAML flow fails if a `NameIDFormat` element is not present in an assertion response

* FRAAS-18464: Sandbox debug logging level set to `WARN` instead of `DEBUG`

* IAM-5656: Fix alignment of text, buttons, and links in Message nodes

* IAM-5660: Hosted pages not displaying list of themes

* OPENAM-20924: Social Provider Handler node does not let end user switch to a different IdP

### 22 Jan 2024

#### Enhancements

* AME-26117: Updated nodes relating to one-time passwords to use secret labels for passwords. Refer to [OTP Email Sender node](https://docs.pingidentity.com/auth-node-ref/latest/otp-email-sender.html) and [OTP SMS Sender node](https://docs.pingidentity.com/auth-node-ref/latest/otp-sms-sender.html).

#### Fixes

* FRAAS-18271: Added the `org.forgerock.opendj.ldap.Dn` and `org.forgerock.opendj.ldap.Rdn` classes to all script contexts

### 19 Jan 2024

#### Key features

* RSA SecurID node (FRAAS-18037)

  The [RSA SecurID](https://docs.pingidentity.com/auth-node-ref/latest/cloud/rsa-securid.html) lets you use the [RSA Cloud Authentication Service (RSA ID Plus)](https://community.rsa.com/s/article/Cloud-Authentication-Service-Overview-235ded8d) or [RSA Authentication Manager](https://community.rsa.com/s/article/How-RSA-Authentication-Manager-Protects-Your-Resources-f6d03a2f) from within an authentication journey on your Advanced Identity Cloud environment.

* Advanced Identity Cloud use case catalog

  Introducing the release of the [Advanced Identity Cloud use case catalog](../use-cases/preface-pages/about-use-case-catalog.html), a collection of guides that focus on tenant administrator use cases and third-party integrations.

### 18 Jan 2024

#### Key features

* Create and manage custom relationship properties (OPENIDM-19106, OPENIDM-19109)

  You can now [create and manage custom relationship properties](../idm-objects/relationships-custom.html) using the Advanced Identity Cloud admin console.

* Schema API improvements (OPENIDM-19107)

  You can now directly modify managed object schemas over REST using the [schema API](../idm-rest-api/endpoints/rest-schema.html). This capability includes configuring custom relationship properties.

* Password timestamps (OPENIDM-19262)

  Enabling this [new feature](../realms/password-policy.html#password-timestamps) lets you view or query when a user password was last changed and when it is set to expire.

#### Enhancements

* OPENIDM-19674: The relationship-defined virtual property (RDVP) schema editor allows you to edit the `flattenProperties` property. The managed object schema editor allows you to edit the `notifyRelationships` property.

#### Fixes

* OPENIDM-18957: The scheduler now attempts to release any triggers it attempted to acquire during a timeout due to an unresponsive repository

* OPENIDM-19141: Workflow engine queries now properly honor `tablePrefix` and `tablePrefixIsSchema` configuration options

* OPENIDM-19279: Resource collection is required to create a relationship

* OPENIDM-19565: The default `apiVersion` configuration has been updated with additional resource paths

### 17 Jan 2024

#### Fixes

* FRAAS-18398: Allow the HTTP OPTIONS method on calls to /openidm/config/\* endpoints for CORS preflight checks

### 09 Jan 2024

#### Fixes

* OPENAM-21856: Introspecting stateless token with IG/Web agents will cause `OAuth2ChfException`

## 2023

### 19 Dec 2023

#### Key features

* Schedule jobs directly in the Advanced Identity Cloud admin console (IAM-3489)

  You can now schedule the following jobs directly in the Advanced Identity Cloud admin console without using the IDM native admin console:

  * Scripts: Execute a script at a regular interval.

  * Task scanner: Execute a scan of identities using a complex query filter at a regular interval. The scan can then execute a script on the identities returned by the query filter.

* New Identity Governance capabilities\[[2](#_footnotedef_2 "View footnote.")] (IAM-4617, IGA-1664)

  The [Workflow UI](../identity-governance/administration/workflow-configure.html) lets you define custom workflow definitions for all access request types.

  [Create a role membership certification template](../identity-governance/administration/template-role-membership-cert.html), a new certification type for access reviews, lets you review and certify roles and the users who have access to roles. Primary reviewers are role owners, a single user, or users assigned to a role.

#### Enhancements

* FRAAS-7382: Add ability to include JavaScript snippets in login and end-user UIs

* IAM-4514\[[2](#_footnotedef_2 "View footnote.")]: Allow reviewers to add user, entitlement, and role columns to an access review

* IAM-4739: Add read schema option to SCIM application template to discover custom schemas/attributes

* IAM-5201: Focus on first input field or button automatically upon page load

* IAM-5268: Add source-missing situation rule to authoritative applications

#### Fixes

* FRAAS-16659: ESV mapping updates aren't captured in promotions report

* IAM-4810: Custom endpoint UI missing context option

* IAM-5072: Inbound mapping tab shows in target applications

* IAM-5171: Azure Active Directory application template doesn't return a user's role membership

* IAM-5187: LDAP v2.1 application template doesn't clear `dc=example,dc=com` base DN

* IAM-5238: LDAP application template is missing the group object classes property

* IAM-5422\[[2](#_footnotedef_2 "View footnote.")]: Entitlement owner doesn't show in the entitlement list

### 15 Dec 2023

#### Fixes

* TNTP-125: Gateway Communication node returns claim values wrapped in double quotes

### 12 Dec 2023

#### Enhancements

* AME-22326\[[16](#_footnotedef_16 "View footnote.")]: The `httpClient` available in scripts now automatically adds the current `transactionId` as an HTTP header. This lets you correlate caller and receiver logs to make requests to other ForgeRock products and services.

* AME-25392\[[16](#_footnotedef_16 "View footnote.")]: Add `org.forgerock.openam.scripting.api.PrefixedScriptPropertyResolver`, used for accessing ESVs from scripts, to the allowlist for `SAML2_SP_ADAPTER` and `SAML2_IDP_ADAPTER` script types

* AME-25433\[[16](#_footnotedef_16 "View footnote.")]: Add `com.sun.crypto.provider.PBKDF2KeyImpl`, `javax.crypto.SecretKeyFactory`, and `javax.crypto.spec.PBEKeySpec` to the allowlists for Scripted Decision nodes and Configuration Provider nodes

* AME-25608\[[16](#_footnotedef_16 "View footnote.")]: Add auditing for opening and closing connections for the LDAP decision node, ID Repo service, and Policy Configuration service

* AME-25630\[[16](#_footnotedef_16 "View footnote.")]: Add `java.security.spec.InvalidKeySpecException` to the allowlist for the Scripted Decision and Configuration Provider nodes

* OPENAM-16897\[[16](#_footnotedef_16 "View footnote.")]: The OAuth 2.0 Device grant flow can now return either JSON or HTML

#### Fixes

* COMMONS-1397\[[16](#_footnotedef_16 "View footnote.")]: Audit event log entries not logged due to thread contention

* FRAAS-17686\[[17](#_footnotedef_17 "View footnote.")]: Add `org.forgerock.json.jose.jwe.JweHeader` to the allowlists for the `AUTHENTICATION_TREE_DECISION_NODE` and `CONFIG_PROVIDER_NODE` script types

* IAM-4401\[[16](#_footnotedef_16 "View footnote.")]: Disabling `Clear-Site-Data` header breaks realm login

* OPENAM-17331\[[16](#_footnotedef_16 "View footnote.")]: Disabled SNS endpoints can now be re-enabled

* OPENAM-17816\[[16](#_footnotedef_16 "View footnote.")]: OAuth 2.0 requests without a `Content-Type` header fail with a 500 error

* OPENAM-19282\[[16](#_footnotedef_16 "View footnote.")]: Recovery Code Display node only works immediately after a registration node

* OPENAM-19889\[[16](#_footnotedef_16 "View footnote.")]: Policy evaluation fails when subject is agent access token JWT

* OPENAM-20026\[[16](#_footnotedef_16 "View footnote.")]: Social IDP with trailing whitespace in the name can't be deleted using the UI

* OPENAM-20329\[[16](#_footnotedef_16 "View footnote.")]: Issuer missing from OAuth 2.0 JARM response

* OPENAM-21053\[[16](#_footnotedef_16 "View footnote.")]: Missing `userId` from access audit log when `org.forgerock.security.oauth2.enforce.sub.claim.uniqueness=false` in JWT client authentication flow

* OPENAM-21421\[[16](#_footnotedef_16 "View footnote.")]: Scripting logger name isn't based on logging hierarchy convention

* OPENAM-21476\[[16](#_footnotedef_16 "View footnote.")]: Persistent cookie is not created when using Configuration Provider node

* OPENAM-21484\[[16](#_footnotedef_16 "View footnote.")]: Introspection of a stateful refresh token for claims field for known OAuth2 fields is now a string and not nested in a list

### 11 Dec 2023

#### Fixes

* FRAAS-18108: Add warning to the **Set up 2-step verification** screen to indicate that 2-step verification will be enforced as of March 1, 2024

### 30 Nov 2023

#### Fixes

* IAM-5275\[[16](#_footnotedef_16 "View footnote.")]: Advanced Identity Cloud admin console doesn't add query parameters to the logout URL

#### Notices

ForgeRock deprecated the option to let Advanced Identity Cloud tenant administrators skip 2-step verification on Friday, February 3, 2023.

The end-of-life date for this deprecation is **Friday, March 1, 2024**, when the skip option functionality will be removed from Advanced Identity Cloud. You have until this date to update your tenants to make 2-step verification mandatory for all tenant administrators. For more information, refer to [Tenant administrator mandatory 2-step verification FAQ](../product-information/migration-dependent-features/tenant-administrator-mandatory-2-step-verification-faq.html).

### 28 Nov 2023

#### Key features

* Duo Universal Prompt node (FRAAS-15675)

  The Duo Universal Prompt node lets you provide two-factor authentication using Duo's Universal Prompt authentication interface. You can integrate Universal Prompt with your web applications using the [Duo Web v4 SDK](https://duo.com/docs/duoweb).

  For details, refer to [Duo Universal Prompt node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/duo-univ-prompt.html).

### 27 Nov 2023

#### Enhancements

* FRAAS-17939\[[18](#_footnotedef_18 "View footnote.")]: Some connectors included with Advanced Identity Cloud were upgraded to the following versions:

  1.5.20.19

  For details, refer to [1.5.20.19 Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html#1_5_20_19).

  * Microsoft Graph API connector

  * SCIM connector

  1.5.20.18

  For details, refer to [1.5.20.18 Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html#1_5_20_18).

  * Google Apps connector

  * Microsoft Graph API connector

  * Salesforce connector

  * SCIM connector

  * Workday connector

- OPENIDM-19037: Update property value substitution to reflect boolean value in the UI

#### Fixes

* IAM-5289: Fix warning message when `maxidletime` is greater than 24.8 days

* OPENIDM-19328: Fix queued sync to recover following node restart

### 17 Nov 2023

#### Enhancements

* IAM-4511: Hide fields in the Users & Roles tab when editing and creating unreadable properties

* IAM-4615: Add a "Skip to main content" link to page headers

#### Fixes

* IAM-4991: When a `suspendedId` is in use, redirect to `failureUrl` fails

* IAM-5075: Login messages are read twice by screen readers

* IAM-5186: User identity related values aren't saved after removal

### 13 Nov 2023

#### Fixes

* FRAAS-17883: Tenant administrators cannot save edits to their personal information

* IAM-5226: Tenant administrator security questions should not be shown when editing personal information

* IAM-5240: No error message displays when a tenant administrator fails to save edits to their personal information

### 31 Oct 2023

#### Key features

* next-generation scripting enhancements (AME-25928)

  The next-generation scripting engine for journey decision node scripts lets you:

  * Reduce the need to allowlist Java classes with a stable set of enhanced bindings.

  * Simplify scripts with fewer imports and more intuitive return types that require less code.

  * Debug efficiently with clear log messages and a simple logging interface based on SLF4J.

  * Make requests to other APIs from within scripts with a more intuitive HTTP client.

  * Modularize your scripts by reusing common code snippets, including external libraries such as CommonJS, with library scripts.

  * Access identity management information seamlessly through the `openidm` binding.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The next-generation engine can't use legacy scripts.If your [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) uses legacy scripts, you must convert them to use updated bindings to take advantage of the benefits of the next-generation scripting engine.Where possible, you should migrate legacy scripts to take advantage of next-generation stability. |

  For more information, refer to [Next-generation scripts](../am-scripting/next-generation-scripts.html).

#### Enhancements

* FRAAS-3841: Activate and deactivate journeys in the Advanced Identity Cloud admin console. Refer to [Deactivate journeys](../journeys/journeys.html#deactivate-journeys).

* IAM-4191: Allow tenant session cookie name to be configured. Refer to [Session cookie name](../am-sessions/about-sessions.html#proc-change-session-cookie).

* IAM-4735: Add support for schema discovery in application templates

* IAM-4806: Show outbound tenant IP addresses in Advanced Identity Cloud admin console. Refer to [Access global settings](../tenants/tenant-settings.html#access-global-settings).

* IAM-4853: Add AS400 application template. Refer to the [AS400](../app-management/provision-an-application.html#provision-as400) section in [Provision an application](../app-management/provision-an-application.html).

#### Fixes

* FRAAS-16785: Incorrect positioning of reCAPTCHA v2 elements

* IAM-2936: Journeys hang indefinitely when using a State Metadata node within a Page node

* IAM-4521: Screen readers announce field labels twice

* IAM-4956: Advanced Identity Cloud admin console doesn't use the current realm when logging out

* IAM-5113: Unable to remove an NAO assignment from a user in Advanced Identity Cloud admin console

### 19 Oct 2023

#### Key features

* Gateway Communication node (FRAAS-17380)

  Lets Advanced Identity Cloud authentication journeys communicate directly with the [PingGateway](../realms/gateways-agents.html#identity-gateway) (PingGateway).

  This secure communication channel extends the Advanced Identity Cloud capabilities with PingGateway features, such as validating a Kerberos ticket and performing other certificate handshakes.

  For details, refer to [Gateway Communication overview](https://docs.pingidentity.com/auth-node-ref/latest/cloud/gateway-communication.html).

### 16 Oct 2023

#### Key features

* New Autonomous Access capabilities\[[19](#_footnotedef_19 "View footnote.")] (DATASCI-1269)

  Autonomous Access User access behavior and tenant access behavior let end users understand their "normal" login behavior for the past six months by graphically displaying key access metrics on a UI. Users can filter the UI to show certain login metrics, like time of day, city, country, day of week, device used for login, operating system, and browser type. Users can also compare an individual user's login behavior to that of the access attempts for all other users.

#### Enhancements

* IAM-4211: Display disaster recovery region in the Advanced Identity Cloud admin console

* IAM-4369: Remove AM applications from application list view

* IAM-5045: Display pop-up warning when an end user is about to be logged out of an Advanced Identity Cloud hosted page

#### Fixes

* IAM-4812: Correctly save array ESVs containing newline characters

* IAM-4863: Display ESV buttons properly when the user gives them focus

* IAM-4877: Display ESV selection button properly while user is modifying a script associated with a Scripted Decision node

* IAM-4698: Fix accessibility issues with messages in page nodes

### 13 Oct 2023

#### Enhancements

* FRAAS-17373\[[20](#_footnotedef_20 "View footnote.")]: The following connectors included with Advanced Identity Cloud were upgraded from 1.5.20.15 to 1.5.20.17:

  * Adobe Marketing Cloud connector

  * Google Apps connector

  * Microsoft Graph API connector

  * Salesforce connector

  * SCIM connector

  Some highlights include:

  * OPENICF-900: SCIM connector: Add support for dynamically generated SCIM schemas

  * OPENICF-2453: SCIM connector: Persist optional refresh token upon successful access token renewal

  For a complete list of enhancements and fixes, refer to [Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html).

#### Fixes

* ANALYTICS-311: The `USER-LAST-LOGIN` report doesn't show results if the last journey failed

* FRAAS-17413: Improve IDM service reliability during upgrades and routine maintenance

* OPENICF-1723: Salesforce connector: Clarify usage of `proxyUri` configuration property

* OPENICF-2297: SCIM connector: Roles attribute should be a list of `Strings`, not a list of `Objects`

* OPENICF-2482: SCIM connector: Dynamic schema doesn't default to static schema on all exceptions

* OPENICF-2483: SCIM connector: Creating a user with special attributes fails with dynamically generated schema

* OPENICF-2484: SCIM connector: PUT with `schemas` attribute fails for providers that support PATCH

* OPENICF-2448: SCIM connector: HTTP client fails to handle OAuth 2.0 errors

### 12 Oct 2023

#### Key features

* OneSpan Get User Authenticator node (FRAAS-17378)

  Retrieves the authenticators assigned to a user and helps enable user's authentication and security levels.

  For details, refer to [OneSpan Get User Authenticator node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-get-user-authenticator.html).

* OneSpan Identity Verification node (FRAAS-17378)

  Sends request to OneSpan to analyze the image and determine whether the document is genuine or fraudulent.

  For details, refer to [OneSpan Identity Verification node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-id-verify.html).

### 03 Oct 2023

#### Fixes

* FRAAS-17283: Tenant status pages not automatically updated during downtime

* IAM-4235: Passthrough authentication using AD connector fails if set up in UI and user DN includes a space

* IAM-4903: API calls to IGA endpoints not working with custom domain

* IAM-4915: User details modal for IGA access review shows manager details as JSON object

* OPENIDM-19192: Personal information is still editable by end users when User Editable is set to `false`

### 25 Sep 2023

#### Enhancements

* IAM-4515\[[21](#_footnotedef_21 "View footnote.")]: Include autocomplete attribute with login form fields

* IAM-4525\[[21](#_footnotedef_21 "View footnote.")]: Update profile picture modal with accessibility improvements for screen readers

* IAM-4576\[[21](#_footnotedef_21 "View footnote.")]: Increase time on screen for loading spinner so that screen readers can announce it

* IAM-4616\[[21](#_footnotedef_21 "View footnote.")]: Include contextual information with the show/hide buttons for improved accessibility

#### Fixes

* FRAAS-17278: Health status reports for `AM`, `IDM`, and `platform-admin` services incorrectly reported as available in some situations

* IAM-4460\[[21](#_footnotedef_21 "View footnote.")]: Screen readers read show/hide buttons for security questions as show/hide password

* IAM-4523\[[21](#_footnotedef_21 "View footnote.")]: Screen readers read avatar alt text when tabbing to action menu

* IAM-4524\[[21](#_footnotedef_21 "View footnote.")]: Two buttons with different labels open the same dialog

### 22 Sep 2023

#### Fixes

* FRAAS-17235: Validate ESV values correctly when they are wrapped in white space

### 20 Sep 2023

#### Key features

* New Identity Governance capabilities\[[2](#_footnotedef_2 "View footnote.")] (IGA-1691)

  [Access requests](../identity-governance/administration/access-request-preface.html) let end users request access to resources and let managers request that access be removed from their delegates. The list of resources an end user can request access to is referred to as the *access catalog*.

  [Manage access request workflows](../identity-governance/administration/workflow-configure.html) is a new feature that lets you optionally define flows to include business logic, decisions, and approvals. For example, decide what happens when an approver rejects an access request for an application. Workflows currently only supports access request-related features.

  [New options](../end-user/hosted-pages-account.html#end-user-menu-items) in the hosted account pages let end users submit access requests, submit requests to remove access, and review assigned request items:

  * The My Requests option lets you view and create access requests to resources (applications, roles, entitlements) for yourself or on behalf of others.

  * The My Directory > Direct Reports option lets managers submit access removal requests.

  * The Inbox > Approvals option lists request items (requests an end user submits) for an approver (designated owner) to act on.

#### Enhancements

* IAM-3648: ESV placeholders can now be entered from a drop-down list

* IAM-3651: ESV placeholders can now be entered from key-value input fields

* IAM-4236: Improve layout of the applications reconciliation tab

* IAM-4367: Separate the connection status of OAuth 2.0 client applications into a dedicated list

* IAM-4662: ESV placeholders can now be entered from tag input fields

* IAM-4717: Added date, datetime, and time fields to the login UI

* IAM-4789: Grant roles now show temporal constraints

* OPENAM-20847: Sanitized HTML can now be added into messages for the Email Suspend node

#### Fixes

* IAM-4418: Fix accessibility issues with multi-select input fields

* IAM-4489: Align checkbox color with other form elements

* IAM-4491: Correctly label sidebar buttons when expanded or collapsed

* IAM-4492: Make navigation bars in end-user UI accessible for screen readers

* IAM-4798: The `aria-label` is now correctly displayed for all component types on sidebar buttons

* IAM-4843: The user column in the certification task list now shows a user's full name instead of only the first name

* IAM-4528: Outbound reconciliation mapping preview shows generated password value

### 19 Sep 2023

#### Enhancements

* OPENAM-21416: Canada Central AWS region (ca-central-1) enabled for the PingAM push notification service

### 15 Sep 2023

#### Key features

* Query Parameter node (AME-24069)

  Allows you to insert query parameter values from a journey URL into configurable node state properties. This lets you customize journeys based on the query parameter values.

  For details, refer to [Query Parameter node](https://docs.pingidentity.com/auth-node-ref/latest/query-parameter.html).

#### Enhancements

* OPENAM-21073: Request headers are now accessible in OAuth 2.0/OIDC scripts for `OIDC_CLAIMS`, `OAUTH2_ACCESS_TOKEN_MODIFICATION`, and `OAUTH2_MAY_ACT` script contexts using the `requestProperties` binding

* OPENAM-21355: Jakarta AWS region (ap-southeast-3) enabled for the PingAM push notification service

#### Fixes

* IAM-4639: String/password field button is highlighted in the UI

* IAM-4829: Eye icon displays over the password field highlight box in the UI

* OPENAM-18599: Allow customization of the error message that displays to end users when their account is locked or inactive using `.withErrorMessage()` in a Scripted Decision node

* OPENAM-18685: Use the OAuth2 Provider service in the AM native admin console to specify if tokens issued should contain the `subname` claim

* OPENAM-19261: Errors are incorrectly logged when triggered by introspection of tokens using OAuth 2.0 client credentials grant

* OPENAM-20451: The WebAuthn Registration node now displays an end user's `userName` when registering a device when the identity's name isn't human-readable

* OPENAM-21158: Add support for trusted platform module (TPM) attestation using elliptic curve cryptography (ECC) unique parameter validation starting with Windows 11 version 22H2

* OPENAM-21304: The `request_uris` field does not populate when OAuth 2.0 clients register using dynamic client registration

* OPENAM-21390: Fix caching error to correctly provide data to `nodeState` when a journey switches server instances

### 11 Sep 2023

#### Enhancements

* IAM-3650: Add a drop-down menu to checkbox inputs for selecting ESV placeholders

* IAM-3826: Add the ability to specify a source and transformation script when mapping application properties. For details, refer to [app-management:provision-an-application.adoc#apply-a-transformation-script-to-a-mapping](../app-management/provision-an-application.html#apply-a-transformation-script-to-a-mapping).

* IAM-4567: Add a warning when running reconciliations and selecting the `persistAssociations` option. For details, refer to [View a report about the last reconciliation](../app-management/provision-an-application.html#view_a_report_about_the_last_reconciliation).

#### Fixes

* IAM-4366: Provide browser-specific logic to handle alternative CSS for accessibility

* IAM-4409: Require at least three characters before running identity searches when there are more than 1000 identities of that type

* IAM-4478: Only allow certain combinations of properties in a mapping transformation script

* IAM-4493: Fix the heading hierarchy in the UI

* IAM-4568: Do not enable the option to change a user association in the UI

* IAM-4703: Fix display of password fields in some themes

* IAM-4710: Fix rounded border of password fields in hosted pages

### 06 Sep 2023

#### Enhancements

* OPENAM-21346: Add classes `java.util.concurrent.TimeUnit`, `java.util.concurrent.ExecutionException`, and `java.util.concurrent.TimeoutException` to the scripting allowlist

### 22 Aug 2023

#### Key features

* Salesforce Community User application template (IAM-4340)

  Provision, reconcile, and synchronize Salesforce, Salesforce Portal, and Salesforce Community accounts.

  For details, refer to [Salesforce application template or Salesforce Community User application template](../app-management/provision-an-application.html#provision-salesforce)

* Add preference-based provisioning to Privacy and Consent settings (IAM-4243)

  End users in target applications can share their data with other applications. After the end user configures a preference to share data with other applications, data from the target application is synchronized with Advanced Identity Cloud.

  For details, refer to [End-user data sharing](../app-management/provision-an-application.html#end-user-data-sharing)

### 18 Aug 2023

#### Key features

* OneSpan Auth VDP User Register node (FRAAS-15426)

  Registers users to authenticate using the virtual one-time password (VOTP). For details, refer to [OneSpan Auth VDP User Register node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-vdp-register.html).

* OneSpan Auth Assign Authenticator node (FRAAS-15426)

  Assigns VIR10 authenticator to the user when there's a VIR10 authenticator available in the tenant and the user isn't assigned a VIR10 authenticator. For details, refer to [OneSpan Auth Assign Authenticator node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-assign-authn.html).

* OneSpan Auth Generate VOTP node (FRAAS-15426)

  Generates and delivers a virtual one-time password (VOTP) through the delivery method configured in the node if there's a VIR10 authenticator assigned to the user. For details, refer to [OneSpan Auth Generate VOTP node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-generate-votp.html).

### 14 Aug 2023

#### Fixes

* IAM-4533: Journeys do not resume correctly when returning from a social identity provider without a realm identifier

* IAM-4534: Redirect callbacks for journeys not working correctly

### 09 Aug 2023

#### Enhancements

* AME-25061\[[22](#_footnotedef_22 "View footnote.")]: Provide additional context information in Marketplace authentication nodes to enable UI improvements

* OPENAM-20772\[[22](#_footnotedef_22 "View footnote.")]: Add new option to the CAPTCHA node to let the submit button be disabled until CAPTCHA verification is successful

#### Fixes

* OPENAM-18004\[[22](#_footnotedef_22 "View footnote.")]: Audit logging does not specify transaction IDs correctly for internal requests to certain APIs

* OPENAM-18709\[[22](#_footnotedef_22 "View footnote.")]: Calls to the `nodeState.get()` method in Scripted Decision nodes do not return values in shared state when a variable is stored in both shared state and secure state

* OPENAM-20230\[[22](#_footnotedef_22 "View footnote.")]: Calls to classes in the allowlist fail occasionally with access prohibited messages

* OPENAM-20682\[[22](#_footnotedef_22 "View footnote.")]: Unable to encrypt `id_token` error when there are multiple JWKs with the same key ID but different encryption algorithms

* OPENAM-20691\[[22](#_footnotedef_22 "View footnote.")]: Session quota reached when oldest session is not destroyed due to race condition

* OPENAM-20783\[[22](#_footnotedef_22 "View footnote.")]: Logging is incorrect when the authorization code grant flow is used successfully

* OPENAM-20920\[[22](#_footnotedef_22 "View footnote.")]: Null pointer exceptions when a SAML 2.0 binding is null and the SSO endpoint list contains non-SAML 2.0 entries

* OPENAM-20953\[[22](#_footnotedef_22 "View footnote.")]: Policy evaluation with a subject type `JwtClaim` returns HTTP response code 500

* OPENAM-20980\[[22](#_footnotedef_22 "View footnote.")]: The OIDC social provider is unable to use an issuer's comparison check regex

* OPENAM-21001\[[22](#_footnotedef_22 "View footnote.")]: Custom scripted SAML 2.0 IDP account mappers are determined incorrectly

* OPENAM-21004\[[22](#_footnotedef_22 "View footnote.")]: Invalid session ID error when session management is disabled in an OIDC provider

* OPENAM-21046\[[22](#_footnotedef_22 "View footnote.")]: The Create Object and Patch Object nodes do not log exception stack traces when they can't retrieve the object schema

* OPENAM-21164\[[22](#_footnotedef_22 "View footnote.")]: XML string formatted incorrectly when using a custom adapter to get the assertion from a SAML 2.0 response

### 31 Jul 2023

#### Enhancements

* IAM-3502: Add the ability to set and reset a sync token for identity management account object type. For details, refer to [Reset the last reconciliation job](../app-management/provision-an-application.html#reset_the_last_reconciliation_job).

* IAM-3678: Update error messages and labels in login and signup pages

* IAM-3962: Improve design of push number challenge page for Push Wait node

* IAM-4248: Add three additional non-account objects to ServiceNow page

* IAM-4326: Improve onLink script to handle mapped properties of type array and object

* IAM-4334: Update SuccessFactors application templates to support Advanced Identity Cloud built-in SuccessFactors connector

#### Fixes

* IAM-3877: UI loader spins indefinitely when realm is deactivated

* IAM-4093: Replace Google Fonts in the login UI to meet GDPR compliancy requirements

* IAM-4176: Advanced setting query filter does not show all available properties

* IAM-4240: Accessibility issues in Page node when NVDA readers are used

* IAM-4261: Accessing end-user UI with query parameter "code" displays empty page

* IAM-4371: Unable to create applications due to `userpassword` property set

* IAM-4384: Platform UI does not resume journeys with custom redirect logic

* IAM-4427: Platform UI does not show assignments for tenants running deprecated application management

* IAM-4475: Platform UI does not load after tenant administrator signs into an upper tenant during promotion

### 25 Jul 2023

#### Fixes

* FRAAS-16471: ESV `variables` and `secrets` API endpoints slow for large result sets

### 17 Jul 2023

#### Fixes

* OPENIDM-18292\[[23](#_footnotedef_23 "View footnote.")]: Add support for the `_fields` request parameter to the sync `getTargetPreview` endpoint

* OPENIDM-18898\[[23](#_footnotedef_23 "View footnote.")]: Add support for the `_countOnly` parameter in identity management scripts

* OPENIDM-18980\[[23](#_footnotedef_23 "View footnote.")]: Add a new metric to measure the duration of a LiveSync event

* OPENIDM-19098\[[23](#_footnotedef_23 "View footnote.")]: Enable ES6 support for identity management scripts

### 13 Jul 2023

#### Fixes

* FRAAS-16271: ESV secrets could be incorrectly marked as "not loaded" when tenant has many ESVs

### 26 Jun 2023

#### Fixes

* IAM-4289: Unable to assign non-account object properties to roles

* IAM-4293: Access reviews and line items not shown for staged campaigns

* IAM-4295: Reviewer not redirected back to pending reviews after access review sign off

### 22 Jun 2023

#### Enhancements

* DATASCI-1331\[[24](#_footnotedef_24 "View footnote.")]: Distributed attack heuristics

* DATASCI-1677\[[24](#_footnotedef_24 "View footnote.")]: Support the right to access or be forgotten (GDPR compliance)

* IAM-2026: Support versioning of the application and connector templates

* IAM-3408: Let provisioners use a range of connector versions

* IAM-4074: Add a loading animation to the pie chart component

* IAM-4242: Add "Conflicting changes" category to reconciliation summary

#### Fixes

* FRAAS-9230: Sanitize `aria-hidden` fields

* FRAAS-16041: Users can choose Basic Auth for Identity Cloud logging endpoints

* IAM-2972: Route users to the correct realm after granting Salesforce permissions

* IAM-3719: Modals not showing display access review comments and activity

* IAM-4116: Don't let access review users add reviewers with greater privileges than they themselves have

* IAM-4134: User pop-up is visible in "Entitlement" tab

* IAM-4200: Last certified date, decision, and actor displaying incorrectly in Governance account details

### 19 Jun 2023

#### Enhancements

* IAM-4051: Improved ADA accessibility for drop-down boxes

* IAM-4053: Improved ADA accessibility when NVDA readers are used on pages that use the Page node

### 16 Jun 2023

#### Fixes

* FRAAS-15974: Unable to promote empty configuration to reset staging environment

### 14 Jun 2023

#### Key features

* New Identity Governance capabilities\[[2](#_footnotedef_2 "View footnote.")] (IGA-1592)

  [Entitlements](../identity-governance/administration/entitlements.html) are specific permissions given to an account in an onboarded target application. Each entitlement correlates to a permission. Pull in entitlements from all onboarded target applications into Advanced Identity Cloud for use in certifications.

  [Entitlement assignment certification](../identity-governance/administration/template-entitlement-cert.html), a new certification type for access reviews, lets you review and certify entitlements and the users who have access to entitlements on some or all applications. Primary reviewers are entitlement owners, a single user, or users assigned to a role.

  The [governance glossary](../identity-governance/administration/glossary.html) lets you attach business-friendly attributes to applications, entitlements, and roles to add more specificity to the data you review in access certifications.

  [New options](../end-user/hosted-pages-account.html#end-user-menu-items) in the hosted account pages let you view your access, your direct reports, and the access your direct reports have:

  * The My Access option lets you view your access in Advanced Identity Cloud and onboarded target applications. This includes accounts from onboarded target applications, roles you are assigned in Advanced Identity Cloud, and entitlements or privileges you have in onboarded target applications.

  * The Direct Reports option lets you get access information for individuals you manage. This includes their profile information, accounts from onboarded target applications, roles they are assigned in Advanced Identity Cloud, and entitlements or privileges they have in onboarded target applications.

* Microsoft Graph API email client (OPENIDM-17899)

  Configure the email client to use the MS Graph API Client for sending email.

  For more information, refer to [Microsoft Graph API email client](../tenants/email-provider.html#ms_graph_api_requirements).

#### Enhancements

* IAM-2826: Filter the "Assignments" tab for identities so that it does not show overrides, entitlements, or resources

* IAM-3677: Remove increment/decrement arrows from numeric input fields

* IAM-3982: Let users filter risk activity using distributed attack as a risk reason

* IAM-3983: Show distributed attack as a risk reason in the risk dashboard

* IAM-4136: Use the tab key to move focus and remove tags in multi-select components

#### Fixes

* FRAAS-14262: Include changes to group privileges in the configuration promotions report

* IAM-2713: Prohibit editing of managed application objects

* IAM-3594: Correctly redirect control to the End User UI after authenticating with itsme

* IAM-3939: Let end users switch to a different authentication journey

* IAM-4013: When using a custom domain, `originalLoginRealm` is set incorrectly

* OPENIDM-17481: Managed object schema can now describe a field as a nullable array and specify a default value for this field if not provided in a create request

* OPENIDM-17771: Processing of a large number of scheduled jobs no longer causes all scheduled tasks to continuously misfire

* OPENIDM-18192: Updating a relationship-defined virtual property (RDVP) on a managed object by signal receipt no longer causes other RDVP state within that object to be lost

* OPENIDM-18360: Use the full object state when validating requests made by a delegated administrator to modify a relationship

* OPENIDM-18613: Provide the ability to remove the `userPassword` attribute

* OPENIDM-18644: Correctly determine whether it's possible to configure clustered reconciliation

* OPENIDM-18895: Fixes support for multi-version concurrency control on managed object patches and updates

### 13 Jun 2023

#### Fixes

* FRAAS-14706: Improve the detection of changes to complex configuration files and IDM script hooks in promotion reports

* FRAAS-14897: Improve the rate limiting behavior of the `/monitoring/logs` endpoint

### 08 Jun 2023

#### Key features

* Lexis-Nexis ThreatMetrix Authentication nodes (FRAAS-15325)

  Integrate [Lexis-Nexis ThreatMetrix](https://risk.lexisnexis.com/products/threatmetrix) decision tools and enable device intelligence and risk assessment in Advanced Identity Cloud.

  For details, refer to [ThreatMetrix Authentication nodes](https://docs.pingidentity.com/auth-node-ref/latest/cloud/threat-metrix.html).

#### Fixes

* FRAAS-14214: Changing an existing ESV type is now denied by the API and new ESVs always require an explicit type

### 05 Jun 2023

#### Key features

* Filter log results

  Use the `_queryFilter` parameter to filter log results on any field or combination of fields in a payload. For details, refer to [Filter log results](https://docs.pingidentity.com/pingoneaic/tenants/audit-debug-logs.html#filter-log-results).

#### Fixes

* FRAAS-15378: Add `_queryFilter` support to `/monitoring/logs` and `/monitoring/logs/tail` endpoints

### 30 May 2023

#### Key features

* Scripted SAML 2.0 SP adapter

  Customize the SAML 2.0 SP adapter using a script.

  For details, refer to [SP adapter](../am-saml2/custom-sp-adapter.html).

* OIDC ID Token Validator node

  The new OIDC ID Token Validator node lets Advanced Identity Cloud rely on an OIDC provider's ID token to authenticate an end user. The node evaluates whether the ID token is valid according to the [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html#IDTokenValidation).

  For details, refer to [OIDC ID Token Validator node](https://docs.pingidentity.com/auth-node-ref/latest/oidc-idtoken-validator.html).

#### Fixes

* AME-21638: Customize an SP adapter by using a script

* AME-24026: Allow specifying inputs required by the provider scripts in the Configuration Provider node

* AME-24073: Expose the `prompt_values_supported` parameter of the provider configuration at the OIDC well-known endpoint

* AME-24175: Provide additional classes in the allowlist that scripts used in the Scripted Decision node

* OPENAM-12030: Authentication node instances are deleted when journeys containing them are deleted

* OPENAM-13293: New OIDC ID Token Validator node evaluates whether the ID token is valid according to the OIDC specification

* OPENAM-13329: Display journeys with spaces in their name in the Authentication Configuration drop-down menu

* OPENAM-13766: Route user session based on whether policy evaluation is requested or not

* OPENAM-17179: Correctly delete a script if its referring journey is deleted

* OPENAM-17566: Display account name instead of UUID in the ForgeRock Authenticator when using MFA

* OPENAM-18488: Support certificate-based attestation in certificate chains terminating at an intermediate CA

* OPENAM-18692: Set the minimum value for the Default Max Age property to 0

* OPENAM-19745: Add support for EdDSA signing algorithm to WebAuthn Registration node

* OPENAM-20082: Show correct error message to locked out users

* OPENAM-20104: Fix the fragment response mode for the OAuth 2.0 authorize endpoint

* OPENAM-20187: Fix the "waiting for response" page so that it fails authentication as configured in the authentication journey

* OPENAM-20230: Prevent class allowlist from failing for classes already on the allowlist

* OPENAM-20318: Allow a restricted set of HTML tags to be rendered in page node headers and descriptions

* OPENAM-20360: Fix default URL encoding to ensure ampersand characters are not double encoded in a SAML assertion

* OPENAM-20386: Fix authentication node state reconciliation in some complex journeys

* OPENAM-20396: Preserve ordering of ACR to chain mapping configuration of OIDC provider after a restart

* OPENAM-20451: Fix WebAuthn registration node to return a human-readable username

* OPENAM-20457: Route Device Location Match node to "Unknown Device" outcome when the previously stored location of the device is not provided

* OPENAM-20479: Enhance OIDC authentication to handle unsecured JWS requests

* OPENAM-20541: Add additional inner classes to scripting allowlist to support RSA key pair generation

### 24 May 2023

#### Fixes

* FRAAS-14956: Promotion preview and report not showing all configuration changes

### 23 May 2023

#### Fixes

* FRAAS-10816: Include thread ID and remove control characters from some Identity Cloud log files for easier log correlation

### 18 May 2023

#### Key features

* Administrator federation enhancements

  **Groups support**: The new groups feature allows you to add and remove administrators depending on group membership in your identity provider. Using administration groups lets you automate the granting and removing of access for administrators that are being on-boarded, switching roles, or leaving your organization.

  **OIDC Federation**: OIDC is now supported as a federation identity provider, along with Microsoft ADFS and Microsoft Azure.

  For more information, refer to [Configure federated access for tenant administrators](../federation/configure-federated-access-for-tenant-administrators.html).

#### Enhancements

* DATASCI-1267\[[25](#_footnotedef_25 "View footnote.")]: Autonomous Access dashboard is now realm-based

* DATASCI-1330\[[25](#_footnotedef_25 "View footnote.")]: Autonomous Access can use blocklists and allowlists of IP addresses

* DATASCI-1336\[[25](#_footnotedef_25 "View footnote.")]: Autonomous Access can avoid putting users in double jeopardy

### 17 May 2023

#### Fixes

* FRAAS-13293: Provide more accurate and granular information in promotion reports

* FRAAS-14063: Remove orphaned unused scripts during promotion

* FRAAS-15022: Improve promotion reports

* FRAAS-15188: Ensure environments can be recreated after deletion

* IAM-2561: Allow adding applications to a user or role from the Identities > Manage page

* IAM-3550: When attempting to validate Office 365 applications, a blank screen appears

* IAM-3580: Improve service accounts UI including error handling

* IAM-3666: Add alternative text to QR code image

* IAM-3676: Add keyboard controls to UI to select multiple values in multivalued lists

* IAM-4030: Improve handling of identity provider and groups claims

* IAM-4031: Generic OIDC configuration returns HTTP 400 Bad Request

* IAM-4032: Federation enforcement is missing from the UI

* IAM-4058: Admin UI routing for locked tenants is no longer working correctly

### 15 May 2023

#### Fixes

| Issue ID    | Summary                                                    |
| ----------- | ---------------------------------------------------------- |
| FRAAS-12469 | Automatically create a status page account for new tenants |

### 05 May 2023

#### Fixes

| Issue ID\[[26](#_footnotedef_26 "View footnote.")] | Summary                                       |
| -------------------------------------------------- | --------------------------------------------- |
| IAM-3043                                           | CAPTCHA node not behaving properly when false |

### 04 May 2023

#### Fixes

| Issue ID     | Summary                                               |
| ------------ | ----------------------------------------------------- |
| OPENAM-20815 | Auth session timeout causes missing login page footer |

### 03 May 2023

#### Fixes

| Issue ID | Summary                                           |
| -------- | ------------------------------------------------- |
| IAM-3937 | Risky events are not shown in the risk dashboard  |
| IAM-3964 | Risk reasons do not display in the risk dashboard |

### 26 Apr 2023

#### Key features

* PowerShell connector

  Use the PowerShell Connector Toolkit to register a connector that can provision any Microsoft system.

  For details, refer to [PowerShell](../app-management/provision-an-application.html#provision-powershell).

* SAP SuccessFactors Account or SAP SuccessFactors HR connector

  Use the SAP SuccessFactors connectors to synchronize SAP SuccessFactors users with Advanced Identity Cloud users.

  For details, refer to [SAP SuccessFactors Account or SAP SuccessFactors HR](../app-management/provision-an-application.html#provision-successfactors).

* Bookmark application

  You can now register a bookmark application - for example, OneNote, Evernote, Google Bookmarks, or raindrop.io - to direct users to specific URLs. A bookmark application displays shortcut links on dashboards. When you click one of the links, the browser opens a new tab.

  For details, refer to [Bookmark](../app-management/register-a-custom-application.html#bookmark).

#### Resolved issues

| Issue ID      | Summary                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------- |
| IAM-2911      | Add support for bookmark apps in application management                                   |
| IAM-3472      | Update promotions UI to set tenant color dynamically based on the tenant name             |
| IAM-3630      | Add SuccessFactors template and connector configuration                                   |
| IAM-3666      | Add alt text to QR code                                                                   |
| IAM-3667      | Add visual indication of keyboard focus on input fields                                   |
| IAM-3681      | Improve accessibility of the `Edit personal info` profile dialog                          |
| IAM-3778      | Allow login UI to work when browser session storage is unavailable                        |
| IAM-3792      | Prevent login UI rendering extra whitespace character in front of text on suspended nodes |
| IAM-3806      | Remove beta indicator from the trends chart in admin UI dashboard                         |
| IAM-3840      | Change color of radio button changed in Choice Collector node                             |
| IAM-3879      | Ensure global variable `assignmentResCollection` is not overwritten when editing scripts  |
| IAM-3910      | New PowerShell configuration properties                                                   |
| OPENAM-18895  | Fix API request timeout errors for slow connections                                       |
| OPENIDM-18917 | Display last name instead of user ID on user profile when no first name is provided       |
| OPENAM-20815  | Add missing footer to Page node when session expired                                      |

### 25 Apr 2023

#### Resolved issues

| Issue ID      | Summary                                                                                 |
| ------------- | --------------------------------------------------------------------------------------- |
| OPENIDM-18967 | Remove unnecessary `&_sortKeys=_id` parameter from `dataRelationshipArray` grid queries |
| OPENIDM-18988 | Prevent repository reads when anonymous users make requests to info and ping endpoints  |

### 24 Apr 2023

#### Key features

* Microsoft Intune node

  Integrates [Microsoft Intune](https://learn.microsoft.com/en-us/mem/intune/fundamentals/what-is-intune) to control features and settings on Android, Android Enterprise, iOS/iPadOS, macOS, and Windows 10/11 devices in your organization.

  For details, refer to [Microsoft Intune node](https://docs.pingidentity.com/auth-node-ref/latest/cloud/microsoft-intune-about.html).

* Secret Double Octopus (SDO) nodes

  PingOne Advanced Identity Cloud integrates with [Secret Double Octopus (SDO)](https://doubleoctopus.com/solutions/passwordless-mfa/) to provide high-assurance, passwordless authentication systems that address the diverse authentication needs of a real-world, working enterprise.

  For details, refer to [Secret Double Octopus (SDO) nodes](https://docs.pingidentity.com/auth-node-ref/latest/cloud/secret-double-octopus.html).

#### Resolved issues

| Issue ID | Summary                                                                       |
| -------- | ----------------------------------------------------------------------------- |
| IAM-3950 | End-user UI fails to load when accessing Advanced Identity Cloud in a new tab |

### 12 Apr 2023

#### Resolved issues

| Issue ID    | Summary                                     |
| ----------- | ------------------------------------------- |
| FRAAS-13247 | Set the log API key creation date correctly |

### 06 Apr 2023

#### Key features

* Support for all Google Fonts for hosted pages

  Meet your organization's brand guidelines by using any [Google Font](https://fonts.google.com/) in your hosted pages.

#### Resolved issues

| Issue ID                                         | Summary                                                                          |
| ------------------------------------------------ | -------------------------------------------------------------------------------- |
| IAM-1686                                         | Allow any Google Font to be used on hosted pages                                 |
| IAM-3164                                         | Prevent table columns from stacking vertically on smaller viewports              |
| IAM-3313\[[2](#_footnotedef_2 "View footnote.")] | Additional Options section missing from Identity Certification campaign template |

### 30 Mar 2023

#### Key features

* IP allowlisting

  Enterprises often need to ensure that requests entering their network come from trusted sources. PingOne Advanced Identity Cloud now offers outbound static IP addressess for sandbox environments.

  Outbound static IP addresses let you implement network security policies by setting up allowlists of IPs originating from Advanced Identity Cloud. This adds an extra layer of security to outbound calls to your APIs or SMTP servers.

  For more information, refer to [Outbound static IP addresses](../tenants/environments-outbound-static-ip-addresses.html).

#### Resolved issues

| Issue ID   | Summary                                                             |
| ---------- | ------------------------------------------------------------------- |
| FRAAS-5995 | Outbound request static IP allows IP allowlisting for new customers |

### 29 Mar 2023

#### Resolved issues

| Issue ID    | Summary                                                                           |
| ----------- | --------------------------------------------------------------------------------- |
| FRAAS-14187 | Updated user registration cloud logging to capture events from identity providers |
| FRAAS-14593 | The Configuration Provider node was unable to retrieve ESVs                       |

### 27 Mar 2023

#### Resolved issues

| Issue ID    | Summary                                                |
| ----------- | ------------------------------------------------------ |
| FRAAS-14475 | Certain searches cause `NoSuchElementException` errors |

### 20 Mar 2023

#### Resolved issues

| Issue ID      | Summary                                                                                      |
| ------------- | -------------------------------------------------------------------------------------------- |
| OPENIDM-18476 | The IDM admin UI now defaults identity object number fields to `0` instead of an empty value |
| OPENIDM-18216 | IDM admin UI should query recon association data instead of audit data                       |
| OPENIDM-18870 | Inability to delete an inline reconciliation or schedule script                              |
| OPENIDM-18868 | Inability to save a schedule when you add or remove a passed variable                        |
| OPENIDM-18865 | Script changes cannot be saved unless you click outside the Inline Script box                |
| FRAAS-14097   | Promotion report should identify journeys by their name                                      |
| FRAAS-13522   | Promotion report does not include changes to custom email provider                           |
| FRAAS-14353   | Configuration placeholder replacement assumes a string value                                 |

### 17 Mar 2023

#### Resolved issues

| Issue ID    | Summary                                                               |
| ----------- | --------------------------------------------------------------------- |
| FRAAS-14260 | UI displays "Resource 'managed/alpha\_application' not found" message |
| FRAAS-14265 | Cannot access ESVs in sandbox tenants                                 |

### 16 Mar 2023

#### Key features

* PingOne® Identity Governance (add-on capability)

  PingOne Identity Governance is a new add-on capability of PingOne Advanced Identity Cloud. Identity Governance allows you to centrally administer and manage user access to applications and data across your organization to support regulatory compliance.

  With Identity Governance you can:

  * Work with onboarded target applications when reviewing user data. This allows you to review user data for onboarded applications.

  * Define and launch reviews of data using certification campaigns.

  * Review and manage user access to applications. This includes managers reviewing the access their direct reports have.

  For more information, refer to [What is PingOne Identity Governance?](../identity-governance/administration/getting-started-what-is-iga.html).

  To purchase an Identity Governance subscription, contact your ForgeRock representative.

#### Resolved issues

| Issue ID | Summary                                                             |
| -------- | ------------------------------------------------------------------- |
| IGA-1433 | Initial release of Identity Governance with identity certifications |

### 15 Mar 2023

#### Resolved issues

| Issue ID   | Summary                                                                                                                                                |
| ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| FRAAS-9376 | Provide the ability to display a login journey in an iframe for specific custom domains. To implement this feature, you need to open a support ticket. |

### 13 Mar 2023

#### Resolved issues

| Issue ID    | Summary                                                |
| ----------- | ------------------------------------------------------ |
| FRAAS-14265 | Enable access to ESVs in sandbox and demo environments |
| FRAAS-14276 | Add `idm-recon` as a log source                        |

### 10 Mar 2023

#### Key features

* Support for Scripted Groovy connector applications

  Application management now lets you register, provision, and manage Scripted Groovy connector applications.

  For details, refer to [Scripted Groovy connector](../app-management/provision-an-application.html#provision-scripted-groovy).

#### Resolved issues

| Issue ID\[[27](#_footnotedef_27 "View footnote.")] | Summary                                                                                                                                                                     |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM-662                                            | Fixed agent logout in platform UI                                                                                                                                           |
| IAM-3160                                           | Added ability to configure the scripted Groovy connector                                                                                                                    |
| IAM-3180                                           | Hide the SSO tab when an application is authoritative                                                                                                                       |
| IAM-3193                                           | Updated SCIM app template to only show the refresh token property for OAuth authentication                                                                                  |
| IAM-3303                                           | Enable clicking a row to edit entries on the service accounts page                                                                                                          |
| IAM-3304                                           | Added breadcrumbs to the service accounts page                                                                                                                              |
| IAM-3305                                           | Added a search field to the service accounts page                                                                                                                           |
| IAM-3462                                           | Corrected AD template property from `ENABLED` to `ENABLE`                                                                                                                   |
| IAM-3478                                           | Addressed accessibility concerns when displaying password policy validation                                                                                                 |
| IAM-3642                                           | Fixed an issue with unselected applications being imported when promoting, and improved the user experience for selecting and deselecting applications in the promotions UI |
| IAM-3669                                           | Fixed drop-down lists to show the value of the selected option in the form                                                                                                  |
| IAM-3694                                           | Added ability to customize the success color in hosted pages                                                                                                                |

### 08 Mar 2023

#### Key features

* Administrator federation

  Administrator federation allows administrators to use single sign-on (SSO) to log in to an Advanced Identity Cloud tenant.

  By using federation to authenticate your administrators to Advanced Identity Cloud, you can quickly and easily deprovision an administrator by removing their access from your centralized identity provider.

  For details, refer to [Configure federated access for tenant administrators](../federation/configure-federated-access-for-tenant-administrators.html).

#### Resolved issues

| Issue ID   | Summary                                                                                               |
| ---------- | ----------------------------------------------------------------------------------------------------- |
| FRAAS-5416 | Administrators can access Advanced Identity Cloud using single sign-on from another identity provider |

### 06 Mar 2023

#### Resolved issues

| Issue ID | Summary                                                                                                                                                                                                                                              |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM-2921 | In the Dashboard, the total number of applications that display in the Applications box now includes those applications registered using the [new app catalog](../app-management/applications.html) in tenants created on or after January 12, 2023. |
| IAM-3760 | Apple social authentication works with other authentication methods                                                                                                                                                                                  |

### 03 Mar 2023

#### Key features

* SCIM built-in connector

  You can now use the [SCIM built-in connector](https://docs.pingidentity.com/openicf/connector-reference/scim.html) to manage user and group accounts on any SCIM-compliant resource provider.

* Promotions API documentation

  The promotions API documentation is now publicly available at <https://apidocs.id.forgerock.io/#tag/Promotion>.

#### Resolved issues

| Issue ID      | Summary                                                                                                                                              |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| FRAAS-8225    | The promotions API documentation is now publicly available at <https://apidocs.id.forgerock.io/#tag/Promotion>                                       |
| FRAAS-8709    | Include the log sources in the logged events                                                                                                         |
| FRAAS-12402   | Add /platform/oauthReturn route to support authentication for Salesforce and Google Apps                                                             |
| FRAAS-12413   | OIDC login from a custom domain results in blank page                                                                                                |
| OPENICF-400   | The LDAP connector now correctly reads the AD Account tokenGroups attribute                                                                          |
| OPENICF-1858  | Add group owners management support to the Microsoft Graph API connector                                                                             |
| OPENICF-2039  | Add archived, languages, isEnrolledIn2Sv, and isEnforcedIn2Sv fields to the Google Apps connector                                                    |
| OPENICF-2067  | Adjust license assignments as part of the user creation and update operations in the Google Apps connector                                           |
| OPENICF-2068  | The Microsoft Graph API connector now lets you assign and revoke directory roles to an Azure AD user account and query the target instance for roles |
| OPENICF-2088  | The Microsoft Graph API connector now lets you assign and revoke custom roles to an Azure AD user account and query the target instance for roles    |
| OPENICF-2102  | Assign and revoke PermissionSets and Groups to Salesforce user accounts in the Salesforce connector                                                  |
| OPENICF-2110  | Expose groups and roles through user object in the ServiceNow connector                                                                              |
| OPENICF-2111  | View, update, and remove a group's roles through the role object in the ServiceNow connector                                                         |
| OPENICF-2129  | The LDAP connector now includes a parameter to use isMemberOf by ldapGroups                                                                          |
| OPENICF-2192  | In the Google Apps connector, don't throw an NPE when updating a user with a change to license assignments if \_NAME\_ is not specified              |
| OPENIDM-17876 | Query filter editor no longer removes double quotes from all properties that aren't of type string                                                   |
| OPENIDM-17936 | Saving changes to the authzRoles field on users no longer overrides the field type                                                                   |
| OPENIDM-18001 | Country codes in locales are no longer ignored when sending emails                                                                                   |
| OPENIDM-18077 | Added new default policy, cannot-contain-others-case-insensitive                                                                                     |
| OPENIDM-18153 | Custom script exception messages are no longer incorrectly truncated in REST responses                                                               |
| OPENIDM-18238 | Improved resiliency of clustered reconciliations                                                                                                     |
| OPENIDM-18243 | Validate that connector names are alphanumeric                                                                                                       |
| OPENIDM-18260 | New sync mapping fields, defaultSourceFields and defaultTargetFields, let you specify which fields to use for read and query requests                |
| OPENIDM-18261 | Endpoints within /system now support specifying additional fields when using wildcards                                                               |
| OPENIDM-18275 | The groups' name field is now searchable                                                                                                             |
| OPENIDM-18319 | An up-to-date target object state is now provided in sync script bindings and sync audit mechanisms                                                  |
| OPENIDM-18336 | The default assignment object schema now contains a "condition" field                                                                                |
| OPENIDM-18498 | Queued sync not triggered if target is a CREST proxy endpoint                                                                                        |
| OPENIDM-18501 | Tenant administrator password policy no longer restricts passwords to a maximum length                                                               |
| OPENIDM-18629 | Reconciliation job identifiers now use a more precise timestamp                                                                                      |
| OPENIDM-18650 | Add new SCIM connector; applications now support creating connections to SCIM services                                                               |

### 01 Mar 2023

| Issue ID                                           | Summary                                                                              |
| -------------------------------------------------- | ------------------------------------------------------------------------------------ |
| IAM-3089\[[28](#_footnotedef_28 "View footnote.")] | Unable to exit a social provider and select a different social provider in a journey |

### 28 Feb 2023

#### Resolved issues

| Issue ID    | Summary                                                              |
| ----------- | -------------------------------------------------------------------- |
| FRAAS-13933 | Make managed groups visible in the AM admin UI                       |
| FRAAS-13983 | Remove OneSpan nodes from the Basic Authentication journey node list |

### 22 Feb 2023

#### Resolved issues

| Issue ID    | Summary                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------- |
| FRAAS-14069 | Add `IdPCallback` class to scripting allowlist                                           |
| FRAAS-14030 | Add inner classes from `java.security` and `java.crypto` packages to scripting allowlist |
| FRAAS-13974 | Add class `sun.security.ec.ECPrivateKeyImpl` to scripting allowlist                      |
| FRAAS-13597 | Remove unexpected changes from promotion reports                                         |

### 16 Feb 2023

#### Resolved issues

| Issue ID    | Summary                                                       |
| ----------- | ------------------------------------------------------------- |
| FRAAS-13597 | Fix inconsistencies between provisional and promotion reports |

### 14 Feb 2023

#### Key features

* Support for REST connector applications

  Application management now lets you register, provision, and manage REST connector applications.

  For details, refer to [Scripted REST connector](../app-management/provision-an-application.html#provision-scripted-rest).

#### Resolved issues

| Issue ID | Summary                                                                                 |
| -------- | --------------------------------------------------------------------------------------- |
| IAM-2879 | Allow properties in forms to be reordered                                               |
| IAM-3094 | Add support for enumerated values in array attributes                                   |
| IAM-3156 | Update the descriptive text in the "Add Property" modal to be more accurate             |
| IAM-3261 | Adjust Autonomous Access risk filter to better handle scoring edge cases                |
| IAM-3262 | Adjust menu width on the Autonomous Access Risk Administration page                     |
| IAM-3461 | Fix display of OAuth 2.0 applications with a UUID for a name                            |
| IAM-3492 | Fix objects ending in `application` or `assignment` not appearing in the Privileges tab |

### 13 Feb 2023

#### Resolved issues

| Issue ID    | Summary                                                       |
| ----------- | ------------------------------------------------------------- |
| FRAAS-13478 | Promotions report shows changes that it shouldn't             |
| FRAAS-13866 | Let Identity Cloud administrators access policy configuration |
| IAM-3512    | Access Management native console incorrect redirect URL       |

### 09 Feb 2023

#### Key features

* OneSpan authentication journey nodes

  The new OneSpan authentication journey nodes integrate [OneSpan Intelligent Adaptive Authentication (IAA)](https://www.onespan.com/products/intelligent-adaptive-authentication) scoring for identity proofing, continuous authentication, and fraud protection.

  For details about OneSpan authentication integration set up, refer to [OneSpan](https://docs.pingidentity.com/auth-node-ref/latest/cloud/onespan-about.html).

* Jumio identity verification

  The new Jumio identity verification integrates with [Jumio's NetVerify](https://www.jumio.com/faq/) service to easily and securely verify identity by using facial recognition to authenticate against government issued IDs.

  For details about Jumio identity verification, refer to [Jumio identity verification](https://docs.pingidentity.com/auth-node-ref/latest/cloud/jumio-id-verify.html).

* Logout for all server-side sessions for a user or set of users

  Administrators can now invalidate (log out) all server-side sessions for a user by sending a POST request to the `json/sessions` endpoint with the `logoutByUser` action, specifying the username in the request payload.

* Composite advice with an AuthLevelCondition in journeys

  Composite advice gives AM hints about which authentication services to use when logging in a user. Journeys now take into account the AuthLevelCondition composite advice.

  For example, you can now use AuthLevelCondition composite advice so that AM uses a journey that provides an authentication level of 10 or higher.

#### Resolved issues

| Issue ID     | Summary                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| AME-22942    | Log out all server-side sessions for a user or set of users so that they have to reauthenticate                                |
| FRAAS-13454  | Integrate Jumio identity verification journey nodes                                                                            |
| FRAAS-13555  | Integrate OneSpan authentication nodes                                                                                         |
| FRAAS-13809  | Autonomous log filters fail in connected environments                                                                          |
| OPENAM-11319 | Add description key to the JSON response from OAuth2UserApplications#getResourceResponse                                       |
| OPENAM-16374 | Add support for composite advices with a AuthLevelCondition to journeys                                                        |
| OPENAM-18270 | Don't raise errors when calls to the access\_token endpoint specify the scope parameter in OAuth2 authorization\_code exchange |
| OPENAM-18488 | Handle the CA certificate correctly for Windows Hello attestations                                                             |

### 31 Jan 2023

#### Resolved issues

| Issue ID\[[29](#_footnotedef_29 "View footnote.")] | Summary                                                                                                      |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| FRAAS-13011                                        | Security improvements                                                                                        |
| IAM-2025                                           | Add Uncategorized to the journey category filter                                                             |
| IAM-3107                                           | Remove bitwise filter on Active Directory page                                                               |
| IAM-3108                                           | Update Maintain LDAP Group Membership option to not be selected by default                                   |
| IAM-3109                                           | Update cn property to be optional in Active Directory target mode                                            |
| IAM-3110                                           | Update ldapGroups property to be available by default in Active Directory target mode                        |
| IAM-3111                                           | Fix password hash algorithm                                                                                  |
| IAM-3139                                           | Fix Revoke button in users and roles to revoke users, and not be clickable when there are no users to revoke |
| IAM-3142                                           | Fix Active Directory user filter anomaly when deleting a row                                                 |
| IAM-3146                                           | Update user-specific attributes to be editable by administrators                                             |
| IAM-3257                                           | Fix escaping of ESV placeholders in the advanced email editor                                                |

### 30 Jan 2023

#### Resolved issues

| Issue ID    | Summary                                                            |
| ----------- | ------------------------------------------------------------------ |
| FRAAS-13519 | Remove unexpected file changes from self-service promotion reports |

### 27 Jan 2023

#### Resolved issues

| Issue ID                                           | Summary                                                                                 |
| -------------------------------------------------- | --------------------------------------------------------------------------------------- |
| FRAAS-13464                                        | Adjust sandbox environment migration to not use development environment migration steps |
| FRAAS-13478                                        | Remove unrelated AM root realm changes from promotion reports                           |
| FRAAS-13620                                        | Improve performance of promotion report generation by removing unrelated data           |
| IAM-2305\[[29](#_footnotedef_29 "View footnote.")] | Add support for localized logos in end-user UI                                          |
| IAM-3091\[[29](#_footnotedef_29 "View footnote.")] | Fix localized headers rendering as \[object Object]                                     |

### 26 Jan 2023

#### Resolved issues

| Issue         | Summary                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------- |
| OPENIDM-16640 | Changes to identity objects by onUpdate scripts not triggering relationship property onRetrieve hooks |

### 25 Jan 2023

#### Key features

* Improved access control for hosted pages

  You can now block access separately for hosted end user account and journey pages:

  * Advanced Identity Cloud displays account pages *after* authentication for user profile and delegated administration details.

  * Advanced Identity Cloud displays journey pages *during* authentication for login, registration, password reset, and more.

  By default, [Hosted pages](../end-user/hosted-pages.html) are active and accessible for accounts and journeys.

  To disable access through the Advanced Identity Cloud admin console, go to Tenant Settings > Global Settings > End User UI and select the pages to disable.

#### Resolved issues

| Issue ID    | Summary                                                                                                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IAM-2735    | SAML application improvements, including adding ability to update metadata without recreating application and adding ability to download IdP certificate from application |
| IAM-3044    | Applications list overflows when screen size is reduced                                                                                                                   |
| IAM-3084    | Only allow unique values when adding application owners                                                                                                                   |
| IAM-3141    | Add the ability to promote dynamic configuration attached to application                                                                                                  |
| IAM-3151    | Remove redirect to global settings during administrator login                                                                                                             |
| IAM-3183    | Let users filter the trends dashboard by date without resetting the journeys dashboard                                                                                    |
| IAM-3339    | After refreshing the realm settings page, set the current tab using the identifier specified in the URL fragment                                                          |
| FRAAS-7542  | Control access to hosted account and journey pages                                                                                                                        |
| FRAAS-11599 | Don't allow changes to scripts in staging and production environments                                                                                                     |

### 13 Jan 2023

#### Key features

* Service accounts

  You can now use service accounts to request access tokens for most Advanced Identity Cloud REST API endpoints without relying on a particular identity in your system:

  * Call Identity Cloud APIs programmatically without needing a human identity.

  * Access AM or IDM APIs in the same way using a signed JWT.

  * Set scopes on each service account to assign only necessary permissions to access tokens.

  * Use for automation and CI/CD tooling.

  For details, refer to [Service accounts](../tenants/service-accounts.html).

#### Resolved issues

| Issue ID   | Summary                                                                             |
| ---------- | ----------------------------------------------------------------------------------- |
| FRAAS-8477 | Service accounts                                                                    |
| IAM-1939   | Fix hCaptcha support in Platform UI                                                 |
| IAM-2224   | Replace bullets with checkmarks when validating password policy                     |
| IAM-2847   | Increase the size of the terms and conditions modal window                          |
| IAM-2912   | Enable promotions UI to ignore encrypted secrets                                    |
| IAM-3011   | Update risk configuration UI to show only user-modifiable configuration             |
| IAM-3012   | Add new `userConfig` endpoint to the `riskConfig` API                               |
| IAM-3015   | Update risk configuration evaluation UI so that updates use the new APIs            |
| IAM-3016   | Fix the `gotoOnFail` query parameter to redirect in case of failure                 |
| IAM-3041   | Prevent proceeding from the Active Directory modal window without entering base DNs |
| IAM-3076   | Fix Salesforce provisioning connection                                              |
| IAM-3079   | Fix single sign-on (SSO) setup when app name has a space                            |
| IAM-3088   | Enable suppression of the login failure message from the failure node               |
| IAM-3122   | Fix font weight of the title text on provisioning tab                               |
| IAM-3145   | Fix Active Directory assignment on array attributes to be a merge and not replace   |
| IAM-3177   | Add paging back to application list view if workforce feature is not enabled        |
| IAM-3335   | Fixed display of localized favicon                                                  |

### 11 Jan 2023

#### Resolved issues

| Issue ID    | Summary                                                                          |
| ----------- | -------------------------------------------------------------------------------- |
| FRAAS-13121 | Provisional reports can cause promotion service to run out of memory and restart |
| FRAAS-13244 | Unable to log into tenant to perform self-service promotion                      |

### 04 Jan 2023

#### Resolved issues

| Issue ID                                               | Summary                                                                                  |
| ------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| FRAAS-13242                                            | Improve invalid page size error message                                                  |
| OPENAM-19485\[[30](#_footnotedef_30 "View footnote.")] | Access multi-tenant social providers without requiring multiple secondary configurations |
| OPENIDM-17392                                          | Prevent script typos that cause services to fail from being introduced into the system   |
| OPENIDM-17953                                          | Support email addresses that contain non-ASCII UTF-8 characters                          |

## 2022

### 21 Dec 2022

#### Resolved issues

| Issue ID    | Summary                                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------------------- |
| FRAAS-13057 | Add only standard placeholders (not user-defined placeholders) prior to enabling placeholder management |

### 20 Dec 2022

#### Key features

* BioCatch authentication nodes

  The new BioCatch authentication nodes integrate [BioCatch](https://www.biocatch.com/) scoring for identity proofing, continuous authentication, and fraud protection.

  For details, refer to [Marketplace journey nodes](../journeys/marketplace.html).

#### Resolved issues

| Issue ID    | Summary                                         |
| ----------- | ----------------------------------------------- |
| FRAAS-12140 | Integrate BioCatch authentication journey nodes |
| FRAAS-12713 | Promotions API failed to generate a report      |

### 16 Dec 2022

#### Resolved issues

| Issue ID    | Summary                                                                   |
| ----------- | ------------------------------------------------------------------------- |
| FRAAS-11964 | Avoid potential performance degradation when removing expired token state |
| FRAAS-12939 | Add proxy state to output of lock state endpoint for promotions API       |

### 15 Dec 2022

#### Resolved issues

| Issue ID    | Summary                                                                        |
| ----------- | ------------------------------------------------------------------------------ |
| FRAAS-12545 | Remove the option to keep orphaned configuration nodes from the promotions API |

### 09 Dec 2022

#### Key features

* Event hooks

  Event hooks let you trigger scripts during various stages of the lifecycle of users, roles, assignments, and organizations.

  You can trigger scripts when one of these identity objects is created, updated, retrieved, deleted, validated, or stored in the repository. You can also trigger a script when a change to an identity object triggers an implicit synchronization operation.

  Post-action scripts let you manipulate identity objects after they are created, updated, or deleted.

  For details, refer to [Event hooks](../developer-docs/scripting-event-hooks.html).

#### Resolved issues

| Issue ID | Summary                            |
| -------- | ---------------------------------- |
| IAM-2941 | Add the event hooks user interface |

### 08 Dec 2022

#### Resolved issues

| Issue ID    | Summary                                            |
| ----------- | -------------------------------------------------- |
| FRAAS-12477 | Add list of encrypted secrets to promotion reports |

### 07 Dec 2022

#### Resolved issues

| Issue ID      | Summary                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------- |
| FRAAS-12494   | Unlock the environment and stop checking progress after successfully promoting an environment |
| FRAAS-12988   | Prevent placeholder support being enabled unless a specific migration flag value is set       |
| OPENIDM-17556 | Ensure RDVPs are not erased for all types of managed objects for all types of PUT operations  |

### 06 Dec 2022

#### Key features

* Workforce application and connector management

  In new tenants created on or after January 12, 2023, you can use the improved applications page to integrate Advanced Identity Cloud with external data stores or identity providers. The applications page acts as a one-stop location where you can:

  * Register and provision popular federation-capable applications quickly and easily by choosing from a library of templates, such as Salesforce and Workday.

  * Register and provision your organization's custom applications.

  * Manage data, properties, rules, SSO, provisioning, users, and groups for an application.

  * View the connection status of each application.

  * Activate and deactivate an application.

  For details, refer to [Application management improvements (new tenants only)](../app-management/applications.html).

* Daon IdentityX authentication nodes

  The new Daon authentication nodes let you integrate with the [Daon IdentityX platform](https://www.daon.com/technology/identityx-platform/) for MFA with mobile authentication or out-of-band authentication using a separate, secure channel.

  For details, refer to [Marketplace journey nodes](../journeys/marketplace.html).

#### Resolved issues

| Issue ID     | Summary                                                                                          |
| ------------ | ------------------------------------------------------------------------------------------------ |
| FRAAS-11574  | Integrate Daon authentication journey nodes                                                      |
| IAM-2658     | Application management improvements                                                              |
| DATASCI-1548 | Update the filter text on the Autonomous Access dashboard from "All Risk Scores" to "Risk Score" |
| DATASCI-1550 | Update text on the Autonomous Access dashboard's Copy on User Detail page                        |

### 29 Nov 2022

#### Key features

* Onfido authentication nodes

  The new Onfido authentication nodes let you use Onfido's solution for collecting and sending document identification and, optionally, biometrics to the Onfido backend for verification.

  For details, refer to [Marketplace journey nodes](../journeys/marketplace.html).

#### Resolved issues

| Issue ID    | Summary                        |
| ----------- | ------------------------------ |
| FRAAS-11575 | Add Onfido authentication node |

### 23 Nov 2022

#### Resolved issues

| Issue ID | Summary                                                                        |
| -------- | ------------------------------------------------------------------------------ |
| IAM-2354 | Add system notification capability to UI                                       |
| IAM-2355 | Self-service promotions migration UI                                           |
| IAM-2465 | Password policy to force password expiry not working                           |
| IAM-2706 | Embedding images in the theme editor only displays alternative text            |
| IAM-2739 | Email suspend message displayed without line breaks                            |
| IAM-2939 | Add translation configuration key for "Passwords do not match" message         |
| IAM-2973 | Self-service promotions migration UI flow should enable promotions UI features |

### 22 Nov 2022

#### Resolved issues

| Issue ID    | Summary                                     |
| ----------- | ------------------------------------------- |
| FRAAS-12552 | Add redirect for custom domain login screen |

### 18 Nov 2022

#### Resolved issues

Addressed a security issue.

### 10 Nov 2022

#### Resolved issues

Addressed a security issue.

### 08 Nov 2022

#### Key features

* Group management

  You can now create and manage groups that are shared across AM and IDM within your Advanced Identity Cloud instance. New tenants have group management enabled by default, and existing tenants can follow an upgrade path to enable it.

  For more information, refer to [Group management](../idm-objects/groups.html).

#### Resolved issues

| Issue ID    | Summary                                              |
| ----------- | ---------------------------------------------------- |
| FRAAS-12379 | Add support for groups and assigning users to groups |
| FRAAS-12625 | Handle ESVs as string type if no type is set         |

### 02 Nov 2022

#### Key features

* ID Cloud Analytics Dashboard enhancements

  You can now take advantage of the following enhancements to the analytics dashboard:

  * The journey chart now lets users drill down at specific points on a trend line to view individual journey outcomes for that date/hour. Journeys are sorted by a ranking of percentage failures, but can also be sorted based on number ranking.

  * Two new widgets — Top Five Journeys by Outcome and Top Five Journeys by Usage — that rank trending journeys based on outcomes and usages are now available.

  For more information, refer to [Advanced Identity Cloud analytics dashboard](../tenants/analytics-dashboard.html).

#### Resolved issues

| Issue ID     | Summary                                                                                        |
| ------------ | ---------------------------------------------------------------------------------------------- |
| ANALYTICS-25 | Add journey ranking and ability to drill down into journey outcomes to the analytics dashboard |

### 25 Oct 2022

#### Key features

* Self-service promotions

  Self-service promotions let you promote configuration between environments without raising a support ticket. You can perform self-service promotions from development to staging tenant environments, and from staging to production tenant environments. You cannot promote sandbox environments.

  For more information, refer to [Introduction to self-service promotions](../tenants/self-service-promotions.html).

* Configuration placeholders visible in all APIs

  Configuration placeholders let you set [ESVs](../tenants/esvs.html) in your configuration.

  For more information, refer to [Manage configuration placeholders using the API](../tenants/configuration-placeholders-api.html).

#### Resolved issues

| Issue ID    | Summary                                                                     |
| ----------- | --------------------------------------------------------------------------- |
| FRAAS-10979 | Configuration placeholders visible in all APIs in new customer environments |
| FRAAS-12219 | Self-service promotions available in new customer environments              |

### 19 Oct 2022

#### Key features

* Duo authentication node

  The new Duo authentication node lets you use Duo's solution for adaptive authentication, bring your own device security, cloud security, endpoint security, mobile security, and two-factor authentication.

* Twilio authentication node

  The new Twilio authentication node allows you to use Twilio for two-factor authentication during account setup, sign-on, and other scenarios. The node lets you integrate Twilio's APIs to build solutions for SMS and WhatsApp messaging, voice, video, and email. The node uses Twilio's latest Lookup API, which uses real-time risk signals to detect fraud and trigger step-up authentication when needed.

For details, refer to [Marketplace journey nodes](../journeys/marketplace.html).

#### Resolved issues

| Issue ID     | Summary                                                                                             |
| ------------ | --------------------------------------------------------------------------------------------------- |
| ANALYTICS-52 | Correct the value in the All Journeys field                                                         |
| DATASCI-1437 | Correct prefilled username fields in Filters window                                                 |
| DATASCI-1474 | Don't show explainability if not specified in response after applying Unusual Day of Week filter    |
| DATASCI-1497 | Let users see previously selected risk reasons after closing the Filter window                      |
| DATASCI-1504 | Prevent the truncation of text on the right side of pages                                           |
| FRAAS-11570  | Add Duo authentication node                                                                         |
| FRAAS-11571  | Add Twilio authentication node                                                                      |
| FRAAS-11825  | Add translation configuration key for no search results message                                     |
| FRAAS-12301  | Add Marketplace nodes to journey editor menu                                                        |
| FRAAS-12413  | Remove blank page shown when user returns to login page following successful login to custom domain |
| IAM-1935     | Expose ESV variable type in the UI                                                                  |
| IAM-2038     | Prevent theme styles rendering in the hosted pages editor                                           |
| IAM-2066     | Show the entire answer to a long security question after clicking the visibility icon               |
| IAM-2259     | Do not let users save email templates that contain JavaScript                                       |
| IAM-2312     | Render SVG images correctly                                                                         |
| IAM-2411     | ForgeRock favicon displays briefly before the customer's favicon                                    |
| IAM-2502     | Remove flashing red text from security questions window                                             |
| IAM-2633     | Support localization for radio display fields in Choice Collector node                              |
| IAM-2696     | Remove legend from Risk Score window                                                                |
| IAM-2869     | Update UI regex validation for ESV list type                                                        |

### 18 Oct 2022

#### Resolved issues

| Issue ID    | Summary                                                                |
| ----------- | ---------------------------------------------------------------------- |
| FRAAS-12373 | Fix Choice Collector nodes so that they can show more than two options |

### 07 Oct 2022

#### Resolved issues

| Issue ID | Summary                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------ |
| IAM-2846 | Fix login issues caused by allowing non-mandatory login journey attributes to have empty values (reverts IAM-1678) |

### 03 Oct 2022

#### Resolved issues

| Issue ID      | Summary                                                                        |
| ------------- | ------------------------------------------------------------------------------ |
| IAM-1933      | Alter AM XUI to display readonly strings wherever placeholders are in use      |
| OPENAM-19868  | Correctly handle multi-line text in Email Suspend nodes                        |
| OPENIDM-18272 | Save managed object properties correctly in Identity Management native console |

### 22 Sep 2022

#### Resolved issues

| Issue ID      | Summary                                                                                         |
| ------------- | ----------------------------------------------------------------------------------------------- |
| AME-22684     | Include grace period configuration in the OAuth2 provider settings                              |
| OPENAM-18112  | Provide better error message when an LDAP authentication node encounters a TLS connection issue |
| OPENAM-19196  | Do not wait for cache timeout before OAuth2 clients reflect changes to Javascript origins       |
| OPENIDM-16420 | Update the default email validation policy to conform with RFC 5322                             |
| OPENIDM-17533 | Allow configuration changes to the repo.ds.json file to take effect without restarting IDM      |
| OPENIDM-17720 | Fix null pointer exception when the repo.ds.json file is misconfigured                          |
| OPENIDM-17836 | Fix for startup error message caused by ObjectMapping constructor exception                     |
| OPENIDM-17911 | Fix email validation errors in the IDM admin UI (native console)                                |

### 20 Sep 2022

#### Resolved issues

| Issue ID     | Summary                                                                                                                  |
| ------------ | ------------------------------------------------------------------------------------------------------------------------ |
| DATASCI-1165 | Remove Automated User Agent from the list of risk reasons filters                                                        |
| DATASCI-1358 | Let users filter dashboards by date, risk scores and features                                                            |
| DATASCI-1365 | Update the Risk Activity page when applying a filter without requiring users to refresh the page                         |
| DATASCI-1394 | Show the times that events occurred correctly without requiring users to refresh the display                             |
| DATASCI-1395 | Let users see their last five risky authentication attempts                                                              |
| DATASCI-1397 | Remove risk administration options from end users' navigation menus                                                      |
| DATASCI-1406 | When filtering activities using a date range, include the activities that occur on the end date                          |
| IAM-1678     | Allow login journey attributes that are not required to have empty values                                                |
| IAM-1682     | When editing email templates, cut text correctly                                                                         |
| IAM-1932     | When placeholders are used, display read-only strings in the Platform UI                                                 |
| IAM-2028     | Remove excess space from journey editor fields that do not require floating labels                                       |
| IAM-2064     | Replace fields for specifying numeric thresholds with a risk score definition slider in Autonomous Access Decision nodes |
| IAM-2080     | Let users create customized footers on Page nodes                                                                        |
| IAM-2141     | Add option to customize Page node background color                                                                       |
| IAM-2142     | Add option to customize Page node button width                                                                           |
| IAM-2143     | Add option to customize label text for Page node fields                                                                  |
| IAM-2227     | Remove spurious "No configuration exists for id external.email" pop-up warning                                           |
| IAM-2249     | Add option to display Message node as a link                                                                             |
| IAM-2250     | After importing journeys, let user delete all imported journeys with a single delete action                              |
| IAM-2251     | Provide a value when the object.password variable is specified in an email template                                      |
| IAM-2258     | Remove tenant information from the realm menu                                                                            |
| IAM-2285     | Make H2, H3, and H4 HTML headings bigger when there's no higher-level predecessor heading                                |
| IAM-2290     | Show the correct number of events per country on the Activity Risk dashboard                                             |
| IAM-2294     | Show previous authentication attempts when doing anomaly lookups                                                         |
| IAM-2320     | Change the default navigation background color of Account pages without changing the dashboard color                     |
| IAM-2329     | Change the color of the Autonomous Access event log indicator to red                                                     |
| IAM-2351     | Correct pagination on the Autonomous Access Risk page                                                                    |
| IAM-2373     | Make dashboard analytics pipeline logs in Autonomous Access work as expected                                             |
| IAM-2468     | Wrap long security questions                                                                                             |
| IAM-2521     | Don't reuse authId during password validation                                                                            |
| OPENAM-18933 | Do not override the Success URL node's value                                                                             |
| SDKS-1720    | Point developers to the ForgeRock SDKs when they create an OAuth2.0 client in the Platform UI                            |
| SDKS-1721    | Point developers to the ForgeRock SDKs when they configure CORS in the Platform UI                                       |

***

[1](#_footnoteref_1). This release focuses on internal improvements and technical updates to enhance the overall stability, performance, and maintainability of the platform. While there are no direct customer-facing changes, these updates lay the groundwork for future feature releases and improvements.[2](#_footnoteref_2). This change applies to a feature only available in PingOne Identity Governance, which is an [add-on capability](../product-information/add-on-capabilities.html) and must be purchased separately.[3](#_footnoteref_3). This change applies to a feature only available in Advanced Reporting, which is an [add-on capability](../product-information/add-on-capabilities.html) and must be purchased separately.[4](#_footnoteref_4). This issue was released on March 13, 2025 but inadvertently excluded from the changelog.[5](#_footnoteref_5). This issue was released on December 16, 2024 (Version 15989.0; ANALYTICS-900) but inadvertently excluded from the changelog.[6](#_footnoteref_6). Advanced Reporting is an [add-on capability](../product-information/add-on-capabilities.html).[7](#_footnoteref_7). IGA is an [add-on capability](../product-information/add-on-capabilities.html).[8](#_footnoteref_8). This issue was released on November 20, 2024 (Version 15726.0) but inadvertently excluded from the changelog.[9](#_footnoteref_9). This issue was released on September 9, 2024 (Version 14888.0) but inadvertently excluded from the changelog.[10](#_footnoteref_10). These nodes were released on June 12, 2024 (Version 13848.0) but inadvertently excluded from the changelog.[11](#_footnoteref_11). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).[12](#_footnoteref_12). This issue was released on May 30, 2024 (Version 13664.0) but inadvertently excluded from the changelog.[13](#_footnoteref_13). This issue was released on April 17, 2024 (Version 13218.0) but inadvertently excluded from the changelog.[14](#_footnoteref_14). This issue was released on January 22, 2024 but inadvertently excluded from the changelog.[15](#_footnoteref_15). This issue was released on January 18, 2024 but inadvertently excluded from the changelog.[16](#_footnoteref_16). This issue was released on November 27, 2023 but inadvertently excluded from the changelog.[17](#_footnoteref_17). This issue was released on November 6, 2023 but inadvertently excluded from the changelog.[18](#_footnoteref_18). The updated connectors for FRAAS-17939 originally listed connectors not included with Advanced Identity Cloud.[19](#_footnoteref_19). This change applies to a feature only available in PingOne Autonomous Access, which is an [add-on capability](../product-information/add-on-capabilities.html) and must be purchased separately.[20](#_footnoteref_20). The updated connectors for FRAAS-17373 were originally listed as: Database Table connector, Microsoft Graph API connector, Oracle EBS connector, Salesforce connector, SCIM connector, ScriptedSQL connector.[21](#_footnoteref_21). This issue was released on September 11, 2023 but inadvertently excluded from the changelog.[22](#_footnoteref_22). This issue was released on August 2, 2023 but inadvertently excluded from the changelog.[23](#_footnoteref_23). This issue was released on June 14, 2023 but inadvertently excluded from the changelog.[24](#_footnoteref_24). This issue was released on June 19, 2023 but inadvertently excluded from the changelog.[25](#_footnoteref_25). This issue was released on May 5, 2023 but inadvertently excluded from the changelog.[26](#_footnoteref_26). This issue was released on May 2, 2023 but inadvertently excluded from the changelog.[27](#_footnoteref_27). The issues listed in this table were released on March 6, 2023 but inadvertently excluded from the changelog.[28](#_footnoteref_28). This issue was released on February 14, 2023 but inadvertently excluded from the changelog.[29](#_footnoteref_29). This issues listed in this table, except FRAAS-13011, were released on January 13, 2023 but inadvertently excluded from the changelog.[30](#_footnoteref_30). This issue was released on November 24, 2022 but inadvertently excluded from the changelog.

---

---
title: Rapid channel features
description: Early access documentation for Advanced Identity Cloud rapid channel features not yet available in the regular channel
component: pingoneaic
page_id: pingoneaic:release-notes:rapid-channel-features
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/rapid-channel-features.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Rapid channel features

This page links to early access documentation for features available in the rapid channel and not in the regular channel. As these features become available in the regular channel, we update the links to refer to the main body of the PingOne Advanced Identity Cloud documentation.

|   |                                                             |
| - | ----------------------------------------------------------- |
|   | These topics are draft documentation and subject to change. |

* [Google Chrome Device Trust node](rapid-channel/auth-node-chrome-trust.html)

* [CLEAR ID Verification node](rapid-channel/auth-node-clear.html)

* [Akamai Account Protector node](rapid-channel/akamai-acc-protect-node.html)

* [Secure your AI-driven solutions using AI agents](rapid-channel/ai-agents.html)

  * [Enable the AI agents feature](rapid-channel/ai-agents-enable.html)

  * [Manage AI agents using the admin console](rapid-channel/ai-agents-ui.html)

  * [Configure an "on behalf of" authentication flow for AI agents](rapid-channel/ai-agents-configure-on-behalf-of-authentication-flow.html)

  * [Configure an autonomous AI agent flow](rapid-channel/ai-agents-configure-autonomous-agent-flow.html)

  * [Configure a DCR onboarding flow](rapid-channel/ai-agents-configure-dcr-onboarding-flow.html)

* [Role lifecycle management for Identity Governance](rapid-channel/DOCS-11971/lcm-role.html)

---

---
title: Regular channel changelog
description: Advanced Identity Cloud regular channel changelog tracking established features, enhancements, and fixes for development, UAT, staging, and production environments
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel-changelog
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel-changelog.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["product-information:changelog.adoc"]
section_ids:
  july_2026: July 2026
  08_jul_2026: 08 Jul 2026
  06_jul_2026: 06 Jul 2026
  02_jul_2026: 02 Jul 2026
  01_july_2026: 01 July 2026
  key_features: Key features
  enhancements: Enhancements
  fixes: Fixes
  june_2026: June 2026
  17_june_2026: 17 June 2026
  4_june_2026: 4 June 2026
  fixes_2: Fixes
  may_2026: May 2026
  18_may_2026: 18 May 2026
  enhancements_2: Enhancements
  fixes_3: Fixes
  multi_region_ha_15_may_2026: 15 May 2026
  key_features_2: Key features
  08_may_2026: 08 May 2026
  key_features_3: Key features
  enhancements_3: Enhancements
  fixes_4: Fixes
  april_2026: April 2026
  28_apr_2026: 28 Apr 2026
  enhancements_4: Enhancements
  23_apr_2026: 23 Apr 2026
  14_apr_2026: 14 Apr 2026
  key_features_4: Key features
  enhancements_5: Enhancements
  fixes_5: Fixes
  10_apr_2026: 10 Apr 2026
  01_april_2026: 01 April 2026
  key_features_5: Key features
  enhancements_6: Enhancements
  fixes_6: Fixes
  march_2026: March 2026
  31_mar_2026: 31 Mar 2026
  enhancements_7: Enhancements
  fixes_7: Fixes
  changed_functionality: Changed functionality
  rcs_1_5_20_34: 26 Mar 2026
  related_product_changes: Related product changes
  deprecation-non-persisted-schedules-2026-03-17: 17 Mar 2026
  deprecations: Deprecations
  rcs_1_5_20_33: 10 Mar 2026
  related_product_changes_2: Related product changes
  february_2026: February 2026
  26_feb_2026: 26 Feb 2026
  changed_functionality_2: Changed functionality
  ws_trust_ms365_upn_23_feb_2026: 23 Feb 2026
  key_features_6: Key features
  17_feb_2026: 17 Feb 2026
  key_features_7: Key features
  enhancements_8: Enhancements
  fixes_8: Fixes
  11_feb_2026: 11 Feb 2026
  fixes_9: Fixes
  03_feb_2026: 03 Feb 2026
  fixes_10: Fixes
  january_2026: January 2026
  27_jan_2026: 27 Jan 2026
  fixes_11: Fixes
  21_jan_2026: 21 Jan 2026
  key_features_8: Key features
  enhancements_9: Enhancements
  fixes_12: Fixes
  19_jan_2026: 19 Jan 2026
  fixes_13: Fixes
  december_2025: December 2025
  12_dec_2025: 12 Dec 2025
  fixes_14: Fixes
  12_dec_2025_2: 12 Dec 2025
  10_dec_2025: 10 Dec 2025
  enhancements_10: Enhancements
  ws_trust_ms365_x509_12_dec_2025: 09 Dec 2025
  key_features_9: Key features
  03_dec_2025: 03 Dec 2025
  key_features_10: Key features
  enhancements_11: Enhancements
  fixes_15: Fixes
  changed_functionality_3: Changed functionality
  november_2025: November 2025
  ws_trust_20_nov_2025: 20 Nov 2025
  key_features_11: Key Features
  11_nov_2025: 11 Nov 2025
  enhancements_12: Enhancements
  fixes_16: Fixes
  october_2025: October 2025
  28_oct_2025: 28 Oct 2025
  key_features_12: Key features
  21_oct_2025: 21 Oct 2025
  key_features_13: Key features
  enhancements_13: Enhancements
  fixes_17: Fixes
  09_oct_2025: 09 Oct 2025
  september_2025: September 2025
  30_sept_2025: 30 Sept 2025
  enhancements_14: Enhancements
  fixes_18: Fixes
  related_releases: Related releases
  26_sept_2025: 26 Sept 2025
  fixes_19: Fixes
  25_sept_2025: 25 Sept 2025
  log_event_exporter_22_sept_2025: 22 Sept 2025
  key_features_14: Key Features
  17_sept_2025: 17 Sept 2025
  enhancements_15: Enhancements
  fixes_20: Fixes
  additional_information: Additional information
  16_sept_2025: 16 Sept 2025
  12_sept_2025: 12 Sept 2025
  enhancements_16: Enhancements
  10_sept_2025: 10 Sept 2025
  03_sept_2025: 03 Sept 2025
  enhancements_17: Enhancements
  fixes_21: Fixes
  01_sept_2025: 01 Sept 2025
  fixes_22: Fixes
  august_2025: August 2025
  19_aug_2025: 19 Aug 2025
  enhancements_18: Enhancements
  fixes_23: Fixes
  12_aug_2025: 12 Aug 2025
  key_features_15: Key features
  enhancements_19: Enhancements
  fixes_24: Fixes
  removed: Removed
  july_2025: July 2025
  16_jul_2025: 16 Jul 2025
  08_jul_2025: 08 Jul 2025
  enhancements_20: Enhancements
  fixes_25: Fixes
  related_releases_2: Related releases
  03_jul_2025: 03 Jul 2025
  fixes_26: Fixes
  june_2025: June 2025
  29_jun_2025: 29 Jun 2025
  24_jun_2025: 24 Jun 2025
  key_features_16: Key features
  enhancements_21: Enhancements
  fixes_27: Fixes
  deprecations_2: Deprecations
  17_jun_2025: 17 Jun 2025
  16_jun_2025: 16 Jun 2025
  fixes_28: Fixes
  12_jun_2025: 12 Jun 2025
  10_jun_2025: 10 Jun 2025
  key_features_17: Key features
  enhancements_22: Enhancements
  fixes_29: Fixes
  may_2025: May 2025
  27_may_2025: 27 May 2025
  enhancements_23: Enhancements
  fixes_30: Fixes
  ws_fed_16_may_2025: 16 May 2025
  key_features_18: Key features
  13_may_2025: 13 May 2025
  enhancements_24: Enhancements
  fixes_31: Fixes
  03_may_2025: 03 May 2025
---

# Regular channel changelog

Subscribe to get automatic updates. Learn more in [Track regular channel releases](release-process.html#track-regular-channel-releases).

For release notes published before May 2025, refer to the [Regular channel changelog archive](regular-channel-changelog-archive.html).

## July 2026

### 08 Jul 2026

**Version 22170.18**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 06 Jul 2026

**Version 22170.17**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 02 Jul 2026

**Version 22170.16**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 01 July 2026

**Version 22170.14**

#### Key features

* Identity Governance role LCM (IGA-4265)\[[2](#_footnotedef_2 "View footnote.")]

  The new role lifecycle management (LCM) feature lets designated end users create, update, and delete roles on behalf of others without full administrative access. All changes are submitted as workflow-driven requests, maintaining governance and security while delegating role management to business owners.

* Identity Governance for AI agents (IGA-4223)\[[2](#_footnotedef_2 "View footnote.")]

  Agent Governance lets you detect, onboard, and govern AI agents the same way you govern human identities, accounts, and roles. This brings them under the governance umbrella alongside human identities.

  Agent Governance provides application templates to discover AI agents in the following agentic platforms:

  * AWS Bedrock

  * AWS Bedrock AgentCore

  * Azure AI Foundry

  * Microsoft Copilot Studio

  * Google Vertex AI

  Find more information in [Agent Governance](../identity-governance/administration/iga-agent-governance.html) and [Agent Governance: custodian and reviewer tasks](../identity-governance/end-user/iga-agent-governance-enduser.html).

#### Enhancements

* AME-28187: You can now set a **Metadata URL** in your remote consent agent. Advanced Identity Cloud retrieves the remote consent server's (RCS) metadata from this URL. When configured, the OIDC `.well-known` endpoint includes the `authorization_details_types_supported` field, populated from the authorization detail types advertised by the RCS.

* AME-33781: Advanced Identity Cloud now supports the [WebAuthn conditional UI](../am-authentication/authn-mfa-webauthn.html#webauthn-conditional-ui), also known as passkey autofill. This lets your end users sign in with a passkey if they've previously saved one in their browser.

* AME-34458: Enhanced the output when you test the connection in the PingOne Worker service to display the values used in the connection test to make them easier to verify. These details are extracted from the credential JWT or derived from the worker service configuration.

* AME-34513: Added support for the `_queryFilter` parameter on the `realm-config/services/pingOneWorkerService/workers` endpoint. Use this to query the configured worker services. For example, you can filter by credential type or by a property value such as the API URL.

* IAM-1478: Autofill is now disabled for fields on pages where you add identities.

* IAM-4646: Tenant administrators registered through federation no longer have the option to update their username and password on the sign-on screen.

* IAM-8699: Advanced Identity Cloud now supports [node versioning](../journeys/node-versions.html). When we make changes to a node in the future, we'll create a new version of the node.

  This release introduces new node versions for the following nodes:

  | Node                                                                                                            | Description of change                                                                                                                                |
  | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [Page node](https://docs.pingidentity.com/auth-node-ref/latest/page.html)                                       | Adds support for standalone nodes within a Page node. Standalone nodes are self-contained and can be included after the final multiple outcome node. |
  | [Platform Username node](https://docs.pingidentity.com/auth-node-ref/latest/platform-username.html)             | Adds an option to prepopulate the username if it's available in the shared state.                                                                    |
  | [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) | Adds support for the WebAuthn conditional UI, also known as passkey autofill, and removes the ability to return the challenge as JavaScript.         |
  | [WebAuthn Registration node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-registration.html)     | Removes the ability to return the challenge as JavaScript.                                                                                           |

  Other node versioning changes include:

  * Resource version `3.0` for `authenticationtrees` REST endpoint

    We've added a version-aware `3.0` resource to the `realm-config/authentication/authenticationtrees` endpoint. When sending a request to this endpoint, set the `Accept-API-Version` header to `protocol=2.1,resource=3.0`.

    Resource versions 1.0 and 2.0 are deprecated.

  * Versioned node endpoints

    The `realm-config/authentication/authenticationtrees/nodes` endpoint is now versioned. Specify the version of the node in the request URL, for example: `https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/realm-config/authentication/authenticationtrees/nodes/UsernameCollectorNode/2.0`.

    Versionless node endpoints are deprecated.

  * Audit logging

    The node version is logged in the [am-authentication](../tenants/audit-debug-log-sources.html#am-sources) source under the `AM-NODE-LOGIN-COMPLETED` event for node versions greater than `1.0`.

* IAM-9002: The **Journeys** page now has an **Add journey** button that opens a modal for creating or importing a journey. This makes the available journey options easier to find.

* IAM-9608: You can now assign an authorization policy to a SAML or OIDC application. This lets you restrict who can access an application to a subset of end users who have authenticated through a specific journey. Find more information in [Configure an application authorization policy](../app-management/configure-app-authorization-policy.html).

* IAM-9937: The [SaaS REST](../app-management/applications/saas-rest.html) and [SaaS REST (connector server)](../app-management/applications/saas-rest-rcs.html) applications now let you add filter policies to object types when you configure provisioning. Adding filters at the API level reduces network overhead, boosts synchronization performance, and prevents unwanted data from entering your identity pipeline.

* IAM-10132: The Advanced Identity Cloud admin console is now fully accessible using keyboard controls.

* IAM-10625: The Custom WS-Fed application now includes logout mode, always authenticate user, and multi-valued claim support for SSO. Find more information in [Configure the custom WS-Fed application](../app-management/register-a-custom-application.html#sso-config-custom-wsfed-app).

* IAM-10626: The Microsoft 365 application now includes logout mode and always authenticate user settings for WS-Trust SSO. Find more information in [Microsoft 365 Sign On settings](../app-management/register-a-custom-application.html#sso-microsoft-365-settings).

* IAM-10810: The PingOne worker service now lets you configure the connection to PingOne using a credential JWT.

* OPENAM-25759: The `jwtValidator` script binding now supports configurable clock skew for `expirationTime` and `issuedAt` claim validation.

* OPENAM-25910: The OAuth 2.0 introspection endpoint now supports an RFC 9701-compliant JWT response format. When enabled, token introspection claims are nested under a top-level `token_introspection` claim, which separates the `aud` claim of the introspection response from the `aud` claim of the token itself. The token's `aud` claim is also now correctly included for all token types, including stateless tokens.

* OPENAM-25936: Next-generation scripts now support the `utils.crypto.checkBcrypt(bcryptHash, password)` method for bcrypt hash verification.

* OPENAM-25957: All next-generation OAuth 2.0 scripts now have access to the `identity`, `session`, `clientProperties`, and `requestProperties` bindings.

* OPENAM-27540: You can now configure a trusted CA certificate for each OAuth 2.0 client using the `tls_client_auth` authentication method, instead of relying only on realm-wide CAs.

#### Fixes

* AME-34254: Added support for next-generation SAML SP account mapper scripts to the Advanced Identity Cloud admin console.

* FRAAS-29198: Fixed an issue where promotions that failed due to the encrypted secrets verification check were not listing the configuration paths that needed updating.

* IAM-5003: Fixed an issue where changing the locale on the terms and conditions creation page didn't change the text in the editor.

* IAM-9751: Fixed an accessibility issue where the VoiceOver screen reader was not vocalizing UI text correctly.

* IAM-10040: Fixed an issue where the browser was incorrectly using autofill if a KBA Definition Node was within a Page node. The issue prevented use of tab and arrow functionality for that node.

* IAM-10087: Fixed an issue where the password policy on a hosted pages sign-on screen disappeared on a window refresh when the **Access Management** > **Authentication** > **Settings** > **Trees** > **Enable Allowlisting** setting was enabled.

* IGA-4139\[[2](#_footnotedef_2 "View footnote.")]: Updated the access filter component in the IGA access graph to accept dynamic filter options. This lets you use different UI components to customize the available filter options, based on context.

* IGA-4275\[[2](#_footnotedef_2 "View footnote.")]: Fixed a pagination issue in the Direct Reports view by removing sortable columns and default sort from the Direct Reports and Delegates pages.

* OPENAM-25543: Allowing a SAML authentication flow to continue when a circle of trust (CoT) is inactive is now deprecated. Review your SAML configurations and ensure that any CoTs used for authentication are active before Advanced Identity Cloud begins enforcing CoT status after the end-of-life date.

* OPENAM-26359: Added a new configuration option, Enable Rich Authorization Requests with RCS, to the `OAuth2 Provider` service. This resolves an issue with remote consent where authorize requests with `authorization_details` would fail with an `invalid_request` error if an RCS was not configured.

## June 2026

### 17 June 2026

**Version 21659.11**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 4 June 2026

**Version 21659.8**

#### Fixes

* FRAAS-32554: Addressed a security issue.

## May 2026

### 18 May 2026

**Version 21659.7**

#### Enhancements

* OPENAM-26335\[[3](#_footnotedef_3 "View footnote.")]: The [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) now lets you suppress the display of the verification code in the PingOne Verify web UI.

#### Fixes

* OPENAM-26326\[[3](#_footnotedef_3 "View footnote.")]: Added a new configuration option, Enable Rich Authorization Requests with RCS, to the `OAuth2 Provider` service. This resolves an issue with remote consent where authorize requests with `authorization_details` would fail with an `invalid_request` error if an RCS was not configured.

### 15 May 2026

**Version N/A**

#### Key features

* Multi-region high availability (FRAAS-17848)

  Advanced Identity Cloud now offers a multi-region high availability deployment option as an [add-on capability](../product-information/add-on-capabilities.html). This deployment option hosts identity-related services across both a primary and a secondary region, with data replicated in near real-time. It allows for rapid failover to the secondary region in the event of a failure in the primary region, with a significantly better recovery time objective (RTO) and recovery point objective (RPO) compared to the default single-region deployment option.

  Learn more in [Architecture, availability, and disaster recovery](../tenants/environments-architecture-availability-disaster-recovery.html).

### 08 May 2026

**Version 21478.4**

#### Key features

* Snowflake connector (OPENIDM-21957)

  The [Snowflake connector](https://docs.pingidentity.com/openicf/connector-reference/snowflake.html) is now bundled with Advanced Identity Cloud. This new connector allows you to manage users, grant and revoke roles and database roles, and synchronize data between Advanced Identity Cloud and Snowflake.

  Learn more about the [1.5.20.33 Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html#1_5_20_33_connectors).

* Identity Governance Access Modeling\[[2](#_footnotedef_2 "View footnote.")] (IGA-3696)

  Advanced Identity Cloud Identity Governance introduces a new feature called Access Modeling (role mining) that analyzes existing user-to-entitlement assignments to discover potential access roles that reflect how people use access in your environment. Using advanced machine learning, it examines current roles and entitlements across your access landscape to propose new role candidates and suggest changes to existing ones.

  Access Modeling is an Advanced Identity Cloud add-on capability that integrates with the Identity Governance add-on capability.

#### Enhancements

* IAM-1715: Improve messaging on back button for 404 pages in the Advanced Identity Cloud admin console.

* IAM-3829: You can now perform dry-run promotions in the Advanced Identity Cloud admin console.

* IAM-3834: Distinguish between dry-run and actual promotions in the promotion report in the Advanced Identity Cloud admin console.

* IAM-8149, IAM-8275, IAM-8988: Added the following configuration options to the Advanced Identity Cloud admin console when you create or edit a journey:

  * `Override authenticated session timeout`, `Maximum Session Time`, and `Maximum Idle Time`

  * `Transactional Only`

  * `No Session`

  Previously, these settings could only be configured over REST.

* IAM-8972: You can now configure managed objects and relationships in the Advanced Identity Cloud admin console.

* IAM-9819\[[4](#_footnotedef_4 "View footnote.")]: Added the ability to export custom reports.

* IAM-9822: You can now perform promotion rollbacks in the Advanced Identity Cloud admin console.

* IAM-9903\[[4](#_footnotedef_4 "View footnote.")]: Added the ability to import custom reports.

* IAM-9960: Added a wider scope to the monitoring search feature by being able to search on `/payload/message` and just `/payload` in cases where the monitoring record's payload is a string.

* OPENIDM-22009: All connectors included with Advanced Identity Cloud were upgraded. Learn more in [1.5.20.34 Connector changes](https://docs.pingidentity.com/openicf/connector-release-notes/connectors.html#1_5_20_34_connectors).

* IGA-4036: Added the ability to add and remove members of an entitlement directly from the entitlement LCM users tab.

#### Fixes

* FRAAS-31613: Fixed an issue where password policy updates weren't properly replicating to the datastore in mutable environments.

* IAM-1907: Fixed an issue where custom endpoint search showed an incorrect message.

* IAM-2537: Fixed an issue where non-dashboard URLs didn't show a 404 page.

* IAM-2615: Fixed an issue where border radius settings affected the hosted pages editor preview.

* IAM-3453: Fixed styling issues with the back button.

* IAM-5439: Fixed an issue where an ESV couldn't be updated after its last value was deleted.

* IAM-7502: Fixed an issue where the color in the `Card Input Border Focus Color` hosted pages setting wasn't applied to the search field in the **My Applications** hosted account page.

* IAM-9475: Fixed an issue in the hosted journey pages where a journey was allowed to continue in the event of a password mismatch when a message node was on the same page.

* IAM-9752: Fixed an issue where VoiceOver gestures didn't work on drop-down lists.

* IAM-9842: Fixed an issue where VoiceOver didn't announce text for some page elements.

* IAM-9936: Fixed an issue with the query operation in the SaaS REST application where setting the type select field prevented the method select field from being cleared, and the other way around.

* IAM-9952: Fixed an issue where the table header for the action column was empty on several pages in the hosted account pages.

* IAM-9958: Fixed an issue where the table header for the action column was empty on several pages in the Advanced Identity Cloud admin console.

* IAM-10056: Fixed an issue on the **Auth Scripts** page where the modal body failed to load after clicking **[icon: add, set=material, size=inline] New Script**.

## April 2026

### 28 Apr 2026

**Version 21182.12**

#### Enhancements

* New binding for next-generation SP adapter scripts (OPENAM-26050)

  A new `authnRequestHelper` binding has been added for next-generation SP adapter scripts. This binding lets you retrieve and modify the destination property of the `AuthnRequest`.

  Find more information in [SP adapter scripting API](../am-scripting/saml2-sp-adapter-api.html).

### 23 Apr 2026

**Version 21182.10**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 14 Apr 2026

**Version 21182.9**

#### Key features

* Partial support for Rich Authorization Requests (RAR) (AME-28325)

  The `/authorize` and `/par` endpoints now optionally accept the `authorization_details` parameter from the RAR (Rich Authorization Requests) specification RFC 9396, allowing clients to specify fine-grained authorization requirements.

* App Policy Decision node (AME-30063)

  A new [App Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/app-policy-decision.html) is a specialized policy node that lets you enforce OIDC and SAML application access policies in journeys. You can use the node to filter access by group, organization, and more.

* Support for audience parameter in token exchange (AME-33970)

  A client can now specify audience parameters in OAuth 2.0 Token Exchange requests. These parameters can be allowlisted and, if valid, are included in the audience claim of the resulting token.

* Next-generation scripted JWT operations (OPENAM-25836)

  The `jwtValidator` and `jwtAssertion` bindings are now available in all next-generation scripts.

#### Enhancements

* AME-33573: Next-generation scripts now include `utils.base64url.encode()` and `utils.base64url.decodeToBytes()` for Base64URL encoding and decoding.

* AME-33971: Added a new Save and Test Connection button to the PingOne worker configuration screen allowing you to validate the connection.

* AME-33973: You can now configure the PingOne Worker Service connection using a credential JWT.

* AME-34248: You can now use next-generation scripts in the Social Provider Handler node to transform normalized profile data into identities or managed users.

* AME-34249: You can now use next-generation scripts in the OIDC ID Token Validator node. The `jwtClaims` binding now behaves as a native JavaScript object.

* AME-34540: You can now specify autocomplete attributes for username nodes.

* OPENAM-21474: A new `Minimum max_age for Authorize Requests` property is now available in the advanced OIDC settings of the OAuth 2.0 provider service.

* OPENAM-24523: You can now dynamically modify the scopes of a refresh token during the refresh flow with the new next-generation scope validation script binding, `scopeValidatorHelper`, and its method, `inheritAccessTokenScopesOnRefresh()`. This is useful when scope validation scripts alter access token scopes and you need the refresh token to inherit those changes.

* OPENAM-25901: Next-generation OAuth 2.0 scope validation scripts now have access to the `availableScopes` binding, which lists all scopes configured for the client. A new `throwInvalidScope()` method is also available to simplify error handling.

#### Fixes

* AME-34216, AME-34398: When using an SSO token as the subject for a policy with an `IDM user` environment condition, it now correctly resolves to the IDM `_id` instead of the user's AM universal ID.

  You can temporarily revert this behavior by setting the ESV `esv.am.policy.condition.idm.universalId` to `true` to let you update policies to use another property.

* AME-34329: By default, parallel updates can no longer be made for CTS sessions. You can revert this behavior by setting the ESV `esv.cts.use.etag.assertion.on.updates` to `false`.

* FRAAS-31318: Fixed an issue where setting certain special characters in an ESV prevented the ESV from being interpreted correctly.

### 10 Apr 2026

**Version 21027.5**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 01 April 2026

**Version 21027.2**

#### Key features

* Policy Decision node (AME-28779)

  A new [Policy Decision node](https://docs.pingidentity.com/auth-node-ref/latest/policy-decision.html) lets you evaluate an authorization policy against resources within an authentication journey.

* Backchannel Notification node (AME-32579)

  Introduced a new [Backchannel Notification node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-notification.html) that allows a backchannel journey to send real-time status updates to the main authentication journey.

#### Enhancements

* FRAAS-28387: Invites for Advanced Identity Cloud tenant registration now use a one-time passcode (OTP) instead of a magic link. This change prevents email scanners from accidentally invalidating single-use links.

* AME-29745: Improved the certificate validation process in the Certificate Collector and Certificate Validation nodes. By default, Advanced Identity Cloud collects the *first* certificate in a certificate chain (the user certificate). You can now create an ESV named `esv-am-nodes-certificatechain-validation-enforced` and set its value to `true` to collect the chain of certificates.

* AME-33851: You can now use next-generation scripts for social identity provider transformation scripts.

* OPENAM-23610: The default value for the Return challenge as JavaScript (Legacy) property on the WebAuthn Authentication and WebAuthn Registration nodes is now not enabled. Ping Identity recommends that you keep this setting.

* OPENAM-25329: The PingOne Protect Initialize node now includes an `Additional Signals SDK Initialization Options` attribute. This allows you to configure options that aren't already defined in the node. The `PingOneProtectInitializeCallback` has been updated with new fields to support this.

* OPENAM-25677: The `PingOneProtectInitializeCallback` now includes a `universalDeviceIdentification` field, which replaces the deprecated `enableTrust` field. The `enableTrust` field is still returned for backward compatibility.

#### Fixes

* IGA-4186\[[2](#_footnotedef_2 "View footnote.")]: Fixed an issue for user LCM in the hosted account pages where large user populations weren't correctly sorted and paginated.

* OPENAM-22698: Fixed a bug that caused duplicate URIs in WS-Federation responses.

## March 2026

### 31 Mar 2026

**Version 20814.9**

#### Enhancements

* The following OAuth 2.0 scripts can now use the next-generation scripting engine, which gives them access to common bindings such as `utils` and `openidm`:

  * AME-33228: OIDC claims

  * AME-33846: Scripted JWT validator

  * AME-33847: Scope validation

  * AME-33848: Authorize endpoint data provider

  * AME-33849: Scope evaluation

  * AME-33850: May act

* The following SAML 2.0 scripts can now use the next-generation scripting engine, which gives them access to common bindings such as `utils` and `openidm`:

  * AME-32919: SP adapter

  * AME-32920: IDP adapter

  * AME-32921: IDP attribute mapper

* AME-32969: You can now make sure the `samlApplication` binding is available for all SAML flows by enabling the application context in the hosted IdP or remote SP entity configuration. Previously this was only added in certain situations such as when using an application journey or IdP-initiated integrated mode.

* AME-32997: Added an `Allow Retry` option to the Backchannel Initialize node that lets end users retry a failed backchannel authentication journey.

* AME-33430: You can now include remote consent agent credentials in a `Basic Authentication` header for pushed consent requests.

* AME-33930: A new `testConnection` action on the `realm-config/services/pingOneWorkerService/workers/pingone-worker-service-name` endpoint lets you test the connection from Advanced Identity Cloud to PingOne.

* AME-33939: A new `listLatestNodeDefinitions` action on the `realm-config/authentication/authenticationtrees/nodes` endpoint provides a list of node definitions for the *latest* version of each node.

  This action combines the responses from the following separate actions into a single response:

  * `getAllTypes` action on the `realm-config/authentication/authenticationtrees/nodes` endpoint

  * `schema`, `template` and `listOutcomes` actions on the `realm-config/authentication/authenticationtrees/nodes/node-name` endpoint

* ANALYTICS-1383\[[4](#_footnotedef_4 "View footnote.")]: The new historical change report feature provides a complete audit trail of changes to your managed identities. It tracks all modifications to user profiles, roles, accounts, and applications. You can easily generate reports to see what changed, who made the change, and when it happened, which gives you clear insights for compliance and security monitoring.

* FRAAS-29084: Custom domains are now restricted to a maximum of 63 characters in the Advanced Identity Cloud admin console. This restriction has always existed on the system backend.

* OPENAM-22125: A new Proxy Configuration tab in the Http Client Service configuration lets you use separate proxy configurations per HTTP Client instance.

* OPENAM-24476: Added `java.util.zip` classes to the allowlist for the Scripted Decision node scripting context.

* The following enhancements have been made to the nodes provided with Advanced Identity Cloud:

  * AME-33009: Enhanced the RADIUS Decision node to capture Vendor-Specific Attributes (VSA) returned by the RADIUS server during authentication.

  * Enhancements to the PingOne Protect Evaluation node:

    * AME-33807: Fixed an issue where a default value was sent for the flow subtype. Previously, the node would fall back to using the value configured in Authentication Flow Subtype or Authorization Flow Subtype. Now, if nothing is found in the node state, the node doesn't send a value to PingOne Protect.

    * OPENAM-24557: Added a configuration property that lets you specify a custom session ID in the node state.

    * OPENAM-24562: Added two configuration properties that let you include a custom browser cookie and any externally maintained `deviceId` in the request sent to PingOne.

    * OPENAM-25553: Added a configuration property that lets you include user group information as part of a risk evaluation.

  * The following nodes now let you set custom headers on journey success, failure, and error:

    * AME-33813: Set Success Details node

    * AME-33874: Set Failure Details node

    * AME-33873: Set Error Details node

  * OPENAM-24401: The CAPTCHA node now prevents submission after expiry.

  * OPENAM-24419: Added a new [RSA SecurID](https://docs.pingidentity.com/auth-node-ref/latest/rsa-securid.html) node. This node replaces the Marketplace RSA SecurID node, which is now deprecated.

  * OPENAM-24489: The Device Binding and Device Signing Verifier nodes now let you specify a clock skew between the client device and AIC. This helps prevent binding failures caused by clocks being out of sync.

  * OPENAM-24546: Removed certain unused and unsupported configuration properties from the PingOne Protect Initialize node and its associated callback (`PingOneProtectInitializeCallback`).

  * OPENAM-25372: Added a [JWT Password Replay](https://docs.pingidentity.com/auth-node-ref/latest/jwt-password-replay.html) node to secure the user's password within an encrypted JSON Web Token (JWT). This node is used by PingGateway and replaces the old Password Replay scripting functionality.

* OPENAM-25371: Added a configuration property to the PingOne Verify Evaluation node to enable automatic redirection to the journey after an end user completes verification (when using the `Redirect` delivery mode).

* OPENAM-25618: The new `locales` binding lets you return the localized version of a string from a translation map. It is available to next-generation Configuration Provider node, Journey Decision node, and Device Match node scripts.

* OPENIDM-21493: You can now cancel a clustered reconciliation even when a route associated with the source or target system is unavailable.

* AME-34191: You can now override the HTTP binding used to redirect users to the SAML error page. To do this, configure an [ESV variable](../tenants/esvs.html#variables) named `esv-global-saml-error-page-http-binding` and set its value to `HTTP-POST` or `HTTP-Redirect`. If you don't set this variable, Advanced Identity Cloud uses the default value of `HTTP-POST`.

* IAM-6546: End users now have more options to manage their devices in the hosted account pages. For each device, they can view when it was last used for sign on, view when it was added, edit its name, and delete it.

* IAM-9672: In the advanced sync **Mapping** tab, if no properties have been mapped, it now shows a more accurate description of the target and source identity objects whose properties can be mapped.

#### Fixes

* AME-33653: Custom nodes now work with the Configuration Provider node.

* AME-33808: If Node State Attribute For User ID is provided in the PingOne Protect Evaluation node, but the corresponding attribute is missing from the node state, the node triggers the failure outcome rather than using the user ID associated with the AM identity.

* AME-34217: Added a version setting to the Configuration Provider node. This update provides the underlying infrastructure for a node versioning feature in an upcoming release.

* AME-34034: Fixed an issue where omitting a shared secret label in the RADIUS Decision node caused Prometheus metrics to become unavailable.

* ANALYTICS-1326\[[4](#_footnotedef_4 "View footnote.")]: Fixed an issue in custom reports caused by relationships between custom identities that contain multiple underscores.

* ANALYTICS-1367\[[4](#_footnotedef_4 "View footnote.")]: Fixed an issue in custom reports caused by IP addresses in journey events.

* OPENAM-23918: Resolved a race condition in the OATH Registration node and OATH Device Storage node where recovery codes could potentially be lost.

* OPENAM-24065: Improved consistency for error responses across realms when processing illegal arguments. The `/authenticate` call now correctly returns a 400 (Bad Request) instead of a 500 (Internal Server Error) for invalid arguments.

* OPENAM-25406: Added an `identity.exists()` method to next-generation objects returned by `idRepository.getIdentity()`. This lets scripts verify an identity's existence in the identity store before further processing.

* OPENAM-25646: For backward compatibility, we've restored the following deprecated fields sent to PingOne Protect by the PingOne Protect Initialize node (in the `PingOneProtectInitializeCallback`):

  * `consoleLogEnabled`

  * `deviceAttributesIgnored`

  * `customHost`

  * `lazyMetadata`

  * `deviceKeyRsyncIntervals`

  * `disableHub`

  |   |                                                                                                                                                                                                   |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | These fields are deprecated and no longer supported in PingOne. This fix restores the fields but you should update your clients and scripts to remove the unsupported fields as soon as possible. |

* OPENAM-25779: Deletion of the `samlApplication` object is now deferred for unsuccessful authentication journeys so that the object is still available for subsequent sign-on attempts in the same session.

* IAM-6640: Fixed an issue in the hosted pages theme preview where clicking **Edit Personal Info** opened two instances of the modal.

* IAM-8221: Fixed an issue in the terms & conditions live preview where interactive elements weren't disabled.

* IAM-9620\[[2](#_footnotedef_2 "View footnote.")]: Fixed an Identity Governance issue where clicking **Save** in the certification template creation wizard didn't disable the button after submission, which could result in the creation of unintended duplicate templates.

* IAM-9786: Fixed an issue where ESV placeholders manually entered into a field were always treated as strings, regardless of whether they were an array, list, or string.

* IAM-9886: Fixed a display issue on the **Reports Run History** tab where the pop-up menu items weren't displayed correctly.

* FRAAS-29855\[[5](#_footnotedef_5 "View footnote.")]: Fixed an issue where OTLP log streaming reported all Advanced Identity Cloud logs with `am-core` or `idm-core` as the source and omitted custom IDM event-hook logs. Logs streamed via OTLP now preserve their correct source (for example, `am-authentication`, `am-access`, `idm-access`) and include custom IDM event-hook messages.

#### Changed functionality

* OPENIDM-21718: The `maxQueueSize` for [queued synchronization](../idm-synchronization/chap-implicit-live-sync.html#queued-sync) now defaults to `1000` and can't be configured to a value higher than `1000` or lower than `100`. The previous default was `20000`.

  The `pageSize` still defaults to `100`, but now can't be configured to a value higher than `100` or lower than `10`. If the configured `pageSize` is greater than `maxQueueSize / 10`, Advanced Identity Cloud uses `maxQueueSize / 10` for the page size.

  If you have any configuration outside of these bounds, Advanced Identity Cloud automatically adjusts the values to the nearest bound.

### 26 Mar 2026

**Version N/A**

#### Related product changes

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section contains information about other Ping Identity products that are often deployed as part of an Advanced Identity Cloud implementation. |

* RCS 1.5.20.34 is now available to [download](https://backstage.pingidentity.com/downloads/browse/identity-cloud/all/productId:idm-connector-servers/minorVersion:1.5/version:1.5.20.34/language:java). To take advantage of these updates, you must manually upgrade your RCS implementation. Learn more in [ICF release notes](https://docs.pingidentity.com/openicf/connector-release-notes/preface.html).

### 17 Mar 2026

**Version N/A**

#### Deprecations

* Non-persisted schedules deprecated

  Non-persisted (in memory) schedules are now deprecated. Update your tenants to use [persisted schedules](../idm-schedules/persistent-schedules.html). You can continue to use non-persisted schedules in the short term, but they will be removed on the [end-of-life date](../product-information/deprecation-notices.html#deprecation-non-persisted-schedules).

### 10 Mar 2026

**Version N/A**

#### Related product changes

|   |                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section contains information about other Ping Identity products that are often deployed as part of an Advanced Identity Cloud implementation. |

* RCS 1.5.20.33 is now available to [download](https://backstage.pingidentity.com/downloads/browse/identity-cloud/all/productId:idm-connector-servers/minorVersion:1.5/version:1.5.20.33/language:java). To take advantage of these updates, you must manually upgrade your RCS implementation. Learn more in [ICF release notes](https://docs.pingidentity.com/openicf/connector-release-notes/preface.html).

* Support for using older versions of the web agent with Advanced Identity Cloud is now deprecated. If you have web agents in your deployment, you should upgrade to 2024.11.2 or 2025.9 and later to ensure you remain compatible in the future. Learn more in [Incompatible changes](https://docs.pingidentity.com/web-agents/latest/release-notes/changes.html).

## February 2026

### 26 Feb 2026

**Version 20512.6**

#### Changed functionality

* Connector server access configuration now added to all tenants (OPENIDM-21744)

  Ping Identity previously introduced access configuration that lets you lock down Advanced Identity Cloud connector servers so that each connector server can be accessed only by an RCS connector using that connector server's designated OAuth 2.0 client. This prevents an RCS connector associated with a particular connector server from gaining unauthorized access to the resources of other connector servers.

  When this access configuration was introduced, it was added to new tenants by default, but needed to be manually added to existing tenants. With this change, the access configuration has been added to all existing tenants too.

  The access configuration adds access rules for connector servers using the `RCSClient` OAuth 2.0 client. If you have connector servers that use a specific OAuth 2.0 client, and you haven't already added this access configuration to your tenant configuration, you need to check or modify the configuration as described in [Connector servers using specific OAuth 2.0 clients](../product-information/migration-dependent-features/rcs-configuration-migration-faq.html#connector-servers-using-specific-oauth2-clients).

### 23 Feb 2026

**Version N/A**

#### Key features

* User Principal Name (UPN) mapping available for Microsoft 365 WS-Trust SSO applications (IAM-9896\[[6](#_footnotedef_6 "View footnote.")])

  Microsoft 365 SSO applications that use the WS-Trust protocol can now map an attribute to the UPN. Learn more in [Configure WS-Trust](../app-management/register-a-custom-application.html#ws-trust-config).

  |   |                                                                         |
  | - | ----------------------------------------------------------------------- |
  |   | This feature requires Advanced Identity Cloud version 20512.5 or later. |

### 17 Feb 2026

**Version 20512.5**

#### Key features

* Identity Governance user-access graph (IGA-4051\[[5](#_footnotedef_5 "View footnote.")]\[[2](#_footnotedef_2 "View footnote.")])

  The user-access graph provides a graphical view of an end user's access. It visualizes the links between an end user and their types of access, such as roles, applications, or entitlements. Identity Governance administrators can view graphs in the Advanced Identity Cloud admin console, and end users can view their own graph in the hosted account pages.

  Learn more in [View the user-access graph](../identity-governance/administration/view-access-graph.html).

* Two-factor authentication report \[[5](#_footnotedef_5 "View footnote.")]\[[4](#_footnotedef_4 "View footnote.")]

  Advanced Reporting now lets you include information in your reports about the two-factor authentication (2FA) configurations of your end users. This includes the specific authentication methods each end user has registered and when each method was last used. This provides administrators with greater insight into second-factor adoption and helps ensure compliance with security policies.

  Learn more in [Report for two-factor authentication](../reports/administration/reports-2FA-profile-attributes.html).

#### Enhancements

* FRAAS-23284: RCS connections to Advanced Identity Cloud now have a default timeout value of `10000` (10 seconds) for new tenants. Existing tenants retain the default timeout value of `-1` (no timeout).

* FRAAS-29829: Removed a reference to "PingOne Advanced Identity Cloud" from the `404 Not Found` error page.

* IAM-4464: Next-generation configuration provider scripts created through the journey editor now contain the default config for the selected node type.

* IAM-9709: Updated the journey editor to make fewer network calls when saving a journey that contains page nodes.

#### Fixes

* IAM-4345: Fixed an issue where vertical tabs were missing a hover state.

* IAM-8033: Journey name field did not have a length check in place.

* IAM-8226: When importing a journey, if you skip the download backup option but then return to it using the **Previous** link, it now completes the backup before offering the download.

* IAM-9590: The message shown in the hosted pages for an unauthorized access attempt is now correctly centered on a single page.

* IAM-9687: When you enter a valid ESV placeholder in the URL field of a bookmark application, the field is now immediately disabled and shows a delete icon to remove the placeholder.

* IGA-4085\[[2](#_footnotedef_2 "View footnote.")]\[[5](#_footnotedef_5 "View footnote.")]: Fixed an Identity Governance access request issue where glossary schema properties displayed an extra space for nonexistent icons.

* IGA-3980\[[2](#_footnotedef_2 "View footnote.")]\[[5](#_footnotedef_5 "View footnote.")]: Fixed an Identity Governance certification issue where the certification count on the **Summary** page didn't include the `certificationType` query parameter.

### 11 Feb 2026

**Version 20340.8**

#### Fixes

* OPENAM-25702: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) again supports a Node State Attribute For Username setting. PingOne Protect risk evaluation calls can depend on the username.

* OPENIDM-21776: The Advanced Identity Cloud identity management service now uses synchronous HTTP client requests to connect to external identity management, REST, and token introspection services. This change prevents connection closure exceptions from terminating reconciliation.

### 03 Feb 2026

**Version 20340.5**

#### Fixes

* FRAAS-13233: AM script validation now ignores ESV placeholders in commented-out code.

* IAM-9803: The link to the access management native console from the Advanced Identity Cloud admin console now always correctly links to the Alpha or Bravo realm.

* OPENAM-25707: Fixed [PingOneProtectInitializeCallback](../am-authentication/callbacks-interactive.html#PingOneProtectInitializeCallback) processing to prevent unwarranted HTTP 4xx and 5xx errors.

## January 2026

### 27 Jan 2026

**Version 20133.10**

#### Fixes

* OPENDJ-11576\[[5](#_footnotedef_5 "View footnote.")]: Empty user attribute values are no longer considered when evaluating password policies.

### 21 Jan 2026

**Version 20133.8**

#### Key features

* AD Decision node to authenticate against Active Directory identity stores (AME-14959)

  The new [AD Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ad-decision.html) verifies that the provided username and password exist in the specified Active Directory data store. The node also checks whether the user account is locked, disabled, or has expired.

* Cache management service (AME-32248, AME-32285)

  A new scripted cache management service lets you create and use caches in Scripted Decision nodes. This can improve performance for slow tasks, such as fetching access tokens for third party services that can be reused between journeys. The service has its own metrics.

  Learn more in [Cache script values](../am-scripting/cache-manager.html).

* SAML 2.0 SP account mapper (OPENAM-23986)

  A new SAML 2.0 SP account mapper script type enables dynamic modification of SAML assertion data before it's used to identify local users.

  Learn more in [SP account mapper](../am-saml2/custom-sp-account-mapper.html).

* Support for SAML 2.0 IdP-initiated flows in integrated mode (AME-29258)

  You can now configure the hosted SP to redirect to a journey when a response is received from the IdP.

  Use the new configuration option to check that the IdP entity ID in the incoming SAML assertion matches the IdP entity ID configured for the node.

  A new method has also been added to the `samlApplication` script binding that returns the assertion as a JSON map.

  Learn more in [Redirect to a journey on the hosted SP](../am-saml2/configure-providers.html#config-redirect-journey).

* RADIUS authentication nodes (AME-32871)\[[5](#_footnotedef_5 "View footnote.")]

  The new [RADIUS Decision node](https://docs.pingidentity.com/auth-node-ref/latest/radius-decision.html) and [RADIUS Challenge Collector node](https://docs.pingidentity.com/auth-node-ref/latest/radius-challenge-collector.html) provide [RADIUS authentication](../am-authentication/radius-authentication.html) functionality from within a journey, where Advanced Identity Cloud is acting as the RADIUS client.

* Set Logout Details node (OPENAM-24505)\[[5](#_footnotedef_5 "View footnote.")]

  The new [Set Logout Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-logout-details.html) lets you add details to the JSON response when a journey ends with the user logging out.

* Identity Governance reports (ANALYTICS-1307)\[[2](#_footnotedef_2 "View footnote.")]\[[5](#_footnotedef_5 "View footnote.")]

  Advanced Identity Cloud now provides pre-built reports for the Identity Governance service. These reports help you understand and manage your identity governance data. Learn more in [Identity Governance Reports](../identity-governance/administration/iga-reports.html).

#### Enhancements

* AME-31153: Consent request data can now be pushed via backchannel.

* AME-31429: A new field on the remote consent agent lets you include properties from the resource owner's session as part of the consent request.

* AME-31846: Next-generation Config Provider Node scripts can now access the following additional scripted node bindings:

  * `callbacks`

  * `callbacksBuilder`

  * `jwtAssertion`

  * `jwtValidator`

  * `resumedFromSuspend`

  * `requestCookies`

  * `samlApplication`

  * `oauthApplication`

* AME-32064: The [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/saml2.html) includes a new configuration option,Validate IdP Entity ID. When enabled, the node validates that the IdP entity ID from the SAML assertion is the same as the IdP entity ID configured on the node.

* AME-32970: You can now access the application context for *all* OAuth 2.0 / OIDC flows through the `oauthApplication` binding by setting `Enable Application Context` in the OAuth 2.0 provider or at the client level. Previously, you could only use this binding when using an application journey.

* IAM-8244: Adds support for bidirectional mappings in synchronization configuration.

* IAM-8497: Added a brand administrator role to the Advanced Identity Cloud admin console. Brand administrators only have access to change hosted pages themes.

* IAM-9484: Added ability to provide translation overrides for the Waiting Message field in the Polling Wait node and the Email Suspend Message field in the Email Suspend node. This lets you provide translations when the `PollingWaitCallback` or the `SuspendedTextOutputCallback` callbacks are added using scripts.

* OPENAM-23711: Adds a Detect Connection Time Out option to the [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/social-provider-handler.html). When enabled, connection timeouts from social identity providers result in the journey following the Timeout outcome.

* OPENAM-24059: Adds support for the `android-key` WebAuthn attestation format.

* OPENAM-24130: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) now lets you set the flow subtype that's sent to PingOne Protect.

* OPENAM-24137: You can now configure the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) to obtain biographic matching data from the node state.

* OPENAM-24350: Cryptographic keys can now be derived in next-generation scripts using the PBKDF2 algorithm.

* OPENAM-24548: The [PingOne Protect Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-initialize.html) now lets you obtain PingID Device Trust Agent attributes when going through a PingOne Protect flow.

* OPENAM-24552: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) now lets you send a target application name in addition to the existing target application ID, in the PingOne Protect evaluation request

* OPENAM-24554: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) now lets you use targeted PingOne policies.

* OPENAM-24560: Removed the User Type and User Name fields from the PingOne Protect Evaluation node. The user type is always `EXTERNAL` and the user name is not applicable to external user types. Only the `User ID` is sent in the PingOne Protect evaluation request.

* OPENAM-24587: You can now override the default Google Secret Manager key ID (`kid`) values with human-readable values. Find more information in [Override default `kid` values](../am-oidc1/managing-jwk_uri.html#override-default-kid-values).

* OPENAM-25327: Next-generation OAuth 2.0 scripts can now access the `redirectUris` property on the `clientProperties` binding.

* OPENAM-25417: You can now configure the SameSite attribute for cookies in the [Set Persistent Cookie node](https://docs.pingidentity.com/auth-node-ref/latest/set-persistent-cookie.html) and the [Persistent Cookie Decision node](https://docs.pingidentity.com/auth-node-ref/latest/persistent-cookie-decision.html).

* OPENAM-25418: The attestation `fmt` type is now included in the transient state data of the WebAuthn nodes.

* OPENAM-24309: The PingOne Verify Evaluation node now supports biographic matching using multiple user attributes.

#### Fixes

* AME-32307: Fixed an issue where end users weren't able to continue a PingOne Verify journey that requested a QR code if they didn't have a separate device to scan the code.

* AME-32513: Added the `suspend` action to [Custom nodes](../journeys/node-designer.html).

* AME-32979: The Core Token Service (CTS) now stores `AUTHENTICATION_WHITELIST` tokens with millisecond-level precision for the expiry timestamp. This minimizes contention in indexes.

* IAM-8766: Fixed an issue with [mustRun](../am-authentication/configure-authentication-trees.html#enable-journey-completion) journeys and query parameters such as `forceAuth=true`, where end users were authenticated then immediately unauthenticated.

* IAM-9430: A warning is now displayed in the Advanced Identity Cloud admin console when a promotion would cause a deferred release tenant to be upgraded at the same time.

* OPENAM-20582: Lets you configure a list of accepted JWT issuers for OAuth 2.0 clients. These are now accepted in addition to the OAuth 2.0 client ID for private key JWT authentication.

* OPENAM-23929: Fixed a performance issue related to schema caching.

* OPENAM-24297: Fixed an issue where the PingOne Verify Evaluation node incorrectly returned a failure outcome when the PingOne environment timed out during the identity verification process. This could happen if an end user didn't engage with the QR code or selfie capture. The update correctly detects the `TRANSACTION_TIMED_OUT` status in PingOne responses and returns the timeout outcome, letting journeys handle timeouts distinctly from failures.

### 19 Jan 2026

**Version 19722.13**

#### Fixes

* OPENIDM-21664: Fixed a provisioning issue where application assignment was failing to create local accounts when the user count exceeded 1000.

## December 2025

### 12 Dec 2025

**Version 19722.12**

#### Fixes

* IGA-4071\[[2](#_footnotedef_2 "View footnote.")]\[[5](#_footnotedef_5 "View footnote.")]: Fixed an issue with dataflow job failures.

### 12 Dec 2025

**Version 19722.11**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 Dec 2025

**Version 19722.10**

#### Enhancements

* IAM-9663\[[5](#_footnotedef_5 "View footnote.")]: The admin console now displays the `useInPlaceholders` and `encoding` attributes for existing ESV secrets.

* IAM-9664\[[5](#_footnotedef_5 "View footnote.")]: The admin console now defaults the `useInPlaceholders` attribute to `true` when creating new ESV secrets.

### 09 Dec 2025

**Version N/A**

#### Key features

* x.509 certificate authentication for Microsoft 365 WS-Trust SSO applications (IAM-9212)

  Microsoft 365 SSO applications that use the WS-Trust protocol can use x.509 authentication. Trusted certificates are accessible to all your Microsoft 365 applications. WS-Trust is included with the WS-Federation\[[7](#_footnotedef_7 "View footnote.")] add-on.

  Learn more in [Manage Microsoft 365 application trusted certificates](../app-management/register-a-custom-application.html#sso-manage-ms-365-x509-certs).

  |   |                                                                         |
  | - | ----------------------------------------------------------------------- |
  |   | This feature requires Advanced Identity Cloud version 19722.7 or later. |

### 03 Dec 2025

**Version 19722.7**

#### Key features

* Entitlement composition certification (IGA-3827\[[5](#_footnotedef_5 "View footnote.")]\[[2](#_footnotedef_2 "View footnote.")])

  Entitlement composition certification provides a review mechanism that allows certifiers to evaluate, review, and modify the definition of entitlements within the certification process. This capability enables reviewers to submit requests to change the entitlement definition, even independently of the certification decision, with options for drafting and deferring modification requests until sign off.

  Learn more in [Create an entitlement composition certification template](../identity-governance/administration/template-entitlement-composition.html).

* Accounts page (IGA-3960\[[5](#_footnotedef_5 "View footnote.")]\[[2](#_footnotedef_2 "View footnote.")])

  The accounts page gives application owners and application administrators a single place to manage all user accounts without granting them full application configuration permissions.

  Learn more in [Accounts](../identity-governance/administration/governance-accounts.html).

#### Enhancements

* IAM-9395: Table columns are now resized uniformly across the Advanced Identity Cloud admin console.

* IAM-9429: If your production environment is configured for deferred release, you can use the new `/environment/promotion/promote` endpoint to check if running a promotion will trigger a release upgrade.

* IAM-9516: The tenant administrator profile page now prompts for re-authentication when adding or removing an MFA device.

* OPENIDM-19400: New Prometheus metric for the availability of connector servers, for example:

  `idm_icf_connector_server_availability{name="system-id",type="connector-server-type",} 1.0`.

* OPENIDM-20341: Identity management scripts now natively support Base64 encoding using the `btoa` (encode) and `atob` (decode) [global script](../idm-scripting/scripting-func-engine.html#global-utility-functions) bindings.

* OPENIDM-20790: The `openidm/sync/mappings` endpoint now [supports paging](../idm-synchronization/mappings.html#sync-mapping-paging) using either offsets or cookies.

* OPENIDM-20933: Improved task scanner exception handling. If the task scanner encounters a task that results in an exception, it now aborts only that task and continues processing the remaining tasks. Previously, the scanner would abort the entire process when any task caused an exception.

* OPENIDM-20937: New provisioner metric `idm_icf_pending`. Includes all the same tags as `idm_icf*`.

* OPENIDM-21170: Metrics for router filters now use `router_filter` for the metric name and include a `name` tag to identify the specific filter.

* OPENIDM-21171: Metrics for managed identity script hooks now use `managed-script-hook` for the metric name, `object` to tag the identity object, and `script-hook` to tag the script hook.

* OPENIDM-21172: Metrics for custom endpoints now use the new `custom_endpoint` metric name and include a `name` tag based on the custom endpoint configuration name after the hyphen. For example, a custom endpoint configuration `endpoint-onboardCustomer.json` will generate metrics with a name tag/label of "onboardCustomer". The policy service makes use of an internal scripted endpoint based on the file `policy.js`, and its metric name is `policy-js`.

* OPENIDM-21233: The `openidm/health/ready` endpoint has been enhanced to include the number of waiting requests. A new set of metrics have been added to provide a historical accounting of IDM health.

#### Fixes

* FRAAS-28885\[[5](#_footnotedef_5 "View footnote.")]: ESV secret `useInPlaceholders` attribute is now taken into account by promotion integrity checks.

* IAM-9466: Annotation comments added to sub-nodes are now saved correctly.

* IAM-9496: The tooltip in journey comments now correctly displays the creator's name without overflow.

* IAM-9527: The hosted account pages logo now correctly uses the height specified in the theme.

* OPENICF-3277: The SaaS REST connector no longer throws a `NullPointerException` when attributes are missing in the request payload.

* OPENIDM-20525: The `cn` and `telephoneNumber` schema for `alpha_user` and `bravo_user` are now `scope: public` and `searchable: true`. This schema change applies to tenants created on or after December 3, 2025. Existing tenants are unchanged.

* OPENIDM-20863: Default values for multivalue mappings are now copied by value to prevent unintended mutations during runtime.

* OPENIDM-21421: Updating the configuration of an inactive provisioner no longer throws an `IllegalStateException`.

* OPENIDM-21454: Every failed record from a live sync is now stored in the dead-letter queue with a unique entry ID.

#### Changed functionality

* Default API version for unversioned requests to `openidm/*` endpoints (OPENIDM-21191)

  Previously, REST API requests made to `openidm/*` endpoints without an `Accept-API-Version` header defaulted to the latest available API version for the resource. These unversioned requests now default to API version `1.0` for most resources. However, the `consent`, `scheduler/job`, `scheduler/trigger`, and `schema` endpoints default to API version `2.0`.

## November 2025

### 20 Nov 2025

**Version N/A**

#### Key Features

* WS-Trust for Microsoft 365 SSO applications (IAM-8263)

  Microsoft 365 SSO applications can now use the WS-Trust protocol for legacy rich applications and hybrid joined devices. WS-Trust is included with the WS-Federation\[[7](#_footnotedef_7 "View footnote.")] add-on.

  Learn more in [Register an SSO application > Microsoft 365](../app-management/register-a-custom-application.html#sso-microsoft-365).

  |   |                                                                         |
  | - | ----------------------------------------------------------------------- |
  |   | This feature requires Advanced Identity Cloud version 19521.3 or later. |

### 11 Nov 2025

**Version 19521.3**

#### Enhancements

* FRAAS-28370: Fixed an issue where requests to the `/monitoring/prometheus/am` and `/monitoring/prometheus/idm` endpoints occasionally didn't return timely responses.

* IAM-1709: Exposed `useInPlaceholders` and `encoding` attributes when creating ESV secrets in the admin console.

* IAM-9312: Table columns are now resized uniformly across the following Advanced Identity Cloud admin console pages:

  * **Tenant settings**

  * **Scripts**

  * **Security**

  * **Terms & Conditions**

* IAM-9323: Added **Metadata** tab to user resource page to display properties such as `createDate` and `loginCount`.

#### Fixes

* IAM-9217: Fixed cron schedule validation for new jobs.

## October 2025

### 28 Oct 2025

**Version 19379.7**

#### Key features

* Audit logging of modifications to environments (FRAAS-17087)

  You can now use the `/monitoring` endpoints and [log streaming](../tenants/audit-debug-logs-push.html) to track configuration changes made to your environments. The new [environment-access](../tenants/audit-debug-log-sources.html#environment-access) log source captures environment changes as audit events.

  This enhancement improves visibility and observability for environment updates, helping teams monitor configuration activity, identify unexpected changes, and support troubleshooting or alerting workflows.

### 21 Oct 2025

**Version 19190.10**

#### Key features

* Create custom authentication nodes (IAM-5759)

  Advanced Identity Cloud lets you create your own nodes to reuse common functionality in authentication journeys. Define properties and run custom server-side scripts in these nodes to dynamically set values and decide the outcome of journeys.

  Learn more in [Custom nodes](../journeys/node-designer.html).

* Next-generation OAuth 2.0 access token modification scripts (AME-31083)

  You can now create next-generation access token modification scripts that can use next-generation common bindings, such as `httpClient`, `openidm`, and `utils`.

* Ability to configure journeys as *transactional only* (AME-31843)

  A transactional authentication journey only runs when Advanced Identity Cloud starts a transaction, which happens when Advanced Identity Cloud does one of the following:

  * Initializes [backchannel authentication](../am-authentication/backchannel-authentication.html) using either the `/authenticate/backchannel/initialize` endpoint or the [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html).

  * Runs a [SAML 2.0 app](../am-saml2/configure-providers.html#samlapp-journey) journey for a remote SP.

  * Runs an [OAuth 2.0 app](../am-oauth2/oauth2-register-client.html) journey when Advanced Identity Cloud is acting as an authorization server.

  * Enforces a [transactional authorization](../am-authorization/transactional-authorization.html) policy.

  You can only configure transactional authentication journeys using the REST API. Set the `transactionalOnly` property to `true` in the journey configuration.

* Mapping custom key IDs to secrets (AME-31380)

  You can now map custom `kid` header values for JWTs signed with the signing key to a specific ESV secret.

* Nodes to support backchannel authentication journeys (AME-31636 and AME-31635)

  The new [Backchannel Initialize node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-initialize.html) and [Backchannel Status node](https://docs.pingidentity.com/auth-node-ref/latest/backchannel-status.html) let you implement backchannel authentication from within a journey.

* Journey binding for scripted nodes (OPENAM-23127)

  The new `journey` binding for scripted nodes lets you obtain details of the current journey, including inner or child journeys.

#### Enhancements

* AME-30984 and AME-30609: Enhanced authentication audit logging to include the SAML Identity Provider (IdP) and Service Provider (SP) entity IDs during SAML flows. This information lets you report on the SAML applications users are accessing, supporting analytics and dashboarding efforts.

* AME-30985: In SAML v2.0 single sign-on (SSO) flows, the JSON web token (JWT) created in the browser's session storage no longer expires.

* AME-31082 and SDKS-3681: Added support for device token refreshing to the Push Notification Service endpoint, enabling the reception of new tokens from mobile devices.

* AME-31351 and AME-31471: Improvements to the Device Code flow mean that end users are now prompted to reauthenticate even when there's an existing session for must-run and app journeys.

* AME-31398: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) has been enhanced to support custom attributes. To specify custom attributes to be used in PingOne Protect for custom predictors, set the `Node State Attribute For Custom Attributes` in the node configuration. The node retrieves a map of custom attributes from the node state to be used in the evaluation request to PingOne Protect.

* AME-31656 and AME-31468: The [PingOne Protect Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-protect-evaluation.html) has been enhanced to support dynamic risk policy IDs and target app IDs. To set the risk policy set ID dynamically, enable `Use Node State Attribute For Risk Policy Set ID` in the node configuration. To set the target app ID dynamically, enable `Use Node State Attribute For Target App ID` in the node configuration. This instructs the node to obtain these IDs from the node state.

* AME-31487: Improvements to SAML v2.0 standalone mode include replacing legacy JSPs with URL endpoints.

  You can still invoke the JSPs because they're mapped to URLs for backward compatibility, but any customizations to these JSPs will be lost.

  The following URLs supersede SAML v2.0 JSPs:

  > **Collapse: URLs**
  >
  > | Old URL                                     | New URL               |
  > | ------------------------------------------- | --------------------- |
  > | `/saml2/jsp/exportmetadata.jsp`             | `/ExportSamlMetadata` |
  > | `/saml2/jsp/idpSingleLogoutInit.jsp`        | `/IDPSloInit`         |
  > | `/saml2/jsp/idpSingleLogoutRedirect.jsp`    | `/IDPSloRedirect`     |
  > | `/saml2/jsp/idpSingleLogoutPOST.jsp`        | `/IDPSloPOST`         |
  > | `/saml2/jsp/idpMNIRedirect.jsp`             | `/IDPMniRedirect`     |
  > | `/saml2/jsp/idpMNIRequestInit.jsp`          | `/IDPMniInit`         |
  > | `/saml2/jsp/idpSSOFederate.jsp`             | `/idpSSOFederate`     |
  > | `/saml2/jsp/spAssertionConsumer.jsp`        | `/Consumer`           |
  > | `/saml2/jsp/saml2AuthAssertionConsumer.jsp` | `/AuthConsumer`       |
  > | `/saml2/jsp/spSingleLogoutInit.jsp`         | `/SPSloInit`          |
  > | `/saml2/jsp/spSingleLogoutRedirect.jsp`     | `/SPSloRedirect`      |
  > | `/saml2/jsp/spSingleLogoutPOST.jsp`         | `/SPSloPOST`          |
  > | `/saml2/jsp/spMNIRedirect.jsp`              | `/SPMniRedirect`      |
  > | `/saml2/jsp/spMNIPOST.jsp`                  | `/SPMniPOST`          |
  > | `/saml2/jsp/spMNIRequestInit.jsp`           | `/SPMniInit`          |
  > | `/saml2/jsp/spSSOInit.jsp`                  | `/spssoinit`          |
  > | `/saml2/jsp/idpSSOInit.jsp`                 | `/idpssoinit`         |
  > | `/saml2/jsp/idpSSOFederate.jsp`             | `/idpSSOFederate`     |
  > | `/saml2/jsp/SA_IDP.jsp`                     | `/idpsaehandler`      |
  > | `/saml2/jsp/SA_SP.jsp`                      | `/spsaehandler`       |

* OPENAM-23051 and AME-31918: A new ESV, `esv.oauth2.request.object.restrictions.enforced` lets you enforce stricter adherence to the [PAR](https://www.rfc-editor.org/rfc/rfc9126.html) and [JAR](https://www.rfc-editor.org/rfc/rfc9101.html#section-5.2) specifications.

  Setting the value of this ESV to `true` enforces the following: **The authorization server ignores authorize parameters outside the `request_uri`. **When sending a JWT-Secured Authorization Request (JAR), the `request_uri` *must* be an `https` URI.

* IAM-8236: The ability to edit journeys from the AM native admin console has been removed. Use the Advanced Identity Cloud admin console to edit journeys.

* IAM-9000, IAM-9001: Add annotations and sticky notes to journeys to assist learning and collaboration.

* IAM-9237: Allow ESVs to be embedded in URL fields for federation IdPs. This lets you set up federation IdPs with fewer ESVs because you can define a single ESV containing a UUID shared by multiple URL fields.

* IAM-9246: Table columns are now resized uniformly across all table views.

* OPENAM-20776: A new OIDC client configuration option, `Private Key JWT Audience`, lets you configure and override the audience (`aud`) claim of a Private Key JWT.

* OPENAM-21783: Improved token management for OAuth 2.0 client applications.

* OPENAM-23669: *Full* scopes (scopes ending in `*`) can now be used by service accounts in all cases where more specific scopes (for example, `:read`) are used.

* OPENAM-23710: The `httpClient` binding is now available to legacy SAML 2.0 IdP adapter scripts.

* OPENAM-23850: Enhanced the [PingOne Verify Evaluation node](https://docs.pingidentity.com/auth-node-ref/latest/pingone/pingone-verify-evaluation.html) with an `Allow same device verification` option that lets end users continue verification on their current device.

* OPENAM-23867: The [LDAP Decision node](https://docs.pingidentity.com/auth-node-ref/latest/ldap-decision.html) no longer logs credential failures as errors. It now logs them at the `info` level.

* OPENAM-24062: Added support for the `ECDSA` algorithm to the `utils.crypto.subtle` next-generation binding. This algorithm is supported for key generation, signing, and verification.

#### Fixes

* AME-31351 and AME-31471: Improvements to the Device Code flow mean that end users are now prompted to reauthenticate even when there's an existing session for must-run and app journeys.

* AME-31481: Validation around policy creation has been improved. If you're using the legacy "Policy" environment condition (or a custom environment condition), you'll need to add that to the list of allowed environment conditions for your policy set to create or update policies that use that condition type.

* IAM-9153: Password validation now works correctly when pasting a value that matches the existing value.

* OPENAM-20749: A new ESV, `esv-enable-oauth2-sync-refresh-token-issuer` causes a stateful OAuth 2.0 introspect response to overwrite the `iss` claim of the introspectable token. To enable this behavior, set this ESV to `false`.

* OPENAM-23770: Canceling a WebAuthn flow now results in a `Client Error` outcome, rather than an internal failure.

* OPENAM-24159: Fixed an issue that prevented multiple [Identity Assertion](https://docs.pingidentity.com/auth-node-ref/latest/identity-assertion-node.html) nodes from being used in a single journey.

### 09 Oct 2025

**Version 19054.10**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

## September 2025

### 30 Sept 2025

**Version 19054.9**

#### Enhancements

* OPENAM-24486: Improved performance when creating large numbers of OAuth 2.0 clients simultaneously.

#### Fixes

* OPENDJ-11486: Fixed an exception caused when identity management queries for users with a filter containing wildcards and specific object classes.

#### Related releases

|   |                                                                                                                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section contains information about releases of other Ping Identity products that are often deployed as part of an Advanced Identity Cloud implementation. To take advantage of these updates, you must manually upgrade your RCS implementation. |

* RCS 1.5.20.32 is now available to [download](https://backstage.pingidentity.com/downloads/browse/identity-cloud/all/productId:idm-connector-servers/minorVersion:1.5/version:1.5.20.32/language:java). Learn more in [ICF release notes](https://docs.pingidentity.com/openicf/connector-release-notes/preface.html).

### 26 Sept 2025

**Version 18842.11**

#### Fixes

* IAM-9374: Fixed an issue where managed identity searches were querying all properties, causing slow performance.

### 25 Sept 2025

**Version 18842.10**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 22 Sept 2025

**Version N/A**

#### Key Features

* Log event exporter (FRAAS-19963)

  Advanced Identity Cloud now lets you export log event data to an external monitoring tool, such as an OpenTelemetry-compatible SIEM or Splunk. This helps you monitor events and troubleshoot issues in near real time.

  Learn more in [Export log events to an external monitoring tool](../tenants/audit-debug-logs-push.html).

  |   |                                                                         |
  | - | ----------------------------------------------------------------------- |
  |   | This feature requires Advanced Identity Cloud version 18842.8 or later. |

### 17 Sept 2025

**Version 18842.8**

#### Enhancements

* ANALYTICS-582\[[8](#_footnotedef_8 "View footnote.")]\[[4](#_footnotedef_4 "View footnote.")]: Custom objects can now be used as data sources for reporting. The system uses an object's configured title for the data source name, makes its properties available as attributes, and represents all object relationships.

* ANALYTICS-1165\[[8](#_footnotedef_8 "View footnote.")]: Added the capability to change a report name.

* ANALYTICS-1195\[[8](#_footnotedef_8 "View footnote.")]: Added the ability to import and export report templates using reports API endpoints.

* FRAAS-25919: You can now use the API to configure custom domains for the Advanced Identity Cloud admin console.

* IAM-8922: The Advanced Identity Cloud admin console now accepts ESV placeholders for the following federation fields:

  * Application ID

  * Application Secret

  * Well-Known Endpoint

  * Authorization Endpoint

  * User Info Endpoint

  * Token Endpoint

  * Issuer

* IAM-8982\[[2](#_footnotedef_2 "View footnote.")]: Add event function for setting the query filter/select options of a select field.

* IAM-9066: Added **Tenant Auditor** option to Advanced Identity Cloud admin console federation groups claim.

* IAM-9099, IAM-9146, IAM-9167: Many table views now support column resizing and customization.

#### Fixes

* IAM-5488: Terms and Conditions now respects target attribute in anchor tags.

* IAM-6588: The Advanced Identity Cloud admin console now correctly displays journey status for journeys disabled and enabled using ESVs.

* IAM-8887: Prevent browsers auto-filling passwords in user registration journeys.

* IAM-8940: Managed identity number property now accepts float values.

* IAM-8956: Deselecting the **Personal Information** option now disables the section containing the user avatar in hosted account pages.

* IAM-9169: Fixed styling for responsive table layouts with sticky action column in **Identities** table views.

* OPENIDM-21372: Advanced Identity Cloud now prevents access to the identity repository endpoint, `/openidm/repo`. This prevents uncontrolled and potentially incompatible schema changes.

#### Additional information

The new [PingOne integration guide](../integrations/pingone.html) helps you configure Advanced Identity Cloud to use PingOne products such as PingOne Protect and PingOne Verify. The guide covers the following topics:

* Best practices for naming and arranging PingOne environments.

* Best practices for configuring PingOne workers and Advanced Identity Cloud worker services when integrating with PingOne products.

* How to configure, test, and optimize PingOne Protect.

### 16 Sept 2025

**Version 18712.11**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 12 Sept 2025

**Version 18712.10**

#### Enhancements

* OPENAM-24476\[[3](#_footnotedef_3 "View footnote.")]: Added `java.util.zip.Deflater`, `java.util.zip.Inflater`, `java.util.zip.DeflaterOutputStream`, and `java.util.zip.InflaterInputStream` to the allowlist for Scripted Decision nodes.

### 10 Sept 2025

**Version 18712.8**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 03 Sept 2025

**Version 18712.7**

#### Enhancements

* FRAAS-24857: CNAME verification is no longer required when creating a custom domain.

* FRAAS-25547: The sender address for emails sent to Advanced Identity Cloud tenant administrators is now `saas@pingidentity.com`.

* FRAAS-26063: You can now override the `samlErrorPageUrl`. To do so, configure an [ESV variable](../tenants/esvs.html#variables) named `esv-global-saml-error-page-url` and set its value to your SAML error page URL. If you don't set this variable, Advanced Identity Cloud uses the default value of `/saml2/jsp/saml2error.jsp`.

#### Fixes

* FRAAS-25734: Exception stacktraces in access management and identity management logs are now truncated to approximately 300-400 lines.

* FRAAS-25821\[[9](#_footnotedef_9 "View footnote.")]: Fixed an issue that prevented IP rules in Proxy Connect from being disabled.

### 01 Sept 2025

**Version 18368.14**

#### Fixes

* AME-32756: Fixed an issue with policy evaluation returning results from a stale policy index cache.

* OPENDJ-11634: Advanced Identity Cloud now prevents searches with many results and no applicable index from overloading the system.

## August 2025

### 19 Aug 2025

**Version 18368.10**

#### Enhancements

* OPENAM-24384: Added `javax.crypto.SecretKeyFactory`, `javax.crypto.spec.PBEKeySpec`, and `com.sun.crypto.provider.PBKDF2KeyImpl` classes to the allowlist for the `OAUTH2_ACCESS_TOKEN_MODIFICATION` scripting context.

#### Fixes

* OPENAM-24393\[[3](#_footnotedef_3 "View footnote.")]: Fixed an issue where the InnerTreeEvaluator node failed for authentication journeys initially accessed using REST without an `authId`.

### 12 Aug 2025

**Version 18368.8**

#### Key features

* Policy binding for next-generation scripting (AME-26150)

  The next-generation `policy` binding lets you access the policy engine API and evaluate policies from within scripts. The `policy` binding works in a similar way to the [Request policy decisions for a specific resource](../am-authorization/rest-api-authz-policy-decisions.html#rest-api-authz-policy-decision-concrete) API call.

* Set Error Details node (AME-30968)

  The [Set Error Details node](https://docs.pingidentity.com/auth-node-ref/latest/set-error-details.html) adds details to the JSON response when a journey ends in an error.

* Monitor log entries in the admin console (FRAAS-25665)

  Advanced Identity Cloud now provides a console for monitoring log entries in development and sandbox\[[10](#_footnotedef_10 "View footnote.")] environments. You can view, filter, and search log entries for specific log sources within a timeframe to quickly identify issues, track events, and ensure system security.

  Learn more in [Monitor log entries in the admin console](../tenants/audit-debug-logs-monitoring.html).

  |   |                                                                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | This is a [beta](../product-information/release-lifecycle.html#beta) feature and is limited to development and sandbox\[[10](#_footnotedef_10 "View footnote.")] environments. It's not available in production environments. |

* Custom WS-Fed applications (IAM-8261)

  You can now create custom WS-Fed\[[7](#_footnotedef_7 "View footnote.")] applications for single sign-on (SSO).

* Try In SDK button (IAM-8618)

  A **Try In SDK** button has been added to the **Details** page for Native / SPA applications. This lets developers quickly test SDKs with dynamic configuration code snippets.

#### Enhancements

* AME-31372\[[5](#_footnotedef_5 "View footnote.")]: An **Agent** journey is now available by default in both Alpha and Bravo realms. The `Agent` journey makes it easier to integrate with Ping Identity agents and gateways. It validates the agent credentials with an [Agent Data Store Decision](https://docs.pingidentity.com/auth-node-ref/latest/agent-data-store-decision.html) node.

* AME-30050: You can now enable a next-generation script in the AM native admin console native console to run after a Dynamic Client Registration request is processed.

* AME-30716: Removed `Failed to create SSO Token` from logs at warning level. To observe these warnings, increase the log level to debug.

* AME-30801: The [Inner Tree Evaluator node](https://docs.pingidentity.com/auth-node-ref/latest/inner-tree-evaluator.html) now has an optional **Error Outcome** that lets you capture exception details if an exception occurs during the evaluation of the child journey.

* FRAAS-25818: The built-in SMTP server in new tenants now has a limit of 10 emails per minute and a fixed email sender address with the format `noreply@<tenant-fqdn>`.

* IAM-7581: Text wrapping in table views has been improved for readability.

* IAM-8573: IDM now includes an endpoint to retrieve individual themes from the `/themerealm` configuration using either an `ID` or a `_queryFilter` by name. This improves performance and ensures reliable theme loading, even on slow networks.

* IAM-8610: When you create an SSO application for Microsoft 365, the application now generates a signing certificate, which you can download or rotate as needed.

* IAM-8633: You can now add, remove, and rearrange table columns for managed identities and application provisioning tables.

* IAM-8925\[[11](#_footnotedef_11 "View footnote.")]: In Identity Governance, you can now configure actions that trigger automatically when a form first loads or when a user changes the value of a specific field.

* OPENAM-22467: Customers can now provide any value in the `typ` header in JWTs.

* Greater control over journey session duration and authenticated session timeouts:

  * OPENAM-23265: The [Set Session Properties node](https://docs.pingidentity.com/auth-node-ref/latest/set-session-properties.html) now lets you customize the **Maximum Session Time** and **Maximum Idle Time** of the session granted at the end of the journey.

  * OPENAM-23290: The new [Update Journey Timeout node](https://docs.pingidentity.com/auth-node-ref/latest/update-journey-timeout.html) lets you update the timeout of the journey.

  * OPENAM-23291: The [Email Suspend node](https://docs.pingidentity.com/auth-node-ref/latest/email-suspend.html) now lets you configure the **Suspend Duration** in minutes. This duration overrides existing global or realm settings.

  * OPENAM-23515: You can now set the suspend duration in next-generation scripted decision nodes when suspending the journey.

* OPENAM-23438: Following WebAuthn registration and authentication, new information is added to the transient state.

* OPENAM-20709: On successful authentication, the [WebAuthn Authentication node](https://docs.pingidentity.com/auth-node-ref/latest/webauthn-authentication.html) now adds the UUID of the device (`webauthnDeviceUuid`) and the name of the device (`webauthnDeviceName`) to the shared state. This lets you track the use of biometric authentication and the device used to authenticate.

#### Fixes

* AME-30969: If the **OIDC Claims Plugin Type** in the OAuth 2.0 provider is set to `SCRIPTED` but no script is selected, the `userinfo` endpoint now returns the `sub` claim, in compliance with the OIDC specification. Previously, the `userinfo` endpoint returned an empty JSON object. If you still require this behavior, set the `esv-scripting-legacynulloidcclaimsscriptbehaviour` ESV to `true`.

* IAM-4397: Fixed an issue in the hosted journey pages where the prompt text for the Choice Collector node wasn't fully visible and the default option wasn't visible at all.

* IAM-8632: Fixed an issue where validation errors were incorrectly displayed for pre-populated fields.

* IAM-8789: Managed identity modals now correctly handle both single-value and array-based enum types.

* IAM-8871: The hosted account pages no longer freeze and throw an error when editing details if there are empty custom enum array values.

* IAM-8902: The application username field in SAML 2.0 NameID flows is now correctly set to `uid` instead of `username`.

* IAM-8933: Fixed an issue in the Advanced Identity Cloud admin console when creating or modifying identity objects with a required boolean property. You can now set the value of the required boolean property to `false`.

* IAM-9062: Hosted pages themes no longer continuously refresh when trying to set up or confirm two-factor authentication (2FA).

* OPENAM-20749: For server-side OAuth 2.0 tokens, the [/oauth2/introspect](../am-oauth2/oauth2-introspect-endpoint.html) response can now overwrite the `iss` claim of the introspectable token. To enable this behavior, set the `esv-enable-oauth2-sync-refresh-token-issuer` ESV to `false`.

* OPENAM-22928: When agents authenticate to Advanced Identity Cloud, the session created no longer expires.

* OPENAM-23303\[[5](#_footnotedef_5 "View footnote.")]: Fixed an issue where access management scripts were failing to load because they contained strings that resembled configuration placeholders. The code that parses these scripts now correctly ignores configuration placeholders and any strings that resemble them.

  |   |                                                                                                                                                                                                                                                   |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you have access management scripts that reference ESVs, ensure that they use the correct syntax for ESVs. For example, for a script that references an ESV named `esv-my-variable`, use the syntax `systemEnv.getProperty("esv.my.variable")`. |

* OPENAM-23334: You can now use the `mergeShared` and `mergeTransient` methods to add nested objects to `ObjectAttributes`.

* OPENAM-23519: Improved error handling during WebAuthn registration when the Android lock screen isn't enabled.

* OPENAM-24159: Fixed an issue with Identity Assertion nodes failing if there are more than one in a journey.

#### Removed

* Modules and chains (AME-30762)

  The legacy PingAM authentication mechanism using modules and chains is enabled by default in Advanced Identity Cloud but has never been supported. Modules and chains remain enabled but have been removed from the Advanced Identity Cloud admin console.

  Modules and chains will be removed entirely in the near future. If you're using them for authentication, you must migrate to nodes and journeys as soon as possible.

  Advanced Identity Cloud provides default journeys that replace the corresponding *default* modules and chains. Any default authentication processes that relied on modules and chains are unaffected by their removal.

## July 2025

### 16 Jul 2025

**Version 18076.4**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 08 Jul 2025

**Version 18076.3**

#### Enhancements

* AME-31379: Setting the new ESV `esv-oauth2-provider-request-object-processing-enforced` to `true` now lets admins enforce which validation rules are applied when processing OAuth 2.0 request objects.

* FRAAS-25437: Tenant administrators with the `tenant-auditor` role can now use federated access to authenticate to Advanced Identity Cloud.

* IAM-3441: Added pagination to all list views.

* IAM-7265: You can now right-click a node in the journey editor to access a context menu.

* IAM-7266: Added an action bar to the journey editor that lets you deselect or delete currently selected nodes.

* IAM-7580: Pages now span the full width of the screen, improving navigation and usability.

* IAM-8260: Advanced Identity Cloud now supports multiple WS-Fed\[[7](#_footnotedef_7 "View footnote.")] applications.

* IAM-8640: The **Release Notes** link in **Tenant Settings** now opens the release notes for the tenant's specific version.

* IAM-8714\[[2](#_footnotedef_2 "View footnote.")]: You can now configure columns in the Identity Governance access review page.

* OPENIDM-21206: Usernames and application names must now be unique, as enforced by the datastore.

#### Fixes

* IAM-7413: The reCAPTCHA Enterprise node is now fully supported.

* IAM-8489: Fixed an issue with the display of application logos in the hosted account pages.

* IAM-8770: Fixed an issue with the calendar icon position in date fields.

* IAM-8773: Fixed an issue where key actions such as realm login were blocked in older tenants with an unmodified original theme.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The impact of the fix for IAM-8773 is that unmodified original themes in older tenants have been purposefully updated to add any missing theme properties that are present on the latest themes. This has been done to make them compatible with recent efficiency improvements to themes in the hosted account pages, but without changing their appearance.The missing properties will appear in your promotion reports, but this is expected and does not require you to take any action. |

#### Related releases

|   |                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This section contains information about releases of other Ping Identity products that are often deployed as part of an Advanced Identity Cloud implementation. To take advantage of these updates, you must manually upgrade your RCS and PingGateway implementations. |

* The RCS 1.5.20.30 release is now available to [download](https://backstage.pingidentity.com/downloads/browse/identity-cloud/all/productId:idm-connector-servers/minorVersion:1.5/version:1.5.20.30/language:java). Learn more in [ICF release notes](https://docs.pingidentity.com/openicf/connector-release-notes/preface.html).

* The PingGateway 2025.6.1 release is now available to [download](https://backstage.forgerock.com/downloads/browse/identity-cloud/all/productId:ig/minorVersion:2025.6/version:2025.6.1/releaseType:full). Learn more in [PingGateway 2025.6.1](https://docs.pingidentity.com/pinggateway/release-notes/whats-new.html#pinggateway_2025_6_1).

### 03 Jul 2025

**Version 17889.11**

#### Fixes

* IAM-8314\[[3](#_footnotedef_3 "View footnote.")]: Fixed an issue where setting ESVs in connector or provisioner configuration stops the Advanced Identity Cloud admin console from being able to update connectors or run a liveSync operation.

## June 2025

### 29 Jun 2025

**Version 17889.10**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 24 Jun 2025

**Version 17889.7**

#### Key features

* Tenant auditors (IAM-8086)

  Advanced Identity Cloud now lets you invite tenant auditors to access the Advanced Identity Cloud admin console. Tenant auditors can view settings, configuration, and data but cannot modify them.

  Learn more in [Tenant administrator groups](../tenants/tenant-administrator-settings.html#tenant-administrator-groups).

#### Enhancements

* FRAAS-25155: Increased log batching size to avoid truncation of large JSON log entries.

* ANALYTICS-868: The **Tenant Admin Activity** report has been changed to the **Tenant Admin Initiated Entity Type Changes** report. The new report provides more detailed and business-friendly insights into changes made by tenant administrators:

  * Field names added, deleted, or modified.

  * Before and after values of changed attributes (if applicable).

  * Business-friendly entity name and entity type changes to custom attributes and custom objects.

  Learn more in [Tenant admin initiated entity type changes report](../reports/administration/analytic-reports.html#tenant-admin-initiated-entity-type-changes-report).

* IAM-8405: You can now duplicate out-of-the-box reports.

* IAM-8591: Dynamic sorting for report results. You can now sort report results directly in the Advanced Identity Cloud admin console after running a report.

#### Fixes

* FRAAS-25142: Fixed a memory issue in the ESV service.

* FRAAS-25434: Fix issue causing source to sometimes be defined as `unknown` in `/monitoring/logs/*` endpoints.

* FRAAS-25226: Allow a higher threshold for large JSON log entries before splitting them into smaller plaintext log entries.

#### Deprecations

* FRAAS-23329: Access to ESV REST API endpoints using the fr:idm:\* scope is now deprecated.

* FRAAS-23330: Access to ESV REST API endpoints using resource version 1.0 is now deprecated.

* FRAAS-25269: The IDC.CLI OAuth 2.0 client is now deprecated in existing tenants and no longer provisioned in new tenants.

Learn more in [Deprecation notices](../product-information/deprecation-notices.html).

### 17 Jun 2025

**Version 17713.10**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 16 Jun 2025

**Version 17713.9**

#### Fixes

FRAAS-25514: Addressed a security issue.

### 12 Jun 2025

**Version 17713.8**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

### 10 Jun 2025

**Version 17713.5**

#### Key features

* Akamai Account Protector node (TNTP-227)\[[5](#_footnotedef_5 "View footnote.")]

  Use the Akamai Account Protector node to inject the Akamai risk score into your authentication journey. When the Akamai Account Protector feature is enabled for your application, the Akamai Edge service provides the risk score in an HTTP header, which is consumed by the Akamai Account Protector node.

  Learn more in [Akamai Account Protector node](rapid-channel/akamai-acc-protect-node.html).

#### Enhancements

* FRAAS-25205: Consolidated `End User UI`, `Login UI`, `Administrator Registration UI`, and `Administrator UI` status page components into a single `Administrator UI` component as they were all reporting the same service.

* IAM-2453\[[5](#_footnotedef_5 "View footnote.")]: Hosted pages themes now show the loading spinner until they are fully loaded.

* IAM-4769\[[5](#_footnotedef_5 "View footnote.")]: Hosted journey pages now fall back to the default theme if a journey is configured with a deleted theme.

* IAM-6781\[[5](#_footnotedef_5 "View footnote.")]: Password policy hints now show all policy conditions when creating a new user identity in the Advanced Identity Cloud admin console.

* IAM-7615\[[5](#_footnotedef_5 "View footnote.")]: The Certificate Collector node now validates the value set in the **HTTP Header Name for Client Certificate** field based on the value selected in the **Certificate Choice Method** field.

* IAM-8358\[[5](#_footnotedef_5 "View footnote.")]\[[2](#_footnotedef_2 "View footnote.")]: Hosted account pages now display a **New User** button in the **Users** list view for delegated administrators.

* OPENIDM-15771: You can now set locales in identity management scripts with the [`_locale` parameter](../tenants/email-send.html#email-send-post-params).

* OPENIDM-17680: Advanced Identity Cloud now supports enumerations in string and number attributes of its identity schema. To make an attribute an enumeration, add `"enum" : [ "one", "two", "three" ]` to the attribute. Advanced Identity Cloud requires create and update privileges to use one of the enumerated values.

* OPENIDM-19918: You can now choose whether synchronization detects identity array changes using *ordered* or *unordered* comparisons. Set the [`comparison`](../idm-synchronization/chap-implicit-live-sync.html#array-comparison) configuration property in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings. Relationship and virtual property array fields default to unordered comparisons. All other fields default to ordered comparisons.

* OPENIDM-20023: RCS communication with Advanced Identity Cloud can now use stricter authorization. Learn more in [Secure RCS access](../idm-auth/authorization-and-roles.html#secure-openicf-access) and [Migration dependent features](../product-information/migration-dependent-features.html).

#### Fixes

* FRAAS-25256: Fixed an issue that was causing missing data in analytics dashboards.

* IAM-1479\[[5](#_footnotedef_5 "View footnote.")]: Email field validation in the Advanced Identity Cloud admin console now runs only when typing stops or the field is unfocused.

* IAM-7858\[[5](#_footnotedef_5 "View footnote.")]: Hosted account pages now use the access management `maxIdleExpirationTime` value to prompt the **You will be signed out soon** modal.

* IAM-8382\[[5](#_footnotedef_5 "View footnote.")]: Fixed an issue in the bookmark app where the **URL** field validation stopped the **Create Application** button working the first time it was clicked.

* IAM-8383\[[5](#_footnotedef_5 "View footnote.")]: Fixed an issue in the bookmark app where the **URL** field accepted ESV secrets.

* IAM-8398\[[5](#_footnotedef_5 "View footnote.")]: Field labels positioned above a field now remain left aligned when autofill is triggered.

* IAM-8441\[[5](#_footnotedef_5 "View footnote.")]: Fixed a display issue in the Advanced Identity Cloud admin console where connector servers and connector server clusters with long names went off the edge of the screen.

* OPENAM-21783: Improved token management for OAuth 2.0 clients that override the **Use Client-Side Access & Refresh Tokens** setting. The OAuth 2.0 `applications` endpoint now correctly shows all tokens issued to these clients. Additionally, administrators can now successfully revoke any of the tokens issued to these clients.

* OPENDJ-11486\[[5](#_footnotedef_5 "View footnote.")]: Fixed an exception caused by identity management user queries with a filter containing wildcards and specific object classes.

## May 2025

### 27 May 2025

**Version 17584.6**

#### Enhancements

* ANALYTICS-1004\[[4](#_footnotedef_4 "View footnote.")]: Support for custom attributes and relationships in the organization entity for advanced reports.

* OPENAM-23218: Legacy SAML 2.0 IDP attribute mapper scripts now have access to the `httpClient` binding.

* OPENAM-23710: Legacy SAML 2.0 IDP adapter scripts now have access to the `httpClient` binding.

#### Fixes

* OPENIDM-20995: Fixed an issue that prevented error reports during certain operations on groups or users. For example, trying to remove a non-existing attribute or null value now correctly results in an exception message to the client if these operations are not supported by the target system.

### 16 May 2025

**Version N/A**

#### Key features

* Integrate with Microsoft 365 (FRAAS-21607)

  Ping Identity introduces Microsoft 365 integration, a new [add-on capability](../product-information/add-on-capabilities.html) for Advanced Identity Cloud. The new Microsoft 365 application lets you set up SSO using the WS-Federation identity protocol.

  Learn more in [Register an SSO application](../app-management/register-a-custom-application.html#register-SSO-application).

### 13 May 2025

**Version 17436.7**

#### Enhancements

* IAM-987: Added support for [enums](../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to hosted account pages.

* IAM-1116: Added support for [enums](../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to the Advanced Identity Cloud admin console.

* IAM-2103: Added support for [enums](../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to hosted journey pages.

* IAM-6822: Added the ability to manage cookie domains in the Advanced Identity Cloud admin console.

* IAM-7412: Updated the password policy feature in the Advanced Identity Cloud admin console. Added the ability to specify a minimum substring length between 3 - 64 to use when validating passwords against user attribute values. The default is still 5 characters, but can now be reduced to as few as 3 characters to catch shorter string matches.

* IAM-7794\[[2](#_footnotedef_2 "View footnote.")]: Added support for using custom identity objects in the form builder.

* IAM-7919: Improved color contrast ratio of the **Delete Account** button text when focused.

* IAM-7934: Improved color contrast ratio of date fields when focused.

* IAM-7957: Improved color contrast ratio of the **Deselect** button text when focused.

* IAM-7966: Improved color contrast ratio of **In Progress** text.

* IAM-8016\[[2](#_footnotedef_2 "View footnote.")]: Allow form authors to specify a user filter when dynamic enums are selected.

* IAM-8085: Updated the **Add a Parameter** reports modal to use entity attributes for input.

#### Fixes

* FRAAS-15518: Fixed issue that prevented localization of **Session timed out** message in certain locales.

* FRAAS-24449: Enhanced the reliability of metrics collection under high-load conditions.

* FRAAS-24990: Fixed an issue where requests to the `/monitoring/logs` and `/monitoring/logs/tail` endpoints timed out after 15 seconds rather than the expected 60 seconds.

* IAM-5834: Fixed a double-encoding issue in the SAML app that affected IdP-initiated sign on.

* IAM-6796: Jobs are now prevented from being scheduled with frequencies that cause invalid date errors.

* IAM-7855: Fixed a typo in the help text returned when there are no results to display.

* IAM-8237: Corrected floating labels in the date picker in the hosted journey pages.

* IAM-8361: The **Save** button in the **Edit Bookmark** application is now inactive while checking if the ESV exists.

* IAM-8364: Fixed issues in SAML end-to-end scenarios.

* IAM-8378: Fixed an issue that stripped HTML elements from email templates.

* IAM-8403: Fixed border focus location and floating label issues in **Tag** fields.

* IAM-8434: Fixed an issue that prevented duplication of new themes that contain special characters.

### 03 May 2025

**Version 17274.5**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

***

[1](#_footnoteref_1). This release focuses on internal improvements and technical updates to enhance the overall stability, performance, and maintainability of the platform. While there are no direct customer-facing changes, these updates lay the groundwork for future feature releases and improvements.[2](#_footnoteref_2). This change applies to a feature only available in PingOne Identity Governance, which is an [add-on capability](../product-information/add-on-capabilities.html) and must be purchased separately.[3](#_footnoteref_3). This issue is a hotfix so has been expedited across both release channels, reaching the regular channel before, or at the same time as, the rapid channel.[4](#_footnoteref_4). This change applies to a feature only available in Advanced Reporting, which is an [add-on capability](../product-information/add-on-capabilities.html) and must be purchased separately.[5](#_footnoteref_5). This issue was inadvertently excluded from the rapid changelog.[6](#_footnoteref_6). Requires WS-Federation/WS-Trust, which is an [add-on capability](../product-information/add-on-capabilities.html).[7](#_footnoteref_7). [WS-Federation/WS-Trust](../app-management/register-a-custom-application.html#sso-microsoft-365) is an [add-on capability](../product-information/add-on-capabilities.html).[8](#_footnoteref_8). This issue was inadvertently excluded from this regular changelog entry when it was initially published.[9](#_footnoteref_9). Proxy Connect is an [add-on capability](../product-information/add-on-capabilities.html).[10](#_footnoteref_10). A [sandbox environment](../tenants/environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[11](#_footnoteref_11). IGA is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Regular channel changelog
description: Version 17106.8
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17106.8
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17106.8.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  15_apr_2025: 15 Apr 2025
  enhancements: Enhancements
  fixes: Fixes
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 15 Apr 2025

**Version 17106.8**

### Enhancements

* ANALYTICS-846: You can now select the attribute type and value for report entity attributes.

* ANALYTICS-983\[[1](#_footnotedef_1 "View footnote.")]: You can now use regular expression operators in Advanced Reporting.

* OPENAM-23718: Added additional Java classes to the SAML 2.0 SP adapter scripting allowlist.

### Fixes

* FRAAS-24631: Fixed a promotions issue where ESVs mapped to secret labels aren't identified as available in the upper environment.

* FRAAS-24648: Fixed an issue with loading ESVs with values containing leading blank spaces.

* IAM-7202: In the custom application modal, the native apps link now correctly points to the SDKs documentation.

***

[1](#_footnoteref_1). This change applies to a feature only available in Advanced Reporting, which is an [add-on capability](../../product-information/add-on-capabilities.html) and must be purchased separately.

---

---
title: Regular channel changelog
description: Version 17274.2
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17274.2
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17274.2.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  30_apr_2025: 30 Apr 2025
  enhancements: Enhancements
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 30 Apr 2025

**Version 17274.2**

### Enhancements

* AME-31141: Multiple Java libraries added to SAML SP Adapter scripting allowlist.

* OPENDJ-11175: The password validation mechanism has been enhanced to include checks for attribute values shorter than the `min-substring-length` (the default is 5).

  For example, if the password contains `Bob` for a user named Bob, the password is rejected, even if `min-substring-length` is set to 5.

---

---
title: Regular channel changelog
description: Version 17274.5
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17274.5
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17274.5.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  03_may_2025: 03 May 2025
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 03 May 2025

**Version 17274.5**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

***

[1](#_footnoteref_1). This release focuses on internal improvements and technical updates to enhance the overall stability, performance, and maintainability of the platform. While there are no direct customer-facing changes, these updates lay the groundwork for future feature releases and improvements.

---

---
title: Regular channel changelog
description: Version 17436.7
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17436.7
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17436.7.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  13_may_2025: 13 May 2025
  enhancements: Enhancements
  fixes: Fixes
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 13 May 2025

**Version 17436.7**

### Enhancements

* IAM-987: Added support for [enums](../../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to hosted account pages.

* IAM-1116: Added support for [enums](../../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to the Advanced Identity Cloud admin console.

* IAM-2103: Added support for [enums](../../idm-objects/creating-modifying-managed-objects.html#enum-managed-object) (drop-down lists) to hosted journey pages.

* IAM-6822: Added the ability to manage cookie domains in the Advanced Identity Cloud admin console.

* IAM-7412: Updated the password policy feature in the Advanced Identity Cloud admin console. Added the ability to specify a minimum substring length between 3 - 64 to use when validating passwords against user attribute values. The default is still 5 characters, but can now be reduced to as few as 3 characters to catch shorter string matches.

* IAM-7794\[[1](#_footnotedef_1 "View footnote.")]: Added support for using custom identity objects in the form builder.

* IAM-7919: Improved color contrast ratio of the **Delete Account** button text when focused.

* IAM-7934: Improved color contrast ratio of date fields when focused.

* IAM-7957: Improved color contrast ratio of the **Deselect** button text when focused.

* IAM-7966: Improved color contrast ratio of **In Progress** text.

* IAM-8016\[[1](#_footnotedef_1 "View footnote.")]: Allow form authors to specify a user filter when dynamic enums are selected.

* IAM-8085: Updated the **Add a Parameter** reports modal to use entity attributes for input.

### Fixes

* FRAAS-15518: Fixed issue that prevented localization of **Session timed out** message in certain locales.

* FRAAS-24449: Enhanced the reliability of metrics collection under high-load conditions.

* FRAAS-24990: Fixed an issue where requests to the `/monitoring/logs` and `/monitoring/logs/tail` endpoints timed out after 15 seconds rather than the expected 60 seconds.

* IAM-5834: Fixed a double-encoding issue in the SAML app that affected IdP-initiated sign on.

* IAM-6796: Jobs are now prevented from being scheduled with frequencies that cause invalid date errors.

* IAM-7855: Fixed a typo in the help text returned when there are no results to display.

* IAM-8237: Corrected floating labels in the date picker in the hosted journey pages.

* IAM-8361: The **Save** button in the **Edit Bookmark** application is now inactive while checking if the ESV exists.

* IAM-8364: Fixed issues in SAML end-to-end scenarios.

* IAM-8378: Fixed an issue that stripped HTML elements from email templates.

* IAM-8403: Fixed border focus location and floating label issues in **Tag** fields.

* IAM-8434: Fixed an issue that prevented duplication of new themes that contain special characters.

***

[1](#_footnoteref_1). This change applies to a feature only available in PingOne Identity Governance, which is an [add-on capability](../../product-information/add-on-capabilities.html) and must be purchased separately.

---

---
title: Regular channel changelog
description: Version 17584.6
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17584.6
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17584.6.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  27_may_2025: 27 May 2025
  enhancements: Enhancements
  fixes: Fixes
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 27 May 2025

**Version 17584.6**

### Enhancements

* ANALYTICS-1004\[[1](#_footnotedef_1 "View footnote.")]: Support for custom attributes and relationships in the organization entity for advanced reports.

* OPENAM-23218: Legacy SAML 2.0 IDP attribute mapper scripts now have access to the `httpClient` binding.

* OPENAM-23710: Legacy SAML 2.0 IDP adapter scripts now have access to the `httpClient` binding.

### Fixes

* OPENIDM-20995: Fixed an issue that prevented error reports during certain operations on groups or users. For example, trying to remove a non-existing attribute or null value now correctly results in an exception message to the client if these operations are not supported by the target system.

***

[1](#_footnoteref_1). This change applies to a feature only available in Advanced Reporting, which is an [add-on capability](../../product-information/add-on-capabilities.html) and must be purchased separately.

---

---
title: Regular channel changelog
description: Version 17713.10
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17713.10
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17713.10.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  17_jun_2025: 17 Jun 2025
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 17 Jun 2025

**Version 17713.10**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

***

[1](#_footnoteref_1). This release focuses on internal improvements and technical updates to enhance the overall stability, performance, and maintainability of the platform. While there are no direct customer-facing changes, these updates lay the groundwork for future feature releases and improvements.

---

---
title: Regular channel changelog
description: Version 17713.5
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17713.5
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17713.5.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  10_jun_2025: 10 Jun 2025
  key_features: Key features
  enhancements: Enhancements
  fixes: Fixes
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 10 Jun 2025

**Version 17713.5**

### Key features

* Akamai Account Protector node (TNTP-227)\[[1](#_footnotedef_1 "View footnote.")]

  Use the Akamai Account Protector node to inject the Akamai risk score into your authentication journey. When the Akamai Account Protector feature is enabled for your application, the Akamai Edge service provides the risk score in an HTTP header, which is consumed by the Akamai Account Protector node.

  Learn more in [Akamai Account Protector node](../rapid-channel/akamai-acc-protect-node.html).

### Enhancements

* FRAAS-25205: Consolidated `End User UI`, `Login UI`, `Administrator Registration UI`, and `Administrator UI` status page components into a single `Administrator UI` component as they were all reporting the same service.

* IAM-2453\[[1](#_footnotedef_1 "View footnote.")]: Hosted pages themes now show the loading spinner until they are fully loaded.

* IAM-4769\[[1](#_footnotedef_1 "View footnote.")]: Hosted journey pages now fall back to the default theme if a journey is configured with a deleted theme.

* IAM-6781\[[1](#_footnotedef_1 "View footnote.")]: Password policy hints now show all policy conditions when creating a new user identity in the Advanced Identity Cloud admin console.

* IAM-7615\[[1](#_footnotedef_1 "View footnote.")]: The Certificate Collector node now validates the value set in the **HTTP Header Name for Client Certificate** field based on the value selected in the **Certificate Choice Method** field.

* IAM-8358\[[1](#_footnotedef_1 "View footnote.")]\[[2](#_footnotedef_2 "View footnote.")]: Hosted account pages now display a **New User** button in the **Users** list view for delegated administrators.

* OPENIDM-15771: You can now set locales in identity management scripts with the [`_locale` parameter](../../tenants/email-send.html#email-send-post-params).

* OPENIDM-17680: Advanced Identity Cloud now supports enumerations in string and number attributes of its identity schema. To make an attribute an enumeration, add `"enum" : [ "one", "two", "three" ]` to the attribute. Advanced Identity Cloud requires create and update privileges to use one of the enumerated values.

* OPENIDM-19918: You can now choose whether synchronization detects identity array changes using *ordered* or *unordered* comparisons. Set the [`comparison`](../../idm-synchronization/chap-implicit-live-sync.html#array-comparison) configuration property in the schema. Unordered JSON array comparison ignores the order of elements and can negate the need for certain custom scripts within mappings. Relationship and virtual property array fields default to unordered comparisons. All other fields default to ordered comparisons.

* OPENIDM-20023: RCS communication with Advanced Identity Cloud can now use stricter authorization. Learn more in [Secure RCS access](../../idm-auth/authorization-and-roles.html#secure-openicf-access) and [Migration dependent features](../../product-information/migration-dependent-features.html).

### Fixes

* FRAAS-25256: Fixed an issue that was causing missing data in analytics dashboards.

* IAM-1479\[[1](#_footnotedef_1 "View footnote.")]: Email field validation in the Advanced Identity Cloud admin console now runs only when typing stops or the field is unfocused.

* IAM-7858\[[1](#_footnotedef_1 "View footnote.")]: Hosted account pages now use the access management `maxIdleExpirationTime` value to prompt the **You will be signed out soon** modal.

* IAM-8382\[[1](#_footnotedef_1 "View footnote.")]: Fixed an issue in the bookmark app where the **URL** field validation stopped the **Create Application** button working the first time it was clicked.

* IAM-8383\[[1](#_footnotedef_1 "View footnote.")]: Fixed an issue in the bookmark app where the **URL** field accepted ESV secrets.

* IAM-8398\[[1](#_footnotedef_1 "View footnote.")]: Field labels positioned above a field now remain left aligned when autofill is triggered.

* IAM-8441\[[1](#_footnotedef_1 "View footnote.")]: Fixed a display issue in the Advanced Identity Cloud admin console where connector servers and connector server clusters with long names went off the edge of the screen.

* OPENAM-21783: Improved token management for OAuth 2.0 clients that override the **Use Client-Side Access & Refresh Tokens** setting. The OAuth 2.0 `applications` endpoint now correctly shows all tokens issued to these clients. Additionally, administrators can now successfully revoke any of the tokens issued to these clients.

* OPENDJ-11486\[[1](#_footnotedef_1 "View footnote.")]: Fixed an exception caused by identity management user queries with a filter containing wildcards and specific object classes.

***

[1](#_footnoteref_1). This issue was inadvertently excluded from the rapid changelog.[2](#_footnoteref_2). This change applies to a feature only available in PingOne Identity Governance, which is an [add-on capability](../../product-information/add-on-capabilities.html) and must be purchased separately.

---

---
title: Regular channel changelog
description: Version 17713.8
component: pingoneaic
page_id: pingoneaic:release-notes:regular-channel/version-17713.8
canonical_url: https://docs.pingidentity.com/pingoneaic/release-notes/regular-channel/version-17713.8.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  12_jun_2025: 12 Jun 2025
---

# Regular channel changelog

|   |                                                                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This is a changelog entry for an individual version. You can review the changelog for all versions in [Regular channel changelog](../regular-channel-changelog.html). |

## 12 Jun 2025

**Version 17713.8**

No customer-facing features, enhancements, or fixes released.\[[1](#_footnotedef_1 "View footnote.")]

***

[1](#_footnoteref_1). This release focuses on internal improvements and technical updates to enhance the overall stability, performance, and maintainability of the platform. While there are no direct customer-facing changes, these updates lay the groundwork for future feature releases and improvements.