---
title: About reports
description: Overview of reporting capabilities in Advanced Identity Cloud for insights and compliance
component: pingoneaic
page_id: pingoneaic:reports:administration/about-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/administration/about-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "reports"]
---

# About reports

Advanced Identity Cloud provides a reporting infrastructure to help you gain better insights into your IAM activities. The reports cover a wide range of services including application access, IDM syncs, journeys, user statistics to assist in making critical business decisions and monitor compliance policies.

Tenant administrators can use the Reports page to view template drafts, view previous report runs, and generate new reports. You can also export the reports as a CSV or JSON file for further analysis.

![reports dashboard no newreport](../_images/reports-dashboard-no-newreport.png)

* 1 On the Advanced Identity Cloud admin console, click Reports to access Advanced Identity Cloud reports. All Advanced Identity Cloud customers (new or existing) get access to the out-of-the-box reports.

* 2 Enter a report name, case-insensitive, to search for a report.

* 3 Click Run on any report to generate a reporting run.

* 4 Click ellipsis ([icon: ellipsis, set=fa]), and then click Run History to view the report, export the file, and view information about past reporting runs.

---

---
title: Advanced Reporting
description: Create custom reports using advanced queries, filters, and joins across identity data
component: pingoneaic
page_id: pingoneaic:reports:administration/advanced-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/administration/advanced-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Advanced Identity Cloud", "Reports", "Template", "Custom reports"]
section_ids:
  assign-report_viewer: Assign report_viewer group
  add_a_user_to_the_report_viewer_group: Add a user to the report_viewer group
  create-custom-reports-using-advanced-reporting: Create custom reports using Advanced Reporting
  reports-name-change: Reports name change
  entities-and-attributes: Entities and attributes available in advanced reporting
---

# Advanced Reporting

Advanced Reporting lets you create custom reports on activity in your Advanced Identity Cloud tenant environment. You can query a number of metrics to create useful reports for your company.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add Advanced Reporting to your PingOne Advanced Identity Cloud subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

Important tips for Advanced Reporting

* The Advanced Reporting feature has the following features:

  * Supports detailed entity relationships to enable a variety of join operations.

  * Allows user-specified query parameters to be included dynamically at runtime.

  * Provides a wide range of operators to meet different query requirements.

  * Supports aggregate operations on the resulting dataset.

  * Restricts data access by assigning reports to specific users or a designated `report_viewer` group.

  * Supports report duplication to extend or modify existing queries.

* Advanced Reporting custom reports can only be assigned to end users.

