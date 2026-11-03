---
title: User management
description: The Zoom Provisioner links users from the datastore to Zoom. The following describes the behavior of each provisioning capability.
component: zoom
page_id: zoom::pf_zoom_connector_user_management
canonical_url: https://docs.pingidentity.com/integrations/zoom/pf_zoom_connector_user_management.html
llms_txt: https://docs.pingidentity.com/integrations/zoom/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 5, 2025
section_ids:
  synchronizing-existing-users: Synchronizing existing users
  user-provisioning: User provisioning
  user-updates: User updates
  user-deprovisioning: User deprovisioning
---

# User management

The Zoom Provisioner links users from the datastore to Zoom. The following describes the behavior of each provisioning capability.

## Synchronizing existing users

By default, the provisioning connector synchronizes users from the datastore to the target service by matching the `mail` attribute in the datastore to the `Username` attribute in the target service. You can change the default mapping in [Creating a provisioning connection](setup/pf_zoom_connector_creating_a_provisioning_connection.html).

For example:

* In the target service, Janet's `Username` is `jsmith@example.com`.

* In your datastore, Janet's `mail` is `jsmith@example.com`.

* On the **Attribute Mapping** tab of your PingFederate channel configuration, you map the `Username` attribute to `mail`.

* When the provisioning connector runs, the datastore user is provisioned with a `Username` of `jsmith`. That matches Janet's existing `Username` in the target service, so her information in the datastore is synchronized to her target service account.

## User provisioning

User provisioning is triggered when a user is added to the datastore group or filter targeted by the provisioning connector.

The target is determined by the **Source Location** tab in the provisioning connection configuration.

## User updates

User updates are triggered when a change occurs to a user attribute mapped in the provisioning connector configuration.

## User deprovisioning

User deprovisioning is triggered by any of the following:

* A user is deleted from the user store.

* A user is disabled in the user store.

* A user is removed from the data store filter targeted by the provisioning connector.

The **Remove User Action** setting in the connection configuration determines whether the deprovisioning action disables or deletes the user.