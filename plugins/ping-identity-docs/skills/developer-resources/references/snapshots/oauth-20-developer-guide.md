---
title: API Developer Considerations
description: The API developer builds the API that the application talks to. This developer is concerned with the protection of the API calls made and determining whether a user is authorized to make a specific API call.
component: developer-resources
page_id: developer-resources:oauth_20_developer_guide:api-developer-considerations
canonical_url: https://docs.pingidentity.com/developer-resources/oauth_20_developer_guide/api-developer-considerations.html
revdate: September 30, 2020
---

# API Developer Considerations

The API developer builds the API that the application talks to. This developer is concerned with the protection of the API calls made and determining whether a user is authorized to make a specific API call.

The OAuth 2.0 process an API developer needs to handle is to:

* Validate a token

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In some cases the "API Developer" may be using a service bus or authorization gateway to manage access to APIs and therefore the task of validating the access token would be shifted to this infrastructure. |
