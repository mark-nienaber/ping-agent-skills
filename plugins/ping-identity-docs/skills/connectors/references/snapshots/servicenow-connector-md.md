---
title: ServiceNow Connector
description: Configure the ServiceNow connector to manage users, group memberships, and incidents in ServiceNow from a PingOne DaVinci flow
component: connectors
page_id: connectors::servicenow_connector
canonical_url: https://docs.pingidentity.com/connectors/servicenow_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-07-09T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-servicenow-connector: Configuring the ServiceNow connector
  connector-configuration: Connector configuration
  api-url: API URL
  admin-username: Admin Username
  admin-password: Admin Password
  using-the-connector-in-a-flow: Using the connector in a flow
  searching-for-users: Searching for users
  managing-users: Managing users
  managing-group-memberships: Managing group memberships
  managing-incidents: Managing incidents
  limitations: Limitations
  capabilities: Capabilities
  getUser: Get User Information
  getUsers: Search Users
  deleteUser: Deactivate User
  createUser: Create User
  addGroup: Add User to Group
  modifyUser: Modify User
  createIncident: Create Incident
  readIncident: Read Incident
  modifyIncident: Modify Incident
---

# ServiceNow Connector

The ServiceNow connector lets you manage users, group memberships, and incidents in ServiceNow from your PingOne DaVinci flow.

You can use the ServiceNow connector to:

* Create, deactivate, modify, and search for users

* Add users to groups

* Read, create, and modify incidents

## Setup

### Resources

Learn more in the following:

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a ServiceNow license.

### Configuring the ServiceNow connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### API URL

The API URL to target, such as "mycompany.service-now\.com". This domain is visible in the URL bar when you sign on to the ServiceNow administrator portal.

##### Admin Username

Your ServiceNow administrator username.

##### Admin Password

Your ServiceNow administrator password.

## Using the connector in a flow

### Searching for users

There are two ways to search for users with the ServiceNow connector:

* Search for a specific user by user ID using the **Search User** capability.

* Search for multiple users based on their attributes using the **Search** capability.

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Managing users

The connector has two capabilities that allow you to create, modify, activate, and deactivate users in ServiceNow:

* **Create User**

* **Modify User**

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Managing group memberships

The **Add User to Group** connector allows you to manage the groups that a user belongs to in ServiceNow:

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Managing incidents

The connector has several capabilities that allow you to manage incidents in ServiceNow:

* **Read an incident**

* **Create an incident**

* **Modify an incident**

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

## Limitations

ServiceNow does not provide support for:

* Deleting users

* Removing users from groups

* Deleting incidents

## Capabilities

### Get User Information

Get information about a user.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - User System ID textField required
>
>   The user's ServiceNow system ID, such as "bdac51a8e4afd91bda9d1018cc4bcbc8".
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * calendar_integration string
>
>       * country string
>
>       * user_password string
>
>       * last_login_time string
>
>       * x_pd_integration_pagerduty_id string
>
>       * hashed_user_id string
>
>       * source string
>
>       * sys_updated_on string
>
>       * building string
>
>       * web_service_access_only string
>
>       * notification string
>
>       * enable_multifactor_authn string
>
>       * sys_updated_by string
>
>       * sso_source string
>
>       * sys_created_on string
>
>       * sys_domain object
>
>         * link string
>
>         * value string
>
>       * state string
>
>       * vip string
>
>       * sys_created_by string
>
>       * zip string
>
>       * home_phone string
>
>       * time_format string
>
>       * last_login string
>
>       * default_perspective string
>
>       * active string
>
>       * sys_domain_path string
>
>       * cost_center string
>
>       * phone string
>
>       * name string
>
>       * employee_number string
>
>       * password_needs_reset string
>
>       * gender string
>
>       * city string
>
>       * failed_attempts string
>
>       * user_name string
>
>       * roles string
>
>       * title string
>
>       * sys_class_name string
>
>       * sys_id string
>
>       * internal_integration_user string
>
>       * ldap_server string
>
>       * mobile_phone string
>
>       * street string
>
>       * company string
>
>       * first_name string
>
>       * email string
>
>       * introduction string
>
>       * preferred_language string
>
>       * manager string
>
>       * locked_out string
>
>       * sys_mod_count string
>
>       * last_name string
>
>       * photo string
>
>       * avatar string
>
>       * middle_name string
>
>       * sys_tags string
>
>       * time_zone string
>
>       * schedule string
>
>       * date_format string
>
>       * location string
>
>   * statusCode number

