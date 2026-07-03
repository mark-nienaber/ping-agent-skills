---
title: Adding identifiers to authentication
description: "\"Shows how to add identifiers to a PingOne Recognize authentication operation for analytics, auditing, or telemetry purposes.\""
component: recognize
page_id: recognize:web-sdk:web-sdk-reference-authentication-identifiers
canonical_url: https://docs.pingidentity.com/recognize/web-sdk/web-sdk-reference-authentication-identifiers.html
llms_txt: https://docs.pingidentity.com/recognize/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  adding-identifiers: Adding identifiers
  headless: Headless
  web-components: Web components
  retrieving-the-user-id: Retrieving the user ID
---

# Adding identifiers to authentication

The PingOne Recognize Web SDK can associate identifiers with authentication operations. This enables analytics, auditing, and orchestration.

This requires adding `OperationID` to the authentication event.

Once identifiers are enabled, use the Telemetry API to retrieve authentication event details.

## Adding identifiers

To enable authentication identifiers, add them to the authentication details, as shown in the following examples:

### Headless

For headless authentication, add the `OperationID` when opening the web socket:

```javascript
await openKeylessWebSocketConnection(sym, {
  ...,
  operation: {
    id: OPERATION_ID
  }
})
```

### Web components

For web components, add `operation-id` to the authentication component:

```html
<kl-auth
  ...
  operation-id="OPERATION_ID"
></kl-auth>
```

## Retrieving the user ID

To use the Telemetry API, you need the PingOne Recognize user ID associated with the authentication event. Use the Check Client Device API to retrieve the user ID associated with the device.

The Check Client Device API requires the following values:

|            |                                                                   |
| ---------- | ----------------------------------------------------------------- |
| Parameter  | Description                                                       |
| `api_key`  | PingOne Recognize API authorization key                           |
| `customer` | Name of the PingOne Recognize tenant associated with your account |
| `username` | Username defined during enrollment and later used to authenticate |
