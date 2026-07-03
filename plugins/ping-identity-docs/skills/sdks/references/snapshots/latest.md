---
title: Access resources using Token Vault
description: After you complete the set up of the Token Vault successfully, you can use the Ping (ForgeRock) SDK for JavaScript or any HTTP or fetch library to request protected resources.
component: sdks
version: latest
page_id: sdks:token-vault:getting-started/04-obtain-tokens
canonical_url: https://docs.pingidentity.com/sdks/latest/token-vault/getting-started/04-obtain-tokens.html
revdate: Tue, 18 Jul 2023 14:37:51 +0100
keywords: ["Setup &amp; Configuration", "OAuth 2.0", "Integration", "Source Code"]
section_ids:
  request_tokens: Request tokens
  make_requests: Make requests
  revoke_tokens: Revoke tokens
  use_convenience_methods: Use convenience methods
  has_method: The has method
  refresh_method: The refresh method
---

# Access resources using Token Vault

After you complete the set up of the Token Vault successfully, you can use the Ping (ForgeRock) SDK for JavaScript or any HTTP or `fetch` library to request protected resources.

With the exception of refreshing tokens, and configuration of the token storage mechanism, using the Ping (ForgeRock) SDK for JavaScript with the Token Vault is almost entirely transparent.

The Token Vault manages token lifecycle automatically. If you enable refresh tokens in your OAuth 2.0 client, the Token Vault automatically refreshes access tokens.

## Request tokens

Use the `TokenManager` class from the SDK as usual to request tokens and have them safely stored within the Token Vault Proxy:

```javascript
import { TokenManager } from '@forgerock/javascript-sdk';

const tokens = TokenManager.getTokens();

console.log(tokens); // Refresh & Access Token values will be redacted
```

You can verify the tokens are stored under the origin of the Token Vault Proxy, not the origin of your main app, by using the developer tools in your browser.

The response your app and the SDK receive contains redacted values. This is expected behavior and increases security.

For example:

```json
{
    "accessToken": "REDACTED",
    "idToken": "eyJ0eXAiOiJKV1QiLCJra...7r8soMCk8A7QdQpg",
    "refreshToken": "REDACTED",
    "tokenExpiry": 1690712227226,
}
```

## Make requests

Use the native `fetch` API or any HTTP request library that emits a fetch event.

For example, you could use the `HttpClient` module provided in the Ping (ForgeRock) SDK for JavaScript.

The Token Vault Interceptor routes any of these requests that matches its configuration through the Token Vault Proxy so that the relevant tokens get attached before reaching your resource server.

## Revoke tokens

To remove tokens and log the user out, use the `FRUser` class as usual:

```javascript
import { FRUser } from '@forgerock/javascript-sdk';

FRUser.logout();
```

This destroys the user's session, revokes tokens on the server, and removes tokens from the Token Vault Proxy.

## Use convenience methods

The `tokenVaultStore` object provides some convenience functions for use in your apps.

These methods are useful as your main app does not have any direct access to the tokens in the Token Vault.

### The `has` method

Use the `has` method to determine whether the Token Vault has relevant tokens stored.

The method returns an object with a `hasTokens` property and a boolean value. It does not return the tokens.

```javascript
const tokenVaultStore = register.store();

const { hasTokens } = tokenVaultStore.has();

console.log(hasTokens); // logs `true` or `false`
```

|   |                                                                                                                                                                                                                                                                            |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This method reflects the presence of tokens but does not validate those tokens. They may have expired or were revoked by the server.To validate the tokens use the `UserManager.getCurrentUser` method. You can consider the tokens valid if the method returns user data. |

### The `refresh` method

Use the `refresh` method to manually request that the Token Vault refreshes its tokens.

The Token Vault attempts to refresh tokens automatically when required, but you can use this `refresh` method to force a refresh of the tokens, if needed.

The method returns an object with a `refreshTokens` property with a boolean value.

```javascript
const tokenVaultStore = register.store();

const { refreshTokens } = tokenVaultStore.refresh();

console.log(refreshTokens); // logs `true` or `false`
```