### Search Users

Search for users based on an attribute filter.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Number of Results textField
>
>   The number of results to return from the search.
>
> - Email textField
>
>   The user's email address.
>
> - First Name textField
>
>   The user's first name.
>
> - Last Name textField
>
>   The user's last name.
>
> - Query Parameters keyValueList
>
>   Define additional query parameters to send to ServiceNow. Learn more in the ServiceNow user table documentation.
>
> * output object
>
>   * rawResponse object
>
>     * result array
>
>   * statusCode number

### Deactivate User

Deactivate a user by the ServiceNow ID.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - User System ID textField required
>
>   The user's ServiceNow system ID, such as "bdac51a8e4afd91bda9d1018cc4bcbc8".
>
> * output object
>
>   * statusCode number

### Create User

Create a new user.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Username textField
>
>   The unique ID of the user.
>
> - First Name textField
>
>   The user's first name.
>
> - Middle Name textField
>
>   The user's middle name.
>
> - Last Name textField
>
>   The user's last name.
>
> - Phone textField
>
>   The user's phone number.
>
> - Email textField required
>
>   The user's email address.
>
> - Activate User toggleSwitch
>
>   When enabled, this sets the user account to active in ServiceNow.
>
> - Group dropDown
>
>   The relevant group.
>
> - City textField
>
>   The User's city
>
> - Employee Number textField
>
>   The User's employee number.
>
> - Custom Attributes keyValueList
>
>   Additional attributes for user creation or modification.
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * country string
>
>       * user_password string
>
>       * gender string
>
>       * city string
>
>       * sys_import_state_comment string
>
>       * template_import_log string
>
>       * sys_updated_on string
>
>       * sys_class_name string
>
>       * sys_target_sys_id object
>
>         * link string
>
>         * value string
>
>       * notification string
>
>       * sys_id string
>
>       * sys_updated_by string
>
>       * sys_created_on string
>
>       * sys_import_set object
>
>         * link string
>
>         * value string
>
>       * sys_transform_map object
>
>         * link string
>
>         * value string
>
>       * first_name string
>
>       * email string
>
>       * preferred_language string
>
>       * sys_created_by string
>
>       * group string
>
>       * sys_import_row string
>
>       * home_phone string
>
>       * sys_row_error string
>
>       * sys_target_table string
>
>       * locked_out string
>
>       * sys_mod_count string
>
>       * active string
>
>       * last_name string
>
>       * import_set_run object
>
>         * link string
>
>         * value string
>
>       * middle_name string
>
>       * sys_tags string
>
>       * sys_import_state string
>
>       * phone string
>
>       * employee_number string
>
>       * mobile_number string
>
>       * username string
>
>       * group_record_id string
>
>       * group_sys_id string
>
>   * statusCode number

### Add User to Group

Add a user to a group.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User System ID textField required
>
>   The user's ServiceNow system ID, such as "bdac51a8e4afd91bda9d1018cc4bcbc8".
>
> - Group dropDown
>
>   The relevant group.
>
> * default object
>
>   * apiUrl string
>
>   * adminUsername string
>
>   * password string
>
>   * userId string
>
>   * group string
>
> - output object
>
>   * statusCode number

### Modify User

