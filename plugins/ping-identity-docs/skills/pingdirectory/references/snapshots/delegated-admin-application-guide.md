---
title: Configuring a resource&#8217;s summary display in the Delegated Admin GUI
description: The Delegated Admin GUI provides a summary of attributes for a resource. For example, the user and group resource profiles show a summary.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_config_resource_summary_display_gui
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_config_resource_summary_display_gui.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 20, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring a resource's summary display in the Delegated Admin GUI

The Delegated Admin GUI provides a summary of attributes for a resource. For example, the user and group resource profiles show a summary.

## About this task

By default, a resource's summary shows all required attributes and all search attributes for the resource. However, you can explicitly set the items to include in the summary.

If you configure any attributes to appear in the summary, the default selection does not appear.

To configure an attribute to appear in the summary, either use `dsconfig` to set the `include-in-summary` property or use the PingDirectory admin console to select the **Include In Summary** checkbox.

## Steps

* For a given resource, configure each attribute to include in the summary.

  ### Choose from:

  * Use `dsconfig`.

    Use the `set-delegated-admin-attribute-prop` subcommand, where *\<name\_of\_type>* is the resource type and *\<type\_of\_attribute>* is the name of an existing attribute for the given resource.

    ```shell
    $ bin/dsconfig set-delegated-admin-attribute-prop \
      --type-name  <name_of_type>  \
      --attribute-type  <type_of_attribute>  \
      --set include-in-summary:true
    ```

    The following example includes the `cn` attribute in the summary for the `users` resource type:

    ```shell
    $ bin/dsconfig set-delegated-admin-attribute-prop \
      --type-name users \
      --attribute-type cn \
      --set include-in-summary:true
    ```

    |   |                                                                                             |
    | - | ------------------------------------------------------------------------------------------- |
    |   | To remove an attribute from the summary, use the same command but change `true` to `false`. |

  * Use the PingDirectory admin console.

    1. Sign on to the PingDirectory admin console.

    2. From the **Configuration** page, click **REST Resource Types**.

    3. To edit a resource type, select it from the **Name** column.

    4. Go to the **Delegated Admin Attributes** section.

    5. To edit an attribute, click the **Pencil** icon.

    6. Select the **Include In Summary** checkbox.

       |   |                                                                                     |
       | - | ----------------------------------------------------------------------------------- |
       |   | To remove an attribute from the summary, clear its **Include In Summary** checkbox. |

---

---
title: Uploading a certificate to a user REST resource type profile in Delegated Admin
description: After you have enabled the certificate upload feature, you can use it to add a certificate to a new or existing user REST Resource type profile in Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_upload_user_cert
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_upload_user_cert.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_da_upload_cert_new_user.adoc", "pd_da_upload_cert_existing_user.adoc"]
section_ids:
  uploading-a-certificate-to-a-new-user-profile-in-delegated-admin: Uploading a certificate to a new user profile in Delegated Admin
  about-this-task: About this task
  steps: Steps
  uploading-a-certificate-to-an-existing-user-profile-in-delegated-admin: Uploading a certificate to an existing user profile in Delegated Admin
  about-this-task-2: About this task
  steps-2: Steps
---

# Uploading a certificate to a user REST resource type profile in Delegated Admin

After you have enabled the certificate upload feature, you can use it to add a certificate to a new or existing user REST Resource type profile in Delegated Admin.

|   |                                                                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must enable the certificate upload feature before you can use it in the Delegated Admin application. For more information and to enable the feature, see [Enabling the Delegated Admin user REST resource type certificate upload feature](pd_da_enable_user_cert_upload.html). |

## Uploading a certificate to a new user profile in Delegated Admin

You can upload a certificate to a new user profile in the Delegated Admin application.

### About this task

To add a certificate to a new user profile in the Delegated Admin application:

### Steps

1. Click **Users → Manage Users**.

2. Click **New Users**.

   ![A screen capture showing the Delegated Admin application Manage Users screen with New Users highlighted.](_images/fry1654027616013.png)

3. To add a certificate, click **Choose a File**.

   ![A screen capture showing the Delegated Admin application New User page with Choose a File highlighted.](_images/jlu1654036460220.png)

4. Complete all other required fields for the new user.

5. Click **Save**.

## Uploading a certificate to an existing user profile in Delegated Admin

You can upload a certificate to an existing user profile in the Delegated Admin application.

### About this task

To add a certificate to an existing user profile in the Delegated Admin application:

### Steps

1. Click **Users → Manage Users**.

2. To locate the user, enter the user information in the search field.

