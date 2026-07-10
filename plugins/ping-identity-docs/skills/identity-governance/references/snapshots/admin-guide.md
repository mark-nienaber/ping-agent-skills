---
title: Access Request
description: The View All Requests page allows administrators to view all requests across the entire application, either in progress or completed.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:chap-access-request
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/chap-access-request.html
section_ids:
  view_all_requests: View All Requests
  requests_table: Requests Table
  table_filters: Table Filters
  request_information: Request Information
  request_item_history: Request Item History
  action_buttons: Action Buttons
  bulk_cancelling_requests: Bulk Cancelling Requests
  bundle_editor: Bundle Editor
  requestable_bundle_table: Requestable Bundle Table
  bundle_search: Bundle Search
  deleting_bundles: Deleting Bundles
  create_bundle: Create Bundle
  editing_a_bundle: Editing a Bundle
  request_fields: Request Fields
  request_fields_table: Request Fields Table
  deleting_request_fields: Deleting Request Fields
  create_request_field_form: Create Request Field Form
  assigning_request_fields_to_items: Assigning Request Fields to Items
  defining_requestable_items: Defining Requestable Items
  access_request_glossary_keys: Access Request Glossary Keys
  standard_request_workflow: Standard Request Workflow
  approval_process: Approval Process
  request_flow: Request Flow
  custom_workflows: Custom Workflows
  defining_a_custom_workflow_on_a_glossary_entry: Defining a Custom Workflow on a Glossary Entry
  creating_a_custom_approval_process_with_bpmn_workflow: Creating a Custom Approval Process with BPMN Workflow
  creating_a_custom_approval_process_via_script: Creating a Custom Approval Process via Script
  access_request_notifications: Access Request Notifications
  modifying_notification_templates: Modifying Notification Templates
---

# Access Request

## View All Requests

The View All Requests page allows administrators to view all requests across the entire application, either in progress or completed.

![iga admin view all requests](_images/iga-admin-view-all-requests.png)

## Requests Table

The table includes the following columns:

* Requestee - user for whom the access is requested

* Requester - user who submitted the request

* Request Date - date the request was submitted

* Item(s) - items that are included as part of the request

## Table Filters

The requests table can be filtered using any of the following options:

* Status:

  * In Progress - Shows all in-flight request that are still waiting on one or more user approvals to be processed

  * Complete - All previously completed requests that have either been completed by all necessary approvers or cancelled by the requester or an administrator.

* Requester: Select a user using the typeahead input box above the column label to display only requests where they are the requester.

* Requestee: Select a user using the typeahead input box above the column label to display only requests where they are the requestee.

* Item: Select a requestable item using the typeahead input box above the column label to display only requests targeting a specific item.

* Request Date: Not specifically a filter, however the current list of results within the table can be sorted by request date, either ascending or descending, by clicking on the column label "Request Date."

* Table Pagination: The requests table allows the user to choose the amount of rows they would like to see within the page of results (10, 20, or 30.) The user has the ability to scroll through subsequent pages of request results by clicking the navigation arrows to move forward or backward.

  ![iga pagination controls](_images/iga-pagination-controls.png)

## Request Information

Clicking on an individual request opens an extended panel showing the entire request process, grouped by each individual approval task.

![iga expanded request view](_images/iga-expanded-request-view.png)

The expanded view of a request shows a list of all of the items that are included as part of a request. Each line includes the following information:

* Item - The display name of the item

  ![iga requestable item information](_images/iga-requestable-item-information.png)

* Info Icon - Get more information on the requested item. Hovering over this icon expands a page containing all displayable metadata for the item.

  ![iga requestable item info dialog](_images/iga-requestable-item-info-dialog.png)

* Remove Icon - Any requested item that was requested to be removed has a small, red minus icon next to its info icon.

* Status - The current approval outcome of each item

  * Pending - Item request is in-progress and still awaiting action by one or more approvers.

  * Denied - Item has been rejected during one of its approval tasks.

  * Provisioned - Item has completed its approval chain, and has been successfully provisioned to the user.

  * Not Provisioned - Item has completed its approval chain, but has not been provisioned to the user. This means one of the following has occurred:

    * An error during provisioning

    * The user already had the specific access requested

    * The item has a manual provisioning task, which the provisioner completed as "Not Provisioned"

  * Cancelled - Request has been cancelled before this item has completed its approval process.

* Comment Icon - Clicking this icon allows the user to add a comment to the given item's history.

## Request Item History

In addition to the information presented initially, each individual line item can be clicked and expanded to reveal a chronological history of the actions taken as part of that item's approval process. This includes comments made, approval task information, reassign or consult actions, file uploads, and more.

![iga expanded history view for requestable item](_images/iga-expanded-history-view-for-requestable-item.png)

The history view is organized as a table that includes the following columns:

* User - The user who took the specified action on the item. In the event that the system acts directly on the request, for example during a task expiration, this column reads "SYSTEM."

* Action - The action taken on the request. Possible values are listed below

  * Pending - An in progress approval task awaiting action

  * Approved - A completed approval task that was manually approved

  * Rejected - A completed approval task that was manually rejected

  * Auto-approved - A completed approval task that was auto-approved

  * Auto-provisioned - Indicator that item required no approval

  * Cancelled - A completed approval task that was cancelled in-progress

  * Comment - A generic comment referencing the item

  * Consult - Indicator that a consult was added to an approval task

  * Upload - Information on an uploaded file

  * Reassign - Information on a reassigned task

* Date - The date and time the action took place

* Content - The content of the action, which varies depending on the specific action. It provides additional details as to what took place. Note that entries into this table for approval task completion may or may not have additional content to display.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Any approval task that is currently pending/in-progress for the given item always appears at the top of the item's history and is listed as pending. |

## Action Buttons

Administrators also have access to take certain actions on individual requests via the row of action buttons found at the bottom of the expanded view. Each action is detailed below:

![iga action buttons expanded request view](_images/iga-action-buttons-expanded-request-view.png)

* Cancel Request - Cancel the request, including all currently in-progress tasks. The administrator is asked to confirm the action before it is completed. Note that any item in a given request that already has a finalized outcome (Provisioned, Not Provisioned, Denied, etc.) won't be affected by a cancellation. Once an item is complete, the provisioning action can not be reversed.

* Attachments - Allows the user to view the current list of attachments assigned to this request, download any of those files, or upload a new file.

![iga attachments dialog](_images/iga-attachments-dialog.png)

If there are any files attached to the request, the files table appears at the top of the page. This table consists of three columns: \* Filename - Name of the uploaded file \* File Owner - User who uploaded the file to the request \* Action Buttons **Download Icon - Click to download the file to your local machine **Delete Icon - Click to remove the file from the request

You can find the form to upload files at the bottom of the page. To choose the file you want to upload, click on the Select File button to open up a file picker screen. Once you've selected the file, the name of the file chosen appears next to the Select File button in the form. Finally, clicking on the Upload button to the right will complete the action and save the file to the request.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | For requests with multiple items, it is possible to "attach" a file to only certain items within the request, so that the file is only visible to those approvers who need to see its contents, and not available to approvers who may not be responsible for that specific item. In these cases, there is an extra input as part of the upload form, that allows the uploader to select the items that the file is relevant to. |

* Reassign - Administrators have the ability to reassign any task that is currently awaiting approval as part of a request. Clicking on the Reassign button pops up a page form for reassigning tasks. Users can choose between reassigning a task to a user or a role/group. Once chosen, the typeahead box below allows for searching the system for the desired assignee. When the option has been selected, clicking Submit will start the reassignment process.

  ![iga reassignment dialog](_images/iga-reassignment-dialog.png)

Some requests may have more than one active approval task that is eligible to be reassigned. In this case, there is an additional selection to be made at the top of the request form for determining which approver's task should be reassigned with this action.

![iga reassignment dialog choose specific task](_images/iga-reassignment-dialog-choose-specific-task.png)

* Consult - Administrators have the ability to add a consult to any task that is currently awaiting approval as part of a request. The interface for adding a consult mirrors the reassign functionality shown above.

## Bulk Cancelling Requests

When viewing in-progress requests, you have the ability to select one (or more) requests and cancel them in bulk. To do so, simply click the checkbox next to the request(s) you wish to cancel and click the 'Cancel Request' button at the top left of the requests page. You are asked to confirm your decision and then receives a confirmation message when the request cancellation process is complete.

![iga selecting requests for cancellation](_images/iga-selecting-requests-for-cancellation.png)

|   |                                                                                                                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | As mentioned above, if you cancel a request in which one or more of the items have already been provisioned, those items remain provisioned. Items are provisioned as their individual approval chains are completed, and at that point are considered final. Any items that were still awaiting any further approvals won't be provisioned. |

## Bundle Editor

Administrators are granted the ability to create a requestable bundle of individual items, that can be submitted as part of a new request as a single package. Each individual item that is contained within a bundle still retains all of its original requirements for approval, notably its individual approval chain; however, it allows for the end user to submit multiple related items simultaneously, without the need for locating and adding each individually.

![iga bundle editor interface](_images/iga-bundle-editor-interface.png)

## Requestable Bundle Table

After navigating to the Bundle Editor interface, the administrator is presented with a table that displays all of the existing bundles within the system. The table includes two columns for each bundle:

![iga requestable item bundle table](_images/iga-requestable-item-bundle-table.png)

* Name: The name given to the bundle of items

* Description: The description and/or purpose of the bundle

## Bundle Search

The table also allows the user to search the list of bundles by using the table's filter box. This search feature works against both the Name and Description fields of the requestable bundle and returns all matches.

|   |                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The bundle table is not currently searchable based off of the items that are included within the bundle; therefore, when creating a new bundle it is highly recommended that you leverage the description to provide sufficient information on which to search for the bundle. |

## Deleting Bundles

The Bundle table allows the administrator to select one or more bundles at a time and delete them from the system. Simply check off any of the bundles that you wish to remove, and select the delete button on the top right of the table. Bundle deletion is permanent, and the only way to recover a deleted bundle is to recreate it manually.

|   |                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deleting a bundle won't affect any current in-progress requests that were created using that bundle. Those requests maintain their state and continues without any issue. |

## Create Bundle

By clicking on the new button on the bundle editor page, the administrator is able to enter information into the Edit Bundle form on the right side of the page to create a new bundle. There are three fields available:

* Name: The name given to the bundle of items

* Description: The description and/or purpose of the bundle

* Items: The requestable items that are included in any request that contains this bundle

Both the name and description fields are simple text boxes. To search for items to add to the bundle, begin by typing the desired item's name within the items input box. As you type, you see a dropdown menu appear with selectable options that match the input that you've entered. Click on any of the available requestable items to add them to the current bundle form. Once added, clicking on the item display name in the input box will display further information about the item in a pop-up page.

Once all of the desired information is set within the form, clicking Save at the bottom of the form saves the bundle to the database and makes it available for viewing within the bundle table on the left.

## Editing a Bundle

To edit an existing bundle, search and find the desired bundle within the bundle table. Once found, clicking the bundle's row within the table populates the Edit Bundle form page. The information can then be edited as needed, including the addition or removal of individual items.

![iga editing an existing bundle](_images/iga-editing-an-existing-bundle.png)

## Request Fields

Request fields are the building blocks that allow administrators to define custom request forms for individual requestable items. This screen allows administrators to create, manage, and delete fields from the application.

### Request Fields Table

The table allows the admin to search the list of request fields by using the table's filter box. This search feature works against both the Name and Description fields of the request field items and returns all matches, paginated.

![iga request fields table](_images/iga-request-fields-table.png)

### Deleting Request Fields

The Request Field table allows the administrator to select one or more fields at a time and delete them from the system. Simply check off any of the fields that you wish to remove, and select the delete button on the top right of the table. Request field deletion is permanent, and the only way to recover a deleted field is to recreate it manually.

|   |                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Deleting a request field won't affect any current in-progress requests that were created using that field. Those requests maintain their state and continues without any issue. Furthermore, any item that is leveraging a request field that has been deleted will simply ignore that field for any new requests, and will automatically reference that field again if it is recreated with the same name. |

## Create Request Field Form

By clicking on the new button on the editor page, the administrator is able to enter information into the Request Field form on the right side of the page to create a new entry.

![iga create request field form](_images/iga-create-request-field-form.png)

The following fields are available:

* Field Name: The name given to the request field (this is the key referenced on each requestable item's `requestFields` key.)

* Field Type: The type of input used for this field. Choose from the following options:

  * Text

  * Select

  * Typeahead

  * Radio

  * Checkbox

  * Datepicker

  * File

* Description: The description and/or purpose of the request field.

* Required: Whether or not this field is required for any requestable item that includes it. For those fields that may be required for some forms and not for others, it is recommended to create two distinct fields.

* Available Options (for Field Types of radio, select, and checkbox): Used to define the items to choose from for those input types with distinct options. Enter in the value of the option in the underlined text field, and click the '+' icon to add the option to the list. To remove an entry, click the 'x' icon next the the field value within the list.

  ![iga request field form available options](_images/iga-request-field-form-available-options.png)

Once all of the desired information is set within the form, clicking Save at the bottom of the form saves the Request Field to the database and appears within the main table.

## Assigning Request Fields to Items

To assign Request Fields to a requestable item, the requestFields key must be added to the glossary entry for that item. This is a reserved key on any entry, and is always of type array. Once created, the `requestFields` uses a custom interface to assign the available fields to that item.

![iga requestFields key on glossary](_images/iga-requestFields-key-on-glossary.png)

To assign existing Request Fields to the open entry, simply select (or optionally filter the options first) an entry on the left side of the form, which moves it to the selected section on the right. Once all the desired fields are attached to the requestable item, click Save to close the page and keep your changes. Note: The order of the fields added to this array key is respected in the Create New Request interface.

![iga request fields create request form](_images/iga-request-fields-create-request-form.png)

## Defining Requestable Items

The Identity Glossary is where glossary administrators are responsible for creating and defining what items are eligible to be requested within the application, what approval process they follow, and any additional data that may or may not affect the request. In order for an object within the PingIDM environment to be requestable, it must have a glossary entry that meets ALL of the following requirements:

For entries of type: \* Object **Must be an existing managed object within PingIDM **The managed user schema must include a relationship property between itself and the managed object type of the item (default property used is roles) \*\* If using a managed user property other than the defined default (roles), the glossary item must specify the desired user property name with the userProvisionProperty key.

* Identity-Value

  * The key attributeName must be an existing non-relationship property on the managed user schema.

* System-Value

  * Must have either a provisioner key or a provisionScript key on the item. As these entries do not reference a direct PingIDM user property, they must have a manual provisioning step. The provisioner user/group is assigned a manual provisioning task, while a provisionScript runs automatically on approval completion.

  * A boolean key of requestable set to true

  * A string key of displayName

If all the above criteria is met, the item appeara within the Create Request form in the Access Request application and ia available for use within request.

### Access Request Glossary Keys

There are several reserved keys for glossary items that are leveraged by the Access Request application. Note that any key marked with an asterisk (\*) is for use within the default approval flow, and won't be enforced when using a custom approval flow:

* requestable (boolean). The item available to be requested

* approvers\* (array). The approval chain for granting access to the requested item. The entries within this approver list is evaluated against both the managed/user object of the requestee, as well as the keys of the glossary item itself. In order for an approver key to be evaluated correctly it must refer to a managed object of either type user or role. For managed/user properties, the specified property must be a single relationship to the user/role.

  Some examples:

* An entry of `manager` in the approvers array evaluates to the requestee user's manager, as the property manager exists on the user schema and is a single relationship to a managed/user.

* An entry of `entitlementOwner` in the approvers array of an item with an entitlementOwner key of type managed object if the ID is set to a role, it uses that role as the approver.

* If the approvers list contains a key that is not able to resolve to a single user or role ID, the Access Request workflow defaults to the group defined in the Access Request settings as the Default Approver Group to handle that task

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The value of 'self' is also reserved as an approver option for any approval chain that wants to use the requestee themselves as an approver. This can be useful when defining a separate approver chain for removal of access. If an item is intended to be auto-provisioned, i.e. requires no approval steps, an approvers key should be created and left as a blank list. If an item is defined as requestable but has no approvers key, it leverages the Access Request setting for Default Approvers. |

* removalApprovers\* (array). The approval chain for the item when the request type is 'remove.' If this key is not used, the approvers key is used in its place. All the same functionality for defining approvers applies here as well.

* parallelApproval\* (boolean). If true, all approval tasks are created concurrently. If false, or not set, approval flow is executed sequentially. Note that provisioning tasks are always created after all approval tasks are completed, not in parallel.

* userProvisionProperty\* (string). The managed user property for which the requestable item is assigned to upon approval when using the default approval flow or the provision endpoint. This is used for requested items with a glossary class of object only, and has a default value of roles.

* preRequestScript (string). Script hook that is run immediately after creation of the request object for any pre-processing of the request, notifications, etc. This is called before any approval task creation or custom workflows are kicked off. The value should be set to the relative path of the javascript file to be run from the `openidm` script directory.

* provisionScript\* (string). Script hook for handling the provisioning of an approved item. Supersedes the default provisioning of items within PingIDM and is called once the item's approval chain is fully approved.

* provisioner\* (managed object id). If defined on an item and referencing a managed/user or managed/role, a manual provisioning task is created when the item's approval chain is completed, and be assigned to that provisioner. Note this should only be used in instances when manual intervention is required, as it supersedes the automated provisioning that normally occurs when a request is approved.

* requestWorkflow (string). Identifies the custom workflow to use for the requestable item. Defining a custom request workflow on a requestable item supersedes the default approval process and control the entire approval flow. See section 5.3 for details.

  * For BPMN workflows, it is the name of the workflow definition in PingIDM.

  * For custom scripts, it is the relative path to the script file within the scripts directory (for example, access-request/roleApproval.js)

* requestWorkflowType (string). Identifies the type of workflow defined by the requestWorkflow key, either 'workflow' or 'script.' Any item with a requestWorkflow defined but without a requestWorkflowType defaults to 'workflow.'

## Standard Request Workflow

Ping Identity Access Request uses an internal workflow to control and manage the approval process for all requestable items that do not explicitly specify their own process. All customizations and controls for the request process are available within the Access Request user interface.

The following section describes in detail the process of the out of the box workflow so that admins can better understand what actions are being taken at what stage.

### Approval Process

An item that is submitted within the Create Request form follows the approval process that is explicitly defined within that item's glossary entry. Each item has a list of approvers that the Access Request system will use to determine which users are assigned a given task and how many levels of approval are needed to provision an item. At each level of approval, the user who is assigned the task has the ability to either approve or reject each item that belongs to their task and submit their decision. Based on those decisions, items can either be provisioned, rejected outright, or continue down the chain of approval.

### Request Flow

Approval Flow

1. When a request is submitted, the following steps are taken, in order, to determine the flow of a request.

2. If a request contains multiple requestees, each requestee is split into their own individual request, so that each requestee's access can be provisioned independently of the other users.

3. If the request contains a requestable bundle as one of the requested items, that bundle is unpacked and each item within the request is then treated as an individual item within the request. This allows each item in the bundle to maintain its defined approval process independently of the items bundled with it.

4. If there are items within the request that have a preRequestScript key in their definition, it is executed at this point for any pre-request logic that needs to occur.

5. If an item has an explicitly defined approvers list that is empty (i.e. an approvers key within their glossary entry that is a list with no entries), then that item is auto-provisioned at this point. This is for any items that do not require any level of approval to be granted.

6. The items within the request are then be grouped, if possible, by the assigned approver. An approval task is then created for each individual user and group that is calculated as an approver for those items. As an example:

   A request that contains: - "Role 1", with approver "A" - "Role 2", with approver "A" - "Role 3", with approver "B"

   \+ results in two separate approval tasks:

   * Approver A receives a task with "Role 1" and "Role 2"

   * Approver B receives a task with "Role 3"

7. Depending on the system settings, auto approval may be enabled for certain approval tasks. There is an option for tasks where the requester is the direct approver and also an option for tasks where the requester belongs to the group assigned as the approver. Any items that meet the criteria of the enabled settings is immediately sent to their next level of approval, or if none exists, is provisioned. This feature allows end users to avoid duplication of effort, for example when a manager is requesting access for his/her reports and the initial approver for the items is defined as manager.

8. Once each approval task is created, the tasks can be completed independently of any other task that is part of the same request. This potentially allows for a single item to continue along its entire approval process and be completed without depending on a separate approval task to be decided on. Important to note here is that any item that completes its approval process has that item provisioned to the user as soon as that final decision is made. Further, any item that has already been completed and provisioned as part of a request that is cancelled at a later date remains provisioned. Any item that is rejected during a given approval task is immediately removed from any further approvals, and a notification is sent to inform users that that item was not successfully approved.

9. Approval task deadlines are calculated using the global setting defined in the access request configuration. When an approval task hits its defined deadline it doesn't expire or get cancelled. Instead, the task at that point is reassigned to the group defined as the Default Approver for further review. The group can decide to reassign the task elsewhere for another user to complete, if enabled.

10. After an item included in the request has either been approved by all listed approvers, its definition is checked for a provisionScript or provisioner key. Any item with a provision script has that script executed in lieu of the default PingIDM provisioning and then is marked as complete. Any item with a provisioner listed has a manual provisioning task created on the request and assigned to that provisioner to be completed. Once that user takes the manual steps to provision the item, they can complete the task as either 'provisioned' or 'not provisioned.'

    |   |                                                                                                                                                                                                                 |
    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | Any disconnected application item that is being requested must include one of the above keys for provisioning, as it is not a direct PingIDM managed resource and cannot be automatically assigned to the user. |

11. If no further provisioning or approval tasks are required for any items within the request,, the request is complete. All approved access has already been provisioned and the request moves to the completed table for reference.

## Custom Workflows

For any item with an approval process that requires additional steps that are not covered by the out-of-the-box functionality, a custom workflow may be used to define the steps necessary for approval. There are two different options available for a custom workflow: a BPMN workflow (activiti in PingIDM 6.5, flowable in 7.0) or a javascript script.

Either choice uses the Access Request API to interact with the request, create approval tasks, provision access, and complete the request. The process for doing so for each method is outlined below.

When a requestable item uses a custom workflow, every step of the approval process is controlled by that flow, immediately following the creation of the request object. Once a call is made to the create request API, the request object is saved to the repository with all of the necessary submitted request information, but no other steps are taken to advance the approval of the given item. Other items in the request follows their own processes, if defined, and won't expect another item's custom workflow to interact with their approval. However those other items are available within the workflows as part of the request object if they need to be leveraged for any custom logic.

### Defining a Custom Workflow on a Glossary Entry

There are two keys on a glossary entry that determine what custom workflow is used to drive the request lifecycle:

* requestWorkflow - This defines the specific workflow definition or script that is used to drive the request.

  * For workflows it is the name of the workflow definition within PingIDM. Refer to the PingIDM documentation for any questions on adding workflows to your environment.

  * For scripts it is the path to the javascript file, starting from within the `openidm/script` directory, (for example, , `basicRequest.js` for a file located directly in that directory).

* requestWorkflowType - Value can be either 'workflow' or 'script'. Entries that have a `requestWorkflow` key but not a `requestWorkflowType` key is assumed to be of type workflow. However, it is recommended best practice to store the proper type with this key.

|   |                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | There are some key differences between the two different types of custom workflow definitions because of the way each method operates. The details of each are described in the following two sections. |

### Creating a Custom Approval Process with BPMN Workflow

A request including an item that has a custom approval process via BPMN workflow (activiti/flowable) has a process instance of that request created upon creation of the request. As mentioned above, a request with multiple items that each have their own custom flow defined creates a workflow instance for each individual item, rather than one process for the entire request contents.

The following information is passed into the workflow process and can be used to drive the approval process:

* requestId - ID of the request object this item belongs to

* requesterId - ID of the user who submitted the request

* requesteeId - ID of the user who is targeted by this request

* item - ID of the requestable item glossary entry

* requestType - Type of request submitted for this item, either add or remove.

A custom BPMN workflow must be responsible for the following functionality in the request process. For more information on any of the API calls mentioned below, please refer to the additional Access Request API and Postman documentation.:

* Creating necessary approval tasks. To create an approval task via the API within a workflow, first create a user task node within the BPMN definition. Within that node's 'create' listener, make a call to `openidm/access-request/approval` and send the following body.

  * requestId - ID of request

  * itemIds - List of item IDs to include in approval task (normally just the single item)

  * approverId - ID of approver user or group

  * workflowTaskId - The user task ID that corresponds to this approval. This is used within BPMN workflows to complete the task upon approval submission and continue the workflow process.

* Sending request notifications. To send an Access Request notification via API, use the `openidm/notification/[NOTIFICATION_ID]` endpoint with the notification template of your choosing. Templates can be found with the accessRequestNotificationTemplates.json file in the conf directory, and any POST body to the endpoint must include any of the variables described in the template definition.

* Provisioning approved access. Access Request provides a provisioning endpoint (`openidm/access-request/provision`) for basic PingIDM attribute/role assignment which can be used for simple request provisioning, or a workflow can provision in another way if more appropriate. Alternatively, a provisioning task can be created for any required manual task.

* Setting the final outcome of the item on the request object. When an item's approval process is complete, the workflow must set the request item's outcome via a POST call to `openidm/access-request/request?_action=update`). When an item's outcome is set to a final outcome (for example, provisioned, denied, etc.), no other action is required on the request, and it is closed if and when any other items on the request have been completed.

### Creating a Custom Approval Process via Script

A request including an item that has a custom approval process via script executes that script upon creation of the request, and following the completion of every approval task containing that item.

The following information is passed into the script as variables to be used to drive the approval process:

* request - The request object

* approval - The approval task object that triggered the script; this is null when the script is run on creation

* glossaryItem - The glossary entry for the requested item.

A custom script must be responsible for the following functionality in the request process:

* Creating necessary approval tasks. To create an approval task via the API within a workflow, first create a user task node within the BPMN definition. Within that node's 'create' listener, make a call to `openidm/access-request/approval` and send the following body.

  * requestId - ID of request

  * itemIds - List of item IDs to include in approval task (normally just the single item)

  * approverId - ID of approver user or group

* Sending request notifications. To send an Access Request notification via API, use the `openidm/notification/[NOTIFICATION_ID]` endpoint with the notification template of your choosing. Templates can be found with the accessRequestNotificationTemplates.json file in the conf directory, and any POST body to the endpoint must include any of the variables described in the template definition. For a more detailed example, please see the Access Request Postman collection.

* Provisioning approved access. Access Request provides a provisioning endpoint (`openidm/access-request/provision`) for basic PingIDM attribute/role assignment which can be used for simple request provisioning, or a workflow can provision in another way if more appropriate. Alternatively, a provisioning approval task can be created for any required manual task.

* Setting the final outcome of the item on the request object. A request object is returned and saved with every iteration of the script, and so can be used to make any adjustments to the item's outcome within the request when a final outcome has been reached.

Every iteration of the script that is executed expects an object to be returned with two keys:

* success - A boolean value determining whether or not the script execution was successfully completed

* request - The request object, including any updates made during the script execution, which is saved to the request.

When an item's outcome is set to a final outcome (for example, provisioned, denied, etc.), no other action is required on the request, and it is closed if and when any other items on the request have been completed.

## Access Request Notifications

Ping Identity Access Request sends user notifications for certain events that take place within the application.

### Modifying Notification Templates

Notifications sent by the Access Request application are stored within the `openidm/conf/accessRequestNotificationTemplates.json` file. This file can be modified to display whatever custom message is desired for each individual notification. Note that modifying these templates directly requires someone with administrative privileges to edit the file within the PingIDM directory itself.

``````
 `````
=== Templates
``````

The following templates are used within the application:

**Templates**

| Field                       | Description                                                                                          |
| --------------------------- | ---------------------------------------------------------------------------------------------------- |
| OUTCOME\_UPDATE             | Sent when an item or items have reached a final request decision.                                    |
| APPROVAL\_TASK\_CREATED     | Sent to approver(s) when an approval task is assigned to them.                                       |
| APPROVAL\_TASK\_EXPIRED     | Sent to the default approver group when an approval task expires and is assigned to them for review. |
| CONSULT\_TASK\_CREATED      | Sent to consult(s) when added to an approval task for additional information.                        |
| CONSULT\_TASK\_CANCELLED    | Sent to consult(s) when a consult task is cancelled.                                                 |
| PROVISIONING\_TASK\_CREATED | Sent to provisioner(s) when a manual provisioning task is assigned to them                           |
| CREATE\_REQUEST\_FAILED     | Sent to the requester when creation of a request fails for an unknown reason.                        |
| REQUEST\_CANCELLED          | Sent to requester/requestee when a request has been cancelled.                                       |
| APPROVAL\_TASK\_CANCELLED   | Sent to approver(s) when an approval task has been cancelled.                                        |

---

---
title: Access Review
description: The UI context for Identity Governance can be found by navigating to /governance from your PingIDM server URL. Once logged in, the user can find the Administrator dashboard by clicking on the Dashboard link in the Administration section of the navigation sidebar, or alternatively by navigating directly to /governance/#/admin/dashboard.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:chap-access-review
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/chap-access-review.html
section_ids:
  dashboard_overview: Dashboard Overview
  metric_display_types: Metric Display Types
  stat_card: Stat Card
  table: Table
  pie_chart: Pie Chart
  user_and_object_certifications: User and Object Certifications
  creating_new_certification_definitions: Creating New Certification Definitions
  modifying_certification_definitions: Modifying Certification Definitions
  certification_tables: Certification Tables
  canceling_active_campaigns: Canceling Active Campaigns
  deleting_certification_definitions: Deleting Certification Definitions
  reviewing_active_certifications: Reviewing Active Certifications
  reassigning_active_certification_events: Reassigning Active Certification Events
  reviewing_active_events: Reviewing Active Events
  reviewing_closed_certifications: Reviewing Closed Certifications
  policies_overview: Policies overview
  policies: Policies
  policy_scans: Policy Scans
  active_violations: Active Violations
  active_exceptions: Active Exceptions
  violation_history: Violation History
  creating_a_new_policy: Creating a New Policy
  modifying_policies: Modifying Policies
  creating_a_new_policy_scan: Creating a New Policy Scan
  modifying_scheduled_policy_scans: Modifying Scheduled Policy Scans
  reviewing_active_policy_scans: Reviewing Active Policy Scans
  configure_reactive_policy_scans: Configure Reactive Policy Scans
  viewing_active_violations: Viewing Active Violations
  cancelling_active_violations: Cancelling Active Violations
  reassigning_active_violations: Reassigning Active Violations
  viewing_active_exceptions: Viewing Active Exceptions
  cancelling_active_exceptions: Cancelling Active Exceptions
  reviewing_violation_history: Reviewing Violation History
  user_summary: User Summary
  user_selection: User Selection
  summary: Summary
  select_system: Select System
  viewing_current_entitlements_only: Viewing Current Entitlements Only
  entitlements_table: Entitlements Table
  single_entitlement_history_view: Single Entitlement History View
  user_certification_tasks: User Certification Tasks
  viewing_a_user_certification: Viewing a User Certification
  reassigning_user_certification_tasks: Reassigning User Certification Tasks
  reassigning_selected_campaigns: Reassigning Selected Campaigns
  reassigning_all_tasks: Reassigning All Tasks
  reassigning_modal: Reassigning Modal
  object_certification_tasks: Object Certification Tasks
  violation_tasks: Violation Tasks
  review_notifications: Review Notifications
  modifying_a_notification_template: Modifying a Notification Template
  predefined_notification_templates: Predefined Notification Templates
  predefined_notifications_variables: Predefined Notifications Variables
  access_review_integration_with_the_glossary: Access Review Integration with the Glossary
  viewing_glossary_metadata_within_a_certification: Viewing Glossary Metadata within a Certification
---

# Access Review

The UI context for Identity Governance can be found by navigating to `/governance` from your PingIDM server URL. Once logged in, the user can find the Administrator dashboard by clicking on the Dashboard link in the Administration section of the navigation sidebar, or alternatively by navigating directly to `/governance/#/admin/dashboard`.