Modify a user.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - User System ID textField required
>
>   The user's ServiceNow system ID, such as "bdac51a8e4afd91bda9d1018cc4bcbc8".
>
> - Username textField
>
>   The unique ID of the user.
>
> - First Name textField
>
>   The user's first name.
>
> - Middle Name textField
>
>   The user's middle name.
>
> - Last Name textField
>
>   The user's last name.
>
> - Phone textField
>
>   The user's phone number.
>
> - Email textField
>
>   The user's email address.
>
> - Activate User toggleSwitch
>
>   When enabled, this sets the user account to active in ServiceNow.
>
> - Lock User Out toggleSwitch
>
>   When enabled, the user is locked out of ServiceNow.
>
> - Custom Attributes keyValueList
>
>   Additional attributes for user creation or modification.
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * calendar_integration string
>
>       * country string
>
>       * user_password string
>
>       * last_login_time string
>
>       * x_pd_integration_pagerduty_id string
>
>       * hashed_user_id string
>
>       * source string
>
>       * sys_updated_on string
>
>       * building string
>
>       * web_service_access_only string
>
>       * notification string
>
>       * enable_multifactor_authn string
>
>       * sys_updated_by string
>
>       * sso_source string
>
>       * sys_created_on string
>
>       * sys_domain object
>
>         * link string
>
>         * value string
>
>       * state string
>
>       * vip string
>
>       * sys_created_by string
>
>       * zip string
>
>       * home_phone string
>
>       * time_format string
>
>       * last_login string
>
>       * default_perspective string
>
>       * active string
>
>       * sys_domain_path string
>
>       * cost_center string
>
>       * phone string
>
>       * name string
>
>       * employee_number string
>
>       * password_needs_reset string
>
>       * gender string
>
>       * city string
>
>       * failed_attempts string
>
>       * user_name string
>
>       * roles string
>
>       * title string
>
>       * sys_class_name string
>
>       * sys_id string
>
>       * internal_integration_user string
>
>       * ldap_server string
>
>       * mobile_phone string
>
>       * street string
>
>       * company string
>
>       * department string
>
>       * first_name string
>
>       * email string
>
>       * introduction string
>
>       * preferred_language string
>
>       * manager string
>
>       * locked_out string
>
>       * sys_mod_count string
>
>       * last_name string
>
>       * photo string
>
>       * avatar string
>
>       * middle_name string
>
>       * sys_tags string
>
>       * time_zone string
>
>       * schedule string
>
>       * date_format string
>
>       * location string
>
>   * statusCode number

### Create Incident

Create a new incident.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Caller ID textField
>
>   The ServiceNow system ID of the user with the issue, such as "bdac51a8e4afd91bda9d1018cc4bcbc8".
>
> - Category dropDown
>
>   The incident category.
>
> - Subcategory dropDown
>
>   The incident subcategory.
>
> - Service dropDown
>
>   The service associated with the incident.
>
> - Configuration Item ID textField
>
>   The ServiceNow system ID of the related configuration item, such as "fd91bda9d10bdac51a8e4a18cc4bcbc8".
>
> - Short Description textArea
>
>   A brief description of the incident.
>
> - Description textArea
>
>   A complete description of the incident.
>
> - Channel dropDown
>
>   The channel (source) where the incident took place.
>
> - Status dropDown
>
>   The status of the incident.
>
> - Impact dropDown
>
>   The level of impact for the incident.
>
> - Urgency dropDown
>
>   The level of urgency for the incident.
>
> - Group dropDown
>
>   The relevant group.
>
> - Custom Attributes keyValueList
>
>   Additional attributes for user creation or modification.
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * x_pd_integration_conf_bridge string
>
>       * parent string
>
>       * made_sla string
>
>       * caused_by string
>
>       * watch_list string
>
>       * upon_reject string
>
>       * sys_updated_on string
>
>       * child_incidents string
>
>       * hold_reason string
>
>       * origin_table string
>
>       * task_effective_number string
>
>       * approval_history string
>
>       * number string
>
>       * resolved_by string
>
>       * sys_updated_by string
>
>       * opened_by object
>
>         * link string
>
>         * value string
>
>       * user_input string
>
>       * sys_created_on string
>
>       * sys_domain object
>
>         * link string
>
>         * value string
>
>       * x_pd_integration_incident string
>
>       * state string
>
>       * route_reason string
>
>       * sys_created_by string
>
>       * knowledge string
>
>       * order string
>
>       * calendar_stc string
>
>       * closed_at string
>
>       * cmdb_ci string
>
>       * delivery_plan string
>
>       * contract string
>
>       * impact string
>
>       * active string
>
>       * work_notes_list string
>
>       * business_service object
>
>         * link string
>
>         * value string
>
>       * business_impact string
>
>       * priority string
>
>       * sys_domain_path string
>
>       * rfc string
>
>       * time_worked string
>
>       * expected_start string
>
>       * opened_at string
>
>       * business_duration string
>
>       * group_list string
>
>       * work_end string
>
>       * caller_id object
>
>         * link string
>
>         * value string
>
>       * reopened_time string
>
>       * resolved_at string
>
>       * approval_set string
>
>       * subcategory string
>
>       * work_notes string
>
>       * x_pd_integration_incident_id string
>
>       * universal_request string
>
>       * short_description string
>
>       * close_code string
>
>       * correlation_display string
>
>       * delivery_task string
>
>       * work_start string
>
>       * assignment_group object
>
>         * link string
>
>         * value string
>
>       * additional_assignee_list string
>
>       * business_stc string
>
>       * cause string
>
>       * description string
>
>       * origin_id string
>
>       * calendar_duration string
>
>       * close_notes string
>
>       * notify string
>
>       * service_offering string
>
>       * sys_class_name string
>
>       * closed_by string
>
>       * follow_up string
>
>       * parent_incident string
>
>       * sys_id string
>
>       * contact_type string
>
>       * reopened_by string
>
>       * incident_state string
>
>       * urgency string
>
>       * problem_id string
>
>       * company string
>
>       * reassignment_count string
>
>       * x_pd_integration_incident_key string
>
>       * activity_due string
>
>       * assigned_to string
>
>       * severity string
>
>       * comments string
>
>       * approval string
>
>       * sla_due string
>
>       * comments_and_work_notes string
>
>       * due_date string
>
>       * sys_mod_count string
>
>       * reopen_count string
>
>       * sys_tags string
>
>       * escalation string
>
>       * upon_approval string
>
>       * correlation_id string
>
>       * location string
>
>       * category string
>
>   * statusCode number

