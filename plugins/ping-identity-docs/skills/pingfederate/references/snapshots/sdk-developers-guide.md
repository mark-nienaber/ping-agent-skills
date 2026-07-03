---
title: "<code class=\"codeph\">IdentityStoreProvisionerWithFiltering</code> interface implementation"
description: Implement the IdentityStoreProvisionerWithFiltering interface to provision and deprovision users and groups to an external user store with list/query and filtering support.
component: pingfederate
version: 13.1
page_id: pingfederate:sdk_developers_guide:identitystoreprovisionerwithfiltering_interface_implemen
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/sdk_developers_guide/identitystoreprovisionerwithfiltering_interface_implemen.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  create-user: Create user
  read-user: Read user
  read-users: Read users
  update-user: Update user
  delete-user: Delete user
  pf_section_checkForGroupProvisioningSupport: Check for group provisioning support
  create-group: Create group
  read-group: Read group
  read-groups: Read groups
  update-group: Update group
  delete-group: Delete group
---

# `IdentityStoreProvisionerWithFiltering` interface implementation

Implement the `IdentityStoreProvisionerWithFiltering` interface to provision and deprovision users and groups to an external user store with list/query and filtering support.

|   |                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------- |
|   | If you do not need to support list/query and filtering, you can implement the `IdentityStoreProvisioner` interface instead. |

Implementing this interface requires the following Java packages:

* `com.pingidentity.sdk.provision`

* `com.pingidentity.sdk.provision.exception`

* `com.pingidentity.sdk.provision.users.request`

* `com.pingidentity.sdk.provision.users.response`

* `com.pingidentity.sdk.provision.groups.response`