|   |                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Identity Governance doesn't support internal users for administrative or end-user tasks. To access the product functionality correctly, you must be logged in as a managed user. Internal users are redirected to a page informing them of this policy. Internal users are redirected to a page informing them of this policy. |

![iga administrator dashboard](_images/iga-administrator-dashboard.png)

## Dashboard Overview

To access the Administrator Dashboard, log into Identity Governance as a user with the governance-administrator authorization role. Select Dashboard in the navigation side bar menu under Review Administration.

The administrator dashboard offers admin users an overview of the entire state of the Review portion of Identity Governance, presenting statistics on the current count of total certifications, events, and more, as well as some analytical information to keep the administrators up to date on the decisions being made by certifiers.

The statistics shown on the dashboard are updated in one of two ways. Some, which are less intensive on the system to calculate on demand, are loaded in at the time the dashboard is accessed. Others, which look through the entire certification history of the system, are calculated via a scheduled script and are stored in the repository at a configurable interval. The script schedule is defined in the file `schedule-script_adminDashboard.json` in the `openidm/conf` directory, where the schedule can be updated to run as often as desired.

The following metrics are displayed as part of the dashboard: \* **Name**. title of the metric shown \* **Description**. Brief explanation of what the metric shows \* **Action**. Specifies if the metric is clickable or interactive in some way \* **Key**. Reference key for the metric, can be referenced in adminDashboard API call to retrieve a single metric

**Dashboard Metrics**

| Name                                    | Description                                                                                                                                                                  | Action | Key                                  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------------------------------------ |
| Active User Campaigns                   | Number of current user certification campaigns in flight                                                                                                                     | No     | activeUserCampaigns                  |
| Active User Events                      | Number of current individual user events in flight (where event is each task within a campaign)                                                                              | No     | activeUserEvents                     |
| Active Object Campaigns                 | Number of current object certification campaigns in flight                                                                                                                   | No     | activeObjectCampaigns                |
| Active Policies                         | Number of active policies defined in the system                                                                                                                              | No     | activePolicies                       |
| Active Violations                       | Number of current violation tasks with a status of 'in-progress' awaiting action                                                                                             | No     | activeViolations                     |
| Glossary Entries                        | Number of entries defined in the Identity Glossary                                                                                                                           | No     | glossaryEntries                      |
| Upcoming User Certification Deadlines   | Table of active user certifications, ordered by most recent upcoming stage deadline                                                                                          | Yes    | upcomingUserCertificationDeadlines   |
| Upcoming Object Certification Deadlines | Table of active object certifications, ordered by most recent upcoming stage decline                                                                                         | Yes    | upcomingObjectCertificationDeadlines |
| Upcoming Violation                      | Table of active violations, ordered by most recent upcoming deadline                                                                                                         | Yes    | upcomingViolationDeadlines           |
| Most Certified Entitlements             | Table of entitlements that have been certified and signed-off, sorted by the percentage of outcomes that are marked as 'certify'                                             | Yes    | mostCertifiedEntitlements            |
| Most Revoked Entitlements               | Table of entitlements that have been certified and signed-off, sorted by the percentage of outcomes that are marked as `revoke.`                                             | Yes    | mostRevokedEntitlements              |
| Highest Violation Count                 | Table of policies, sorted in descending order by the number of violations that have been found against the policy.                                                           | No     | highestViolationCount                |
| Certification Results                   | This chart allows the admin to see the complete breakdown of all certified entitlements within the system, grouped by the certification decision that was made against them. | Yes    | certificationResults                 |
| Violation Results                       | This chart allows the admin to see the complete breakdown of all violations acted on within the system, grouped by the decision that was made against them.                  | Yes    | violationResults                     |

## Metric Display Types

Metrics are displayed on the dashboard using one of three different display types, each of which is described below.

### Stat Card

The top row of metrics on the dashboard are all displayed as stat cards. This display is used for basic counts or totals of things within the Access Review environment such as Active User Campaigns or total Glossary Entries.

A single stat card displays the metric value centered on the card, with the title displayed along the bottom. The percentage on the top right of the card shows the difference in value between the most recent scheduled run of the admin dashboard script and the current value. Note that the longer the time period between iterations of the scheduled script, the more informative these numbers tend to be.

![Admin Dashboard Stat Card](_images/iga-stat-card.png)

### Table

Dashboard metrics that are displayed within a table view offer a paginated and interactive view to a sorted list of campaigns, violations, or entitlements within the system. The tables are all defaulted to show five (5) rows per page, and can be individually advanced through sorted pages by using the navigation arrows found at the bottom right of the table.

![iga admin dashboard table](_images/iga-admin-dashboard-table.png)

Most of the tables within the view offer the ability to click on a given row and view more information about the item chosen. Tables of certifications offer you a brief preview of the certification campaign, as well as a button that takes the administrator directly to the administration view of the campaign.

![iga admin dashboard campaign details](_images/iga-admin-dashboard-campaign-details.png)

Violation tables, when clicked, show the administrative view of a violation that is available to admins when accessed from the Policies and Violations table.

![iga admin dashboard violation details](_images/iga-admin-dashboard-violation-details.png)

Finally, the entitlement tables displays the standard metadata screen view when clicked. This information is grabbed directly from the corresponding glossary entry for the certified entitlement.

### Pie Chart

Metrics displayed via a pie chart show the division of entitlement certification of violation details. Upon initial installation, these charts won't appear populated until certifications and/or violations have been created and signed-off/completed and a scheduled scan of the adminDashboard script has been run. Each chart contains a select box above the chart that allows administrators to target an entitlement or policy to see the data that pertains only to that single object.

![iga pie chart](_images/iga-pie-chart.png)

## User and Object Certifications

User and object certifications target individual users or managed objects for certification. Certifications allow one or more certifiers to review a target's attributes and properties from the PingIDM schema. For user certifications, attributes and access defined within a linkey system may be reviewed in the applications section, and for object certifications glossary metadata as defined in the Identity Glossary can be certified. Certifiers can make a certification decision as to whether they want to certify or revoke a given entitlement, or abstain from making a choice entirely.

### Creating New Certification Definitions

Create a user certification:

1. For User Certifications, navigate to the User Certifications screen by clicking on its link on the navigation sidebar.

2. From the User Certifications page, click the **New Certification** button in the actions row of the table.

   ![iga create new certification basic](_images/iga-create-new-certification-basic.png)

3. On the Create New Certification screen, fill in each of the required fields. Additional details on the available fields are presented below.

   ![iga create new certification](_images/iga-create-new-certification.png)

   * **Certification Name**. **(Required)**. Title for the certification that appears on all summary pages.

   * **Description**. Provides additional details about the purpose of the certification for certifiers.

   * **Trigger**. **(Required)**. Identifies when the certification is created. Options are:

     * **Ad-Hoc**. Generates a new certification immediately after submitting the current form and can only be triggered once.

     * **Scheduled**. Generates a new certification each time a specified time duration has passed. When selecting the `Scheduled` option, additional fields become available, allowing duration to be specified. Note: For more information on scheduling events, refer to section 3.5.

     * **Event-based**. Generates a certification based upon criteria evaluated when a user's attributes or managed object is updated. After selecting an Event-based trigger, select 'Open Expression Builder' under Event Trigger to identify the criteria for triggering certification generation. Note: For more information on building expressions, refer to section 3.7.

   * **Target Object Type**. **(Object Certifications Only)**. Object certifications must specify which managed object type is targeted in the campaign. A certification can target any number of instances of the chosen object type, but it can only target one type per campaign. All managed objects within the system are eligible to be targeted by an object certification with the exception of 'user' (which is handled separately.) As noted in other places within this document, it is highly recommended that any object type you wish to target in a campaign have at a minimum a name and description as part of its schema properties to display properly within the certification screens.

   * **Target Filter**. **(Required)**. Identifies filter for targeting a specific subset of users for the certification. The current number of users that are currently targeted by the given expression is displayed next to the 'User Filter' text. The 'Reset Filter' option is available on the right-hand side of the filter, which restores the filter to its default state. The filter uses the two following categories: Basic and Advanced.

     * **Basic**. Upon selecting, the left dropdown is populated with the following options:

       * **User/Single Object**. Allows certification to be filtered to target only one specific user or managed object. Upon selecting, the right input box becomes available to enter in a username or object name.

         ![iga basic filter user](_images/iga-basic-filter-user.png)

       * **Users with manager**. (User Certifications Only). Allows certification to be filtered to any user with a specified manager. Upon selecting, the right input box becomes available to enter in a username corresponding to the manager.

         ![iga basic filter user manager](_images/iga-basic-filter-user-manager.png)

       * **Users with application**. (User Certifications Only). Allows certification to be filtered to any user assigned to a specified application. Upon selecting, the right select box becomes available to select the name of the connected application.

         ![iga basic filter user application](_images/iga-basic-filter-user-application.png)

       * **All Users/Every Object**. Allows certification to be run with no filter and target all users/objects of the type selected.

         ![iga basic filter all users objects](_images/iga-basic-filter-all-users-objects.png)

       * **Filter by provisioning/authorization role**. (User Certifications Only). Allows certification to be filtered to any user assigned to a specified instance of either a provisioning role or an authorization role. Upon selecting, the right input box becomes available to enter in the name of the role.

         ![iga basic filter user provisioning role](_images/iga-basic-filter-user-provisioning-role.png)

     * **Advanced**. Upon selecting, the advanced expression builder is displayed. The following options for creating a custom expression are available within the certification creation advanced target filter. For a more detailed description of what the individual options determine, refer to section 3.7.

       * **User/Object property**. Choose from any user attribute

       * **User application**. (User Certifications Only). Allows choice of any connected application to be selected from the dropdown menu

       * **All of**. Match all of the nested rows.

       * **Any of**. Match at least one of the nested rows.

       * **None of**. Negate the expression in the nested row.

       * **All users/Every object**. Select all users.

         ![iga advanced user filter](_images/iga-advanced-user-filter.png)

     * **Certification Stages**. A certification may have one or more stages. Each selected certifier is responsible for one stage, and additional stages may be added as needed (by selecting the 'Add Stage' button.), while selecting. Optionally, stage names may be modified by editing the text within the Name input field.

       * **Stage icons**. Name Input: Change the stage name

         * Up/Down arrows (next to the stage name): Change the stage order

         * 'X' icon: remove a specific stage

         * Caret: (at the top left of each stage): collapse/expand details for a given stage

           ![iga user creation form](_images/iga-user-creation-form.png)

       * **Entitlement Filter**. Specifies the entitlements/access that appears to certifiers within the given stage. For user certifications, the attributes/applications that appear in these sections correspond to those that are defined with a key of certifiable set to true in the glossary metadata. For object certifications, the entire managed object schema for the selected type is available to choose as certifiable in any campaign.

         * **Attributes**. The entitlements on the user or object that are tracked and stored by PingIDM; the managed object properties defined on the object's schema. Basic attributes and single object relationships are included in a certification stage via a basic checkbox. Multi-valued relationship objects are chosen and included as shown below:

           ![iga entitlement filter](_images/iga-entitlement-filter.png)

         * **Relationships**. When a relationship attribute is selected, add and remove buttons appear below the attribute name, allowing a complex target expression to be built. The number of objects currently selected is displayed to the right. If no expression is specified, all possible options are selected.

           ![iga filter multi valued relationship](_images/iga-filter-multi-valued-relationship.png)

           When choosing to filter a multi-valued relationship, the administrator is decided which values of the managed object is eligible for inclusion within this certification. Any objects that match this filter and belong to a target as part of the selected attribute appears in the campaign, while those excluded by the filter won't, even if a target user has that relationship. The following operators are available: **\*** Equals - Exact match of property

           * Contains - Property value contains string

           * Does Not Contain - Negation of above

           * Starts With - Property value starts with string

           * Does Not Start With - Negation of above

           * Selected Roles: Clicking on the number of objects currently selected on the top right of the attribute row displays the targeted screen. This screen shows the names and descriptions of the items selected.

             ![iga selected roles](_images/iga-selected-roles.png)

       * **Applications**. (User Certifications Only). The external applications and user data that are tracked by PingIDM through a connected system. To populate the applications list with certifiable systems, a glossary system entry must be created for the connector and assigned a key of certifiable. In addition, the attributes that can be certified must also correspond to a system-attribute entry with a key of certifiable set to true.

         ![iga selected attributes to certify](_images/iga-selected-attributes-to-certify.png)

       * **Metadata**. (Object Certifications Only). The entries within the Identity Glossary entry for the targeted managed object(s). Since the keys and entries that exist within the glossary are entirely arbitrary and could contain any given values across multiple instances of the same object, the administrator has the option to either not certify metadata at all, or to include all existing metadata to be certified by the certifier(s).

         ![iga glossary metadata](_images/iga-glossary-metadata.png)

     * **Risk Level**. Specifies a filter for the entitlements within the given stage. Only certifications with entitlements that match the specified levels of risk is generated. For more information on how Low, Medium and High risk levels are defined, see the System Settings section. Risk level on an entitlement basis is defined within the identity glossary. Relationships to managed objects use the corresponding glossary entry of type object, while managed user properties with specific values use glossary entries of type identity-value to define their risk.

       ![iga risk level filter](_images/iga-risk-level-filter.png)

       The following results occur from selecting the listed filter combination:

       * **Use Risk Level off**. Risk level won't be considered when filtering entitlements in a given campaign. Entitlements with a risk level defined at any level, as well as entitlements without a risk level defined is included.

       * **Use Risk Level on, one box selected**. Only items that match that risk level range is included.

       * **Use Risk Level on, two boxes selected**. Only items that match either level selected is included.

       * **Use Risk Level on, all selected**. All items that have a risk level defined is included in certification. Entitlements without a risk level defined are excluded.

     * **Certifier**. (Required). Identifies to whom the certification stage is assigned once generated, with the following available options:

       * **User**. User certifier assigns the generated certification stage to a specific user and a single user certifies all targets. When specifying a user, autocomplete helps identify the user login for the assignment.

         ![iga user certifier](_images/iga-user-certifier.png)

       * **Group**. Certifier assigns generated certification stage to a group of specified users. All targets are certified by users with the given group role attribute. To specify a group, select an available role in the choose certifier drop-down menu. See the section in the post-installation steps on membership property for information on how group membership is determined.

         ![iga group certifier](_images/iga-group-certifier.png)

       * **User Manager**. Certifier assigns generated certification stage to users designated by the Manager attribute. Their managers certify all targets.

       * **Previous Certifier's Manager**. Certifier assigns generated certification to the manager of the user specified in the preceding stage. Note that this option is disabled for the first stage in the sequence, or if the preceding stage has the Certifier field set to 'Group.'

       * **Entitlement Owner**. (User Certifications Only). Certifier assigns generated certification to the entitlement owner of the included entitlements. The certification targets for the stage are split among the users/roles who are set as the owner of the entitlement in the AccessReview Glossary (glossary key of entitlementOwner, with a type of managed object.) This option allows for multiple certifiers to be assigned a subset of entitlements for a given certification within a stage.

       * **Glossary Key**. (Object Certifications Only). This option allows administrators to specify any glossary key of their choosing to become the certifier for the selected stage. This allows for any defined key, or multiple keys using subsequent stages, to be certifiers for entitlements in a given stage. As with entitlement owner certifications, if a given entitlement has the defined key in its glossary entry, that key is defined as type managed object, and that managed object is a user or role, then that person or role is assigned as the certifier. If the entitlement doesn't have the entry defined as described above, the entitlement won't be included in the stage or goes to the default certifier if specified.

     * **Deadline**. (Required). Specifies how long certification stage should remain active. After the specified date or duration, the certification stage expires. Certification then either 1) moves to the next stage or 2) expires and become unavailable for modification, based on which option has been specified for the On Stage Expiration field.

       ![iga ad hoc deadline](_images/iga-ad-hoc-deadline.png)

     * **Escalation Schedule**. Administrators are now able to define a configured schedule of escalation notifications that are delivered to a specific party at a specific time period before the certification expires.

       * **Add an escalation date**. To add an escalation notification to the schedule, simply click the 'Add Escalation Date' button located on the stage form beneath the deadline field. This populates a single instance of the escalation form which consists of the following fields:

         * **Amount**. The numeric value that combines with the chosen time period to determine the time before the certification expires that the notification is sent.

         * **Time period**. Days or weeks before certification expires.

         * **Escalation owner type**. Specifies who is notified of the escalation. Choice of either user, group, or manager. The manager in this case refers to the manager of the certifier for the given user events.

         * **Choose escalation owner**. If owner type is user or group, select the user or role that receives the notification.

           To add an additional escalation date the preceding form must be completed before the add button is enabled again. Escalation dates must be added in order of furthest from the deadline to closest.

       * **Escalation Schedule**. Administrators are now able to define a configured schedule of escalation notifications that are delivered to a specific party at a specific time period before the certification expires.

         To add an escalation notification to the schedule, simply click the 'Add Escalation Date' button located on the stage form beneath the deadline field. This populates a single instance of the escalation form which consists of the following fields:

         ![iga escalation schedule](_images/iga-escalation-schedule.png)

         * **Amount**. This setting determines how far in advance of the expiration date a reminder notification is sent.

         * **Time period**. Days or weeks before certification expires.

         * **Escalation owner type**. Specifies who is notified of the escalation. Choice of either user, group, or manager. The manager in this case refers to the manager of the certifier for the given user events.

         * **Choose escalation owner**. If the owner type is user or group, select the user or role that receives the notification.

           To add an additional escalation date the preceding form must be completed before the add button is enabled again. Escalation dates must be added in order of furthest from the deadline to closest.

       * **Remove escalation date**. To remove the most recent escalation date, click on the 'Remove Escalation Date' found next to the add button.

     * **Default Certifier**. Specifies a default certifier for the entire campaign. If a default certifier is set, then stage events with no owner are assigned to that certifier. If no default certifier is set, events with no owner receives the status `No Certifier.` If no default certifier is set, events with no owner receives the status `No Certifier.`

     * **On Stage Expiration**. If a stage is not completed before the deadline, the events of that stage are marked as expired. The 'On Stage Expiration' field determines how the same events in subsequent stages are affected.

       ![iga on stage expiration](_images/iga-on-stage-expiration.png)

       * **Continue Certification**. The expired event(s) won't be affected in the next stage of the campaign; the next certifier is able to take action as they would normally.

       * **Expire Throughout**. The events are expired for all future stages within the campaign. This prevents any future certifiers of the campaign to take action on the event.

     * **Post Certification Workflow**. Identifies an automated remediation task for handling revocations from the certification. Note: For more information on remediation tasks, refer to section 3.6.

       ![iga post certification workflow](_images/iga-post-certification-workflow.png)

