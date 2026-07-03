---
title: API Access Management
description: The PingOne Authorize API access management service provides tools to externalize the management and evaluation of access control policies for HTTP-based APIs. The access control policies defined in the API Service configuration are enforced through an API gateway, which delegates policy evaluation using a Ping Identity-provided integration kit that connects with the PingOne API.
component: pingone-api
page_id: pingone-api:authorize:api-access-management
canonical_url: https://developer.pingidentity.com/pingone-api/authorize/api-access-management.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# API Access Management

The PingOne Authorize API access management service provides tools to externalize the management and evaluation of access control policies for HTTP-based APIs. The access control policies defined in the API Service configuration are enforced through an API gateway, which delegates policy evaluation using a Ping Identity-provided integration kit that connects with the PingOne API.

The integration kit installed in your API gateway authenticates to PingOne. You configure a gateway and obtain a gateway credential. This credential is used to configure the API gateway integration kit. For more information, refer to [PingOne Authorize API Gateway Integration Kits](https://docs.pingidentity.com/pingone/authorization_using_pingone_authorize/p1az_api_gateway_is.html).

To create a gateway resource, refer to [Create API Gateway Integration](../platform/gateway-management/gateways/create-api-gateway-integration.html). In addition, API access management also uses the gateways credentials service. For more information, refer to [Gateway Credentials](../platform/gateway-management/gateway-credentials.html).