* Users must be assigned to the [report\_viewer](#assign-report_viewer) group to run and access custom reports.

* Advanced Reporting continuously streams data from Advanced Identity Cloud, resulting in near-real time report results (approximately a minute behind real time).

* **Query Limits**: For customers who have the advanced reporting add-on capability, the tenant administrators can query data from the most recent 90 days for reports that cover AM entities and some IDM operations (sync and recon). The query limits apply to both draft and published advanced reports.

* **Use case**: Learn more about advanced reporting at [Creating a custom report using Advanced Reporting](../../use-cases/use-case-advanced-reporting.html)

## Assign `report_viewer` group

Advanced Identity Cloud provides a group to which users can be assigned to access custom reports.

| Group              | Capability                                                                                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **report\_viewer** | A user with this group can do the following:- View and run all custom reports.

- View and run all published custom reports allowed for the **report\_viewer** group. |

### Add a user to the report\_viewer group

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha-name - Groups.

3. Click [icon: plus, set=fa]New Alpha realm - Group.

4. On the New Alpha realm - group modal, enter the following:

   * Name: Enter `report_viewer`.

   * Description: Enter a general description for the group.

   * Click Next.

5. On the Dynamic Alpha realm - group Assignment modal, click A filter for conditionally assigned members if you want to add a filter.

   1. Select Any or All conditions that must be met to assign to a user.

   2. Select a property, such as `username`, `first name` or others for your condition.

   3. Select an operator, such as `contains`, `does not contain`, or others for your condition.

   4. Enter a property value.

   5. Click plus:icon\[] to add the condition to your filter.

6. Click Save.

## Create custom reports using Advanced Reporting

1. In the Advanced Identity Cloud admin console, click [icon: plus, set=fa]New Report.

2. On the New Report modal, enter the following properties, and then click Next:

   | Field       | Description                                                                                                                                                                                                                                        |
   | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name        | Name of the report. Follow the naming conventions established by your company.                                                                                                                                                                     |
   | Description | Optional. Enter a description describing the report.                                                                                                                                                                                               |
   | Who Can Run | Click to set who can run this report.**Groups**:- Report Viewer**Users**:- Select the users who can run this report. To select a user, you must have assigned the `report_viewer` group permissions to the user from the **Manage Identity** page. |

3. Next, add a data source or select an existing data source:

   1. Click [icon: plus, set=fa]Data Source.

   2. On the Add a Data Source modal, select a data source to use in this report, and then click Next:

      > **Collapse: Click to review the data sources:**
      >
      > * am\_access\_outcome
      >
      > * idm\_config
      >
      > * idm\_sync
      >
      > * roles
      >
      > * idm\_recon
      >
      > * users
      >
      > * orgs
      >
      > * node\_events
      >
      > * applications
      >
      > * idm\_activities
      >
      > * governance\_data\[[1](#_footnotedef_1 "View footnote.")]
      >
      > * journey\_events
      >
      > * governance\_decision\_events\[[1](#_footnotedef_1 "View footnote.")]
      >
      > * campaign\_details\[[1](#_footnotedef_1 "View footnote.")]
      >
      > * campaign\_decision\_details\[[1](#_footnotedef_1 "View footnote.")]

4. Next, select the columns in the report in the right pane for your report result. Each data source can have different attributes. When you click an attribute, the column appears on the main window.

5. Click the plus icon ([icon: plus, set=fa]) to define parameters that the end user provides or extracted from the end user profile while running the report:

   1. On the Add a Parameter modal, enter the following fields:

      | Field             | Description                                                                                                                                                        |
      | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      | Name              | Name of the parameter or profile attribute. Also, the name appears on the filter attribute list.                                                                   |
      | Parameter Type    | User provided parameter or a profile attribute.                                                                                                                    |
      | Input Label       | Label for parameter that appears when you do a reporting run.                                                                                                      |
      | Input Type        | Options are:- String

      - Boolean

      - Integer

      - Float

      - Date                                                                                                        |
      | Help Text         | Optional. Enter any help text for the parameter.                                                                                                                   |
      | Multivalued       | Click Multivalued to allow the end user to provide multiple values while running the report.                                                                       |
      | Enumerated Values | Click Enumerated Values if the property is an enumerated value. This property creates a drop-down list for the end user to select a value when running the report. |

   2. Click Save.

6. Next, click Filters to specify data source attributes for report filtering:

   > **Collapse: Click to review the filtering options:**
   >
   > | Field             | Description                                                                                                                                                                                                                                                                                        |
   > | ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   > | Any\|All          | Select `Any` or `All` conditions that must be met for the filters.                                                                                                                                                                                                                                 |
   > | Value             | List of attributes in the selected data source, including any custom attributes.                                                                                                                                                                                                                   |
   > | Connectors        | Options are:- has pattern (used for regular expressions)
   >
   > - contains
   >
   > - does not contain
   >
   > - greater than or equal to
   >
   > - equals to
   >
   > - not equals to
   >
   > - less than or equal to
   >
   > - less than
   >
   > - greater than
   >
   > - starts with
   >
   > - ends with
   >
   > - not starts with
   >
   > - not ends with
   >
   > - is null
   >
   > - is not null |
   > | Literal\|Variable | Value. End user provided variable. Select a value from the data source attributes or a property value passed by the end user during the report run.                                                                                                                                                |

   1. Click Save. A `Filter active` message with a checkmark appears.

7. Click Aggregate to define aggregated data counts:

   1. On the Add an Aggregate modal, enter the following:

      | Field | Description                                                                                     |
      | ----- | ----------------------------------------------------------------------------------------------- |
      | Name  | Enter a descriptive label for the aggregate.                                                    |
      | Type  | Options are:- Count of specific rows

      - Sum of specific rows

      - Distinct count of specific rows |
      | Value | Enter a value for the aggregate.                                                                |

   2. Click Save.

8. Click Sorting to sort the data tables in the report:

   1. On the Sort Data By modal, enter or select the following properties:

      | Field      | Description                                                                |
      | ---------- | -------------------------------------------------------------------------- |
      | Sort by    | Provided a list of attributes from the selected data source.               |
      | Sort order | Select the sort order for your data. Options are:- Ascending

      - Descending |

   2. Click Save.

9. Click Save at the top of the report. Your report draft appears on the Reports page and is only visible to the report template creator.

   ![reports custom](../_images/reports-custom.png)

   * 1 Click [icon: plus, set=fa]New Report to create a custom report.

   * 2 Search for a report.

   * 3 Click Run to generate a reporting run.

   * 4 Click ellipsis ([icon: ellipsis, set=fa]) to publish the draft, view the reporting run history, edit, duplicate, or delete the draft.

## Reports name change

Advanced Identity Cloud supports the ability to rename report templates in Advanced Identity Cloud.

With this feature, you can rename your custom or duplicated report templates at any time. This allows administrators to maintain a clean and organized report list, ensuring that template names are always accurate and clearly communicate their intent.

|   |                                                                                                                                                             |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | This capability applies only to report templates you have created. You can't change the name of an out-of-the-box report template provided with the system. |

1. In the Advanced Identity Cloud admin console, go to Reports.

2. Select a report.

3. Click the ellipsis ([icon: ellipsis, set=fa]), and then click Edit Template.

4. In the Settings pane, click the Details tab.

5. Change the report name. The report name can contain only alphanumeric characters and spaces, and it has no character limit.

6. Click Save.

## Entities and attributes available in advanced reporting

The following entities and attributes are available to tenant administrators when creating advanced reports:

| Entity                                                          | Attributes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Query Limited? |
| --------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Users                                                           | * Account Status

* City

* Common Name

* Consented Mappings

* Country

* Description

* Display Name

* Email Address

* Generic Indexed Date 1

* Generic Indexed Date 2

* Generic Indexed Date 3

* Generic Indexed Date 4

* Generic Indexed Date 5

* Generic Indexed Integer 1

* Generic Indexed Integer 2

* Generic Indexed Integer 3

* Generic Indexed Integer 4

* Generic Indexed Integer 5

* Generic Indexed Multivalued 1

* Generic Indexed Multivalued 2

* Generic Indexed Multivalued 3

* Generic Indexed Multivalued 4

* Generic Indexed Multivalued 5

* Generic Indexed String 1

* Generic Indexed String 2

* Generic Indexed String 3

* Generic Indexed String 4

* Generic Indexed String 5

* Generic UnIndexed Date 1

* Generic UnIndexed Date 2

* Generic UnIndexed Date 3

* Generic UnIndexed Date 4

* Generic UnIndexed Date 5

* Generic UnIndexed Integer 1

* Generic UnIndexed Integer 2

* Generic UnIndexed Integer 3

* Generic UnIndexed Integer 4

* Generic UnIndexed Integer 5

* Generic UnIndexed Multivalued 1

* Generic UnIndexed Multivalued 2

* Generic UnIndexed Multivalued 3

* Generic UnIndexed Multivalued 4

* Generic UnIndexed Multivalued 5

* Generic UnIndexed String 1

* Generic UnIndexed String 2

* Generic UnIndexed String 3

* Generic UnIndexed String 4

* Generic UnIndexed String 5

* Given Name

* Id

* Last Name

* Password Expiration Date

* Password Last Changed Time

* Postal Address

* Postal Code

* Preferences

* Realm

* State Province

* Telephone Number

* Update Date

* User Name | No             |
| Roles                                                           | - Condition

- Creation Date

- Object Id

- Realm

- Role Description

- Role Name

- Temporal Constraints

- Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No             |
| Organizations                                                   | * Creation Date

* Id

* Org Name

* Realm

* Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No             |
| Applications                                                    | - Application Name

- Authoritative

- Connector ID

- Creation Date

- Id

- Mapping Names

- Realm

- Template Name

- Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No             |
| Journeys                                                        | * Component

* Event Name

* IP Address

* Journey Name

* Journey Result

* Principal

* Realm

* Source

* Timestamp

* Tracking Ids

* Transaction Id

* User Id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Yes            |
| Nodes                                                           | - Component

- Event Name

- Journey Name

- Node Event Time

- Node Id

- Node Name

- Node Outcome

- Node Type

- Principal

- Tracking Ids

- Transaction Id

- User Id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes            |
| AM Access Outcome                                               | * Application Name

* Component

* Event Name

* Event Time

* Http Request Method

* Http Request Path

* Http Request Secure

* IsActive

* Realm

* Request

* Resource Owner Id

* Scope

* Status

* Token Type

* Transaction Id

* User Id

* User Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Yes            |
| AM Access Attempt                                               | - Component

- Event Name

- Event Time

- Http Request Method

- Http Request Path

- Http Request Secure

- Object Id

- Realm

- Status

- Token Type Hint

- Transaction Id

- User Id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes            |
| IDM Sync                                                        | * Action

* Event Time

* Exception

* Mapping

* Message

* Realm

* Situation

* Source Object

* Status

* Target Object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Yes            |
| IDM Recon                                                       | - Action

- Event Time

- Exception

- Mapping

- Message

- Realm

- Recon Id

- Situation

- Source Object

- Status

- Target Object

- Transaction Id

- User Id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Yes            |
| IDM Config                                                      | * After

* Before

* Changed Fields

* Event Time

* Object Id

* Operation

* Revision                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | No             |
| Entitlements                                                    | - Creation Date

- Display Name

- Entitlement Data

- Entitlement Description

- Entitlement Id

- Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No             |
| Assignments                                                     | * Assignment Description

* Assignment Mapping

* Assignment Name

* Assignment Type

* Creation Date

* Realm

* Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No             |
| Groups                                                          | - Group Condition

- Group Description

- Group Name

- Object Id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No             |
| Internal Roles                                                  | * Creation Date

* Internal Role Condition

* Internal Role Description

* Internal Role Name

* Object Id

* Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | No             |
| Accounts                                                        | - Account Date

- Application Name

- Creation Date

- Display Name

- Id

- Update Date

- UserId                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No             |
| Campaigns                                                       | * Certification Type

* Completion Date

* Creation Date

* Deadline

* Event Based

* Id

* Name

* Owner Given Name

* Owner Email

* Owner Last Name

* Owner User Name

* Start Date

* Status

* Template Id

* Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No             |
| Policy                                                          | - Creation Date

- Description

- Id

- Name

- Owner Email

- Owner Given Name

- Owner Id

- Owner Last Name

- Owner User Name

- Status

- Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No             |
| Policy Rules                                                    | * Allow Exception

* Allow Remediation

* Correction Advice

* Creation Date

* Description

* Detective

* Documentation Url

* Id

* Max Exception Duration

* Mitigation Control

* Name

* Owner Given Name

* Owner Email

* Owner Id

* Owner Last Name

* Owner User Name

* Preventive

* Risk Score

* Role Definition

* Status

* Update Date

* Violation Action

* Violation Owner Email

* Violation Owner Given Name

* Violation Owner Id

* Violation Owner Last Name

* Violation Owner UserName

* Workflow Id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No             |
| Policy Scan                                                     | - Completion Date

- Creation Date

- Id

- Is Simulation

- Scan Target

- Start Date

- Status

- Total Rules

- Total Violations

- Update Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | No             |
| Policy Violation                                                | * Creation Date

* Description

* Id

* Name

* Outcome

* Policy Rule Id

* Status

* Type

* Update Date

* User Id

* User Name

* Work Flow Id

* Start Date                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No             |
| Account Review Items (Not available as main datasource)         | - Account Display Name

- Account Id

- Account Type

- Actors

- Application Id

- Application Name

- Campaign Id

- Completion Date

- Confidence Score

- Creation Date

- Deadline

- Decision

- Decision By

- Decision Comments

- Decision Date

- Entitlement Display Name

- Entitlement Id

- Id

- Last Certified

- Primary Reviewer Id

- Primary Reviewer Type

- Provisioning Method

- Reviewers

- Status

- Update Date

- User Given Name

- User Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No             |
| Entitlement Review Items (Not available as main datasource)     | * Account Display Name

* Account Id

* Account Type

* Actors

* Campaign Id

* Completion Date

* Confidence Score

* Creation Date

* Deadline

* Decision

* Decision By

* Decision Comments

* Decision Date

* Entitlement Display Name

* Entitlement Id

* Id

* Last Certified

* Primary Reviewer Id

* Primary Reviewer Type

* Provisioning Method

* Reviewers

* Status

* Update Date

* User Given Name

* User Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | No             |
| Role Membership Review Items (Not available as main datasource) | - Actors

- Campaign Id

- Completion Date

- Confidence Score

- Creation Date

- Deadline

- Decision

- Decision By

- Decision Comments

- Decision Date

- Id

- Last Certified

- MembershipType

- Primary Reviewer Id

- Primary Reviewer Type

- Reviewers

- Role Id

- Role Name

- Status

- Update Date

- User Given Name

- User Name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | No             |

***

[1](#_footnoteref_1). PingOne® Identity Governance is an add-on capability to Advanced Identity Cloud. Contact your Ping Identity representative if you want to add PingOne® Identity Governance to your Advanced Identity Cloud subscription.

---

---
title: Create a historical change report for IDM identities
description: Generate historical change reports tracking modifications to identity profiles over time
component: pingoneaic
page_id: pingoneaic:reports:use-cases/use-case-historical-data-reporting
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/use-cases/use-case-historical-data-reporting.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Feb. 4, 2026
keywords: ["Advanced Identity Cloud", "Reports", "Template", "Custom reports", "Use Case", "Historical data"]
section_ids:
  use-case-name-goals: Goals
  use-case-name-before-begin: Before you begin
  use-case-name-tasks: Tasks
  use-case-task-1-create-report-template: "Task 1: Create the report template"
  use-case-name-task-2-add-data-source: "Task 2: Add the data source"
  use-case-name-task-3-run-report: "Task 3: Run the report"
---

# Create a historical change report for IDM identities

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add Advanced Reporting to your PingOne Advanced Identity Cloud subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

Advanced Identity Cloud's advanced reporting capability allows you to generate historical data reports for IDM objects, summarizing the audit trail of changes to these managed identities. For each IDM profile change, Advanced Identity Cloud tracks the modified attribute, its previous and new values, the actor who made the change, timestamp, and transaction ID.

As a report author, you can generate reports on the history of managed identities. For example, you can create reports that list all profile changes for specific users over a period, show which users were deleted, or detail attribute changes for objects like roles, accounts, and applications.

Important tips for historical change reporting

The following are important points to keep in mind when using historical change reporting:

* **Scope**

  * Advanced Identity Cloud reports display changes for all IDM-managed entities with the ability to filter by specific entity types. This includes users, roles, accounts, and applications.

  * Support is limited to IDM object profile changes only.

  * Relationship changes between entities aren't included in the historical data reports.

* **Entity identification**

  * To identify entities in reports, Advanced Identity Cloud uses a generic name attribute:

    * For end users: The report uses `username`.

    * For other IDM-managed entities like roles or applications: The report uses `name`.

    * For entity-specific display attributes: The report doesn't show entity-specific display attributes, such as an end user's first or last name, as part of the entity identifier. However, it does capture and display all attribute changes with their before and after values.

* **Custom objects**

  * For custom objects, the report uses the `name` attribute as the entity name. If a `name` attribute doesn't exist, it uses the object ID.

* **Actor representation**

  * A universally unique identifier (UUID) represents the actor who performed the change and can correspond to a user, application, or another system actor.

* **Quota query limits**

  * Historical reports adhere to the same paid tier query limits as existing reports. Learn more in [Query limits](../administration/advanced-reports.html#advanced-reporting-important-tips).

## Goals

After completing this use case, you'll know how to do the following:

* Create a historical data report template.

* Run and view a historical data report.

## Before you begin

Before you start work on this use case, ensure you have these prerequisites:

* Make sure you have the advanced reporting capability in your Advanced Identity Cloud tenant.

* Ensure you have the necessary permissions to create and run reports in Advanced Identity Cloud.

## Tasks

Nova Fleming, an end user, needs to track all new account provisions within the organization. She asks the reports administrator to create a report for this purpose.

The reports administrator creates a new report template using the `IDM Activity` data source. Make sure the report only shows recent account provisions, the administrator adds a filter to track profile changes from the start of the year.

### Task 1: Create the report template

1. In the Advanced Identity Cloud admin console, go to Reports.

2. On the Reports page, click [icon: add, set=material, size=inline] New Report.

3. In the New Report modal, enter this information:

   * Name: Enter a name for your report.

   * Description: (optional) enter a description for your report.

   * Who Can Run: Select the end users who can run the report.

   * Report Viewer Group: Click to select a group of users who can view the report results. If not selected, all users who can run the report can view the results.

     ![UI example of the new report modal for historical data reports](../_images/reports-historical-data-new-report.png)

4. Click Next.

### Task 2: Add the data source

1. On the Add Data page, click [icon: add, set=material, size=inline] Data Source.

   ![UI example of the add data source page for historical data reports](../_images/reports-historical-data-add-data-source.png)

2. In the Add Data Source modal, select a Data Source and click Next. For example, select IDM Activity.

   ![UI example of the add data source modal for historical data reports](../_images/reports-historical-data-add-a-data-source-modal.png)

3. On the draft report page, select the properties in the right column that you want to appear in the report. For example:

   * Actor: The actor who made the change.

   * Changed Attribute: The specific attribute that was modified in the IDM object.

   * Entity Name: The name of the IDM-managed entity that was changed. For end users, this is the `username`. For other entities like roles or applications, this is the `name` attribute. For custom objects, this is the `name` attribute if it exists, or the object ID if a name attribute doesn't exist.

   * Entity Type: The type of the IDM-managed entity that was changed, such as user, role, account, or application.

   * Old Value: The value of the modified attribute before the change was made.

   * New Value: The value of the modified attribute after the change was made.

   * Timestamp: The date and time when the change occurred.

   * Transaction ID: The unique identifier for the transaction that triggered the change, which can be used to correlate related changes across different entities.

     |   |                                                                                   |
     | - | --------------------------------------------------------------------------------- |
     |   | You can rearrange the columns by dragging and dropping them in the desired order. |

     ![UI example of a historical data report template with selected properties](../_images/reports-historical-data-template.png)

4. Limit the report results to a specific time range by adding filters on the timestamp property and excluding automated processes:

   1. In the right pane, scroll down to Add Filters and click [icon: add, set=material, size=inline].

   2. In the Add Filters modal, enter this information:

      * Value: Enter a value for the filter. For example, select idm\_activity\_logs.Timestamp.

      * Operator: Select an operator for the filter. For example, select greater than or equal to.

      * Literal: Select the Literal option.

      * Value: Enter the literal value. For example, enter 2026-01-01T00:00:00.

   3. Click [icon: add, set=material, size=inline], and then click Add Rule.

   4. Repeat the previous step to add another filter for the timestamp property to set an end date for the report results. For example, you can set the end date to the current date to show all account provisions from the start of the year.

      * Value: Enter a value for the filter. For example, select idm\_activity\_logs.Timestamp.

      * Operator: Select an operator for the filter. For example, select less than or equal to.

      * Literal: Select the Literal option.

      * Value: Enter the literal value. For example, enter 2026-02-07T00:00:00.

   5. Click Save.

      ![UI example of the add filter modal for historical data reports](../_images/reports-historical-data-add-filters.png)

5. On the report template, click Save in the top right.

### Task 3: Run the report

1. On the Reports page, click on the report you just created.

2. Click Run Report.

3. On the Run History tab, click View Report to see the result.

   The report shows a historical view of all profile changes for the IDM-managed entities matching the report filters. For example:

   ![UI example of the report results for a historical data report](../_images/reports-historical-data-report-results.png)

---

---
title: Custom attribute for relationships in Advanced Reporting
description: Create custom reports on relationships between identity objects using custom attributes
component: pingoneaic
page_id: pingoneaic:reports:use-cases/custom-attributes-for-relationship-in-advanced-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/use-cases/custom-attributes-for-relationship-in-advanced-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Advanced Identity Cloud", "Reports", "Template", "Custom attributes", "Relationships"]
section_ids:
  steps: Steps
  create-a-custom-relationship: Create a custom relationship
  create-a-custom-report-with-custom-relationship: Create a new report using the custom relationship
  generate-the-custom-relationship-report: Generate your custom relationship report
---

# Custom attribute for relationships in Advanced Reporting

Advanced Reporting supports custom attributes for relationships in its reports. When an administrator creates a custom relationship in the native IDM console for the `user` identity object, the relationship is available in Advanced Reporting (custom reports) and filters.

A relationship represents a connection between two identity objects, such as users, devices, groups, or roles. Relationships define how these entities interact, enabling hierarchical structures, access controls, and delegation of responsibilities.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add Advanced Reporting to your PingOne Advanced Identity Cloud subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

## Steps

In this example, you have a user who is a developer lead with an `Analyst` role. The user supervises other developers in the company.

The tenant administrator creates a relationship, `custom_alpharoles` in IDM that represents the connection between two identity objects, `alpha_user` and `alpha_role`.

The general steps are:

* [Create a custom relationship](#create-a-custom-relationship)

* [Create a new report using the custom relationship](#create-a-custom-report-with-custom-relationship)

* [Generate your custom relationship report](#generate-the-custom-relationship-report)

### Create a custom relationship

1. Sign on to Advanced Identity Cloud admin console as as tenant administrator.

2. Add a custom relationship:

   1. Go to Native Consoles > Identity Management.

   2. Click Configure > Managed Objects and click Alpha\_user.

   3. On the Alpha\_user page, click [icon: add, set=material, size=inline] Add a property.

   4. Scroll down to the bottom of the page and enter the following:

      * For Name, enter `custom_alpharoles`.

        |   |                                                                                                                                                                                                   |
        | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Custom relationships must be prefixed with `custom_`. Learn more about custom relationships at [Create a relationship between two objects](../../idm-objects/relationships-between-objects.html). |

      * For Type, select Relationship.

   5. Click Next.

   6. In the Add Resource modal, select alpha\_role for Resource.

   7. For Display Properties, select name.

3. In the Advanced Identity Cloud admin console, go to Identities > Manage and click Alpha realm - Users.

   1. Locate and click your test user to open the Details page.

   2. On the Details page, select the Analyst role in the Custom\_alpharoles field.

   3. Click Save.

### Create a new report using the custom relationship

1. In the Advanced Identity Cloud admin console, go to Reports.

   1. Click [icon: add, set=material, size=inline] New Report.

   2. In the New Report modal, enter the following:

      * Name: Enter a descriptive name for the new report.

      * Description (optional): Enter a general description for the report.

      * Who can run: Select Users.

   3. Click Next.

2. Click [icon: add, set=material, size=inline] Data Source.

   1. In the Add a Data Source modal, select Users and click Next.

   2. On the draft report page, select the properties in the right pane you want to appear in the report. For example:

      * Username

      * First Name

      * Last Name

3. On the same page in the right pane, scroll down to Related Data Sources.

   1. Next to Custom\_alpharoles, click [icon: add, set=material, size=inline] and then click [icon: add, set=material, size=inline] Add as Data Source.

   2. Scroll down to users/custom\_alphaRoles and click Role Name.

      |   |                                                                                   |
      | - | --------------------------------------------------------------------------------- |
      |   | You can rearrange the columns by dragging and dropping them in the desired order. |

   3. Click Save.

### Generate your custom relationship report

1. On the Reports page, locate your custom report and click Run.

2. On your report page, click Run Now.

3. After your report has generated, click View Report.

   The report displays all users with a custom relationship.

4. Review your report if you are satisfied with the results, click [icon: ellipsis, set=fa]> Publish to activate it.

   ![An example of a generated custom report using a custom relationship.](../_images/custom-relationship-report-example.png)

---

---
title: Custom attributes for organization objects in Advanced Reporting
description: Create custom reports displaying custom attributes added to organization objects
component: pingoneaic
page_id: pingoneaic:reports:use-cases/custom-attributes-for-organization-in-advanced-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/use-cases/custom-attributes-for-organization-in-advanced-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Advanced Identity Cloud", "Reports", "Template", "Custom attributes", "Organization Object"]
section_ids:
  steps: Steps
  create-an-organization: Create an organization with custom attributes
  create-suborganizations: Create suborganizations
  create-a-new-report-for-custom-organization: Create a new report for the custom organization
  generate-the-custom-organization-report: Generate your custom organization report
---

# Custom attributes for organization objects in Advanced Reporting

An [organization object](../../idm-objects/organizations.html) defines a hierarchical tree structure for users, allowing you to assign privileges to all or specific parts of the tree.

Advanced Reporting supports custom attributes for the organization object in its reports. When an administrator creates a custom attribute in the native IDM console for the `organization` object, the attributes are available in Advanced Reporting (custom reports) and filters.

|   |                                                                                                                                                                                                                                                                         |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Advanced Identity Cloud add-on capabilityContact your Ping Identity representative if you want to add Advanced Reporting to your PingOne Advanced Identity Cloud subscription. Learn more in [Add-on capabilities](../../product-information/add-on-capabilities.html). |

## Steps

In this example, you're a system administrator for a large AI company and want to generate a custom report displaying tech leads in your departments.

You need to set up a hierarchical organization for the `Research and Development` division, which comprises multiple departments: `Computer Vision`, `Data Engineering`, and `Data Science`. Within each department, there are multiple projects with tech leads.

Complete the following steps to create the custom report:

* [Create an organization with custom attributes](#create-an-organization)

* [Create suborganizations](#create-suborganizations)

* [Create a new report for the custom organization](#create-a-new-report-for-custom-organization)

* [Generate your custom organization report](#generate-the-custom-organization-report)

### Create an organization with custom attributes

1. Sign on to the Advanced Identity Cloud admin console as as a tenant administrator.

2. Add an organization in the IDM native console:

   1. Go to Native Consoles > Identity Management.

   2. Go to Configure > Managed Objects and click Alpha\_organization.

   3. On the Alpha\_organization page, click [icon: add, set=material, size=inline] Add a Property.

   4. Scroll down to the bottom of the page and create the `cust_dept` attribute:

      * For Name, enter `custom_dept`.

      * For Label, enter `Department`.

      * For Type, select String.

   5. Click Save.

   6. Create the `custom_techLead` attribute:

      * For Name, enter `custom_techLead`.

      * For Label, enter `Tech Lead`.

      * For Type, select String.

   7. Click Save.

      ![IDM native console displaying the custom attributes](../_images/custom-organization-attributes.png)

### Create suborganizations

1. Sign on to the Advanced Identity Cloud admin console as as a tenant administrator.

2. Add a `Computer Vision` suborganization:

   1. Go to Identities > Manage.

   2. Click Alpha realm - Organizations.

   3. Click [icon: add, set=material, size=inline] New Alpha realm - Organization.

   4. In the New Alpha realm - Organization modal, enter `Computer Vision` in the Name field, and click Save.

   5. In the new `Alpha realm - Organization` page, enter the following:

      * Description: Enter a general description for the suborganization.

      * Parent Organization: Select a parent organization, such as `Research and Development`.

      * Department: Enter a department, like `NLP`, a subdivision of the `Computer Vision` organization.

      * Tech Lead: Enter or select a user for tech lead.

   6. Click Save.

3. Repeat step 4 to add `Data Engineering` and `Data Science` suborganizations, respectively.

### Create a new report for the custom organization

1. In the Advanced Identity Cloud admin console, go to Reports.

   1. Click [icon: add, set=material, size=inline] New Report.

   2. In the New Report modal, enter the following:

      * Name: Enter a descriptive name for the new report.

      * Description (optional): Enter a general description for the report.

      * Who can run: Select Users.

   3. Click Next.

2. Click [icon: add, set=material, size=inline] Data Source.

   1. In the Add a Data Source modal, select Organizations and click Next.

   2. On the draft report page, select the properties in the Settings pane you want to appear in the report.

   3. In the orgs section:

      * Click Department.

      * Click Tech Lead.

        |   |                                                                                   |
        | - | --------------------------------------------------------------------------------- |
        |   | You can rearrange the columns by dragging and dropping them in the desired order. |

   4. Click Save.

### Generate your custom organization report

1. On the Reports page, locate your custom report and click Run.

2. On your report page, click Run Now.

3. After your report has generated, click View Report.

   The report displays your departments and tech leads.

   ![An example of a generated custom report using a custom attributes for the organization object](../_images/custom-organization-report-example.png)

4. Review your report. If you are satisfied with the results, click [icon: ellipsis, set=fa]> Publish to activate it.

---

---
title: Custom attributes for user objects
description: Create custom reports displaying custom attributes added to user identity profiles
component: pingoneaic
page_id: pingoneaic:reports:use-cases/custom-attributes-for-user-in-advanced-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/use-cases/custom-attributes-for-user-in-advanced-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Advanced Identity Cloud", "Reports", "Template", "Custom attributes", "User Object"]
section_ids:
  custom_attribute_example: Custom attribute example
---

# Custom attributes for user objects

When an administrator creates a custom attribute in the native IDM console for the `user` identity object, the attribute is available in Advanced Reporting (custom reports) and filters.

|   |                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------- |
|   | Any new custom attributes for the `user` identity object are specific to the realm to which it was added. |

## Custom attribute example

1. Add a custom attribute in the IDM native console:

   1. In the Advanced Identity Cloud admin console, go to Native Consoles > Identity Management.

   2. Click Configure > Managed Objects and click Alpha\_user.

   3. On the Alpha\_user page, click [icon: add, set=material, size=inline] Add a property.

   4. Scroll down to the bottom of the page and enter the following:

      * Name: enter `custom_department`.

        |   |                                                                                                                                                                                                                              |
        | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        |   | Custom attributes must be prefixed with `custom_`. Learn more about custom attributes at [Customize user identities using custom attributes](../../identities/identity-cloud-identity-schema.html#create-custom-attributes). |

      * Label (Optional): enter `Custom department`.

      * Select String.

      * Click Required if the property is required.

        |   |                                                                                                                                                                                                                                                                                                                                                                                                  |
        | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
        |   | The `required` policy is assessed only during object creation, not when an object is updated. You can effectively bypass the policy by updating the object and supplying an empty value for that property. To prevent this inconsistency, set both `required` and `notEmpty` to `true` for required properties. This configuration indicates that the property must exist and must have a value. |

   5. Click Save.

2. Next, create a custom report using the Advanced Reporting feature:

   1. In the Advanced Identity Cloud admin console, go to Reports.

   2. Click [icon: add, set=material, size=inline] New Report.

   3. On the New Report modal, enter the following:

      * Name: Enter a descriptive name for the new report.

      * Description (optional): Enter a general description for the report.

      * Who can run: Select Users.

   4. Click Next.

   5. Click [icon: add, set=material, size=inline] Data Source.

   6. On the Add a Data Source modal, select Users and click Next.

   7. On the draft report page, select the properties in the right column that you want to appear in the report. For example:

      * Username

      * First Name

      * Common Name

      * Custom Department

        |   |                                                                                   |
        | - | --------------------------------------------------------------------------------- |
        |   | You can rearrange the columns by dragging and dropping them in the desired order. |

   8. Click Save.

3. On the Reports page, locate your custom report and click Run.

   1. On your report page, click Run Now.

   2. After your report has generated, click View Report.

   3. Review your report if you are satisfied with the results, click [icon: ellipsis, set=fa]> Publish to activate it.

      ![An example of a generated custom report using a custom attribute.](../_images/custom-attribute-report-example.png)

---

---
title: Custom objects use cases
description: Create reports joining standard, custom, and relationship objects for complex data models
component: pingoneaic
page_id: pingoneaic:reports:use-cases/custom-objects-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/use-cases/custom-objects-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  realm_visibility_for_custom_objects: Realm visibility for custom objects
  use-case-1: "Use case 1: Relate an identity schema object to another identity schema object."
  scenario: Scenario
  what_youll_do: What you'll do
  before_you_begin: Before you begin
  data_model: Data model
  report_model: Report model
  use-case-1-tasks: Tasks
  create-the-organizations: "Task 1: Create the organizations"
  task_2_create_the_suborganizations: "Task 2: Create the suborganizations"
  task_3_create_the_users_and_link_them_to_organizations: "Task 3: Create the users and link them to organizations"
  task_4_create_the_role_and_add_members: "Task 4: Create the role and add members"
  task_5_create_the_report_template: "Task 5: Create the report template"
  task_6_generate_the_report: "Task 6: Generate the report"
  use-case-2: "Use case 2: Relate an identity schema object to a new custom object."
  use_case_2_scenario: "Use case 2: Scenario"
  what_youll_do_2: What you'll do
  before_you_begin_2: Before you begin
  data_model_2: Data model
  report_model_2: Report model
  use-case-2-tasks: Tasks
  task_1_create_the_publication_custom_object: "Task 1: Create the 'publication' custom object"
  task_2_create_the_publication_records: "Task 2: Create the publication records"
  task_3_add_a_relationship_from_the_user_object_to_the_publication_object: "Task 3: Add a relationship from the User object to the Publication object"
  task_4_link_users_to_their_publications: "Task 4: Link users to their publications"
  task_5_create_the_report_template_2: "Task 5: Create the report template"
  task_6_generate_the_report_2: "Task 6: Generate the report"
  use-case-3: "Use case 3: Relate a custom object to an identity schema object."
  scenario_2: Scenario
  what_youll_do_3: What you'll do
  before_you_begin_3: Before you begin
  data_model_3: Data model
  report_model_3: Report model
  use-case-3-tasks: Tasks
  task_1_create_the_researchproject_custom_object: "Task 1: Create the researchProject custom object"
  task_2_create_records_for_each_research_project: "Task 2: Create records for each research project"
  task_3_create_the_report_template: "Task 3: Create the report template"
  task_4_generate_the_report: "Task 4: Generate the report"
  use-case-4: "Use case 4: Relate a custom object to another custom object."
  scenario_3: Scenario
  what_youll_do_4: What you'll do
  before_you_begin_4: Before you begin
  data_model_4: Data model
  report_model_4: Report model
  use-case-4-tasks: Tasks
  task_1_create_the_specializedequipment_custom_object: "Task 1: Create the specializedEquipment custom object"
  task_2_create_the_researchprojectequipment_custom_object: "Task 2: Create the researchProjectEquipment custom object"
  task_3_create_records_for_specialized_equipment: "Task 3: Create records for specialized equipment"
  task_4_create_records_for_the_allocated_equipment: "Task 4: Create records for the allocated equipment"
  task_5_create_the_report_template_3: "Task 5: Create the report template"
  task_6_generate_the_report_3: "Task 6: Generate the report"
---

# Custom objects use cases

Analytic reports now support additional custom object use cases for companies that require more refined reports.

* **[Use case 1](#use-case-1)**: Relate an identity schema object to another identity schema object.

* **[Use case 2](#use-case-2)**: Relate an identity schema object to a new custom object.

* **[Use case 3](#use-case-3)**: Relate a custom object to an identity schema object.

* **[Use case 4](#use-case-4)**: Relate a custom object to another custom object.

## Realm visibility for custom objects

The realm visibility of your custom objects depends on a naming prefix. The following table displays the rules for the naming prefix:

| Description                                                                            | Example               | Realm visibility     |
| -------------------------------------------------------------------------------------- | --------------------- | -------------------- |
| Custom object name starts with "alpha\_"                                               | alpha\_leadResearcher | Only Alpha           |
| Custom object name starts with "bravo\_"                                               | bravo\_leadResearcher | Only Bravo           |
| Custom object name doesn't start with "alpha\_", "bravo\_", nor has "\_" in the name   | parentOrganization    | Both Alpha and Bravo |
| Custom object name doesn't start with "alpha\_", "bravo\_", but has a "\_" in the name | parent\_organization  | None                 |

## Use case 1: Relate an identity schema object to another identity schema object.

In this use case, you link a standard, out-of-the-box identity schema object to another identity schema object.

### Scenario

An AI research company wants to generate a report that lists all of its lead researchers for each suborganization. This report helps create a comprehensive view of your company's leadership structure.

### What you'll do

To configure your report, do the following tasks:

* Create a parent organization and its suborganizations.

* Define a role and assign users as members.

* Create user profiles and link them to the appropriate roles and organizations.

* Build a report template in the Advanced Reporting UI that joins `Users`, `Roles`, and `Organizations`.

* Generate the final report to view the results.

### Before you begin

* Ensure you have administrator access to the Advanced Identity Cloud admin console.

* Confirm you're familiar with creating and managing standard objects like `Users`, `Roles`, and `Organizations`.

* Verify you have access to the Advanced Reporting feature.

### Data model

The data model for use case 1 has the following structure:

* **Organizations**: The company has a parent `AI Research` organization with two suborganizations: `Natural Language Processing` and `Computer Vision`.

* **Roles**: A `lead_researcher` role grants permissions to approve research proposals and access high-performance computing resources.

* **Users**: Researchers like Dr. Evelyn Reed and Dr. Kenji Tanaka are created as users.

* **Relationship**: You link a `user` to a `role` and then scope that role membership to a specific `organization`. For example, Dr. Evelyn Reed is assigned the `lead_researcher` role, but her permissions are constrained to only the `Natural Language Processing` organization.

### Report model

Create a report on the following identity relationships to produce a clear overview of who leads which research unit.

| User             | Role             | Organization                |
| ---------------- | ---------------- | --------------------------- |
| Dr. Evelyn Reed  | lead\_researcher | Natural Language Processing |
| Dr. Kenji Tanaka | lead\_researcher | Computer Vision             |

### Tasks

#### Task 1: Create the organizations

Create the parent `AI Research` organization and its two suborganizations, `Natural Language Processing` and `Computer Vision`.

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Organizations and New Alpha realm - Organizations.

3. On the New Alpha realm - Organizations page, enter the name: AI Research.

4. Click Save.

5. In the organization page, leave the Parent Organization field blank.

6. Click Save.

#### Task 2: Create the suborganizations

Create the suborganizations: `Natural Language Processing` and `Computer Vision`.

1. Create `Natural Language Processing`:

   1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

   2. On the Manage Identities page, click Alpha realm - Organizations and New Alpha realm - Organizations.

   3. On the New Alpha realm - Organizations page, enter the Name: `Natural Language Processing`.

   4. Click Save.

   5. In the organization page, enter AI Research in the Parent Organization field.

   6. Click Save.

2. Create `Computer Vision`:

   1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

   2. On the Manage Identities page, click Alpha realm - Organizations and New Alpha realm - Organizations.

   3. On the New Alpha realm - Organizations page, enter the name: Computer Vision.

   4. Click Save.

   5. In the organization page, enter AI Research in the Parent Organization field.

   6. Click Save.

#### Task 3: Create the users and link them to organizations

Create the user profiles for Evelyn Reed and Kenji Tanaka. For each user, link their profile to the appropriate organization. For example, on Evelyn Reed's profile:

1. In the Advanced Identity Cloud admin console, go to Identities > Manage.

2. On the Manage Identities page, click Alpha realm - Users and New Alpha realm - User.

3. On the New Alpha realm - User page, enter information for the following users and then click Save.

   * Evelyn Reed

   * Kenji Tanaka

4. On the user page for `Evelyn Reed`, add the following:

   1. Click Provisioning Roles > [icon: add, set=material, size=inline] Add Provisioning Roles, and select Lead Researcher.

   2. Click Organizations I Administer > [icon: add, set=material, size=inline] Add Organizations I Administer, and select Natural Language Processing.

   3. Click Save.

   4. Click Organizations to which I belong > [icon: add, set=material, size=inline] Add Organizations to which I Belong, and select Natural Language Processing.

   5. Click Save.

5. Repeat the previous steps for `Kenji Tanaka`.

#### Task 4: Create the role and add members

Create an internal role named `Lead Researcher` and add the users `evelynReed` and `kenjiTanaka` as members.

1. On the New Alpha realm - Role page, go to Role Members > [icon: add, set=material, size=inline] Add Role Members.

2. In the Add Role Members modal, enter `evelynReed` and `kenjiTanaka`, and click Save.

#### Task 5: Create the report template

Create a report template that combines these three objects to produce a clear overview of who leads which research unit.

1. In the Advanced Identity Cloud admin console, click [icon: plus, set=fa]New Report.

2. On the New Report modal, enter the following properties, and then click Next:

   | Field       | Description                                                                                                                                                                                                  |
   | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   | Name        | Name of the report. Follow the naming conventions established by your company.                                                                                                                               |
   | Description | (Optional) Enter a description describing the report.                                                                                                                                                        |
   | Who Can Run | Click to set who can run this report.**Groups**:- Report Viewer**Users**:- Select the users who can run this report. The users available to select are those assigned the `report_viewer` group permission." |

3. Next, add a data source or select an existing data source:

   1. Click [icon: plus, set=fa]Data Source.

   2. On the Add a Data Source modal, select a data source to use in this report, and then click Next:

   3. Select Roles as a data source.

   4. On the Reports canvas, click Name in the Roles source.

4. In Related Data Sources, click Members.

   1. In the Roles/members source, click Common Name.

5. In Related Data Sources, click Organizations to which I Belong.

   1. In the Roles/members/orgs source, click Name.

6. In Related Data Sources, click Parent Organization.

   1. In the Roles/members/orgs/parentOrganization source, click Name.

7. Click Save.

8. Click Save.

#### Task 6: Generate the report

1. On the Reports page, locate your report.

2. Click Run and then Run Now.

3. On the report page, click View Report.

   ![Example of a custom object relationship for out-of-the-box IDM object to another out-of-the-box IDM object.](../_images/custom-objects-use-case-1-report.png)

## Use case 2: Relate an identity schema object to a new custom object.

In this use case, you link a standard identity schema object to a new custom object. This allows you to extend your core identity data with business-specific information.

### Use case 2: Scenario

The AI research company wants to track the academic publications authored by its researchers. The standard `User` object doesn't have fields for this, so you must link the `User` object to a new `publication` custom object.

### What you'll do

* Define the new `publication` custom object.

* Add a relationship property to the standard `User` object to link to your new custom object.

* Create records for individual publications.

* Edit user profiles to link them to their corresponding publication records.

* Build and run a report that joins the `Users` data source with your custom `publication` data.

### Before you begin

* Ensure you have administrator access to the Advanced Identity Cloud admin console.

* Verify you have access to the IDM native admin console to modify objects.

* Confirm you are familiar with creating and managing standard `User` objects.

### Data model

The data model for use case 2 has the following structure:

* **Custom Object `publication`**: Define a new object to store publication details.

  * `paperTitle` (String): Title of the paper.

  * `journalName` (String): Name of the journal.

  * `publicationDate` (Date): Date of publication.

* **Standard Object `User`**: Out-of-the-box user object.

* **Relationship**: Add a new relationship attribute, `authoredPapers`, to the `User` object. This attribute links a user's profile to one or more records in the `publication` object.

### Report model

Create a report that joins the `User` object with the `publication` custom object to see which papers were authored by which researchers.

| Researcher Name  | Paper Title                                | Journal                               |
| ---------------- | ------------------------------------------ | ------------------------------------- |
| Dr. Evelyn Reed  | Advances in Neural Network Compression     | Journal of Machine Learning Research  |
| Dr. Kenji Tanaka | Real-time Object Detection on Edge Devices | IEEE Transactions on Pattern Analysis |

### Tasks

#### Task 1: Create the 'publication' custom object

To create a custom object `publication`:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. In the top navigation menu, click Configure > Managed Objects.

3. Click [icon: add, set=material, size=inline] New Managed Object.

   1. In the Managed Object Name field, enter `publication`.

   2. In the Readable Title field, enter `Publication`.

   3. In the Managed Object Icon field, select an icon for the object to appear on the Managed Objects page.

   4. In the Managed Design Icon field, find an icon in the Google icon repository.

   5. In the Description field, enter a general description of the object. For example, `Stores metadata for academic papers published by company researchers`.

4. In the Managed Object/publication page, click [icon: add, set=material, size=inline] Add a property. For each property, enter or select the following:

   | Property Name   | Label                   | Type   | Required |
   | --------------- | ----------------------- | ------ | -------- |
   | papertitle      | Title of the paper      | String | Required |
   | journalname     | Name of the journal     | String | Required |
   | publicationdate | Date of the publication | String |          |

5. Click Save.

#### Task 2: Create the `publication` records

To create a `publication` custom object:

1. In the Advanced Identity Cloud admin console, navigate to Identities > Manage.

2. Click Publications to view the list of existing publication records if any.

3. Click [icon: add, set=material, size=inline] New Publication to open the creation form.

4. Fill in the details for the paper. For example:

   * Title of the paper: `Advances in Neural Network Compression`

   * Name of the journal: `Journal of Machine Learning Research`

   * Date of the publication: `2025-10-15`

5. Click Save.

6. On the Publication page, click Save.

7. Repeat the steps for another publication:

   * Title of the paper: `Real-time Object Detection on Edge Devices`

   * Name of the journal: `IEEE Transactions on Pattern Analysis`

   * Date of the publication: `2025-02-19`

You've now created a record for the specific publications.

#### Task 3: Add a relationship from the `User` object to the `Publication` object

To create a custom relationship property using the Advanced Identity Cloud admin console:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. In the top navigation menu, click Configure > Managed Objects.

3. Select a managed object type: alpha\_user.

4. Click [icon: add, set=material, size=inline] Add a Property. An entry field displays.

   1. In the Name field, enter a name for the custom relationship property. The name must begin with the string `custom_`, such as `custom_publication`.

   2. In the Type list, select Relationship.

   3. Click Next. The Add Resources modal displays.

   4. In the Resource list, select the resource to map the custom relationship property to. Select publication.

   5. In the Display Properties list, select the properties on the resource to map to the custom relationship property. Select paperTitle.

5. Click Save. The Relationships Property screen for the new relationship property displays.

6. Click Save.

|   |                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Objects are limited to 10 custom relationships. If you need an object to have more, create custom relationships from the related object and map them to the original object. |

#### Task 4: Link users to their publications

To set the `publication` object for each user:

1. In the Advanced Identity Cloud admin console, navigate to Identities > Manage.

2. Click Alpha realm - Users, search for `evelynReed`, and click the user.

   1. On the Alpha realm - User page, scroll down to Custom\_publication. Select Advances in Neural Network Compression.

   2. Click Save.

3. Repeat the steps for `kenjiTanaka`. Click Alpha realm - Users, search for `kenjiTanaka`, and click the user.

   1. On the Alpha realm - User page, scroll down to Custom\_publication. Select Real-time Object Detection on Edge Devices.

   2. Click Save.

#### Task 5: Create the report template

1. In the Advanced Identity Cloud admin console, click [icon: plus, set=fa]New Report.

2. On the New Report modal, enter the following properties, and then click Next:

   | Field       | Description                                                                                                                                                                                                                                        |
   | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name        | Name of the report. Follow the naming conventions established by your company.                                                                                                                                                                     |
   | Description | (Optional) Enter a description of the report.                                                                                                                                                                                                      |
   | Who Can Run | Click to set who can run this report.**Groups**:- Report Viewer**Users**:- Select the users who can run this report. To select a user, you must have assigned the `report_viewer` group permissions to the user from the **Manage Identity** page. |

3. Next, add a data source or select an existing data source:

   1. Click [icon: plus, set=fa]Data Source.

   2. On the Add a Data Source modal, select a data source to use in this report, and then click Next:

   3. Select Users.

   4. On the Reports canvas, click Common Name.

4. In Related Data Sources, click Custom relationship.

   1. In the users/custom\_publication source:

      1. Click Title of the paper.

      2. Click Name of the journal.

5. Click Save.

6. Click Save.

#### Task 6: Generate the report

1. On the Reports page, locate your report.

2. Click Run and then Run Now.

3. On the report page, click View Report.

   ![Example of a custom object relationship for out-of-the-box IDM object to a custom object.](../_images/custom-objects-use-case-2-report.png)

## Use case 3: Relate a custom object to an identity schema object.

In this use case, you link a new custom object to a standard identity schema object. This allows you to track business-specific information and relate it directly to your core identity data.

### Scenario

The AI research company wants to track specific research projects and assign them to lead researchers. To do this, create a `researchProject` custom object and link it to the standard `User` object.

### What you'll do

* Define the new `researchProject` custom object that includes a relationship to the `User` object.

* Create records for individual research projects.

* Link each project record to a lead researcher by selecting a user.

* Build and run a report that joins the `researchProject` data source with the `User` data.

### Before you begin

* Ensure you have administrator access to the Advanced Identity Cloud admin console.

* Verify you have access to the IDM native admin console to modify objects.

* Confirm you're familiar with creating and managing standard `User` objects.

### Data model

The data model for use case 3 has the following structure:

* **Custom Object `researchProject`**: Define a new object to store project details.

  * `projectName` (String): Public name of the project.

  * `projectID` (String): Unique internal identifier.

  * `projectStatus` (String): Current state, such as "Active" or "Completed."

  * `leadResearcher` (Relationship): Link to a record in the `User` object.

* **Standard Object `User`**: Out-of-the-box user object.

* **Relationship**: The `leadResearcher` attribute on the `researchProject` object creates a direct link from a project to the user who leads it.

### Report model

You can create a report that joins the `researchProject` custom object with the `User` object to see which projects are assigned to which researchers.

| Project Name    | Project Status | Lead Researcher  |
| --------------- | -------------- | ---------------- |
| Project Chimera | Active         | Dr. Evelyn Reed  |
| Project Griffin | Active         | Dr. Kenji Tanaka |

### Tasks

#### Task 1: Create the `researchProject` custom object

To create a custom object `researchProject`:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. In the top navigation menu, click Configure > Managed Objects.

3. Click [icon: add, set=material, size=inline] New Managed Object.

   1. In the Managed Object Name field, enter "researchProject".

   2. In the Readable Title field, enter "Research Project".

   3. In the Managed Object Icon field, select an icon for the object to appear on the Managed Objects page.

   4. In the Managed Design Icon field, find an icon in the Google icon repository.

   5. In the Description field, enter a general description of the object. For example, `Stores information about active and proposed research projects`.

4. In the Managed Object/publication page, click [icon: add, set=material, size=inline] Add a property. For each property, enter or select the following:

   |                |                 |              |          |
   | -------------- | --------------- | ------------ | -------- |
   | Property Name  | Label           | Type         | Required |
   | projectName    | Project Name    | String       | Required |
   | projectID      | Project ID      | String       |          |
   | projectStatus  | Project Status  | string       |          |
   | leadResearcher | Lead Researcher | Relationship |          |

5. Click Save.

#### Task 2: Create records for each research project

To create records for each `researchProject`:

1. In the Advanced Identity Cloud admin console, navigate to Identities > Manage.

2. Click Research Projects to view the list of existing project records if any.

3. Click [icon: add, set=material, size=inline] New Research Project to open the creation form.

4. Fill in the details for the project. For example:

   * Project Name: `Project Chimera`

   * Project ID: `RC-2025-01`

   * Project Status: `Active`

   * Lead Researcher: `Evelyn Reed`

5. Click Save.

6. On the Research Project page, click Save.

7. Repeat the steps for another project:

   * Project Name: `Project Griffin`

   * Project ID: `TC-2025-01`

   * Project Status: `Active`

   * Lead Researcher: `Kenji Tanaka`

You've now created a record for the specific projects.

#### Task 3: Create the report template

1. In the Advanced Identity Cloud admin console, click [icon: plus, set=fa]New Report.

2. On the New Report modal, enter the following properties, and then click Next:

   | Field       | Description                                                                                                                                                                                                                                        |
   | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name        | Name of the report. Follow the naming conventions established by your company.                                                                                                                                                                     |
   | Description | (Optional) Enter a description of the report.                                                                                                                                                                                                      |
   | Who Can Run | Click to set who can run this report.**Groups**:- Report Viewer**Users**:- Select the users who can run this report. To select a user, you must have assigned the `report_viewer` group permissions to the user from the **Manage Identity** page. |

3. Next, add a data source or select an existing data source:

   1. Click [icon: plus, set=fa]Data Source.

   2. On the Add a Data Source modal, select a data source to use in this report, and then click Next:

   3. Select Users.

   4. On the Reports canvas, click Common Name.

4. In Related Data Sources, click Custom relationship.

   1. In the users/custom\_publication source:

      1. Click Title of the paper.

      2. Click Name of the journal.

5. Click Save.

6. Click Save.

#### Task 4: Generate the report

Run the report to view the final output:

1. On the Reports page, locate your report.

2. Click Run and then Run Now.

3. On the report page, click View Report.

   ![Example of a custom object relationship for a custom object to out-of-the-box IDM object.](../_images/custom-objects-use-case-3-report.png)

## Use case 4: Relate a custom object to another custom object.

In this use case, you link two different custom objects. This is useful when you need to model complex business processes that involve multiple types of unique data that don't exist in the standard identity schema.

### Scenario

Continuing with the AI Research company example, you need to track not only the research projects but also specialized, high-cost equipment allocated to each project. You can achieve this by creating a relationship between two custom objects: `researchProjectEquipment` and `specializedEquipment`.

### What you'll do

* Define the `specializedEquipment` custom object.

* Define the `researchProject` custom object, including a relationship to `specializedEquipment`.

* Create records for individual specialized equipment objects.

* Create records for research projects and link them to their allocated equipment.

* Build and run a report that joins your two custom objects.

### Before you begin

* Ensure you have administrator access to the Advanced Identity Cloud admin console.

* Verify you have access to the IDM native admin console to modify objects.

* Confirm you are familiar with the process of creating a single custom object.

### Data model

The data model for use case 4 has the following structure:

* **Custom Object `specializedEquipment`**: Define an object to track equipment details.

  * `equipmentName` (String): Name of the equipment (for example, "Quantum Computing Pod").

  * `assetTag` (String): Unique internal tracking tag.

  * `equipmentStatus` (String): Current state, such as "In Use" or "Available."

* **Custom Object `researchProjectEquipment`**: You use the same object from use case 3, but add a new relationship property.

  * `projectName` (String): Project name.

  * `projectID` (String): Unique project ID.

  * `leadResearcher` (Relationship): A link to the out-of-the-box `User` object.

  * `allocatedEquipment` (Relationship): New field to link to the `specializedEquipment` custom object.

* **Relationship**: The `allocatedEquipment` attribute on the `researchProjectEquipment` object creates a link from a project to the specific equipment it uses.

### Report model

You can create a report that joins these two custom objects to see which equipment is allocated to which project, which helps with resource management and auditing.

| Project Name    | Lead Researcher  | Allocated Equipment   |
| --------------- | ---------------- | --------------------- |
| Project Chimera | Dr. Evelyn Reed  | Quantum Computing Pod |
| Project Griffin | Dr. Kenji Tanaka | GPU Cluster B         |

### Tasks

#### Task 1: Create the `specializedEquipment` custom object

In the IDM native admin console, create a new managed object named `specializedEquipment` with the properties `equipmentName`, `assetTag`, and `equipmentStatus`.

* **Object Name**: `specialized Equipment`

* **Description**: Stores information about specialized computing hardware and lab equipment.

* **Attributes**:

  * `equipmentName` (String): Name of the equipment, for example, "Quantum Computing Pod."

  * `assetTag` (String): Unique internal tracking tag, for example, "EQUIP-QC-001."

  * `equipmentStatus` (String): Current state, such as "In Use", "Available", or "Under Maintenance."

To create a custom object `specializedEquipment`:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. In the top navigation menu, click Configure > Managed Objects.

3. Click [icon: add, set=material, size=inline] New Managed Object.

   1. In the Managed Object Name field, enter `specializedEquipment`.

   2. In the Readable Title field, enter `Specialized Equipment`.

   3. In the Managed Object Icon field, select an icon for the object to appear on the Managed Objects page.

   4. In the Managed Design Icon field, find an icon in the Google icon repository.

   5. In the Description field, enter a general description of the object. For example, `Stores the information about active and proposed research projects`.

4. In the Managed Object/publication page, click [icon: add, set=material, size=inline] Add a property. For each property, enter or select the following:

   |                 |                  |        |          |
   | --------------- | ---------------- | ------ | -------- |
   | Property Name   | Label            | Type   | Required |
   | equipmentName   | Equipment Name   | String | Required |
   | assetTag        | Asset Tag        | String |          |
   | equipmentStatus | Equipment Status | String |          |

5. Click Save.

#### Task 2: Create the `researchProjectEquipment` custom object

The `researchProjectEquipment` object has the following structure:

* **Object Name**: `researchProjectEquipment`

* **Description**: Stores the information about active and proposed research projects

* **Attributes**:

  * `projectName` (String): `Project Chimera`

  * `projectID` (String): `RC-2025-07`

  * `leadResearcher` (Relationship): A link to the out-of-the-box `User` object

  * `allocatedEquipment` (Relationship): A new field to link to the `specializedEquipment` custom object

To create a custom object `researchProjectEquipment`:

1. In the Advanced Identity Cloud admin console, click Native Consoles > Identity Management.

2. In the top navigation menu, click Configure > Managed Objects.

3. Click [icon: add, set=material, size=inline] New Managed Object.

   1. In the Managed Object Name field, enter `researchProjectEquipment`.

   2. In the Readable Title field, enter `Research Project Equipment`.

   3. In the Managed Object Icon field, select an icon for the object to appear on the Managed Objects page.

   4. In the Managed Design Icon field, find an icon in the Google icon repository.

   5. In the Description field, enter a general description of the object. For example, `Stores the information about active and proposed research projects`.

4. In the Managed Object/publication page, click [icon: add, set=material, size=inline] Add a property. For each property, enter or select the following:

   |                    |                     |              |          |
   | ------------------ | ------------------- | ------------ | -------- |
   | Property Name      | Label               | Type         | Required |
   | projectName        | Project Name        | String       | Required |
   | projectID          | Project ID          | String       |          |
   | leadResearcher     | Lead Researcher     | Relationship |          |
   | allocatedEquipment | Allocated Equipment | String       |          |

5. Click Save.

#### Task 3: Create records for specialized equipment

To create records for the `specializedEquipment` object:

1. In the Advanced Identity Cloud admin console, navigate to Identities > Manage.

2. Click Research Project Equipment to view the list of existing project records if any.

3. Click [icon: add, set=material, size=inline] New Research Project Equipment to open the creation form.

4. Fill in the details for the equipment. For example:

   * Equipment Name: `Quantum Computing`

   * Asset Tag: `EQUIP-QC-001`

   * Equipment Status: `In Use`

5. On the Research Project page, click Save.

6. Repeat the steps for another project:

7. Fill in the details for the equipment. For example:

   * Equipment Name: `GPU Cluster B`

   * Asset Tag: `EQUIP-QC-004`

   * Equipment Status: `In Use`

You've now created records for the specific equipment.

#### Task 4: Create records for the allocated equipment

To create records for the `allocatedEquipment` object:

1. In the Advanced Identity Cloud admin console, navigate to Identities > Manage.

2. Click Research Projects to view the list of existing project records if any.

3. Click [icon: add, set=material, size=inline] New Research Project to open the creation form.

4. Fill in the details for the project. For example:

   * Project Name: `Project Chimera`

   * Project ID: `RC-2025-07`

   * Lead Researcher: `Evelyn Reed`

   * Allocated Equipment: Quantum Computing Pod

5. Click Save.

6. On the Research Project page, click Save.

7. Repeat the steps for another project:

   * Project Name: `Project Griffin`

   * Project ID: `TC-2025-01`

   * Lead Researcher: `Kenji Tanaka`

   * Allocated Equipment: GPU Cluster B

You've now created a record for the specific equipment.

#### Task 5: Create the report template

1. In the Advanced Identity Cloud admin console, click [icon: plus, set=fa]New Report.

2. On the New Report modal, enter the following properties, and then click Next:

   | Field       | Description                                                                                                                                                                                                                                        |
   | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | Name        | Name of the report. Follow the naming conventions established by your company.                                                                                                                                                                     |
   | Description | (Optional) Enter a description of the report.                                                                                                                                                                                                      |
   | Who Can Run | Click to set who can run this report.**Groups**:- Report Viewer**Users**:- Select the users who can run this report. To select a user, you must have assigned the `report_viewer` group permissions to the user from the **Manage Identity** page. |

3. Next, add a data source or select an existing data source:

   1. Click [icon: plus, set=fa]Data Source.

   2. On the Add a Data Source modal, select a data source to use in this report, and then click Next:

   3. Select Research Project Equipment.

   4. On the Reports canvas, click Project Name.

4. In Related Data Sources, click Lead Researcher.

   1. In the researchProjectEquipment/allocatedEquipment source, click Equipment Name.

5. In Related Data Sources, click Allocated Equipment.

   1. In the researchProjectEquipment/allocatedEquipment source, click Equipment Name.

6. Click Save.

7. Click Save.

#### Task 6: Generate the report

Run the report to view the final output:

1. On the Reports page, locate your report.

2. Click Run and then Run Now.

3. On the report page, click View Report.

   ![Example of a custom object relationship for out-of-the-box IDM object to a custom object.](../_images/custom-objects-use-case-4-report.png)

---

---
title: Important points about reports
description: Key considerations for creating and managing reports in Advanced Identity Cloud
component: pingoneaic
page_id: pingoneaic:reports:administration/reports-important-points
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/administration/reports-important-points.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Important points about reports

The following are important tips and points to know about Advanced Identity Cloud reports:

* **Out-of-the-box reports**: There are 15 [out-of-the-box reports](analytic-reports.html#available-reports) available to your company. Nineteen additional reports are available for those who have the Identity Governance\[[1](#_footnotedef_1 "View footnote.")] service. Tenant administrators can access and run the out-of-the-box reports.

* **Report states**: Each report has two states:

  * `Draft`: A staging state to validate a report before publishing. You must publish a report to make it live.

  * `Published`: A published report is read-only and live.

* **Report creation**: You can create reports using the following:

  * Reports page: An intuitive extension to the Advanced Identity Cloud admin console

  * REST APIs

* **Report formats**: You can export reports in JSON or CSV format.

* **Report results**: For out-of-the-box reports, the backend streams events at set intervals, for example, 15 and 45 minutes, which could cause a delay in the report results. For near real-time reporting, learn about the [Advanced Reporting](advanced-reports.html) feature.

* **Realm support**: When a user logs into a specific realm and selects the `User` identity object in Advanced Reporting, the `User` attributes are specific to the `Alpha` realm.

* **Query data restrictions**: Tenant administrators can only query data from the most recent 30 days for certain reports. The query limits apply to both draft and published reports.

  The 30-day data restriction applies to reports that cover the following AM entities and some IDM operations:

  * Journeys

  * Nodes

  * AM access attempts

  * AM access outcomes

  * IDM synchronization

  * IDM reconciliation

  Reports that cover the following topics are *excluded* from the query limit restrictions:

  * Identities and their attributes

  * Relationships like entitlements, roles, organizations (current state or historical snapshots)

  |   |                                                                                                                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Reports covering the current state of an object and its relationships are always available, even if changes or assignments occurred before the restricted query period. However, if a report requires a history change trail, the query limitation will apply. |

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you see an error message stating:"Report run failed. Report run failed with the errors \[Custom quota exceeded: Your usage exceeded the custom quota for QueryUsagePerDay, which is set by your administrator.]"Advanced Identity Cloud's reports have high query limits, so customers are unlikely to encounter this error. Ping Identity enforces fair usage policies to prevent excessive or unnecessary use of certain features. Typically, this error occurs when fair usage limits are exceeded, resulting in temporary query restrictions. If you see this error, please contact your Ping Identity representative. |

* **Duplicate functionality**: You can duplicate some reports to create variations. Learn more in [Duplicate report](analytic-reports.html#duplicate-report).

* **Download limits**: Ping Identity limits downloads to 10,000 rows per download. This helps maintain system performance and reduces security risks associated with large data downloads. If your report uses timestamps, the download includes only the most recent 10,000 entries.

  |   |                                                                                                                                |
  | - | ------------------------------------------------------------------------------------------------------------------------------ |
  |   | If you require more data, apply filters (date ranges, categories, or other properties) to define your report before exporting. |

***

[1](#_footnoteref_1). Identity Governance is an add-on capability to Advanced Identity Cloud. Contact your Ping Identity representative if you want to add PingOne® Identity Governance to your Advanced Identity Cloud subscription.

---

---
title: Manage reports
description: Generate pre-configured and custom reports on identity access, journeys, and managed objects
component: pingoneaic
page_id: pingoneaic:reports:administration/analytic-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/administration/analytic-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["Identity Cloud", "reports"]
section_ids:
  generate-view-reports: Generate and view reports using the Advanced Identity Cloud admin console
  run-new-report: Run and view a report
  available-reports: Available reports
  application-access-report-oauth-report: Application access for OAuth report
  tenant-admin-initiated-entity-type-changes-report: Tenant admin initiated entity type changes report
  idm-sync-error-report: IDM sync error report
  user-count-by-activity-report: User count by activity report
  user-count-by-status-report: User count by status report
  user-last-login-report: User last login report
  user-current-access-report: User current access report
  journey-usage-report: Journey usage report
  user-journey-usage-report: User journey usage report
  journey-node-usage-report: Journey node usage report
  user-journey-history-report: User journey history report
  journey-node-history-report: Journey node history report
  role-composition-report: Role composition report
  role-membership-report: Role membership report
  org-membership-report: Organization membership report
  duplicate-report: Duplicate report
  run_report_duplication: Run report duplication
---

# Manage reports

## Generate and view reports using the Advanced Identity Cloud admin console

Use the Advanced Identity Cloud admin console reports page to generate the pre-configured reports or run a history for a particular reporting run.

### Run and view a report

1. Log in to the Advanced Identity Cloud, and then click Reports.

2. Select a report, and then click Run.

3. For a specific report, enter or select the parameter values in the report.

4. Click Run Report.

5. Click the Run History tab, do the following:

   * Click View Report to view the report.

   * Click [icon: arrow-down-to-bracket, set=fa]to export the report as JSON or CSV.

   * Click the ellipsis ([icon: ellipsis, set=fa]), and then click Run Details to view information about the reporting run.

     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
     | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | After you generate a report, the report is available for download and view for 24 hours. If you have downloaded the report, the same report is available for additional downloads for 30 days.Data is stored in the Advanced Identity Cloud for 30 days for general Advanced Identity Cloud customers. For customers who have the advanced reporting add-on capability, application report data is stored for 90 days.You can download reports with up to 10,000 rows. Reports exceeding this limit cause a download error. |

     ![Run history page](../_images/reports-download-button.png)

     * 1 Started: Date and time the reporting run started.

     * 2 Status: If the reporting run is successful, the Status displays `Complete`; if it fails, `Error`.

     * 3 Click View Report to open it.

     * 4 Click the download icon ([icon: arrow-down-to-bracket, set=fa]) to export the report as JSON or CSV.

     * 5 Click ellipsis ([icon: ellipsis, set=fa]) to view the run history details.

## Available reports

Advanced Identity Cloud provides the following out-of-the-box report types:

**Activity**:

* [Application access for OAuth report](#application-access-report-oauth-report)

* [Tenant admin initiated entity type changes report](#tenant-admin-initiated-entity-type-changes-report)

* [IDM sync error report](#idm-sync-error-report)

**End user insights**:

* [User count by activity report](#user-count-by-activity-report)

* [User count by status report](#user-count-by-status-report)

* [User last login report](#user-last-login-report)

* [User current access report](#user-current-access-report)

**Journey**:

* [Journey usage report](#journey-usage-report)

* [User journey usage report](#user-journey-usage-report)

* [Journey node usage report](#journey-node-usage-report)

* [User journey history report](#user-journey-history-report)

* [Journey node history report](#journey-node-history-report)

**Managed object**:

* [Role composition report](#role-composition-report)

* [Role membership report](#role-membership-report)

* [Organization membership report](#org-membership-report)

**Governance**\[[1](#_footnotedef_1 "View footnote.")]:

* [Identity Governance Reports](../../identity-governance/administration/iga-reports.html)

### Application access for OAuth report

The application access for OAuth report provides a history of who and how many users accessed an application associated with an OAuth2 client in the realm for a given time period.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report helps understand the list of users who access Advanced Identity Cloud using the access details.

|   |                                                                                                     |
| - | --------------------------------------------------------------------------------------------------- |
|   | Currently, only OAuth2 client IDs are supported. The application name cannot be used for the query. |

The report options are:

| Field                   | Description                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------- |
| **Timeframe**           | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom |
| **OAuth2 Applications** | Select one or more applications.                                                         |
| **Users**               | Select one or more users who accessed the application.                                   |

The report output contains the following columns:

| Field                   | Description                                        |
| ----------------------- | -------------------------------------------------- |
| **OAuth2 Applications** | Select OAuth2 application(s) for the report.       |
| **Users**               | Select users for the report.                       |
| **Report From**         | Start date for the report range.                   |
| **Report To**           | End date for the report range.                     |
| **Event Time**          | Date and time when the application was accessed.   |
| **User Name**           | Selected username for the report.                  |
| **User Id**             | UUID of the user who access the application.       |
| **Application Name**    | Selected application name for the report.          |
| **Scope**               | Scope of the authentication.                       |
| **Token Type**          | Type of access token.                              |
| **Status**              | Status of the operation:- `SUCCESSFUL`

- `FAILED` |

![Application access report](../_images/reports-application-access.png)

### Tenant admin initiated entity type changes report

The Tenant admin initiated entity type changes report provides detailed, business-friendly insights into changes made by tenant administrators. The report provides clearer tracking of changes made by tenant administrators, for example, understanding exactly who updated a user object.

|   |                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------- |
|   | Relationship updates (for example, group, role assignments) aren't included in this report and are planned for a future release. |

|   |                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------- |
|   | The `Tenant admin initiated entity type changes` report replaces the `Tenant admin activity` report. |

The report options are:

| Field         | Description                                                                                                                             |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Admins**    | Select one or more administrators to track in the report.                                                                               |
| **Timeframe** | Select a report timeframe:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom. Select the start and end dates for the report. |

The report output contains the following columns:

| Field             | Description                                                               |
| ----------------- | ------------------------------------------------------------------------- |
| **Entity Name**   | Name of the user.                                                         |
| **Entity Type**   | Type of object. For example, the `user` identity object.                  |
| **Operation**     | Type of operation. Supported operations: `PATCH`, `CREATE`, and `DELETE`. |
| **Timestamp**     | Timestamp of the operation.                                               |
| **Tenant Admin**  | Name of the administrator running the operation.                          |
| **Message**       | A custom message built from data originating from an IDM audit event.     |
| **Changed Field** | The modified field.                                                       |
| **Before Value**  | Value of the field before the change.                                     |
| **After Value**   | Value of the field after the change.                                      |

![Tenant admin initiated entity type changes report.](../_images/tenant-admin-initiated-entity-type-changes.png)

### IDM sync error report

The IDM sync report provides an error report of user sync activities for a given time period.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report is useful to understand the errors that occurred during provisioning.

The report options are:

| Field         | Description                                                                              |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom |

The report output contains the following columns:

| Field                | Description                                          |
| -------------------- | ---------------------------------------------------- |
| **Report From**      | Selected campaign name for the report.               |
| **Report To**        | Selected status for the report.                      |
| **User Name**        | Username who ran the sync operation.                 |
| **Application Name** | Name of application for the report.                  |
| **Action**           | Type of action for the Advanced Identity Cloud sync. |
| **Message**          | Any comments attached to the reports.                |
| **Exception**        | Any exceptions discovered during the sync.           |
| **Event Time**       | Date and time of the sync event.                     |

![IDM sync error report](../_images/reports-idm-sync-error.png)

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | This report has a duplicate report functionality. Learn more in [Duplicate report](#duplicate-report). |

### User count by activity report

The user count by activity report provides a unique user count with at least one activity like sign on, set or update password, or token requests.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report can be used to understand the count of unique users interacting with Advanced Identity Cloud during go-live or new application onboarding events.

The report options are:

| Field         | Description                                                                              |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom |

The report output contains the following columns:

| Field                   | Description                                                                                           |
| ----------------------- | ----------------------------------------------------------------------------------------------------- |
| **Report From**         | Start date for the report.                                                                            |
| **Report To**           | End date for the report.                                                                              |
| **User Activity Count** | Number of unique user activity events like sign on, set or update password, or access token requests. |

![User count by activity report](../_images/reports-user-count-by-activity.png)

### User count by status report

The user count by status report provides the number of users in an active, inactive, or blocked status.

The report can be used to query on more than one status to provide an aggregated count. To get numbers for each status, run multiple reports.

The report options are:

| Field      | Description                                            |
| ---------- | ------------------------------------------------------ |
| **Status** | Select a status option:- Active

- Inactive

- Blocked |

The report output contains the following columns:

| Field      | Description                               |
| ---------- | ----------------------------------------- |
| **Status** | Selected status to include in the report. |
| **Count**  | Number of users with the selected status. |

![User count by status report](../_images/reports-user-count-by-status.png)

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | This report has a duplicate report functionality. Learn more in [Duplicate report](#duplicate-report). |

### User last login report

The user last login report lists the users in a particular status, along with their last login time.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report is based on the successful journey completion of the selected journeys. The report can be used to get the journey names designated as `login` journeys.

The report options are:

| Field         | Description                                                                              |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom |
| **Status**    | Select a status option:- Active

- Inactive

- Blocked                                   |
| **Journeys**  | Enter or select one or more journeys.                                                    |

The report output contains the following columns:

| Field              | Description                      |
| ------------------ | -------------------------------- |
| **Account Status** | Status included in the report.   |
| **Journeys**       | Journeys tracked in the report.  |
| **Report From**    | Start date for the report.       |
| **Report To**      | End date for the report.         |
| **Last Name**      | Surname of the user.             |
| **First Name**     | First name of the user.          |
| **User Name**      | Username of the user.            |
| **JourneyName**    | Journey name for the last login. |
| **Timestamp**      | Timestamp of the last login.     |

![User last login report](../_images/reports-user-last-login.png)

### User current access report

The user current access report lists a user's current assigned applications, organizations, and role assignments.

|   |                                                         |
| - | ------------------------------------------------------- |
|   | Currently, the report is only available in JSON format. |

The report options are:

| Field     | Description                                                     |
| --------- | --------------------------------------------------------------- |
| **Users** | Select one or more users who may have accessed the application. |

The report output contains the following columns:

| Field                 | Description                                              |
| --------------------- | -------------------------------------------------------- |
| **Users**             | User selected for the report.                            |
| **User Name**         | Username of the user.                                    |
| **First Name**        | First name of the user.                                  |
| **Last Name**         | Surname of the user.                                     |
| **Role Names**        | Any role names assigned to the user.                     |
| **Application Names** | Application name of the accessed resource.               |
| **Org Names**         | Organization name of the user who accesses the resource. |

![User access details report](../_images/reports-user-access-details.png)

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | This report has a duplicate report functionality. Learn more in [Duplicate report](#duplicate-report). |

### Journey usage report

The journey Usage report provides a count of the times one or more journeys completed in a period of time with a particular status.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report can be used to query on more than one outcome to provide an aggregated count. To get numbers for each outcome, run multiple reports.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report only includes information about the main journey. It doesn't include details about child/inner journeys. To view child/inner journey details, run the [Journey node history report](#journey-node-history-report). |

The report options are:

| Field         | Description                                                                                                                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom                                                                                                                                                                        |
| **Outcomes**  | Select a journey outcome:- Successful: Select journeys that ended successfully.

- Failed: Select journeys that failed.

- Continue: Select journeys that are in a pending state, such as waiting for user input in a multifactor authentication (MFA) journey. |
| **Journeys**  | Select one or more journeys for the report.                                                                                                                                                                                                                     |

The report output contains the following columns:

| Field            | Description                                                                          |
| ---------------- | ------------------------------------------------------------------------------------ |
| **Journeys**     | Journeys tracked in the report.                                                      |
| **Outcomes**     | Outcome of the journey covered in the report:- `SUCCESSFUL`

- `FAILED`

- `OUTCOME` |
| **Report From**  | Start date for the report.                                                           |
| **Report To**    | End date for the report.                                                             |
| **User Name**    | Username for the person owning the journey.                                          |
| **Journey Name** | Name of the journey.                                                                 |
| **Count**        | Number of journeys for the user.                                                     |

![Journey stats report](../_images/reports-user-journey-stats.png)

### User journey usage report

The user journey Usage report lists the number of times a user completed or did not complete a journey.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report can be used to query on more than one outcome to provide an aggregated count. To get numbers for each outcome, run multiple reports.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report only includes information about the main journey. It doesn't include details about child/inner journeys. To view child/inner journey details, run the [Journey node history report](#journey-node-history-report). |

The report options are:

| Field         | Description                                                                                                                                                                                                                                                    |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom                                                                                                                                                                       |
| **Outcomes**  | Select a journey outcome- Successful: Select journeys that ended successfully.

- Failed: Select journeys that failed.

- Continue: Select journeys that are in a pending state, such as waiting for user input in a multifactor authentication (MFA) journey. |
| **Journeys**  | Select one or more journeys for the report.                                                                                                                                                                                                                    |

The report output contains the following columns:

| Field            | Description                                                   |
| ---------------- | ------------------------------------------------------------- |
| **Journeys**     | Selected journeys included in the report.                     |
| **Outcomes**     | Selected outcomes included in the report.                     |
| **Report From**  | Start date for the report.                                    |
| **Report To**    | End date for the report.                                      |
| **Username**     | Username of the user who ran the journey.                     |
| **Journey Name** | Name of the journey.                                          |
| **Count**        | Number of times the user ran the journey successfully or not. |

![User journey stats report](../_images/reports-user-journey-stats.png)

### Journey node usage report

The journey node usage report provides the count and details of nodes traversed by a user for one or more journeys for a given time period.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report shows when a user used a journey, such as One Time Password (OTP), in a given time period and when the user last used the journey.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report only includes information about the main journey. It doesn't include details about child/inner journeys. To view child/inner journey details, run the [Journey node history report](#journey-node-history-report). |

The report options are:

| Field         | Description                                                                              |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom |
| **Journeys**  | Select one or more journeys for the report.                                              |

The report output contains the following columns:

| Field                | Description                                         |
| -------------------- | --------------------------------------------------- |
| **Journeys**         | Selected journey(s) for the report.                 |
| **Report From**      | Start date for the report.                          |
| **Report To**        | End date for the report.                            |
| **Journey Name**     | Name of the journey.                                |
| **Journey Status**   | Status of the journey.                              |
| **User Name**        | Username for the person running the report.         |
| **Node Name**        | Name of the specific node.                          |
| **Node type**        | Type of node.                                       |
| **Node Outcome**     | Outcome of the node: `true`, `false`, or `outcome`. |
| **Node Usage Count** | Number of times the node was used.                  |
| **Last Usage**       | Date and time of the latest node usage.             |

![Journey node usage report](../_images/reports-journey-node-usage.png)

### User journey history report

The user journey history report provides a history of all journeys one or more user(s) completed for a given time period.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report can be used to understand when one or more users have registered, logged in, or reset their password.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report only includes information about the main journey. It doesn't include details about child/inner journeys. To view child/inner journey details, run the [Journey node history report](#journey-node-history-report). |

The report options are:

| Field         | Description                                                                             |
| ------------- | --------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 day

- Last 30 days

- Custom |
| **Users**     | Select one or more users who may have accessed the application.                         |

The report output contains the following columns:

| Field              | Description                                                    |
| ------------------ | -------------------------------------------------------------- |
| **Users**          | Selected users for the report.                                 |
| **Report From**    | Start date for the report range.                               |
| **Report To**      | End date for the report range.                                 |
| **Users**          | Selected users for the report.                                 |
| **Journey Name**   | Name of the journey.                                           |
| **Journey Result** | Displays the result of the journey: `SUCCESSFUL` or `FAILURE`. |
| **Timestamp**      | Date and time for the journey.                                 |

![Journey history report](../_images/reports-journey-history.png)

### Journey node history report

The journey node history report provides a history of a user's journey and nodes traversed for a given time period.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | This report has a data query limit depending on your add-on capabilities:- Customers using out-of-the-box reports: Reports cover the latest 30 days.

- Customers who have the Advanced Reporting add-on capability: Reports cover the latest 90 days. |

The report can be used to understand login or churn issues. To understand a user's journeys and node traversal history, download the report and filter on the user.

The report options are:

| Field         | Description                                                                              |
| ------------- | ---------------------------------------------------------------------------------------- |
| **Timeframe** | Select a report time frame:- Today

- Yesterday

- Last 7 days

- Last 30 days

- Custom |
| **Journeys**  | Select one or more journeys for the report.                                              |

The report output contains the following columns:

| Field              | Description                                                                                                                                                                                                                                                       |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Journeys**       | Selected journey(s) for the report.                                                                                                                                                                                                                               |
| **Report From**    | Start date for the report.                                                                                                                                                                                                                                        |
| **Report To**      | End date for the report.                                                                                                                                                                                                                                          |
| **Tracking Id**    | Tracking ID for the journey.                                                                                                                                                                                                                                      |
| **Journey Name**   | Name of the journey.                                                                                                                                                                                                                                              |
| **Journey Status** | Selected journey status.                                                                                                                                                                                                                                          |
| **User Name**      | Username for the person running the report.                                                                                                                                                                                                                       |
| **Timestamp**      | Date and time.                                                                                                                                                                                                                                                    |
| **Node Details**   | Node details used in the journeys:- **Node Type**. Type of node in the journey.

- **Node Name**. Name of the node in the journey.

- **Node Event Time**. Date and time of the node event.

- **Node Outcome**. Outcome of the node, depending on the node type. |

![Journey node history report](../_images/reports-journey-node-history.png)

### Role composition report

The role composition report provides a list of roles and their metadata.

| Field    | Description                       |
| -------- | --------------------------------- |
| **None** | Click Run to generate the report. |

The report output contains the following columns:

| Field                    | Description                                         |
| ------------------------ | --------------------------------------------------- |
| **Role Name**            | Name of the role.                                   |
| **Description**          | Description for the role.                           |
| **Temporal Constraints** | Any time-limited constraints for the assigned role. |

![Role composition report](../_images/reports-role-composition.png)

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | This report has a duplicate report functionality. Learn more in [Duplicate report](#duplicate-report). |

### Role membership report

The role membership report provides a list of roles and their associated members.

The report options are:

| Field     | Description                             |
| --------- | --------------------------------------- |
| **Roles** | Enter one or more roles for the report. |

The report output contains the following columns:

| Field          | Description                                  |
| -------------- | -------------------------------------------- |
| **Roles**      | Selected roles for the report.               |
| **Role Name**  | Name of the role.                            |
| **User Name**  | Username of the user assigned the role.      |
| **First Name** | First name of the user assigned the role.    |
| **Last Name**  | Surname of the user assigned the role.       |
| **Email**      | Email address of the user assigned the role. |

![Role membership report](../_images/reports-role-membership.png)

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | This report has a duplicate report functionality. Learn more in [Duplicate report](#duplicate-report). |

### Organization membership report

The organization membership report provides a list of the organizations in your company and their associated members.

The report options are:

| Field             | Description                      |
| ----------------- | -------------------------------- |
| **Organizations** | Enter one or more organizations. |

The report output contains the following columns:

| Field             | Description                                    |
| ----------------- | ---------------------------------------------- |
| **Organizations** | Selected organizations for the report.         |
| **Org Name**      | Name of the organization.                      |
| **User Name**     | Username of a user in the organization.        |
| **First Name**    | First name of user in the organization.        |
| **Last Name**     | Surname of the user in the organization.       |
| **Email**         | Email address of the user in the organization. |

![Organization membership report](../_images/reports-org-users-report.png)

|   |                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------ |
|   | This report has a duplicate report functionality. Learn more in [Duplicate report](#duplicate-report). |

### Duplicate report

You can use this report to create a duplicate, which you can then customize to support different report variations. The following reports provide the duplicate functionality:

* [IDM-SYNC-ERROR](#idm-sync-error-report)

* [ORG-USERS-REPORT](#org-membership-report)

* [ROLE-COMPOSITION](#role-composition-report)

* [ROLE-MEMBERSHIP](#role-membership-report)

* [USER-ACCESS-DETAILS](#user-current-access-report)

* [USER-COUNT-BY-STATUS](#user-count-by-status-report)

#### Run report duplication

1. Log in to the Advanced Identity Cloud, and then click Reports.

2. Select the report you want to duplicate.

3. Click the ellipsis ([icon: ellipsis, set=fa]), and then click Duplicate to create a copy of the report.

   1. In the Duplicate Report modal, enter the following:

      * Name: Enter a name of the duplicated report.

      * \[.label]Description (optional)#: Enter a description of the duplicated report.

      * \[.label]Who Can Run#: Select the users who can run the report.

      * \[.label]Groups#: Click Report Viewer Group to limit users in the `report_viewer` group who can run the report.

   2. Click Duplicate.

4. In the duplicated draft of the report page, create a variation of the report by clicking properties in the Settings pane. To rename the report or change the report details, click the Details tab and change the report details.

   You can also click and drag the columns to resort them.

5. Click Save.

***

[1](#_footnoteref_1). Identity Governance is an add-on capability to Advanced Identity Cloud. Contact your Ping Identity representative if you want to add PingOne® Identity Governance to your Advanced Identity Cloud subscription.

---

---
title: Report for two-factor authentication
description: Create reports exposing two-factor authentication device profiles and authentication methods
component: pingoneaic
page_id: pingoneaic:reports:administration/reports-2FA-profile-attributes
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/administration/reports-2FA-profile-attributes.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["release-notes:rapid-channel/reports-2FA-profile-attributes.adoc"]
section_ids:
  create_a_two_factor_authentication_report: Create a two-factor authentication report
---

# Report for two-factor authentication

Advanced Identity Cloud enhances reporting capabilities by exposing multivalue two-factor authentication (2FA) profile attributes for user identities. You can create reports that include details about your users' 2FA configurations, such as which authentication methods they have registered and when they were last used. This feature provides administrators with greater visibility into 2FA adoption and helps ensure compliance with security policies.

The multivalue 2FA profile attributes are:

* **Device profiles**: Contains general information about the devices a user has registered for authentication.

* **Device print profiles**: Stores unique fingerprints of user devices to help recognize them during authentication.

* **Web authentication device profiles**: Manages devices that use biometrics or security keys for passwordless authentication through the Web Authentication (WebAuthn) standard.

* **Oath device profiles**: Manages devices registered to generate one-time passwords (OTP) for authentication.

* **Push device profiles**: Manages devices that receive push notifications for you to approve or deny login attempts.

Learn more at [Multivalue 2FA profile attributes](../../identities/user-identity-properties-attributes-reference.html#multivalue-2fa).

## Create a two-factor authentication report

Create a custom report for two-factor authentication using the Advanced Reporting feature:

1. In the Advanced Identity Cloud admin console, go to Reports.

2. Click [icon: add, set=material, size=inline] New Report. The New Report modal appears.

   1. On the New Report modal, enter the following:

      * Name: Enter a descriptive name for the new report.

      * Description (optional): Enter a general description for the report.

      * Who can run: Select Users.

   2. Click Next.

3. Click [icon: add, set=material, size=inline] Data Source.

   1. On the Add a Data Source modal, select Users and click Next.

   2. On the draft report page, select the properties in the right column that you want to appear in the report. For example, select the following:

      * Username

      * Device Profiles

      * Device Print Profiles

      * Web AuthN Device Profile

      * Oath Device Profiles

      * Push Device Profiles

        |   |                                                                                   |
        | - | --------------------------------------------------------------------------------- |
        |   | You can rearrange the columns by dragging and dropping them in the desired order. |

   3. Click Save.

4. On the Reports page, locate your custom report and click Run.

   1. On your report page, click Run Now.

   2. After your report has generated, click View Report.

   3. Review your report. If you're satisfied with the results, click the ellipsis ([icon: more_horiz, set=material, size=inline]) > Publish to activate it.

      ![An example of a generated custom report tracking two-factor authentication.](../_images/reports-2fa.png)

---

---
title: Reports API
description: Use REST API endpoints to programmatically create, run, and manage report templates
component: pingoneaic
page_id: pingoneaic:reports:rest-api/reports-api
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/rest-api/reports-api.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
section_ids:
  download_postman_and_import_the_reports_collection: Download Postman and import the reports collection
  token-request: Token request
  general_endpoints: General endpoints
  create-a-report: Create a report
  publish-report: Publish a report
  get-all-templates: Get all templates
  delete-a-report: Delete a report
  duplicate-a-report: Duplicate a report
  edit-a-report: Edit a report
  update-a-report: Update a report
  run-report: Run report
  view-report: View report
  download-report: Download report
  import-report: Import a new report
  export-the-report: Export the report
  role_and_organization_reports_endpoints: Role and organization reports endpoints
  run-template-org-users: Run template - organization membership report
  view-report-result-org-users: View report result - organization membership report
  run-template-role-composition: Run template - role composition report
  view-result-role-composition: View result - role composition report
  run-template-role-membership: Run template - role membership report
  view-results-role-membership: View results - role membership report
  journey_reports_endpoints: Journey reports endpoints
  run-template-journey-stats: Run template - journey stats report
  view-report-result-journey-stats: View report result - journey stats report
  run-template-user-journey-stats: Run template - user journey stats report
  view-report-result-user-journey-stats: View report result - user journey stats report
  end_user_insights_reports_endpoints: End user insights reports endpoints
  run-template-user-last-login: Run template - user last login report
  view-result-user-last-login: View result - user last login report
  run-template-user-access-details: Run template - user access details report
  view-results-user-access-details: View results - user access details report
  run-template-user-count-by-status: Run template - user count by status report
  view-results-user-count-by-status: View results - user count by status report
  run-template-user-normal-view: Run template - user normal view report
  view-report-result-user-normal-view: View report - user normal view report
  governance1_reports_endpoints: Governance[1] reports endpoints
  run-template-certification-details: Run template - certification details report
  view-result-certification-details: View result - certification details report
  run-template-campaign-decision: Run template - campaign decision report
  view-result-campaign-decision: View result - campaign decision report
---

# Reports API

The Reports API provides a comprehensive set of endpoints to manage the entire lifecycle of your reports. You can programmatically create, read, update, and delete report templates.

The API also enables you to import and export templates, which simplifies moving report configurations between different environments.

Once a template is ready, you can run the report, check the status of the execution job, and then view or download the results.

## Download Postman and import the reports collection

The Reports Postman collection provides a set of pre-configured requests that you can use to interact with the Reports API.

1. Download and install the [Postman application](https://www.postman.com/downloads/).

2. Download the [Reports Q3 Postman collection](../_attachments/reports-Q3.postman_collection_20250917.json).

3. Download the [Reports Q3 Postman environment](../_attachments/reports-Q3.postman_environment_20250917.json).

4. In Postman:

   1. Go to File > Import... > Upload Files.

   2. Browse to the collection JSON file you downloaded in the previous step, and then click Open.

   3. Click Import to bring the collection and environment into your workspace. Make sure to change your environment variables to match your tenant.

## Token request

You need a service account to allow the requests in the collection to connect to your Advanced Identity Cloud tenant. You also need an access token to use each reports endpoint.

You can obtain a service account and an access token by following the instructions in [Get an access token](../../developer-docs/authenticate-to-rest-api-with-access-token.html).

|   |                                                                                                                                                                                                    |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The service account must have the `fr:idc:analytics:*` scope to use the Reports API endpoints. Learn more in [Service account scopes](../../tenants/service-accounts.html#service-account-scopes). |

## General endpoints

### Create a report

A POST request to `/reports/templates?_action=create` to generate a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates?_action=create' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access-token>' \
--data '
{
    "reportTemplate": {
        "displayName": "rain report",
        "description": "rain report",
        "version": 2,
        "reportConfig": "{\"version\":\"v2\",\"entities\":[{\"entity\":\"users\"}],\"fields\":[{\"label\":\"City\",\"value\":\"users.city\"},{\"label\":\"Country\",\"value\":\"users.country\"}]}",
        "ootb": true,
        "editable": true,
        "duplicatable": true,
        "visible": true,
        "viewers": []
    }
}'
```

**Query parameters**

| Name      | Required | Example  | Schema |
| --------- | -------- | -------- | ------ |
| `_action` | true     | `create` | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |
| `Content-Type`       | false    | `application/json`      | string |

**Body parameters**

| Name                          | Required | Example                                                                                                                                      | Schema |
| ----------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| `reportTemplate`              | true     |                                                                                                                                              | object |
| `reportTemplate.description`  | false    | `""`                                                                                                                                         | string |
| `reportTemplate.viewers`      | false    | `[]`                                                                                                                                         | array  |
| `reportTemplate.displayName`  | true     | `report-name`                                                                                                                                | string |
| `reportTemplate.reportConfig` | true     | `{\"version\":\"v2\",\"entities\":[{\"entity\":\"accounts\"}],\"fields\":[{\"label\":\"Account Data\",\"value\":\"accounts.accountData\"}]}` | string |
| `reportTemplate.name`         | true     | `5CAAC80A-0A64-4C1C-BC75-1529A12E43B5`                                                                                                       | string |

### Publish a report

A POST request to `/reports/templates/REPORT-UUID?_action=publish` to publish a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/REPORT-UUID?_action=publish' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name          | In   | Required | Example       | Schema |
| ------------- | ---- | -------- | ------------- | ------ |
| `REPORT-UUID` | path | true     | `REPORT-UUID` | string |

**Query parameters**

| Name      | In    | Required | Example   | Schema |
| --------- | ----- | -------- | --------- | ------ |
| `_action` | query | false    | `publish` | string |

### Get all templates

A GET request to `/reports/templates?templateType=draft` to get all report templates.

Curl example

```
curl --location --request GET 'https://<tenant-env-fqdn>/reports/templates?templateType=draft' \
--header 'Authorization: Bearer <access-token>' \
--header "Accept-API-Version: resource=1.0"
```

**Query parameters**

| Name           | In    | Required | Example | Schema |
| -------------- | ----- | -------- | ------- | ------ |
| `templateType` | query | false    | `draft` | string |

**Header parameters**

| Name                 | In     | Required | Example                 | Schema |
| -------------------- | ------ | -------- | ----------------------- | ------ |
| `Accept-API-Version` | header | false    | `resource=1.0`          | string |
| `Authorization`      | header | false    | `Bearer <access-token>` | string |

### Delete a report

A POST request to `/reports/templates/REPORT-UUID?_action=delete&templateType=draft` to delete a report template.

Curl example

```
curl --location --request GET 'https://<tenant-env-fqdn>/reports/templates/REPORT-UUID?_action=delete&templateType=draft' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Query parameters**

| Name           | In    | Required | Example  | Schema |
| -------------- | ----- | -------- | -------- | ------ |
| `_action`      | query | false    | `delete` | string |
| `templateType` | query | false    | `draft`  | string |

**Header parameters**

| Name                 | In     | Required | Example                 | Schema |
| -------------------- | ------ | -------- | ----------------------- | ------ |
| `Accept-API-Version` | header | false    | `resource=1.0`          | string |
| `Authorization`      | header | false    | `Bearer <access-token>` | string |

### Duplicate a report

A POST request to `/reports/templates/REPORT-UUID?_action=duplicate` to duplicate a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/REPORT-UUID?_action=duplicate&templateType=draft' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <access-token>' \
--data-raw '{
    "reportTemplate": {
        "description": "",
        "name": "",
        "viewers": [],
        "displayName": "reportTest12356"
    }
}'
```

**Path parameters**

| Name          | Required | Example       | Schema |
| ------------- | -------- | ------------- | ------ |
| `REPORT-UUID` | true     | `REPORT-UUID` | string |

**Query parameters**

| Name           | Required | Example     | Schema |
| -------------- | -------- | ----------- | ------ |
| `_action`      | true     | `duplicate` | string |
| `templateType` | true     | `draft`     | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Content-Type`       | false    | `application/json`      | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

**Body parameters**

| Name                         | Required | Example           | Schema |
| ---------------------------- | -------- | ----------------- | ------ |
| `reportTemplate`             | true     |                   | object |
| `reportTemplate.displayName` | true     | `reportTest12356` | string |
| `reportTemplate.description` | false    | `""`              | string |
| `reportTemplate.name`        | false    | `""`              | string |
| `reportTemplate.viewers`     | false    | `[]`              | array  |

### Edit a report

A POST request to `/reports/templates/REPORT-UUID?_action=edit` to edit a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/REPORT-UUID?_action=edit' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name          | Required | Example       | Schema |
| ------------- | -------- | ------------- | ------ |
| `REPORT-UUID` | true     | `REPORT-UUID` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | true     | `edit`  | string |

**Header parameters**

| Name            | Required | Example                 | Schema |
| --------------- | -------- | ----------------------- | ------ |
| `Authorization` | false    | `Bearer <access-token>` | string |

### Update a report

A POST request to `/reports/templates` to update a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates?_action=update&templateType=draft' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>' \
--header 'Content-Type: application/json' \
--data-raw '{
    "reportTemplate": {
        "description": "",
        "viewers": [],
        "displayName": "11thaugv2   ",
        "reportConfig": "{\\\"version\\\":\\\"v2\\\",\\\"entities\\\":[{\\\"entity\\\":\\\"accounts\\\"}],\\\"fields\\\":[{\\\"label\\\":\\\"Account Data\\\",\\\"value\\\":\\\"accounts.accountData\\\"}]}",
        "name": "5CAAC80A-0A64-4C1C-BC75-1529A12E43B5"
    }
}'
```

**Query parameters**

| Name           | Required | Example  | Schema |
| -------------- | -------- | -------- | ------ |
| `_action`      | true     | `update` | string |
| `templateType` | true     | `draft`  | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |
| `Content-Type`       | false    | `application/json`      | string |

**Body parameters**

| Name                          | Required | Example                                                                                                                                      | Schema |
| ----------------------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| `reportTemplate`              | true     |                                                                                                                                              | object |
| `reportTemplate.description`  | false    | `""`                                                                                                                                         | string |
| `reportTemplate.viewers`      | false    | `[]`                                                                                                                                         | array  |
| `reportTemplate.displayName`  | true     | \`11thaugv2 \`                                                                                                                               | string |
| `reportTemplate.reportConfig` | true     | `{\"version\":\"v2\",\"entities\":[{\"entity\":\"accounts\"}],\"fields\":[{\"label\":\"Account Data\",\"value\":\"accounts.accountData\"}]}` | string |
| `reportTemplate.name`         | true     | `5CAAC80A-0A64-4C1C-BC75-1529A12E43B5`                                                                                                       | string |

### Run report

A POST request to `/reports/templates/REPORT-UUID?_action=run&templateType=published` to run a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/REPORT-UUID?_action=run&templateType=published' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>' \
--data '
{
    "parameters": "{}",
    "context": [
        {
            "type": "global",
            "data": [
                {
                    "key": "realm",
                    "value": "alpha"
                }
            ]
        }
    ]
}'
```

**Path parameters**

| Name          | Required | Example       | Schema |
| ------------- | -------- | ------------- | ------ |
| `REPORT-UUID` | true     | `REPORT-UUID` | string |

**Query parameters**

| Name           | Required | Example     | Schema |
| -------------- | -------- | ----------- | ------ |
| `_action`      | true     | `run`       | string |
| `templateType` | true     | `published` | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View report

A POST request to `/reports/templates/JOB-ID?_action&_pageSize=10&_pagedResultsOffset=0&name=REPORT-UUID&templateType=published` to view a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/JOB-ID?_action&_pageSize=10&_pagedResultsOffset=0&name=REPORT-UUID&templateType=published' \
--header "Accept-API-Version: resource=1.0" \
--header "Authorization: Bearer <access-token>"
```

**Path parameters**

| Name          | Required | Example       | Schema |
| ------------- | -------- | ------------- | ------ |
| `REPORT-UUID` | true     | `REPORT-UUID` | string |

**Query parameters**

| Name                  | Required | Example       | Schema |
| --------------------- | -------- | ------------- | ------ |
| `_action`             | true     | `view`        | string |
| `_pageSize`           | false    | `10`          | string |
| `_pagedResultsOffset` | false    | `0`           | string |
| `name`                | true     | `REPORT-UUID` | string |
| `templateType`        | true     | `published`   | string |

**Header parameters**

| Name                 | Required | Example        | Schema |
| -------------------- | -------- | -------------- | ------ |
| `Accept-API-Version` | false    | `resource=1.0` | string |

### Download report

A POST request to `/reports/runs/JOB-ID?_action=download&name=REPORT-UUID&format=csv` to download a report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/JOB-ID?_action=download&name=REPORT-UUID&format=csv' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name          | Required | Example       | Schema |
| ------------- | -------- | ------------- | ------ |
| `REPORT-UUID` | true     | `REPORT-UUID` | string |

**Query parameters**

| Name      | Required | Example       | Schema |
| --------- | -------- | ------------- | ------ |
| `_action` | true     | `download`    | string |
| `name`    | true     | `REPORT-UUID` | string |
| `format`  | true     | `csv`         | string |

**Header parameters**

| Name                 | Required | Example        | Schema |
| -------------------- | -------- | -------------- | ------ |
| `Accept-API-Version` | false    | `resource=1.0` | string |

### Import a new report

A POST request to `/reports/templates/import` to import a new report.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Importing and exporting report templates is only applicable to custom report templates. Administrators can export both draft and published templates. |

Curl example

```
curl \
--location \
https://<tenant-env-fqdn>/reports/templates/import' \
--header 'Content-Type: application/json, text/plain, */\*' \
--header 'Accept-API-version: resource=1.0' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Bearer <access-token>' \
--form 'file=@"/path/to/report/New_draft"'
```

**Header parameters**

| Name                 | In     | Required | Example                 | Schema |
| -------------------- | ------ | -------- | ----------------------- | ------ |
| `Accept-API-Version` | header | true     | `resource=1.0`          | string |
| `accept-language`    | header | true     | `en-US,en;q=0.9`        | string |
| `Authorization`      | header | true     | `Bearer <access-token>` | string |
| `Content-Type`       | header | true     | `application/json`      | string |

### Export the report

A POST request to `/reports/templates/REPORT-UUID?templateType=draft&_action=export` to export a report.

|   |                                                                                                                                                       |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Importing and exporting report templates is only applicable to custom report templates. Administrators can export both draft and published templates. |

Curl example

```
curl \
--request POST \
'https://<tenant-env-fqdn>/reports/templates/A1C07D0B-49C9-48C6-B225-CE05F27A5DEE?templateType=draft&_action=export' \
--header 'Content-Type: application/json, text/plain, */\*' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Accept-Language: en-US,en;q=0.9' \
--header 'Authorization: Bearer <access-token>' \
--data ''
```

**Path parameters**

| Name          | Required | Example       | Schema |
| ------------- | -------- | ------------- | ------ |
| `REPORT-UUID` | true     | `REPORT-UUID` | string |

**Query parameters**

| Name           | Required | Example  | Schema |
| -------------- | -------- | -------- | ------ |
| `templateType` | false    | `draft`  | string |
| `_action`      | false    | `export` | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Accept-API-Version` | true     | `resource=1.0`          | string |
| `Authorization`      | true     | `Bearer <access-token>` | string |
| `Content-Type`       | true     | `application/json`      | string |

## Role and organization reports endpoints

### Run template - organization membership report

A POST request to `/reports/templates/ORG-USERS-REPORT-NAME` to run an organization membership report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/ORG-USERS-REPORT-NAME?_action=run' \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=1.0" \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                    | Required | Example                 | Schema |
| ----------------------- | -------- | ----------------------- | ------ |
| `ORG-USERS-REPORT-NAME` | true     | `ORG-USERS-REPORT-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View report result - organization membership report

A POST request to `/reports/runs/ORG-USERS-REPORT-JOB-ID` to view the organization users report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/ORG-USERS-REPORT-JOB-ID?_action=view&name=ORG-USERS-REPORT-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                      | Required | Example                   | Schema |
| ------------------------- | -------- | ------------------------- | ------ |
| `ORG-USERS-REPORT-JOB-ID` | true     | `ORG-USERS-REPORT-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                 | Schema  |
| ----------- | -------- | ----------------------- | ------- |
| `_action`   | false    | `view`                  | string  |
| `name`      | false    | `ORG-USERS-REPORT-NAME` | string  |
| `_pageSize` | false    | `10`                    | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### Run template - role composition report

A POST request to `/reports/templates/ROLE-COMPOSITION-NAME` to run a role composition report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/ROLE-COMPOSITION-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                    | Required | Example                 | Schema |
| ----------------------- | -------- | ----------------------- | ------ |
| `ROLE-COMPOSITION-NAME` | true     | `ROLE-COMPOSITION-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View result - role composition report

A POST request to `/reports/runs/ROLE-COMPOSITION-JOB-ID` to view a role composition report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/ROLE-COMPOSITION-JOB-ID?_action=view&name=ROLE-COMPOSITION-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                      | Required | Example                   | Schema |
| ------------------------- | -------- | ------------------------- | ------ |
| `ROLE-COMPOSITION-JOB-ID` | true     | `ROLE-COMPOSITION-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                 | Schema  |
| ----------- | -------- | ----------------------- | ------- |
| `_action`   | false    | `view`                  | string  |
| `name`      | false    | `ROLE-COMPOSITION-NAME` | string  |
| `_pageSize` | false    | `10`                    | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### Run template - role membership report

A POST request to `/reports/templates/ROLE-MEMBERSHIP-NAME` to run a role membership report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/ROLE-MEMBERSHIP-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                   | Required | Example                | Schema |
| ---------------------- | -------- | ---------------------- | ------ |
| `ROLE-MEMBERSHIP-NAME` | true     | `ROLE-MEMBERSHIP-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View results - role membership report

A POST request to `/reports/runs/ROLE-MEMBERSHIP-JOB-ID` to view role membership report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/ROLE-MEMBERSHIP-JOB-ID?_action=view&name=ROLE-MEMBERSHIP-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                     | Required | Example                  | Schema |
| ------------------------ | -------- | ------------------------ | ------ |
| `ROLE-MEMBERSHIP-JOB-ID` | true     | `ROLE-MEMBERSHIP-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                | Schema  |
| ----------- | -------- | ---------------------- | ------- |
| `_action`   | false    | `view`                 | string  |
| `name`      | false    | `ROLE-MEMBERSHIP-NAME` | string  |
| `_pageSize` | false    | `10`                   | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

## Journey reports endpoints

### Run template - journey stats report

A POST request to `/reports/templates/JOURNEY-STATS-NAME` to run a journey stats report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/JOURNEY-STATS-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                 | Required | Example              | Schema |
| -------------------- | -------- | -------------------- | ------ |
| `JOURNEY-STATS-NAME` | true     | `JOURNEY-STATS-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View report result - journey stats report

A POST request to `/reports/runs/JOURNEY-STATS-JOB-ID` to view a journey stats report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/JOURNEY-STATS-JOB-ID?_action=view&name=JOURNEY-STATS-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                   | Required | Example                | Schema |
| ---------------------- | -------- | ---------------------- | ------ |
| `JOURNEY-STATS-JOB-ID` | true     | `JOURNEY-STATS-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example              | Schema  |
| ----------- | -------- | -------------------- | ------- |
| `_action`   | false    | `view`               | string  |
| `name`      | false    | `JOURNEY-STATS-NAME` | string  |
| `_pageSize` | false    | `10`                 | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### Run template - user journey stats report

A POST request to `/reports/templates/USER-JOURNEY-STATS-NAME` to run a user journey stats name report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/USER-JOURNEY-STATS-NAME?_action=run' \
--header 'X-TENANT-ID: 436392a8-3ef4-11ee-be56-0242ac120002' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                      | Required | Example                   | Schema |
| ------------------------- | -------- | ------------------------- | ------ |
| `USER-JOURNEY-STATS-NAME` | true     | `USER-JOURNEY-STATS-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View report result - user journey stats report

A POST request to `/reports/runs/USER-JOURNEY-STATS-JOB-ID` to view a user journey stats report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/USER-JOURNEY-STATS-JOB-ID?_action=view&name=USER-JOURNEY-STATS-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                        | Required | Example                     | Schema |
| --------------------------- | -------- | --------------------------- | ------ |
| `USER-JOURNEY-STATS-JOB-ID` | true     | `USER-JOURNEY-STATS-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                   | Schema  |
| ----------- | -------- | ------------------------- | ------- |
| `_action`   | false    | `view`                    | string  |
| `name`      | false    | `USER-JOURNEY-STATS-NAME` | string  |
| `_pageSize` | false    | `10`                      | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

## End user insights reports endpoints

### Run template - user last login report

A POST request to `/reports/templates/USER-LAST-LOGIN-NAME` to run a user last login name report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/USER-LAST-LOGIN-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                   | Required | Example                | Schema |
| ---------------------- | -------- | ---------------------- | ------ |
| `USER-LAST-LOGIN-NAME` | true     | `USER-LAST-LOGIN-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View result - user last login report

A POST request to `/reports/runs/USER-LAST-LOGIN-JOB-ID` to view a user last login name report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/USER-LAST-LOGIN-JOB-ID?_action=view&name=USER-LAST-LOGIN-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                     | Required | Example                  | Schema |
| ------------------------ | -------- | ------------------------ | ------ |
| `USER-LAST-LOGIN-JOB-ID` | true     | `USER-LAST-LOGIN-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                | Schema  |
| ----------- | -------- | ---------------------- | ------- |
| `_action`   | false    | `view`                 | string  |
| `name`      | false    | `USER-LAST-LOGIN-NAME` | string  |
| `_pageSize` | false    | `10`                   | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### Run template - user access details report

A POST request to `/reports/templates/USER-ACCESS-DETAILS-NAME` to run a user access details name report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/USER-ACCESS-DETAILS-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                       | Required | Example                    | Schema |
| -------------------------- | -------- | -------------------------- | ------ |
| `USER-ACCESS-DETAILS-NAME` | true     | `USER-ACCESS-DETAILS-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View results - user access details report

A POST request to `/reports/runs/USER-ACCESS-DETAILS-JOB-ID` to view user access details name report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/USER-ACCESS-DETAILS-JOB-ID?_action=view&name=USER-ACCESS-DETAILS-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                         | Required | Example                      | Schema |
| ---------------------------- | -------- | ---------------------------- | ------ |
| `USER-ACCESS-DETAILS-JOB-ID` | true     | `USER-ACCESS-DETAILS-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                    | Schema  |
| ----------- | -------- | -------------------------- | ------- |
| `_action`   | false    | `view`                     | string  |
| `name`      | false    | `USER-ACCESS-DETAILS-NAME` | string  |
| `_pageSize` | false    | `10`                       | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### Run template - user count by status report

A POST request to `/reports/templates/USER-COUNT-BY-STATUS-NAME` to run a user count by status report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/USER-COUNT-BY-STATUS-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                        | Required | Example                     | Schema |
| --------------------------- | -------- | --------------------------- | ------ |
| `USER-COUNT-BY-STATUS-NAME` | true     | `USER-COUNT-BY-STATUS-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View results - user count by status report

A POST request to `/reports/runs/USER-COUNT-BY-STATUS-JOB-ID` to view user count by status report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/USER-COUNT-BY-STATUS-JOB-ID?_action=view&name=USER-COUNT-BY-STATUS-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                          | Required | Example                       | Schema |
| ----------------------------- | -------- | ----------------------------- | ------ |
| `USER-COUNT-BY-STATUS-JOB-ID` | true     | `USER-COUNT-BY-STATUS-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                     | Schema  |
| ----------- | -------- | --------------------------- | ------- |
| `_action`   | false    | `view`                      | string  |
| `name`      | false    | `USER-COUNT-BY-STATUS-NAME` | string  |
| `_pageSize` | false    | `10`                        | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### Run template - user normal view report

A POST request to `/reports/templates/USER-NORMAL-VIEW-NAME` to run a user normal view report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/USER-NORMAL-VIEW-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                    | Required | Example                 | Schema |
| ----------------------- | -------- | ----------------------- | ------ |
| `USER-NORMAL-VIEW-NAME` | true     | `USER-NORMAL-VIEW-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View report - user normal view report

A POST request to `/reports/runs/USER-NORMAL-VIEW-JOB-ID` to view a user normal view report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/USER-NORMAL-VIEW-JOB-ID?_action=view&name=USER-NORMAL-VIEW-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                      | Required | Example                   | Schema |
| ------------------------- | -------- | ------------------------- | ------ |
| `USER-NORMAL-VIEW-JOB-ID` | true     | `USER-NORMAL-VIEW-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                 | Schema  |
| ----------- | -------- | ----------------------- | ------- |
| `_action`   | false    | `view`                  | string  |
| `name`      | false    | `USER-NORMAL-VIEW-NAME` | string  |
| `_pageSize` | false    | `10`                    | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

## Governance**\[[1](#_footnotedef_1 "View footnote.")]** reports endpoints

### Run template - certification details report

A POST request to `/reports/templates/certification-details` to run a certification details report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/certification-details?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View result - certification details report

A POST request to `/reports/runs/CERTIFICATION-DETAILS-JOB-ID` to view a certification details report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/CERTIFICATION-DETAILS-JOB-ID?_action=view&name=CERTIFICATION-DETAILS-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                           | Required | Example                        | Schema |
| ------------------------------ | -------- | ------------------------------ | ------ |
| `CERTIFICATION-DETAILS-JOB-ID` | true     | `CERTIFICATION-DETAILS-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                      | Schema  |
| ----------- | -------- | ---------------------------- | ------- |
| `_action`   | false    | `view`                       | string  |
| `name`      | false    | `CERTIFICATION-DETAILS-NAME` | string  |
| `_pageSize` | false    | `10`                         | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### Run template - campaign decision report

A POST request to `/reports/templates/CAMPAIGN-DECISION-NAME` to run a campaign decision name report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/templates/CAMPAIGN-DECISION-NAME?_action=run' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                     | Required | Example                  | Schema |
| ------------------------ | -------- | ------------------------ | ------ |
| `CAMPAIGN-DECISION-NAME` | true     | `CAMPAIGN-DECISION-NAME` | string |

**Query parameters**

| Name      | Required | Example | Schema |
| --------- | -------- | ------- | ------ |
| `_action` | false    | `run`   | string |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

### View result - campaign decision report

A POST request to `/reports/runs/CAMPAIGN-DECISION-JOB-ID` to view a campaign decision report.

Curl example

```
curl --location --request POST 'https://<tenant-env-fqdn>/reports/runs/CAMPAIGN-DECISION-JOB-ID?_action=view&name=CAMPAIGN-DECISION-NAME&_pageSize=10' \
--header 'Content-Type: application/json' \
--header 'Accept-API-Version: resource=1.0' \
--header 'Authorization: Bearer <access-token>'
```

**Path parameters**

| Name                       | Required | Example                    | Schema |
| -------------------------- | -------- | -------------------------- | ------ |
| `CAMPAIGN-DECISION-JOB-ID` | true     | `CAMPAIGN-DECISION-JOB-ID` | string |

**Query parameters**

| Name        | Required | Example                  | Schema  |
| ----------- | -------- | ------------------------ | ------- |
| `_action`   | false    | `view`                   | string  |
| `name`      | false    | `CAMPAIGN-DECISION-NAME` | string  |
| `_pageSize` | false    | `10`                     | integer |

**Header parameters**

| Name                 | Required | Example                 | Schema |
| -------------------- | -------- | ----------------------- | ------ |
| `Content-Type`       | false    | `application/json`      | string |
| `Accept-API-Version` | false    | `resource=1.0`          | string |
| `Authorization`      | false    | `Bearer <access-token>` | string |

***

[1](#_footnoteref_1). Identity Governance is an add-on capability to Advanced Identity Cloud. Contact your Ping Identity representative if you want to add PingOne® Identity Governance to your Advanced Identity Cloud subscription.

---

---
title: Use cases
description: Use cases demonstrating advanced reporting capabilities with custom objects and attributes
component: pingoneaic
page_id: pingoneaic:reports:use-cases/use-cases-reports
canonical_url: https://docs.pingidentity.com/pingoneaic/reports/use-cases/use-cases-reports.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
---

# Use cases

This section provides use cases for the advanced reporting feature, including examples of how to create custom reports and use historical data reporting.

The following use cases are included in this section:

* [Custom attributes for user objects](custom-attributes-for-user-in-advanced-reports.html)

* [Custom attribute for relationships in Advanced Reporting](custom-attributes-for-relationship-in-advanced-reports.html)

* [Custom attributes for organization objects in Advanced Reporting](custom-attributes-for-organization-in-advanced-reports.html)

* [Custom objects use cases](custom-objects-reports.html)

* [Create a historical change report for IDM identities](use-case-historical-data-reporting.html)