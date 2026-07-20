---
title: Access authorization
description: Configure access authorization using scopes to delegate user and entitlement management
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/governance-lcm-authorization
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-lcm-authorization.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["LCM", "user management", "authorization", "scopes", "permissions", "internal roles"]
section_ids:
  configure-authorization-using-scopes: Configure authorization using scopes
  add_scopes_and_assign_to_users: Add scopes and assign to users
  create_an_internal_role: Create an internal role
---

# Access authorization

Before you can delegate user and entitlement management to designated end users, you must configure access authorization using scopes. Access authorization defines what actions a delegated administrator can perform and on which set of users.

## Configure authorization using scopes

Scope permissions grant a specific subset of permissions for user management.

Permissions for user management are as follows:

| Permission  | Description                                                                                                                                                                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create User | Allows the end user to create new users in the system.This global permission overrides a scope's target conditions. For example, even if a scope is set to target only contractor users, a person with this permission can create any type of user, not just contractors. |
| Modify User | Allows the end user to modify the users matching the filter.                                                                                                                                                                                                              |
| Delete User | Allows the end user to delete the users matching the filter.                                                                                                                                                                                                              |
| View Grants | Allows the user to view the access of the matching users, for example, applications, entitlements, and roles.                                                                                                                                                             |

## Add scopes and assign to users

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. Go to Governance > Scopes.

3. Click [icon: add, set=material, size=inline] New Scopes.

4. On the New Scope page, enter the following in the Details section:

   1. Name: Enter the name for the scope.

   2. Description: Enter a description for the scope.

   3. Click Next.

      ![Scope details page displaying name and description](../_images/governance-user-lcm-scope-details.png)

