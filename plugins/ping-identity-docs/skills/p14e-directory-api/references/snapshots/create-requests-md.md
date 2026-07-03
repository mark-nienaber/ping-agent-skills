---
title: Creating Requests
description: A request consists of using the appropriate verb to call the SCIM resource endpoint (that is, User or Group). When modifying a resource directly, perform the action on the resources location URL (that is, the location attribute for a given resource).
component: p14e-directory-api
page_id: p14e-directory-api::create-requests
canonical_url: https://developer.pingidentity.com/p14e-directory-api/create-requests.html
revdate: November 3, 2025
---

# Creating Requests

A request consists of using the appropriate verb to call the SCIM resource endpoint (that is, User or Group). When modifying a resource directly, perform the action on the resources location URL (that is, the `location` attribute for a given resource).

Request authorization requires:

* Basic authorization

* A Base64 encoding of the client ID and API key displayed in the PingOne for Enterprise Directory user interface: **Setup** > **Directory** > **API Credentials**. Learn more in [View or renew directory API credentials](https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_view_renew_p1d_api_credentials.html) in the PingOne for Enterprise administration guide.

For example, `Basic base64encode(clientid:apiKey)`.

As an example, the following POST action to the user endpoint will create a new user in the directory:

```shell
curl -v -X POST --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -d '{
        "schemas":["urn:scim:schemas:core:1.0"],
        "userName":"marcher",
        "password":"2Federate",
        "active":true,
        "name":{ "familyName":"Archer", "givenName":"Meredith" },
        "emails": [ { "type": "work", "value": "meredith.archer@pingdevelopers.com }]
     }' \
     https://directory-api.pingone.com/api/directory/user
```