## Modifying Certification Definitions

1. To modify an existing certification definition, click on the User or Object Certifications link under the administrative section of the side navigation bar.

2. Choose either the Scheduled or Triggered tabs.

3. The table is populated with all existing scheduled or triggered certification definitions that exist within the system.

4. To modify a given certification, click on the row that contains the desired campaign to open up the edit screen. This screen is the same as the one used for creating certifications, with the certification data from the given campaign populated.

5. Once you have finished making your adjustments to the certification, click Save at the bottom of the form to complete the update. Note: For additional information on fields to update on this form, refer to section 4.2.1.

   ![iga edit existing scheduled certification](_images/iga-edit-existing-scheduled-certification.png)

## Certification Tables

To review the different certifications tables, click on the User or Object Certifications link under the administrative section of the side navigation bar. The information below describes the columns and functionality of each of the existing tables.

* **Active Certifications**

  ![iga active certifications table](_images/iga-active-certifications-table.png)

  * **Action Buttons**

    * New Certification. Create a new certification campaign.

    * Cancel Certification. Cancel an in-progress campaign.

  * **Display Columns**

    * Campaign Name

      * Description: Name of the active campaign

      * Searchable: Yes

      * Sortable: Yes

    * Object Type (Object certifications only).

      * Description: Type of managed object the campaign is targeting

      * Searchable: Yes

      * Sortable: Yes

    * Campaign Start Date

      * Description: Date the campaign was initially kicked off

      * Searchable: No

      * Sortable: Yes

    * Next Deadline

      * Description: Deadline of the earliest active stage (future stages may have a deadline further out than this date.)

      * Searchable: No

      * Sortable: Yes

    * Progress

      * Description: Shows the number of events completed out of the total number of events across all stages of the campaign. Note that to be considered completed, an event must be reviewed and signed-off by the certifier.

      * Searchable: No

      * Sortable: No

* **Closed Certifications**

  ![iga closed certifications table](_images/iga-closed-certifications-table.png)

  * **Action Buttons**

    * New Certification

  * **Display Columns**

    * Campaign Name

      * Description: Name of the closed campaign

      * Searchable: Yes

      * Sortable: Yes

  * **Object Type (Object certifications only)**

    * Description: Type of managed object the campaign is targeting

    * Searchable: Yes

    * Sortable: Yes

  * **Campaign Start Date**

    * Description: Date the campaign was initially kicked off

    * Searchable: No

    * Sortable: Yes

  * **Completed On**

    * Description: Date that the last stage of the campaign was completed and signed-off

    * Searchable: No

    * Sortable: Yes

  * **Total Events**

    * Description: Total events in campaign

    * Searchable: No

    * Sortable: No

* **Scheduled Certifications**

  * **Action Buttons**

    * New Certification

    * Cancel Certification

  * **Display Columns**

    * Campaign Name

      * Description: Name of the scheduled campaign

      * Searchable: Yes

      * Sortable: Yes

  * **Next Run Date**

    * Description: Date that the scheduled campaign starts based on its defined scheduler object

    * Searchable: No

    * Sortable: Yes

* **Triggered Certifications**

  * **Action Buttons**

    * New Certification

    * Cancel Certification

  * **Display Columns**

    * Campaign Name

      * Description: Name of the scheduled campaign

      * Searchable: Yes

      * Sortable: Yes

## Canceling Active Campaigns

To cancel an active campaign from the "Active" tab, check the checkbox next to the row of the campaign or campaigns that you wish to cancel. Note that once at least one row selected, the cancel certification button in the table's action row becomes enabled. Once this button is clicked the administrator is asked to confirm their choice, and if done so, the certification campaigns are cancelled.

## Deleting Certification Definitions

Deleting a certification definition from the scheduled or triggered tab of a Certifications page works exactly as described above for cancellation of active campaigns.

## Reviewing Active Certifications

From the active certifications tab of the User or Object Certifications table, search or sort the table until you find the desired campaign that you wish to review. Clicking on that certifications row takes you to the administrator certification list for that campaign.

![iga admin closed certification list](_images/iga-admin-closed-certification-list.png)

Select a certification from the Active Certifications list to display additional information. The following details are displayed:

* **Campaign Name**. Name of the campaign

* **Campaign Description**. Description of the campaign

* **Campaign Information**. Displays a summary of the campaign with the following information:

  ![iga campaign information](_images/iga-campaign-information.png)

  * **Campaign Status**. Identifies the current state of the certification. Values may include In-Progress, Cancelled, Signed-off, or Expired

  * **Progress**. The number of campaign events signed-off against the total number of events in the campaign

  * **Active Certifiers**. Any certifier with an in-progress event assigned to them that is part of the given campaign. Note this doesn't include certifiers with a pending (future stage) event assigned to them.

  * **Completed Certifiers**. Any certifier that has completed and signed-off on an event that is part of the given campaign.

* **Stage Information**. Displays a breakdown of each stage within the certification campaign with the following information:

  ![iga stage information](_images/iga-stage-information.png)

  * **Stage Name**. Name assigned to the stage

  * **Deadline**. Date that stage is set to or did expire

  * **Progress**. The number of stage events signed-off against the total number of events in the stage

* **Stage Stepper**. Shows a chronological visual of the certification stages. By selecting a stage node, the page is updated to reflect data for the selected stage.

  ![iga stage stepper](_images/iga-stage-stepper.png)

* **Target List**. List containing all targets for the certification. Each line contains a summary of the targeted user or object with the following information:

  * **Status icon**. The status of the current target's event for the selected stage. The following statuses are possible:

    * Pending

    * Incomplete

    * Certified

    * Certified, signed off

    * Revoked

    * Revoked, signed off

    * Abstained

    * Abstained, signed off

    * Cancelled

    * No Certifier

    * Expired

      Each status is displayed via a circular icon, and may have a different color or fill depending on the individual status. Certified statuses are colored green, revoked colored red, and abstained colored yellow. The difference between when a normal value and the signed-off version of that value is displayed, the normal version is displayed when all actions on an event have been completed, but the certifier has not yet signed off on it. After sign-off, the signed off version of the icon is displayed. This allows the administrator to have a little more insight at this level into the progress of the campaign even before any sign offs occur.

      ![iga certified revoked abstained icons](_images/iga-certified-revoked-abstained-icons.png)

      Note that each icon displays a tooltip with the display status text if the administrator hovers over the icon.

  * **Displayable Target Info Columns**. The information that displays in the certification list table may vary depending on certification type and the special displayInUserInfo key in the glossary on identity objects.

    For object certifications these displayable columns are always the name and description, so it's highly recommended that these attributes exist on any custom managed object that you wish to certify

    For user certifications, the displayable columns always include at least the user's givenName, sn, and email address, as well as any user attribute that has a glossary entry of type identity in the glossary and the displayInUserInfo boolean key set to true. Note that this key won't prevent you from displaying relationship attributes in the target list table, however with the exception of manager these attributes are not supported to display properly.

  * **Claimed By**. If the certifier for the given stage is a group, this column displays to inform the administrator as to which single user, if any, has claimed the given event.

  * **Certifier**. The user or role who is the certifier for the target event.

    ![iga target list table columns](_images/iga-target-list-table-columns.png)

## Reassigning Active Certification Events

Administrators have the ability to reassign active or pending certification events from the certification list for a given campaign. The admin has the option to either reassign all given events within a given campaign, or to select one or more rows within the target list table and reassign only those selected. The buttons to reassign the events are found in the action buttons section of the certification list table.

![iga reassign buttons](_images/iga-reassign-buttons.png)

Once the administrator has clicked on one of the available buttons to reassign, a small dialog box appears with a few options for selecting the new certifier. The administrator can choose to reassign to an individual user or a group. When searching for a user, the administrator can use any of the properties made available and searchable via the User Name Display Format setting, while group roles are searchable by name.

![iga reassigning event to a user](_images/iga-reassigning-event-to-a-user.png)

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Reassignment of Entitlement Owner user certifications can't be done on the certification list page. For reassignment of these certifications, you can use the User Summary page reassignment function when the entitlement owner is a user. For role entitlement owners, it is recommended to add an appropriate user to the role assigned, or to reconfigure your glossary data to reflect the appropriate owner and recreate the certification to ensure integrity of the certification process. |

![iga reassigning event to a role](_images/iga-reassigning-event-to-a-role.png)

## Reviewing Active Events

Select a target from the certification target list to display the complete event details view of the certification in a dropdown page. This is the same interface that is displayed to the end users when certifying a target, with some slight adjustments to what actions are available. The following information is displayed:

![iga admin event details view](_images/iga-admin-event-details-view.png)

* **Event Details**. The section at the top of the page displays details about the given event's certification progress. It includes some or all of the following information:

  * **Stage Selector**. If the campaign has multiple stages, the stage stepper selection bar is shown to allow the administrator to toggle between stages.

  * **Certifier**. The certifier for the event, if a single user or role

  * **Active Certifiers**. If an entitlement owner certification, shows the certifiers for the event that are active (have tasks to complete).

  * **Claimed By**. If the event has a role certifier and is claimed, displays the single user who has claimed it

  * **Completion Date**. Date and time that the event was signed off

  * **Progress Bar**. The progress bar for the event

* **User Information**. Details a summary of the target of the event with the following information. Note that more attributes may appear in user certifications if the displayInUserInfo boolean key is set to true on the glossary entry for the identity attributes:

  ![iga information panel](_images/iga-information-panel.png)

  * **User certifications**

    * First Name: First name of the target user

    * Last Name: Last name of the target user

    * Email Address: Contact information of the target user

    * Identity attributes set to display as described above

  * **Object certifications**

    * Name: Name of the object

    * Description: Description of the object

* **User/Object Attributes**. Contains attributes to be certified for the target of the event. Attributes that are single-valued are listed in a Name: Value format, while attributes that are multi-valued appears underneath a parent row with the attribute name listed. These attributes with parent rows can be collapsed and expanded by clicking on the expand icon to the left of the attribute name.

  ![iga attributes panel for user certification](_images/iga-attributes-panel-for-user-certification.png)

  Each row contains the following information:

  * **Attribute Name and/or Value**

    * Each attribute name and value is clickable by the administrator to see any attached metadata that belongs to the given item. Those items that do not have a corresponding glossary entry displays a page informing the administrator that no entry exists. Note that in object certifications, only the value allows for displaying metadata as individual object schema attributes do not have direct metadata definitions.

      ![iga clicking entitlement name to view metadata](_images/iga-clicking-entitlement-name-to-view-metadata.png)

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | For object certifications, when certifying an object that has a relationship to an out-of-the-box Ping Identity managed assignment, the display of those entitlements within the certification table is slightly altered from any other type of entitlement. For each assignment, any entry in the attributes property of that assignment is displayed in a readable format below the assignment name. This allows the certifiers to see exactly what access is being provisioned via this assignment, to make their decision easier. |

      ![iga certifying managed assignments with attributes](_images/iga-certifying-managed-assignments-with-attributes.png)

  * **Certification Action Buttons**. These buttons, disabled for administrators, shows the result of the certification action taken on each item if one has been made. If no button is selected and filled, then no decision has been made for that item. The buttons included are listed below:

    ![iga action buttons certify selected](_images/iga-action-buttons-certify-selected.png)

    * Certify

    * Revoke

    * Abstain

  * **Comment Icon**. The comment icon either is unfilled if no current comments exist, or have mini comment lines inside of the icon to indicate there are existing comments (pictured below). The administrator can click on the comment icon to display the existing comments, and also to add a new comment to that entitlement.

    ![iga action buttons certify selected](_images/iga-action-buttons-certify-selected.png)

* **Applications (User Certifications only)**. Contains attributes within connected systems to be certified for the target user.

  ![iga applications panel for user certification](_images/iga-applications-panel-for-user-certification.png)

  * **Attribute Name and/or Value**. Each attribute name and value is clickable by the administrator to see any attached metadata that belongs to the given item. Those items that do not have a corresponding glossary entry displays a page informing the administrator that no entry exists.

  * **Certification Action Buttons**. These buttons, disabled for administrators, shows the result of the certification action taken on each item if one has been made. If no button is selected and filled, then no decision has been made for that item. The buttons included are listed below:

    * Certify

    * Revoke

    * Abstain

  * **Comment icon**. The comment icon either is unfilled if no current comments exist, or has mini comment lines inside of the icon to indicate there are existing comments (pictured below). The administrator can click on the comment icon to display the existing comments, and also to add a new comment to that entitlement.

    |   |                                                         |
    | - | ------------------------------------------------------- |
    |   | For more information on Comments, refer to section 3.3. |

    ![iga comment icons](_images/iga-comment-icons.png)

* **Metadata (Object Certifications only)**. Contains each metadata entry that exists within the glossary entry for the target object.

  ![iga glossary metadata for object certification](_images/iga-glossary-metadata-for-object-certification.png)

  * **Metadata Key and Value**. Displays the glossary entry in \[Key]: \[Value] format for the certifier to act on. Those entries in the glossary that are of type managed object are converted to a displayable format if possible.

  * **Certification Action Buttons**. These buttons, disabled for administrators, show the result of the certification action taken on each item if one has been made. If no button is selected and filled, then no decision has been made for that item. The buttons included are listed below:

    * Certify

    * Revoke

    * Abstain

  * **Comment icon**. The comment icon either is unfilled if no current comments exist, or has mini comment lines inside of the icon to indicate there are existing comments (pictured below). The administrator can click on the comment icon to display the existing comments, and also to add a new comment to that entitlement.

    |   |                                                         |
    | - | ------------------------------------------------------- |
    |   | For more information on Comments, refer to section 3.3. |

    ![iga comment icons](_images/iga-comment-icons.png)

