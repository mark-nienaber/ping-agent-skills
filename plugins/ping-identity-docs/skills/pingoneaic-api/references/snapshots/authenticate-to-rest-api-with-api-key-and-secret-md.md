---
title: Authenticate to Advanced Identity Cloud REST API with API key and secret
description: You will need an API key and secret to authenticate to the following Advanced Identity Cloud REST API endpoints:
component: pingoneaic-api
page_id: pingoneaic-api::authenticate-to-rest-api-with-api-key-and-secret
canonical_url: https://developer.pingidentity.com/pingoneaic-api/authenticate-to-rest-api-with-api-key-and-secret.html
keywords: ["Integration", "REST API", "Authentication"]
section_ids:
  get-an-api-key-and-secret: Get an API key and secret
  use-an-api-key-and-secret: Use an API key and secret
---

# Authenticate to Advanced Identity Cloud REST API with API key and secret

You will need an API key and secret to authenticate to the following Advanced Identity Cloud REST API endpoints:

* `/monitoring`

* `/logs`

Summary of use:

1. Create an API key and secret in the Advanced Identity Cloud admin console.

2. Set the API key and secret as `x-api-key` and `x-api-secret` HTTP headers for each API request:

   ```
   x-api-key: <api-key>
   x-api-secret: <api-secret>
   ```

## Get an API key and secret

1. In the Advanced Identity Cloud admin console, click the user icon, and then click Tenant Settings.

   > **Collapse: Show me where**
   >
   > ![tenant menu](_images/tenant-menu.png)

2. On the Global Settings tab, click Log API Keys.

3. Click New Log API Key, provide a name for the key, and then click Create Key.

   A dialog box appears containing the new keys:

   ![log api key](_images/log-api-key.png)

4. Store the `api_key_id` and `api_key_secret` values securely.

   |   |                                                                               |
   | - | ----------------------------------------------------------------------------- |
   |   | You **cannot** view the `api_key_secret` value again once you click **Done**. |

5. Click Done.

## Use an API key and secret

To use the API credentials, set them as `x-api-key` and `x-api-secret` HTTP headers:

> **Collapse: Show request**
>
> ```bash
> $ curl \
> --request GET 'https://<tenant-env-fqdn>/monitoring/logs/sources?_prettyPrint=true' \
> --header 'x-api-key: <api-key>' \
> --header 'x-api-secret: <api-secret>'
> ```

> **Collapse: Show response**
>
> ```json
> {
>     "result": [
>         "am-access",
>         "am-activity",
>         "am-authentication",
>         "am-config",
>         "am-core",
>         "am-everything",
>         "idm-access",
>         "idm-activity",
>         "idm-authentication",
>         "idm-config",
>         "idm-core",
>         "idm-everything",
>         "idm-recon",
>         "idm-sync"
>     ],
>     "resultCount": 14,
>     "pagedResultsCookie": null,
>     "totalPagedResultsPolicy": "NONE",
>     "totalPagedResults": 1,
>     "remainingPagedResults": 0
> }
> ```