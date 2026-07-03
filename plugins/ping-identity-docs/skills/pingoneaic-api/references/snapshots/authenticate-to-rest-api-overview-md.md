---
title: Authenticate to the Advanced Identity Cloud REST API
description: The Advanced Identity Cloud REST API has two different authentication methods, depending on what you are trying to achieve:
component: pingoneaic-api
page_id: pingoneaic-api::authenticate-to-rest-api-overview
canonical_url: https://developer.pingidentity.com/pingoneaic-api/authenticate-to-rest-api-overview.html
keywords: ["Integration", "REST API", "Authentication"]
section_ids:
  summary-of-authentication-methods: Summary of authentication methods
---

# Authenticate to the Advanced Identity Cloud REST API

The Advanced Identity Cloud REST API has two different authentication methods, depending on what you are trying to achieve:

* Use an API key and secret for read-only operations.\
  Examples: Advanced Identity Cloud monitoring and logging.

* Use an access token for access management operations or identity management operations.\
  Examples: Setting up authentication journeys or policies; configuring user profiles, roles, or assignments.

## Summary of authentication methods

The following table summarizes the REST API endpoints and their different authentication methods:

| REST endpoints                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Authentication method                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| * `/monitoring/health`

* `/.well-known/*` (for `GET` requests)                                                                                                                                                                                                                                                                                                                                                                                                              | Not applicable (publicly accessible endpoint)                                                                                                                       |
| - `/monitoring`

- `/logs`                                                                                                                                                                                                                                                                                                                                                                                                                                                   | API key and secret.Learn more in [Authenticate to Advanced Identity Cloud REST API with API key and secret](authenticate-to-rest-api-with-api-key-and-secret.html). |
| * `/am/*`

* `/openidm/*`

* `/.well-known/*`

* `/environment/certificates`, `/environment/csrs` 

* `/environment/content-security-policy/*`

* `/environment/cookie-domains`

* `/environment/custom-domains`

* `/environment/promotion/*`

* `/environment/proxy-connect/*`

* `/environment/release`

* `/environment/restart`, `/environment/secrets`, `/environment/variables` 

* `/environment/release`

* `/environment/sso-cookie`

* `/environment/telemetry/*` | Access tokenLearn more in [Authenticate to Advanced Identity Cloud REST API with access token](authenticate-to-rest-api-with-access-token.html).                    |