## Reviewing Closed Certifications

From the closed certifications tab of the User or Object Certifications table, search or sort the table until you find the desired campaign that you wish to review. Clicking on that certification's row takes you to the administrator certification list for that campaign.

![iga admin closed certification list](_images/iga-admin-closed-certification-list.png)

Select a certification from the Closed Certifications list to display additional information on the campaign. The following details are displayed:

* **Campaign Name**. Name of the campaign

* **Campaign Description**. Description of the campaign

* **Campaign Information**. Displays a summary of the campaign with the following information:

  ![iga campaign information](_images/iga-campaign-information.png)

  * **Campaign Status**. Identifies the current state of the certification. Values may include In-Progress, Cancelled, Signed-off, or Expired

  * **Progress**. The number of campaign events signed-off against the total number of events in the campaign

  * **Completed Certifiers**. Any certifier that has completed and signed-off on an event that is part of the given campaign.

* **Stage Information**. Displays a breakdown of each stage within the certification campaign with the following information:

  ![iga stage information](_images/iga-stage-information.png)

  * **Stage Name**. Name assigned to the stage

  * **Deadline**. Date that stage is set to or did expire

  * **Progress**. The number of stage events signed-off against the total number of events in the stage

* **Stage Stepper**. Shows a chronological visual of the certification stages. By selecting a stage node, the page is updated to reflect data for the selected stage.

  ![iga stage stepper](_images/iga-stage-stepper.png)

* **Target List**. List containing all targets for the certification. Each line contains a summary of the targeted user or object with the following information:

  * **Status icon**. The status of the current target's event for the selected stage. The following statuses are possible:

    * Pending

    * Certified, signed off

    * Revoked, signed off

    * Abstained, signed off

    * Cancelled

    * No Certifier

    * Expired

      Each status is displayed via a circular icon, and may have a different color or fill depending on the individual status. Certified statuses are colored green, revoked colored red, and abstained colored yellow. The difference between when a normal value and the signed-off version of that value is displayed, the normal version is displayed when all actions on an event have been completed, but the certifier has not yet signed off on it. After sign-off, the signed off version of the icon is displayed. This allows the administrator to have a little more insight at this level into the progress of the campaign even before any sign offs occur.

      ![iga certified revoked abstained icons](_images/iga-certified-revoked-abstained-icons.png)

      Note that each icon displays a tooltip with the display status text if the administrator hovers over the icon.

  * **Displayable Target Info Columns**. The information that displays in the certification list table may vary depending on certification type and the special displayInUserInfo key in the glossary on identity objects.

    For object certifications these displayable columns always are the name and description, so it's highly recommended that these attributes exist on any custom managed object that you wish to certify

    For user certifications, the displayable columns always include at least the user's givenName, sn, and email address, as well as any user attribute that has a glossary entry of type identity in the glossary and the displayInUserInfo boolean key set to true. Note that this key won't prevent you from displaying relationship attributes in the target list table, however with the exception of manager these attributes are not supported to display properly.

  * **Claimed By**. If the certifier for the given stage is a group, this column displays to inform the administrator as to which single user, if any, has claimed the given event.

  * **Certifier**. The user or role who is the certifier for the target event.

    ![iga target list table columns](_images/iga-target-list-table-columns.png)

To see additional information on the individual certification events for a closed campaign, simply click on the target row in the certification list and the event details page drop-downs to view. All information contained within the event details reflects the same format and styling as described in section 4.2.8

## Policies overview

Policies allow the administrator to define a set of criteria and schedule to determine violations within the identity system, as well as providing the ability to either grant exceptions to those violations or remediate the appropriate access.

To manage violations, the administrator should create a policy with a defined expression for a given combination of access that violates a business rule, create a policy scan to generate violations from that policy and monitor any exceptions granted from certifiers. Configure scheduled policy scans to scan for violations on a regular basis or configure reactive policy scans to scan a user for violations whenever a user is updated.

![iga policies tab](_images/iga-policies-tab.png)

### Policies

* Action Buttons

  * New Policy. Create a new policy.

  * Delete Policy. Delete an existing policy object.

* Display Columns

  * Policy Name

    * Description: Name of the policy

    * Searchable: Yes

    * Sortable: Yes

  * Description: Description of the policy

    * Searchable: Yes

    * Sortable: Yes

### Policy Scans

![iga policy scans tab](_images/iga-policy-scans-tab.png)

The policy scan and active scan tables have the following properties:

Scheduled Table: \* Action Buttons: \*\* New Scan. Create a new policy scan.

* Delete Scan. Delete an existing policy scan.

  * Display Columns

* Policy Name

  * Description: Name of the policy

  * Searchable: Yes

  * Sortable: Yes

* Next Run Data

  * Description: Next date policy scan is scheduled to run

  * Searchable: No

  * Sortable: Yes

### Active Violations

![iga active violations tab](_images/iga-active-violations-tab.png)

* Action Buttons:

  * Cancel Violation. Cancel the selected violation(s)

  * Reassign Selected. Reassign the selected violation(s) to a different owner

  * User

    * Description: User who violated the policy

    * Searchable: Yes, by username

    * Sortable: no

  * Policy

    * Description: Name of the policy that was violated

    * Searchable: Yes

    * Sortable: Yes

  * Owner

    * Description: User or role who owns the policy violated

    * Searchable: No

    * Sortable: Yes

  * Expiration Date

    * Description: Date the violation task expires

    * Searchable: No

    * Sortable: Yes

### Active Exceptions

![iga active exceptions tab](_images/iga-active-exceptions-tab.png)

* Action Buttons:

  * Cancel Exception. Cancel the selected exception(s).

* Display Columns

  * User

    * Description: User who violated the policy

    * Searchable: Yes, by username

    * Sortable: no

  * Policy

    * Description: Name of the policy that was violated

    * Searchable: Yes

    * Sortable: Yes

  * Owner

    * Description: User or role who owns the violation exception

    * Searchable: No

    * Sortable: Yes

  * Expiration Date

    * Description: Date the violation exception expires

    * Searchable: No

    * Sortable: Yes

### Violation History

![iga violations history tab](_images/iga-violations-history-tab.png)

* Action Buttons:

  * None

* Display Columns

  * User

    * Description: User who violated the policy

    * Searchable: Yes, by username

    * Sortable: no

  * Policy

    * Description: Name of the policy that was violated

    * Searchable: Yes

    * Sortable: Yes

  * Completed By

    * Description: User who completed the violation

    * Searchable: No

    * Sortable: Yes

  * Completion Date

    * Description: Date the violation was completed (date remediated, cancelled, or exception expired)

    * Searchable: No

    * Sortable: Yes

  * Result

    * Description: Final result of the violation

    * Searchable: No

    * Sortable: Yes

### Creating a New Policy

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. From the Policies tab, select 'New Policy'.

3. On the Create Policy page, fill in each of the required fields. Additional details on the available fields are given below:

   ![iga base policy creation form](_images/iga-base-policy-creation-form.png)

   * Policy Name: (Required) Reference name of the policy

   * Policy Description: Additional details describing the purpose of the policy. It is recommended to make this field as descriptive as possible to give the policy owner as much information as they need to make a remediation or exception decision.

   * Policy Expression: (Required) Rule for triggering a violation from the policy. If an event causing the rule to evaluate is true, a violation is created. The expression is defined using the Identity Governance expression builder.

4. Upon selecting Open Expression Builder, the advanced expression builder is displayed. The following options for creating a custom expression are available within the policy scan target filter. For a more detailed description of what the individual options determine, refer to section 3.7.

   ![iga policy expression](_images/iga-policy-expression.png)

   * The user/object property: Choose from any user attribute

   * The user application: (User Certifications Only) Allows choice of any connected application to be selected from the dropdown menu

   * All of: Match all of the nested rows

   * Any of: Match at least one of the nested rows

   * None of: Negate the expression in the nested row

   * All users

     |   |                                                                     |
     | - | ------------------------------------------------------------------- |
     |   | For more information on building expressions, refer to section 3.7. |

   * Risk Level: (Required) Risk level for the policy on a 1 - 10 scale. A risk score of 1 indicates a policy that is tracking a low risk violation or combination of access, while a score of 10 is given for a policy that is tracking an access violation that is of the utmost importance. These scores can be used during a remediation workflow to determine what steps should be taken to revoke the violating access.

   * Owner Type: (Required) Type of owner to assign to this policy. The options are between a single user or a group.

   * Policy Owner: (Required) Specific owner being assigned to this policy. Choose the single user or role that is the owner and responsible for decisions on all violations created by this policy.

     ![iga policy owner user role](_images/iga-policy-owner-user-role.png)

   * Violation Remediation Task: An automated remediation task for handling revocations from violation acceptance .

     |   |                                                                 |
     | - | --------------------------------------------------------------- |
     |   | For more information on remediation tasks, refer to section 3.6 |

   * Active: Identifies whether the policy is active or inactive. If unchecked, the policy won't be evaluated on updates.

### Modifying Policies

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Ensure the Policies tab is selected.

3. The table is populated with all existing policy definitions that exist within the system.

4. To modify a policy, click on the row that contains the desired policy definition to open up the edit page. This page is the same as the one used for creating policies, with the policy data already populated. See Section 6.2 for descriptions of the fields found within this form.

   ![iga edit policy](_images/iga-edit-policy.png)

5. Once you have finished making your adjustments to the policy, click Save at the bottom of the form to complete the update. Note: For additional information on the fields to update on this form, refer to section 4.3.1.

### Creating a New Policy Scan

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. From the Policies page, navigate to the Policy Scans tab and select 'New Scan'.

3. On the Create Scan page, fill in each of the required fields.

   ![iga create new policy scan](_images/iga-create-new-policy-scan.png)

   Additional details on available fields are given below:

   * Name: (Required) Name of the policy scan

   * Trigger: (Required) When the policy scan runs. Options are described below:

     * Ad-hoc: Triggers a policy scan immediately after submitting the current form and can only be triggered once

     * Scheduled: Triggers a policy scan when a specified time duration has passed. Additional fields become available when selecting the 'Scheduled' option to allow specific durations. Note: For more information on scheduling events, refer to section 3.5

   * User Target Filter: The subset of users the created scan searches for violations

     * Upon selecting Open Expression Builder, the advanced expression builder is displayed. The following options for creating a custom expression are available within the policy scan target filter. For a more detailed description of what the individual options determine, refer to section 3.7.

       * image

         iga-target-user-filter.png\[]

     * The user/object property: Choose from any user attribute

     * The user application: (User Certifications Only) Allows choice of any connected application to be selected from the dropdown menu

     * All of: Match all of the nested rows

     * Any of: Match at least one of the nested rows

     * None of: Negate the expression in the nested row

     * All users

![iga selecting policies to target](_images/iga-selecting-policies-to-target.png)

* Select Policies: (Required) Policies that are triggered by the scan. The field consists of side-by-side lists, with the left side containing available policies and the right side containing policies to be triggered in the scan. Selecting a policy in either list moves the policy to the opposite list.

  * Expiration Date: (Required) Specifies how long a violation should remain active. After the specified date or duration, the violation expires and becomes unavailable for modification. For Ad-hoc policy scans, the expiration date is a static date in the future. For scheduled policy scans, the expiration date is a period of time after the violation has been found and the task created.

    ![iga ad hoc expiration date form](_images/iga-ad-hoc-expiration-date-form.png)

  * Escalation Schedule: Administrators are now able to define a configured schedule of escalation notifications that are delivered to a specific party at a specific time period before the violation expires.

    ![iga escalation schedule controls](_images/iga-escalation-schedule-controls.png)

    * Add an escalation date. To add an escalation notification to the schedule, simply click the 'Add Escalation Date' button located on the stage form beneath the deadline field. This populates a single instance of the escalation form which consists of the following fields:

      * Amount: This setting determines how far in advance of an expiration date the notification is sent.

      * Time period: Days or weeks before certification expires.

      * Escalation owner type: Specifies who is notified of the escalation. Choice of either user, group, or manager. The manager in this case refers to the manager of the owner for the given policy.

      * Choose escalation owner: If owner type is user or group, select the user or role that receives the notification.

        To add an additional escalation date the preceding form must be completed before the add button is enabled again. Escalation dates must be added in order of furthest from the deadline to closest.

* Remove escalation date. To remove the most recent escalation date, click on the 'Remove Escalation Date' found next to the add button.

### Modifying Scheduled Policy Scans

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Policy Scans tab to navigate to the scans section.

3. The top table is populated with all existing policy scan definitions that exist within the system.

4. To modify a policy scan, click on the row that contains the desired scan definition to open up the edit page. This page is the same as the one used for creating policy scans, with the scheduled scan data already populated. See Section 6.4 for descriptions of the fields found within this form.

   ![iga editing a scheduled scan](_images/iga-editing-a-scheduled-scan.png)

### Reviewing Active Policy Scans

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Policy Scans tab to navigate to the scans section.

3. If any scans are currently in progress, the bottom table is populated with all existing active scans that exist.

4. The information within this table constantly updates as a scan is running, and once a scan is completed it is removed from the table completely.

### Configure Reactive Policy Scans

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Policy Scans tab to navigate to the scans section.

3. On the top right of the policy scans table, there is an action button for 'Configure Reactive Scans.' Clicking this button displays the reactive scans page.

   ![iga reactive scan button](_images/iga-reactive-scan-button.png)

4. The following fields are configurable for reactive scans.

   * Expiration Date: (Required) Specifies how long a violation should remain active. After the specified duration, a violation expires and becomes unavailable for modification. The expiration date is calculated from the day that the violation is found.

   * Escalation Schedule: Specifies where escalation notifications should be sent, at what day, and how many should go out overall. For more information on escalation schedules in policy scans, see section 4.3.4.

### Viewing Active Violations

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Active Violations tab to navigate to the active violations section. The table is populated with any active violations that are currently assigned out to users for completion. Note that this doesn't include violations that are currently being granted an exception, only those that are not yet acted on.

   ![iga violation details](_images/iga-violation-details.png)

3. To view a given violation, click on its row within the table to expand the violation page. This page shows the following information:

   * Target User: The user who violated the policy

   * Policy Owner: The user or role who is assigned the violation task

   * Violation Detected: Date that the violation was found

   * Expiration Date: Date that the task expires

   * Policy Name: Policy that was violated

   * Policy Description: Description of the policy that was violated

   * Comments: Any comments on the violation appear at the bottom of the violation view screen

     * Date: Date comment was made

     * Comment: The message that was added

     * By: The person who made the comment

### Cancelling Active Violations

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Active Violations tab to navigate to the active violations section.

3. Select the checkboxes next to the row or rows of the violations that you wish to cancel.

4. Click Cancel Violations.

5. The administrator sees a confirmation dialog to confirm that they wish to cancel the selected violations. Clicking OK completes the cancellation action.

   ![iga active violation action buttons](_images/iga-active-violation-action-buttons.png)

### Reassigning Active Violations

Administrators have the ability to reassign active violation tasks from the active violations tab. The button to reassign a violation is found in the action buttons section of the violation table.

Once the administrator has selected one or more violation rows to reassign, a small dialog box appears with a few options for selecting the new owner. The administrator can choose to reassign to an individual user or a role (group.) When searching for a user, the administrator can use any of the properties made available and searchable via the User Name Display Format setting, while roles are searchable by name.

![iga reassigning event to user role](_images/iga-reassigning-event-to-user-role.png)

### Viewing Active Exceptions

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Active Exceptions tab to navigate to the active exceptions section. The table is populated with any active exceptions that have currently been granted by the owner of the policy violated. A violation exception is considered active if it has been granted by the owner and has not yet reached its exception expiration date.

   ![iga violation details exception](_images/iga-violation-details-exception.png)

