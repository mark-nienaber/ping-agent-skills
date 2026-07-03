---
title: User Authentication
description: The SCIM protocol doesn't define a method for authenticating a user. The PingOne for Enterprise Directory API uses the OAuth 2.0 Resource Owner Password Credential grant to facilitate user authentication.
component: p14e-directory-api
page_id: p14e-directory-api::user-authentication
canonical_url: https://developer.pingidentity.com/p14e-directory-api/user-authentication.html
revdate: November 3, 2025
---

# User Authentication

The SCIM protocol doesn't define a method for authenticating a user. The PingOne for Enterprise Directory API uses the OAuth 2.0 Resource Owner Password Credential grant to facilitate user authentication.

To authenticate the user Meredith using her username and password, perform the following request:

```shell
curl -v -X POST --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-d "grant_type=password&username=marcher&password=2Federate"
https://directory-api.pingone.com/api/oauth/token
```

An HTTP `200 OK` response signals a successful login. Any other response is a failed authentication attempt.
