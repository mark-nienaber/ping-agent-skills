---
title: Admin User Tasks
description: The Admin user functionality is similar to that of a system administration superuser. Admin users have the access rights to company-wide entitlement data on the Ping Autonomous Identity console. Admin users can approve or revoke a user's entitlement.
component: autonomous-identity
version: 2022.11.12
page_id: autonomous-identity:users-guide:chap-admin-user-tasks
canonical_url: https://docs.pingidentity.com/autonomous-identity/2022.11.12/users-guide/chap-admin-user-tasks.html
section_ids:
  admin-tasks: Performing Admin Tasks
---

# Admin User Tasks

The Admin user functionality is similar to that of a system administration *superuser*. Admin users have the access rights to company-wide entitlement data on the Ping Autonomous Identity console. Admin users can approve or revoke a user's entitlement.

## Performing Admin Tasks

> **Collapse: Investigate Most Critical Entitlements**
>
> One important task that an administrator must perform is to examine all critical entitlements. Critical entitlements are assigned entitlements that have are highly-assigned but have a low confidence score associated with it. The Ping Autonomous Identity console provides a means to examine these entitlements.
>
> Follow these steps to evaluate the most critical entitlements list:
>
> 1. On the Dashboard, scroll down to the Most Critical Entitlements section. This section displays the entitlements that have low confidence scores and a high number of employees who have this entitlement.
>
> 2. Click an entitlement to view its details.
>
> 3. On the Entitlements detail page, review the key metrics.
>
> 4. Click the right arrow in one of the category ranges to view the users, and then click one of the users in the list.
>
> 5. On the User's Entitlements page, scroll down to review the Confidence Score Comparison table to see the differences between the user's attribute and the driving factor attributes.
>
> 6. Click Employees associated with this entitlement to review other uses who have this entitlement.
>
> 7. Click Actions, and then click Approve or Revoke for this entitlement. You can also bulk approve more than one entitlement. You can only revoke one entitlement at a time.
>
> > **Collapse: Click an example**
> >
> > ![investigate most critical](_images/investigate-most-critical.gif)

> **Collapse: Approve or Revoke Access an Entitlement for a User**
>
> Follow these steps to investigate a confidence score and approve or revoke access an entitlement assigned to a specific user:
>
> 1. On Ping Autonomous Identity console, click Identities, and enter a name of a supervisor. The only way to access a user's entitlements is through the Most Critical Entitlements section or the Identities page.
>
> 2. On the Identities page, click a circle, and then click the user in the list on the right.
>
> 3. On the User Entitlement page, click a confidence circle on the graph to highlight the entitlement below.
>
> 4. For the selected entitlement, click the down arrow on the right to view the Driving Factor Comparison.
>
> 5. Click Employees associated with this entitlement to view the justifications for those users with high confidence scores with this entitlement.
>
> 6. Click Actions, and then click `Approve Access` or `Revoke access`. If you have more than one entitlement that you want to approve, select them all and do a bulk Approval. You can only do one Revoke Access at a time.
>
> > **Collapse: Click an example**
> >
> > ![approve revoke access admin](_images/approve-revoke-access-admin.gif)

> **Collapse: Check Non-Scored Users**
>
> Follow these steps to check Not Scored entitlements. Not scored indicates that it doesn't have a justification associated with the entitlement:
>
> 1. On Ping Autonomous Identity console, click Identities, and enter a name of a supervisor. The only way to access a user's entitlements is through the Most Critical Entitlements section or the Identities page.
>
> 2. On the Identities page, click a circle, and then click the user in the list on the right.
>
> 3. On the User Entitlement page, click Not Scored.
>
> 4. On the Not Scored Entitlements page, click the down arrow to view the driving factors comparison.
>
> 5. Click Employees associated with this entitlement to view the justifications for those users with high confidence scores with this entitlement.
>
> 6. Click Actions, and then click`Approve Access` or `Revoke access`. At a later date, you can re-click the Approve or Revoke button to cancel the operation.
>
> > **Collapse: Click an example**
> >
> > ![entitlements not scored admin](_images/entitlements-not-scored-admin.gif)

> **Collapse: Apply Filters**
>
> Follow these steps to apply filters to your confidence score graphs on the Identities and Entitlements pages:
>
> |   |                                                                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> |   | The Filters for the Identities and Entitlements are similar. The filters for the Applications and Rules pages offer different options to filter your searches. |
>
> 1. On the Identities or Entitlements page, view the average confidence score graph.
>
> 2. On the right, click Filters.
>
> 3. Under filters, do one or all of the following:
>
>    * Click `Remove High Scores from Average` or enable any filter in the Application Filters section.
>
>    * Under Applications, click one or more applications to see the identities or entitlements asssociated with the selected application.
>
>    * Click Add Filters to further see only those identities or entitlements based on a user attribute, such as `city`. When ready, click Apply Filters.
>
> 4. Click Clear Filters to remove your filters.
>
> > **Collapse: Click an example**
> >
> > ![apply filters admin](_images/apply-filters-admin.gif)
