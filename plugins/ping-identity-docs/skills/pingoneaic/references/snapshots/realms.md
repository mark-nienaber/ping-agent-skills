---
title: Alpha and Bravo realms
description: Explore the default Alpha and Bravo realms, delegated administration, and realm-specific features in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:realms:alpha-bravo-realms
canonical_url: https://docs.pingidentity.com/pingoneaic/realms/alpha-bravo-realms.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Administration", "Features", "Getting started", "Realms", "User Interface"]
section_ids:
  end_user_sign_in: End-user sign-in
  delegated_administration: Delegated administration
  assign_internal_roles: Assign internal roles
---

# Alpha and Bravo realms

The Alpha and Bravo realms are the two default realms that are included as part of an PingOne Advanced Identity Cloud tenant. These realms are configurable, unlike the top-level realm that Advanced Identity Cloud configures for tenant administrator identities.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud doesn't support more than two realms in the same tenant. Additionally, [delegated administration](#delegated_administration) and [Identity Governance](../identity-governance/administration/getting-started-what-is-iga.html)\[[1](#_footnotedef_1 "View footnote.")] are only supported in the Alpha realm.For customer identity and access management (CIAM) use cases, you can use either the Alpha or Bravo realm. |

## End-user sign-in

End users access their sign-in page using a URL that specifies the realm they belong to. For example:

* Alpha realm end users: https\://\<tenant-env-fqdn>/am/XUI/?**realm=alpha**\&authIndexType=service\&authIndexValue=Login

* Bravo realm end users: https\://\<tenant-env-fqdn>/am/XUI/?**realm=bravo**\&authIndexType=service\&authIndexValue=Login

Tenant administrators cannot authenticate using these realm-specific login URLs. Learn more in [Sign on to a tenant admin console](../tenants/tenant-administrator-settings.html#sign-on-to-a-tenant-admin-console).

## Delegated administration

In the Alpha realm, you can set up [internal roles](../identities/roles-assignments.html#internal_roles) for delegated administration using a custom set of privilege attributes.You can then assign those internal roles to users so that Alpha realm users can act as delegated administrators and perform actions on the custom set of attributes specified by the role.

The Bravo realm does not support delegated administration.

### Assign internal roles

You can assign the internal roles in two different ways using the Advanced Identity Cloud admin console:

* To add an internal role to a user, go to Identities > Manage > *Realm* - Users. Select a user, then select the Authorization Roles tab, then click + Add Authorization Roles.

* To add a user to an internal role, go to Identities > Manage > Internal Roles. Select a role, then select the Members tab, then click + Add Members.

In the Bravo realm, while you can set up internal roles for delegated administration, you cannot use them. Also, you cannot add a user to an internal role, and even though it appears possible to add an internal role to a user, this will not correctly link the user to the role. If you attempt this, the user will not be listed in the internal role Members tab.

The following table summarizes these differences:

| Action                                                            | Alpha Realm           | Bravo Realm                                                             |
| ----------------------------------------------------------------- | --------------------- | ----------------------------------------------------------------------- |
| Create internal role for the purposes of delegated administration | [icon: check, set=fa] | [icon: check, set=fa]                                                   |
| Add user to internal role                                         | [icon: check, set=fa] | [icon: times, set=fa]                                                   |
| Add internal role to user                                         | [icon: check, set=fa] | [icon: triangle-exclamation, set=fa] appears possible but will not work |

***

[1](#_footnoteref_1). IGA is an [add-on capability](../product-information/add-on-capabilities.html).
