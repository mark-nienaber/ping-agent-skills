---
title: ACIs
description: To add, modify, or remove access control instructions (ACIs), submit a request through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_acis
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_acis.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# ACIs

To add, modify, or remove access control instructions (ACIs), submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

Global ACIs are a set of ACIs that can apply to entries anywhere in the server, although they can also be scoped so that they only apply to a specific set of entries. These ACIs work in conjunction with access control rules stored in user data and provide a convenient way to define ACIs that span disparate portions of the DIT (Directory Information Tree).

You can apply Global ACIs to administrator access, anonymous and authenticated access, delegated access to a manager, or used for proxy authorization. Access control components, descriptions, and the syntax used for each component are listed in the following table:

| Access Control Components | Description                                                                                            | Syntax                                                                                                       |
| ------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| targets                   | Specifies the set of entries and/or attributes to which an access control rule applies.                | ```none
(target keyword = || != expression)
```                                                              |
| name                      | Specifies the name of the ACI.                                                                         |                                                                                                              |
| permissions               | Specifies the type of operations to which an access control rule might apply.                          | ```none
allow||deny (permission)
```                                                                         |
| bind rules                | Specifies the criteria that indicate whether an access control rule should apply to a given requester. | ```none
bind rule keyword = ||!= expression;
```The bind rule syntax requires a terminating semicolon (`;`). |

To learn more, see [Global ACIs](http://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_global_acis.html) in the *PingDirectory Server Administration Guide*.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingDirectory service request → ACIs**.

3. In the **Access control instruction** field, provide the instruction. Include the name of the ACI, targets, permissions, and bind rules.

4. Select the appropriate description in the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. In the **Description** field, provide additional information regarding the request.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.