3. Click the **Expand** icon on the user profile.

4. To edit the profile, click the **Pencil** icon.

5. To add a certificate, click **Choose a File** and select a certificate file.

6. Click **Save**.

---

---
title: Uploading a photo to a user REST resource type profile in Delegated Admin
description: After you have enabled the photo upload feature, you can use it to add a photo to a new or existing user REST resource type profile in Delegated Admin.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_upload_user_photo
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_upload_user_photo.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_da_upload_photo_new_user.adoc", "pd_da_upload_photo_existing_user.adoc"]
section_ids:
  uploading-a-photo-to-a-new-user-profile-in-delegated-admin: Uploading a photo to a new user profile in Delegated Admin
  about-this-task: About this task
  steps: Steps
  uploading-a-photo-to-an-existing-user-profile-in-delegated-admin: Uploading a photo to an existing user profile in Delegated Admin
  about-this-task-2: About this task
  steps-2: Steps
---

# Uploading a photo to a user REST resource type profile in Delegated Admin

After you have enabled the photo upload feature, you can use it to add a photo to a new or existing user REST resource type profile in Delegated Admin.

|   |                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You must enable the photo upload feature before you can use it in the Delegated Admin application. For more information and to enable the feature, see [Enabling the Delegated Admin user REST resource type photo upload feature](pd_da_enable_user_profile_photo_upload.html). |

## Uploading a photo to a new user profile in Delegated Admin

### About this task

To add a photo to a new user profile in the Delegated Admin application:

### Steps

1. Click **Users → Manage Users**.

2. Click **New Users**.

   ![A screen capture showing the Delegated Admin application Manage Users screen with New Users highlighted.](_images/fry1654027616013.png)

3. To add a photo, click the **[icon: plus, set=fa]**icon and select a photo.

   ![A screen capture showing the Delegated Admin application New User page with the add photo icon highlighted.](_images/dpi1654027828196.png)

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Because of a server limitation, only a thumbnail of the photo and not the file name is displayed after the upload.The maximum photo size is 4MB. |

4. Complete all other required fields for the new user.

5. Click **Save**.

## Uploading a photo to an existing user profile in Delegated Admin

### About this task

To add a photo to an existing user profile in the Delegated Admin application:

### Steps

1. Click **Users → Manage Users**.

2. To locate the user, enter the user information in the search field.

3. Click the **Expand** icon on the user profile.

4. To edit the profile, click the **Pencil** icon.

5. (Optional) If you already have a photo and want to replace it, click **Remove** to remove the original photo.

6. To add a photo, click the **[icon: plus, set=fa]**icon and select a photo.

   |   |                                                                                                                                                  |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | Because of a server limitation, only a thumbnail of the photo and not the file name is displayed after the upload.The maximum photo size is 4MB. |

7. Click **Save**.

---

---
title: Users and groups
description: You can configure delegated administrators to manage users and groups in the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_users_groups
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_users_groups.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Users and groups

You can configure delegated administrators to manage users and groups in the PingDirectory server.

Configuring delegated administrators involves the following:

* Create new entries.

* Read, view, and search existing entries.

* Edit and update existing entries.

* Edit referenced items.

  For example, if a delegated administrator is viewing an item that references a user, the delegated administrator can edit that user's information inline.

The following sections describe users and groups in more detail.

---

---
title: Viewing groups
description: Use the group reference right to grant delegated admins the right to see what groups a user is a member of without granting group resource management rights.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:pd_da_viewing_groups
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/pd_da_viewing_groups.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  about-this-task: About this task
  steps: Steps
  result: Result
---

# Viewing groups

Use the group `reference` right to grant delegated admins the right to see what groups a user is a member of without granting group resource management rights.

## About this task

To grant a delegated admin the group `reference` right:

## Steps

* Run `dsconfig` with the `create-delegated-admin-resource-rights` option.

  ```
  dsconfig create-delegated-admin-resource-rights \
      --rights-name DArights  \
      --rest-resource-type groups  \
      --set enabled:true  \
      --set admin-permission:reference  \
      --set admin-scope:all-resources-in-base
  ```

## Result

The admin can see the user's group memberships on the entry preview's **Group Membership** tab.

---

---
title: Working with correlated REST resources
description: You can link resource types based on a common attribute value. When two or more resources are linked this way, they are known as correlated resources.
component: pingdirectory
version: 11.1
page_id: pingdirectory:delegated_admin_application_guide:ds_da_correlated_rest_resources
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/delegated_admin_application_guide/ds_da_correlated_rest_resources.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 19, 2023
section_ids:
  correlated-rest-resources: Correlated REST resources
  configuration: Configuration
  linking-and-unlinking: Linking and unlinking
  permissions: Permissions
