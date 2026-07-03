---
title: Native SDKs
description: The PingOne Native SDKs are iOS and Android client SDKs for PingOne services built to interact with the PingOne Platform API. Currently, native PingOne SDKs are available for these services:
component: pingone-api
page_id: pingone-api:native-sdks:introduction
canonical_url: https://developer.pingidentity.com/pingone-api/native-sdks/introduction.html
llms_txt: https://developer.pingidentity.com/pingone-api/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["index.adoc"]
section_ids:
  assigning-admin-roles-and-permissions-to-this-service: Assigning admin roles and permissions to this service
---

# Native SDKs

The PingOne Native SDKs are iOS and Android client SDKs for PingOne services built to interact with the PingOne Platform API. Currently, native PingOne SDKs are available for these services:

* [PingOne MFA](pingone-mfa-mobile-sdks.html)

* [PingOne Neo](pingone-neo-native-sdks.html)

* [PingOne Protect](pingone-risk-sdks/risk_evaluation_sdk.html)

To integrate your mobile and web apps with PingOne DaVinci, or for OIDC redirect login, refer to the [Ping SDKs](https://docs.pingidentity.com/sdks/latest/index.html).

## Assigning admin roles and permissions to this service

Admin role assignments determine access to PingOne APIs. When assigning admin roles to this service, refer to [PingOne Permissions by Service](../platform/reference/roles-and-permissions-in-pingone/permissions-by-service.html) for the service-specific permissions.

You can also choose to assign admin roles based on particular service resources. Refer to [PingOne Permissions by Resource](../platform/reference/roles-and-permissions-in-pingone/permissions-by-resource.html) when assigning admin roles per service resources.

Admin assignments to roles are set by:

* [Automatic assignment for some roles](../platform/roles/predefined-roles.html#automatic-role-assignment).

* [Group Role Assignments](../platform/group-role-assignments/group-role-assignments.html).

* [User Role Assignments](../platform/users/user-role-assignments.html).

Refer to [Roles Management](../platform/roles.html) for more information.