3. To view a given exception, click on its row within the table to expand the exception page. This page shows the following information:

   * Target User: The user who violated the policy

   * Policy Owner: The user or role who is assigned the violation task

   * Violation Detected: Date that the violation was found

   * Exception Start Date: Date that the exception was granted

   * Exception End Date: Date that the exception expires

   * Policy Name: Policy that was violated

   * Policy Description: Description of the policy that was violated

   * Comments: Any comments on the violation appear at the bottom of the violation view screen

     * Date: Date comment was made

     * Comment: The message that was added

     * By: The person who made the comment

### Cancelling Active Exceptions

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Active Exceptions tab to navigate to the active exceptions section.

3. Select the checkboxes next to the row(s) of exceptions that you wish to cancel.

4. Click Cancel Exception.

5. The administrator sees a confirmation dialog to confirm that they wish to cancel the selected exceptions. Clicking OK completes the cancellation action.

### Reviewing Violation History

1. Navigate to the Policies page by clicking the Policies link under the Administration section of the side navigation bar.

2. Click the Violations History tab to navigate to the history section. The table is populated with any past violations that have been completed. A violation is considered complete if it has any of the following statuses:

   * Remediated

   * Exception Expired

   * Cancelled

To view a completed violation, click on its row within the table to expand the violation page. This page shows the following information:

* Target User: The user who violated the policy

* Policy Owner: The user or role who is assigned the violation task

* Violation Detected: Date that the violation was found

* Exception Start Date: (if exception granted) Date that the exception was granted

* Exception End Date: (if exception granted) Date that the exception expired

* Completed By: User that completed the task

* Completion Date: Date task was completed

* Policy Name: Policy that was violated

* Policy Description: Description of the policy that was violated

* Comments: Any comments on the violation appear at the bottom of the violation view screen

  * Date: Date comment was made

  * Comment: The message that was added

  * By: The person who made the comment

    ![iga completed violation details](_images/iga-completed-violation-details.png)

## User Summary

The Access Review User Summary page allows governance administrators to access and view any given user's entitlement certification history in one single screen. Administrators can see the user's entire certifiable profile, the date and result of each certification of each entitlement, who made the certification decision, and view previous certifications for each entitlement as well. The user summary also allows the administrator to access any tasks that are currently assigned to that user, organized by task type (user certification, object certification, or violation). These task tables can be leveraged to easily reassign any or all tasks that belong to a given user in the event that they are no longer able to complete them as assigned.

![iga user summary](_images/iga-user-summary.png)

### User Selection

When first navigating to the User Summary section, administrators won'tice a blank auto select input field labelled 'Select User.' This field can be used to search for any user within the PingIDM system using the fields found in the display name format set in the system settings. Once a user is selected, the information for the given tab selected populates below.

### Summary

![iga user n system selection](_images/iga-user-n-system-selection.png)

#### Select System

When the summary tab is selected, administrators won'tice a second select input appears directly next to the user select input box at the top of the page, labelled 'Select System.' The "system" in this context refers to either the Ping Identity PingIDM environment or any of the linked systems that the given user has a connection to via a mapping in PingIDM. As Ping Identity Access Review allows attributes in both the PingIDM schema as well as connected systems to be certifiable, this selection allows administrators to view certification history for the entitlements derived from any of those given sources. The default view and selection always is 'PingIDM' and shows the certifiable entitlements that exist on the user profile.

![iga view current entitlements toggle](_images/iga-view-current-entitlements-toggle.png)

### Viewing Current Entitlements Only

When viewing the Summary tab, administrators have the option to toggle on or off a view of the user's currently assigned entitlements only. If toggled on, the only items displayed in the certification history summary table are those that exist on the current user object. This view is useful when the administrator wants to view the current certification state of the user, to gain insight into whether or not there are entitlements on the user that have not yet been certified and possibly rectify that situation. If toggled off, the administrator sees not only the user's current entitlements, but also any other entitlement that has ever been certified for that user. This allows administrators to get an entire lifetime view of a single user, even as their access has changed, been revoked, or otherwise altered.

### Entitlements Table

The entitlements table is where the individual user entitlements are displayed, displaying data in four separate columns and separated into groups by attribute name. The entry shown for any given entitlement is the most recently completed and signed-off certification of that item, or in the event that a certification is in progress for that given entry, it shows that the entitlement is currently in-progress. The four columns displayed are:

![iga user summary entitlement table](_images/iga-user-summary-entitlement-table.png)

* Entitlement - Name of the given entitlement

* Decision - Most recent decision made on that entitlement. Possible values are listed below:

  * Certified

  * Revoked \*\*Abstained

  * Not Certified

  * In-Progress

* Date - Most recent date of certification

* Certifier - Person who made the most recent certification decision

Each grouping of entitlements by attribute name can be collapsed or expanded by clicking on the arrow icon located to the left of the attribute name itself.

### Single Entitlement History View

For any entitlement that is not listed as 'Not Certified,' the administrator can click on that entitlement row and expand the historical certification view for that item. The page shows every time that the given entitlement has been certified for the target user in a table, organized by most recent data first, with the following columns:

![iga entitlement history with comments](_images/iga-entitlement-history-with-comments.png)

* Date - Date the certification was signed off

* Decision - Decision made for that certification

* Certifier - User who completed and signed-off the listed event

* Campaign Name - The campaign which the listed event was a part of

* Comments - If comments were made on the specific object during the certification, the comment icon is clickable, and displays the comments made in chronological order.

![iga entitlement history no comments](_images/iga-entitlement-history-no-comments.png)

### User Certification Tasks

The User Certification Tasks tab displays any certification campaign that currently has the selected user as a certifier for any of its events. This table won't display any certification tasks that the user is eligible to certify due to their membership of a role. This table, when populated, mirrors the table found on the end-user My Tasks dashboard page. For a further description on all of the columns and information found within the table, please refer to the Identity Governance 3.0 User Guide.

![iga user certification tasks](_images/iga-user-certification-tasks.png)

### Viewing a User Certification

To get more details on any given campaign that's assigned to the current user, the administrator can simply click on the certification row to navigate directly to the certification list. This is the same landing page that an admin ends up on when clicking a campaign from the User Certifications page.

### Reassigning User Certification Tasks

Administrators have two options for reassignment of tasks from the User Certification Tasks table: reassign selected campaigns or reassign all tasks.

#### Reassigning Selected Campaigns

To reassign only those tasks that belong to select campaigns, the administrator can select the checkbox(es) next to any campaign that they wish to reassign. Once selected, clicking on Reassign Selected Tasks displays the reassign page where the admin can choose the user or role to reassign to (described below in section 7.3.2.3) After the process has been completed any event that belonged directly to the chosen user is assigned to the new certifier.

#### Reassigning All Tasks

Alternatively, admins can choose to reassign all User Certification Tasks that belong to a given user. This functionality can be used when a certifier is on an extended leave or no longer an active user within the system to transfer all of open the reassign page where the admin chooses the new certifier (described below.)

#### Reassigning Modal

Once the administrator has selected one of the reassign actions, a small dialog box appears with a few options for selecting the new owner. The administrator can choose to reassign to an individual user or a group (role.) When searching for a user, the administrator can use any of the properties made available and searchable via the User Name Display Format setting, while roles are searchable by name.

![iga reassigning user certification tasks event to role](_images/iga-reassigning-user-certification-tasks-event-to-role.png)

### Object Certification Tasks

The object certification tasks table mirrors the exact functionality of the user certification tasks table but for object certification tasks. Administrators are able to view all of the selected users' object tasks, navigate directly to the tasks' campaigns, or reassign any or all tasks from this table. For further information on the table's functionality, refer to Section 7.3 above.

![iga object certification tasks](_images/iga-object-certification-tasks.png)

### Violation Tasks

Like the certification tables described above, the violation tasks table show all of the violation tasks directly assigned to the selected user. Administrators have the ability to reassign selected violation tasks or all violations tasks to another user or role. In addition, admins can view the current status of the violation by clicking on the violation row in the displayed table. For more information on viewing a violation as an administrator, see Section 6.8.

![iga violation tasks](_images/iga-violation-tasks.png)

## Review Notifications

Notification templates are used to define the messages sent to administrators and end-users when a certain event occurs.

### Modifying a Notification Template

1. Navigate to the Manage Notifications page, located in the Administrative Section of the Navigation Bar.

   ![iga notifications](_images/iga-notifications.png)

2. View contents under Notification List.

3. To display additional information about the notification, select a notification from the Notification List.

   ![iga edit notification](_images/iga-edit-notification.png)

   The following details are displayed:

   * ID: Represents unique identifier for the notification template. This field is not editable.

   * Name: (Required) Name of the notification template

   * From: (Required) Information that appears in the From field of the notification

   * To: (Required) Address of those who receives the notification. It contains a default variable that evaluates information from the certification. Note: For more information on supported variables, see section 4.5.3.

   * CC: Addresses of users who may receive a copy of the notification

   * Subject: (Required) Information that appears in the Subject field of the notification

   * Type: (Required) Form of the notification to be sent. The value is defaulted to 'text/html'.

   * Body: (Required) Contents of the notification. The default format is html, according to the value in the Type field, and may contain variables.

   * Enabled: (Required) Identifies whether the notification is enabled or disabled. If unchecked, the notification won't be sent on a triggering event. Note: For more information on supported variables, see section 4.5.3.

### Predefined Notification Templates

The following list describes the predefined notification templates:

**Predefined Notification Templates**

| Name                                               | Description                                                                                                                                                                           |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Certification Cancellation Failure                 | Sent when a certification cancel fails during the cancellation process.                                                                                                               |
| Certification Cancelled                            | Triggered when an administrator cancels a certification to inform the certifier that the certification is no longer available.                                                        |
| Certification Completion                           | Triggered when a user certification is completed to inform the certifier that the certification is complete.                                                                          |
| Certification Creation Adhoc                       | Triggered when a user certification is created from an administrator to inform the certifier that the certification is pending.                                                       |
| Certification Creation Adhoc Default Certifier     | Triggered when an ad-hoc user certification event is assigned to the default certifier                                                                                                |
| Certification Creation Scheduled                   | Triggered when a user certification is created as a scheduled event to inform the certifier that the certification is pending.                                                        |
| Certification Creation Scheduled Default Certifier | Triggered when a scheduled user certification event is assigned to the default certifier                                                                                              |
| Certification Creation Triggered                   | Triggered when a user certification is created after an update to a user to inform the certifier that the certification is pending.                                                   |
| Certification Creation Triggered Default Certifier | Triggered when an event-based user certification event is assigned to the default certifier                                                                                           |
| Certification Escalated                            | Triggered when a user certification is active past the escalation date set in the certification definition to inform the escalation owner that the certification is still pending.    |
| Certification Expired                              | Triggered when a user certification was active past the expiration date set in the certification definition to inform the certifier that the certification is now inactive.           |
| Object Certification Completion                    | Triggered when an object certification is completed to inform the certifier that the certification is complete.                                                                       |
| Object Certification Creation Adhoc                | Triggered when an object certification is created from an administrator to inform the certifier that the certification is pending.                                                    |
| Object Certification Creation Scheduled            | Triggered when an object certification is created as a scheduled event to inform the certifier that the certification is pending.                                                     |
| Object Certification Creation Triggered            | Triggered when an object certification is created after an update to an object to inform the certifier that the certification is pending.                                             |
| Object Certification Escalated                     | Triggered when an object certification is active past the escalation date set in the certification definition to inform the escalation owner that the certification is still pending. |
| Object Certification Expired                       | Triggered when an object certification was active past the expiration date set in the certification definition to inform the certifier that the certification is now inactive.        |
| Policy Exception                                   | Triggered when an exception is created for a violation to confirm the exception with the violation owner.                                                                             |
| Policy Exception Expired                           | Triggered when an exception for a violation has expired to inform the violation owner of the change.                                                                                  |
| Policy Remediated                                  | Triggered when a violation is remediated by either an administrator or task to inform the violation owner.                                                                            |
| Policy Violation Detected                          | Triggered when a violation is raised from a policy scan to inform the violation owner.                                                                                                |
| Policy Violation Escalated                         | Triggered when an escalation duration has been exceeded for a violation to inform the escalation owner of the violation.                                                              |
| Policy Violation Expired                           | Triggered when an expiration duration has been exceeded for a violation to inform the violation owner of the change.                                                                  |

### Predefined Notifications Variables

The following describes the predefined variables that are used within notifications:

**Predefined Notification Variables**

| Variable             | Description |
| -------------------- | ----------- |
| ${x.email}           |             |
| ${x.certifierEmail}  |             |
| ${x.escalatorEmail}  |             |
| $x.user              |             |
| $x.certifier         |             |
| $x.owner             |             |
| $x.certificationName |             |

### Access Review Integration with the Glossary

There are a few major areas of functionality within Access Review that are handled by Glossary entries for certain identity objects. The following is the full list of keys, and what they control within the application:

**Access Review Keys**

| Class            | Key               | Type           | Function                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------- | ----------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identity         | certifiable       | boolean        | Allows the attribute to appear within the user certification creation screen as an option for 'Access to Certify'. If not present or set to false the attribute won't appear.                                                                                                                                                                                                   |
| Identity         | displayInUserInfo | boolean        | Displays this attribute in the user certification list and event details tables. If not present or set to false the attribute won't appear. Note as of v3.0 this setting doesn't properly display relationship attributes within the above tables, with the exception of 'manager', which displays correctly.                                                                   |
| Identity-Value   | displayName       | String         | Displays the value defined here in lieu of the actual value on the user event details page, if the displayed attribute matches this entry.                                                                                                                                                                                                                                      |
| Object           | riskLevel         | Integer        | When risk level is enabled in system settings, certifications for user, object, and assignment uses this value to match against the provided certification filter for each object.                                                                                                                                                                                              |
| Object           | entitlementOwner  | managed object | The entitlement owner key is used to determine the user or role that should be assigned a certification task for the given object. This is used in user certifications when the certifier is set to "Entitlement Owner', as well as when the glossary key certifier is chosen for object certifications. The value here should reference only a managed/user or a managed/role. |
| Object           | displayName       | String         | Displays the value defined here in lieu of the actual value on the user event details page, if the object is included within a certification.                                                                                                                                                                                                                                   |
| System           | certifiable       | boolean        | Allows the system to appear within the user certification creation screen as an option for `Access to Certify`. If not present or set to false the system won't appear.                                                                                                                                                                                                         |
| System           | riskLevel         | Integer        | When risk level is enabled in system settings, certifications for users use this value to match against the provided certification filter for each system. Note that the risk level for connected systems is global to that entire system and all its attributes.                                                                                                               |
| System           | entitlementOwner  | managed object | The entitlement owner is used to determine the user or role that should be assigned a certification task for the given system. It's used in user certifications when the certifier is set to 'Entitlement Owner'. The value here should reference only a managed/user or a managed/role, and is global to the system and all its attributes.                                    |
| System-Attribute | certifiable       | boolean        | Allows the system attribute to appear within the user certification creation screen as an option for 'Access to Certify'. If not present or set to false the attribute won't appear.                                                                                                                                                                                            |
| System-Attribute | displayable       | boolean        | Allows the system attribute to appear within the user event details page as a non-certifiable attribute. It can be used to provide the certifier more insight to the user's account, for entitlements that may be helpful to see not certify (for example, `cn`, `uid`, etc.)                                                                                                   |

### Viewing Glossary Metadata within a Certification

When viewing the event details display of a single event within a certification, users won'tice that the entitlements, and in user certifications the attribute names, of each certifiable row are clickable links. If clicked, a glossary page appears that corresponds to the identity attribute or value chosen. If that entry exists, the metadata for that item is displayed in a key-value table. If that entry doesn't exist, the user is informed that there is no current glossary entry for that item. This view allows the certifier or admin to gain more information and perspective on the things included in that particular certification.

![iga clickable metadata links](_images/iga-clickable-metadata-links.png)

There is often metadata in glossary entries that administrators would either not want the end user to see, whether that be for privacy reasons or simply because the information would be more confusing than helpful. Access Review leverages a configuration file within the `openidm/conf` directory called `displayableMetadata.json` to restrict the keys that displays in these pages for each of the different glossary object classes. Only keys that appear for each class type are shown to end users, and they are global for each class type.