---

# Working with correlated REST resources

You can link resource types based on a common attribute value. When two or more resources are linked this way, they are known as correlated resources.

## Correlated REST resources

When you retrieve a resource configured with correlated resources, any correlated resource with matching attribute values is included with the resource.

You can view, update, and delete a resource's correlated resources. You can also link them to and unlink them from a resource.

## Configuration

The following example shows how to create a correlated resource by linking a `documents` resource type to a `users` resource type. When a user resource is retrieved, any document resources with the user's `entryUUID` in their `documentPublisher` attribute are included.

```
dsconfig create-delegated-admin-correlated-rest-resource \
    --type-name users  \
    --resource-name Documents  \
    --set display-name:Documents  \
    --set correlated-rest-resource:Documents  \
    --set primary-rest-resource-correlation-attribute:entryUUID  \
    --set secondary-rest-resource-correlation-attribute:documentPublisher
```

## Linking and unlinking

You can link resources to correlated resources by taking an attribute value from either the primary resource or the correlated resource and assigning it to the other. To control the direction that the linking value is assigned, use the `use-secondary-value-for-linking` property. If `use-secondary-value-for-linking `is `false` or isn't set, the primary correlation attribute's value is assigned to the secondary correlation attribute to create the link. If `use-secondary-value-for-linking `is `true`, the secondary correlation attribute's value is assigned to the primary correlation attribute.

The following is an example of a `users` resource type linked to a `documents` resource type by assigning the document's `entryUUID` value to the user's `description` attribute. The secondary correlation attribute's value is assigned to the primary correlation attribute, so `use-secondary-value-for-linking` is `true`.

```
dsconfig create-delegated-admin-correlated-rest-resource \
    --type-name users  \
    --resource-name ownedDocuments  \
    --set display-name:Owned Documents  \
    --set correlated-rest-resource:Documents  \
    --set primary-rest-resource-correlation-attribute:description  \
    --set secondary-rest-resource-correlation-attribute:entryUUID  \
    --set use-secondary-value-for-linking:true
```

If you inspected a user's `description` attribute with this setup, you see a list of all of the documents owned by the user.

The next example links the attributes in the other direction. Here, the user's `entryUUID` value is assigned to the `documentAuthor` attribute on the document.

```
dsconfig create-delegated-admin-correlated-rest-resource \
    --type-name users  \
    --resource-name authoredDocuments  \
    --set display-name:Authored Documents  \
    --set correlated-rest-resource:Documents  \
    --set primary-rest-resource-correlation-attribute:entryUUID  \
    --set secondary-rest-resource-correlation-attribute:documentAuthor  \
    --set use-secondary-value-for-linking:false
```

If you inspect a document's `documentAuthor` attribute with this setup, you see a list of all of the users who authored the document.

You can also unlink correlated resources from the primary resource. Resources are unlinked by removing the common attribute value using the logic based on the `use-secondary-value-for-linking` property described above.

Unlinking correlated resources differs from deleting correlated resources. When correlated resources are unlinked, the common attribute value is removed, but the correlated resource still exists in the directory. When a correlated resource is deleted, it is removed from the directory.

The attribute that the linking value is assigned to must be a writable attribute because the value must be updated to link and unlink correlated resources. The attributes should also have the same syntax so that the value of one can be assigned to the other successfully.

|   |                                                                                                                                                                                                                                                                                                                                               |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When `use-secondary-value-for-linking` is enabled and a linked object is deleted, the linking value is not removed from the primary correlation attribute. This means that if a secondary object is recreated with the same value in the secondary correlation attribute, the secondary object is automatically linked to the primary object. |

## Permissions

The following table describes the permissions required to perform the specified actions.

| Action         | Permissions required                                                                                                                                                                                                                                                                                                                                                   |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| View           | The `read` permission on the secondary resource type.                                                                                                                                                                                                                                                                                                                  |
| Update         | The `update` or `update-profile` permission on the secondary resource type.                                                                                                                                                                                                                                                                                            |
| Delete         | The `delete` permission on the secondary resource type.                                                                                                                                                                                                                                                                                                                |
| Link or unlink | The `update` or `update-profile` permission.&#xA;&#xA;The required permission is dependent on the use-secondary-value-for-linking setting. If use-secondary-value-for-linking is set to false, the permission is required on the correlated resource type. If use-secondary-value-for-linking is set to true, the permission is required on the primary resource type. |