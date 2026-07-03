---
title: April 2023
description: New Form Connector
component: connectors
page_id: connectors::relnotes/archive/2023-04-April
canonical_url: https://docs.pingidentity.com/connectors/relnotes/archive/2023-04-April.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: January 16, 2026
section_ids:
  april-22: April 22
  the-forms-connector-is-now-available: The Forms connector is now available
  find-multiple-users: Find multiple users
  pingone-mfa-connector: PingOne MFA Connector
  new-flows-for-the-pingone-radius-gateway-connector: New flows for the PingOne RADIUS Gateway connector
  pingid-connector: PingID Connector
---

# April 2023

## April 22

### The Forms connector is now available

New Form Connector

You can use the [Form Connector](../../form_connector.html) to:

* Build flows around user experiences that you create on the **Experiences > Forms** tab in PingOne.

* Show messages using the branding that you define on the **Experiences > Branding & Themes** tab in PingOne.

### Find multiple users

New PingOne Connector

You can now use the [PingOne Connector](../../p1_connector.html) **Find Multiple Users** capability to search and return up to 100 users.

### PingOne MFA Connector

Improved PingOne MFA Connector

We've enhanced the [PingOne MFA Connector](../../p1_mfa_connector.html) to enable the user to enter their One-time Passcode (OTP) when triggering Multi-factor Authentication (MFA). It's now possible for the user to enter a TOTP/HOTP-generated OTP when starting authentication using the Create Device Authentication endpoint.

### New flows for the PingOne RADIUS Gateway connector

Improved PingOne RADIUS Gateway Connector

We have added the following [PingOne RADIUS Gateway Connector](../../p1_radius_gateway_connector.html) flow templates to support authentication for MS-CHAP v2 protocol, authentication in no-challenge mode, and on-the-fly registration:

* [RADIUS Gateway - Registration and Authentication](https://marketplace.pingone.com/item/radius-gateway-registration-and-authentication)

* [RADIUS Gateway - No Challenge Authentication](https://marketplace.pingone.com/item/radius-gateway-no-challenge-authentication)

* [RADIUS Gateway - Advanced Protocols Authentication](https://marketplace.pingone.com/item/radius-gateway-advanced-protocols-authentication)

### PingID Connector

Improved PingID Connector

We've enhanced the [PingID Connector](../../pid_connector.html) to enable the user to enter their One-time Passcode (OTP) when triggering Multi-factor Authentication (MFA). It's now possible for the user to enter a TOTP/HOTP-generated OTP when starting authentication using the Create Device Authentication endpoint.