![iga glossary metadata](_images/iga-glossary-metadata.png)

---

---
title: Administration Guide
description: This guide is written for administrators who must manage and maintain Ping® Identity Governance.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:preface
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/preface.html
page_aliases: ["index.adoc"]
---

# Administration Guide

This guide is written for administrators who must manage and maintain Ping® Identity Governance.

This guide describes administrative usage of Identity Governance, including overviews and instructions for administrative tasks occurring within the application. It is not intended to document end-user processes interacting with administrative tasks described herein.

This guide is written for Ping Identity Identity Governance administrators performing actions in certification campaigns, Segregation-of-Duty (SOD) violation processes, request administration, and other general administrative configurations throughout the module.

**Quick Start**

|                                                                                                                                        |                                                                                                                                        |                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [](chap-common-interfaces.html)[Common Interfaces](chap-common-interfaces.html)Learn about the Identity Governance common interfaces. | [](chap-access-review.html)[Access Review](chap-access-review.html)Learn about the Identity Governance access review.                 | [](chap-access-request.html)[Access Request](chap-access-request.html)Learn about the Identity Governance access request. |
| [](chap-system-settings.html)[System Settings](chap-system-settings.html)Learn about the Identity Governance system settings.         | [](chap-identity-glossary.html)[Identity Glossary](chap-identity-glossary.html)Learn about the Identity Governance identity glossary. | [](chap-gdpr-compliance.html)[GDPR](chap-gdpr-compliance.html)Learn about the Identity Governance GDPR compliance.        |

---

---
title: Common Interfaces
description: The following sections detail functionality common throughout the Identity Governance Administrative Screens.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:chap-common-interfaces
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/chap-common-interfaces.html
section_ids:
  navigation_sidebar: Navigation Sidebar
  access_review_administration: Access Review Administration
  access_request_administration: Access Request Administration
  configuration: Configuration
  tables: Tables
  comments: Comments
  metadata: Metadata
  scheduling_events: Scheduling Events
  remediation_tasks: Remediation Tasks
  expression_builder: Expression Builder
---

# Common Interfaces

The following sections detail functionality common throughout the Identity Governance Administrative Screens.

## Navigation Sidebar

The navigation sidebar, pictured to the right, is the main way for users and administrators to navigate throughout Identity Governance. It is split into four separate sections, one for the end user functionality (My Review Tasks, My Requests, My Approvals) and one section each for the different administrator roles and capabilities: Review Administration, Request Administration, and Configuration.

All administrative screens are available from this location, and only those accessible to a given user based on their administrator privileges are shown.

![Navigation Bar](_images/iga-navigation-bar.png)

## Access Review Administration

This section is available to any user assigned the governance-administrator internal role and includes the following options:

* **Dashboard**. Administrative dashboard

* **User Certifications**. Manage and create user certification campaigns

* **Object Certifications**. Manage and create object certification campaigns

* **Policies**. Manage and create policies, scans, and violations

* **User Summary**. View individual user certification history and tasks view

* **Notifications**. Manage Access Review notification templates

![Access Review](_images/iga-access-review.png)

## Access Request Administration

This section is available to any user assigned the access-request-admin internal role and includes the following options:

* **View All Requests**. Manage requests for access

* **Bundle Editor**. Create and manage request bundles

* **Request Fields**. Create and manage custom form fields for requests

![Access Request](_images/iga-access-request-administration.png)

## Configuration

This section is available to any user that is assigned any of the three Identity Governance internal roles and includes the following options:

* **Glossary Editor**. Create and manage glossary entries

* **System Settings**. Configuration options (available to governance-administrators and access-request-admins)

![Access Configuration](_images/iga-access-configuration.png)

## Tables

Throughout the admin controls, information is often stored in tables with a common set of properties, including the following options:

![iga table interface](_images/iga-table-interface.png)

* **Section Tabs**. Navigate through the different tabs that the current table view allows

* **Action Buttons**. Lists the available actions that can be taken on the table rows. Note that some actions require one or more rows to be selected via the row checkboxes and remains gray if disabled.

* **Search Filter**. Allows the user to enter in a value to search against the different columns of the table. Note that not all columns in a given table are searchable, please refer to the individual sections of documentation for more information.

* **Sortable Column Names**. Clicking the column name sorts the data by that column. Clicking again reverses the search order.

* **Row Checkboxes**. If a table has row checkboxes available, these can be used to select one or more rows to target for the available stage actions.

* **Table Pagination Controls**. Rows per page allows you to select the number of results made visible at a specific time within the table. Values may include 10, 25, or 50. Also included are navigation arrows for moving forward and backward between pages.

## Comments

Comments appear throughout review screens for certifications, violations, and exceptions, identifying actions taken against these objects. Once one or more actions have occurred, the following information details the history of events leading up to the current state of an object:

* **Date**. Time an action was taken

* **Comment**. The message entered by the user when performing the action or submitting a general comment

* **By**. Display name of the user who submitted the comment

![iga comments](_images/iga-comments.png)

## Metadata

Metadata, in the form of glossary entries, can be created for various object and attribute values. Each metadata entry can contain any number of extended attributes, defined independently from other entries. In some cases, this metadata may even substitute the value that is displayed to the certifier. Pictured above is a sample metadata screen that appears when clicking on a certification entitlement. Additional information is detailed in the Glossary section.

![iga metadata](_images/iga-metadata.png)

## Scheduling Events

Events can be scheduled for generating certifications or running policy scans. To determine the duration between actions, the following options are available:

* **Daily**. Allows the administrator to generate a certification every specified number of days, starting on a specified day of the month.

  ![iga scheduling events daily](_images/iga-scheduling-events-daily.png)

* **Weekly**. Allows the administrator to generate a certification on specified days of the week.

  ![iga scheduling events weekly](_images/iga-scheduling-events-weekly.png)

* **Monthly**. Allows the administrator to generate a certification every specified number of months starting on a specified month. Day of the month for the certification generation can also be specified, with 'Last day of the month' as an option.

  ![iga scheduling events monthly](_images/iga-scheduling-events-monthly.png)

## Remediation Tasks

Remediation Tasks complete revocations resulting from certifications or violations, via workflows defined in PingIDM. Identity Governance includes a single remediation workflow to handle basic remediation for both violations and certifications, however, it is recommended that these be modified or replaced to adhere to custom policy:

* **None**. Skips automatic remediation to allow manual intervention from an administrator

* **Remove Entitlements**. Takes the following actions depending on the type of task being remediated:

  * **Certifications**. For any revoked entitlement either removes or alters the attribute depending on the type of attribute as defined in the object schema:

    * **Relationship**. Relationship between target and entitlement is deleted

    * **Array**. Item is removed from array

    * **Other**. Attribute is altered to generic stage or to reflect remediation (for example, appending "-REMEDIATED" to a string or setting a boolean to false)

  * **Violation**. For every target attribute defined within the given policy's expression, the same actions listed above for certification are taken on the target object.

## Expression Builder

Expression Builder identifies criteria for filters in certification definitions and policy rules. The criteria identify attribute constraints for target users. Depending on the exact expression builder being used (for example, user target filter, user event based expression, policy expression) the options in the builder may differ. This section covers the basic format and use of a generic expression builder. Refer to the individual documentation section for the screen in question for more specific details.

To build an expression, select one of the following options: Each option presents either another tier for additional criteria or identifies an attribute/managed object to serve as a base for the trigger.

* **Every \[user/role/etc]**. Selects every matching object to the given object type. This doesn't require any further nested expressions.

* **The \[user/role/etc] property**. Allows the administrator to specify an attribute and evaluate its value. Depending on the attribute chosen the administrator can specify whether to evaluate a direct equals comparison or a contains comparison. In the instance of event based certifications, users can choose is, was, or changed to compare previous values, current values, or detect any change at all.

  ![iga expression builder user property](_images/iga-expression-builder-user-property.png)

* **Any of**. Allows the administrator to specify multiple expressions concatenated by 'OR' conditions. If any of the contained expressions are true, the entire expression evaluates to true. Selecting '+' appends additional expressions while selecting '-' removes expressions from the end.

* **All of**. Allows the administrator to specify multiple expressions concatenated by 'AND' conditions. If all of the contained expressions are true the entire expression evaluates to true. Selecting '+' appends additional expressions while selecting '-' removes expressions from the end.

  ![iga expression builder all of](_images/iga-expression-builder-all-of.png)

* **None of**. Allows the administrator to specify an expression and negate its value. If the contained expression is false, the expression evaluates to true.

  ![iga expression builder none of](_images/iga-expression-builder-none-of.png)

* **The user has application**. In user target filters for certifications, you can filter users by whether or not they have a link to an externally connected system.

---

---
title: GDPR Compliance
description: Due to the GDPR regulations, Ping Identity has identified the following critical areas that would assist in implementing a compliant system. The below identifies what personal data is captured, where that data is stored, when it is stored and who can potentially access the data. It is the implementer's responsibility to scrub the personal data as necessary to be considered compliant with GDPR regulations.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:chap-gdpr-compliance
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/chap-gdpr-compliance.html
section_ids:
  what_personal_data_is_being_stored: What personal data is being stored?
  where_the_personal_data_is_being_stored: Where the personal data is being stored?
  when_is_the_data_being_stored: When is the data being stored?
  who_can_access_the_data: Who can access the data?
---

# GDPR Compliance

Due to the GDPR regulations, Ping Identity has identified the following critical areas that would assist in implementing a compliant system. The below identifies what personal data is captured, where that data is stored, when it is stored and who can potentially access the data. It is the implementer's responsibility to scrub the personal data as necessary to be considered compliant with GDPR regulations.

## What personal data is being stored?

Since Ping Identity PingIDM allows the user schema to be customized and linked to outside resources; it is not feasible to identify all the potential Personal Identification Information (PII) that Ping Identity AccessReview can access. It is important to know that any application data that contains PII linked to an PingIDM user is exposed to the Ping Identity AccessReview application. If the attributes that contain sensitive data are set to displayable or certifiable, it is stored at the time of creating the user certification.

Examples: \* User Attributes: **username **givenName **sn **email \* OpenDJ **member\_address **member\_ssn

## Where the personal data is being stored?

* auditactivity

* genericobjects

* genericobjectproperties

## When is the data being stored?

* During the creation of a certification campaign or policy violation

* When a certification campaign or policy violation is acted upon

## Who can access the data?

* Ping Identity AccessReview administrators

* Ping Identity AccessReview certifiers

* PingIDM Admins

---

---
title: Identity Glossary
description: Users who are assigned to the glossary-admin internal authorization role see the Glossary subsection available on the side taskbar. Navigating to this screen will allow the user to directly edit, create, or delete glossary objects within the system. This role defines the item properties in the PingIDM system that are required for the access request process.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:chap-identity-glossary
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/chap-identity-glossary.html
section_ids:
  glossary_introduction: Glossary Introduction
  glossary_object_classes: Glossary Object Classes
  selecting_a_glossary_object_class: Selecting a Glossary Object Class
  creating_a_new_glossary_entry: Creating a New Glossary Entry
  editing_an_existing_glossary_entry: Editing an Existing Glossary Entry
  deleting_a_glossary_entry: Deleting a Glossary Entry
  reserved_keys: Reserved Keys
---

# Identity Glossary

Users who are assigned to the glossary-admin internal authorization role see the Glossary subsection available on the side taskbar. Navigating to this screen will allow the user to directly edit, create, or delete glossary objects within the system. This role defines the item properties in the PingIDM system that are required for the access request process.

## Glossary Introduction

The glossary is an extensive collection of metadata that refers to any and all of the identity information that is compiled and tracked by PingIDM. It allows administrators to store as much information as desired about any of the components described below. The data stored can directly affect some of the product functionality, or it can be as simple as arbitrary information that allows for easier maintainability and categorization of the system on a whole.

![iga glossary editor interface](_images/iga-glossary-editor-interface.png)

## Glossary Object Classes

![iga glossary object classes](_images/iga-glossary-object-classes.png)

* Identity: The user properties that exist on a managed user within PingIDM.

  * Examples: jobCode, department, location

  * Required Keys:

    * attributeName (string): the attribute property on the user

* Identity-Value: Specific values that are assigned to any of properties that exist on a managed user within PingIDM.

  * Examples: a jobCode of AT152, a status of T

  * Required Keys:

    * attributeName (string): the attribute property on the user

    * attributeValue (string): the value assigned to that property

* Object: A specific instance of a managed object within PingIDM. Can refer to a managed object of any type, as long as it currently exists within the system.

  * Examples: Database Administrator Role, LDAP Group Assignment

  * Required Keys:

    * objectId (managed object id): the \_id of the object in PingIDM

    * displayName (string): the readable name of the object

    * order (array): the displayable order of the object's properties

* System: A connected external system managed by PingIDM

  * Examples: Active Directory, PeopleSoft

  * Required Keys:

    * name (string): the name of the connected system

* System-Attribute: A user property within the external connected system.

  * Examples: ldapGroups, cn

  * Required Keys:

    * system (string): the name of the connected system that tracks this attribute

    * objectType (string): the object type of the attribute (for example, account or group)

    * attributeName (string): the name of the attribute

    * order (integer): numeric ranking used to determine display order

* System-Value: Specific values that are assigned to any of properties that exist on an external connected system.

  * Examples: a jobCode of AT152, a status of T

  * Required Keys:

    * system (string): the name of the connected system that tracks this attribute

    * objectType (string): the object type of the attribute (for example, account or group)

    * attributeName (string): the name of the attribute

    * attributeValue (string): the value assigned to that attribute

## Selecting a Glossary Object Class

Using the available select list, administrators are able to view a single glossary object class at a time within the glossary editor interface. Once a class is chosen, the table displays existing glossary entries that pertain to that class in a searchable and paginated fashion. The table includes text inputs that allow you to further filter the results by properties such as name, attributeValue, system, and more. There are also pagination controls available near the bottom of the table, that allow admins to control how many entries they see at a given time.

## Creating a New Glossary Entry

Once a glossary object class is selected, clicking the "New" button displays a blank form to the administrator, with all of the required keys pre-populated and awaiting entry. Note that next to each required key, the type of metadata is also pre-populated, and is locked to the required type for that entry. These fields must all be completed before a glossary entry is allowed to be saved.

To add a new metadata key to the glossary object, simply add the key name to the empty input box below the existing keys marked 'New key' and then click on the '+' icon. Doing so adds the new key to the list of entries, which then makes it editable. Each entry row has multiple inputs, the number of which may vary depending on the type selected. Firstly, the delete icon next to non-required keys allows admins to remove the corresponding key from the object. Next to that icon is the key itself, which is followed by the entry type selector, which allows the admin to define the type of data being entered.

The choices for this selector are as follows:

* String

* Boolean

* Integer

* Managed Object

* Object

* Array

* Date

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Entries of type Managed Object allow the admin to further choose the type of object being entered, and once the type is selected, it queries the PingIDM system for objects of that type. The fields for which this input box queries against per managed object is defined in the commons.json file located in the `openidm/conf` directory. The initial configuration of `commons.json` contains the PingIDM OOTB attributes for user, role, and assignment only. To add entries for different custom managed objects, each object must be added to commons.json in order for it to be an available choice for a new glossary entry. |

Once all entries have been added and the entry is complete, clicking on the Save button saves the entry to the glossary.

## Editing an Existing Glossary Entry

To edit an existing entry, simply locate the entry desired within the search table of the editor, and click on its row. Doing so displays the editor form, much like when creating a new entry, but with the current metadata populated within the form.

![iga editing a glossary entry](_images/iga-editing-a-glossary-entry.png)

## Deleting a Glossary Entry

To delete an existing glossary entry, click on the entry in question to display the edit glossary entry form for the object. Once populated, clicking delete allows the entry to be removed.

## Reserved Keys

