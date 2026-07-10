---
title: ServiceNow Connector
description: The ServiceNow connector lets you manage users, group memberships, and incidents in ServiceNow from your PingOne DaVinci flow.
component: connectors
page_id: connectors::servicenow_connector
canonical_url: https://docs.pingidentity.com/connectors/servicenow_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
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

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need a ServiceNow license.

### Configuring the ServiceNow connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

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
>       * calendar\_integration string
>
>       * country string
>
>       * user\_password string
>
>       * last\_login\_time string
>
>       * x\_pd\_integration\_pagerduty\_id string
>
>       * hashed\_user\_id string
>
>       * source string
>
>       * sys\_updated\_on string
>
>       * building string
>
>       * web\_service\_access\_only string
>
>       * notification string
>
>       * enable\_multifactor\_authn string
>
>       * sys\_updated\_by string
>
>       * sso\_source string
>
>       * sys\_created\_on string
>
>       * sys\_domain object
>
>         * link string
>
>         * value string
>
>       * state string
>
>       * vip string
>
>       * sys\_created\_by string
>
>       * zip string
>
>       * home\_phone string
>
>       * time\_format string
>
>       * last\_login string
>
>       * default\_perspective string
>
>       * active string
>
>       * sys\_domain\_path string
>
>       * cost\_center string
>
>       * phone string
>
>       * name string
>
>       * employee\_number string
>
>       * password\_needs\_reset string
>
>       * gender string
>
>       * city string
>
>       * failed\_attempts string
>
>       * user\_name string
>
>       * roles string
>
>       * title string
>
>       * sys\_class\_name string
>
>       * sys\_id string
>
>       * internal\_integration\_user string
>
>       * ldap\_server string
>
>       * mobile\_phone string
>
>       * street string
>
>       * company string
>
>       * first\_name string
>
>       * email string
>
>       * introduction string
>
>       * preferred\_language string
>
>       * manager string
>
>       * locked\_out string
>
>       * sys\_mod\_count string
>
>       * last\_name string
>
>       * photo string
>
>       * avatar string
>
>       * middle\_name string
>
>       * sys\_tags string
>
>       * time\_zone string
>
>       * schedule string
>
>       * date\_format string
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
>       * user\_password string
>
>       * gender string
>
>       * city string
>
>       * sys\_import\_state\_comment string
>
>       * template\_import\_log string
>
>       * sys\_updated\_on string
>
>       * sys\_class\_name string
>
>       * sys\_target\_sys\_id object
>
>         * link string
>
>         * value string
>
>       * notification string
>
>       * sys\_id string
>
>       * sys\_updated\_by string
>
>       * sys\_created\_on string
>
>       * sys\_import\_set object
>
>         * link string
>
>         * value string
>
>       * sys\_transform\_map object
>
>         * link string
>
>         * value string
>
>       * first\_name string
>
>       * email string
>
>       * preferred\_language string
>
>       * sys\_created\_by string
>
>       * group string
>
>       * sys\_import\_row string
>
>       * home\_phone string
>
>       * sys\_row\_error string
>
>       * sys\_target\_table string
>
>       * locked\_out string
>
>       * sys\_mod\_count string
>
>       * active string
>
>       * last\_name string
>
>       * import\_set\_run object
>
>         * link string
>
>         * value string
>
>       * middle\_name string
>
>       * sys\_tags string
>
>       * sys\_import\_state string
>
>       * phone string
>
>       * employee\_number string
>
>       * mobile\_number string
>
>       * username string
>
>       * group\_record\_id string
>
>       * group\_sys\_id string
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
>       * calendar\_integration string
>
>       * country string
>
>       * user\_password string
>
>       * last\_login\_time string
>
>       * x\_pd\_integration\_pagerduty\_id string
>
>       * hashed\_user\_id string
>
>       * source string
>
>       * sys\_updated\_on string
>
>       * building string
>
>       * web\_service\_access\_only string
>
>       * notification string
>
>       * enable\_multifactor\_authn string
>
>       * sys\_updated\_by string
>
>       * sso\_source string
>
>       * sys\_created\_on string
>
>       * sys\_domain object
>
>         * link string
>
>         * value string
>
>       * state string
>
>       * vip string
>
>       * sys\_created\_by string
>
>       * zip string
>
>       * home\_phone string
>
>       * time\_format string
>
>       * last\_login string
>
>       * default\_perspective string
>
>       * active string
>
>       * sys\_domain\_path string
>
>       * cost\_center string
>
>       * phone string
>
>       * name string
>
>       * employee\_number string
>
>       * password\_needs\_reset string
>
>       * gender string
>
>       * city string
>
>       * failed\_attempts string
>
>       * user\_name string
>
>       * roles string
>
>       * title string
>
>       * sys\_class\_name string
>
>       * sys\_id string
>
>       * internal\_integration\_user string
>
>       * ldap\_server string
>
>       * mobile\_phone string
>
>       * street string
>
>       * company string
>
>       * department string
>
>       * first\_name string
>
>       * email string
>
>       * introduction string
>
>       * preferred\_language string
>
>       * manager string
>
>       * locked\_out string
>
>       * sys\_mod\_count string
>
>       * last\_name string
>
>       * photo string
>
>       * avatar string
>
>       * middle\_name string
>
>       * sys\_tags string
>
>       * time\_zone string
>
>       * schedule string
>
>       * date\_format string
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
>       * x\_pd\_integration\_conf\_bridge string
>
>       * parent string
>
>       * made\_sla string
>
>       * caused\_by string
>
>       * watch\_list string
>
>       * upon\_reject string
>
>       * sys\_updated\_on string
>
>       * child\_incidents string
>
>       * hold\_reason string
>
>       * origin\_table string
>
>       * task\_effective\_number string
>
>       * approval\_history string
>
>       * number string
>
>       * resolved\_by string
>
>       * sys\_updated\_by string
>
>       * opened\_by object
>
>         * link string
>
>         * value string
>
>       * user\_input string
>
>       * sys\_created\_on string
>
>       * sys\_domain object
>
>         * link string
>
>         * value string
>
>       * x\_pd\_integration\_incident string
>
>       * state string
>
>       * route\_reason string
>
>       * sys\_created\_by string
>
>       * knowledge string
>
>       * order string
>
>       * calendar\_stc string
>
>       * closed\_at string
>
>       * cmdb\_ci string
>
>       * delivery\_plan string
>
>       * contract string
>
>       * impact string
>
>       * active string
>
>       * work\_notes\_list string
>
>       * business\_service object
>
>         * link string
>
>         * value string
>
>       * business\_impact string
>
>       * priority string
>
>       * sys\_domain\_path string
>
>       * rfc string
>
>       * time\_worked string
>
>       * expected\_start string
>
>       * opened\_at string
>
>       * business\_duration string
>
>       * group\_list string
>
>       * work\_end string
>
>       * caller\_id object
>
>         * link string
>
>         * value string
>
>       * reopened\_time string
>
>       * resolved\_at string
>
>       * approval\_set string
>
>       * subcategory string
>
>       * work\_notes string
>
>       * x\_pd\_integration\_incident\_id string
>
>       * universal\_request string
>
>       * short\_description string
>
>       * close\_code string
>
>       * correlation\_display string
>
>       * delivery\_task string
>
>       * work\_start string
>
>       * assignment\_group object
>
>         * link string
>
>         * value string
>
>       * additional\_assignee\_list string
>
>       * business\_stc string
>
>       * cause string
>
>       * description string
>
>       * origin\_id string
>
>       * calendar\_duration string
>
>       * close\_notes string
>
>       * notify string
>
>       * service\_offering string
>
>       * sys\_class\_name string
>
>       * closed\_by string
>
>       * follow\_up string
>
>       * parent\_incident string
>
>       * sys\_id string
>
>       * contact\_type string
>
>       * reopened\_by string
>
>       * incident\_state string
>
>       * urgency string
>
>       * problem\_id string
>
>       * company string
>
>       * reassignment\_count string
>
>       * x\_pd\_integration\_incident\_key string
>
>       * activity\_due string
>
>       * assigned\_to string
>
>       * severity string
>
>       * comments string
>
>       * approval string
>
>       * sla\_due string
>
>       * comments\_and\_work\_notes string
>
>       * due\_date string
>
>       * sys\_mod\_count string
>
>       * reopen\_count string
>
>       * sys\_tags string
>
>       * escalation string
>
>       * upon\_approval string
>
>       * correlation\_id string
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
>       * x\_pd\_integration\_conf\_bridge string
>
>       * parent string
>
>       * made\_sla string
>
>       * caused\_by string
>
>       * watch\_list string
>
>       * upon\_reject string
>
>       * sys\_updated\_on string
>
>       * child\_incidents string
>
>       * hold\_reason string
>
>       * origin\_table string
>
>       * task\_effective\_number string
>
>       * approval\_history string
>
>       * number string
>
>       * resolved\_by string
>
>       * sys\_updated\_by string
>
>       * opened\_by object
>
>         * link string
>
>         * value string
>
>       * user\_input string
>
>       * sys\_created\_on string
>
>       * sys\_domain object
>
>         * link string
>
>         * value string
>
>       * x\_pd\_integration\_incident string
>
>       * state string
>
>       * route\_reason string
>
>       * sys\_created\_by string
>
>       * knowledge string
>
>       * order string
>
>       * calendar\_stc string
>
>       * closed\_at string
>
>       * cmdb\_ci string
>
>       * delivery\_plan string
>
>       * contract string
>
>       * impact string
>
>       * active string
>
>       * work\_notes\_list string
>
>       * business\_service object
>
>         * link string
>
>         * value string
>
>       * business\_impact string
>
>       * priority string
>
>       * sys\_domain\_path string
>
>       * rfc string
>
>       * time\_worked string
>
>       * expected\_start string
>
>       * opened\_at string
>
>       * business\_duration string
>
>       * group\_list string
>
>       * work\_end string
>
>       * caller\_id object
>
>         * link string
>
>         * value string
>
>       * reopened\_time string
>
>       * resolved\_at string
>
>       * approval\_set string
>
>       * subcategory string
>
>       * work\_notes string
>
>       * x\_pd\_integration\_incident\_id string
>
>       * universal\_request string
>
>       * short\_description string
>
>       * close\_code string
>
>       * correlation\_display string
>
>       * delivery\_task string
>
>       * work\_start string
>
>       * assignment\_group object
>
>         * link string
>
>         * value string
>
>       * additional\_assignee\_list string
>
>       * business\_stc string
>
>       * cause string
>
>       * description string
>
>       * origin\_id string
>
>       * calendar\_duration string
>
>       * close\_notes string
>
>       * notify string
>
>       * service\_offering string
>
>       * sys\_class\_name string
>
>       * closed\_by string
>
>       * follow\_up string
>
>       * parent\_incident string
>
>       * sys\_id string
>
>       * contact\_type string
>
>       * reopened\_by string
>
>       * incident\_state string
>
>       * urgency string
>
>       * problem\_id string
>
>       * company string
>
>       * reassignment\_count string
>
>       * x\_pd\_integration\_incident\_key string
>
>       * activity\_due string
>
>       * assigned\_to string
>
>       * severity string
>
>       * comments string
>
>       * approval string
>
>       * sla\_due string
>
>       * comments\_and\_work\_notes string
>
>       * due\_date string
>
>       * sys\_mod\_count string
>
>       * reopen\_count string
>
>       * sys\_tags string
>
>       * escalation string
>
>       * upon\_approval string
>
>       * correlation\_id string
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
>       * x\_pd\_integration\_conf\_bridge string
>
>       * parent string
>
>       * made\_sla string
>
>       * caused\_by string
>
>       * watch\_list string
>
>       * upon\_reject string
>
>       * sys\_updated\_on string
>
>       * child\_incidents string
>
>       * hold\_reason string
>
>       * origin\_table string
>
>       * task\_effective\_number string
>
>       * approval\_history string
>
>       * number string
>
>       * resolved\_by string
>
>       * sys\_updated\_by string
>
>       * opened\_by object
>
>         * link string
>
>         * value string
>
>       * user\_input string
>
>       * sys\_created\_on string
>
>       * sys\_domain object
>
>         * link string
>
>         * value string
>
>       * x\_pd\_integration\_incident string
>
>       * state string
>
>       * route\_reason string
>
>       * sys\_created\_by string
>
>       * knowledge string
>
>       * order string
>
>       * calendar\_stc string
>
>       * closed\_at string
>
>       * cmdb\_ci string
>
>       * delivery\_plan string
>
>       * contract string
>
>       * impact string
>
>       * active string
>
>       * work\_notes\_list string
>
>       * business\_service object
>
>         * link string
>
>         * value string
>
>       * business\_impact string
>
>       * priority string
>
>       * sys\_domain\_path string
>
>       * rfc string
>
>       * time\_worked string
>
>       * expected\_start string
>
>       * opened\_at string
>
>       * business\_duration string
>
>       * group\_list string
>
>       * work\_end string
>
>       * caller\_id object
>
>         * link string
>
>         * value string
>
>       * reopened\_time string
>
>       * resolved\_at string
>
>       * approval\_set string
>
>       * subcategory string
>
>       * work\_notes string
>
>       * x\_pd\_integration\_incident\_id string
>
>       * universal\_request string
>
>       * short\_description string
>
>       * close\_code string
>
>       * correlation\_display string
>
>       * delivery\_task string
>
>       * work\_start string
>
>       * assignment\_group object
>
>         * link string
>
>         * value string
>
>       * additional\_assignee\_list string
>
>       * business\_stc string
>
>       * cause string
>
>       * description string
>
>       * origin\_id string
>
>       * calendar\_duration string
>
>       * close\_notes string
>
>       * notify string
>
>       * service\_offering string
>
>       * sys\_class\_name string
>
>       * closed\_by string
>
>       * follow\_up string
>
>       * parent\_incident string
>
>       * sys\_id string
>
>       * contact\_type string
>
>       * reopened\_by string
>
>       * incident\_state string
>
>       * urgency string
>
>       * problem\_id string
>
>       * company string
>
>       * reassignment\_count string
>
>       * x\_pd\_integration\_incident\_key string
>
>       * activity\_due string
>
>       * assigned\_to string
>
>       * severity string
>
>       * comments string
>
>       * approval string
>
>       * sla\_due string
>
>       * comments\_and\_work\_notes string
>
>       * due\_date string
>
>       * sys\_mod\_count string
>
>       * reopen\_count string
>
>       * sys\_tags string
>
>       * escalation string
>
>       * upon\_approval string
>
>       * correlation\_id string
>
>       * location string
>
>       * category string
>
>   * statusCode number