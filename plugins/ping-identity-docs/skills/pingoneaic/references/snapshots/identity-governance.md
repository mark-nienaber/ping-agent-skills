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

   2. In the Internal role Permissions modal, select Alpha realm - Users managed/alpha_user, and click [icon: add, set=material, size=inline] Add.

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
title: Access graph
description: View the access graph to visualize connections between users and their roles, applications, or entitlements.
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/view-access-graph
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/view-access-graph.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Governance", "user", "access", "graph", "identity", "governance"]
page_aliases: ["release-notes:rapid-channel/view-access-graph.adoc"]
section_ids:
  view_user_access: View user access
  access_graph_filters_and_details: Access graph filters and details
---

# Access graph

The access graph provides a read-only view of a user's access at any time. Use it to understand what a user can do before approving or revoking access in a certification campaign (a scheduled review where you assess access rights).

|   |                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------- |
|   | The access graph is a feature of the Identity Governance add-on capability for Advanced Identity Cloud. |

## View user access

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. Search for and select a user.

3. On the user's Details tab, click View User Access.

   The access graph opens, showing the user's connections to their roles, applications, and entitlements.

   ![User access graph showing relationships between a user, roles, applications, and entitlements with filter controls.](../_images/governance-view-access-graph-button.png)![The access graph displays the connections between a user's roles, applications, and entitlements.](../_images/governance-view-access-graph.png)

## Access graph filters and details

After the access graph opens, use the sidebar to narrow the view and click items in the graph to explore their details:

* By access type: Roles, applications, or entitlements.

* By certification status: Filter the graph by whether items have been reviewed in a certification campaign. Certified items have been reviewed and approved. Uncertified items haven't yet been reviewed.

* By role type: Direct roles (assigned explicitly to the user) or conditional roles (assigned based on criteria such as group membership).

When you click a role, application, or entitlement on the graph, its details appear in the right pane.

For example, clicking an account under Application expands the graph to show the account's entitlements as connected items, and the account details appear in the right pane.

![Access graph sidebar with filters for certification status, direct or conditional roles, applications, and entitlements.](../_images/governance-access-graph-details.png)

---

---
title: Access Modeling
description: Overview of Access Modeling, which uses role mining to discover candidate roles in your PingOne Identity Governance environment
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/access-modeling-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/access-modeling-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-28
keywords: ["access modeling", "role mining", "candidate roles", "confidence scoring", "configure access modeling", "run a role mining job", "review and publish roles", "PingOne Identity Governance", "IGA"]
section_ids:
  how_access_modeling_works: How Access Modeling works
---

# Access Modeling

Access Modeling, also known as role mining, analyzes existing access patterns to help optimize user-to-entitlement assignments. Identity Governance uses machine learning and analytics to propose candidate roles for review and publication by role owners.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | PingOne Identity Governance add-on capabilityAccess Modeling is an additional add-on capability for PingOne Identity Governance. Contact your Ping Identity representative if you want to add the Access Modeling (Role Mining) add-on SKU to your PingOne Advanced Identity Cloud Identity Governance subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

## How Access Modeling works

The Access Modeling workflow involves the following participants:

1. An administrator [configures Access Modeling](iga-access-modeling-admin.html), activates governance lifecycle management (the machine learning model that powers role mining), sets confidence thresholds, and creates the `access-modeling-administrator` group.

2. The administrator assigns one or more end users to the `access-modeling-administrator` group.

3. An authorized end user (a member of the `access-modeling-administrator` group) [runs a role mining job](../end-user/iga-access-modeling-end-user.html#run-a-role-mining-job). Identity Governance analyzes the latest access data and generates candidate roles.

4. A role owner and an approver [review and publish roles](../end-user/iga-access-modeling-end-user.html#create-drafts-and-publish-roles). The role owner refines a candidate into a draft, and an approver publishes the draft as an active role in Identity Governance.

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
title: Activity collectors
description: Understand what users, agents, and non-human identities are doing with their access by using activity collectors to aggregate and load logs into Identity Governance.
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/governance-activity-collectors
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-activity-collectors.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["activity collectors", "activity log", "access logs", "audit events", "cloud logs", "non-human identity", "shadow access"]
section_ids:
  activity-log: Activity log
  available-collectors: Available collectors
  custom-collectors: Custom collectors
  viewing-activity-data: Viewing activity data
  data-retention: Data retention
---

# Activity collectors

Activity collectors help you understand what users, agents, and non-human identities are doing with the access they have. These collectors aggregate access logs, audit events, system logs, and cloud logs, and load them into Identity Governance. They enable you to map system activity to user identities and identify abnormal activity, compliance violations, and shadow access, which exists in source systems but isn't tracked by your Identity Governance system.

## Activity log

The activity log is a standardized record that contains fields for authentication events and activity associated with agents, service accounts, other non-human identities, and access. It also has extension attributes that you can use to accommodate custom events.

The schema of the activity log is versioned to support backward compatibility. If you write custom field maps or integrations that rely on specific attributes, verify the schema version before loading data.

Three identifiers are relevant to activity log events:

* `id`: The unique event ID

* `actor_global_id`: The identity, such as a non-human identity, workload, human, or agent

* `actor_id`: The actor's local identifier within Identity Governance

Identity Governance correlates activity events from a source system based on `actor_global_id` and `actor_id`.

## Available collectors

Activity collectors pull logs from the source systems where your identities operate. Identity Governance provides the following collectors:

* AWS

* Azure

* Entra

* Google Cloud

* Google Workspace

* Salesforce

* JDBC

* Windows

Each collector consists of:

* Collector configuration: A `.json` file containing connectivity and other configuration parameters

* Field map: A `.json` file that maps the raw field names from the source system to the standard activity log attributes in Identity Governance

Learn more about deploying and using the collectors in the `README.md` file by downloading the [IGA Collectors Zip](../_attachments/iga-collectors.zip).

## Custom collectors

Use the activity collector toolkit, a Python-based tool that loads activity data and helps you build new collectors. You can create these additional collectors to read raw logs, transform them into a format that Identity Governance can ingest, and load the data with the toolkit.

If you don't want to use the toolkit, use the REST API instead. Learn more in [Identity Governance REST API reference](../rest-api/endpoints/rest-iga.html).

## Viewing activity data

After activity collectors load data into Identity Governance, you can review the activity log for individual accounts and AI Agents to investigate access events, detect anomalies, and confirm compliance.

To view activity data, go to the Accounts or AI Agents on the Advanced Identity Cloud admin console.

|   |                                                                                                                                         |
| - | --------------------------------------------------------------------------------------------------------------------------------------- |
|   | Viewing AI agent activity data requires the Agent Governance add-on capability. Contact your Ping Identity representative to enable it. |

## Data retention

Activity data is retained for at least 13 months. You can choose to purge and reload data at any time.

---

---
title: Administer Access Modeling
description: Administer PingOne Identity Governance access modeling, including role mining, confidence scoring, and role lifecycle management
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/iga-access-modeling-admin
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/iga-access-modeling-admin.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-28
keywords: ["access modeling", "role mining", "confidence scores", "role candidates", "role states", "role administrator", "role owner", "thresholds", "governance LCM"]
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

# Administer Access Modeling

Access Modeling (also known as *role mining*) analyzes existing user-to-entitlement assignments and discovers candidate access roles describing how people use access in your environment. It uses advanced machine learning algorithms and analytics thresholds to:

* Examine current roles and entitlements across your access landscape.

* Propose new role candidates and changes to existing roles.

* Calculate confidence scores and driving factors for each role and entitlement assignment.

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
title: Administrator tasks
description: Learn how to manage identity governance tasks, including accounts, access, certification campaigns, lifecycle management, recommendations, reports, and APIs
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/administator-tasks-preface
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/administator-tasks-preface.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-25
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

[icon: plug, set=fas, size=3x]

#### [Unmanaged apps](unmanaged-apps.html)

Learn how to onboard disconnected applications.

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

Learn about notifications.

[icon: thumbs-up, set=fad, size=3x]

#### [Recommendations](governance-recommendations-preface.html)

Learn about governance recommendations.

[icon: file-chart-column, set=fad, size=3x]

#### [Reports](iga-reports.html)

Learn about governance reports.

[icon: user-ninja, set=fas, size=3x]

#### [Agent Governance](iga-agent-governance.html)

Learn about Agent Governance.

[icon: cogs, set=fas, size=3x]

#### [Activity collectors](governance-activity-collectors.html)

Learn about activity collectors.

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
  run-reconciliation: Run reconciliation
  deploy-the-platform-specific-inventory-collector: Deploy the platform-specific inventory collector
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

* **Discover AI agents across all platforms and onboard them as first-class identities**: Agent Governance includes out-of-the-box connectors for major agent platforms such as Microsoft Copilot, Azure AI Foundry, AWS Bedrock, and Google Vertex AI. It automatically discovers and onboards AI agents into your Identity Governance framework with minimal setup. Once onboarded, agents receive the same identity attributes, lifecycle management, and governance controls as human users and accounts.

* **Discover the full anatomy of each agent using deep discovery**: Beyond the agent identity itself, Agent Governance discovers and catalogs the resources each agent uses to perform its work, including:

  * **Tools**: APIs and services the agent can invoke.

  * **Knowledge bases**: Data sources the agent queries.

  * **Guardrails**: Policies that limit agent behavior.

  * **Credentials**: API keys and access tokens the agent uses to authenticate. This is a key risk surface to monitor.

  * **Bindings**: Which users or systems can invoke this agent.

  * **Sub-agents**: Other agents this agent can delegate work to.

    This **deep discovery** approach goes beyond basic profile metadata (name, version, platform, owner) that other vendors provide, giving you full visibility into what each agent can do. It also scans your infrastructure to identify disconnected apps running outside your governance framework and detect "shadow agents" operating without proper oversight.

* **Assign one or more human custodians to each agent to provide oversight**: Every agent needs accountability. You can designate one or more human custodians responsible for overseeing the agent's behavior, approving access requests, and ensuring the agent operates within your organization's policies. Custodians can review agent activity, modify permissions, and act as the point of contact for governance decisions related to that agent.

* **Monitor agent activity with normalized logs from multiple sources**: Agent Governance ingests and normalizes activity logs from multiple sources, giving you visibility into what your agents are doing. The normalized activity schema classifies logs by actor type, so you can monitor agent behavior, detect unmanaged agents operating without oversight, and identify anomalies.

  The Activity page shows you when agents execute actions, what resources they access, and whether those actions were approved or autonomous. You can investigate suspicious behavior and maintain a complete audit trail of agent operations.

* **Apply comprehensive governance including access requests and workflows, and access certifications**: Agents inherit all the governance capabilities you already use for human identities. You can require approval workflows before agents receive access to sensitive resources, run periodic access certifications to review and validate agent permissions, ensuring agents operate under the same security and compliance standards as your workforce.

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

        ![Identity type configuration page showing the custom_iga_identity_type property with two enumerated values: Agent and Human](../_images/agent-governance-identity-type.png)

4. On the Identity Type (String) (`custom_iga_identity_type`) page, set the following properties, and then click Save:

   1. Click Property Value, and then click Enumerate allowable values for this property. Enumerating values restricts this property to "Agent" or "Human," preventing inconsistent values.

   2. In the Label field, enter `Agent`, and in the Value field, enter `Agent`. Click [icon: add, set=material, size=inline] to add this value to the list of allowed values.

   3. In the Label field, enter `Human`, and in the Value field, enter `Human`. Click [icon: add, set=material, size=inline] to add this value to the list of allowed values.

      ![Screenshot showing enumerated values for custom_iga_identity_type: Agent and Human.](../_images/agent-governance-identity-type-property-value.png)

5. Click Display, check that the following properties are set, and update them if necessary:

   * Show in Admin List View: Select this checkbox to include this property as a column in internal admin lists and tables.

   * Show in Admin Form: Select this checkbox to display this property in forms used by admins to view or update records.

   * Show in User-facing Form: Select this checkbox to allow end users to edit this property in the self-service UI. When deselected, this property remains visible to end users in read-only mode.

6. Click Save.

### Set up an application for your AI agent platform

Before you can onboard AI agents, set up one of the following applications:

1. In the Advanced Identity Cloud admin console, go to Applications > Applications > Browse App Catalog.

   * [AWS Bedrock](../../app-management/applications-agent-governance/aws-bedrock.html)

   * [AWS Bedrock AgentCore](../../app-management/applications-agent-governance/aws-bedrock-agentcore.html)

   * [Azure AI Foundry](../../app-management/applications-agent-governance/azure-ai-foundry.html)

   * [Google Vertex AI](../../app-management/applications-agent-governance/google-vertex-ai.html)

   * [Microsoft Copilot Studio](../../app-management/applications-agent-governance/microsoft-copilot-studio.html)

### Onboard AI agents

To onboard Ai agents, configure your application by mapping agent properties to identity fields.

#### Configure connected tools as entitlements

1. In the Advanced Identity Cloud admin console, go to Applications > Applications.

2. Click the application you just registered to open the application details page.

3. Click the Provisioning tab, choose one of the following options based on the message displayed:

4. On the AI application page, select Account to map agent properties to identity fields in Advanced Identity Cloud.

5. Click the Properties tab, and review the agent's properties.

   1. Search for the Connected Tools property. Click the ellipsis icon ([icon: more_horiz, set=material, size=inline]) for this property, and then click Edit.

   2. In the Edit Property modal, click Entitlement to specify that this property contains entitlements.

      ![Edit property modal with the entitlement option highlighted.](../_images/agent-governance-edit-property.png)

   3. Click Save.

#### Configure synchronization mappings

Synchronization mappings tell Identity Governance which agent properties from your source platform (such as agent name or ID) should be stored in which user fields in Advanced Identity Cloud.

1. In the Advanced Identity Cloud admin console, go to Applications > Applications, browse the app catalog, and select your AI Agent.

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

   3. In the userName (string) property modal, select the agent's property. For example, select `source.__NAME__`, and then click Save.

      |   |                                                                                                                                                                                                                                                   |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | Some properties require hardcoded values (static text that applies to all synced agents). For example, `custom_iga_identity_type` should always be `"Agent"`. For these, click Apply transformation script, enter the value, and then click Save. |

   4. Repeat the previous steps to add more property mappings.

      | Ping Identity property   | Agent property                     | Notes                                             |
      | ------------------------ | ---------------------------------- | ------------------------------------------------- |
      | userName                 | `source.__NAME__`                  | Unique identifier for the agent                   |
      | custom_iga_identity_type | `"Agent"`                          | Hardcoded value to flag this as an agent identity |
      | givenName                | `source.agentName`                 | Agent's display name                              |
      | sn                       | `"Bedrock"`                        | Last name—customize to your platform name         |
      | mail                     | source.agentId+"@pingidentity.com" | Synthetic email—adjust domain as needed           |

#### Define correlation rules

Correlation rules tell Identity Governance how to match agent accounts from your source platform (like AWS Bedrock) to identities that may already exist in Advanced Identity Cloud. Without these rules, the system might create duplicate identities when you import agents, resulting in confusion and governance gaps.

1. In the Advanced Identity Cloud admin console, go to Applications > Applications, select your AI Agent application, and click the Provisioning tab.

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

#### Deploy the platform-specific inventory collector

After agents are onboarded, deploy the platform-specific inventory collector to enable deep discovery of agent tools and capabilities.

Contact your Custom Success Outcome Manager or Ping Identity representative to obtain the inventory collector package and runbook.

|   |                                                                                                                                                                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Don't skip this step. Without deploying the inventory collector, Agent Governance only imports basic profile information about your agents (name, ID, owner) but doesn't discover the tools they use, their permissions, or their activity. This limits your visibility and governance capabilities. |

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

   * custom_iga_identity_type: Select agent identity type, select `is`, and then enter `Human`. This scope only applies to identities flagged as human users.

     ![Scope applies to configuration showing a filter for identities with the custom_iga_identity_type property equal to Human](../_images/agent-governance-scope-applies-to.png)

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
title: Audit logs
description: View, filter, and export governance and identity activity audit events
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/governance-audit-log
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/governance-audit-log.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-08-26
keywords: ["audit log", "audit events", "governance events", "identity activity", "event filtering", "audit export"]
section_ids:
  view-audit-events: View audit events
  view-a-user-profile-audit-events: View a user's audit events
  filter-audit-events: Filter audit events
  view-daily-activity-counts: View daily activity counts
  view-event-details: View event details
  paginate-audit-events: Paginate audit events
  export-audit-events: Export audit events
---

# Audit logs

The audit logs provide a centralized view of governance events and selected identity activity in your tenant. For example, use the audit log to confirm when a role changed or investigate an unexpected account update. You can review events, filter the results, view daily activity counts, and export the results. You can also view event details and move between pages.

The audit log includes governance events and the following identity activity:

* User creation, updates, and deletion

* Role creation, updates, and deletion

* Account creation, updates, and deletion after you use the account API

## View audit events

Use this task when you need to review governance and identity activity.

1. In the Advanced Identity Cloud admin console, go to Governance > Audit.

2. Review the audit events in the table. An actor is the user, administrator, or system that performed an event. The table displays information about each event, including the event timestamp, actor, event type, and display name.

3. In the Event Activity dashboard, hover over a specific day to see the number of events recorded on that day.

   ![Identity Governance audit log page.](../_images/governance-audit-logs.png)

### View a user's audit events

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users, and click on a username.

3. Click Audit.

   The audit events include events where the user is the actor or the target. You can review the event details and use the available pagination controls to view additional events.

## Filter audit events

Use filters when you need to narrow the audit log to a specific date range, event type, or actor. After you apply the filters, the table displays only matching events.

1. On the Audit Log page, set the date range for the events that you want to view.

2. In the Event Type list, select the event type to display.

3. In the Actor field, select or enter the actor whose events you want to view. Available options are:

   * All Actors

   * User

   * Admin

   * System

4. Review the filtered events in the table.

To remove the filters, clear the filter values or reset the filters.

## View daily activity counts

On the Audit Log page, view the Event Activity dashboard. The dashboard displays the number of events recorded for each day in a seven-day period.

Hover over a day to see its date and event count. Select a day to review the events recorded on that day.

## View event details

View an event's details when you need to understand the changes it records. The details page displays the changes associated with the selected event.

1. On the Audit Log page, find the event that you want to review.

2. Click the Ellipsis icon ([icon: more_horiz, set=material, size=inline]), and click View Details for a specific audit log.

3. Review the changes associated with the event.

   ![Identity Governance audit log details page displaying element changes before and after and the raw event JSON.](../_images/governance-audit-logs-details.png)

## Paginate audit events

The audit log displays a limited number of events on each page.

Use the pagination controls at the bottom of the table to move between pages. The table displays the events on the selected page.

## Export audit events

Export events when you need to retain or share audit records, or analyze them outside the product. You can export the events that the audit log displays to an `.xlsx` spreadsheet or a `.pdf` file.

1. On the Audit Log page, apply any filters that you want to include in the export.

2. Select XLSX or PDF.

   The export contains the audit events that match the current filter criteria.

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
revdate: 2026-08-31
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

1. In the Advanced Identity Cloud admin console, go to the Governance > Certification > Templates tab.

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

1. From the Advanced Identity Cloud admin console, go to Certification > Templates tab.

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

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You can't undo the deletion of a certification template.If the template has been used to create campaigns, a warning indicates that campaigns are based on the template. You can override the warning and delete the template. |

To delete a template:

1. From the Advanced Identity Cloud admin console, go to Certification > Templates tab.

2. Locate the template.

3. Click [icon: more_horiz, set=material, size=inline], and then click Delete.

4. If the template has been used to create campaigns, a warning indicates that campaigns are based on the template. Review the warning and confirm that you want to override the warning and delete the template. If the template hasn't been used, confirm that you want to delete the template.

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
title: Configure entitlement lifecycle management
description: Enable delegated entitlement management for application and entitlement owners to manage permissions
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/lcm-entitlement
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/lcm-entitlement.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["entitlement lifecycle management", "entitlement management", "delegated administration", "create entitlement", "modify entitlement", "scopes", "workflows"]
section_ids:
  governance_personas: Governance personas
  enable_entitlement_management: Enable entitlement management
  configure_entitlement_workflows: Configure entitlement workflows
  troubleshooting_entitlements: Troubleshooting entitlements
---

# Configure entitlement lifecycle management

Identity Governance provides a type of delegated administration, allowing application owners, entitlement owners, and end users authorized with the proper scope permissions to manage entitlements within the applications available to them. By using this feature, companies can keep entitlement attributes up-to-date, reducing the risk of outdated or inaccurate entitlements impacting decision making.

Manage entitlements also enforces policies by requiring approval workflows before any entitlement changes are applied. This prevents users from granting excessive permissions without oversight and ensures access remains aligned with organizational policies.

## Governance personas

By default, governance administrators, application owners, entitlement owners, and end users with scoped permissions can manage entitlements in the system. These users have the following permissions:

| Action                          | Admin                    | Application Owner        | Entitlement Owner        | End user  |
| ------------------------------- | ------------------------ | ------------------------ | ------------------------ | --------- |
| View entitlement                | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |
| View users who have entitlement | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |
| Create entitlement              | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: times, set=fa]No  | If scoped |
| Modify entitlement              | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |

## Enable entitlement management

Governance administrators must enable entitlement management to activate the feature for their users. The entitlement management functionality is also known as entitlement lifecycle management (entitlement LCM).

1. In the Advanced Identity Cloud admin console, go to Governance > Requests.

2. On the Requests page, click the Settings tab.

3. In the Governance LCM section, click Activate.

4. In the Governance LCM modal, read what activating this feature entails, and click Next.

5. In the Governance LCM modal, click Entitlement LCM, and then click Activate. The manage entitlement feature is now active on your tenant.

   ![Enable the manage access feature on the requests page.](../_images/governance-lcm-enable.png)

## Configure entitlement workflows

Identity Governance provides the out-of-the-box request types and workflows to enable authorized users to carry out entitlement tasks:

| Request Type      | Workflow           |
| ----------------- | ------------------ |
| createEntitlement | Create Entitlement |
| modifyEntitlement | Modify Entitlement |

As with all other Identity Governance requests, the entitlement management actions are defined and processed in request workflows that allow users to:

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
title: Configure role lifecycle management
description: Configure role LCM to delegate role management to end users with governance controls
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/lcm-role
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/lcm-role.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  personas: Personas
  activate_role_lcm: Activate role LCM
  create_a_scope_to_define_which_roles_a_delegated_end_user_can_manage: Create a scope to define which roles a delegated end user can manage
  role_scope_permissions: Role scope permissions
  create_a_scope_for_role_lcm: Create a scope for role LCM
  create_an_internal_role_that_grants_the_delegated_end_user_capability: Create an internal role that grants the delegated end user capability
  assign_end_users_to_the_internal_role: Assign end users to the internal role
  test_role_lcm: Test role LCM
---

# Configure role lifecycle management

Role lifecycle management (role LCM) lets authorized end users create, update, delete, and view role information. It also enforces policies by requiring approval workflows before the system applies any role changes. This prevents users from granting excessive permissions without oversight and ensures access remains aligned with organizational policies.

As a tenant administrator or governance administrator, you must configure and enable role lifecycle management (role LCM) before delegated end users can manage roles.

|   |                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Role LCM doesn't support custom forms. You must use the default forms provided with the feature.

* Role LCM automatically seeds request types and workflows for create role, modify role, and delete role. |

## Personas

Role LCM involves the following personas:

**Role LCM personas**

| Persona       | Description                                                                                                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Administrator | A tenant administrator or an internal administrator, such as a configured OAuth 2.0 client.                                                                                                   |
| Role owner    | A user listed as the owner of a role in Advanced Identity Cloud.                                                                                                                              |
| End user      | An end user that's an application owner or an entitlement owner. They might also receive permissions directly from Identity Governance scopes or have no additional role-related permissions. |

## Activate role LCM

Administrators must enable role LCM to activate the feature in the hosted account pages.

1. In the Advanced Identity Cloud admin console, go to Governance > Requests, and click the Settings tab.

2. In the Governance LCM section, click Ellipsis ([icon: more_horiz, set=material, size=inline]), and then click Settings.

3. In the Governance LCM modal, read the note stating that this feature adds request and approval flows for selected identity profiles and removes direct create, update, and delete capabilities, and then click Next.

   ![Governance LCM modal showing introductory information about the feature with a Next button to proceed.](../_images/governance-lcm-modal-about.png)

4. In the Governance LCM modal, click Role LCM, and then click Activate.

   ![Governance LCM modal with Role LCM option displayed and an Activate button to enable the feature.](../_images/governance-lcm-modal-roles.png)

   The role LCM feature is now enabled.

## Create a scope to define which roles a delegated end user can manage

Create one or more scopes to define who can manage roles and what data they can access. Scopes let you control visibility and permissions for roles, role members, and assigned entitlements so you can delegate role management to the right administrators.

|   |                                                                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To use role LCM, a delegated end user must both match a role-management scope **and** be assigned an internal role that grants access to the Roles object. |

### Role scope permissions

Scopes control what roles a user can see and manage. They define boundaries for role lifecycle operations based on role attributes, such as which applications or entitlements the role includes. When you assign a scope to a user, that scope determines whether they can view, create, modify, or delete specific roles.

By default, administrators, role owners, and end users have the following scope permissions:

| Action      | Admin                    | Role owner               | End user  |
| ----------- | ------------------------ | ------------------------ | --------- |
| View role   | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |
| Create role | [icon: check, set=fa]Yes | If scoped                | If scoped |
| Modify role | [icon: check, set=fa]Yes | If scoped                | If scoped |
| Delete role | [icon: check, set=fa]Yes | If scoped                | If scoped |

Example: Combined role owner and end user permissions

Sarah owns the Marketing role. As an end user, she also has a scope that lets her manage roles that match a filter for CRM entitlements.

Together, these permissions let Sarah:

* View and edit the Marketing role through role ownership.

* View and edit any role that matches the CRM-entitlement filter through her end-user scope.

* Create roles that match the CRM-entitlement filter through her end-user scope.

* Delete roles that match the CRM-entitlement filter through her end-user scope.

Because Sarah is the Marketing role owner and also has a scope that applies to roles matching the CRM-entitlement filter, she can still edit the Marketing role after it includes CRM entitlements.

### Create a scope for role LCM

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. Go to Governance > Scopes, and click [icon: add, set=material, size=inline] New Scopes.

3. On the New Scope page, enter the following on the Details page:

   1. Name: Enter a descriptive name for the scope. The name should be descriptive enough to easily identify the purpose of the scope. For example, enter Scope for role LCM for contractors if you want to assign an employee to manage roles for contractors.

   2. Description: Enter a description for the scope. For example, enter `This internal scope allows managing roles for contractors`.

   3. Click Next.

      ![The New Scope page showing the Details tab with Name field containing 'Role LCM scope for contractors', Description field with explanatory text, and a Next button at the bottom.](../_images/governance-role-lcm-scope-details.png)

4. On the Applies to page, define which users should be subject to this scope.

   1. Select if the All or Any condition must be met.

   2. Select a property for this scoping rule. For example, select description.

   3. Select an operator for the scoping rule. For example, select contains.

   4. Enter a condition. For example, enter Default Approvers.

   5. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

   6. Click Next.

      ![The New Scope page showing the Applies to tab with condition builder containing All/Any selector, property list set to 'description', operator list set to 'contains', and value field with 'Default Approvers', plus a Next button.](../_images/governance-role-lcm-scope-appliesto.png)

5. On the Access page, click Roles.

   1. Select the All Roles or Roles matching a filter if this scope applies to all configured roles, or select Roles matching a filter to define the conditions under which this scope applies.

   2. If you selected Roles matching a filter, select if All or Any conditions must be met.

      1. Select a property for this scoping rule.

      2. Select an operator for the scoping rule.

      3. Enter a condition.

      4. If you want to add another rule, click [icon: add, set=material, size=inline] and repeat the steps.

   3. Select the permissions available to the scope:

      * Create Roles: Permission to create a new role.

      * Modify Role: Permission to modify a role.

      * Publish Roles: Permission to publish a role.

      * Delete Role: Permission to delete a role.

   4. Click Save.

      ![The New Scope page showing the Access tab with Roles selected and four permission checkboxes: Create Roles, Modify Role, Publish Roles, and Delete Role, plus a Save button.](../_images/governance-role-lcm-scope-access.png)

## Create an internal role that grants the delegated end user capability

Administrators must create an internal role, so that authorized end users can view the Roles object.

1. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

2. Go to Identities > Manage.

3. Click Internal Roles > [icon: add, set=material, size=inline] New Internal Role.

4. In the New Internal Role modal, enter the following and click Next.

   * Name: Enter a name for the internal role, such as Role LCM.

   * Description: Enter a description for the internal role.

     ![New Internal Role modal with Name field containing 'Role LCM' and Description field for entering role description, and a Next button.](../_images/governance-role-lcm-internal-role-new.png)

5. In the Internal role Permissions modal, select Alpha realm - Roles, and click [icon: add, set=material, size=inline] Add.

   ![Internal role Permissions modal showing a selectable list with 'Alpha realm - Roles' option and an Add button.](../_images/governance-role-lcm-internal-role-permissions.png)

6. Select the internal role permissions you want available with the role:

   * View: Allows viewing role information.

   * Create: Allows creating new roles.

   * Update: Allows updating existing roles.

   * Delete: Allows deleting roles.

     ![Permission configuration showing four checkboxes: View for viewing role information, Create for creating new roles, Update for updating existing roles, and Delete for deleting roles.](../_images/governance-role-lcm-internal-role-permissions-add.png)

7. Click Show advanced. Click set all attributes and select Read/Write for the attribute permissions.

   * Name

   * Description

   * Members

   * assignments

   * applications

   * condition

   * temporalConstraints

     |   |                                                                                                                                    |
     | - | ---------------------------------------------------------------------------------------------------------------------------------- |
     |   | Click Administer only a subset of Alpha realm - Roles by applying a filter to access a subset of roles based on specific criteria. |

8. Click Next.

9. In the Dynamic Internal role Assignment modal, click A conditional filter for this role if you want to set a conditional role assignment. Otherwise, click Next.

   ![Dynamic Internal role Assignment modal with option to select 'A conditional filter for this role' and Next button to continue or skip.](../_images/governance-role-lcm-internal-role-assignment.png)

10. In the Time Constraint modal, click Set a start and end date during which this role will be active if you want to assign the role on a temporary basis. Otherwise, click Save to finish creating the internal role.

    ![Time Constraint modal with option to 'Set a start and end date during which this role will be active', with Save button to complete or continue without time constraint.](../_images/governance-role-lcm-internal-role-time-constraint.png)

## Assign end users to the internal role

Associate the scope to the assigned end users to limit their authority to the intended roles.

1. On the Role LCM page, click [icon: add, set=material, size=inline] Add Members.

2. In the Add Members modal, select the users to which the internal role applies, and then click Save.

   ![Add Members modal showing a list of users with checkboxes for selection and a Save button to add selected users to the role.](../_images/governance-role-lcm-internal-role-add-members.png)

## Test role LCM

After you enable role LCM, test the feature to ensure it's working as expected before delegating role management to end users.

1. Sign on as a test user that's a role LCM administrator.

2. Go to Administer > Roles.

3. Click [icon: add, set=material, size=inline] New Role.

4. In the New role modal, fill out the form for the new role, and then click Save.

5. Click View request to see the details of the change request you just submitted, and ensure the workflow is correct.

6. Sign on to the Advanced Identity Cloud admin console as a tenant administrator.

7. Go to Governance > Requests.

8. Click the change request you just submitted, and ensure the request details are correct.

9. Approve or reject the request, and ensure the request status updates accordingly.

---

---
title: Configure user display properties
description: Configure which managed user attributes appear in user details modals across access request and certification workflows.
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/configure-user-display-properties
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/configure-user-display-properties.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["user display properties", "user info modal", "user attributes", "iga_ui_config", "access requests", "certifications"]
section_ids:
  remove_the_display_restriction: Remove the display restriction
---

# Configure user display properties

You can control which managed user attributes Identity Governance displays in user details across access request and certification workflows. By default, Identity Governance shows all available attributes. Use the `user.displayProperties` setting in `iga_ui_config`, the Identity Governance UI configuration resource, to restrict the view to a specific set of attributes.

|   |                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can't configure user display properties in the Advanced Identity Cloud admin console. You must use the API for this configuration. |

The following table describes the three modals affected by this setting:

| Surface                                | Effect                                                                                                                             |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| Certification task: user details modal | Only the listed properties appear on the User Details tab.                                                                         |
| Certification task: column sort modal  | Identity Governance filters the User column category to the listed properties; you can't add hidden properties as visible columns. |
| Access request: New request user modal | Only the listed properties appear when you open a requester's user details.                                                        |

|   |                                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * This is a display-only restriction. Identity Governance retrieves the full user object from Advanced Identity Cloud; the configuration controls only what is visible to reviewers.

* In the following examples, replace \<access-token> with an access token created with the `fr:iga:*` service account scope. Learn more in [Get an access token](../../developer-docs/authenticate-to-rest-api-with-access-token.html). |

To configure user display properties:

1. Get the current `iga_ui_config` to preserve any existing settings:

   ```bash
   curl \
   --request GET \
   --header "Authorization Bearer <access-token>" \
   --header "Accept-API-Version: resource=1.0" \
   "https://<tenant-env-fqdn>/iga/commons/config/iga_ui_config"
   ```

2. Use `PUT iga/commons/config/iga_ui_config` with the full config object, setting `user.displayProperties` to an array of attribute names:

   ```bash
   curl \
   --request PUT \
   --header "Authorization Bearer <access-token>" \
   --header "Content-Type: application/json" \
   --header "Accept-API-Version: resource=1.0" \
   --data '{
     ...
     "user": {
       "displayProperties": ["givenName", "sn", "mail", "userName"]
     }
     ...
   }'
   https://<tenant-env-fqdn>/iga/commons/config/iga_ui_config"
   ```

   The properties appear in the order listed. You can include any attribute from your managed user schema, including custom attributes. Changes take effect immediately on the next page load. To confirm the configuration, open a certification task or access request and verify the user details modal, where only the attributes you listed appear.

   ![Access review user details modal displaying the limited set of user attributes.](../_images/governance-user-display-properties.png)

## Remove the display restriction

To restore the default behavior and show all attributes, set `displayProperties` to an empty array or omit the key:

```bash
curl \
--request PUT \
--header "Authorization Bearer <access-token>" \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "user": {
    "displayProperties": []
  }
}'
"https://[.var]##<tenant-env-fqdn>##/iga/commons/config/iga_ui_config"
```

---

---
title: Configure user lifecycle management
description: Enable delegated user management allowing authorized users to create, modify, and delete users
component: pingoneaic
page_id: pingoneaic:identity-governance:administration/lcm-user
canonical_url: https://docs.pingidentity.com/pingoneaic/identity-governance/administration/lcm-user.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["user lifecycle management", "user LCM", "delegated administration", "create user", "modify user", "delete user", "scopes", "workflows"]
section_ids:
  manage_user_permissions: Manage user permissions
  enable_manage_users: Enable manage users
  configure_the_user_create_form: Configure the user create form
  configure_user_lifecycle_workflows: Configure user lifecycle workflows
  configure_workflows_for_user_lcm: Configure workflows for user LCM
---

# Configure user lifecycle management

Identity Governance allows authorized end users to create, update, delete, and view user information. This functionality enforces policies by requiring approval workflows before authorized end users can apply any user changes.

## Manage user permissions

By default, administrators, manager, direct report, and end users have the following permissions:

| Action            | Admin                    | Manager                  | End user  |
| ----------------- | ------------------------ | ------------------------ | --------- |
| View user         | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |
| View users access | [icon: check, set=fa]Yes | [icon: check, set=fa]Yes | If scoped |
| Create user       | [icon: check, set=fa]Yes | If scoped                | If scoped |
| Modify user       | [icon: check, set=fa]Yes | If scoped                | If scoped |
| Delete user       | [icon: check, set=fa]Yes | If scoped                | If scoped |

## Enable manage users

Administrators must enable user management functionality to activate the feature in the hosted account pages. The user management functionality is also known as user lifecycle management (user LCM).

1. In the Advanced Identity Cloud admin console, go to Governance > Requests.

2. On the Requests page, click the Settings tab.

3. In the Governance LCM section, click Activate.

4. In the Governance LCM modal, read what activating this feature entails, and click Next.

   ![Governance LCM modal](../_images/governance-lcm-modal.png)

5. In the Governance LCM modal, click User LCM, and then click Activate.

   ![Enable Users LCM on the Requests page.](../_images/governance-lcm-users-entitlements.png)

   The manage user access is now enabled.

## Configure the user create form

Create a form for the end users to use during the user create process.

1. In the Advanced Identity Cloud admin console, go to Governance > Forms.

2. Click [icon: add, set=material, size=inline] New Form.

3. In the New Form modal, select LCM form.

   ![Select LCM form on the New Form modal](../_images/governance-user-lcm-new-form.png)

4. In the LCM form modal, configure the following:

   * Form Name: Enter a form name.

   * Description (optional): Enter a general description of the form.

   * Identity Profile: Select User.

   * Use this form for request creation: Click this option to use with LCM operations.

   * Operation: Associate the form to the LCM operation. Select Create.

5. Click Save.

   ![LCM form details](../_images/governance-user-lcm-new-form-details.png)

6. In the Create New User form editor, drag and drop the fields you want to include on the form and then click Save.

   ![User create form](../_images/governance-user-lcm-new-form-user-create.png)

7. (Optional) Repeat the process to create forms for Modify User and Delete User, which appear in place of the default forms.

## Configure user lifecycle workflows

Identity Governance provides the out-of-the-box request types and workflows to enable authorized users to carry out user LCM tasks. You can customize these workflows by creating copies of an out-of-the-box workflow.

| Request Type | Workflow    |
| ------------ | ----------- |
| Create User  | Create User |
| Modify User  | Modify User |
| Delete User  | Delete user |

### Configure workflows for user LCM

Use the following steps to duplicate a default workflow, set approvers, and publish it:

1. In the Advanced Identity Cloud admin console, go to Governance > Workflows.

2. Select the default workflow for the Create User request type, click the ellipsis ([icon: more_horiz, set=material, size=inline]), and then click Duplicate.

3. In the Workflow Details modal, enter a name for the workflow, and click Save.

4. In the Workflow Editor, click the Approval node.

5. In the right pane, click add approvers manually and click [icon: add, set=material, size=inline] to add approvers.

6. In the Edit Approver modal, configure the following:

   * Approver Type: Select User.

   * User: Select a user.

   * Permissions: Select the permissions available to the approver.

     * Approver

     * Reject

     * Forward

     * Modify

     * Comment

7. Click Add.

   ![Edit approver page in the Create User workflow](../_images/governance-user-lcm-edit-approver.png)

8. Click Save to apply your changes to the workflow.

9. When you're ready to use your workflow, click Publish.

10. Repeat the process to set the approver for the default workflows associated with the Modify User and Delete User request types.