### Read Incident

Search for an incident by the incident number or by the ServiceNow ID.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Incident Search Attribute dropDown required
>
>   Determines whether to get incident information based on an incident number or by ServiceNow system ID.
>
>   * Use Incident ID (Default)
>
>   * Use Incident number
>
> - Incident Number textField required
>
>   The incident number, such as "INC0010077".
>
> - Incident ID textField required
>
>   The incident's ServiceNow system ID, such as "c4bcbc8bdac51a8e4afd91bda9d1018c".
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * x_pd_integration_conf_bridge string
>
>       * parent string
>
>       * made_sla string
>
>       * caused_by string
>
>       * watch_list string
>
>       * upon_reject string
>
>       * sys_updated_on string
>
>       * child_incidents string
>
>       * hold_reason string
>
>       * origin_table string
>
>       * task_effective_number string
>
>       * approval_history string
>
>       * number string
>
>       * resolved_by string
>
>       * sys_updated_by string
>
>       * opened_by object
>
>         * link string
>
>         * value string
>
>       * user_input string
>
>       * sys_created_on string
>
>       * sys_domain object
>
>         * link string
>
>         * value string
>
>       * x_pd_integration_incident string
>
>       * state string
>
>       * route_reason string
>
>       * sys_created_by string
>
>       * knowledge string
>
>       * order string
>
>       * calendar_stc string
>
>       * closed_at string
>
>       * cmdb_ci string
>
>       * delivery_plan string
>
>       * contract string
>
>       * impact string
>
>       * active string
>
>       * work_notes_list string
>
>       * business_service object
>
>         * link string
>
>         * value string
>
>       * business_impact string
>
>       * priority string
>
>       * sys_domain_path string
>
>       * rfc string
>
>       * time_worked string
>
>       * expected_start string
>
>       * opened_at string
>
>       * business_duration string
>
>       * group_list string
>
>       * work_end string
>
>       * caller_id object
>
>         * link string
>
>         * value string
>
>       * reopened_time string
>
>       * resolved_at string
>
>       * approval_set string
>
>       * subcategory string
>
>       * work_notes string
>
>       * x_pd_integration_incident_id string
>
>       * universal_request string
>
>       * short_description string
>
>       * close_code string
>
>       * correlation_display string
>
>       * delivery_task string
>
>       * work_start string
>
>       * assignment_group object
>
>         * link string
>
>         * value string
>
>       * additional_assignee_list string
>
>       * business_stc string
>
>       * cause string
>
>       * description string
>
>       * origin_id string
>
>       * calendar_duration string
>
>       * close_notes string
>
>       * notify string
>
>       * service_offering string
>
>       * sys_class_name string
>
>       * closed_by string
>
>       * follow_up string
>
>       * parent_incident string
>
>       * sys_id string
>
>       * contact_type string
>
>       * reopened_by string
>
>       * incident_state string
>
>       * urgency string
>
>       * problem_id string
>
>       * company string
>
>       * reassignment_count string
>
>       * x_pd_integration_incident_key string
>
>       * activity_due string
>
>       * assigned_to string
>
>       * severity string
>
>       * comments string
>
>       * approval string
>
>       * sla_due string
>
>       * comments_and_work_notes string
>
>       * due_date string
>
>       * sys_mod_count string
>
>       * reopen_count string
>
>       * sys_tags string
>
>       * escalation string
>
>       * upon_approval string
>
>       * correlation_id string
>
>       * location string
>
>       * category string
>
>   * statusCode number