* `com.pingidentity.sdk.provision.groups.request`

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | Group support is optional (see [Check for group provisioning support](#pf_section_checkForGroupProvisioningSupport)). |

For each identity store provisioner implementation, in addition to the methods described under [Shared plugin interfaces](pf_share_plugin_interface.html), you must implement the following:

* Create user

* Read user

* Read users (not applicable to the `IdentityStoreProvisioner` interface)

* Update user

* Delete user

* Check for group provisioning support

* Create group

* Read group

* Read groups (not applicable to the `IdentityStoreProvisioner` interface)

* Update group

* Delete group

## Create user

```
UserResponseContext createUser(CreateUserRequestContext createRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `createUser()` method of your identity store provisioner in response to create-user requests made to PingFederate services, such as inbound provisioning. This method creates the user in the user store managed by the identity store provisioner.

The `CreateUserRequestContext` contains all information needed to fulfill the request. If the user is successfully provisioned, the method returns a `UserResponseContext` containing the user attributes used to provision the user. The method throws an `IdentityStoreException` if an error occurred during the creation process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read user

```
UserResponseContext readUser(ReadUserRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readUser()` method of your identity store provisioner in response to get-user requests made to PingFederate services, such as inbound provisioning. This method retrieves user data from the user store managed by the identity store provisioner.

The `ReadUserRequestContext` contains all information needed to fulfill the request. If the user data is successfully retrieved, the method returns a `UserResponseContext` containing the user attributes for the user. The method throws an `IdentityStoreException` if an error occurred during the retrieval process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read users

```
UsersResponseContext readUsers(ReadUsersRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readUsers()` method of your identity store provisioner in response to list/query requests for user attributes made to PingFederate services, such as inbound provisioning. This method retrieves user data from the user store managed by the identity store provisioner.

|   |                                                                                                                                                              |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The `readUsers` method applies only to the `IdentityStoreProvisionerWithFiltering` interface; it does not apply to the `IdentityStoreProvisioner` interface. |

The `ReadUsersRequestContext` contains all information needed to fulfill the request. If the user data is successfully retrieved, the method returns a `UsersResponseContext` containing the user attributes satisfying the filter. If an error occurred during the retrieval process, the method returns an `IdentityStoreException` . See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Update user

```
UserResponseContext updateUser(UpdateUserRequestContext updateRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `updateUser()` method of your identity store provisioner in response to update-user requests made to PingFederate services, such as inbound provisioning. This method updates the user in the user store managed by the identity store provisioner.

The `UpdateUserRequestContext` contains all information needed to fulfill the request. If the user data is successfully updated, the method returns a `UserResponseContext` containing the user's updated attributes. The method throws an `IdentityStoreException` if an error occurred during the update process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Delete user

```
void deleteUser(DeleteUserRequestContext deleteRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `deleteUser()` method of your identity store provisioner in response to delete-user requests made to PingFederate services, such as inbound provisioning. This method deprovisions the user in the user store managed by the identity store provisioner.

The `DeleteUserRequestContext` contains all information needed to fulfill the request. The method throws an `IdentityStoreException` if an error occurred during the deprovision process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The plugin implementation can choose not to permanently delete the resource, but must return a `NotFoundException` for all `readUser()`, `updateUser()`, and `deleteUser()` operations associated with the previously deleted ID. In addition, the plugin must not consider the deleted user in conflict calculation. For example, a `createUser()` request for a user with a previously deleted ID should not throw a `ConflictException`. |

## Check for group provisioning support

```
boolean isGroupProvisioningSupported()
throws IdentityStoreException
```

Implement the `isGroupProvisioningSupported()` method to return true if group provisioning is supported by your identity store provisioner or false otherwise. The method throws an `IdentityStoreException` if an error occurred during the query process. See `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Create group

```
GroupResponseContext createGroup(CreateGroupRequestContext createRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `createGroup()` method of your identity store provisioner in response to create-group requests made to PingFederate services, such as inbound provisioning. This method creates the group in the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` method returns true; otherwise, it should throw `NotImplementedException`.

The `CreateGroupRequestContext` contains all information needed to fulfill the request, such as group attributes. If the group is successfully provisioned, the method returns a `GroupResponseContext` containing the group attributes used to provision the group. The method throws an `IdentityStoreException` if an error occurred during the creation process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read group

```
GroupResponseContext readGroup(ReadGroupRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readGroup()` method of your identity store provisioner in response to get-group requests made to PingFederate services, such as inbound provisioning. This method retrieves group data from the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` returns true; otherwise, it should throw `NotImplementedException`.

The `ReadGroupRequestContext` contains all information needed to fulfill the request, such as group ID. If the group data is successfully retrieved, the method returns a `GroupResponseContext` containing the group attributes. The method throws an `IdentityStoreException` if an error occurred during the retrieval process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Read groups

```
GroupsResponseContext readGroups(ReadGroupsRequestContext readRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `readGroups()` method of your identity store provisioner in response to list/query requests for group attributes made to PingFederate services, such as inbound provisioning. This method retrieves group data from the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` returns true; otherwise, it should throw `NotImplementedException`.

|   |                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `readGroups` method applies only to the `IdentityStoreProvisionerWithFiltering` interface; it does not apply to the `IdentityStoreProvisioner` interface. |

The `ReadGroupsRequestContext` will contain all information needed to fulfill the request (for example, a filter). If the group data was successfully retrieved, a `GroupsResponseContext` should be returned and contain the group attributes for the groups. An `IdentityStoreException` should be thrown if an error occurred during the retrieval process. See `com.pingidentity.sdk.provision.exception` package for different exceptions that can be thrown.

## Update group

```
GroupResponseContext updateGroup(UpdateGroupRequestContext updateRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `updateGroup()` method of your identity store provisioner in response to update-group requests made to PingFederate services, such as inbound provisioning. This method updates the group in the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` method returns true; otherwise, it should throw `NotImplementedException`.

The `UpdateGroupRequestContext` contains all information needed to fulfill the request, such as group attributes. If the group data is successfully updated, the method returns a `GroupResponseContext` containing the group's updated attributes. The method throws an `IdentityStoreException` if an error occurred during the update process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.

## Delete group

```
void deleteGroup(DeleteGroupRequestContext deleteRequestCtx)
throws IdentityStoreException
```

PingFederate invokes the `deleteGroup()` method of your identity store provisioner in response to delete-group requests made to PingFederate services, such as inbound provisioning. This method deprovisions the group in the user store managed by the identity store provisioner if the `isGroupProvisioningSupported()` returns true; otherwise, it should throw `NotImplementedException`.

The `DeleteGroupRequestContext` contains all information needed to fulfill the request, such as a group ID. The method throws an `IdentityStoreException` if an error occurred during the deprovisioning process. See the `com.pingidentity.sdk.provision.exception` package for exceptions that can be thrown.
