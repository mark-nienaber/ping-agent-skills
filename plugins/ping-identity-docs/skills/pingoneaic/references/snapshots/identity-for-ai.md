---
title: Configure a DCR onboarding flow
description: Use Dynamic Client Registration to automatically onboard OAuth 2.0 clients as AI agent identities in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:identity-for-ai:ai-agent-identities-configure-dcr-onboarding-flow
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities-configure-dcr-onboarding-flow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/ai-agents-configure-dcr-onboarding-flow.adoc"]
section_ids:
  configure-the-oauth-2-abbr-provider-service-dcr: "Task 1: Configure the OAuth 2.0 provider service"
  create-and-register-a-dcr-script: "Task 2: Create and register a DCR script"
  discover-the-ai-agent-dcr-endpoint: "Task 3: Discover the AI agent DCR endpoint"
  register-and-configure-a-dynamic-client: "Task 4: Register and configure a dynamic client"
  get-a-dynamic-client-access-token: "Task 5: Get a dynamic client access token"
---

# Configure a DCR onboarding flow

To streamline the onboarding of OAuth 2.0 clients, Advanced Identity Cloud supports Dynamic Client Registration (DCR), which allows for the automated creation and configuration of dynamic clients without manual intervention.

In addition to the standard DCR endpoint (`/register`), Advanced Identity Cloud provides an AI agent-specific DCR endpoint (`/aiagent/register`) for onboarding AI agent identities as dynamic clients, enabling your AI-driven solutions to programmatically register and obtain credentials for secure access to applications on behalf of end users. Learn more in [Discover the AI agent DCR endpoint](#discover-the-ai-agent-dcr-endpoint).

What is Dynamic Client Registration (DCR)?

Dynamic Client Registration (DCR) is an OAuth 2.0 extension that allows *dynamic clients* to be programmatically registered with an authorization server at runtime without manual administrative intervention. Instead of a static setup, dynamic clients send their own metadata (including names and authorized redirect URLs) directly to a dedicated registration endpoint to obtain unique credentials. This process is essential for scaling high-velocity environments where numerous individual client instances require distinct identities for secure tracking and lifecycle management.

DCR is a key component of Model Context Protocol (MCP) authorization, where MCP clients such as AI assistants and IDEs need to interact securely with MCP servers that host data and tools. DCR allows these MCP clients to be dynamically onboarded with appropriate access permissions and security settings, enabling seamless and secure interactions in AI-driven solutions.

## Task 1: Configure the OAuth 2.0 provider service

Configure the OAuth 2.0 provider service to support the grant types needed for the DCR onboarding flow:

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Services.

2. Click the OAuth2 Provider service, then click the Advanced tab:

   1. In the Grant Types field, select the Client Credentials grant type, if it isn't already selected.

   2. In the Client Registration Scope Allowlist field, select the scopes that AI-driven solutions can request when they use the DCR onboarding flow to onboard AI agent identities.

3. Click the Client Dynamic Registration tab:

   * Select the Allow Open Dynamic Client Registration checkbox, if it isn't already selected.

4. Click Save Changes.

## Task 2: Create and register a DCR script

Create a DCR script to configure the settings for AI agent identities onboarded as dynamic clients.

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Scripts.

2. Click [icon: add, set=material, size=inline] New Script.

3. In the New Script page:

   1. Enter a Name for the script, such as `AI Agent Dynamic Client Registration Script`.

   2. In the Script Type drop-down list, select `OAuth2 Dynamic Client Registration`.

   3. Click Create.

4. In the script editor:

   1. (Optional) Enter a Description for the script, such as `Script to configure AI agent identity access settings during dynamic client registration`.

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

## Task 3: Discover the AI agent DCR endpoint

The OIDC discovery endpoint (`/.well-known/openid-configuration`) always advertises the standard DCR endpoint (`/register`) in its `registration_endpoint` value. It doesn't advertise the AI agent-specific DCR endpoint, even when the AI agents feature is enabled in the realm.

To discover the AI agent-specific DCR endpoint, call the OAuth 2.0 authorization server metadata endpoint ([RFC 8414](https://datatracker.ietf.org/doc/html/rfc8414)) with the realm and `/aiagent` appended to the well-known path:

```shell
$ curl 'https://<tenant-env-fqdn>/.well-known/oauth-authorization-server/alpha/aiagent' \(1)
```

> **Collapse: Show request guidance**
>
> |       |                                                                                                                                         |
> | ----- | --------------------------------------------------------------------------------------------------------------------------------------- |
> | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment, and `alpha` with the realm that contains your AI agent identities. |

```json
{
    ...
    "registration_endpoint": "https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha/aiagent/register" (1)
}
```

> **Collapse: Show response guidance**
>
> |       |                                                                                                                                                                                                                                                          |
> | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **1** | The `registration_endpoint` value is the AI agent DCR endpoint for the realm. Use this endpoint to register AI agent identities as dynamic clients, as described in [Register and configure a dynamic client](#register-and-configure-a-dynamic-client). |

**Example AI agent DCR endpoints**

| Metadata endpoint URL                                                            | Example `registration_endpoint` value                                                                                                    |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| `https://<tenant-env-fqdn>/.well-known/oauth-authorization-server/alpha/aiagent` | `https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha/aiagent/register`                                                      |
| `https://<tenant-env-fqdn>/.well-known/oauth-authorization-server/bravo/aiagent` | `https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/bravo/aiagent/register`                                                      |
| `https://<tenant-env-fqdn>/.well-known/oauth-authorization-server`               | `https://<tenant-env-fqdn>:443/am/oauth2/realms/root/realms/alpha/aiagent/register`(A URL without a realm defaults to the `alpha` realm) |

## Task 4: Register and configure a dynamic client

1. Use the AI agent-specific DCR endpoint (`/aiagent/register`) to register a dynamic client.

   |   |                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The `/aiagent/register` endpoint doesn't support setting the client ID in the request payload. The `client_id` is automatically generated by Advanced Identity Cloud for AI agent identities registered as dynamic clients. |

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

2. (Optional) Configure an application privilege for the dynamic client. Learn more in [Create application privileges](ai-agent-identities-ui.html#create-application-privileges).

## Task 5: Get a dynamic client access token

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
page_id: pingoneaic:identity-for-ai:ai-agent-identities-configure-on-behalf-of-authentication-flow
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities-configure-on-behalf-of-authentication-flow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/ai-agents-configure-on-behalf-of-authentication-flow.adoc"]
section_ids:
  configure-the-oauth-2-abbr-provider-service: "Task 1: Configure the OAuth 2.0 provider service"
  create-and-configure-a-custom-oauth2-application: "Task 2: Create and configure a custom OAuth 2.0 application"
  create-a-custom-oauth2-application: "Task 2.1: Create a custom OAuth 2.0 application"
  configure-a-custom-oauth2-application: "Task 2.2: Configure a custom OAuth 2.0 application"
  create-and-configure-an-ai-agent-identity: "Task 3: Create and configure an AI agent identity"
  create-an-ai-agent-identity: "Task 3.1: Create an AI agent identity"
  configure-an-ai-agent-identity: "Task 3.2: Configure an AI agent"
  test-the-authentication-flow: "Task 4: Test the authentication flow"
  get-an-end-user-access-token: "Task 4.1: Get an end user access token"
  get-an-ai-agent-identity-access-token: "Task 4.2: Get an AI agent identity access token"
---

# Configure an "on behalf of" authentication flow for AI agents

The "on behalf of" flow allows an AI agent to perform actions on behalf of an end user, which is useful for securing the actions of [digital assistants](https://developer.pingidentity.com/identity-for-ai/glossary/idai-glossary.html#digital-assistant).

The following instructions use an example scenario of a digital assistant AI agent that performs actions on behalf of end users in a web application. The AI agent needs to access to the web application to perform actions such as retrieving data, creating or updating records, and performing administrative tasks.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For ease of understanding, this example uses a simple [Resource owner password credentials grant](../am-oauth2/oauth2-ropc-grant.html) (ROPC) to obtain an access token for the end user, which is then exchanged for a new access token that represents the AI agent acting on behalf of the end user. In production environments, use a more secure flow, such as the [Authorization code grant](../am-oauth2/oauth2-authz-grant.html). |

## Task 1: Configure the OAuth 2.0 provider service

Configure the OAuth 2.0 provider service to support the grant types needed for the "on behalf of" authentication flow:

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Services.

2. Click the OAuth2 Provider service, then click the Advanced tab:

   * In the Grant Types field, select the Resource Owner Password Credentials and Token Exchange grant types, if they aren't already selected.

3. Click Save Changes.

## Task 2: Create and configure a custom OAuth 2.0 application

Create and configure a custom OAuth 2.0 application with a confidential client type to act as a resource that the AI agent identity can access on behalf of end users.

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

## Task 3: Create and configure an AI agent identity

Create and configure an AI agent identity that can access the custom OAuth 2.0 application on behalf of end users using the token exchange grant type.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Tasks 3.1 and 3.2 use the admin console to create and configure an AI agent identity. To create the same identity in the API, refer to [Create an AI agent identity](ai-agent-identities-api.html#create-an-ai-agent-identity) and [Create an AI agent identity privilege](ai-agent-identities-api.html#create-an-ai-agent-identity-privilege) and use payloads similar to the following:> **Collapse: Show payload examples**
>
> * Payload to create AI agent identity:
>
>   ```json
>   {
>     "aiAgentIdentityAttributes": {
>       "inherited": false,
>       "value": {
>         "name": "Digital Assistant Web App",
>         "oauth2ClientId": "digital-assistant-ai-agent"
>       }
>     },
>     "coreOAuth2ClientConfig": {
>       "status":     { "inherited": false, "value": "Active" },
>       "clientType": { "inherited": false, "value": "Confidential" }
>     },
>     "advancedOAuth2ClientConfig": {
>       "grantTypes":              { "inherited": false, "value": ["urn:ietf:params:oauth:grant-type:token-exchange"] },
>       "tokenEndpointAuthMethod": { "inherited": false, "value": "client_secret_post" }
>     },
>     "overrideOAuth2ClientConfig": {
>       "providerOverridesEnabled": true,
>       "statelessTokensEnabled": true,
>       "acceptAudienceParametersInTokenExchangeRequests": true
>     }
>   }
>   ```
>
> * Payload to create AI agent identity privilege (replace the `_ref` values in the payload with actual managed object references):
>
>   ```json
>   {
>     "agent": {
>       "_ref":           "managed/alpha_aiagent/19301b4f-27ae-43fd-adc3-04389fd97f42",
>       "_refProperties": {}
>     },
>     "resource": {
>       "_ref":           "managed/alpha_application/7dd5b63f-274e-4984-8306-824d1c51ec35",
>       "_refProperties": {}
>     },
>     "subjects": [{
>       "_ref":           "managed/alpha_user/fc87eea4-3c96-49d1-9620-bf23aca9bd97",
>       "_refProperties": {}
>     }],
>     "subjectGroups": [],
>     "permissions": [{
>       "type":   "scopes",
>       "values": ["read-data"]
>     }]
>   }
>   ``` |

### Task 3.1: Create an AI agent identity

1. Follow the instructions in [Create an AI agent identity](ai-agent-identities-ui.html#create-an-ai-agent-identity). An example name for the identity is `Digital Assistant AI Agent`, and an example client ID is `digital-assistant-ai-agent`.

2. Follow the instructions in [Configure an AI agent](#configure-an-ai-agent-identity) to configure the identity you created.

### Task 3.2: Configure an AI agent

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the identity you want to configure, then click it.

3. Click the Access tab to configure the identity's OAuth 2.0 client:

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

   4. In the Subjects field, select users that the AI agent identity will act on behalf of or in the Subject Groups field, select groups of users that the identity will act on behalf of.

   5. In the Permissions field, choose one of the following approaches:

      * To limit the scopes the identity can request, select specific scopes. For example, `read-data`. This approach is recommended for "on behalf of" operations where the identity only needs access to a limited set of permissions.

      * To allow the identity to request any or all of the scopes that are assigned to the custom OAuth 2.0 application, select all scopes in this field or leave it empty. This approach might be suitable for "human-in-the-loop" workflows, where end users are required to explicitly approve high-risk or sensitive operations.

      You can also enter custom scope values that aren't in the drop-down list by typing them into the field.

   6. Click Save.

## Task 4: Test the authentication flow

Run a series of commands to get an access token for an end user and then exchange it for a new access token that represents an AI agent identity acting on behalf of the end user.

### Task 4.1: Get an end user access token

1. [Create a user account](../identities/manage-identities.html#create-a-user-profile) for the end user that the AI agent identity will act on behalf of, if one doesn't already exist.

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
   > | **3** | Replace \<end-user-username> with the username of the end user that the AI agent identity will act on behalf of. For example, `barbara.jensen`.         |
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

### Task 4.2: Get an AI agent identity access token

1. Use the Token Exchange grant type to exchange the end user's access token for a new access token that the AI agent identity can use to access the custom OAuth 2.0 application on behalf of the end user:

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
   > |       |                                                                                                                                                                                                                                                                                     |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                                |
   > | **2** | The `grant_type` for this request is `urn:ietf:params:oauth:grant-type:token-exchange`, which represents the Token Exchange grant type.                                                                                                                                             |
   > | **3** | Replace \<end-user-access-token> with the end user's access token.                                                                                                                                                                                                                  |
   > | **4** | Replace \<ai-agent-client-id> with the client ID of the AI agent identity you created in task 3. For example, `digital-assistant-ai-agent`.                                                                                                                                         |
   > | **5** | Replace \<ai-agent-client-secret> with the client secret of the AI agent identity.                                                                                                                                                                                                  |
   > | **6** | Replace \<oauth2-app-client-id> with the client ID of the custom OAuth 2.0 application. For example, `digital-assistant-web-app`. Setting this as the `audience` indicates that the AI agent identity intends to access the custom OAuth 2.0 application on behalf of the end user. |
   > | **7** | Replace \<ai-agent-scopes> with some or all of the scopes that you assigned to the AI agent identity in task 3.2, step 5e. For example, `read-data`.                                                                                                                                |

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
   > |       |                                                                                                                                                        |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | The `access_token` value in the response is can be used by the AI agent identity to access the custom OAuth 2.0 application on behalf of the end user. |

2. Introspect the AI agent identity's access token to verify the claims contain expected values:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/tokeninfo' \(1)
   --data-urlencode 'access_token=<ai-agent-access-token>'(2)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                     |
   > | ----- | ----------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                |
   > | **2** | Replace \<ai-agent-access-token> with the access token from the response in step 1. |

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
   > |       |                                                                                                                                                                                                                          |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | The `sub` claim contains the end user's UUID, which indicates that the token represents the end user.                                                                                                                    |
   > | **2** | The `aud` claim contains the client ID of the AI agent identity and the custom OAuth 2.0 application, which indicates that the intended audience of this access token is both the AI agent identity and the application. |
   > | **3** | The `act` claim contains a `sub` claim with the AI agent identity's client ID, which indicates that the AI agent identity is acting on behalf of the end user.                                                           |
   > | **4** | The `scope` claim contains the scopes that the AI agent identity can access.                                                                                                                                             |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `aud` claim in this example includes both the AI agent identity's client ID and the application's client ID because this guide configures Accept Audience parameter in token exchange requests on the OAuth 2.0 provider. Without that setting, the default behavior is for `aud` to contain only the AI agent identity's own `client_id`. You can use the presence of the application client ID in `aud` as a signal that the AI agent identity authenticated on behalf of a user against that specific application. |

---

---
title: Configure an autonomous AI agent flow
description: Configure autonomous AI agents to act independently without end user presence for automated pipelines and background tasks
component: pingoneaic
page_id: pingoneaic:identity-for-ai:ai-agent-identities-configure-autonomous-agent-flow
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities-configure-autonomous-agent-flow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/ai-agents-configure-autonomous-agent-flow.adoc"]
section_ids:
  configure-the-oauth-2-abbr-provider-service: "Task 1: Configure the OAuth 2.0 provider service"
  create-and-configure-a-custom-oauth2-application: "Task 2: Create and configure a custom OAuth 2.0 application"
  create-a-custom-oauth2-application: "Task 2.1: Create a custom OAuth 2.0 application"
  configure-a-custom-oauth2-application: "Task 2.2: Configure a custom OAuth 2.0 application"
  create-and-configure-an-ai-agent-identity: "Task 3: Create and configure an AI agent identity"
  create-an-ai-agent-identity: "Task 3.1: Create an AI agent identity"
  configure-an-ai-agent-identity: "Task 3.2: Configure an AI agent identity"
  test-the-authentication-flow: "Task 4: Test the authentication flow"
  get-an-ai-agent-identity-access-token: "Task 4.1: Get an AI agent identity access token"
  exchange-the-ai-agent-identity-token-for-application-access: "Task 4.2: Exchange the AI agent identity token for application access"
---

# Configure an autonomous AI agent flow

The autonomous AI agent flow lets an AI agent act independently, without requiring an end user to be present, which is useful for securing the actions of [digital workers](https://developer.pingidentity.com/identity-for-ai/glossary/idai-glossary.html#digital-worker). The AI agent obtains its own access token using the Client Credentials grant type and then exchanges it for a scoped token that it can use to access a specific application. This is useful for automated pipelines, background tasks, and other scenarios where an AI agent acts on its own behalf rather than on behalf of an end user.

The following instructions use an example scenario of an AI agent that analyzes a web server's access logs for bot traffic. The AI agent needs to access the web server's logs API autonomously, to read and search the logs for indicators of bot traffic.

## Task 1: Configure the OAuth 2.0 provider service

Configure the OAuth 2.0 provider service to support the grant types needed for the autonomous agent flow:

1. In the Advanced Identity Cloud admin console, go to Native Consoles > Access Management > Services.

2. Click the OAuth2 Provider service, then click the Advanced tab:

   * In the Grant Types field, select the Client Credentials and Token Exchange grant types, if they aren't already selected.

3. Click Save Changes.

## Task 2: Create and configure a custom OAuth 2.0 application

Create and configure a custom OAuth 2.0 application with a confidential client type to act as a resource that the AI agent identity can access autonomously.

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

## Task 3: Create and configure an AI agent identity

Create and configure an AI agent identity that can autonomously access the custom OAuth 2.0 application.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Tasks 3.1 and 3.2 use the admin console to create and configure an AI agent identity. To create the same AI agent identity in the API, refer to [Create an AI agent identity](ai-agent-identities-api.html#create-an-ai-agent-identity) and [Create an AI agent identity privilege](ai-agent-identities-api.html#create-an-ai-agent-identity-privilege) and use payloads similar to the following:> **Collapse: Show payload examples**
>
> * Payload to create AI agent identity:
>
>   ```json
>   {
>     "aiAgentIdentityAttributes": {
>       "inherited": false,
>       "value": {
>         "name": "Bot Traffic Analyzer Agent",
>         "oauth2ClientId": "bot-traffic-analyzer-agent"
>       }
>     },
>     "coreOAuth2ClientConfig": {
>       "status":     { "inherited": false, "value": "Active" },
>       "clientType": { "inherited": false, "value": "Confidential" }
>     },
>     "advancedOAuth2ClientConfig": {
>       "grantTypes":              { "inherited": false, "value": ["urn:ietf:params:oauth:grant-type:token-exchange"] },
>       "tokenEndpointAuthMethod": { "inherited": false, "value": "client_secret_post" }
>     },
>     "overrideOAuth2ClientConfig": {
>       "providerOverridesEnabled": true,
>       "statelessTokensEnabled": true,
>       "acceptAudienceParametersInTokenExchangeRequests": true
>     }
>   }
>   ```
>
> * Payload to create AI agent identity privilege (replace the `_ref` values in the payload with actual managed object references):
>
>   ```json
>   {
>     "agent": {
>       "_ref":           "managed/alpha_aiagent/2835a79f-aa51-446c-808d-0195b2fec75c",
>       "_refProperties": {}
>     },
>     "resource": {
>       "_ref":           "managed/alpha_application/2d479b8c-1e5a-4170-87bd-de44b468d3a7",
>       "_refProperties": {}
>     },
>     "subjectGroups": [],
>     "permissions": [{
>       "type":   "scopes",
>       "values": ["logs-read", "logs-search"]
>     }]
>   }
>   ``` |

### Task 3.1: Create an AI agent identity

1. Follow the instructions in [Create an AI agent identity](ai-agent-identities-ui.html#create-an-ai-agent-identity). An example name for the identity is `Bot Traffic Analyzer Agent`, and an example client ID is `bot-traffic-analyzer-agent`.

2. Follow the instructions in [Configure an AI agent identity](#configure-an-ai-agent-identity) to configure the identity you created.

### Task 3.2: Configure an AI agent identity

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the AI agent identity you want to configure, then click it.

3. Click the Access tab to configure the agent's OAuth 2.0 client:

   1. Click Show Advanced Settings to display a vertical tab menu. The Core vertical tab is selected by default.

   2. In the Scopes field, enter the scopes the identity needs for basic operations. For example, `monitor-system`.

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

   4. Leave the Subjects and Subject Groups fields empty, because the AI agent identity acts autonomously rather than on behalf of a specific user.

   5. In the Permissions field, choose one of the following approaches:

      * To limit the scopes the identity can request, select specific scopes. For example, `logs-read` and `logs-search`. This approach is recommended when you want to apply least privilege to the identity's access.

      * To allow the identity to request any or all of the scopes assigned to the custom OAuth 2.0 application, select all scopes or leave the field empty.

   6. Click Save.

## Task 4: Test the authentication flow

Run a series of commands to get an access token for the AI agent identity and then exchange it for a scoped token the AI agent identity can use to access the custom OAuth 2.0 application autonomously.

### Task 4.1: Get an AI agent identity access token

1. Get an access token for the identity using the Client Credentials grant type:

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
   > |       |                                                                                                                                             |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                        |
   > | **2** | The `grant_type` for this request is `client_credentials`, which represents the Client Credentials grant type.                              |
   > | **3** | Replace \<ai-agent-client-id> with the client ID of the AI agent identity you created in task 3. For example, `bot-traffic-analyzer-agent`. |
   > | **4** | Replace \<ai-agent-client-secret> with the client secret of the AI agent identity.                                                          |
   > | **5** | Replace \<ai-agent-scopes> with one or more of the scopes you assigned to the AI agent identity. For example, `monitor-system`.             |

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
   > |       |                                                                                   |
   > | ----- | --------------------------------------------------------------------------------- |
   > | **1** | The `access_token` value in the response is the AI agent identity's access token. |

2. Introspect the AI agent identity's access token to verify the claims contain the expected values:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/oauth2/realms/root/realms/alpha/tokeninfo' \(1)
   --data-urlencode 'access_token=<ai-agent-access-token>'(2)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                         |
   > | ----- | ------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                    |
   > | **2** | Replace \<ai-agent-access-token> with the AI agent identity's access token from the response in step 1. |

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
   > |       |                                                                                                                                           |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `sub` claim contains the AI agent identity's client ID, which indicates that the token represents the agent.                          |
   > | **2** | The `aud` claim contains the AI agent identity's client ID, which indicates that the intended audience of this access token is the agent. |
   > | **3** | The `scope` claim contains the scopes that the AI agent identity can access.                                                              |

### Task 4.2: Exchange the AI agent identity token for application access

1. Use the Token Exchange grant type to exchange the AI agent identity's access token for a new token scoped to the custom OAuth 2.0 application:

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
   > |       |                                                                                                                                                                                                                                                                                           |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                                      |
   > | **2** | The `grant_type` for this request is `urn:ietf:params:oauth:grant-type:token-exchange`, which represents the Token Exchange grant type.                                                                                                                                                   |
   > | **3** | Replace \<ai-agent-access-token> with the AI agent identity's access token from task 4.1.                                                                                                                                                                                                 |
   > | **4** | Replace \<ai-agent-client-id> with the client ID of the AI agent identity. For example, `bot-traffic-analyzer-agent`.                                                                                                                                                                     |
   > | **5** | Replace \<ai-agent-client-secret> with the client secret of the AI agent identity.                                                                                                                                                                                                        |
   > | **6** | Replace \<oauth2-app-client-id> with the client ID of the custom OAuth 2.0 application. For example, `web-server-logs-api-app`. Setting this as the `audience` indicates that the AI agent identity intends to use the exchanged access token to access the custom OAuth 2.0 application. |
   > | **7** | Replace \<exchanged-scopes> with the scopes that the AI agent identity needs to access the application. For example, `logs-read logs-search`.                                                                                                                                             |

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
   > |       |                                                                                                                                                          |
   > | ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `access_token` value in the response is the scoped token that the AI agent identity can use to access the custom OAuth 2.0 application autonomously. |

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
   > |       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The `sub` claim contains the AI agent identity's client ID, which indicates that the token represents the AI agent identity acting autonomously.                                                                                                                                                                                                                                                                                                                                                                                                |
   > | **2** | The `aud` claim contains the client ID of the AI agent identity and the custom OAuth 2.0 application, which indicates that the intended audience of this access token is both the AI agent identity and the application.                                                                                                                                                                                                                                                                                                                        |
   > | **3** | The `act` claim also contains the AI agent identity's client ID. In an autonomous flow, both `sub` and `act` represent the AI agent identity, in contrast to the "on behalf of" flow where `sub` represents the end user and `act` is the AI agent identity. The presence of `act` alone can't distinguish an autonomous flow from an on-behalf-of flow — you must inspect the `sub` claim to determine whether the token represents an AI agent identity acting autonomously (AI agent identity client ID) or on behalf of a user (user UUID). |
   > | **4** | The `scope` claim contains the scopes that the AI agent identity can access on the application.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `aud` claim in this example includes both the AI agent identity's client ID and the application's client ID because this guide configures Accept Audience parameter in token exchange requests on the OAuth 2.0 provider. Without that setting, the default behavior is for `aud` to contain only the AI agent identity's own `client_id`. You can use the presence of the application client ID in `aud` as a signal that the AI agent identity authenticated autonomously against that specific application. |

---

---
title: Enable the AI agents feature
description: Enable the AI agents feature for Advanced Identity Cloud tenants created before April 2026
component: pingoneaic
page_id: pingoneaic:identity-for-ai:ai-agent-identities-enable
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities-enable.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  enable-the-ai-agents-feature-in-your-development-tenant-environment: "Task 1: Enable the AI agents feature in your development tenant environment"
  promote-the-ai-agents-feature-to-your-other-tenant-environments: "Task 2: Promote the AI agents feature to your other tenant environments"
---

# Enable the AI agents feature

The AI agents feature is enabled by default for tenant environments created on or after the following dates:

* March 30, 2026 (sandbox\[[1](#_footnotedef_1 "View footnote.")] environments)

* April 14, 2026 (development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments)

For tenant environments created before those dates, you can enable the feature using the Ping Identity admin console. After the feature is enabled, you can promote the configuration to your other tenant environments.

## Task 1: Enable the AI agents feature in your development tenant environment

In your development tenant environment:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents (in either realm), then take one of the following actions:

   * If the [icon: add, set=material, size=inline] Enable AI Agent Identity button displays, the feature isn't enabled, and you should continue to the next step in this task.

   * If the [icon: add, set=material, size=inline] Add AI Agent button displays, the feature is already enabled, and you can skip the rest of the steps in this task. However, you should check if the feature is enabled in your other tenant environments, and if necessary, enable the feature in those environments by following the steps in Task 2.

2. Check that the tenant supports these features:

   * **Application management**: Check using the [Application management migration FAQ](../product-information/migration-dependent-features/application-management-migration-faq.html). If the tenant doesn't support application management, contact your Ping Identity representative.

   * **Groups**: Check using the [Group identity migration FAQ](../product-information/migration-dependent-features/group-identity-migration-faq.html). If the tenant doesn't have groups enabled, follow the feature enablement instructions in [Group management](../idm-objects/groups.html).

3. Click the [icon: add, set=material, size=inline] Enable AI Agent Identity button:

   * If the AI Agent Identity is enabling progress message displays, the enablement request was successful. This progress message can display for up to 10 minutes while the feature is being enabled. You can leave the page and return later to check progress. When the feature is fully enabled, the page displays the [icon: add, set=material, size=inline] Add AI Agent button.

   * If an error message displays, the enablement request failed. Double-check that your tenant environment meets the prerequisites in step 2, and if necessary, refresh the page and try enabling the feature again.

   * If you still can't access the feature, open a support case with Ping Identity support:

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
     >    | Field                                                | Value                                                                    |
     >    | ---------------------------------------------------- | ------------------------------------------------------------------------ |
     >    | What product family is experiencing the issue?       | Select PingOne Advanced Identity Cloud                                   |
     >    | What specific product is experiencing the issue?     | Select Configuration                                                     |
     >    | What version of the product are you using?           | Select NA                                                                |
     >    | What Hostname(s) or Tenant ID(s) does this apply to? | Enter the fully-qualified domain name (FQDN) for the tenant environment. |
     >
     > 5. On the Tell us about the issue page, enter the following details, and then click Next:
     >
     >    | Field                                      | Value                                                                                                                                                                                                                                                                                                                                                                     |
     >    | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     >    | Provide a descriptive title for your issue | Enter `Unable to enable AI agents feature`                                                                                                                                                                                                                                                                                                                                |
     >    | Describe the issue below                   | Enter one of the following descriptions based on the HTTP status code you received in step 4:\* `Received a 500 HTTP status code when making a POST request to the /environment/aiagent?_action=enable endpoint.`\* `Received a 200 HTTP status code when making a POST request to the /environment/aiagent?_action=enable endpoint, but still can't access the feature.` |
     >
     > 6. Click Submit.
     >
     > 7. Wait for Ping Identity support to respond to your case with next steps for troubleshooting the issue.

## Task 2: Promote the AI agents feature to your other tenant environments

After you enable the feature in your development tenant environment, you can promote the configuration to your other tenant environments (UAT\[[2](#_footnotedef_2 "View footnote.")], staging, production).

1. Determine the promotion order of your tenant environments. This depends on whether you have a [standard promotion group of environments](../tenants/self-service-promotions.html#standard-promotion-group-of-environments) or whether you also have [additional UAT environments](../tenants/self-service-promotions.html#additional-uat-environments).

2. In promotion order, for each upper tenant environment in your promotion group, perform the following steps:

   1. Run a promotion to move the configuration to the upper tenant environment from its respective lower tenant environment. Learn more in:

      * [Manage self-service promotions using the admin console](../tenants/self-service-promotions-ui.html)

      * [Manage self-service promotions using the API](../tenants/self-service-promotions-api.html)

   2. In the Advanced Identity Cloud admin console in the upper tenant environment, confirm that the left navigation menu displays the [icon: smart_toy, set=material, size=inline] AI Agents link, and that the [icon: add, set=material, size=inline] Add AI Agent button displays on the page.

3. (Optional) If you have sandbox\[[1](#_footnotedef_1 "View footnote.")] tenant environments, repeat task 1 for each of those.

***

[1](#_footnoteref_1). A [sandbox environment](../tenants/environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Manage AI agent identities using the admin console
description: Create, configure, and manage AI agent identities and their application policies using the Advanced Identity Cloud admin console
component: pingoneaic
page_id: pingoneaic:identity-for-ai:ai-agent-identities-ui
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities-ui.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/ai-agents-ui.adoc"]
section_ids:
  create-an-ai-agent-identity: Create an AI agent identity
  update-an-ai-agent: Update an AI agent identity
  update-basic-settings-or-custom-attributes: Update basic settings or custom attributes
  update-access-settings: Update access settings
  create-application-privileges: Create application privileges
  update-application-privileges: Update application privileges
  delete-an-ai-agent-identity: Delete an AI agent identity
---

# Manage AI agent identities using the admin console

You can find background information on AI agent identities in PingOne Advanced Identity Cloud in [Secure your AI-driven solutions using AI agent identities](ai-agent-identities.html).

## Create an AI agent identity

To create a new AI agent identity:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Click [icon: add, set=material, size=inline] Add AI Agent.

3. In the Add new AI Agent modal:

   1. Enter a descriptive Name for the identity. For example, `Retail Chatbot` or `Workforce Assistant`.

   2. Enter a Client ID for the identity using only alphanumeric characters, dashes, or underscores. For example, `retail-chatbot` or `workforce-assistant`.

      |   |                                                                                   |
      | - | --------------------------------------------------------------------------------- |
      |   | Once you enter a client ID and save the identity, the client ID can't be changed. |

   3. (Optional) Enter a Client Secret:

      * If you don't enter a value for the client secret, you can enter it later using the Access tab.

      * If you do enter a value, make a note of it, as you won't be able to view it again after creating the identity.

   4. (Optional) Click Use Secret Store for secrets, then enter a Secret Label Identifier.

      * If you don't enter a value, you can enter it later using the Access tab.

      * If you do enter a value, after saving the identity you must also create an ESV secret and map it to a secret label with the format `am.applications.oauth2.client.<identifier>.secret`. For example, if you enter `retail-chatbot-secret` as the secret label identifier, you must create an ESV secret and map it to the secret label `am.applications.oauth2.client.retail-chatbot-secret.secret`. Learn more in [Secret labels with identifiers](../tenants/esvs-signing-encryption.html#secret-labels-with-identifiers).

   5. Click Save.

4. Complete the new identity's configuration using the instructions in [Update an AI agent identity](#update-an-ai-agent).

## Update an AI agent identity

To update an AI agent identity, use the following instructions:

* [Update basic settings or custom attributes](#update-basic-settings-or-custom-attributes)

* [Update access settings](#update-access-settings)

* Manage application policies:

  * [Create application privileges](#create-application-privileges)

  * [Update application privileges](#update-application-privileges)

### Update basic settings or custom attributes

To view or edit an AI agent identity's basic settings or custom attributes:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the identity you want to edit, then click it.

3. Click the Overview tab:

   1. (Optional) Edit the identity's Name. The name should be a descriptive label for the identity, such as `Retail Chatbot` or `Workforce Assistant`.

   2. (Optional) Enter a Description for the identity. The description should provide additional context about the identity's purpose or functionality, such as `A chatbot that helps retail customers navigate products and answer questions` or `A workforce assistant that helps employees access enterprise tools and resources`.

   3. (Optional) Select one or more Agent Owners for the identity. Agent owners are symbolic owners that can be used for visibility within your organization, but don't have any functional permissions or privileges related to the AI agent identity.

   4. (Optional) Click Show advanced settings, then enter one or more Custom attributes. Custom attributes are key-value pairs that let you add additional metadata to the identity. For example, you could add `status` and `state` attributes to track the identity's lifecycle.

      You can enter custom attributes in two ways:

      * **Basic editor**: Use Name and Value fields to enter custom attributes one at a time. You can click the add button ([icon: add, set=material, size=inline]) to add additional custom attributes as needed and click the remove button ([icon: remove, set=material, size=inline]) to remove any custom attributes you no longer need.

        ![AI agent identity custom attributes basic editor showing two custom attributes: 'status': 'active' and 'state': 'awaiting-approval'](_images/ai-agent-custom-attributes-basic-editor.png)

      * **Advanced editor**: Use a JSON editor to directly manage the underlying JSON object that stores the custom attributes. To switch to the JSON editor, click Use advanced editor. You can switch back to the basic editor at any time by clicking Use basic editor.

        ![AI agent identity custom attributes advanced editor showing a JSON object with two key-value pairs: 'status': 'active' and 'state': 'awaiting-approval'](_images/ai-agent-custom-attributes-advanced-editor.png)

4. Click Save.

### Update access settings

To view or edit an AI agent identity's OAuth 2.0 settings:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the identity you want to edit, then click it.

3. Click the Access tab.

4. Review the identity's Client ID and Client Secret fields:

   * The Client ID is a read-only field and can't be modified.

   * The Client Secret is a read-only, masked field.

5. (Optional) To add, update, or reset the Client Secret:

   1. Click the Reset button to the right of the Client Secret field.

   2. In the Reset Client Secret modal, enter a password in the New Client Secret field. Make a note of the new secret, as you won't be able to view it again after clicking Save.

   3. Click Save.

6. (Optional) Click Use Secret Store for secrets, then enter a Secret Label Identifier. If you enter a value, after saving the identity you must also create an ESV secret and map it to a secret label with the format `am.applications.oauth2.client.<identifier>.secret`. For example, if you enter `retail-chatbot-secret` as the secret label identifier, you must create an ESV secret and map it to the secret label `am.applications.oauth2.client.retail-chatbot-secret.secret`. Learn more in [Secret labels with identifiers](../tenants/esvs-signing-encryption.html#secret-labels-with-identifiers).

7. (Optional) Click Show advanced settings and update the OAuth 2.0 client profile settings as needed. The settings are listed in step 4 of [Create a client profile](https://docs.pingidentity.com/pingam/8/am-oauth2/oauth2-register-client.html#configure-oauth2-client-profile).

8. Click Save.

### Create application privileges

You can create application privileges for an AI agent identity to specify which applications the identity can access, which end users or groups of end users the identity can act on behalf of when accessing those applications, and which OAuth 2.0 scopes the identity can use when accessing those applications.

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the identity you want to edit, then click it.

3. Click the Applications tab.

4. For each application privilege needed, do the following:

   1. Click [icon: add, set=material, size=inline] Add Application to open the Add new Application modal.

   2. In the Resources list, select an application. Learn how to create an application to select here in [Application management](../app-management/applications.html).

   3. (Optional) Enter a Description for the application privilege. The description should provide additional context about the application privilege. For example:

      * `Allows the retail chatbot to access the product catalog on behalf of customers to help them find products and answer questions`

      * `Allows the workforce assistant to access Salesforce on behalf of employees`.

   4. (Optional) In the Acting On Behalf Of section, use one or both of the Subjects and Subject Groups drop-down lists to select which individual users (subjects) or groups of users (subject groups) the identity can act on behalf of when accessing the application. For example:

      * For a retail chatbot, you could specify a `Privilege Member` customer group to allow the identity to act on behalf of any user in that group.

      * For a workforce assistant, you could specify `Sales Support` and `Customer Service` employee groups to allow the identity to act on behalf of any user in that group.

      To create users or groups to select here, refer to [Manage identities](../identities/manage-identities.html).

   5. (Optional) In the Permissions section, use the Permissions field to select or enter scopes:

      * You can select specific scopes in the list. The scopes in this list come from the application you select in the Resources field.

        > **Collapse: Guidance on selecting scopes for AI agent identities**
        >
        > When selecting scopes, you should choose only the scopes that are necessary for the identity to perform its intended functions when accessing the application, following the principle of least privilege. In particular, you should avoid selecting any high-risk or sensitive scopes that would allow the identity to perform actions that could be destructive or have significant consequences if misused, such as deleting data or managing user accounts.
        >
        > For example:
        >
        > * For a retail chatbot accessing a product catalog application, you might only select read-only scopes that allow the identity to view product information on behalf of customers, but not any write scopes that would allow the identity to modify or delete product information. Additionally, you might want to select scopes that allow the identity to add a product to a customer's shopping cart on their behalf, but avoid any scopes that would allow the identity to complete a purchase on the customer's behalf without their explicit approval.
        >
        > * For a workforce assistant accessing Salesforce, you might select a mix of read and write scopes that allow the identity to view and update customer information on behalf of employees, but avoid any high-risk scopes that would allow the identity to delete customer information or manage user accounts.

        To create scopes to select here, in the Advanced Identity Cloud admin console, go to [icon: apps, set=material, size=inline] Applications, select the application you want to create scopes for, click the Sign On tab, then enter scope values in the Scopes field.

      * You can also enter custom scope values that aren't in the list by typing them into the field.

   6. Click Save.

### Update application privileges

To update application privileges for an AI agent identity:

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Review the AI Agents page to find the identity you want to edit, then click it.

3. Click the Applications tab.

4. Review the application privileges to find the privilege you want to update.

5. To update an application privilege:

   1. Click the application privilege.

   2. In the Edit Application modal, follow the instructions in step 6 of [Create application privileges](#create-application-privileges).

6. To revoke an application privilege:

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Revoking an application privilege immediately removes the identity's access to the associated application, which could cause disruptions if the identity is actively performing tasks on behalf of end users when you revoke the privilege. Before revoking an application privilege, review the identity's activity and audit logs to understand its recent actions and ensure that revoking the privilege won't cause unintended consequences for your end users or your organization's AI-driven solutions. |

   1. Click the application privileges' ellipsis icon ([icon: more_horiz, set=material, size=inline]) to open its actions menu, then click [icon: delete, set=material, size=inline] Revoke.

## Delete an AI agent identity

Before deleting an AI agent identity, review the identity's activity and audit logs to understand its recent actions and ensure that it's not still in use by any of your organization's AI-driven solutions.

1. In the Advanced Identity Cloud admin console, go to [icon: smart_toy, set=material, size=inline] AI Agents.

2. Choose one of the following actions:

   * To delete an identity from the AI Agents page:

     1. Click the identity's ellipsis icon ([icon: more_horiz, set=material, size=inline]) to open its actions menu, then click [icon: delete, set=material, size=inline] Delete.

     2. In the Delete AI Agent? modal, click Delete.

   * To delete an identity from the identity's own page:

     1. Click the AI agent.

     2. Click Delete Agent.

     3. In the Delete Agent? modal, click Delete.

---

---
title: Manage AI agent identities using the API
description: Use the Advanced Identity Cloud REST API to create, read, update, and delete AI agent identities and AI agent privileges programmatically using a service account bearer token.
component: pingoneaic
page_id: pingoneaic:identity-for-ai:ai-agent-identities-api
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities-api.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  prerequisites: Prerequisites
  authenticate-to-the-endpoints: Authenticate to the API endpoints
  manage-ai-agent-identities: Manage AI agent identities
  get-all-ai-agent-identities: Get all AI agent identities
  get-an-ai-agent-identity: Get an AI agent identity
  create-an-ai-agent-identity: Create an AI agent identity
  update-an-ai-agent-identity: Update an AI agent identity
  delete-an-ai-agent-identity: Delete an AI agent identity
  manage-ai-agent-identity-privileges: Manage AI agent identity privileges
  get-all-ai-agent-identity-privileges: Get all AI agent identity privileges
  get-an-ai-agent-identity-privilege: Get an AI agent identity privilege
  create-an-ai-agent-identity-privilege: Create an AI agent identity privilege
  update-an-ai-agent-privilege: Update an AI agent identity privilege
  delete-an-ai-agent-privilege: Delete an AI agent identity privilege
  look-up-identity-management-uuids: Look up identity management UUIDs
  look-up-an-ai-agent-identity-uuid: Look up an AI agent identity UUID
  look-up-application-uuid: Look up an application UUID
  look-up-user-uuid: Look up a user UUID
---

# Manage AI agent identities using the API

You can find background information on AI agent identities in PingOne Advanced Identity Cloud in [Secure your AI-driven solutions using AI agent identities](ai-agent-identities.html).

## Prerequisites

Before managing AI agent identities using the API, verify that the following prerequisites are met:

* The AI agents feature is enabled for your tenant environments. Learn more in [Enable the AI agents feature](ai-agent-identities-enable.html).

* The OAuth 2.0 provider for your realm has the Token Exchange grant type enabled. Learn more in [Configure the OAuth 2.0 provider service](ai-agent-identities-configure-autonomous-agent-flow.html#configure-the-oauth-2-abbr-provider-service).

## Authenticate to the API endpoints

To authenticate to the access management and identity management API endpoints, use an [access token](../developer-docs/authenticate-to-rest-api-with-access-token.html) created with one or both of the `fr:am:*` and `fr:idm:*` scopes.

| Scope      | API endpoint                                                                                                                                                     | Description                                                                                                                                                                                                                      |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `fr:am:*`  | * `/am/json/realms/root/realms/<realm>/realm-config/agents/AIAgent`                                                                                              | Endpoint is part of the access management API. Use for agent operations. Each token request creates an access management session.	A maximum of 5 concurrent access management sessions are allowed per service account identity. |
| `fr:idm:*` | - `/openidm/managed/<realm>_aiagentprivilege`

- `/openidm/managed/<realm>_aiagent`

- `/openidm/managed/<realm>_application`

- `/openidm/managed/<realm>_user` | Endpoints are part of the identity management API. Use for privilege operations and UUID lookups. Doesn't consume session quota.                                                                                                 |

For full lifecycle management of both agents and privileges, request both `fr:am:*` and `fr:idm:*` scopes.

## Manage AI agent identities

All operations in this section use the access management REST API at `realm-config/agents/AIAgent` and require `fr:am:*` scope.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you create an AI agent identity via the access management REST API, Advanced Identity Cloud automatically creates a linked `managed/alpha_aiagent` object in identity management and records its UUID in the `aiAgentIdentityUid` field on the OAuth 2.0 client. You need this UUID when creating privileges for the identity. Learn more in [Look up identity management UUIDs](#look-up-identity-management-uuids). |

### Get all AI agent identities

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:am:*` scope, or reuse an existing access token to minimize access management session consumption.

2. Run the following command:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/agents/AIAgent' \(1)(2)
   --header 'Accept-API-Version: resource=2.0' \
   --header 'Authorization: Bearer <access-token>' \(3)
   --data-urlencode '_queryFilter=true'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                      |
   > | ----- | -------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment. |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                            |
   > | **3** | Replace \<access-token> with your service account access token.      |

   ```json
   {
     "result": [
       {
         "_id": "bot-traffic-analyzer-agent", (1)
         "_rev": "-69253262",
         ...,
         "aiAgentIdentityUid": "2835a79f-aa51-446c-808d-0195b2fec75c", (2)
         ...
       },
       {
         "_id": "digital-assistant-ai-agent", (1)
         "_rev": "-142442485",
         ...
         "aiAgentIdentityUid": "19301b4f-27ae-43fd-adc3-04389fd97f42", (2)
         ...
       }
     ],
     "resultCount": 2,
     ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                      |
   > | ----- | -------------------------------------------------------------------- |
   > | **1** | The OAuth 2.0 client IDs of the AI agent identities.                 |
   > | **2** | The identity management UUIDs of the linked `alpha_aiagent` objects. |

### Get an AI agent identity

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:am:*` scope, or reuse an existing access token to minimize access management session consumption.

2. Run the following command:

   ```shell
   $ curl \
   --request GET 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/agents/AIAgent/<agent-client-id>' \(1)(2)(3)
   --header 'Accept-API-Version: resource=2.0' \
   --header 'Authorization: Bearer <access-token>'(4)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                            |
   > | ----- | ---------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                       |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                                  |
   > | **3** | Replace \<agent-client-id> with the OAuth 2.0 client ID of the AI agent identity, for example, `my-agent`. |
   > | **4** | Replace \<access-token> with your service account access token.                                            |

   ```json
   {
     "_id": "digital-assistant-ai-agent", (1)
     "_rev": "2028182383",
     "overrideOAuth2ClientConfig": {
       ...
       "acceptAudienceParametersInTokenExchangeRequests": true, (2)
       ...
       "providerOverridesEnabled": true, (3)
       ...,
       "statelessTokensEnabled": true, (4)
       ...
     },
     "advancedOAuth2ClientConfig": {
       ...
         "tokenEndpointAuthMethod": { (5)
           "inherited": false,
           "value": "client_secret_post"
         },
         ...
         "grantTypes": { (6)
           "inherited": false,
           "value": [
             "urn:ietf:params:oauth:grant-type:token-exchange"
           ]
         },
     },
     ...
     "coreOAuth2ClientConfig": {
       ...
       "status": { (7)
         "inherited": false,
         "value": "Active"
       },
       ...
       "clientType": { (8)
         "inherited": false,
         "value": "Confidential"
       },
       ...
       "scopes": { (9)
         "inherited": false,
         "value": []
       },
       ...
     },
     ...
     "aiAgentIdentityAttributes": {
       "inherited": false,
       "value": {
         "_id": "19301b4f-27ae-43fd-adc3-04389fd97f42", (10)
         "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1309951",
         "oauth2ClientId": "digital-assistant-ai-agent", (11)
         "name": "Digital Assistant Web App", (12)
         ...
       }
     },
     "aiAgentIdentityUid": {
       "inherited": false,
       "value": "19301b4f-27ae-43fd-adc3-04389fd97f42" (13)
     },
     "_type": {
       "_id": "AIAgent",
       "name": "AI Agents",
       "collection": true
     }
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |        |                                                                                                                                                                                                  |
   > | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1**  | The OAuth 2.0 client ID of the AI agent identity.                                                                                                                                                |
   > | **2**  | Accept audience parameters in token exchange requests. When enabled, the identity can request access tokens for audiences that differ from its own.                                              |
   > | **3**  | Enable OAuth 2.0 provider overrides. When enabled, the identity can bypass realm-wide provider defaults and enforce its own custom token lifetimes, scripts, consent rules, and plugin settings. |
   > | **4**  | Allow client-side access and refresh tokens. When enabled, the identity can request access and refresh tokens that are not stored in the server-side session.                                    |
   > | **5**  | The token endpoint auth method for the identity. Valid values are `client_secret_post` (credentials in POST body) or `client_secret_basic` (HTTP Basic Auth).                                    |
   > | **6**  | The OAuth 2.0 grant types for the identity.                                                                                                                                                      |
   > | **7**  | The status of the identity.                                                                                                                                                                      |
   > | **8**  | The client type of the identity.                                                                                                                                                                 |
   > | **9**  | The allowed scopes for the identity.                                                                                                                                                             |
   > | **10** | The identity management UUID of the linked `alpha_aiagent` object.                                                                                                                               |
   > | **11** | The OAuth 2.0 client ID of the linked `alpha_aiagent` object.                                                                                                                                    |
   > | **12** | The name of the linked `alpha_aiagent` object.                                                                                                                                                   |
   > | **13** | The identity management UUID of the linked `alpha_aiagent` object.                                                                                                                               |

### Create an AI agent identity

You can use a single PUT request to create both the access management OAuth 2.0 client and the linked identity management `alpha_aiagent` object.

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:am:*` scope, or reuse an existing access token to minimize access management session consumption.

2. Run the following command:

   ```shell
   $ curl \
   --request PUT 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/agents/AIAgent/<agent-client-id>' \(1)(2)(3)
   --header 'Accept-API-Version: resource=2.0' \
   --header 'Content-Type: application/json' \
   --header 'If-None-Match: *' \(4)
   --header 'Authorization: Bearer <access-token>' \(5)
   --data-raw '{
     "aiAgentIdentityAttributes": {
       "inherited": false,
       "value": {
         "name": "<agent-id>",
         "oauth2ClientId": "<agent-id>"
       }
     },
     "coreOAuth2ClientConfig": {
       "status":     { "inherited": false, "value": "Active" },
       "clientType": { "inherited": false, "value": "Confidential" },
       "scopes":     { "inherited": false, "value": <scopes> }(6)
     },
     "advancedOAuth2ClientConfig": {
       "grantTypes":              { "inherited": false, "value": <grant-types> },(7)
       "tokenEndpointAuthMethod": { "inherited": false, "value": "<auth-method>" }(8)
     }
   }'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                                                                                                                                   |
   > | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                              |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                                                                                                                                                                                         |
   > | **3** | Replace \<agent-client-id> with the OAuth 2.0 client ID for the new AI agent identity, for example, `my-agent`.                                                                                                                                                   |
   > | **4** | `If-None-Match: *` enforces create-only semantics; the request fails with HTTP 412 if an AI agent identity with this OAuth 2.0 client ID already exists. Omit this header to allow upsert (create or overwrite).                                                  |
   > | **5** | Replace \<access-token> with your service account access token.                                                                                                                                                                                                   |
   > | **6** | Replace \<scopes> with a JSON array of scopes, for example, `["openid", "profile", "email"]`. An AI agent identity with no allowed scopes can't mint tokens.                                                                                                      |
   > | **7** | Replace \<grant-types> with a JSON array of grant types:- For an on-behalf-of agent: `["urn:ietf:params:oauth:grant-type:token-exchange"]`
   >
   > - For an autonomous agent: `["client_credentials", "urn:ietf:params:oauth:grant-type:token-exchange"]`                |
   > | **8** | Replace \<auth-method> with the token endpoint auth method: `client_secret_post` (credentials in POST body) or `client_secret_basic` (HTTP Basic Auth). The caller must use the same method when authenticating the AI agent identity in token exchange requests. |

   The request returns an HTTP 201 status code on success. Find an example response body in [Get an AI agent identity](#get-an-ai-agent-identity).

### Update an AI agent identity

The access management REST API doesn't support PATCH for AI agent identity configuration. To update an AI agent identity, read the current configuration, modify the fields you want to change, remove `_rev` from the body, then PUT the full body back.

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:am:*` scope, or reuse an existing access token to minimize access management session consumption.

2. Get the current configuration with a GET request:

   ```shell
   $ curl \
   --request GET 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/agents/AIAgent/<agent-client-id>' \(1)(2)(3)
   --header 'Accept-API-Version: resource=2.0' \
   --header 'Authorization: Bearer <access-token>'(4)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                             |
   > | ----- | ------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                        |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                   |
   > | **3** | Replace \<agent-client-id> with the OAuth 2.0 client ID of the AI agent identity to update. |
   > | **4** | Replace \<access-token> with your service account access token.                             |

3. Take the response body from the previous step, update the fields you want to change, then remove the `_rev` field. The following table contains common fields and their `jq` paths:

   | Field                      | `jq` path                                                   |
   | -------------------------- | ----------------------------------------------------------- |
   | Allowed scopes             | `.coreOAuth2ClientConfig.scopes.value`                      |
   | Grant types                | `.advancedOAuth2ClientConfig.grantTypes.value`              |
   | Token endpoint auth method | `.advancedOAuth2ClientConfig.tokenEndpointAuthMethod.value` |
   | Client secret              | `.userpassword` (write-only; not returned in GET responses) |

4. Update the configuration with a PUT request:

   ```shell
   $ curl \
   --request PUT 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/agents/AIAgent/<agent-client-id>' \(1)(2)(3)
   --header 'Accept-API-Version: resource=2.0' \
   --header 'Content-Type: application/json' \
   --header 'Authorization: Bearer <access-token>' \(4)
   --data-raw '<modified-configuration-body>'(5)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                                                                                                                                                                  |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                                                                             |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                                                                                                                                                                                                                        |
   > | **3** | Replace \<agent-client-id> with the OAuth 2.0 client ID of the AI agent identity to update.                                                                                                                                                                                                      |
   > | **4** | Replace \<access-token> with your service account access token.                                                                                                                                                                                                                                  |
   > | **5** | Replace \<modified-configuration-body> with the response body from step 1, with your changes applied and the `_rev` field removed. To set the OAuth 2.0 client secret, add `"userpassword": "<agent-client-secret>"` to the body (this field is write-only and isn't returned in GET responses). |

   The request returns an HTTP 200 status code on success. Find an example response body in [Get an AI agent identity](#get-an-ai-agent-identity).

### Delete an AI agent identity

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:am:*` scope, or reuse an existing access token to minimize access management session consumption.

2. Run the following command:

   ```shell
   $ curl \
   --request DELETE 'https://<tenant-env-fqdn>/am/json/realms/root/realms/<realm>/realm-config/agents/AIAgent/<agent-client-id>' \(1)(2)(3)
   --header 'Accept-API-Version: resource=2.0' \
   --header 'Authorization: Bearer <access-token>'(4)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                             |
   > | ----- | ------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                        |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                   |
   > | **3** | Replace \<agent-client-id> with the OAuth 2.0 client ID of the AI agent identity to delete. |
   > | **4** | Replace \<access-token> with your service account access token.                             |

   The request returns an HTTP 200 status code on success.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deleting an AI agent identity cascades immediately to delete the linked identity management `alpha_aiagent` object and all `alpha_aiagentprivilege` records associated with the identity. There's no need to delete privileges first. If you recreate an identity with the same client ID, it gets a new identity management UUID and you must recreate its privileges from scratch. Learn more in [Cascade behavior](ai-agent-identities-supplementary-information.html#cascade-behavior). |

## Manage AI agent identity privileges

All privilege operations use the identity management REST API at `managed/alpha_aiagentprivilege` and require `fr:idm:*` scope.

Privilege request bodies use identity management UUID references, not OAuth 2.0 client IDs. Use [Look up identity management UUIDs](#look-up-identity-management-uuids) to resolve human-readable IDs to identity management UUIDs before creating or updating privileges.

### Get all AI agent identity privileges

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/openidm/managed/<realm>_aiagentprivilege' \(1)(2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --data-urlencode '_queryFilter=true'(4)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                          |
   > | ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                     |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                                                                |
   > | **3** | Replace \<access-token> with your service account access token.                                                                          |
   > | **4** | To filter by a specific AI agent identity, replace `true` with `agentOAuth2ClientId eq "<agent-client-id>"` (curl handles URL-encoding). |

   ```json
   {
     "result": [
       {
         "_id": "cfdd1e7f-2750-4c6d-8730-2d689450b223", (1)
         "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1069810",
         "agentID": "19301b4f-27ae-43fd-adc3-04389fd97f42", (2)
         ...
         "agentOAuth2ClientId": "digital-assistant-ai-agent" (3)
       },
       {
         "_id": "0fbe36e5-adff-481c-9adc-f7f8d08114a1", (1)
         "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1316846",
         "agentID": "2835a79f-aa51-446c-808d-0195b2fec75c", (2)
         ...
         "agentOAuth2ClientId": "bot-traffic-analyzer-agent" (3)
       }
     ],
     "resultCount": 2,
     ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                 |
   > | ----- | ------------------------------------------------------------------------------- |
   > | **1** | The UUID of the privilege.                                                      |
   > | **2** | The UUID of the AI agent identity associated with the privilege.                |
   > | **3** | The OAuth 2.0 client ID of the AI agent identity associated with the privilege. |

### Get an AI agent identity privilege

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl \
   --request GET 'https://<tenant-env-fqdn>/openidm/managed/<realm>_aiagentprivilege/<privilege-id>' \(1)(2)(3)
   --header 'Authorization: Bearer <access-token>'(4)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                             |
   > | ----- | --------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.        |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                   |
   > | **3** | Replace \<privilege-id> with the identity management UUID of the privilege. |
   > | **4** | Replace \<access-token> with your service account access token.             |

   ```json
   {
     "_id": "cfdd1e7f-2750-4c6d-8730-2d689450b223", (1)
     "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1069810",
     "agentID": "19301b4f-27ae-43fd-adc3-04389fd97f42", (2)
     "subjectIDs": [
       "fc87eea4-3c96-49d1-9620-bf23aca9bd97" (3)
     ],
     "permissions": [
       {
         "type": "scopes",
         "values": [ (4)
           "read-data",
           "write-data"
         ]
       }
     ],
     "resourceData": {
       "ssoEntities": {
         "oidcId": "digital-assistant-web-app" (5)
       },
       "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1057044",
       "_id": "7dd5b63f-274e-4984-8306-824d1c51ec35",
       "_refResourceCollection": "managed/alpha_application",
       "_refResourceId": "7dd5b63f-274e-4984-8306-824d1c51ec35",
       "_ref": "managed/alpha_application/7dd5b63f-274e-4984-8306-824d1c51ec35"
     },
     "description": null,
     "agentOAuth2ClientId": "digital-assistant-ai-agent" (6)
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                      |
   > | ----- | ------------------------------------------------------------------------------------ |
   > | **1** | The UUID of the privilege.                                                           |
   > | **2** | The UUID of the AI agent identity associated with the privilege.                     |
   > | **3** | The UUIDs of permitted users (subjects) for this privilege.                          |
   > | **4** | The scopes the AI agent identity can request in a token exchange for this privilege. |
   > | **5** | The OAuth 2.0 client ID of the application associated with the privilege.            |
   > | **6** | The OAuth 2.0 client ID of the AI agent identity associated with the privilege.      |

### Create an AI agent identity privilege

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl \
   --request POST 'https://<tenant-env-fqdn>/openidm/managed/<realm>_aiagentprivilege?_action=create' \(1)(2)
   --header 'Content-Type: application/json' \
   --header 'Authorization: Bearer <access-token>' \(3)
   --data-raw '{
     "agent": {
       "_ref":           "managed/alpha_aiagent/<agent-uuid>",(4)
       "_refProperties": {}
     },
     "resource": {
       "_ref":           "managed/alpha_application/<application-uuid>",(5)
       "_refProperties": {}
     },
     "subjects": [{
       "_ref":           "managed/alpha_user/<user-uuid>",(6)
       "_refProperties": {}
     }],
     "subjectGroups": [],
     "permissions": [{
       "type":   "scopes",
       "values": <scopes>(7)
     }]
   }'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                                                                                                            |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                                                       |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                                                                                                                                                                  |
   > | **3** | Replace \<access-token> with your service account access token.                                                                                                                                                                            |
   > | **4** | Replace \<agent-uuid> with the identity management UUID of the AI agent identity. Learn more in [Look up identity management UUIDs](#look-up-identity-management-uuids).                                                                   |
   > | **5** | Replace \<application-uuid> with the identity management UUID of the application. Learn more in [Look up identity management UUIDs](#look-up-identity-management-uuids).                                                                   |
   > | **6** | For an on-behalf-of privilege, replace \<user-uuid> with the identity management UUID of a permitted user. For an autonomous privilege (no user subject), set `"subjects": []`.                                                            |
   > | **7** | Replace \<scopes> with a JSON array of scopes the identity can request in a token exchange, for example, `["openid", "profile", "email"]`. To allow any scope permitted by both the AI agent identity and application, set `"values": []`. |

   ```json
   {
     "_id": "cfdd1e7f-2750-4c6d-8730-2d689450b223", (1)
     "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1069810",
     "agentID": "19301b4f-27ae-43fd-adc3-04389fd97f42", (2)
     "subjectIDs": [
       "fc87eea4-3c96-49d1-9620-bf23aca9bd97" (3)
     ],
     "permissions": [
       {
         "type": "scopes",
         "values": [ (4)
           "read-data",
           "write-data"
         ]
       }
     ],
     "resourceData": {
       "ssoEntities": {
         "oidcId": "digital-assistant-web-app" (5)
       },
       "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1057044",
       "_id": "7dd5b63f-274e-4984-8306-824d1c51ec35",
       "_refResourceCollection": "managed/alpha_application",
       "_refResourceId": "7dd5b63f-274e-4984-8306-824d1c51ec35",
       "_ref": "managed/alpha_application/7dd5b63f-274e-4984-8306-824d1c51ec35"
     },
     "description": null,
     "agentOAuth2ClientId": "digital-assistant-ai-agent" (6)
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                      |
   > | ----- | ------------------------------------------------------------------------------------ |
   > | **1** | The UUID of the privilege.                                                           |
   > | **2** | The UUID of the AI agent identity associated with the privilege.                     |
   > | **3** | The UUIDs of permitted users (subjects) for this privilege.                          |
   > | **4** | The scopes the AI agent identity can request in a token exchange for this privilege. |
   > | **5** | The OAuth 2.0 client ID of the application associated with the privilege.            |
   > | **6** | The OAuth 2.0 client ID of the AI agent identity associated with the privilege.      |

The response is denormalized, which means that identity management resolves reference fields and returns computed values. The key differences between the POST request body and the response are:

| Read field            | Write field       | Notes                                                                                               |
| --------------------- | ----------------- | --------------------------------------------------------------------------------------------------- |
| `agentID`             | `agent._ref`      | Identity management UUID of the AI agent identity                                                   |
| `agentOAuth2ClientId` | (computed)        | OAuth 2.0 client ID of the AI agent identity (useful for filtering)                                 |
| `subjectIDs[]`        | `subjects[]._ref` | Identity management UUIDs of permitted users                                                        |
| `resourceData`        | `resource._ref`   | Resolved application object, including `ssoEntities.oidcId` (the application's OAuth 2.0 client ID) |
| `permissions`         | `permissions`     | Same structure in both directions                                                                   |

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A privilege that omits the `permissions` field entirely, or omits `resource`, never matches at token-exchange time even if the identity management API accepts the object. Always include both fields. |

### Update an AI agent identity privilege

Identity management supports partial updates to privileges using PATCH operations. Use the write field names (for example, `subjects`, `resource`), not the denormalized read field names returned in responses (for example, `subjectIDs`, `resourceData`).

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl \
   --request PATCH 'https://<tenant-env-fqdn>/openidm/managed/<realm>_aiagentprivilege/<privilege-id>' \(1)(2)(3)
   --header 'Content-Type: application/json' \
   --header 'Authorization: Bearer <access-token>' \(4)
   --data-raw '[{
     "operation": "replace",
     "field":     "/permissions",
     "value":     [{ "type": "scopes", "values": ["openid", "profile", "email"] }]
   }]'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                             |
   > | ----- | --------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.        |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                   |
   > | **3** | Replace \<privilege-id> with the identity management UUID of the privilege. |
   > | **4** | Replace \<access-token> with your service account access token.             |

   ```json
   {
     "_id": "cfdd1e7f-2750-4c6d-8730-2d689450b223",
     "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1069810",
     ...
     "permissions": [
       {
         "type": "scopes",
         "values": [ (1)
           "openid",
           "profile",
           "email"
         ]
       }
     ],
     ...
     "agentOAuth2ClientId": "digital-assistant-ai-agent"
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                              |
   > | ----- | -------------------------------------------------------------------------------------------- |
   > | **1** | The updated scopes the AI agent identity can request in a token exchange for this privilege. |

The following table shows supported PATCH operations for privilege updates:

| Field          | Operation | Result                                                                                                        |
| -------------- | --------- | ------------------------------------------------------------------------------------------------------------- |
| `/permissions` | `replace` | Replaces the full permissions array. Returns HTTP 200.                                                        |
| `/subjects`    | `replace` | Replaces the full subjects array, including replacing with an empty `[]`. Returns HTTP 200.                   |
| `/subjects/-`  | `add`     | Appends a single `_ref` object to the subjects list. Returns HTTP 200.                                        |
| `/resource`    | `replace` | Replaces the resource reference (changes which application the privilege grants access to). Returns HTTP 200. |

To remove a specific user from subjects, use `replace` with a filtered array. The GET response returns subject UUIDs in the flat `subjectIDs` array. Reconstruct `_ref` objects from those UUIDs, filter out the UUID to remove, then PATCH with the updated array.

### Delete an AI agent identity privilege

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl \
   --request DELETE 'https://<tenant-env-fqdn>/openidm/managed/<realm>_aiagentprivilege/<privilege-id>' \(1)(2)(3)
   --header 'Authorization: Bearer <access-token>'(4)
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                             |
   > | ----- | --------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.        |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                   |
   > | **3** | Replace \<privilege-id> with the identity management UUID of the privilege. |
   > | **4** | Replace \<access-token> with your service account access token.             |

   The request returns an HTTP 200 status code on success. The referenced AI agent identity and application are unaffected.

|   |                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Privilege changes take effect after the privilege cache expires (10 seconds by default). If you delete a privilege and immediately test a token exchange, you may still get a successful response until the cache expires. |

## Look up identity management UUIDs

Privilege request bodies require identity management UUIDs, not OAuth 2.0 client IDs. Use these queries to resolve human-readable identifiers to identity management UUIDs. All lookups require `fr:idm:*` scope.

### Look up an AI agent identity UUID

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/openidm/managed/<realm>_aiagent' \(1)(2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --data-urlencode '_queryFilter=oauth2ClientId eq "<agent-client-id>"' \(4)
   --data '_fields=_id'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                            |
   > | ----- | ---------------------------------------------------------------------------------------------------------- |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                       |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                                  |
   > | **3** | Replace \<access-token> with your service account access token.                                            |
   > | **4** | Replace \<agent-client-id> with the OAuth 2.0 client ID of the AI agent identity, for example, `my-agent`. |

   ```json
   {
     "result": [
       {
         "_id": "19301b4f-27ae-43fd-adc3-04389fd97f42", (1)
         "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1064136"
       }
     ],
     "resultCount": 1,
     ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                                                                                                                                                               |
   > | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | **1** | The UUID is in `.result[0]._id` of the response. You can also find the UUID in the `aiAgentIdentityUid.value` field of the response in [Get an AI agent identity](#get-an-ai-agent-identity). |

### Look up an application UUID

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/openidm/managed/<realm>_application' \(1)(2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --data-urlencode '_queryFilter=ssoEntities/oidcId eq "<app-client-id>"' \(4)
   --data '_fields=_id'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                                                                                                                                                        |
   > | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.                                                                                                                                   |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                                                                                                                                              |
   > | **3** | Replace \<access-token> with your service account access token.                                                                                                                                        |
   > | **4** | Replace \<app-client-id> with the OAuth 2.0 client ID of the application, for example, `my-app`. The filter uses `ssoEntities/oidcId`, which stores the OAuth 2.0 client ID on the application object. |

   ```json
   {
     "result": [
       {
         "_id": "7dd5b63f-274e-4984-8306-824d1c51ec35", (1)
         "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1057044",
       }
     ],
     "resultCount": 1,
     ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                  |
   > | ----- | ------------------------------------------------ |
   > | **1** | The UUID is in `.result[0]._id` of the response. |

### Look up a user UUID

1. [Get an access token](../developer-docs/authenticate-to-rest-api-with-access-token.html#get_an_access_token) with `fr:idm:*` scope.

2. Run the following command:

   ```shell
   $ curl -G \
   --request GET 'https://<tenant-env-fqdn>/openidm/managed/<realm>_user' \(1)(2)
   --header 'Authorization: Bearer <access-token>' \(3)
   --data-urlencode '_queryFilter=userName eq "<username>"' \(4)
   --data '_fields=_id'
   ```

   > **Collapse: Show request guidance**
   >
   > |       |                                                                          |
   > | ----- | ------------------------------------------------------------------------ |
   > | **1** | Replace \<tenant-env-fqdn> with the FQDN of your tenant environment.     |
   > | **2** | Replace \<realm> with `alpha` or `bravo`.                                |
   > | **3** | Replace \<access-token> with your service account access token.          |
   > | **4** | Replace \<username> with the username of the user, for example, `alice`. |

   ```json
   {
     "result": [
       {
         "_id": "fc87eea4-3c96-49d1-9620-bf23aca9bd97", (1)
         "_rev": "696f19cc-4cda-4f9b-aad8-6fbd6d933672-1057047",
       }
     ],
     "resultCount": 1,
      ...
   }
   ```

   > **Collapse: Show response guidance**
   >
   > |       |                                                  |
   > | ----- | ------------------------------------------------ |
   > | **1** | The UUID is in `.result[0]._id` of the response. |

---

---
title: Secure your AI-driven solutions using AI agent identities
description: Secure AI-driven solutions using AI agent identities as specialized OAuth 2.0 clients with delegated token exchange and granular access control
component: pingoneaic
page_id: pingoneaic:identity-for-ai:ai-agent-identities
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/ai-agents.adoc"]
section_ids:
  enable-the-ai-agents-feature: Enable the AI agents feature
  create-an-ai-agent-identity: Create an AI agent identity
  configure-authentication-flows-for-ai-agent-identities: Configure authentication flows for AI agent identities
---

# Secure your AI-driven solutions using AI agent identities

Advanced Identity Cloud lets you secure your organization's AI-driven solutions using *AI agent identities*. These are specialized OAuth 2.0 clients that are onboarded with their own identities. They can securely perform tasks on behalf of end users or autonomous agents through a delegated token exchange process, ensuring distinct accountability and granular access control.

You can use AI agent identities to securely build [digital assistants](https://developer.pingidentity.com/identity-for-ai/glossary/idai-glossary.html#digital-assistant) that operate on behalf of end users, such as a chatbot on a retail website helping a user navigate products, or an internal workforce assistant acting on behalf of an employee to access enterprise tools like Salesforce. You can also use these identities to securely build [digital workers](https://developer.pingidentity.com/identity-for-ai/glossary/idai-glossary.html#digital-worker) that perform tasks without an end user present, such as an automated pipeline that processes data and updates a dashboard, or a background task that monitors for security threats and takes action when a threat is detected.

Advanced Identity Cloud models AI agent identities as OAuth 2.0 clients with their own [agent and privilege](ai-agent-identities-supplementary-information.html#ai-agent-identity-managed-object-types) managed object types. This structure lets you configure these identities to use delegation rather than simple impersonation and ensures that when an identity requests access to an application, it uses a token exchange process that presents both its own identity and the identity of the end user or autonomous agent. This granular approach to token exchange improves security by preventing unauthorized access and stopping autonomous agents from executing unintended or destructive commands. It also enables "human-in-the-loop" workflows, where end users must explicitly approve high-risk or sensitive operations.

You can find a quick summary of the AI agents feature in the [Key capabilities and benefits](ai-agent-identities-supplementary-information.html#key-capabilities-and-benefits).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have a large number of externally hosted or short-lived clients, maintaining individual AI agent identities may be impractical. While standard AI agent identities use delegated token exchange to manage granular, per-agent privileges, Advanced Identity Cloud also supports an alternative that requires no individual registration: *Client ID Metadata Document* (CIMD).With CIMD, clients host a JSON metadata document at an HTTPS URL, and Advanced Identity Cloud configures them dynamically at runtime using that document. Advanced Identity Cloud doesn't require pre-registered identity records or individual client configuration. This lightweight model is ideal for agents that don't need delegated token exchange or per-agent privileges, such as Model Context Protocol (MCP) clients.Learn more in [Client ID metadata document (CIMD)](../am-oauth2/oauth2-cimd.html). |

## Enable the AI agents feature

The AI agents feature is enabled by default for tenant environments created on or after the following dates:

* March 30, 2026 (sandbox\[[1](#_footnotedef_1 "View footnote.")] environments)

* April 14, 2026 (development, UAT\[[2](#_footnotedef_2 "View footnote.")], staging, and production environments)

For tenant environments created before those dates, refer to [Enable the AI agents feature](ai-agent-identities-enable.html).

## Create an AI agent identity

Use the following steps to create and configure an AI agent identity in Advanced Identity Cloud.

* To use the admin console:

  1. Follow the instructions in [Create an AI agent identity](ai-agent-identities-ui.html#create-an-ai-agent-identity). This creates a new identity and creates its OAuth 2.0 client, but it doesn't configure the OAuth 2.0 client or any application privileges.

  2. Complete the configuration of the identity by creating custom attributes, configuring its OAuth 2.0 client, and assigning it application privileges:

     * [Update basic settings or custom attributes](ai-agent-identities-ui.html#update-basic-settings-or-custom-attributes)

     * [Update access settings](ai-agent-identities-ui.html#update-access-settings)

     * Manage application privileges:

       * [Create application privileges](ai-agent-identities-ui.html#create-application-privileges)

       * [Update application privileges](ai-agent-identities-ui.html#update-application-privileges)

* To use the API:

  1. Follow the instructions in [Create an AI agent identity](ai-agent-identities-api.html#create-an-ai-agent-identity). This creates a new identity and creates and configures its OAuth 2.0 client, but it doesn't create any application privileges.

  2. Follow the instructions in [Create an AI agent identity privilege](ai-agent-identities-api.html#create-an-ai-agent-identity-privilege). This assigns application privileges to the identity.

  |   |                                                                                                                                                                                                                                                                                                        |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | There are also API payload examples in task 3 of [Configure an "on behalf of" authentication flow for AI agents](ai-agent-identities-configure-on-behalf-of-authentication-flow.html) and task 3 of [Configure an autonomous AI agent flow](ai-agent-identities-configure-autonomous-agent-flow.html). |

## Configure authentication flows for AI agent identities

* [Configure an "on behalf of" authentication flow for AI agents](ai-agent-identities-configure-on-behalf-of-authentication-flow.html)\
  The "on behalf of" flow allows an AI agent to perform actions on behalf of an end user, which is useful for securing the actions of assistants.

* [Configure an autonomous AI agent flow](ai-agent-identities-configure-autonomous-agent-flow.html)\
  The autonomous AI agent flow lets an AI agent act independently, without requiring an end user to be present, which is useful for automated pipelines and background tasks.

* [Configure a DCR onboarding flow](ai-agent-identities-configure-dcr-onboarding-flow.html)\
  To streamline the onboarding of OAuth 2.0 clients, Advanced Identity Cloud supports Dynamic Client Registration (DCR), which allows for the automated creation and configuration of dynamic clients without manual intervention.

***

[1](#_footnoteref_1). A [sandbox environment](../tenants/environments-sandbox.html) is an [add-on capability](../product-information/add-on-capabilities.html).[2](#_footnoteref_2). A [user acceptance testing (UAT) environment](../tenants/environments-uat.html) is an [add-on capability](../product-information/add-on-capabilities.html).

---

---
title: Supplementary information for AI agent identities
description: Key capabilities and benefits of securing AI-driven solutions using AI agent identities, summary of managed object types for AI agents
component: pingoneaic
page_id: pingoneaic:identity-for-ai:ai-agent-identities-supplementary-information
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-for-ai/ai-agent-identities-supplementary-information.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  key-capabilities-and-benefits: Key capabilities and benefits
  ai-agent-identity-managed-object-types: AI agent identity managed object types
  object-model: Object model
  cascade-behavior: Cascade behavior
  privilege-evaluation: Privilege evaluation
  error-reference: API error reference
---

# Supplementary information for AI agent identities

## Key capabilities and benefits

The following table summarizes the key capabilities and benefits of securing your AI-driven solutions using AI agent identities:

| Capabilities                                                                                                                                                                               | Benefits                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Specialized agent identity**: Treats AI agents as distinct entities with unique identities and privileges, rather than using simple impersonation.                                       | **Granular security and least privilege**: Eliminates "over-privileged" accounts by applying tailored security policies specific to autonomous entities.           |
| **Streamlined onboarding & lifecycle**: Manual onboarding using OAuth 2.0 grant flow or automated onboarding via Dynamic Client Registration (DCR), with centralized lifecycle management. | **Operational efficiency**: Reduces administrative overhead and "agent sprawl" while ensuring agents can be instantly revoked or rotated.                          |
| **Advanced access and token delegation**: Sophisticated token exchange mechanisms to manage "on-behalf-of" permissions and resource scoping.                                               | **Reduced complexity**: Simplifies the "who, what, and how" of agent access using low-code tools, ensuring secure delegation without custom-coded security logic.  |
| **Dedicated agent observability**: Isolated logging and monitoring that separates agent telemetry from end users and static applications.                                                  | **Clear auditability**: Provides an auditable trail of AI activity, making it easy to prove compliance and understand exactly when an AI agent acted autonomously. |

## AI agent identity managed object types

The following table summarizes the managed object types related to AI agent identities:

| Managed object type | Description                                                                                                                                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| AI agent            | This is distinct from the user managed object type. It provides unique AI agent identities and allows for clear accountability and distinct audit trails for their activities, with Advanced Identity Cloud acting as the dedicated Identity Provider (IdP). |
| AI agent privilege  | This lets AI agent identities have delegated privileges, ensuring that they can only access specific applications, act for specific end users or groups of end users, and use specific OAuth 2.0 scopes.                                                     |

## Object model

The AI agent identity object model spans two systems: access management (system of record) and identity management (privileges store). When you create an AI agent identity in access management, Advanced Identity Cloud automatically creates a linked identity management `<realm>_aiagent` object and records its UUID in the `aiAgentIdentityUid` field on the access management OAuth 2.0 client.

| Object type                          | System              | Purpose                                                                                                                                                                                                                            |
| ------------------------------------ | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OAuth 2.0 client (AI agent identity) | Access management   | The agent's OAuth 2.0 identity; defines grant types, scopes, and authentication method. Deleting this object cascades to all linked identity management objects.                                                                   |
| `alpha_aiagent`                      | Identity management | Created automatically when an access management AI agent identity is created. Stores the agent's identity management UUID, which is referenced by privilege objects.                                                               |
| `alpha_aiagentprivilege`             | Identity management | Links the AI agent identity to a specific application (`<realm>_application`), a set of permitted users (`<realm>_user`), and a scope allowlist. Multiple privilege records can exist for a single identity (one per application). |

## Cascade behavior

Access management is the system of record for the entire AI identity object graph. Deleting an AI agent identity using the access management endpoint cascades immediately to:

1. Delete the linked identity management `<realm>_aiagent` object.

2. Delete all `<realm>_aiagentprivilege` records that reference the agent.

Application and user objects are independent and aren't affected.

Key consequences:

* **Single-step deletion**: Associated privileges are removed automatically without needing manual cleanup, preventing orphaned records.

* **Non-recoverable**: Recreating an identity with the same client ID generates a new identity management UUID. Previous privileges are permanently lost and must be reconfigured.

## Privilege evaluation

At token-exchange time, Advanced Identity Cloud evaluates the privileges of an AI agent identity in the following order:

1. **Audience check**: The token exchange request includes an `audience` parameter containing the application's OAuth 2.0 client ID. Advanced Identity Cloud matches this against privileges where `resource.ssoEntities.oidcId` equals the audience value.

2. **Permission check**: The requested scopes must be a subset of the scopes in the privilege's `permissions.values` list. If `values` is empty, any scope permitted by both the AI agent identity and the application is allowed.

3. **Subject check**: For on-behalf-of flows, the subject token's user identity must appear in the privilege's `subjects` list. For autonomous flows, the `subjects` list must be empty (or the privilege must have no subject restriction).

4. **Scope check**: The final granted scopes are the intersection of: the scopes in the privilege, the scopes on the application, and the scopes on the AI agent identity.

|   |                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Privilege changes take effect after the privilege cache expires (10 seconds by default). A privilege you create or update may not be applied immediately in the next token exchange. |

## API error reference

Common error responses when managing AI agent identities via the REST API:

| HTTP status                | Condition                                                                                                                                             | Resolution                                                                                                                                                                                                |
| -------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `400 Bad Request`          | Missing required field in privilege request body (for example, no `resource` or no `agent` reference)                                                 | Ensure both `agent._ref` and `resource._ref` are present in the request body.                                                                                                                             |
| `401 Unauthorized`         | Access token is missing, expired, or has insufficient scope                                                                                           | Obtain a new service account access token with the required scopes (`fr:am:*` for agent operations; `fr:idm:*` for privilege operations).                                                                 |
| `404 Not Found`            | AI agent identity or privilege does not exist at the specified path                                                                                   | Verify the agent client ID or privilege UUID in the URL. Use the list endpoint to confirm the object exists.                                                                                              |
| `412 Precondition Failed`  | `If-None-Match: *` was specified for create-only semantics, but an AI agent identity with this client ID already exists.                              | The AI agent identity already exists. Omit `If-None-Match: *` to allow an upsert, or use a different OAuth 2.0 client ID.                                                                                 |
| `422 Unprocessable Entity` | A privilege reference points to an identity management object that doesn't exist (for example, an invalid AI agent identity UUID or application UUID) | Verify the UUIDs in `agent._ref`, `resource._ref`, and `subjects[]._ref` using the lookup queries in [Look up identity management UUIDs](ai-agent-identities-api.html#look-up-identity-management-uuids). |
| `501 Not Implemented`      | The AI agent feature is not enabled                                                                                                                   | Verify that the AI agent feature is enabled. Learn more in [Enable the AI agents feature in your tenant environment](ai-agent-identities-enable.html).                                                    |