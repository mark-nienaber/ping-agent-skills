---
title: Access an identity&#8217;s profile
description: "Access an identity's profile in PingAM authentication tree nodes to read and write permanent data storage beyond session or node state"
component: pingam
version: 8.1
page_id: pingam:auth-nodes:access-identity-profile
canonical_url: https://docs.pingidentity.com/pingam/8.1/auth-nodes/access-identity-profile.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Extensibility", "Nodes &amp; Trees"]
section_ids:
  read_an_identitys_profile: Read an identity's profile
  read_attributes_of_an_identitys_profile: Read attributes of an identity's profile
  write_a_value_into_an_identitys_profile: Write a value into an identity's profile
---

# Access an identity's profile

AM allows a node to read and write data to and from an identity's profile. This is useful if a node needs to store information more permanently than when using either the authentication trees' `NodeState` or the identity's session.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any node that reads or writes to an identity's profile must only occur in a tree after the identity has been verified. For example, as the final step in a tree or directly after a [Data Store Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/data-store-decision.html).To store a verified identity in the journey session, call `ActionBuilder.withIdentifiedIdentity()`. This ensures identities with the same username are correctly resolved. |

## Read an identity's profile

Use the `IdUtils` static class:

```java
AMIdentity id = IdUtils.getIdentity(username, realm);
```

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | Use the [IdUtilsWrapper](../_attachments/apidocs/com/sun/identity/idm/IdUtilsWrapper.html) class to assist with testing. |

If AM is configured to search for the identity's profile using a different search attribute than the default, provide the attributes as a third argument to the method.

To obtain the attributes, you could request them in the configuration of the node or obtain them from the realm's authentication service configuration.

The following example demonstrates how to obtain the user alias:

```java
public AMIdentity getIdentityFromSearchAlias(String username, String realm) {
    ServiceConfigManager mgr = new ServiceConfigManager(
            ISAuthConstants.AUTH_SERVICE_NAME,
            AccessController.doPrivileged(AdminTokenAction.getInstance());

    ServiceConfig serviceConfig = mgr.getOrganizationConfig(realm, null);

    Set<String> realmAliasAttrs = serviceConfig.getAttributes()
        .get("iplanet-am-auth-alias-attr-name");

   return IdUtils.getIdentity(username, realm, realmAliasAttrs);
}
```

By combining these approaches, you can search for an identity by using the ID and whichever configured attribute field(s) as necessary.

## Read attributes of an identity's profile

After obtaining the profile, use the `AMIdentity.getAttribute(String name)` method.

## Write a value into an identity's profile

Create a `Map<String, Set<String>>` structure of the attributes you want to write, as follows:

```java
Map<String, Set<String>> attrs = new HashMap<>();
attrs.put("attribute", Collections.singleton("value"));
user.setAttributes(attrs);
user.store();
```