While the glossary editor allows the user to enter in nearly any value as a key within the glossary object, the admin should take note that there are certain keys that are leveraged across different products to provide different levels of functionality. Examples of these include the key approvers for Access Request and riskLevel for Access Review. Glossary admins should be aware of any keys used throughout other applications before creating new key entries to avoid potential conflicts. The full list of reserved keys used by Identity Governance can be found within the respective Access Review and Request sections above.

---

---
title: Installation
description: The following chapter provides details about the Identity Governance installation.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:chap-installation
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/chap-installation.html
section_ids:
  provided_files: Provided Files
  installation_instructions: Installation Instructions
  clustered_environment: Clustered Environment
  post_installation_instructions: Post-Installation Instructions
  installer_backups: Installer Backups
  pingidmam_integration_for_7_0: PingIDM/AM Integration for 7.0
  patchingupdating_process: Patching/Updating Process
---

# Installation

The following chapter provides details about the Identity Governance installation.

## Provided Files

The installer is provided in the `identity-governance-winter-2021.zip` archive. The top-level directory contains the following files and directories:

* **install.sh**. Linux installer.

* **install.bat**: Windows installer.

* **governance.groovy**: Common installer, invoked by both Linux and Windows installers.

* **governance.properties**: Properties file that can be used in place of interactive input with the installers.

* **legal-notices**: Contains the Ping Identity license agreement and any third party licensing agreements.

* **openidm**: Files to be installed in the PingIDM home directory. These files include configuration files, scripts, workflows, CLI tools, user interface configuration and file fragments that is injected into existing files.

* **integrations**: Files and scripts used to make adjustments to out of the box Ping Identity PingIDM configuration files.

## Installation Instructions

1. Unzip the `identity-governance-winter-2021.zip` to a temporary directory then navigate to the directory that was unzipped.

2. Run the following command to initiate the installer:

   ```
   For Windows:
   install.bat [--properties filename | -p filename]

   For Linux:
   ./install.sh [--properties filename | -p filename]
   ```

   The installer prints updates to the console until successful completion.

The command can be run with the following optional argument: \* -`-properties` or `–p <location/of/properties/file>`: Provides a properties file for script input. If no properties file is specified, the user must input the following properties at run time.

The following input is used for the installer: \* **openidm\_location**: File location of PingIDM home directory.

* **project\_location**: File location of PingIDM project directory, if used. This is an optional property that defaults to the `openidm_location` if left blank.

* **identity\_governance\_installer\_location**: Location where the installer is being run from

* **openidm\_version**: The version of PingIDM. This is either 6.5 or 7.0.

* **initial\_install**: If this is the first install in a cluster of installs

|   |                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------- |
|   | Names are those found in the properties file. If a properties file is not used, equivalent input is gathered directly from the installer. |

3. After installation completes, the PingIDM server must be restarted.

## Clustered Environment

Currently, the installer script can only be run once per environment. In a clustered environment, manual steps need to be taken to copy over artifacts to subsequent nodes once the installer has run on the initial node. The following requires replication on each node after the first:

1. Copy the following files from the installer zip into the PingIDM installation directory:

   1. Everything in the `./openidm/script` directory, copied into the script directory of the installation.

   2. Everything in the `./openidm/conf` directory, copied into the conf directory of the installation.

   3. Everything in the `./openidm/workflow` directory, copied into the workflow directory of the installation.

   4. Everything in the `./openidm/tools` directory, copied into the tools directory of the installation.

   5. The entire `./openidm/governance` directory, copied into the `openidm` installation directory.

   6. The entire `./legal-notices` directory, copied into the `openidm` installation directory

2. Copy the following files from the first node's PingIDM installation directory:

   * `openidm/script/access.js`

   * `openidm/conf/managed.json`

   * `openidm/conf/policy.json`

## Post-Installation Instructions

The UI context for Identity Governance can be found by navigating to `/governance` from your PingIDM server URL.

Additional configuration is needed on each node as described below:

* **Administrator Roles**. For a user to access the administrator functionality of Identity Governance, they must be assigned the intended internal authorization role (`governance-administrator`, `access-request-admin`, or `glossary-admin`) that was created during installation. Note that if you are assigning the role to the currently logged in user you must log out and back in again for the role to take effect, and internal users (for example, , `openidm-admin`) are not supported by Identity Governance}.

* **Enable Workflow**. If planning to use the PingIDM workflow functionality for certification remediation or custom request flows, Identity Governance requires workflow to be enabled in the PingIDM administrator configuration. To do so, navigate to Configuration > System Preferences > Workflow and toggle the Enable setting.

* **Setting the membershipProperties configuration**. Administrators have the ability to determine which default managed user property is used to determine membership for group assigned approvals, either `roles` or `authzRoles`. If 'roles' is selected, users that are assigned a managed role to their Provisioning Roles attribute ('roles' in the schema) are eligible to approve tasks assigned to that managed role. If 'authzRoles' is selected, users that are assigned a role to their Authorization Roles attribute ('authzRoles') is eligible to approve tasks assigned to that role. In previous versions of Access Request this was always determined by the Authorization Roles property.

  To edit this configuration, open the file found at `openidm/conf/commons.json` and edit the `membershipProperties` array value. By default the configuration contains both `'authzRoles'` and `'roles'` as options; however, it is recommended that only one is chosen. Note that only those two properties are currently supported as options for determining group membership.

* **Event-Driven Certifications**. To enable event based certifications for managed users or other managed objects, the following snippet of code (in JavaScript) must be added to the `onUpdate` hook for each individual object that you want to create certifications for:

  ```
  require('script/idg/onUpdateManagedObject.js').triggerCerts(oldObject,newObject, 'user');
  ```

  where 'user' should correspond to the managed object you are editing (for example, , 'role', 'assignment', etc.)

* **Reactive Policy Scans**. To enable reactive policy scans on managed users, the following snippet of code (in JavaScript) must be added to the postUpdate hook for the managed user object:

  ```
  if(request.method.equals('update') || request.method.equals('patch'))
    openidm.action('governance/policyScan', 'reactive', { userId: object._id });
  ```

  |   |                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | After installation steps are complete, it is recommended that the installer ZIP and the created installation folders and files be removed from the server. |

## Installer Backups

As part of the installation process, backups of any PingIDM files that are changed or edited are created within the `openidm/backup` folder. The file names follow the pattern of `<original file name>.pre-accessreview-install-<timestamp>`, and are located within the same subdirectories of the backup folder as they would be in the original `openidm` directory.

## PingIDM/AM Integration for 7.0

If installing Identity Governance into an PingIDM environment that is configured to authenticate through Access Management, you must configure an OAuth client in AM for the Governance context.

To start, refer to section 2.1.2 of the Ping Identity Platform Setup Guide found at the following url: [Configure OAuth Clients](https://backstage.pingidentity.com/docs/platform/7/platform-setup-guide/#proc-auth-clients).

In step 5 of the section, instructions are given to configure a client for the end-user-ui. For Identity Governance, please repeat those steps with the following adjustments:

* Client ID: `identity-governance-ui`

* Core:

  * Redirect URIs: \<IDM domain>/governance/appAuthHelperRedirect.html

* Advanced:

  * Subject Type: Public

In the Ping Identity Platform admin interface, click on Applications and then Add Application. The data entered in this form should match the configurations included in the AM client.

## Patching/Updating Process

If installing a patch update to the current installation the following steps are recommended to ensure proper installation of the update. For updating a major version of the product (for example, 2.5 > 3.0), consult the release notes for any instructions on the upgrade process.

1. Check the patch/update zip for a README file and confirm if there are any additional actions that need to be taken for the specific patch or update. Any steps found within this file should take precedence over the steps found below.

2. Manually create a backup of the following directories with the `openidm` installation: `/conf`, `/script/idg`, `/script/commons`, `/governance`, and `/workflow`.

3. Unzip the provided patch/update into the `openidm` directory

4. Restart the PingIDM server.

|   |                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the event the update needs to be backed out and reverted, simply copy the backup directories back into the `openidm` directory to overwrite the new changes and restart the server once again. |

---

---
title: System Settings
description: Users who are assigned to either the governance-administrator or access-request-admin internal authorization role sees the System Settings tab under the Configuration subsection on the side taskbar. Navigating to this screen allowa the user to adjust any of the configuration options within the system.
component: identity-governance
version: 7.1.2
page_id: identity-governance:admin-guide:chap-system-settings
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/admin-guide/chap-system-settings.html
section_ids:
  network: Network
  display: Display
  delegation: Delegation
  custom_attribute_mapping: Custom Attribute Mapping
  autonomous_identity_integration: Autonomous Identity Integration
  menu_management: Menu Management
  review: Review
  risk_level_management: Risk Level Management
  request: Request
  general: General
  approval_options: Approval Options
  display_2: Display
  about: About
---

# System Settings

Users who are assigned to either the governance-administrator or access-request-admin internal authorization role sees the System Settings tab under the Configuration subsection on the side taskbar. Navigating to this screen allowa the user to adjust any of the configuration options within the system.

![iga system settings general tab](_images/iga-system-settings-general-tab.png)

## Network

Server Hostname: This field is used to define the alias for the PingIDM environment that is running the Identity Governance application. This setting is used in email notifications to directly link users to a request, approval task, etc., among other places.

## Display

User Display Format: This field is used to define the custom display format for a user within the Identity Governance module. The value set in this field is used to dynamically display user names, so any field that leverages this property automatically updates to show the defined format once saved.

To define a display format, simply enter the desired string into the input, using double curly braces to define a user attribute on the managed user object that you want to display. A few examples are defined below:

```
{{userName}}                            -  	jsmith
{{givenName}} {{sn} {{userName}}        - 	John Smith (jsmith)
{{givenName}} {{sn}} - {{jobCode}}	-	John Smith - AB123
{{sn}}, {{givenName}}                   -	Smith, John
```

### Delegation

Identity Governance allows administrators to enable a property within PingIDM that is used to delegate all of a user's tasks for certifications, violations, and approvals. If delegation is enabled and the user has a relationship to another managed user through the defined property, then delegation occurs for that user when a task is set to be assigned to them. In the event that the defined property is not a relationship property, is not a relationship property to a managed user, or is not defined for a given user, then delegation is ignored and the user is assigned tasks as they normally would be. When delegation does occur, it is assigned directly to the new user during task creation and won't be visible to the original intended recipient.

* Allow User Delegation: If enabled, the system attempts to leverage the defined User Delegation property to assign tasks.

* User Delegation Property: Select any property from the managed user schema that should be used to determine a user's delegate.

### Custom Attribute Mapping

To display user information throughout the user interface, Ping Identity Access Review relies on the values stored in the out-of-the-box PingIDM attributes username, givenName, sn, and email. However, to accommodate those implementations that use alternative custom attributes to store this basic information, an administrator can choose to map those attributes to the values available in this setting.

![iga custom attribute mapping](_images/iga-custom-attribute-mapping.png)

### Autonomous Identity Integration

For those implementations that are running Ping Identity Identity Governance in parallel with Ping Identity Autonomous Identity, these settings are used to allow the application to communicate with AutoID and enable some of the advanced recommendations that it provides.

* AutoID Enabled: Whether or not to enable the AutoID integration

* AutoID URL: Hostname of the AutoID server

* AutoID User: Username of the user admin or service account to make API calls with

* AutoID Password: Password of the above user/account

### Menu Management

Menu Management allows an administrator to add / remove links to the top-right user dropdown menu for easier navigation to other applications that would be beneficial to the end user.

![iga menu management setting](_images/iga-menu-management-setting.png)

1. To add links to the menu, select Add. A new blank row to be filled in appears.

2. Enter the name of the link in the name field and the URL next to it.

3. You can add multiple links at once by continuing to click the add button to show more blank rows.

4. To reset the links back to their saved value, click the reset button.

5. Once the settings have been saved, users are able to see the navigation links in the dropdown menu at the top of the page.

   ![iga menu links user dropdown](_images/iga-menu-links-user-dropdown.png)

## Review

![iga system settings review](_images/iga-system-settings-review.png)

* Allow Bulk Certify: If set to True, certifiers are able to certify all users at once for a specific campaign. If set to False, certifiers need to certify each user individually.

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | It is best practice to set the Allow Bulk Certify option to False as it prevents 'rubber stamping' |

### Risk Level Management

Risk level Management allows an administrator to adjust levels of risk defined as Low, Medium and High.

![iga risk level management slider](_images/iga-risk-level-management-slider.png)

Drag tabs to adjust the levels of risk. As tabs move, the adjustment is reflected in the table below the bar. The leftmost tab sets the delimiter between Low risk and Medium risk, where the tab value is the inclusive upper boundary of the Low level of risk. Similarly, the rightmost tab sets the delimiter between Medium and High risk, where the tab value is the inclusive upper boundary of the Medium level of risk.

## Request

![iga system settings request tab](_images/iga-system-settings-request-tab.png)

### General

Check Requests Against Policies: Enables the application to leverage policies defined in Access Review when a user attempts to submit a request. If set to true, and a user attempts to submit a request that would violate an existing policy, they are presented an error message in the Review section of their request explaining what policy is being violated. This blocks the user from submitting the request unless it is altered to meet policy conditions.

Max Filename Length: Sets the max allowable size of a submitted filename, in characters. Access Request saves submitted files to the PingIDM repository within the files table of the database. To increase this setting, the size of the column for filename within that table must first be increased to store longer strings of text. The default value of 25 allows Access Request to save files properly using the default value for that column as installed.

### Approval Options

Require Comment on Reject: Requires an approver to add a comment to their approval task submission for any item that they choose to reject.

Require Comment on Approval: Requires an approver to add a comment to their approval task submission for any item that they choose to approve.

Enable Approver Reassign: Allows approvers the ability to reassign their own tasks to another user or group.

Enable Auto Approval: If set to true, any time an approver for a task is calculated to be the same user as the one who submitted the request (for example, a manager submits a request for their requestee, and the item requires manager approval,) that task is auto-approved and won't require manual approval by the requester. The item automatically advances to the next approver within its approval chain.

Enable Auto Approval for Group: If set to true, functions the same as the above setting, but applies to any approval tasks that are assigned to a group that the requester belongs to. As an example, there is a requestable item requiring approval from a manager and an admin group, and a member of that admin group submits a request for the item. The approval goes to the manager, and if approved, then is auto-approved by the admin group that the requester belongs to.\`

Days to Complete Approval Task: The number of days allowed for an approval user or group to act on an approval request before the task "expires." Note that task expiration doesn't mean that the request is removed or the approval is rejected. In the event that a task is not completed by the 'Due Date', it is automatically reassigned to the group defined below it with the Default Group for Approval setting. That team is then be responsible for determining which user should be given the task for completion, or alternatively cancel it.

Default Group for Approval: The group that is assigned to handle approval tasks in the following situations:

* When an approver key is set on a requestable item but can not be found during task creation (for example, manager is not set on user, entitlementOwner that is not set on object)

* When a task reaches its expiration date

Default Approvers: This list is applied as the de facto approval chain for any item that is set as requestable but doesn't have an approvers key defined. It functions the same as the list would if it were defined the exact same way on the requestable item itself.

|   |                                                                                                                                                                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The options for enabling auto-approval and default approvers, do not automatically apply to any requestable item using a custom workflow, as they follow their own logic and approval process. However, they can be leveraged within those flows, if desired, by using the API to read the setting values. |

### Display

Displayable User Properties: The properties on the managed user schema that are displayed within the popup page in requests and approval tasks when the user hovers over a user's userName.

Displayable Item Properties: The keys on the requestable item glossary entry that are displayed within the popup page in requests and approval tasks when the user hovers over the item's info icon.

User Search Properties: The properties on the managed user schema that are used to search against when a user queries for users during request creation or reassignment.

Requestable Item Search Properties: They keys on the requestable item glossary entry that are used to search against when a user queries for items to add to request.

Requestable Item Display Format: Format used to display requestable items within the user interface. See the user display format in section 6.1 above for information on syntax.

Requestable Item Bundle Display Format: Format used to display requestable item bundles within the user interface. See the user display format in section 6.1 above for information on syntax.

### About

The about tab of the System Settings allows the user to see some basic information about the current version of the product that is installed. This information can be useful in debugging or diagnosing any issues or bugs through Ping Identity support.