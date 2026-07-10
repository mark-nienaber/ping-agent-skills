---
title: Authenticate to Advanced Identity Cloud REST API with access token
description: You need an access token to authenticate to the following Advanced Identity Cloud REST API endpoints:
component: pingoneaic-api
page_id: pingoneaic-api::authenticate-to-rest-api-with-access-token
canonical_url: https://developer.pingidentity.com/pingoneaic-api/authenticate-to-rest-api-with-access-token.html
keywords: ["Integration", "REST API", "Authentication"]
section_ids:
  get-an-access-token: Get an access token
  prerequisites: Prerequisites
  create-a-service-account-and-download-its-private-key: "Task 1: Create a service account and download its private key"
  create-and-sign-a-jwt: "Task 2: Create and sign a JWT"
  get-an-access-token-using-the-jwt-profile-authorization-grant: "Task 3: Get an access token using the JWT profile authorization grant"
  use-an-access-token: Use an access token
---

# Authenticate to Advanced Identity Cloud REST API with access token

You need an access token to authenticate to the following Advanced Identity Cloud REST API endpoints:

* `/am/*`

* `/openidm/*`

* `/.well-known/*`

* `/environment/certificates`, `/environment/csrs` ([self-managed certificate endpoints](https://docs.pingidentity.com/pingoneaic/latest/realms/server-certificates-api.html))

* `/environment/content-security-policy/*`

* `/environment/cookie-domains` ([cookie domains endpoint](https://docs.pingidentity.com/pingoneaic/latest/realms/cookie-domains-api.html))

* `/environment/custom-domains`

* `/environment/promotion/*` ([self-service promotion endpoints](https://docs.pingidentity.com/pingoneaic/latest/tenants/self-service-promotions-api.html))

* `/environment/proxy-connect/*` ([Proxy Connect endpoints](https://docs.pingidentity.com/pingoneaic/latest/tenants/proxy-connect-api.html))

* `/environment/release` ([release endpoint](https://docs.pingidentity.com/pingoneaic/latest/tenants/environments-release-information.html#view-release-information-using-the-api))

* `/environment/restart`, `/environment/secrets`, `/environment/variables` ([ESV endpoints](https://docs.pingidentity.com/pingoneaic/latest/tenants/esvs-manage-api.html))

* `/environment/sso-cookie`

* `/environment/telemetry` ([log event exporter endpoints](https://docs.pingidentity.com/pingoneaic/latest/tenants/audit-debug-logs-push-api.html))

Summary of use:

1. Create a service account in the Advanced Identity Cloud admin console and download a private key.

2. Create a JSON Web Token (JWT) and sign it using the private key.

3. Create an access token using the JWT profile for OAuth 2.0 authorization grant flow.

4. Set the access token as a bearer token in the `Authorization` HTTP header for each API request:

   ```bash
    Authorization: Bearer <access-token>
   ```

## Get an access token

### Prerequisites

You need the [jose](https://github.com/latchset/jose) command-line tool to run some of the commands. The jose command-line tool is a C-language implementation of the JavaScript Object Signing and Encryption (JOSE) standards. You can find installation instructions for your particular package manager in <https://command-not-found.com/jose>.

|   |                                                                                                                                                                   |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The instructions won't work using any of the Node.js tools called jose. Although they have the same name, they're separate implementations of the JOSE standards. |

### Task 1: Create a service account and download its private key

1. Follow the steps in [Create a new service account](https://docs.pingidentity.com/pingoneaic/latest/tenants/service-accounts.html#create-a-new-service-account).

   1. In step 9, save the private key as a local file called `key.jwk`.

   2. Note the ID for the service account you created. An example of an ID is `449d7e27-7889-47af-a736-83b6bbf97ec5`.

### Task 2: Create and sign a JWT

1. Set the following variables in your terminal, to be used as claims in a JWT payload:

   1. Set `SERVICE_ACCOUNT_ID` to hold the ID of the service account. For use in the `iss` (issuer) and `sub` (subject) claims.

      ```bash
      $ SERVICE_ACCOUNT_ID="<service-account-id>"(1)
      ```

      |       |                                                                                                                  |
      | ----- | ---------------------------------------------------------------------------------------------------------------- |
      | **1** | Replace `<service-account-id>` with the service account ID; for example, `449d7e27-7889-47af-a736-83b6bbf97ec5`. |

   2. Set `AUD` to hold the URL (including port number) where the JWT will be used to request the access token. For use in the `aud` (audience) claim.

      ```bash
      $ AUD='https://<tenant-env-fqdn>:443/am/oauth2/access_token'
      ```

   3. Set `EXP` to hold a 15-minute expiration time for the JWT, expressed as a Unix timestamp. For use in the `exp` (expiration time) claim.

      ```bash
      $ EXP=$(($(date -u +%s) + 899))
      ```

      |   |                                                                                                                                                                                                                                                                                                                                         |
      | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Service account access tokens have a non-configurable, fixed expiry of 899 seconds (15 minutes), so the previous example sets a timestamp value that matches the fixed expiry. Despite the expiry being non-configurable, you must supply the `exp` claim, set with a nominal future timestamp, to create an access token successfully. |

   4. Set `JTI` to hold a unique ID for the JWT. For use in the `jti` (JWT ID) claim.

      ```bash
      $ JTI=$(openssl rand -base64 16)
      ```

2. Combine the claims to create a payload for the JWT:

   ```bash
   $ echo -n "{
       \"iss\":\"${SERVICE_ACCOUNT_ID}\",
       \"sub\":\"${SERVICE_ACCOUNT_ID}\",
       \"aud\":\"${AUD}\",
       \"exp\":${EXP},
       \"jti\":\"${JTI}\"
   }" > payload.json
   ```

3. Sign the JWT using the private key you downloaded and saved as `key.jwk` in step 1a:

   ```bash
   $ jose jws sig -I payload.json -k key.jwk -s '{"alg":"RS256"}' -c -o jwt.txt
   ```

### Task 3: Get an access token using the JWT profile authorization grant

1. Request an access token from the `/oauth2/access_token` endpoint using the JWT:

   ```bash
   $ curl \
   --request POST ${AUD} \
   --data "client_id=service-account" \(1)
   --data "grant_type=urn:ietf:params:oauth:grant-type:jwt-bearer" \(2)
   --data "assertion=$(< jwt.txt)" \(3)
   --data "scope=<scope>"(4)
   ```

   |       |                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | **1** | The client ID `service-account` targets the built-in OAuth 2.0 public client for service accounts. The client only allows the [JWT profile for OAuth 2.0 authorization grant flow](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-jwt-bearer-grant.html).	Access the built-in OAuth 2.0 public client using the tenant FQDN. You cannot access it using an Alpha or Bravo realm alias URL or a custom domain URL. |
   | **2** | The grant type `urn:ietf:params:oauth:grant-type:jwt-bearer` represents the JWT profile for OAuth 2.0 authorization grant flow.                                                                                                                                                                                                                                                                                                     |
   | **3** | The `assertion` parameter is populated with the output of the signed JWT from step 2c.                                                                                                                                                                                                                                                                                                                                              |
   | **4** | Replace `<scope>` with a scope or a space delimited set of scopes; for example, `fr:idc:esv:*` or `fr:am:* fr:idm:*`. Learn more in [Service account scopes](https://docs.pingidentity.com/pingoneaic/latest/tenants/service-accounts.html#service-account-scopes). The specified scopes must be the same as (or a subset of) the scopes that you assigned to the service account.                                                  |

2. Examine the response to find the access token, represented as `access_token`:

   ```json
   {
       "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9... ...8ECmkyDJKow8Qp_Tnp_lGNRJzLWi18iUGQrCTtxyTXw",
       "scope": "fr:am:* fr:idm:*",
       "token_type": "Bearer",
       "expires_in": 899
   }
   ```

## Use an access token

To use the access token with the REST API, set it as a bearer token in the `Authorization` HTTP header for each API request.

The following example uses the access token to get a list of identities:

> **Collapse: Show request**
>
> ```bash
> $ curl \
> --request GET 'https://<tenant-env-fqdn>/openidm/managed/<realm>_user?_fields=userName,givenName,sn,mail,accountStatus&_prettyPrint=true&_queryFilter=true' \(1)
> --header 'Authorization: Bearer <access-token>'(2)
> ```

|       |                                                                                                                                             |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **1** | Replace \<realm> with the realm where you created the access token.                                                                         |
| **2** | Replace \<access-token> with the `access_token` in the authentication response (learn more in [Get an access token](#get-an-access-token)). |

> **Collapse: Show response**
>
> ```json
> {
>     "result": [
>         {
>             "_id": "f413db4c-cebd-4950-81e6-57bdb47921a4",
>             "_rev": "0000000016e6754b",
>             "userName": "exampleuser",
>             "accountStatus": "active",
>             "givenName": "Example",
>             "sn": "User",
>             "mail": "exampleuser@example.com"
>         },
>         {
>             "_id": "15249a65-8f9a-4063-9586-a2465963cee4",
>             "_rev": "0000000016e6754b",
>             "userName": "exampleuser2",
>             "accountStatus": "active",
>             "givenName": "Example",
>             "sn": "User",
>             "mail": "exampleuser2@example.com"
>         },
>         {
>             "_id": "30485bc4-fdbb-4946-8ce4-1a53c6824d92",
>             "_rev": "0000000016e6754b",
>             "userName": "exampleuser3",
>             "accountStatus": "active",
>             "givenName": "Example",
>             "sn": "User",
>             "mail": "exampleuser3@example.com"
>         }
>     ],
>     "resultCount": 3,
>     "pagedResultsCookie": null,
>     "totalPagedResultsPolicy": "NONE",
>     "totalPagedResults": -1,
>     "remainingPagedResults": -1
> }
> ```