5. On the Applies to page, define which users should be subject to this scope.

   1. Select if the All or Any condition must be met.

   2. Select a property for this scoping rule. For example, select userName.

   3. Select an operator for the scoping rule. For example, select contains.

   4. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

   5. Click Next.

      ![Scope \`applies to\` page defining the user to which the scope applies.](../_images/governance-user-lcm-scope-applies-to.png)

6. If you're granting user permissions, configure the following on the Access page:

   1. Select the Users checkbox.

   2. Select if All or Any condition must be met.

   3. Select a property for this scoping rule. For example, select accountStatus.

   4. Select an operator for the scoping rule. For example, select is.

   5. Enter a condition. For example, enter active.

   6. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

   7. Select the permissions available to the scope:

      * Create Users: Permission to create a new user.

      * Modify User: Permission to modify a user.

      * Delete User: Permission to delete a user.

      * View Grants: Permission to view the access for the users matching the scope filter.

   8. Click Save.

      ![Scope access matching the conditions.](../_images/governance-user-lcm-scope-access.png)

## Create an internal role

Administrators must create an internal role so that authorized end users can view the Users identity object.

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. Go to Identities > Manage.

3. Click Internal Roles > [icon: add, set=material, size=inline] New Internal Role.

   1. In the New Internal Role modal, enter the following and click Next.

      * Name: Enter a name for the internal role, such as UserLCMTest.

      * Description: Enter a description for the internal role.

        ![Creating a new internal role](../_images/governance-user-lcm-new-internal-role.png)

   2. In the Internal role Permissions modal, select Alpha realm - Users managed/alpha\_user, and click [icon: add, set=material, size=inline] Add.

      1. Click the internal role permissions you want available with the role:

         * View

         * Create

         * Update

         * Delete

      2. Click Show advanced. Select Read/Write for the attribute permissions and click Next:

         * userName

         * givenName

         * cn

         * sn

         * mail

           ![Internal role permissions](../_images/governance-user-lcm-internal-role-permissions-expanded.png)

      3. In the Dynamic Internal role Assignment modal, click Next.

      4. In the Time Constraint modal, click Save.

4. In the UserLCMTest page, click [icon: add, set=material, size=inline] Add Members.

   1. In the Add Members modal, select the users to which the internal role applies, and then click Save.

---

---
title: Access Modeling
description: Run role mining jobs and examine candidate roles generated by machine learning analysis
component: pingoneaic
page_id: pingoneaic:identity-governance:end-user/iga-access-modeling-end-user
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/end-user/iga-access-modeling-end-user.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  what_is_access_modeling: What is Access Modeling?
  what_is_confidence_scoring: What is confidence scoring?
  before_you_begin: Before you begin
  run-a-role-mining-job: Run a role mining job
  search_roles_using_the_filter: Search roles using the filter
  examine-role-details: Examine role details
  examine-role-entitlements: Examine role entitlements details
  examine-role-members: Examine the role's members
  examine-role-access-patterns: Examine the role's access patterns
  create-drafts-and-publish-roles: Create drafts and publish roles
  maintain-and-export-roles: Maintain and export roles
  delete_a_role: Delete a role
  keep-roles-aligned: Keep roles aligned with your access landscape
---

# Access Modeling

This section is for Identity Governance users, such as role owners and governance analysts, who use Access Modeling but don't configure it.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Identity Governance add-on capabilityAccess Modeling is an additional add-on capability for PingOne Identity Governance. Contact your Ping Identity representative if you want to add the Access Modeling (Role Mining) add-on SKU to your PingOne Advanced Identity Cloud Identity Governance subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

Authorized access modeling administrators who are part of the `access-modeling-administrator` group can run a role mining job in the Advanced Identity Cloud end-user UI.

|   |                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Best practice is to run the role mining job on a daily basis. This cadence lets Identity Governance capture access and attribute changes and refresh recommendations. It keeps roles aligned with real-world usage. However, depending on your environment and how quickly access changes, you might run the job more or less frequently. |

## What is Access Modeling?

Access Modeling (also known as *role mining*) analyzes existing user-to-entitlement assignments and discovers candidate access roles describing how people use access in your environment. It uses advanced machine learning algorithms and analytics thresholds to:

* Examine current roles and entitlements across your access landscape.

* Propose new role candidates and changes to existing roles.

* Calculate confidence scores and driving factors for each role and entitlement assignment.

## What is confidence scoring?

Every entitlement assignment has a confidence score. The score answers a simple question: of all employees who share this end user's relevant attributes (like job function, department, and location), what percentage also hold this entitlement?

A score of 0.93 means 93% of comparable employees have this access. A score of 0.12 means almost no one with this end user's profile has it.

Identity Governance computes the score from observed data across your entire population. It reflects actual provisioning patterns rather than any single approver's judgment or any one team's interpretation of policy.

* High-confidence assignments are consistent with how the organization actually operates.

* Low-confidence assignments warrant review.

## Before you begin

Before you can use Access Modeling, make sure that:

* Your organization has purchased and enabled the Access Modeling add-on capability for Identity Governance. If you don't see the Access Modeling page in the Advanced Identity Cloud end-user UI, contact your Identity Governance or Advanced Identity Cloud tenant administrator to confirm whether the feature is enabled for your organization.

* You have the correct permissions. To run a role mining job, you must be in the `access-modeling-administrator` group. To manage roles, you might need to be designated as a role owner. Contact your Identity Governance or Advanced Identity Cloud tenant administrator if you believe you should have access.

### Run a role mining job

The role mining job is part of the Identity Governance machine learning analytics pipeline. It processes the latest access data and generates candidate roles and updates to existing roles based on observed patterns in your environment.

|   |                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Only users in the `access-modeling-administrator` group and governance administrators can run the role mining job on the Advanced Identity Cloud end-user UI. If you don't have access, contact your administrator. |

To run the role mining job:

1. In the Advanced Identity Cloud end-user UI, sign on as an end user who has role mining permissions.

2. Click Access Modeling.

3. Click Run Role Mining Job. The system queues the role mining job in the analytics pipeline. When you select the button, Identity Governance runs the role mining job with the current configuration and thresholds.

   |   |                                                                                                                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Only one role mining job can run at a time. Depending on your environment size and analytics load, the job can take from several minutes to a few hours to complete. After the Run Role Mining button becomes active again, you'll know the job completed. |

   ![Access Modeling UI accessible for authorized end users](../_images/governance-end-user-access-modeling.png)

### Search roles using the filter

Most companies have a large number of roles within their system. The Access Modeling page provides a useful filter to locate specific roles.

1. In the Advanced Identity Cloud end-user UI, click Access Modeling.

2. On the Access Modeling page, click Show Filters.

3. On the Filter Roles modal, select the criteria you want to filter by:

   * Entitlement: Display only roles that include a specific entitlement.

   * Status: Select Candidate or Draft.

   * Users: Number of users in the role.

   * Minimum number of members: Display only roles with at least minimum specified members.

   * Minimum number of entitlements: Display only roles with at least the minimum specified entitlements.

4. Click Apply Filters.

### Examine role details

For each candidate or existing role, Access Modeling provides a Details tab.

To examine a specific role:

1. On the Access Modeling page, select a candidate, draft, or active role.

2. On the role details page, review the following information:

   | UI element                    | Description                                                                                             |
   | ----------------------------- | ------------------------------------------------------------------------------------------------------- |
   | General role information      | Displays when the role mining analytics were last refreshed, role status, and role identifier.          |
   | Export                        | Downloads the role definition JSON for use outside the UI.                                              |
   | Identity Coverage             | Displays what percentage of identities are currently in this role.                                      |
   | Average Assignment Confidence | Displays the average confidence score for entitlements in this role.                                    |
   | Name                          | Lets you edit the display name for the role.                                                            |
   | Description                   | Lets you add a short explanation of what the role is for.                                               |
   | Requestable                   | Designates a role as searchable and requestable in the Access Modeling page and other governance areas. |
   | Role Owner                    | Assigns a role owner responsible for managing this role.                                                |
   | Delete                        | Removes the role from access modeling.                                                                  |
   | Create Draft                  | Creates a draft version of the role you can refine and publish.                                         |

### Examine role entitlements details

For each candidate or existing role, Access Modeling provides an Entitlements tab that displays the entitlements included in the role and their confidence scores.

1. On the Access Modeling page, select a candidate, draft, or active role.

2. Click the Entitlements tab.

3. On the role details page, review the following information:

   | UI element   | Description                                                                               |
   | ------------ | ----------------------------------------------------------------------------------------- |
   | Entitlements | Lists the entitlements included in the role. Click the entitlement to review its details. |

### Examine the role's members

For each candidate or existing role, Access Modeling provides a members tab displaying the users included in the role and their attributes.

1. On the Access Modeling page, select a candidate, draft, or active role.

2. Click the Members tab.

3. On the role members page, review the following information:

   | UI element             | Description                                                                                                                                                                                          |
   | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Attribute Distribution | Introduces the chart that summarizes member attributes.                                                                                                                                              |
   | Attribute selector     | Lets you choose which attribute to analyze in the distribution chart. If you're not sure what an attribute means, learn more in [Examine the role's access patterns](#examine-role-access-patterns). |
   | Attribute distribution | Displays how many members share the selected attribute value.                                                                                                                                        |
   | Search                 | Filters the members list by username or other visible data.                                                                                                                                          |
   | Username               | Displays each member's username.                                                                                                                                                                     |
   | Attribute              | Displays key attribute values (such as manager, location, or flags) for each member.                                                                                                                 |

### Examine the role's access patterns

For each candidate or existing role, Access Modeling provides an Access Patterns tab displaying the rules that define the driving factors for the machine learning analytics job.

1. On the Access Modeling page, select a candidate, draft, or active role.

2. Click the Access Patterns tab.

3. On the role access patterns page, review the following information:

   | UI element      | Description                                                                                                              |
   | --------------- | ------------------------------------------------------------------------------------------------------------------------ |
   | Sort by         | Displays options to sort access patterns, such as by Attribute Count or User Count and by Ascending or Descending order. |
   | Users           | Displays how many users match the access pattern.                                                                        |
   | Attribute label | Displays the name of a user attribute used in the pattern.                                                               |

### Create drafts and publish roles

Access Modeling lets authorized users review discovered candidate roles.

1. On the Access Modeling page, select a candidate role.

2. Review the role details, entitlements, members, and access patterns.

3. Click Create Draft. This creates a draft role based on the candidate role, which you can refine and publish.

   |   |                                                                                                                                                                                   |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You'll see an additional Recommendations tab. In the Recommendations tab, you can review and accept or reject suggested changes to the role definition based on other candidates. |

4. Update the role draft, and then click Publish. This submits the role for approval and publishing to Identity Governance.

5. In the Request Submitted modal, click View Request to see the request details and approval workflow.

6. If the request is approved, Identity Governance creates the role and marks it as `Active`. If the request is rejected, click Comments to view the error message or feedback from the approver.

### Maintain and export roles

Over time, use Access Modeling to keep roles accurate and useful:

* Rerun the role mining job daily to capture changes in access and refresh recommendations.

* Create new drafts from existing active roles when mining suggests significant changes or when roles become stale.

* Unpublish or delete roles that no longer represent meaningful patterns.

To export the role definition:

1. On the Access Modeling page, select a candidate role.

2. Review the role details, entitlements, members, and access patterns.

3. Click Export to download the role definition as JSON for offline analysis or integration with other systems.

### Delete a role

Access Modeling lets role admins and role owners delete a draft or candidate role.

1. On the Access Modeling page, select a candidate or draft role.

2. Review the role details, entitlements, members, and access patterns.

3. Click Delete.

### Keep roles aligned with your access landscape

As a role owner, governance analyst, or other Identity Governance end user, you can help keep Access Modeling effective by:

* Reviewing new candidate roles after each analytics run.

* Cleaning up roles that no longer represent meaningful patterns (for example, roles with very low membership or stale entitlements).

* Providing feedback to administrators when thresholds are too strict or too permissive based on what you see in the UI.

* Together, administrators and end users use Access Modeling to maintain a clean, accurate set of roles that reflect real-world access and support effective governance.

---

---
title: Access Modeling
description: Administer access modeling including role mining, confidence scoring, and role lifecycle management
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/iga-access-modeling-admin
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/iga-access-modeling-admin.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  what_is_confidence_scoring: What is confidence scoring?
  why_mine_roles: Why mine roles?
  how_does_identity_governances_top_down_access_modeling_help_in_compliance: How does Identity Governance's top-down access modeling help in compliance?
  role_states: Role states
  for_identity_governance_administrators: For Identity Governance administrators
  before_you_start: Before you start
  role_user_types: Role user types
  roles_workflow: Roles workflow
  role_mined_and_custom_roles: Role-mined and custom roles
  configure-access-modeling-thresholds: Configure access modeling thresholds
  configure_access_modeling_administrators: Configure access modeling administrators
  run_an_access_modeling_job: Run an access modeling job
---

# Access Modeling

Access Modeling (also known as *role mining*) analyzes existing user-to-entitlement assignments and discovers candidate access roles describing how people use access in your environment. It uses advanced machine learning algorithms and analytics thresholds to:

* Examine current roles and entitlements across your access landscape.

* Propose new role candidates and changes to existing roles.

* Calculate confidence scores and driving factors for each role and entitlement assignment.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Identity Governance add-on capabilityAccess Modeling is an additional add-on capability for PingOne Identity Governance. Contact your Ping Identity representative if you want to add the Access Modeling (Role Mining) add-on SKU to your PingOne Advanced Identity Cloud Identity Governance subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

## What is confidence scoring?

Every entitlement assignment carries an implicit question: should this end user have this access? At enterprise scale, no reviewer can independently evaluate every single access assignment from scratch. Confidence scores provide the answer empirically.

Identity Governance analyzes your workforce data, for example `job function`, `department`, `location`, `cost center`, and other HR attributes, alongside existing entitlement assignments. It discovers which combinations of attributes reliably predict which entitlements. For each user-entitlement pair, the confidence score answers a simple question: of all employees who share this end user's relevant attributes, what percentage also hold this entitlement? A score of 0.93 means 93% of comparable employees have this access. A score of 0.12 means almost no one with this end user's profile has it.

Identity Governance computes the score from observed data across your entire population. It reflects actual provisioning patterns rather than any single approver's judgment or any one team's interpretation of policy. High-confidence assignments are consistent with how the organization actually operates. Low-confidence assignments warrant review.

The same mechanism powers [access recommendations](governance-recommendations-preface.html). When an end user joins or changes roles, Identity Governance evaluates their updated attributes against known patterns and surfaces entitlements where confidence exceeds your configured threshold and the access their peers already have.

## Why mine roles?

Organizations pursue automated access modeling (or role mining) for two reasons. First, manual role engineering doesn't scale to large enterprises. You can't realistically define and maintain roles for 50,000 users and 15,000 entitlements through workshops, interviews, and spreadsheets. Automated mining turns a months-long consulting exercise into a repeatable process that covers the entire organization.

Second, access landscapes drift. People change jobs or transfer, new applications come online, and entitlements pile up. Roles that accurately described access six months ago might no longer match reality. Periodic re-mining compares newly discovered role candidates to your active roles. It flags where role definitions no longer match what the data supports and highlights new patterns that justify new roles. This gives role owners a structured, data-driven basis for governance decisions, instead of relying on periodic manual audits.

## How does Identity Governance's top-down access modeling help in compliance?

Confidence scores tell you whether an individual assignment is expected. Access modeling answers the next question: which assignments belong together?

The term "top-down" here doesn't mean someone designs roles from an organization chart and pushes them out. It means Identity Governance starts discovery from organizational attributes. HR attributes, such as `department`, `location`, and `job code`, act as the explanatory variables. Access is what gets explained. It asks: given these attributes, what access does the data predict? Access modeling is still a data-driven discovery process, but it's anchored in the structure the business already uses to describe its workforce.

The system looks at all discovered attribute-to-entitlement rules and finds places where they converge—where the same attribute combinations consistently predict the same entitlements. When it finds this pattern, it groups those entitlements into a candidate role. The attribute combinations that produced the grouping become the role's driving factors.

For example, a candidate role might appear because employees in the Finance department in the Western region almost always have the same five entitlements. The system doesn't name this role. Instead, it presents the entitlement set, the driving factors, and confidence scores for a role engineer to review, refine, and name before publishing.

Every discovered role comes with a built-in justification: the attribute combination that produced it. If an auditor asks, "Why does this role contain these entitlements?" you can point directly to the observed workforce pattern that created the role.

## Role states

Roles in access modeling have one of three states indicating their readiness for production use:

| Status    | Description                                                                                                                   |
| --------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Candidate | Suggested role generated by role mining analytics job.                                                                        |
| Draft     | A user-created draft of a role either from scratch or based on a candidate role.                                              |
| Active    | A draft role that has been approved, created in Advanced Identity Cloud identity management, and marked active in governance. |

## For Identity Governance administrators

In a typical scenario, an administrator or authorized end user runs a role mining job as part of the analytics pipeline in the Advanced Identity Cloud end-user UI. During a role mining analytics run, Identity Governance discovers candidates for new roles and displays them on the Access Modeling page with confidence scores and user access patterns. Administrators and authorized users can review these roles, make edits to entitlements and access patterns, and rerun the role mining analytics until the correct mix of entitlements meets your threshold objectives for given rules. If the threshold objectives require adjustments, administrators can make the changes in the Advanced Identity Cloud admin console. Learn more in [Configure access modeling thresholds](#configure-access-modeling-thresholds).

### Before you start

Make sure that:

* Your organization has purchased and enabled the Access Modeling SKU in your Identity Governance tenant.

* You can access the governance configuration and job scheduling pages for your Identity Governance environment.

* Set up a test user account with access to the Access Modeling user interface (UI) for testing and review purposes.

### Role user types

Identity Governance supports two user role types to manage roles within Identity Governance. You can assign these roles using the Manage Identities function.

| User type          | Description                                                                                                                                                                                                                                                                                                                         |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Role administrator | As a role administrator, you can view, edit, delete, and export all roles. Role administrators can create drafts from mined candidates and assign role owners to the draft. They can also create custom roles for further evaluation and testing. The system automatically assigns this role to Identity Governance administrators. |
| Role owner         | As a role owner, you can view, edit, delete, and export active and draft roles assigned to you.                                                                                                                                                                                                                                     |

### Roles workflow

The Access Modeling page displays roles in three states: `Candidate`, `Draft`, and `Active`.

* **Candidate**: A candidate is a template role that is discovered through the latest role mining analytics job. After each role mining job, all newly mined roles are marked as a candidate. Role admins can review a candidate and create a draft.

  |   |                                                                                                                                                                                                                                                                                                                  |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Candidate roles are read-only; you must create a draft from a candidate to change its details. Identity Governance retains candidate roles for later adjustments and for creating additional new roles until it runs the next role mining job, when it deletes all candidates and rebuilds a new candidate pool. |

* **Draft**: A draft is a role that requires review and approval by an authorized approver to become active. Role admins can re-run a role mining job to pick up the latest changes in the access landscape. The Access Modeling page displays the latest confidence scores, access patterns, and a Recommendations section that shows a suggested course of action for the role. Also, when you create a custom role, Identity Governance saves the role in draft status. You can edit the draft, publish the role for production, or delete the draft.

* **Active**: After an approver approves a draft, the role is considered *active* for production use. The role has an `Active` status and appears on the Roles page in the Advanced Identity Cloud admin console and is available for assignment to users and groups. Role owners can maintain the role over time by reviewing its access patterns and recommendations, and by re-running the role mining job to keep the role aligned with changes in the access landscape.

### Role-mined and custom roles

You can create roles in two different ways: based on role-mined candidates or custom. Role-mined roles are discovered through Identity Governance's machine learning process. The role mining job analyzes your access landscape and identifies patterns of access that form the basis of candidate roles. You can create a draft role based on a candidate role, which you can then refine and publish for production use.

You can create a new role on the Manage Identities page by selecting the [icon: add, set=material, size=inline] New Alpha realm - Role button.

|   |                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------- |
|   | Custom roles don't have recommendations as those are based on the difference between a mined role and its candidate. |

### Configure access modeling thresholds

Identity Governance implements a dedicated machine learning model configuration that controls the role mining process. These parameters determine how strict Identity Governance is when proposing new roles and help ensure that discovered roles are meaningful in production.

To configure access modeling thresholds:

1. In the Advanced Identity Cloud admin console, go to Governance > Requests.

2. On the Requests page, click the Settings tab.

3. In the Governance LCM section, click Activate.

   |   |                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Governance lifecycle management (LCM) is the underlying machine learning model that powers both Identity Governance Access Modeling and Recommendations features. |

4. In the Governance LCM modal, read what activating this feature entails, and click Next.

5. In the Governance LCM modal, click Role LCM, and then click Activate. The governance LCM is now active on your tenant.

6. In the Advanced Identity Cloud admin console, click Governance > Recommendations.

7. On the Recommendations page, click Activate Recommendations. The status changes to `Active`.

8. In the User Properties field, enter three or more user properties to use as features for role mining. These attributes help Identity Governance identify patterns in access based on user characteristics.

   |   |                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You must select at least three properties to get meaningful role mining results and to ensure the role mining job completes successfully. |

9. On the Recommendations page, set the confidence scores by moving the threshold sliders to determine whether the recommended role is listed as low, medium, or high confidence.

10. Click Save.

### Configure access modeling administrators

To control who can run role mining jobs and manage access modeling configurations, create a dedicated administrator group. Identity Governance checks user membership in this group to grant administrator permissions.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. Click Alpha realm - Groups.

3. In the New Alpha realm - Groups modal, do the following:

   * Name: Enter `access-modeling-administrator`.

   * Description: Enter a description for the group, for example, "Administrators of access modeling jobs and configurations."

4. Click Next.

5. In the Dynamic Alpha realm - group Assignment modal, skip this step, and then click Save.

6. On the access-modeling-administrator group page, click the Members tab.

7. Click [icon: add, set=material, size=inline] Add Members.

8. In the Add Members modal, select the users you want assigned to the group, and click Save.

### Run an access modeling job

The role mining job is part of the Identity Governance analytics pipeline. When enabled, Identity Governance automatically kicks off a training job to build the machine learning model based on the latest role data.

After the model is trained, governance administrators or access modeling administrators must sign on to the Advanced Identity Cloud end-user UI as a test user to run a job. The role mining job analyzes the latest access data and generates candidate roles and updates to existing roles.

To run the role mining job, learn more in [Run a role mining job](../end-user/iga-access-modeling-end-user.html#run-a-role-mining-job).

---

---
title: Access requests
description: Overview of access requests where end users request and approvers manage resource access
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/access-request-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/access-request-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Access request", "Request access", "Approve access", "Deny access", "Access catalog"]
---

# Access requests

In Identity Governance, end users can request access to resources, such as target applications, entitlements, or roles.

You define the resources end users can request by adding them to the *access catalog*.

An organization works with access requests as follows:

1. An Identity Governance administrator who can [configure access requests](access-request-configure.html). This includes defining which resources (applications, entitlements, and roles) end users can request in the access catalog.

2. After an administrator defines requestable resources in the access catalog, end users submit requests to [gain](../end-user/access-requests-request-access.html) or [remove](../end-user/access-request-revoke-access.html) (managers only) access to resources using the hosted account pages.

3. Approvers [approve or deny access requests](../end-user/access-request-approve-access.html): End users configured as the *approver* (designated owner) to review and approve or reject the request. The items that are displayed to the approver are known as *request items*.

---

---
title: Administrator tasks
description: Overview of administrator tasks for managing governance framework and identity lifecycle
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/administator-tasks-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/administator-tasks-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["administrator", "admin tasks", "getting started", "configuration", "setup", "governance"]
---

# Administrator tasks

Use the topics in this section to learn how to perform Identity Governance administrative tasks.

[icon: rocket-launch, set=fas, size=3x]

#### [Getting started](admin-ui.html)

Learn about Identity Governance.

[icon: file-user, set=fas, size=3x]

#### [Accounts](governance-accounts.html)

Learn about managing accounts.

[icon: user-shield, set=fas, size=3x]

#### [Scopes](scopes.html)

Learn about managing scopes.

[icon: key, set=fas, size=3x]

#### [Entitlements](entitlements.html)

Learn more about entitlements.

[icon: hand-wave, set=fas, size=3x]

#### [Access requests](access-request-preface.html)

Learn more about access requests.

[icon: badge-check, set=fas, size=3x]

#### [Certification campaigns](access-review-certification-preface.html)

Learn about certification campaigns.

[icon: up-right-and-down-left-from-center, set=fad, size=3x]

#### [Segregation of duties](sod-policies-preface.html)

Learn about segregation of duties.

[icon: user-gear, set=fad, size=3x]

#### [Governance lifecycle management](governance-lifecycle-mgmt.html)

Learn about governance lifecycle management.

[icon: thumbs-up, set=fad, size=3x]

#### [Recommendations](governance-recommendations-preface.html)

Learn about governance recommendations.

[icon: file-chart-column, set=fad, size=3x]

#### [Reports](iga-reports.html)

Learn about governance reports.

[icon: handshake, set=fad, size=3x]

#### [REST APIs](../rest-api/rest-api-preface.html)

Learn about Identity Governance REST APIs.

---

---
title: Agent Governance
description: Discover, onboard, and govern AI agents with Agent Governance. Apply governance controls to AI agents the same way you manage human identities.
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/iga-agent-governance
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/iga-agent-governance.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  discovery_and_governance_workflow: Discovery and governance workflow
  what_is_an_ai_agent: What is an AI agent?
  challenges_this_solves: Challenges this solves
  what_you_can_do_with_agent_governance: What you can do with Agent Governance
  understanding_connected_and_disconnected_modes: Understanding connected and disconnected modes
  summary-of-agent-governance-workflow: Summary of Agent Governance workflow
  before_you_start: Before you start
  create-the-identity-type: Create the identity type
  set_up_an_application_for_your_ai_agent_platform: Set up an application for your AI agent platform
  onboard-ai-agents: Onboard AI agents
  configure-connected-tools-as-entitlements: Configure connected tools as entitlements
  configure_synchronization_mappings: Configure synchronization mappings
  define_correlation_rules: Define correlation rules
  configure_situation_rules: Configure situation rules
  run_reconciliation: Run reconciliation
  deploy_the_platform_specific_collector: Deploy the platform-specific collector
  configure_governance: Configure governance
  create_a_certification_template: Create a certification template
  create_an_agent_policy: Create an agent policy
  create_scopes: Create scopes
  workflows: Workflows
  monitor_agent_activity: Monitor agent activity
  finalize_agent_governance_setup: Finalize agent governance setup
  assign_custodians: Assign custodians
  enrich_the_entitlement_glossary: Enrich the entitlement glossary
  test_the_setup: Test the setup
  next_steps: Next steps
---

# Agent Governance

Agent Governance lets you discover and onboard agents you've created in external AI agent platforms, such as AWS Bedrock, Azure AI Foundry, Microsoft Copilot, and Google Vertex AI, then govern them in the same way you govern human identities, accounts, and roles. This brings your automated systems under a single compliance umbrella, ensuring consistent security oversight across your entire digital workforce.

This unified approach is critical as organizations increasingly deploy these agents to automate complex business processes and decision making. Because these systems require direct access to sensitive applications, credentials, and data, they quickly become security and compliance blind spots without proper oversight, often operating with untracked permissions and zero clear accountability.

|   |                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Identity Governance add-on capabilityAgent Governance is an additional add-on capability for PingOne Identity Governance. Contact your Ping Identity representative if you want to add the Agent Governance add-on SKU to your PingOne Advanced Identity Cloud Identity Governance subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

## Discovery and governance workflow

Agent Governance fulfills four responsibilities to govern and provide visibility into agent activity:

* **Discovery and visibility**: The platform discovers agents, catalogs their capabilities, tracks their permissions, and monitors their activity after the fact.

* **Governance and remediation**: You can certify agent access, revoke permissions, assign custodians, and apply approval workflows—the same way you would for human identities.

|   |                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Runtime enforcement for agent actions happens through Agent IAM Core and Agent Gateway during the execution-time control flow for live agent requests and is outside the scope of Agent Governance. |

## What is an AI agent?

An AI agent is a type of identity, like a user or service account, that performs actions autonomously or on behalf of others. For example, querying a database, calling tools, or triggering workflows without human intervention.

Agents typically use AI models, such as large language models (LLMs), and require:

* Assigned permissions to access systems

* Tools to execute tasks

* Credentials to authenticate

* Context to make decisions

Like human users, agents need governance to ensure they operate securely and within defined boundaries.

|   |                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Agent Governance currently focuses on *centralized agentic platforms* where agents are deployed and managed by your CIO team, CTO team, or development team. This includes commercial agent platforms and agents running on infrastructure you control. Support for personal desktop agents and shadow AI agents is planned for future releases. |

## Challenges this solves

Organizations face several critical challenges with AI agents:

* **Lack of visibility**: Security and identity and access management (IAM) teams don't know where agents are deployed, what they're actually doing across the infrastructure.

* **Multi-platform complexity**: Organizations rarely standardize on a single agent platform. They might use AWS Bedrock alongside Salesforce CRM agents and custom in-house agents, requiring a universal governance solution that works across all platforms.

* **Overprivileged agents**: Many agents are deployed with excessive permissions, creating security posture gaps that put sensitive systems and data at risk.

* **No accountability or compliance visibility**: Without designated custodians, there's no clear ownership or oversight. Agents access sensitive systems without the same governance rigor applied to human identities, creating audit and compliance risks.

## What you can do with Agent Governance

With Agent Governance enabled, you gain the following capabilities:

* **Discover AI agents across all platforms and onboard them as first-class identities.**: Agent Governance includes out-of-the-box connectors for major agent platforms such as Microsoft Copilot, Azure AI Foundry, AWS Bedrock, and Google Vertex AI. It automatically discovers and onboards AI agents into your Identity Governance framework with minimal setup. Once onboarded, agents receive the same identity attributes, lifecycle management, and governance controls as human users and accounts.

* **Discover the full anatomy of each agent using deep discovery.**: Beyond the agent identity itself, Agent Governance discovers and catalogs the resources each agent uses to perform its work, including:

  * **Tools**: APIs and services the agent can invoke.

  * **Knowledge bases**: Data sources the agent queries.

  * **Guardrails**: Policies that limit agent behavior.

  * **Credentials**: API keys and access tokens the agent uses to authenticate. This is a key risk surface to monitor.

  * **Bindings**: Which users or systems can invoke this agent.

  * **Sub-agents**: Other agents this agent can delegate work to.

    This **deep discovery** approach goes beyond basic profile metadata (name, version, platform, owner) that other vendors provide, giving you full visibility into what each agent can do. It also scans your infrastructure to identify disconnected apps running outside your governance framework and detect "shadow agents" operating without proper oversight.

* **Assign one or more human custodians to each agent to provide oversight.**: Every agent needs accountability. You can designate one or more human custodians responsible for overseeing the agent's behavior, approving access requests, and ensuring the agent operates within your organization's policies. Custodians can review agent activity, modify permissions, and act as the point of contact for governance decisions related to that agent.

* **Monitor agent activity with normalized logs from multiple sources.**: Agent Governance ingests and normalizes activity logs from multiple sources, giving you visibility into what your agents are doing. The normalized activity schema classifies logs by actor type, so you can monitor agent behavior, detect unmanaged agents operating without oversight, and identify anomalies.

  The Activity page shows you when agents execute actions, what resources they access, and whether those actions were approved or autonomous. You can investigate suspicious behavior and maintain a complete audit trail of agent operations.

* **Apply comprehensive governance including access requests and workflows, access certifications, and role-based access control.**: Agents inherit all the governance capabilities you already use for human identities. You can require approval workflows before agents receive access to sensitive resources, run periodic access certifications to review and validate agent permissions, and assign role-based access control to enforce least-privilege principles, ensuring agents operate under the same security and compliance standards as your workforce.

### Understanding connected and disconnected modes

Agent Governance supports two modes for discovering agents:

* **Connected mode**: Identity Governance uses out-of-the-box connectors to directly connect to your agent platforms (AWS Bedrock, Azure AI Foundry, Google Vertex AI, and others) and automatically pull agent data on a regular schedule.

* **Disconnected mode**: For custom agents or platforms without pre-built connectors, you can ingest agent data through flat files.

Because most organizations deploy agents across multiple platforms, a hybrid approach is common: connected mode for platforms with pre-built connectors, and disconnected mode for custom or proprietary platforms.

## Summary of Agent Governance workflow

The following steps outline the core workflow for setting up agent governance in your Identity Governance tenant. After completing these steps, your agents will be discovered, onboarded, and ready for governance controls.

1. **Create a custom property to mark agents**: Add a custom property (`custom_iga_identity_type`) to the user object schema (the blueprint for all identities in Advanced Identity Cloud) with two allowed values: "Agent" and "Human".

2. **Onboard your AI agent platform**: Select a supported platform and configure provisioning, property mappings, correlation rules, and reconciliation to import agent identities and their tools or entitlements into Advanced Identity Cloud.

3. **Apply governance controls after onboarding**: Once the agents are synchronized, you can assign custodians, review entitlements, create certification templates, define agent policies, create scopes, configure workflows, and monitor agent activity so agents can be governed with the same oversight, review, and auditability as other identities.

### Before you start

To begin onboarding AI agents, ensure your organization meets these prerequisites:

* Your organization has purchased and enabled the Agent Governance SKU in your Identity Governance tenant.

* Your organization is using at least one of the following AI agent platforms. If you use multiple platforms from the same vendor, such as both AWS Bedrock and AWS Bedrock AgentCore, you can onboard agents from each separately:

  * **AWS Bedrock**: Amazon's service for generative AI applications using foundation models.

  * **AWS Bedrock AgentCore**: Amazon's framework for autonomous agents that execute multi-step tasks.

  * **Azure AI Foundry**: Microsoft's platform for AI models and agents with built-in governance.

  * **Microsoft Copilot**: Microsoft's AI assistant for Microsoft 365 applications.

  * **Google Vertex AI**: Google Cloud's platform for machine learning models and AI agents.

|   |                                                                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you need Agent Governance to support additional agent platforms, contact your Ping Identity representative to express your interest and help us prioritize. |

### Create the identity type

Agent identities use the same object structure as human users but are distinguished by a custom property that flags them as agents. This property is required before onboarding so Agent Governance can distinguish agents from human identities during reconciliation.

1. Sign on to the Advanced Identity Cloud admin console.

2. Go to Identities > Configure.

3. Select Alpha realm - User from the list of object types. This is the default user object type in Advanced Identity Cloud. Agent identities use the same object structure as human users but are distinguished by the identity type property you'll create in the following steps:

   1. Click Properties, and then click [icon: add, set=material, size=inline] Add a Property.

   2. On the New Alpha realm - user Property modal, select String as the property type, and then click Next.

   3. On the New String Property modal, enter the following properties, and then click Save:

      * Property Key: Enter `custom_iga_identity_type`. The `custom_` prefix is required for all custom properties you create. This property must be unique across all identity types.

      * Display Label (optional): Enter `Identity Type`. This is the human-friendly name that appears in the UI.

        ![Identity type configuration page showing the custom\_iga\_identity\_type property with two enumerated values: Agent and Human](../_images/agent-governance-identity-type.png)

4. On the Identity Type (String) (`custom_iga_identity_type`) page, set the following properties, and then click Save:

   1. Click Property Value, and then click Enumerate allowable values for this property. Enumerating values restricts this property to "Agent" or "Human," preventing inconsistent values.

   2. In the Label field, enter `Agent`, and in the Value field, enter `Agent`. Click [icon: add, set=material, size=inline] to add this value to the list of allowed values.

   3. In the Label field, enter `Human`, and in the Value field, enter `Human`. Click [icon: add, set=material, size=inline] to add this value to the list of allowed values.

      ![Screenshot showing enumerated values for custom\_iga\_identity\_type: Agent and Human.](../_images/agent-governance-identity-type-property-value.png)

5. Click Display, check that the following properties are set, and update them if necessary:

   * Show in Admin List View: Select this checkbox to include this property as a column in internal admin lists and tables.

   * Show in Admin Form: Select this checkbox to display this property in forms used by admins to view or update records.

   * Show in User-facing Form: Select this checkbox to allow end users to see and edit this property in the self-service UI.

6. Click Save.

### Set up an application for your AI agent platform

Before you can onboard AI agents, set up one of the following applications:

1. In the Advanced Identity Cloud admin console, go to Applications > Browse App Catalog.

   * [AWS Bedrock](../../app-management/applications-agent-governance/aws-bedrock.html)

   * [AWS Bedrock AgentCore](../../app-management/applications-agent-governance/aws-bedrock-agentcore.html)

   * [Azure AI Foundry](../../app-management/applications-agent-governance/azure-ai-foundry.html)

   * [Google Vertex AI](../../app-management/applications-agent-governance/google-vertex-ai.html)

   * [Microsoft Copilot Studio](../../app-management/applications-agent-governance/microsoft-copilot-studio.html)

### Onboard AI agents

To onboard Ai agents, configure your application by mapping agent properties to identity fields.

#### Configure connected tools as entitlements

1. In the Advanced Identity Cloud admin console, go to Applications.

2. Click the application you just registered to open the application details page.

3. Click the Provisioning tab, choose one of the following optinos based on the message displayed:

4. On the AI application page, select Account to map agent properties to identity fields in Advanced Identity Cloud.

5. Click the Properties tab, and review the agent's properties.

   1. Search for the Connected Tools property. Click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) for this property, and then click Edit.

   2. In the Edit Property modal, click Entitlement to specify that this property contains entitlements.

      ![Edit property modal with the entitlement option highlighted.](../_images/agent-governance-edit-property.png)

   3. Click Save.

#### Configure synchronization mappings

Synchronization mappings tell Identity Governance which agent properties from your source platform (such as agent name or ID) should be stored in which user fields in Advanced Identity Cloud.

1. In the Advanced Identity Cloud admin console, go to Applications, browse the app catalog, and select your AI Agent.

2. Click the Provisioning tab.

3. Make sure you are viewing the Account object type.

4. Click Advanced Sync, and then click [icon: add, set=material, size=inline] Sync Data.

5. In the Sync account object type modal, select Object Type in the Sync To section.

6. Select `alpha_user`, and click Save.

   ![Sync mappings page showing the source properties on the left and target properties on the right, with a button to add new property mappings](../_images/agent-governance-configure-sync-mappings.png)

7. Set up the mappings between your agent platform properties and Ping Identity identity properties.

   1. On the AI agent to Mapping page, click [icon: add, set=material, size=inline] Add a property.

      ![Sync mapping chart showing Ping Identity properties mapped to AWS Bedrock agent source properties.](../_images/agent-governance-sync-mapping-chart.png)

   2. In the Add a property modal, select a Ping Identity property. For example, select userName, and then click Next.

   3. In the userName (string) property modal, select the agent's property. For example, select source.*NAME*, and then click Save.

      |   |                                                                                                                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Some properties require hardcoded values (static text that applies to all synced agents). For example, `custom_iga_identity_type` should always be `"Agent"`. For these, click Apply transformation script, enter the value, and then click Save. |

   4. Repeat the previous steps to add more property mappings.

      | Ping Identity property      | Agent property                     | Notes                                             |
      | --------------------------- | ---------------------------------- | ------------------------------------------------- |
      | userName                    | source.*NAME*                      | Unique identifier for the agent                   |
      | custom\_iga\_identity\_type | `"Agent"`                          | Hardcoded value to flag this as an agent identity |
      | givenName                   | source.agentName                   | Agent's display name                              |
      | sn                          | `"Bedrock"`                        | Last name—customize to your platform name         |
      | mail                        | source.agentId+"@pingidentity.com" | Synthetic email—adjust domain as needed           |

#### Define correlation rules

Correlation rules tell Identity Governance how to match agent accounts from your source platform (like AWS Bedrock) to identities that may already exist in Advanced Identity Cloud. Without these rules, the system might create duplicate identities when you import agents, resulting in confusion and governance gaps.

1. In the Advanced Identity Cloud admin console, go to Applications, select your AI Agent application, and click the Provisioning tab.

2. Go to Reconciliation > Settings.

3. Next to Custom, click the ellipsis icon ([icon: more_horiz, set=material, size=inline]), and select Edit. This opens the correlation query editor.

4. Enter the correlation query that Identity Governance uses to match agent accounts to existing identities and prevent duplicates. For example:

   ```javascript
   var qry = {'_queryFilter': 'userName eq "' + source.__NAME__ + '"'}; qry
   ```

5. Click Save.

#### Configure situation rules

Situation rules define what action Identity Governance takes during synchronization scenarios, for example, creating a new identity when an agent account exists in AWS Bedrock but not in Advanced Identity Cloud (a "Missing" situation). This ensures consistent handling across all scenarios without manual intervention.

1. On the same Reconciliation Settings page, go to the Situation Rules section.

2. Under Actions, click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) for each of the following situations, and select the appropriate action:

   | Situation | Recommended action                                                                               |
   | --------- | ------------------------------------------------------------------------------------------------ |
   | Missing   | Select Create. This occurs when the account exists in the source but not in the target.          |
   | Confirmed | Select Update. This occurs when the account exists in both the source and target and are linked. |
   | Found     | Select Update. This occurs when the account exists in both but aren't linked yet.                |
   | Absent    | Select Create. This occurs when the account doesn't exist in the source.                         |

3. Click Save.

#### Run reconciliation

Reconciliation is the process that syncs agent data from your source platform into Identity Governance. Run reconciliation twice: first for agent identities, then for their tools and entitlements. Identity Governance reconciles each object type separately, so both runs are required to import the complete agent profile.

1. On your application page, make sure you're viewing the Account object type.

2. Click Reconciliation, and then click Reconcile Now to onboard the agent identities.

   ![Reconciliation page showing the Account object type with a Reconcile Now button](../_images/agent-governance-reconciliation-agent-account.png)

3. On the application page, select the Agent Tool object type.

4. Click Reconciliation, and then click Reconcile Now to onboard the agent tools and entitlements.

   ![Reconciliation page showing the Agent Tool object type with a Reconcile Now button](../_images/agent-governance-reconciliation-agent-tool.png)

#### Deploy the platform-specific collector

After agents are onboarded, deploy the platform-specific collector to enable deep discovery of agent tools and capabilities.

Contact your Custom Success Outcome Manager or Ping Identity representative to obtain the inventory package and runbook.

|   |                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Don't skip this step. Without deploying the collector, Agent Governance only imports basic profile information about your agents (name, ID, owner) but doesn't discover the tools they use, their permissions, or their activity. This limits your visibility and governance capabilities. |

### Configure governance

To configure governance, start by creating a certification template to define which agents and entitlements are reviewed.

#### Create a certification template

For AI agents, create a template that specifies which agents to include, what entitlements to review, who performs the review, and the review schedule.

To create a certification template for AI agents:

1. In the Advanced Identity Cloud admin console, go to Governance > Certification.

2. Click the Templates tab, and then click [icon: add, set=material, size=inline] New Template.

3. In the New Certification Campaign Template modal, select Identity Certification, and then click Next.

4. On the New Identity Certification Template page, enter the following information, and then click Next:

   * Name: Enter a name for the template. For example, enter `AI Agent Certification Template`.

   * Description: Enter a description for the template. For example, enter `Certification template for reviewing AI agent access and permissions`.

   * Campaign Owner: Select the owner of this certification campaign. For example, enter `AGT001 CrewAI (AGT001)`.

   * Enable Campaign Staging: Skip this option. Staging is used for testing campaigns before they go live, but you can leave it disabled for your first campaign.

5. On the What to Certify page, select the following options, and then click Next:

   * Certify User Entitlements: Select this option to include agent entitlements in the certification campaign.

   * Organizations: Select All Organizations to include agents from all organizational units in this campaign.

   * Users: Select Users matching a filter.

     * Any: Select this option to include all of the rules specified.

     * Identity Type:Select `Equals`, then enter `Agent` to include only agent identities in this campaign.

   * Applications: Select Specific Applications, and then select Bedrock. This limits the campaign to AWS Bedrock agents.

   * Entitlements: Select All entitlements to include all entitlements for the selected agents.

   * Exclude access granted only from a role: Excludes entitlements agents hold only through roles, focusing the review on direct entitlements (increased risk).

     ![Screen capture showing certification options: certify user entitlements, select organizations, filter by identity type, select specific applications, choose entitlements.](../_images/agent-governance-what-to-certify.png)

6. On the When to Certify page, select the default options (for example, 14 days), and then click Next.

7. On the Who will Certify page, select the following options, and then click Next:

   * Certifier Type: Select User.

   * Select user: Select the user who'll act as the certifier for this campaign.

8. On the Notifications page, select any options, and then click Next.

9. On the Additional Options page, select the following options, and then click Next:

   * Enable line-item reassignment and delegation: Select this option to allow certifiers to reassign specific access items to other reviewers or delegate the entire certification to someone else.

     * Forward: Select this option to allow certifiers to forward specific access items to other reviewers for input without reassigning them.

     * Reassign: Select this option to allow certifiers to reassign specific access items to other reviewers for approval.

       * Add comment: Select this option to require certifiers to provide a comment when they reassign an access item.

       * Make decision: Select this option to require certifiers to make an approval decision when they reassign an access item.

       * Reassign/Forward: Select this option to allow certifiers to either forward or reassign access items.

       * Sign off: Select this option to allow certifiers to sign off on specific access items without reviewing the entire certification.

   * Require justification on revoke: Select this option to require certifiers to provide a justification when they revoke access from an agent.

   * Require justification on exception: Select this option to require certifiers to provide a justification when they mark an access item as an exception.

   * Allow exceptions: Select this option to allow certifiers to mark access items as exceptions, which means they acknowledge the risk but choose to accept it for a specified period.

   * Campaign expiration: Select Do Nothing to allow certifiers to continue reviewing access items even after the campaign end date. This is useful for your first campaign while you're getting familiar with the process, but for future campaigns, you might want to select Expire Access to automatically revoke any access that wasn't certified by the end date.

     ![Additional options page showing various checkboxes for line-item reassignment, justification requirements, exception handling, and campaign expiration](../_images/agent-governance-additional-options.png)

10. On the Customization page, select the default column configuration of the table for access reviewers, and then click Next:

11. On the Summary page, review the campaign settings, and then click Save.

    The new certification template appears in the list of templates. You can use this template to create certification campaigns that include your AI agents and their entitlements.

12. On the Certification page, select the ellipsis icon ([icon: more_horiz, set=material, size=inline]) for your new template, and then click Run Now.

    Monitor the campaign progress on the Campaigns tab. After the campaign completes, review which agents were certified, which were revoked, and which items require attention.

    ![Campaigns page showing a list of certification campaigns with their name, template, type, status, start date, end date, and actions columns](../_images/agent-governance-campaigns.png)

#### Create an agent policy

Agent policies detect conflicting or inappropriate entitlements and help you define prohibited combinations before they pose a security risk. For example, an agent with both `Asset Lookup Tool` and `Benefits Search Tool` entitlements could expose sensitive data if compromised; a policy rule prohibiting this combination lets you detect and remediate it proactively.

To create a policy rule for your agents:

1. In the Advanced Identity Cloud admin console, go to Governance > Compliance.

2. On the Compliance page, click the Policy Rules tab to add a policy rule.

   1. Click [icon: add, set=material, size=inline] New Rule.

   2. On the New Policy Rule page, enter the following, and then click Next:

      * Name: Enter a name for the policy rule. For example, enter `Restrict HR access`.

      * Description: Enter a description for the policy rule. For example, enter `Policy rule to restrict access to HR resources for AI agents`.

      * Owner: Select a user for this policy rule. For example, select `Danielle Johnson`.

      * Risk Score: Enter a risk score for this policy rule. For example, enter `0`.

      * Mitigating Control: (Optional) Skip this option.

      * Control URL: (Optional) Skip this option.

      * Correction Advice: (Optional) Skip this option.

   3. Click Violation Condition, enter the following, and then click Save:

      * Any of the following conditions are met: Select this option to specify that a violation occurs if any of the conditions you define are met.

        * Display Name: Select this option, select `is`, and then enter the name of the entitlement you want to restrict. For example, enter `Access Lookup Tool`. Click [icon: add, set=material, size=inline].

      * Under Conflicts with, enter the following rule:

        * Display Name: Select this option, select `is`, and then enter the name of an entitlement that conflicts with the restricted entitlement. For example, enter `Benefits Search Tool`.

          ![Policy rule configuration page showing the details, violation condition, applies to, and settings sections with various options for each](../_images/agent-governance-policy-rule.png)

   4. Click Applies To, select User matching a filter, enter the following, and then click Save:

      * Any of the following conditions are met: Select this option to specify that this policy rule applies if any of the conditions you define are met.

      * Identity Type: Select this option, select `is`, and then enter `Agent` as the value. This policy rule only applies to identities flagged as agents.

        ![Policy rule applies to configuration showing a filter for user identities with the identity type equal to Agent](../_images/agent-governance-policy-rule-applies-to.png)

   5. Click Settings, select the following options, and then click Save:

      * Violation Owner: Select the user responsible for managing violations of this policy rule. For example, select `Frank York`.

      * Enable Allow: Select this decision option to allow users to retain their violating access permanently.

      * Enable Exception: Select this decision option to allow users to be granted a temporary exception to retain access.

        * Require a justification when allowing exceptions: Select this option to require a justification when granting an exception.

      * Preventative: Select this scan type to enforce rules during access requests and provisioning.

      * Detective: Select this scan type to enforce rules during compliance scans.

      * Launch Violation Workflow: Select this violation lifecycle option to automatically launch a workflow when a violation of this policy rule is detected. For example, select `Basic Violation Process`.

      * Never: Select this Violation Expires option to specify that violations of this policy rule never expire.

      * Close violation: Select this "When violation expires" option to specify that violations of this policy rule are closed when they expire.

To create a policy that applies to agents:

1. In the New Policy modal, enter the following, and then click Next:

   * Name: Enter a name for the policy. For example, enter `CrewAI Compliance Policy`.

   * Description: Enter a description for the policy. For example, enter `Policy to enforce compliance for CrewAI agents`.

   * Policy Owner: Select a user for this policy. For example, select `Danielle Johnson`.

2. Click the Rules tab, click [icon: add, set=material, size=inline] Add Rules.

   1. In the Add Rules modal, select the policy rule you just created (for example, `Restrict HR access`), and then click Save.

3. On the policy page, click the Scans tab, and then click Simulate Scan to test this policy against your agents and identify any violations.

   ![Policy rule scans page showing a list of violations with columns for identity, violation, status, and actions](../_images/agent-governance-policy-rule-scans.png)

#### Create scopes

Use scopes to restrict which identities can see or request specific resources in Agent Governance. For example, create a scope limiting "End User Access Request" to human identities to prevent agents from autonomously requesting access without human approval. Learn more in [Scopes](scopes.html).

To create a scope:

1. In the Advanced Identity Cloud admin console, go to Governance > Scopes.

2. Click [icon: add, set=material, size=inline] New Scopes.

3. On the New Scope page, enter the following information on the Details page, and then click Next:

   * Name: Enter a name for the scope. For example, enter `End User Access Request`.

   * Description: Enter a description for the scope. For example, enter `Scope to restrict access requests to human users only`.

4. On the Applies to page, enter or select the following information, and then click Next:

   * custom\_iga\_identity\_type: Select agent identity type, select `is`, and then enter `Human`. This scope only applies to identities flagged as human users.

     ![Scope applies to configuration showing a filter for identities with the custom\_iga\_identity\_type property equal to Human](../_images/agent-governance-scope-applies-to.png)

5. On the Access page, select access to the following resources, and then click Save:

   * Applications: Select All Applications and View Applications.

   * Entitlements: Select All Entitlements and View Entitlements.

   * Roles: Select All Roles and View Roles.

Now only human users can request access to applications through the self-service UI. Agents can't submit access requests autonomously. Any access changes for agents must be initiated by their assigned custodians or through automated provisioning rules you define.

#### Workflows

Configure workflows to require human approvals and ensure oversight of agent activity. For example, you could create an access request workflow that requires custodian approval for any access requests submitted on behalf of an agent. Or, you could create a violation remediation workflow that automatically revokes access from any agent that violates a compliance policy. Learn more about workflows at [Workflow configuration](workflow-configure.html).

### Monitor agent activity

The activity log helps organizations understand what users, accounts, and AI agents are actually doing with the access they have. Instead of treating access as a one-time grant, it adds the activity context needed to evaluate whether that access is being used appropriately, whether it introduces risk, and whether it still makes sense from a cost and governance perspective.

To make that possible across different platforms, the activity log uses a canonical schema that normalizes activity data from sources such as Salesforce, SAP, Office 365, cloud platforms, and identity systems into a searchable format. This gives governance and security teams a consistent way to review events across applications, investigate suspicious behavior, identify unused or excessive access, and support broader analytics such as activity-based risk analysis and token-consumption monitoring.

|   |                                                                                                                                                                                                                                                                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The feature is implemented primarily through APIs. Customers can ingest and normalize activity logs programmatically by mapping their source logs to the canonical schema, and then use the resulting normalized data to search and analyze activity across their environment, without depending on source-specific log formats or custom UI-driven ingestion workflows. |

To monitor agent activity:

1. In the Advanced Identity Cloud admin console, go to Governance > Agents.

2. Select an agent from the list, and click the Activity tab.

3. Filter the activity logs by date and time range, and time zone offset, or search for a specific activity.

   ![Screen capture of activity logs showing timestamp, actor, action, resource, result columns and date range and time zone filters.](../_images/agent-governance-activity.png)

   | Field          | Description                                                                     |
   | -------------- | ------------------------------------------------------------------------------- |
   | Actor Details  |                                                                                 |
   | Actor ID       | The unique identifier of the agent performing the action.                       |
   | Username       | The display name of the agent.                                                  |
   | Email          | This field is empty for agents.                                                 |
   | Global ID      | The global identifier for the agent in Advanced Identity Cloud.                 |
   | Environment    |                                                                                 |
   | Location       | The geographic location where the action was performed, if available.           |
   | User Agent     | The user agent string associated with the action, if available.                 |
   | Device         | The device used to perform the action, if available.                            |
   | Cloud Region   | The cloud region where the action was performed, if available.                  |
   | Result         |                                                                                 |
   | Response Code  | The response code returned by the action, if applicable.                        |
   | Risk Score     | The risk score associated with the action, if available.                        |
   | Bytes in/Out   | The amount of data transferred during the action, if applicable.                |
   | Raw Event JSON | The full raw event data in JSON format, which might include additional details. |

### Finalize agent governance setup

After configuring governance controls, complete your setup by assigning custodians to provide human oversight and enriching the entitlement glossary to help reviewers understand what each permission allows.

#### Assign custodians

1. In the Advanced Identity Cloud admin console, go to Governance > Agents.

   You see all agents from your connected platform listed here.

   ![Dashboard with metric cards (Recently Discovered, Review Pending, Action Required, Provisioned), platform filters sidebar, and agent table with application and description columns.](../_images/agent-governance-ui.png)

2. Assign custodians to each agent. You can:

   * Assign custodians manually by selecting an agent and adding owners.

   * Configure automated custodian assignment rules based on agent properties.

3. Go to Governance > Entitlements to review the agent tools and permissions discovered during reconciliation.

#### Enrich the entitlement glossary

Enrich the entitlement glossary by adding business-friendly descriptions to each tool or permission.

To edit glossary entries:

1. Select an entitlement from the list.

2. Click Edit.

3. In the Description field, enter a clear explanation of what this entitlement allows.

4. Click Save.

#### Test the setup

1. Sign on to the hosted console as a test user who has been assigned as a custodian.

2. Go to My Access > My Agents.

   You should see a list of agents you're assigned as a custodian for. If the list is empty, reconciliation might not have completed or mappings might not be correct.

3. Select an agent to review:

   * Agent profile information

   * Assigned custodians

   * Connected tools and entitlements

If you don't see the expected agents or their access details, return to the reconciliation step and check the mapping and correlation configurations.

## Next steps

After you've successfully onboarded your AI agent and configured governance controls, consider these recommended actions:

**Expand governance coverage:**

* **Onboard agents from additional platforms**: If your organization uses multiple agent platforms, repeat the onboarding process for each one. Agent Governance supports agents from AWS Bedrock, Azure AI Foundry, Microsoft Copilot, Google Vertex AI, and custom platforms. Manage all agents in a centralized location.

* **Establish agent lifecycle processes**: Define how new agents are requested, approved, provisioned, and decommissioned in your organization. Consider creating templates for common agent types to streamline onboarding while maintaining security standards.

**Maintain continuous oversight:**

* **Schedule regular certification campaigns**: Use the certification template you created to run periodic access reviews. Configure campaigns to run quarterly or whenever your compliance policies require. Regular certification ensures agent permissions remain appropriate as your organization evolves.

* **Configure activity monitoring and alerts**: Set up notifications to alert custodians when agents exhibit unusual behavior or access patterns. Review logs regularly to identify risks, policy violations, or operational issues early.

* **Train custodians on their responsibilities**: Ensure the human custodians you assigned understand their role in overseeing agent access and behavior. Provide guidance on approval decisions, certification review, and investigation of suspicious activity.

* **Document Agent Governance policies**: Create organizational policies that define acceptable use for AI agents, required approval workflows, and escalation procedures for violations. Document which types of agents require custodian oversight and which access combinations are prohibited.

**Integrate with runtime security:**

* **Integrate with runtime enforcement**: For real-time control of agent behavior during execution, combine Agent Governance with Ping Gateway and Ping Privilege. This provides both administrative governance (what agents can access) and runtime authorization (what agents should do right now). Learn more about the complete Identity for AI solution in Ping Identity documentation.

---

---
title: "Agent Governance: custodian and reviewer tasks"
description: View and manage AI agents as a custodian. Review agent profiles, certify entitlements, and request access to tools on behalf of agents.
component: pingoneaic
page_id: pingoneaic:identity-governance:end-user/iga-agent-governance-enduser
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/end-user/iga-agent-governance-enduser.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  view_and_manage_agents_as_a_custodian: View and manage agents as a custodian
  access_reviews: Access reviews
  access_requests: Access requests
---

# Agent Governance: custodian and reviewer tasks

As a custodian, certifier, or reviewer, you are responsible for managing and overseeing AI agents. You interact with the hosted pages to perform governance tasks such as reviewing agent profiles, entering and approving access requests, and certifying agent entitlements.

## View and manage agents as a custodian

Custodians manage agents' access and lifecycle. Agent Governance events support succession management, ensuring new custodians are assigned when existing ones move within or leave the organization.

To view the agents assigned to you and review their properties and entitlements:

1. On the hosted page, click My Access > My Agents.

2. On the My Agents page, select an agent to view its details.

   ![Screen capture of the agent profile page showing the display name and description.](../_images/agent-governance-custodian-view.png)

3. Click the Entitlements tab to view the agent's access to tools and permissions.

4. Click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) for a specific entitlement.

5. Click View Details to see more information about that entitlement, including its description from the entitlement glossary.

   ![Screen capture of the agent entitlements showing a list of entitlements with a detail modal open.](../_images/agent-governance-end-user-agent-entitlements.png)

## Access reviews

Access reviews enable human oversight of agent access and reduce access drift, improving your organization's security posture. When a campaign is active, you review agent access to ensure it is correct and complies with your organization's security policies.

To review and certify, revoke, or flag exceptions for agent access:

1. On the hosted pages, click Inbox > Access Reviews.

2. On the Access Reviews page, select an active campaign to review the agents included in that campaign.

3. For each agent, review the agent's properties and entitlements to determine if the access is appropriate.

   ![Screen capture of the access review page showing agents and review actions.](../_images/agent-governance-end-user-access-review.png)

   1. Under Actions, click Certify, Revoke, or Allow an exception for the agent's access.

   2. If you need additional reviewers or information, click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) to do the following:

      * Forward: Forward the review to another user who might have more context about the agent or its access.

      * View Reviewers: View who else is reviewing this agent's access in the current campaign.

      * Add a Comment: Provide additional context or information about the agent's access for other reviewers to see.

      * View Activity: View the agent's activity history to help inform your decision about whether to certify or revoke access.

## Access requests

As a custodian or administrator, you can request access to tools on behalf of agents. Agent Governance lets you set a time limit on how long an agent retains access to a tool or entitlement, limiting agents to only the access they need for a specific task.

To request tool access for an agent:

1. On the hosted pages, click My Requests, and then click [icon: add, set=material, size=inline] New Request.

2. In the New Request modal, select Other Users, and then click Next.

3. For Users, select an agent, for example, AGT001 CrewAI, and then click Next.

4. On the Access Catalog page, click the Entitlements tab.

5. Select the entitlements you want to request access to for the agent.

6. In the entitlement modal, click Add to Request.

7. In the right pane, enter the justification for why the agent needs this access and the duration for which access is needed.

8. Click Complete Request to submit the access request for approval.

9. On the My Requests page, track the status of your access request.

   When the status changes to Approved, the agent has access to the requested entitlements for the specified duration.

   ![Screen capture of the My Requests page showing access request details.](../_images/agent-governance-end-user-access-request.png)

---

---
title: Application grant workflow example
description: Example workflow for application access requests with context checks and line-of-business routing
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/example-app-grant-workflow
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/example-app-grant-workflow.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["workflows", "use cases", "examples", "application grant"]
section_ids:
  assumptions: Assumptions
  example: Example
---

# Application grant workflow example

In this example, an administrator wants to create an application grant workflow that:

* Requires the manager to approve the request. If an administrator sends a request, the request is auto-approved.

* If approved, check what line of business (LOB) the application is in.

* Based on the LOB, the workflow requires a separate approver to approve the request.

## Assumptions

* Each application has an application owner. An application owner is a user identity designated to manage the application. You populate this value for each target application.

* You create an [application glossary attribute](glossary.html#create-application-glossary) LOB, and populate the LOB for each application. For this scenario, the LOBs are:

  * `Sales`

  * `Finance`

  * `Human Resources`

* Your end users have a manager assigned to them. An administrator populates this property and it isn't modifiable by the end user.

## Example

![An example of an application grant workflow.](../_images/governance-example-app-workflow-lob.png)

* 1 Use a Script node to do a context check for the request.

  > **Collapse: Click to display the request context check script**
  >
  > ```js
  > /*
  > Script nodes are used to invoke APIs or execute business logic.
  > You can invoke governance APIs or IDM APIs.
  > You can find details in Manage workflows.
  >
  > Script nodes should return a single value and should have the
  > logic enclosed in a try-catch block.
  >
  > Example:
  > try {
  >   var requestObj = openidm.action('iga/governance/requests/' + requestId, 'GET', {}, {});
  >   applicationId = requestObj.application.id;
  > }
  > catch (e) {
  >   failureReason = 'Validation failed: Error reading request with id ' + requestId;
  > }
  > */
  > var content = execution.getVariables();
  > var requestId = content.get('id');
  > var context = null;
  > var skipApproval = false;
  > var lineItemId = false;
  > try {
  >   var requestObj = openidm.action('iga/governance/requests/' + requestId, 'GET', {}, {});
  >   if (requestObj.request.common.context) {
  >     context = requestObj.request.common.context.type;
  >     lineItemId = requestObj.request.common.context.lineItemId;
  >     if (context == 'admin') {
  >       skipApproval = true;
  >     }
  >   }
  > }
  > catch (e) {
  >   logger.info("Request Context Check failed "+e.message);
  > }
  >
  > logger.info("Context: " + context);
  > execution.setVariable("context", context);
  > execution.setVariable("lineItemId", lineItemId);
  > execution.setVariable("skipApproval", skipApproval);
  > ```

* 2 Use an IF/ELSE node to set the context gateway for auto approval or standard approval based on a manager review.

* 3 Use the Script node to run any auto approvals:

  > **Collapse: Click to display the auto approval script**
  >
  > ```js
  > var content = execution.getVariables();
  > var requestId = content.get('id');
  > var context = content.get('context');
  > var lineItemId = content.get('lineItemId');
  > var queryParams = {
  >   "_action": "update"
  > }
  > try {
  >   var decision = {
  >       "decision": "approved",
  >       "comment": "Request auto-approved due to request context: " + context
  >   }
  >   openidm.action('iga/governance/requests/' + requestId, 'POST', decision, queryParams);
  > }
  > catch (e) {
  >   var failureReason = "Failure updating decision on request. Error message: " + e.message;
  >   var update = {'comment': failureReason, 'failure': true};
  >   openidm.action('iga/governance/requests/' + requestId, 'POST', update, queryParams);
  > }
  > ```

* 4 Using an Approval node, the manager of the end user must approve the request.

* 5 If approved, a Script node checks the application glossary attribute `lineOfBusiness` (LOB) and sets the outcome based on the LOB of the application. Based on the outcome, the Switch node evaluates the LOB.

  > **Collapse: Click to display check LOB script**
  >
  > ```js
  > var content = execution.getVariables();
  > var requestId = content.get('id');
  > var requestObj = null;
  > var appId = null;
  > var appGlossary = null;
  > var lob = null;
  >
  > try {
  >   requestObj = openidm.action('iga/governance/requests/' + requestId, 'GET', {}, {});
  >   appId = requestObj.application.id;
  >   }
  >   catch (e) {
  > 	logger.info("Validation failed: Error reading application grant request with id " + requestId);
  >   }
  >
  > try {
  >   appGlossary = openidm.action('iga/governance/application/' + appId + '/glossary', 'GET', {}, {});
  >   lob = appGlossary.lineOfBusiness || "default";
  >   execution.setVariable("lob", lob);
  > }
  > catch (e) {
  >   logger.info("Could not retrieve glossary with appId " + appId + " from application grant request ID " + requestId);
  > }
  > ```

* 3 If the LOB is:

  * `sales`: An Approval node requires members of the role `Sales App Approver` to approve the request.

  * `finance`: An Approval node requires members of the role `Finance App Approver` to approve the request.

  * `humanResources`: An Approval node requires members of the role `Human Resources App Approver` to approve the request.

  * `null`: An Approval node requires the application owner to approve the request.

* 7 If the required approvals are met, a Script node runs a validation check.

  > **Collapse: Click to display app grant validation script**
  >
  > ```js
  > logger.info("Running application grant request validation");
  >
  > var content = execution.getVariables();
  > var requestId = content.get('id');
  > var failureReason = null;
  > var applicationId = null;
  > var app = null;
  >
  > try {
  >   var requestObj = openidm.action('iga/governance/requests/' + requestId, 'GET', {}, {});
  >   applicationId = requestObj.application.id;
  > }
  > catch (e) {
  >   failureReason = "Validation failed: Error reading request with id " + requestId;
  > }
  >
  > // Validation 1 - Check application exists
  > if (!failureReason) {
  >   try {
  >     app = openidm.read('managed/alpha_application/' + applicationId);
  >     if (!app) {
  >       failureReason = "Validation failed: Cannot find application with id " + applicationId;
  >     }
  >   }
  >   catch (e) {
  >     failureReason = "Validation failed: Error reading application with id " + applicationId + ". Error message: " + e.message;
  >   }
  > }
  >
  > // Validation 2 - Check the user doesn't already have application granted
  > // Note: this is done at request submission time as well, the following is an example of how to check user's accounts
  > if (!failureReason) {
  >   try {
  >     var user = openidm.read('managed/alpha_user/' + requestObj.user.id, null, [ 'effectiveApplications' ]);
  >     user.effectiveApplications.forEach(effectiveApp => {
  >       if (effectiveApp._id === applicationId) {
  >         failureReason = "Validation failed: User with id " + requestObj.user.id + " already has effective application " + applicationId;
  >       }
  >     })
  >   }
  >   catch (e) {
  >     failureReason = "Validation failed: Unable to check effective applications of user with id " + requestObj.user.id + ". Error message: " + e.message;
  >   }
  > }
  >
  > if (failureReason) {
  >   logger.info("Validation failed: " + failureReason);
  > }
  > execution.setVariable("failureReason", failureReason);
  > ```

  If any Approval node has the `Reject` outcome, a Script node denies the request.

  > **Collapse: Click to display reject request script**
  >
  > ```js
  > logger.info("Rejecting request");
  >
  > var content = execution.getVariables();
  > var requestId = content.get('id');
  >
  > logger.info("Execution Content: " + content);
  > var requestIndex = openidm.action('iga/governance/requests/' + requestId, 'GET', {}, {});
  > var decision = {'outcome': 'denied', 'status': 'complete', 'decision': 'rejected'};
  > var queryParams = { '_action': 'update'};
  > openidm.action('iga/governance/requests/' + requestId, 'POST', decision, queryParams);
  > ```

* 8 If the If/Else node outcome is:

  * `validationSuccess`: A Script node provisions the application to the end user.

    > **Collapse: Click to display auto provisioning script**
    >
    > ```js
    > logger.info("Auto-Provisioning");
    >
    > var content = execution.getVariables();
    > var requestId = content.get('id');
    > var failureReason = null;
    >
    > try {
    >   var requestObj = openidm.action('iga/governance/requests/' + requestId, 'GET', {}, {});
    >   logger.info("requestObj: " + requestObj);
    > }
    > catch (e) {
    >   failureReason = "Provisioning failed: Error reading request with id " + requestId;
    > }
    >
    > if(!failureReason) {
    >   try {
    >     var request = requestObj.request;
    >     var payload = {
    >       "applicationId": request.common.applicationId,
    >       "startDate": request.common.startDate,
    >       "endDate": request.common.endDate,
    >       "auditContext": {},
    >       "grantType": "request"
    >     };
    >     var queryParams = {
    >       "_action": "add"
    >     }
    >
    >     logger.info("Creating account: " + payload);
    >     var result = openidm.action('iga/governance/user/' + request.common.userId + '/applications' , 'POST', payload,queryParams);
    >   }
    >   catch (e) {
    >     failureReason = "Provisioning failed: Error provisioning account to user " + request.common.userId + " for application " + request.common.applicationId + ". Error message: " + e.message;
    >   }
    >
    >   var decision = {'status': 'complete', 'decision': 'approved'};
    >   if (failureReason) {
    >     decision.outcome = 'not provisioned';
    >     decision.comment = failureReason;
    >     decision.failure = true;
    >   }
    >   else {
    >     decision.outcome = 'provisioned';
    >   }
    >
    >   var queryParams = { '_action': 'update'};
    >   openidm.action('iga/governance/requests/' + requestId, 'POST', decision, queryParams);
    >   logger.info("Request " + requestId + " completed.");
    > }
    > ```

  * `validationFailure`: A Script node doesn't provision the application to the end user.

    > **Collapse: Click to display validation failure script**
    >
    > ```js
    > var content = execution.getVariables();
    > var requestId = content.get('id');
    > var failureReason = content.get('failureReason');
    >
    > var decision = {'outcome': 'not provisioned', 'status': 'complete', 'comment': failureReason, 'failure': true, 'decision': 'approved'};
    > var queryParams = { '_action': 'update'};
    > openidm.action('iga/governance/requests/' + requestId, 'POST', decision, queryParams);
    > ```

|   |                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Download the JSON file for this workflow [here](../_attachments/workflows/workflowUIAppGrantWorkflowExample.json).Learn more about how to import or export workflows in [workflow editor canvas](workflow-configure.html#orch-ui-canvas). |

---

---
title: Approve access
description: Review and approve or reject access requests submitted by team members or for applications you own
component: pingoneaic
page_id: pingoneaic:identity-governance:end-user/access-request-approve-access
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/end-user/access-request-approve-access.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["approve access", "reject access", "forward access", "request items", "approvals", "inbox"]
section_ids:
  approve-access-access-request-types: Access request types
  decision-approval-item: Approve, reject, or forward a request item
  approve-item: Approve item
  reject-item: Reject item
  forward-item: Forward to another user or role
---

# Approve access

When an end user submits an access request, designated owners (approvers) must grant approval for the provisioning of resources.

The items on which approvers review and make decisions are referred to as *request items*.

Approvers review and make decisions on items referred to as *request items* in the Advanced Identity Cloud end-user UI.

For more information, learn more in [Sign on as an end user](../../end-user/hosted-pages.html#sign-on-end-user) and navigate to Inbox > Approvals.

![An approver reviews their assigned access requests on the approvals page.](../_images/governance-enduser-ui-approvals-landing-page.png)

* 1 Click Inbox > Approvals from the Advanced Identity Cloud end-user UI to display the access requests landing page.

* 2 Filter submitted request items by status:

  * Pending: The items are pending review.

  * Completed: The approver reviewed the items and made a decision (approve or reject).

* 3 Click Sort By, and sort the items by an attribute in ascending or descending order.

* 4 Click Show Filters to filter by attributes or priority. An end user sets the priority when they create the access request.

* 5 Click on the item to view the details of the request.

## Access request types

End users and managers can submit different access request types, such as removing and adding access requests.

The access request type breaks out the request items displayed to approvers.

The following table describes the access request types:

| Access request type | Description                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------------- |
| Grant Application   | End user requests access to an application.                                                 |
| Remove Application  | End user's manager requests to remove an application from an end user.                      |
| Grant Role          | End user requests access to an Advanced Identity Cloud provisioning role.                   |
| Remove Role         | End user's manager requests to remove a role from an end user.                              |
| Grant Entitlement   | End user requests access to an entitlement (an additional privilege inside an application). |
| Remove Entitlement  | End user's manager requests to remove an entitlement from an end user.                      |

|   |                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | The access request type is indicated at the top of each request item.![A screenshot displaying where an end user views the request type.](../_images/governance-enduser-ui-approvals-request-type.png) |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | When end users enter an entitlement request, end users will see a warning message if the request results in a Segregation of Duties (SoD) violation.`Granting access to these entitlement(s) will result in a Segregation of Duties (SoD) violation.`End users can click View Details to review the entitlements on the Violations Found modal. The end user has the option to click Submit with Violation or Close the modal. |

## Approve, reject, or forward a request item

The access request details of a request item include the requested resource(s), justification, and submission date.

Click a request item to view the details and take action, such as approve or reject.

![An approver reviewing the details of an access request.](../_images/governance-enduser-ui-approvals-details-page.png)

### Approve item

1. Click the desired item to view the details.

2. (Optional) Add a comment to the request:

   1. Click the Comments tab, then click [icon: add, set=material, size=inline] Add Comment.

   2. Enter a comment, and then click Add Comment to save it.

3. Click Approve.

4. Click Approve again to confirm the approval of the resource.

   Identity Governance provisions the resource to the end user.

### Reject item

1. Click the desired item to view the details.

2. (Optional) Add a comment to the request:

   1. Click the Comments tab, then click [icon: add, set=material, size=inline] Add Comment.

   2. Enter a comment, and then click [icon: add, set=material, size=inline] Add Comment.

3. Click Reject.

4. Enter a justification as to why the request is being rejected.

5. Click Reject.

### Forward to another user or role

If the owner is unable to make a decision on their assigned access request due to insufficient information or other reasons, they can approve the request item request to one or more users assigned to a specific role.

To forward a request item to another user or role:

1. Click desired request to view the details.

2. Click Forward.

3. Select one of the following:

   * Another user: Forward the item to a single user.

   * Users with assigned role: Forward the item to users in a role.

     |   |                                                                                                                                                    |
     | - | -------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Every user within the role can make a decision on the item. However, once a decision is reached, the assigned request item is considered complete. |

4. Select the user or role to assign the item to.

5. Enter a comment as to why the item is being forwarded.

6. Click Forward.

---

---
title: Certification campaigns
description: Overview of access certification campaigns for reviewing and certifying user access permissions
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/access-review-certification-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/access-review-certification-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["access certification", "access review", "certification campaign", "certification template", "certify access"]
section_ids:
  steps_to_certify_access: Steps to certify access
  certifications_tab: Certifications tab
  overview_tab: Overview tab
  example_of_certifying_access: Example of certifying access
---

# Certification campaigns

In Identity Governance, *certifying access* means reviewing the data and access a user has, such as access to applications, the accounts in those applications, and more.

## Steps to certify access

To certify access for users, you must:

1. [Create templates](access-review-manage-templates.html): Allows you to configure the data you want to certify.

2. [Run campaigns](access-review-manage-campaigns.html): After you create a template and are ready to kick off the review process, create a campaign.

3. [Certify data and access by end users](../end-user/access-review-user-cert-items.html): After you start a campaign, the template-defined end users (certifiers) receive notifications to review the data. The certifiers' review of the data is referred to as an *access review*.

## Certifications tab

Certifications and related features can be found by selecting Certification from the left navigation bar in the Advanced Identity Cloud admin console.

Three tabs display under Certification:

* [Overview](#governance_overview)

* [Templates](access-review-manage-templates.html)

* [Campaigns](access-review-manage-campaigns.html)

### Overview tab

To access the Overview tab, from the Advanced Identity Cloud admin console, go to Certification > Overview.

![Administration overview tab for Identity Governance.](../_images/governance-overview-tab.png)

The Overview landing page displays various metrics that allow you to view items such as campaign status, active reviews, and campaigns by type.

You can hover your cursor over the charts to view the data details.

| Data Element          | Description                                                                                                                                                                                                                                   |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Active Campaigns      | The number of campaigns currently in progress.                                                                                                                                                                                                |
| Expiring Campaigns    | The number of campaigns that expire in the next 2 weeks.                                                                                                                                                                                      |
| Active Reviews        | The total amount of line items in access reviews that are in progress. A line item is a record for a certifier to review. For example, the user Barbara Jensen's record that details their access to a particular application is a line item. |
| Campaigns By Type     | A breakdown of the varying types of certifications.                                                                                                                                                                                           |
| Campaigns By Status   | A breakdown of certifications by status.                                                                                                                                                                                                      |
| access review History | The number of line items certified versus revoked from campaigns.                                                                                                                                                                             |

## Example of certifying access

As an example of certifying access, an end user wants to know what applications a specific user, Barbara Jenson, has access to. The end user could want to do this for several reasons, such as increasing the company's security landscape by ensuring end users have accurate, appropriate access, or to comply with organizational, industry, or governmental policies. Barbara Jensen has an account and access to an application, called App A.

With Identity Governance, perform the following actions to achieve this:

* Configure and assign end users (certifiers) in your company to review Barbara's access to App A using templates.

* Kick off the data review using campaigns. Campaigns are the active processes, where certifiers review the data. In this case, it is Barbara's data. Certifiers are assigned to review the data in a campaign.

* Certifiers review Barbara's data and either certify (allow) or revoke (remove) the access to App A.

---

---
title: Certify access by event
description: Overview of event-based certification triggered by user lifecycle changes for faster access review
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/event-certification-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/event-certification-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["event-based certification", "access certification", "workflow events", "user create event", "user modify event"]
section_ids:
  governance-events: Events tab
  create_a_new_event: Create a new event
  edit_an_event: Edit an event
  activate_or_deactivate_an_event: Activate or deactivate an event
  delete_an_event: Delete an event
---

# Certify access by event

Administrators have the ability to configure certifications triggered by specific governance events. This process, known as *event-based certification*, provides faster certification resolution compared to scheduled campaigns spanning several weeks or months that involve multiple applications, complex rules, and hundreds of reviewers.

Event-based certifications runs an identity certification for any user that triggers the following events:

* User create: Advanced Identity Cloud detects when a user has been created.

* User modify: Advanced Identity Cloud detects when an existing user has been modified.

* Attribute change: Advanced Identity Cloud detects changes in an existing user's account attributes.

* User delete/deactivate: Advanced Identity Cloud detects if a user's account has been deleted or deactivated.

## Events tab

To access the Events tab, from the Advanced Identity Cloud admin console, go to Governance > Events.

|   |                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you have no events configured in the system, the message "There are no events to show" appears with a [icon: add, set=material, size=inline] New Event button on the page. |

![The governance events page.](../_images/governance-events.png)

* 1 Click Governance > Events on the Advanced Identity Cloud end-user UI.

* 2 [icon: add, set=material, size=inline] New Event. Click to add an event.

* 3 Search. Search by name (case-insensitive).

* 4 Name: Name of the event.

* 5 Event type: `User created` or `User updated`.

* 6 Action: `Certification` or `Workflow`.

* 7 Status: `Active` or `Inactive`.

* 8 Ellipsis ([icon: more_horiz, set=material, size=inline]). Click to edit, activate (deactivate if active), or delete the event.

The Name, Event type, Action, and Status columns are sortable in descending or ascending order.

## Create a new event

1. In the Advanced Identity Cloud admin console, click Governance > Events.

2. Click [icon: add, set=material, size=inline] New Event. You will have the option to create the following:

   * [Create a certification event](event-certification-editor.html)

   * [Create a workflow event](event-workflow-editor.html)

## Edit an event

1. In the Advanced Identity Cloud admin console, click Governance > Events.

2. Select an event, and then click ellipsis ([icon: more_horiz, set=material, size=inline]).

3. Click Edit, and make any changes to your event settings.

4. Click Save when done.

## Activate or deactivate an event

1. In the Advanced Identity Cloud admin console, click Governance > Events.

2. Select an event, and then click ellipsis ([icon: more_horiz, set=material, size=inline]).

3. Click Activate to set the event active in the system. The green `Active` label appears in the `Status` column.

4. To deactivate an active event:

   1. Select an event, and then click ellipsis ([icon: more_horiz, set=material, size=inline]).

   2. Click Deactivate.

   3. In the Deactivate Event modal, click Deactivate. The Inactive label appears in the Status column.

## Delete an event

1. In the Advanced Identity Cloud admin console, click Governance > Events.

2. Select an event, and then click ellipsis ([icon: more_horiz, set=material, size=inline]).

3. Click Delete to remove the event from the system.

4. Click Delete again in the confirmation modal.

---

---
title: Certify access by organization
description: Configure organization-based access certification for multi-tenant environments and partners
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/organization-certification-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/organization-certification-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["access certification", "access review", "organization certification", "partner certification", "organization admin"]
---

# Certify access by organization

Companies that host business partners, suppliers, or non-employees on a single platform can configure [organizations](../../identities/organizations.html) to differentiate the type of users. Identity Governance provides a way for companies to allow their business partners to certify access for their users.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Certifying access by organization is only available for non-event based identity certification templates. |

You can set up your organizations and organization admins In the Advanced Identity Cloud admin console. Learn more in [Organizations](../../identities/manage-identities.html#manage-organizations). When you have created an organization, you can add or import members and set the organization admins on the Administrators tab.

![Add organization admins in Advanced Identity Cloud admin console.](../_images/governance-add-organization-admins.png)

When creating an identity certification template, select your organization and child organizations on the What to Certify page.

![Select an organization on the What to certify page.](../_images/governance-template-organizations.png)

On the Who will Certify page, select `Organization Admin` as the Certifier Type.

![Select an organization admin on the Who will certify page.](../_images/governance-template-whowillcertify-orgs.png)

When end users from a partner organization submit access requests, the organization's administrators are responsible for reviewing and approving these requests.

![Organization admins appear on the access review page.](../_images/governance-access-review-orgs.png)

---

---
title: Configure data to review using templates
description: Create and manage certification templates that define data to review and review schedules
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/access-review-manage-templates
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/access-review-manage-templates.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["identity governance", "access certification", "certification templates", "access review templates", "create templates", "manage templates"]
section_ids:
  governance-template-landing-page: View saved templates
  which_certification_template_to_choose: Which certification template to choose
  governance-admin-create-campaign-templates: Create templates
  governance-admin-modify-cert-template: Modify templates
  activate_templates: Activate templates
  delete_a_template: Delete a template
---

# Configure data to review using templates

Templates are the first step in certifying access for users.

Templates are the underlying configurations of certifying access and define the data to review, who is responsible for the review, and when the data needs to be reviewed (on a periodic or ad hoc basis).

Often, organizations need to review the same data multiple times a year to ensure access is accurate. Templates make the certification process easier by saving the configuration settings used in the data review process.

Manage (create, duplicate, edit, or delete) templates on the Templates tab and schedule each campaign to run at a specific interval (if desired).

You can run templates on an ad-hoc or scheduled basis.

## View saved templates

To view saved templates, from the Advanced Identity Cloud admin console, click Certification > Templates tab. The page displays saved templates.

![Administration of templates in Identity Governance.](../_images/governance-templates-tab.png)

| Field         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name          | The name of the template.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Next run date | A date displays when the template is configured to run according to a schedule. If the template runs ad-hoc, then (None Scheduled) displays.                                                                                                                                                                                                                                                                                                   |
| Status        | A template can be in one of the following states:- Creating: The template is created in the background. This is a temporary state.

- Unused: The template isn't part of a campaign. In this state, you can edit or modify the template.

- Active: The template is turned into a campaign. In this state, you can view the template details, but you can't edit or modify it.The general sequence of states are *Creating → Unused → Active*. |

## Which certification template to choose

Identity Governance provides various certification templates to choose from. The underlying business objective you want to achieve determines which template type you choose.

![Certification template.](../_images/governance-certificate-campaign-template-modal.png)

The following scenarios show which template type to choose:

* You want to review the template to certify or revoke access to applications (accounts). You can specify to review the entitlements or roles a user has. The primary certifier (reviewer) of the certification should be users' managers.

  | Identity              | Entitlement assignment | Role membership       | Entitlement composition | Notes                                                                                                                                                                                 |
  | --------------------- | ---------------------- | --------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [icon: check, set=fa] | [icon: times, set=fa]  | [icon: times, set=fa] | [icon: times, set=fa]   | Not every user has entitlements. If you want to review the applications users have access to, and include those users who don't have entitlements, choose the identity certification. |

* You want to review to certify or revoke specific entitlements assigned to users in target applications. The primary certifier of the certification should be entitlement owners.

  | Identity              | Entitlement assignment | Role membership       | Entitlement composition | Notes                                                                                                                                                                           |
  | --------------------- | ---------------------- | --------------------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [icon: times, set=fa] | [icon: check, set=fa]  | [icon: times, set=fa] | [icon: times, set=fa]   | The entitlement assignment certification is the best choice in this scenario. It provides entitlement owners the ability to review the access users have to their entitlements. |

* You want to review the template to certify or revoke a user's role memberships. The primary certifier of the certification should be role owners.

  | Identity              | Entitlement assignment | Role membership       | Entitlement composition | Notes                                                                                                                                                                            |
  | --------------------- | ---------------------- | --------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [icon: times, set=fa] | [icon: times, set=fa]  | [icon: check, set=fa] | [icon: times, set=fa]   | The role membership certification is the best choice in this scenario as it provides the ability to review roles and users who are assigned to roles in Advanced Identity Cloud. |

* You want to review the template to evaluate, review, and modify the definition of entitlements within the certification process.

  | Identity              | Entitlement assignment | Role membership       | Entitlement composition | Notes                                                                                                                                                                                                                                                                                               |
  | --------------------- | ---------------------- | --------------------- | ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [icon: times, set=fa] | [icon: times, set=fa]  | [icon: times, set=fa] | [icon: check, set=fa]   | The entitlement composition certification is the best choice in this scenario because it enables reviewers to submit requests to change the entitlement definition, even independently of the certification decision, with options for drafting and deferring modification requests until sign off. |

## Create templates

Before you create a template, consider creating custom [governance glossary attributes](glossary.html) to enhance the data for onboarded target applications, entitlements, or roles. This will assist with template filtering and business decisions.

To create a template:

1. Navigate to the Certification > Templates tab.

2. Click [icon: add, set=material, size=inline] New Template.

3. Select the template type:

   * [Identity certification](template-identity-cert.html): Review and certify user accounts, entitlements, and access a user has on some or all applications. Primary reviewers are the users' managers, a single user, or users assigned to a role. Entitlements are the specific permissions given to an account in an target application. Each entitlement correlates to a permission.

   * [Entitlement assignment certification](template-entitlement-cert.html): Review and certify entitlements and the users who have access to entitlements in target applications. Primary reviewers are entitlement owners, a single user, or users assigned to a role.

   * [Role membership certification](template-role-membership-cert.html): Review and certify role memberships and the users who have access to roles in Advanced Identity Cloud. Primary reviewers are role owners, a single user, or users assigned to a role.

   * [Entitlement composition certification](template-entitlement-composition.html): Review and certify technical details and glossary metadata of entitlements. Primary certifiers are user, role, entitlement owner, custom certifier.

4. Click Next.

   |   |                                                                                         |
   | - | --------------------------------------------------------------------------------------- |
   |   | To continue setting up the template you select, click on the preceding links in step 3. |

## Modify templates

You can modify various template items:

1. From the Advanced Identity Cloud admin console, go to Certification > Template tab.

2. Locate the template and click the ellipsis ([icon: more_horiz, set=material, size=inline]) to perform various actions:

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | To view additional templates, click the caret icons at the bottom of the table. |

   | Field         | Description                                                                                                                                                                                                       |
   | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Duplicate     | Duplicate the template details to create a new template, and edit or modify as needed. The characters **(copy)** are appended to the newly duplicated template.                                                   |
   | View Details  | This option displays **if the template has been run at least once**. It provides a read-only view into the configurations on the template. After you run a template, you can't change the configuration settings. |
   | Edit Template | This option displays if you create the template, but never run it to create a campaign. In this case, you can edit or modify the template configuration.                                                          |

## Activate templates

Activate a template to kick off the review process (a campaign).

You can activate a template by:

* Creating a schedule when you define the template.

* Adding a schedule to the template after you define the template.

* Running the template on an ad-hoc basis.

To activate a template:

1. From the Advanced Identity Cloud admin console, go to Certification > Template tab.

2. Locate the template and click [icon: add, set=material, size=inline] to perform various actions:

   |   |                                                                                 |
   | - | ------------------------------------------------------------------------------- |
   |   | To view additional templates, click the caret icons at the bottom of the table. |

   | Action            | Field                                                                                                                                                                                                                                                                                                                                       |
   | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Run Now           | This activates the template and kicks off the review process (campaign). When selected, the active campaign displays in the Campaigns tab.	When you create a template, if you select Run on a schedule under the When to Certify section. The campaign runs on the set schedule and display on the Campaigns tab at the specified interval. |
   | Schedule Campaign | This option displays **if you didn't configure a schedule** when creating the template. This creates a run schedule for the template.                                                                                                                                                                                                       |
   | Edit Schedule     | This option displays **if you did configure a schedule** when creating the template, but you would like to modify the existing schedule.                                                                                                                                                                                                    |

## Delete a template

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can only delete Unused certification templates through the UI. This deletion can't be undone.A template becomes active after you use it to create a campaign. It remains active even if there are no campaigns attached to it. You can't modify or delete an active template through the UI.If you must delete an active template, you can use the REST API. Learn more in [REST API: delete certification template](../rest-api/endpoints/rest-iga.html#certification-template-id-delete). |

To delete a template:

1. From the Advanced Identity Cloud admin console, go to Certification > Template tab.

2. Locate the template, check that the template is in an Unused state.

3. Click [icon: more_horiz, set=material, size=inline], and then click Delete. You can't undo the deletion.

---

---
title: Configure entitlement lifecycle management
description: Enable and configure delegated entitlement lifecycle management with scopes and approval workflows
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/entitlement-lifecycle-mgmt
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/entitlement-lifecycle-mgmt.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["entitlement lifecycle management", "entitlement LCM", "delegated administration", "create entitlement", "modify entitlement", "scopes", "workflows"]
section_ids:
  governance_personas: Governance personas
  enable_entitlement_lcm: Enable Entitlement LCM
  configure_authorization: Configure authorization
  tips_on_scopes: Tips on scopes
  add_scopes_and_assign_to_users: Add scopes and assign to users
  configure_entitlement_lifecycle_workflows: Configure entitlement lifecycle workflows
  troubleshooting_entitlements: Troubleshooting entitlements
---

# Configure entitlement lifecycle management

Entitlement lifecycle management (LCM) provides a type of delegated administration, allowing application owners, entitlement owners, and end users authorized with the proper scope permissions to manage entitlements within the applications available to them. By using Entitlement LCM, companies can keep entitlement attributes up-to-date, reducing the risk of outdated or inaccurate entitlements impacting decision making.

Entitlement LCM also enforces policies by requiring approval workflows before any entitlement changes are applied. This prevents users from granting excessive permissions without oversight and ensures access remains aligned with organizational policies.

## Governance personas

By default, governance administrators, application owners, entitlement owners, and end users with scoped permissions can manage entitlements in the system. These users have the following permissions:

| Action                          | Admin                    | Application Owner        | Entitlement Owner        | End user  |
| ------------------------------- | ------------------------ | ------------------------ | ------------------------ | --------- |
| View entitlement                | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |
| View users who have entitlement | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |
| Create entitlement              | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: times, set=fa]No  | If scoped |
| Modify entitlement              | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |

## Enable Entitlement LCM

Governance administrators must enable Entitlement LCM to activate the feature for their users.

1. In the Advanced Identity Cloud admin console, go to Governance > Requests.

2. On the Requests page, click the Settings tab.

3. In the Governance LCM section, click Activate.

4. In the Governance LCM modal, read what activating this feature entails, and click Next.

5. In the Governance LCM modal, click Entitlement LCM, and then click Activate. The governance LCM is now active on your tenant.

   ![Enable governance LCM on the Requests page.](../_images/governance-lcm-enable.png)

## Configure authorization

Entitlement LCM enables administrators to delegate entitlement management to authorized users. Scope permissions have been enhanced to grant a specific subset of permissions for managing entitlements. The scope permissions are summarized as follows:

| Permission          | Applies to   | Description                                                                                                                                                                                                                                                         |
| ------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| View Applications   | Applications | Allows the user to view matching applications. This scope is implicit when Create Entitlements is selected.                                                                                                                                                         |
| Create Entitlements | Applications | Allows the user to create entitlements for the matching applications.                                                                                                                                                                                               |
| View Entitlements   | Entitlements | Allows the user to view matching entitlements. This scope is implicit when Modify Entitlements or View Grants is selected.                                                                                                                                          |
| Modify Entitlements | Entitlements | Allows the user to modify the matching entitlements.                                                                                                                                                                                                                |
| View Grants         | Entitlements | Allows the user to view the other users who are assigned the entitlement.&#xA;&#xA;Ping Identity recommends that you always grant View Grants privileges so that users carrying out entitlement lifecycle management can see who has been assigned the entitlement. |

### Tips on scopes

|   |                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Scopes provide the permissions to let end users to act only on applications and entitlements to which they're permitted.For example, when you assign a scope for an application with the `Create Entitlements` permission, the end user can create entitlements for the application in that scope. However, this doesn't mean they can view entitlements. For that, they must have the `View Entitlements` permission. |

The following rules apply to scope permission:

* By default, scopes are disabled in Identity Governance. You can enable scopes using the API. Learn more in [Enable scopes](access-request-configure.html#enable-scopes).

* If end users have scope permissions for view entitlements, they can view those entitlements regardless of the application permissions.

* If end users have modify permissions, they can modify the entitlements you can see.

* If end users have view grant permissions, they can view the users of the entitlements you can see.

### Add scopes and assign to users

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. In the Advanced Identity Cloud admin console, go to Governance > Scopes.

3. Click [icon: add, set=material, size=inline] New Scopes.

4. On the New Scope page, enter the following in the Details section:

   1. Name: Enter the name for the scope.

   2. Description: Enter a description for the scope.

   3. Click Next.

      ![Scope details page displaying name and description](../_images/governance-lcm-scope-details.png)

5. On the Applies to page, define which users should be subject to this scope. Decide if you want to grant application or entitlement permissions to the end user.

   1. Select if the All or Any condition must be met.

   2. Select a property for this scoping rule. For example, select userName.

   3. Select an operator for the scoping rule. For example, select contains.

   4. Enter an entitlement.

   5. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

   6. Click Next.

      ![Scope applies to page defines the user to which the scope applies.](../_images/governance-lcm-scope-applies-to.png)

6. On the Access page, enter the following depending if you are granting applications or entitlement permissions:

   * For application permissions:

     1. Select the Applications checkbox.

     2. Click All Applications or Applications matching a filter. Click Applications matching a filter.

     3. Select if All or Any condition must be met.

     4. Select a property for this scoping rule. For example, select name.

     5. Select an operator for the scoping rule. For example, select is.

     6. Enter an application.

     7. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

     8. Click Create Entitlements.

        |   |                                                          |
        | - | -------------------------------------------------------- |
        |   | The View Applications scope permission is also included. |

     9. Click Save.

        The end user now has the permission to create new entitlements for the matching application.

        ![Scope access displaying the filters for the application.](../_images/governance-lcm-scope-access-apps.png)

   * For entitlement permissions:

     1. Select the Entitlements checkbox.

     2. If you click Applications matching a filter, click All Entitlements or Entitlements matching a filter.

     3. Select if the All or Any condition must be met.

     4. Select a property for this scoping rule. For example, select userName.

     5. Select an operator for the scoping rule. For example, select is.

     6. Enter a user.

     7. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

     8. Click Modify Entitlements.

        |   |                                                          |
        | - | -------------------------------------------------------- |
        |   | The View Entitlements scope permission is also included. |

     9. Click View Grants to allow the end user to view who has the entitlement.

     10. Click Save.

         ![Scope access displaying the filters for the entitlement.](../_images/governance-lcm-scope-access-entitlements.png)

## Configure entitlement lifecycle workflows

Identity Governance provides the out-of-the-box request types and workflows to enable authorized users to carry out Entitlement LCM tasks:

| Request Type      | Workflow           |
| ----------------- | ------------------ |
| createEntitlement | Create Entitlement |
| modifyEntitlement | Modify Entitlement |

As with all other Identity Governance requests, the Entitlement LCM actions are defined and processed in request workflows that allow users to:

* Create new entitlements

* Provide source entitlement attribute values

* Enrich the entitlement glossary

* Modify existing entitlements.

## Troubleshooting entitlements

Typical troubleshooting cases that can occur with entitlements are:

* Entitlements aren't being onboarded from the application.

* Onboarded entitlements aren't visible in the catalog.

* Onboarded entitlements don't have a display name.

* Entitlements have been assigned to users but aren't visible in the user's access.

* Duplicate entitlement assignments assigned to the user.

---

---
title: Copy and edit the default workflows
description: Copy and edit default workflows to customize approval processes for access requests
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/workflow-modify-default
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/workflow-modify-default.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["workflows", "default workflows", "copy workflow", "edit workflow", "custom workflow"]
section_ids:
  copy_and_edit_your_default_workflow: Copy and edit your default workflow
---

# Copy and edit the default workflows

Default workflows are read-only to preserve their original functionality and behavior. However, you can create a copy of any default workflow and modify the draft version to fit your needs.

## Copy and edit your default workflow

1. In the Advanced Identity Cloud admin console, click Governance > Workflows.

2. Select a default workflow, click the ellipsis icon ([icon: more_horiz, set=material, size=inline]), and then click Duplicate.

3. In the Workflow Details modal, enter a name (also referred to as `workflow ID`) for your workflow copy, and click Save. For example, `BasicApplicationGrant-copy`.

4. In your workflow copy, make any changes to the workflow or its nodes, and when ready, click Save.

5. Click Publish to activate it.

6. Integrate the new workflow by updating the request type. Go to Governance > Requests > Request Types.

7. Click the request type that you want to update. For example, click the Grant Application request type.

8. Click Workflow, and select the new workflow copy. For example, select BasicApplicationGrant-copy.

9. Click Save.

---

---
title: Create a certification event
description: Create event-triggered certification campaigns that run when specific governance events occur
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/event-certification-editor
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/event-certification-editor.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["event-based certification", "certification event", "create event", "access review", "campaign"]
section_ids:
  cert-event-new: Create a new certification event
  cert-event-trigger: Event trigger
  cert-event-action: Event action
  cert-event-details: Event details
  cert-event-campaign-details: Event campaign details
  cert-event-what-to-certify: What to certify
  cert-event-duration: Duration
  cert-event-who-will-certify: Who will Certify
  cert-event-notifications: Notifications
  cert-event-additional-options: Additional options
  cert-event-summary: Summary
---

# Create a certification event

The Advanced Identity Cloud admin console provides simple steps to set up a certification event using the campaign template format.

The following table lists the sections that you must follow to set up a certification event template.

| Section                                                | Description                                                          |
| ------------------------------------------------------ | -------------------------------------------------------------------- |
| [Create a new certification event](#cert-event-new)    | Create a new certification event.                                    |
| [Event trigger](#cert-event-trigger)                   | Type of event trigger.                                               |
| [Event action](#cert-event-action)                     | Type of action to take when the trigger occurs.                      |
| [Event details](#cert-event-details)                   | General event details of the template.                               |
| [Event campaign details](#cert-event-campaign-details) | Certification campaign details.                                      |
| [What to certify](#cert-event-what-to-certify)         | Items to be certified.                                               |
| [Duration](#cert-event-duration)                       | Duration of the certification event.                                 |
| [Who will Certify](#cert-event-who-will-certify)       | Users who will certify the event.                                    |
| [Notifications](#cert-event-notifications)             | (Optional) Email notifications options.                              |
| [Additional options](#cert-event-additional-options)   | (Optional) Various configurations to allow during the certification. |
| [Summary](#cert-event-summary)                         | Summary of your selected sections.                                   |

## Create a new certification event

1. In the Advanced Identity Cloud admin console, click Governance > Events.

2. On the Governance Events page, click [icon: add, set=material, size=inline] New Event. The New Event modal appears.

### Event trigger

This section sets the type of event trigger for your workflow.

1. In the New Event modal, select an event trigger:

   * User created: Trigger an action when a user is created.

   * User updated: Trigger an action when a user is updated.

2. Click Next.

### Event action

This section sets the type of action for your certification when the event is triggered.

1. In the New Event modal, review the event actions, and click Certification:

   * Certification. Trigger a certification campaign when an event occurs.

   * Workflow. Trigger a workflow when an event occurs.

2. Click Next.

### Event details

* In the Event Details modal, complete the following fields, and click Next.

  | Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Event Name        | Display name for the event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | Event Description | (Optional) Enter a general description for the event. Your company should follow a descriptive convention to describe each of your events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | Event Owners      | Enter the owner(s) of the event. Only owners can fully control their events, including event decisions, event assignment changes, sign off, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | Trigger for       | Determine the users for which to apply the trigger. Options are:- All users: Trigger for all users in your system.

  - A subset of users: Trigger for a subset of users in your system. This option opens a filter to set up your users.

    > **Collapse: Event filter**
    >
    > ![governance event filter](../_images/governance-event-filter.png)
    >
    > * 1 Trigger if `All` or `Any` conditions are met.
    >
    > * 2 Previous value of
    >
    >   * `Previous value of` (appears for `User created` triggers)
    >
    >   * `Current value of` (appears for `User created` triggers)
    >
    >   * `Before` (appears for `User updated` triggers)
    >
    >   * `After` (appears for `User updated` triggers)
    >
    > * 3 Type to search: Select an attribute from the list.
    >
    > * 4 Conditions:
    >
    >   * Contains
    >
    >   * Does not contain
    >
    >   * Is
    >
    >   * Is not
    >
    >   * Is present
    >
    >   * Is not present
    >
    >   * Starts with
    >
    >   * Does not start with
    >
    >   * GTE
    >
    >   * GT
    >
    >   * LTE
    >
    >   * LT
    >
    > * 5 Enter a value for your filtered condition.
    >
    > * 6 Click [icon: plus, set=fa]to add the condition.
    >
    > * 7 Click Advanced Editor. |

### Event campaign details

This section sets the campaign details for your certification when the event is triggered.

* In the New Certification Event modal, complete the following fields, and click Next.

  | Field          | Description                                                                                                                                                                                                    |
  | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Name           | Display name for the campaign.                                                                                                                                                                                 |
  | Description    | (Optional) Enter a general description for the certification campaign. Your company should follow a descriptive convention to describe each of your events.                                                    |
  | Campaign Owner | Enter the owner(s) of the certification campaign event. Only certification owners can fully control their certifications, including certification decisions, certifier assignment changes, sign off, and more. |

### What to certify

This section defines what to certify as part of this campaign.

1. In the New Certification Event modal, select any or all of the following:

   * Accounts: The user accounts in the external [applications](../../app-management/applications.html).

   * Entitlements: The authorization (privileges) the user has in the external [applications](../../app-management/applications.html).

   * Roles: The Advanced Identity Cloud roles a user is a member of.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                     |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | Depending on your selection, the estimated total of applications, accounts, and entitlements subject to this certification are displayed at the bottom of the page:- If you selected Accounts: *Applications* and *accounts* totals are displayed.

     - If you selected Entitlements: *Applications* and *entitlements* totals are displayed.

     - If you selected Roles: *Roles* totals are displayed. |

2. Complete the following fields, and click Next.

   | Field                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Applications                            | Certify one of the following:- All applications

   - Specific applications: If you select this, an additional box displays to select which Applications to certify.

   - Applications matching a specific filter: Create a filter to certify specific applications.                                                                                                                                                                                                                                                                                                                           |
   | Accounts                                | *Displays if you select Accounts in step 1*. Select one of the following:- All accounts in selected applications.

   - Accounts matching a filter: Create a filter for accounts that match the filter.                                                                                                                                                                                                                                                                                                                                                                                      |
   | Entitlements                            | *Displays if you select Entitlements in step 1*.Certify one of the following:- All entitlements

   - Entitlements matching a filter: Create a filter to match specific entitlements.

     If you create a governance glossary attribute and populate the attribute you create on the onboarded entitlement(s), you can filter on the attribute(s) you create. Learn more in [Create an entitlement glossary attribute](glossary.html#create-entitlement-attribute).                                                                                                                           |
   | Roles                                   | *Displays if you select Roles in step 1.*Certify one of the following:- All roles

   - Roles matching a filter: Create a filter to certify specific roles.

     If you create a governance glossary attribute and populate the attribute you create on roles, you can filter on the attribute(s) you create. Learn more in [Create a role glossary attribute](glossary.html#create-role-glossary).                                                                                                                                                                                            |
   | Exclude access granted only from a role | *Displays if you select `Accounts` or `Entitlements` in step 1.* Excludes account and entitlement line items that are granted *only* through a role. Enabled by default.	Identity Governance can't certify or revoke an application or entitlement from an end user when they're granted access through a role; therefore, excluding these line items can help reduce unnecessary information in the certification.Learn more in [Decisions change based on how you grant access](../end-user/access-review-user-cert-items.html#governance-user-items-cert-make-decision-change-access). |
   | Filter by last certification decision   | Set a filter when one of the following conditions are met. The decision properties are:- Campaign ID

   - Completion date\[.label]

   - Status

   - DecisionClick [icon: add, set=material, size=inline] to add the rule to your filter.                                                                                                                                                                                                                                                                                                                                                        |

### Duration

The Duration section lets the administrator specify when to kick off the review process (campaign) and what to do in the event the campaign expires.

* Complete the following fields, and click Next.

  | Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Duration              | Specify the amount of time each access review (campaign) has before expiration. You can specify the duration in days, weeks, months, or years.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | When Campaign Expires | Select a behavior to handle the open access review (campaign) line items when the campaign expires:- Close \<selection> open items: Complete the items using the given information after the campaign expires. The administrator can select what decision to add to the item (`certify`, `revoke`, and `allow exception to`) and when that decision takes effect. The decision can take effect `immediately` or `after a duration` (in days).

  - Reassign to: Select a given user or role that the access review (campaign) is reassigned to after the expiration date. The campaign won't be closed.

  - Do Nothing: No action will be taken, and the line items will remain in progress. |

### Who will Certify

This section allows you to specify the users that review and make decisions about the items you defined in the What to Certify section.

* Complete the following fields, and click Next.

  | Field                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
  | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Certifier Type            | Specify who can review and certify user access by selecting one of the following:- User: Select a single user to review and make a decision on every record. When you select this, a Select user box displays. Select the user who will certify the campaign.

  - Role: Select a role that allows any of its members to review every record. When you select this, a Select a role box displays. Select a role from the list of the created roles in Advanced Identity Cloud.

  - Manager: The user's manager becomes the certifier of their data (also known as a line item). |
  | Enable default certifiers | Select a certifier to assign in case an access review (campaign) line item isn't assigned a certifier. For example, if the manager is the certifier and the user has no manager defined, then the default certifier will be assigned the access review for this user.                                                                                                                                                                                                                                                                                                        |

### Notifications

This optional section allows you to send email notifications when one or more campaign events are triggered. For example, when a campaign is about to expire or when a certifier is reassigned.

1. Define an email template for each selected notification. Each notification requires an associated email template.

   1. From the left navigation pane in the Advanced Identity Cloud admin console, go to Email > Templates. Learn more in [Email templates](../../tenants/email-templates.html).

      |   |                                                                                                                                                            |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | There are preset email templates created for certification templates. Use these as a base, copy the email template, and customize them to suit your needs. |

2. Select any of the notification types, and then click Next.

   | Field                        | Description                                                                                                                                                                                                                                                                  |
   | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Send initial notification    | Send a notification any time a certifier is assigned to a line item.                                                                                                                                                                                                         |
   | Send reassign notification   | Send to a new certifier when a line item in an access review (campaign) is reassigned or forwarded to them.                                                                                                                                                                  |
   | Send expiration notification | Send a reminder notification to the certifiers before a campaign expires. Select the number of days, before the campaign expires, to send the reminder.                                                                                                                      |
   | Send reminders               | Send a notification to remind certifiers to act on access review (campaign) line items. Select the number of days, weeks, months, or years to send the reminder.                                                                                                             |
   | Enable escalation            | Send an escalation notification to specific recipients that certifiers haven't completed their actions on a campaign. When selected, an additional Escalation Owner box displays. Select the number of days, weeks, months, or years and the user to send the escalation to. |

### Additional options

This optional section allows you to configure other options for a campaign, such as performing bulk certifications or reassigning tasks to another user or group.

1. Complete the following optional fields, and then click Next.

   | Field                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Allow self-certification                     | Allows select individuals to certify their own data.The options to choose from are:- All certifiers: Users who are certifying the access review (campaign) can certify their own access.

   - Owners and administrators: Users who are campaign owners or tenant administrators can certify their own access.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   | Enable line-item reassignment and delegation | Allow the certifier to reassign or forward a line item to another user.When you select this box, you can choose the following options:- Forward: Allow certifiers to forward their access review (campaign) to another certifier. When forwarding an access review, other certifiers are **removed from the access review in its entirety**. Learn more in [forward line items](../end-user/access-review-user-cert-items.html#governance-user-items-cert-forward).

   - Reassign: Select the privileges the current certifier can assign to the new certifier:

     * Add Comment

     * Make Decision

     * Reassign/Forward

     * Sign off

       Learn more in [reassign line items](../end-user/access-review-user-cert-items.html#governance-user-items-cert-reassign). |
   | Require justification on revoke              | Require a justification when revoking.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   | Require justification on exception           | Require a justification for an exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Allow exceptions                             | Allow certifiers to continue to certify line items assigned to them **after** the campaign expires. Select a duration in days, months, weeks, or years.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | Allow bulk-decisions                         | Allow certifiers to make line item decisions in bulk.This includes:- Making a decision (certify, revoke, exception).

   - If Enable line item reassignment and delegation is enabled, then you can bulk Reassign or Forward line items.	As an administrator, most access reviews require an in-depth look on each line item to ensure the accuracy of each item. Bulk-decisions allow for a certifier to make a decision on many items at once, which could lead to inaccurate data. Use caution when selecting this option.                                                                                                                                                                                                                                          |
   | Allow partial sign-off                       | Allow a certifier to sign-off on an access review **before** their assigned line items have a decision made on them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   | Process remediation                          | Revokes the end user's access in the target application when a certifier revokes (denies) the line item. Select a workflow to run either immediately after revocation of access or after a duration.	To ensure end-user access is removed when revoking a line item, you must enable this property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Summary

The Summary section is the final section in creating a template. It gives a breakdown of each section in the template, allowing for a review.

Summary steps:

1. Review each section.

2. Click Save to complete the template. Your event appears on the Events page.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Under the What to Certify review section, ensure that the Total Decision Items is greater than 0. If you identify that this is 0, this means that the template didn't identify items to be certified. Therefore, if you create the campaign off of the template, the system will immediately cancel the campaign. If you identify this to be 0, go back to the What to Certify section and adjust your settings. |

---

---
title: Create a form for custom request types
description: Create and configure custom request forms for custom request types with approval workflows
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/governance-forms-custom-request
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-forms-custom-request.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["forms", "custom request form", "custom request type", "create form", "access request"]
section_ids:
  key_points: Key points
  steps: Steps
  end_user_steps: End user steps
---

# Create a form for custom request types

Creating a form for custom request types requires several steps the administrator must carry out:

* Create a custom request type.

* Create a simple form for the new custom request type.

* Create a workflow to handle the custom request type and the form.

* Submit a request.

## Key points

The Form creator must consider the following key points:

* You can only link a custom request type to a single form. While a form can be used with multiple custom requests, each custom request can only be associated with one form at a time.

* The typical use case is to create a form that aligns with the custom request's object type schema. For an example, learn more in [Create a custom request type](example-workflow-custom-request-type-with-form.html#create-custom-request-type).

* In a workflow, you can assign a form in the Approval node properties pane. For typical cases, you can select Choose a form and select your custom request form.

  ![Approval node with choose a form selection](../_images/governance-forms-choose-a-form.png)

- For more customization, you can define the keys exactly as you want. Once a request is generated, the form's contents are copied into the request, making those properties available for use within the workflow to provision access as needed. For example, you can define a key with a value of `custom.NAME`. When a user submits a request, the key appears in `request.custom.NAME` with the value, Testing:

  ```json
  {
    "id": "409f28fc-65f6-41b8-a9f5-bb3a64f55925",
    "requester": {
      "givenName": "Frank",
      "id": "managed/user/c51d9ee1-43b3-49d1-8742-cbb33842a5cc",
      "mail": "frank.york@example.com",
      "sn": "York",
      "userName": "fyork",
      "isAdmin": false
    },
    "requestType": "applicationGrant",
    "request": {
      "common": {
        "priority": "low",
        "justification": "Testing",
        "applicationId": "d248cc89-79b2-4f6a-98bc-46d0a938318f",
        "userId": "f3617664-4dd2-48eb-bdae-512f45b157df",
        "isDraft": false,
        "context": {
          "type": "request"
        }
      },
      "custom": {
        "NAME": "Testing"
      },
      "_rev": 1
    }
    .....
  }
  ```

## Steps

Governance or tenant administrators can carry out the following steps to create a new custom request form:

1. Create a custom request type. You can find an example in [Workflow using a custom request type and form](example-workflow-custom-request-type-with-form.html#create-custom-request-type).

2. In the Advanced Identity Cloud end-user UI, click Forms > [icon: add, set=material, size=inline] New Form.

3. In the New Form modal, click Custom request form, and then click Next.

4. In the modal, enter the following and click Save when completed:

   | Field                                  | Description                                                                                                                                                                                                                                               |
   | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Form Name                              | Enter a descriptive name for your form. Follow any convention established by your company.                                                                                                                                                                |
   | Description (optional)                 | Enter a general description for the form.                                                                                                                                                                                                                 |
   | Request Type (optional)                | Select a request type this form is intended for.	You can only assign one form to each request type.                                                                                                                                                       |
   | []()Use this form for request creation | If you click the checkbox, make this form available to the end user for new requests on the Advanced Identity Cloud end-user UI.If you leave the checkbox unchecked, the request type only offers `Key` field suggestions during the form design process. |

   ![Custom request form page showing the Use this form for request creation checkbox.](../_images/custom-request-form-new-request.png)

5. In the Forms editor, create your form by dragging and dropping any of the [form fields](governance-forms-fields.html) onto the canvas and fill in the fields in the right pane.

6. Click Preview to see the form you created. Click Exit Preview to go back. Copy and save the Preview URL in the top right corner. This is the URL on the Advanced Identity Cloud end-user UI.

   ![Custom request form showing the Preview button and the Preview URL](../_images/custom-request-form-field.png)

7. Click Save. Your form appears on the Forms page.

## End user steps

Administrators can test the new custom request form by logging in to an end-user account.

1. In the Advanced Identity Cloud end-user UI, log in as an end user.

2. If you clicked Use this form for request creation, you can make the new custom request form available to the end user by using the Preview URL. For example, the end user pastes in the preview URL in the Advanced Identity Cloud end-user UI browser to access the custom request form.

   ![Custom request form in the Advanced Identity Cloud end-user UI.](../_images/custom-request-form-end-user.png)

---

---
title: Create a role membership certification template
description: Create a role membership certification template to certify or revoke user role memberships
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/template-role-membership-cert
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/template-role-membership-cert.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["role membership certification", "certification template", "access review", "create template", "role owner"]
section_ids:
  role-membership-cert-template-details: Details
  role-membership-cert-template-what-to-certify: What to Certify
  role-membership-cert-template-when-to-certify: When to Certify
  role-membership-cert-template-who-will-certify: Who will Certify
  role-membership-cert-template-notifications: Notifications
  role-membership-cert-template-additional-options: Additional options
  role-membership-cert-template-customization: Customization
  role-membership-cert-template-cert-summary: Summary
---

# Create a role membership certification template

Select a role membership certification to certify or revoke user's role memberships using a template.

Certifiers review roles a user has in Advanced Identity Cloud. When certifying, if the role line item has the decision of `revoke`, then Identity Governance removes the role when the certification is signed-off. Learn more in [Make a decision (certify)](../end-user/access-review-user-cert-items.html#governance-user-items-cert-make-decision).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Before creating a role membership certification template, assign a role owner to each role in Advanced Identity Cloud. Role owners are the individuals responsible for the role, for example, the members of the role and metadata.To assign a role owner:1) From the Advanced Identity Cloud admin console, click [icon: people, set=material, size=inline] > Manage > Alpha realm — roles.

2) Select desired role.

3) On the Details tab, select a user from the Role Owner field.

4) Click Save. |

The following table lists the areas to configure for each campaign template type:

| Section                                                                 | Description                                                                                                               |
| ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| [Details](#role-membership-cert-template-details)                       | General details of the template, such as the name, description, and a default certifier.                                  |
| [What to Certify](#role-membership-cert-template-what-to-certify)       | The items to be certified.                                                                                                |
| [When to Certify](#role-membership-cert-template-when-to-certify)       | The cadence in which the review process is kicks off (campaign).                                                          |
| [Who will Certify](#role-membership-cert-template-who-will-certify)     | The end users responsible for certifying the items in the campaign.                                                       |
| [Notifications](#role-membership-cert-template-notifications)           | (Optional) Set up email notifications based on various events that take place during the certification process.           |
| [Additional options](#role-membership-cert-template-additional-options) | (Optional) Various configurations to allow during the campaign, such as bulk actions on line items or self-certification. |
| [Summary](#role-membership-cert-template-cert-summary)                  | Summary of configured sections.                                                                                           |

## Details

This section includes basic information about the template, such as the display name, description, owner, and staging process. To add basic template information, do the following:

1. From the Advanced Identity Cloud admin console, click Certification > Templates > + New Template.

2. Select Role Membership Certification.

3. Click Next.

4. Complete the following fields:

   | Field                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Certification Name      | The display name for the certification. This certification name displays on both the certification tab and the end-user task dashboard.Define a date variable in the name of the certification to know which campaign kicks off. Identity Governance uses [moment.js](https://momentjs.com/docs/#/displaying/format/) to format the date.For example, if you have a certification that's scheduled to run every 2 weeks, appending the date to the name lets you know which campaign you are working on. The certification name can include the date (year, month, day), time (hour, minute), and time of day (AM/PM):`Campaign name: {{YYYY-MM-DD-hh:mma}}`When you kick off a template into a campaign, an example of the name is: `Campaign name — 2023-12-12-08:18pm`	After you start the campaign for the first time, you can't change the template name. |
   | Description             | Enter a general description for the certification. Your company should follow a convention to describe each of your certifications.	This field is limited to 1000 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Certification Owner     | Enter the owner of the certification. Only certification owners can fully control their certifications, including certification decisions, certifier assignment changes, sign off, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | Enable Campaign Staging | Enable certification staging to set up the certification in the system but not activate it in production. This option allows compliance officers to preview a certification before it's activated and exposed to end users. Compliance officers can inspect and review the content, decision items, and other details to decide whether to activate or delete the campaign.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

5. Click Next.

## What to Certify

This section lets you define which roles or users to certify.

To define which users and roles to certify:

1. Complete the following fields:

   | Field                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Roles                                        | Certify one of the following:- All roles

   - Roles matching a filter: Create a filter to certify specific roles.

     If you create a governance glossary attribute and enhance roles with the attribute, you can filter on the attribute(s) you create. Learn more in [Manage governance glossary](glossary.html).                                                                                                                                                                |
   | Users                                        | Certify one of the following:- All users

   - A single user

   - Users matching a filter: Create a filter to certify select users.                                                                                                                                                                                                                                                                                                                                                  |
   | Exclude dynamically granted role memberships | Enabled by default.Exclude role line items that are granted to an end user through a condition.	Identity Governance can't certify or revoke an end user being a member of a role through a condition; therefore, excluding these line items can help reduce unnecessary information in the certification.Learn more in [Decisions change based on how you grant access](../end-user/access-review-user-cert-items.html#governance-user-items-cert-make-decision-change-access). |
   | (Optional) Show advanced filters             | To certify accounts based on properties from the last certification decision made on a line item from the drop-down, select Filter by last certification decision.A line item is a particular record for a certifier to review.                                                                                                                                                                                                                                                 |

2. Click Next.

## When to Certify

The When to Certify section lets the administrator specify when to kick off the review process (campaign) and what to do in the event the campaign expires.

To complete this section, do the following:

1. Complete the following fields:

   | Field                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Schedule              | Define whether the template will kick off on a periodic basis. If selected, input various choices to define the schedule.Check the Run on a schedule box to define a schedule for the template.Options include:- Run Every: Run the certification every specified number of days, weeks, months, or years.

   - Start: Specify a date and start time when this campaign kicks off for the first time.

   - End: Run the certification on its defined periodic basis until this date and time is reached.                                                                                                                                                                  |
   | Campaign Duration     | Specify the amount of time each access review (campaign) has before expiration. You can specify the duration in days, weeks, months, or years.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   | When Campaign Expires | Select a behavior to handle the open access review (campaign) line items when the campaign expires:- Close open items: Complete the items using the given information after the campaign expires. The administrator can select what decision to add to the item (certify, revoke, and allow exception to) and when that decision takes effect. The decision can take effect immediately or after a duration (in days).

   - Reassign to: Select a given user or role that the access review (campaign) is reassigned to after the expiration date. The campaign will not be closed.

   - Do Nothing: No action will be taken, and the line items will remain in progress. |

2. Click Next.

## Who will Certify

This section allows you to specify the users that review and make decisions about the items you defined in the What to Certify section.

To define who will certify the certification:

1. Complete the following fields:

   | Field                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Certifier Type            | Specify who can review and certify user access by selecting one of the following:- User: Select a single user to review and make a decision on every record. When you select this, a Select user box displays. Select the user who will certify the campaign.

   - Role: Select a role that allows any of its members to review every record. When you select this, a Select a role box displays. Select a role from the list of the created roles in Advanced Identity Cloud.

   - Role Owner: The individual who manages the role. Learn more in [add role owner](#role-membership-cert-add-role-owner). |
   | Enable default certifiers | Select a certifier to assign in case an access review (campaign) line item isn't assigned a certifier. For example, if the role owner is the certifier and the role has no role owner defined, then Identity Governance assigns the specified default certifier to the access review for the role.                                                                                                                                                                                                                                                                                                     |

2. Click Next.

## Notifications

This optional section allows you to send email notifications when one or more campaign events are triggered. For example, when a campaign is about to expire or when a certifier is reassigned.

To complete this section, do the following:

1. Define an email template for each selected notification. Each notification requires an associated email template. From the left navigation pane in the Advanced Identity Cloud admin console, go to Email > Templates. Learn more in [Email templates](../../tenants/email-templates.html).

   |   |                                                                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | There are preset email templates created for certification templates. Use these as a base, copy the email template, and customize them to suit your needs. |

   To reference variables in your email templates for Identity Governance, the object is nested an additional level. The following table shows how to access these objects:

   | Item                | Usage                                                                                                                                                                                                                                                                                                                                                                                                         |
   | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | User attributes     | Use the syntax `object.user.userAttribute`.Use the attributes available from the email template screen. Learn more in [Email templates](../../tenants/email-templates.html).                                                                                                                                                                                                                                  |
   | Manager attributes  | Use the syntax `object.manager.managerAttribute`.Use the attributes available from the email template screen. Learn more in [Email templates](../../tenants/email-templates.html).	If the manager is the certifier type in the Who will Certify section, use the same user attributes in the managerAttribute. For example, if you need to reference a user's manager within the email, then use this object. |
   | Campaign attributes | Use the syntax `object.campaign.campaignAttribute`.Available attributes are `name` and `type`.                                                                                                                                                                                                                                                                                                                |

2. Select any of the notification types:

   | Field                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Send initial notification    | Send a notification any time a certifier is assigned to a line item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | Send reassign notification   | Send to a new certifier when a line item in an access review (campaign) is reassigned or forwarded to them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | Send expiration notification | Send a reminder notification to the certifiers before a campaign expires. Select the number of days, before the campaign expires, to send the reminder.&#xA;&#xA;To illustrate the expiration notification mechanism:&#xA;&#xA;If the notification is set for three days prior to expiration, reviewers will receive an email when the campaign is three days away from the expiration date. If the deadline is extended by a week, the expiration date of the notification will be recalculated and sent three days before the new deadline, regardless of any previously sent notifications. |
   | Send reminders               | Send a notification to remind certifiers to take action on access review (campaign) line items. Select the number of days, weeks, months, or years to send the reminder.                                                                                                                                                                                                                                                                                                                                                                                                                       |
   | Enable escalation            | Send an escalation notification to specific recipients that certifiers have not completed their actions on a campaign. When selected, an additional Escalation Owner box displays. Select the number of days, weeks, months, or years and the user to send the escalation to.                                                                                                                                                                                                                                                                                                                  |

3. Click Next.

   |   |                                                                                                                                                                                                                        |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Identity Governance sends notification emails using an email template. If an email fails to send because of [API rate limits](../../tenants/audit-debug-logs-pull.html#rate-limiting), Identity Governance resends it. |

## Additional options

This optional section allows you to configure other options for a campaign, such as performing bulk certifications or reassigning tasks to another user or group.

To complete this section, do the following:

1. Complete the following optional fields:

   | Field                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   | -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Enable line item reassignment and delegation | Allow the certifier to reassign or forward a line item to another user.When you select this box, you can choose the following options:- Forward - Allow certifiers to forward their access review (campaign) to another certifier. When forwarding an access review, other certifiers are **removed from the access review in its entirety**. Learn more in [forward line items](../end-user/access-review-user-cert-items.html#governance-user-items-cert-forward).

   - Reassign - Select the privileges the current certifier can assign to the new certifier:

     * Add Comment

     * Make Decision

     * Reassign/Forward

     * Sign off

       Learn more in [reassign line items](../end-user/access-review-user-cert-items.html#governance-user-items-cert-reassign). |
   | Require justification on revoke              | Require a mandatory comment or reason for the revocation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   | Require justification on exception           | Require a mandatory comment or reason for any allowed exception.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | Allow exceptions                             | Allow certifiers to continue to certify line items assigned to them **after** the campaign expires. Select a duration in days, months, weeks, or years.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   | Allow bulk-decisions                         | Allow certifiers to make line item decisions in bulk.This includes:- Making a decision (certify, revoke, exception).

   - If Enable line item reassignment and delegation is enabled, then you can bulk Reassign or Forward line items.	As an administrator, most access reviews require an in-depth look on each line item. This is to ensure accuracy of each item. Bulk-decisions allow for a certifier to make a decision on many items at once, which could lead to inaccurate data. Use caution when selecting this option.                                                                                                                                                                                                                                       |
   | Allow partial sign-off                       | Allow a certifier to sign-off on an access review **before** their assigned line items have a decision made on them.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | Process remediation                          | Revokes the end user's access in the target application when a certifier revokes (denies) the line item. Select a workflow to run either immediately after revocation of access or after a duration.	To ensure end-user access is removed when revoking a line item, you must enable this property.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

2. Click Next.

## Customization

This optional section allows you to configure the default table columns for the reviewers.

To complete this section, do the following:

1. Complete the following optional fields:

   | Field       | Description                                                                 |
   | ----------- | --------------------------------------------------------------------------- |
   | Application | Select a value for `application`, such as `Description` and `Name`.         |
   | Entitlement | Select a value for `entitlement`, such as `Description` and `Display Name`. |
   | Review      | Enter `Flags` and `Comments` to add fields to the access review table.      |

2. Click Next.

## Summary

The Summary section is the final section in creating a template. It gives a breakdown of each section in the template, allowing for a review.

Summary steps:

1. Review each section.

2. Click Save to complete the certification template.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Under the What to Certify review section, ensure that the Total Decision Items is greater than 0. If you identify that this is 0, this means that the template did not identify items to be certified. Therefore, if you create the campaign off of the template, the system will immediately cancel the campaign. If you identify this to be 0, go back to the What to Certify section and adjust your settings. |

---

---
title: Create a workflow event
description: Create event-triggered custom workflows that execute when governance events are detected
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/event-workflow-editor
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/event-workflow-editor.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["workflow event", "create event", "event trigger", "event action", "custom workflow"]
section_ids:
  workflow-event-new: Create a new workflow event
  workflow-event-trigger: Event trigger
  workflow-event-action: Event action
  workflow-event-details: Event details
  workflow-details: Workflow details
  workflow-event-summary: Summary
---

# Create a workflow event

The Advanced Identity Cloud admin console provides simple steps to set up a workflow event using the campaign template format.

The following table lists the sections that you must follow to set up a workflow event template.

| Section                                            | Description                                     |
| -------------------------------------------------- | ----------------------------------------------- |
| [Create a new workflow event](#workflow-event-new) | Create a new workflow event.                    |
| [Event trigger](#workflow-event-trigger)           | Type of event trigger.                          |
| [Event action](#workflow-event-action)             | Type of action to take when the trigger occurs. |
| [Event details](#workflow-event-details)           | General event details of the template.          |
| [Summary](#workflow-event-summary)                 | Summary of your selected sections.              |

## Create a new workflow event

1. In the Advanced Identity Cloud admin console, click Governance > Events.

2. On the Governance Events page, click [icon: add, set=material, size=inline] New Event. The New Event modal appears.

### Event trigger

This section sets the type of event trigger for your workflow.

1. In the New Event modal, select an event trigger:

   * User created: Trigger an action when a user is created.

   * User updated: Trigger an action when a user is updated.

2. Click Next.

### Event action

This section sets the type of action for your workflow when the event is triggered.

1. In the New Event modal, review the event actions, and click Workflow:

   * Certification. Trigger a certification campaign when an event occurs.

   * Workflow. Trigger a workflow when an event occurs.

2. Click Next.

### Event details

* In the Event Details modal, complete the following fields, and click Next.

  | Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Event Name        | Display name for the event.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  | Event Description | (Optional) Enter a general description for the event. Your company should follow a descriptive convention to describe each of your events.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | Event Owners      | Enter the owner(s) of the event. Only owners can fully control their events, including event decisions, event assignment changes, sign off, and more.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | Trigger for       | Determine the users for which to apply the trigger. Options are:- All users: Trigger for all users in your system.

  - A subset of users: Trigger for a subset of users in your system. This option opens a filter to set up your users.

    > **Collapse: Event filter**
    >
    > ![governance event filter](../_images/governance-event-filter.png)
    >
    > * 1 Trigger if `All` or `Any` conditions are met.
    >
    > * 2 Previous value of
    >
    >   * `Previous value of` (appears for `User created` triggers)
    >
    >   * `Current value of` (appears for `User created` triggers)
    >
    >   * `Before` (appears for `User updated` triggers)
    >
    >   * `After` (appears for `User updated` triggers)
    >
    > * 3 Type to search: Select an attribute from the list.
    >
    > * 4 Conditions:
    >
    >   * Contains
    >
    >   * Does not contain
    >
    >   * Is
    >
    >   * Is not
    >
    >   * Is present
    >
    >   * Is not present
    >
    >   * Starts with
    >
    >   * Does not start with
    >
    >   * GTE
    >
    >   * GT
    >
    >   * LTE
    >
    >   * LT
    >
    > * 5 Enter a value for your filtered condition.
    >
    > * 6 Click [icon: plus, set=fa]to add the condition.
    >
    > * 7 Click Advanced Editor. |

### Workflow details

This section sets the details for your workflow when the event is triggered.

* In the New Workflow Event modal, complete the following fields, and click Next.

  | Field              | Description                                                                                                                         |
  | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------- |
  | Workflow           | Select the workflow from the list.                                                                                                  |
  | Workflow Variables | (Optional) Specify variables to pass to the event, and its value. Click [icon: add, set=material, size=inline] to add the variable. |

### Summary

The Summary section is the final section in creating a template. It gives a breakdown of each section in the template, allowing for a review.

Summary steps:

1. Review each section.

2. Click Save to complete the template. Your event appears on the Events page.

---

---
title: Create an application request form
description: Create an application request form linked to specific applications for collecting user access requests
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/governance-forms-app-request
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-forms-app-request.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["forms", "application request form", "create form", "custom form", "access request"]
section_ids:
  key_points: Key points
  steps: Steps
  end_user_steps: End user steps
---

# Create an application request form

The Identity Governance Forms provides an easy-to-use interface to create an application request form.

## Key points

The Form creator must consider the following key points:

* You can only link an application to a single form. While a form can be used with multiple applications, each application can only be associated with one form at a time.

* The typical use case is to create a form that aligns with the application's account object type schema.

* In a workflow, you can assign a form in the Approval node. For typical cases, you can select Dynamic form selection, which uses the form associated with the application.

  ![Approval node with dynamic form selection](../_images/governance-forms-dynamic-selection.png)

- For more customization, you can define the keys exactly as you want. Once a request is generated, the form's contents are copied into the request, making those properties available for use within the workflow to provision access as needed. For example, you can define a key with a value of `custom.NAME`. When a user submits a request, the key appears in `request.custom.NAME` with the value, Testing:

  ```json
  {
    "id": "409f28fc-65f6-41b8-a9f5-bb3a64f55925",
    "requester": {
      "givenName": "Frank",
      "id": "managed/user/c51d9ee1-43b3-49d1-8742-cbb33842a5cc",
      "mail": "frank.york@example.com",
      "sn": "York",
      "userName": "fyork",
      "isAdmin": false
    },
    "requestType": "applicationGrant",
    "request": {
      "common": {
        "priority": "low",
        "justification": "Testing",
        "applicationId": "d248cc89-79b2-4f6a-98bc-46d0a938318f",
        "userId": "f3617664-4dd2-48eb-bdae-512f45b157df",
        "isDraft": false,
        "context": {
          "type": "request"
        }
      },
      "custom": {
        "NAME": "Testing"
      },
      "_rev": 1
    }
    .....
  }
  ```

## Steps

Governance or tenant administrators can carry out the following steps to create a new application request form:

1. In the Advanced Identity Cloud end-user UI, click Forms > [icon: add, set=material, size=inline] New Form.

2. In the New Form modal, click Application request form, and then click Next.

3. In the modal, enter the following and click Save when completed:

   | Field                  | Description                                                                                                        |
   | ---------------------- | ------------------------------------------------------------------------------------------------------------------ |
   | Form Name              | Enter a descriptive name for your form. Follow any convention established by your company.                         |
   | Description (optional) | Enter a general description for the form.                                                                          |
   | Application            | Select application to associate the form to.&#xA;&#xA;You can only link one form to an application or object type. |
   | Object type            | Select an option:- User

   - Group

   - Directory Role

   - Service Plan                                                 |

4. In the Forms editor, drag-and-drop [forms fields](governance-forms-fields.html) onto the canvas and fill in the fields in the right pane.

5. In a workflow, you can assign a form in the Approval node properties pane. For typical cases, you can select Dynamic form selection, which uses the form you associated with the application.

6. Click Preview to see the form you created.

7. Click Save when complete. Your form appears on the Forms page.

## End user steps

Administrators can test the new custom request form by logging in to an end-user account.

1. In the Advanced Identity Cloud end-user UI, the end user logs in and clicks My Requests.

2. On the My Requests page, click [icon: add, set=material, size=inline] New Request.

3. In the New Request modal, click Next.

4. On the Access Catalog page, click [icon: add, set=material, size=inline] Request for an application.

   ![Application access catalog](../_images/application-request-access-catalog.png)

5. In the Request Application Access modal, review the application details and click Add to Request.

6. In the Request Application Access modal, fill out the form associated with the application, and then click Add to Request.

   ![Application request form associated with the app](../_images/application-request-form.png)