### Modify Incident

Modify an incident by its ServiceNow ID.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Incident ID textField required
>
>   The incident's ServiceNow system ID, such as "c4bcbc8bdac51a8e4afd91bda9d1018c".
>
> - Caller ID textField
>
>   The ServiceNow system ID of the user with the issue, such as "bdac51a8e4afd91bda9d1018cc4bcbc8".
>
> - Category dropDown
>
>   The incident category.
>
> - Subcategory dropDown
>
>   The incident subcategory.
>
> - Service dropDown
>
>   The service associated with the incident.
>
> - Configuration Item ID textField
>
>   The ServiceNow system ID of the related configuration item, such as "fd91bda9d10bdac51a8e4a18cc4bcbc8".
>
> - Short Description textArea
>
>   A brief description of the incident.
>
> - Description textArea
>
>   A complete description of the incident.
>
> - Channel dropDown
>
>   The channel (source) where the incident took place.
>
> - Status dropDown
>
>   The status of the incident.
>
> - Impact dropDown
>
>   The level of impact for the incident.
>
> - Urgency dropDown
>
>   The level of urgency for the incident.
>
> - Group dropDown
>
>   The relevant group.
>
> - Custom Attributes keyValueList
>
>   Additional attributes for user creation or modification.
>
> * output object
>
>   * rawResponse object
>
>     * result object
>
>       * x_pd_integration_conf_bridge string
>
>       * parent string
>
>       * made_sla string
>
>       * caused_by string
>
>       * watch_list string
>
>       * upon_reject string
>
>       * sys_updated_on string
>
>       * child_incidents string
>
>       * hold_reason string
>
>       * origin_table string
>
>       * task_effective_number string
>
>       * approval_history string
>
>       * number string
>
>       * resolved_by string
>
>       * sys_updated_by string
>
>       * opened_by object
>
>         * link string
>
>         * value string
>
>       * user_input string
>
>       * sys_created_on string
>
>       * sys_domain object
>
>         * link string
>
>         * value string
>
>       * x_pd_integration_incident string
>
>       * state string
>
>       * route_reason string
>
>       * sys_created_by string
>
>       * knowledge string
>
>       * order string
>
>       * calendar_stc string
>
>       * closed_at string
>
>       * cmdb_ci string
>
>       * delivery_plan string
>
>       * contract string
>
>       * impact string
>
>       * active string
>
>       * work_notes_list string
>
>       * business_service object
>
>         * link string
>
>         * value string
>
>       * business_impact string
>
>       * priority string
>
>       * sys_domain_path string
>
>       * rfc string
>
>       * time_worked string
>
>       * expected_start string
>
>       * opened_at string
>
>       * business_duration string
>
>       * group_list string
>
>       * work_end string
>
>       * caller_id object
>
>         * link string
>
>         * value string
>
>       * reopened_time string
>
>       * resolved_at string
>
>       * approval_set string
>
>       * subcategory string
>
>       * work_notes string
>
>       * x_pd_integration_incident_id string
>
>       * universal_request string
>
>       * short_description string
>
>       * close_code string
>
>       * correlation_display string
>
>       * delivery_task string
>
>       * work_start string
>
>       * assignment_group object
>
>         * link string
>
>         * value string
>
>       * additional_assignee_list string
>
>       * business_stc string
>
>       * cause string
>
>       * description string
>
>       * origin_id string
>
>       * calendar_duration string
>
>       * close_notes string
>
>       * notify string
>
>       * service_offering string
>
>       * sys_class_name string
>
>       * closed_by string
>
>       * follow_up string
>
>       * parent_incident string
>
>       * sys_id string
>
>       * contact_type string
>
>       * reopened_by string
>
>       * incident_state string
>
>       * urgency string
>
>       * problem_id string
>
>       * company string
>
>       * reassignment_count string
>
>       * x_pd_integration_incident_key string
>
>       * activity_due string
>
>       * assigned_to string
>
>       * severity string
>
>       * comments string
>
>       * approval string
>
>       * sla_due string
>
>       * comments_and_work_notes string
>
>       * due_date string
>
>       * sys_mod_count string
>
>       * reopen_count string
>
>       * sys_tags string
>
>       * escalation string
>
>       * upon_approval string
>
>       * correlation_id string
>
>       * location string
>
>       * category string
>
>   * statusCode number