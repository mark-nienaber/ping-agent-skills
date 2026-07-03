---
title: Google Workspace Admin Connector
description: The Google Workspace Admin connector lets you manage Google Workspace users, groups, and application licenses in your PingOne DaVinci flow.
component: connectors
page_id: connectors::google_workspace_admin_connector
canonical_url: https://docs.pingidentity.com/connectors/google_workspace_admin_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-google-workspace-admin: Setting up Google Workspace Admin
  setting-up-the-google-workspace-admin-connector-configuration: Setting up the Google Workspace Admin connector configuration
  connector-configuration: Connector configuration
  service-account-email-address: Service Account Email Address
  admin-email-address: Admin Email Address
  private-key: Private Key
  using-the-connector-in-a-flow: Using the connector in a flow
  managing-users: Managing users
  managing-group-memberships: Managing group memberships
  managing-user-devices: Managing user devices
  managing-application-licenses: Managing application licenses
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  createUser: Create a User
  deleteUser: Delete a User
  getUser: Get User Information
  updateUser: Update a User
  addUserToGroup: Add a User to a Group
  removeUserFromGroup: Remove a User from a Group
  listDevices: List a User's Devices
  deviceAction: Manage a Device
  assignLicense: Assign a License to a User
  unAssignLicense: Revoke a User's License
  makeCustomApiCall: Make a Custom API Call
---

# Google Workspace Admin Connector

The Google Workspace Admin connector lets you manage Google Workspace users, groups, and application licenses in your PingOne DaVinci flow.

## Setup

### Resources

Learn more in the following documentation:

* Google Workspace documentation:

  * [Using OAuth 2.0 for Server to Server Applications](https://developers.google.com/identity/protocols/oauth2/service-account)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need administrator access for your Google organization.

### Setting up Google Workspace Admin

Follow the instructions in [Using OAuth 2.0 for Server to Server Applications](https://developers.google.com/identity/protocols/oauth2/service-account) to do the following:

1. Create a service account.

2. Delegate domain-wide authority to the service account and authorize it with the following scopes:

   ```
   https://www.googleapis.com/auth/admin.directory.user,
   https://www.googleapis.com/auth/admin.directory.group,
   https://www.googleapis.com/auth/admin.directory.device.chromeos,
   https://www.googleapis.com/auth/admin.directory.device.mobile,
   https://www.googleapis.com/auth/apps.licensing
   ```

### Setting up the Google Workspace Admin connector configuration

In DaVinci, add a **Google Workspace Admin** connection. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector configuration

##### Service Account Email Address

The email address associated with the Google Workspace service, such as `google-workspace-admin@xenon-set-123456.iam.gserviceaccount.com`. You can find this on the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts) page.

![A screen capture of the service account page.](_images/connector-images/dvc-google-workspace-admin-service-account-page.png)

##### Admin Email Address

The email address you use to sign on to Workspace as an administrator.

##### Private Key

The private key associated with the public key that you added to the Google Workspace Admin service.

If you allowed Workspace to generate the key pair, open the downloaded `.json` file and copy the private key value.

![A screen capture of the .json file with the private key highlighted.](_images/connector-images/dvc-google-workspace-admin-json-private-key.png)

## Using the connector in a flow

### Managing users

The connector has several capabilities that allow you to manage users in Workspace:

* **Create a User**

* **Delete a User**

* **Update a User**

* **Get User Information**

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Managing group memberships

The connector has several capabilities that allow you to manage the users that belong to each group in Workspace:

* **Add a User to a Group**

* **Remove a User from a Group**

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Managing user devices

The connector has several capabilities that allow you to list and take administrative action on the mobile devices associated with users in Workspace:

* **List a User's Devices**

* **Manage a Device**

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Managing application licenses

The connector has several capabilities that allow you to manage the applications that each user can access in Workspace:

* **Assign a License to a User**

* **Revoke a User's License**

No special flow configuration is needed. Add the capability you want and populate its properties according to the help text.

### Creating a custom API call

If you want to do something that isn't supported by one of the provided capabilities, you can use the **Make Custom API Call** capability to define your own action.

This capability uses the credentials from your connection to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Create a User

Create a new user account

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Primary Email textField
>
>   The user's primary email address.
>
> - Password textField
>
>   The password to assign to the user account.
>
> - Family Name textField
>
>   The user's last name.
>
> - Given Name textField
>
>   The user's given name.
>
> - Other User Attributes variableInputList
>
>   Define additional attributes to add to the user account. Learn more in the User Accounts section of the Google Workspace SDK documentation.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * primaryEmail string required
>
>     * password string required
>
>     * familyName string required
>
>     * givenName string required
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * primaryEmail string
>
>     * password string
>
>     * hashFunction string
>
>     * isAdmin boolean
>
>     * isDelegatedAdmin boolean
>
>     * agreedToTerms boolean
>
>     * suspended boolean
>
>     * changePasswordAtNextLogin boolean
>
>     * ipWhitelisted boolean
>
>     * name object
>
>       * givenName string
>
>       * familyName string
>
>       * fullName string
>
>     * kind string
>
>     * etag string
>
>     * emails array
>
>     * externalIds array
>
>     * relations array
>
>     * aliases array
>
>     * isMailboxSetup boolean
>
>     * customerId string
>
>     * addresses array
>
>     * organizations array
>
>     * lastLoginTime string
>
>     * phones array
>
>     * suspensionReason string
>
>     * thumbnailPhotoUrl string
>
>     * languages array
>
>     * posixAccounts array
>
>     * creationTime string
>
>     * nonEditableAliases array
>
>     * sshPublicKeys array
>
>     * notes object
>
>       * contentType string
>
>       * value string
>
>     * websites array
>
>     * locations array
>
>     * includeInGlobalAddressList boolean
>
>     * keywords array
>
>     * deletionTime string
>
>     * gender object
>
>       * addressMeAs string
>
>       * customGender string
>
>       * type string
>
>     * thumbnailPhotoEtag string
>
>     * ims array
>
>     * customSchemas object
>
>       * somefield string
>
>     * isEnrolledIn2Sv boolean
>
>     * isEnforcedIn2Sv boolean
>
>     * archived boolean
>
>     * orgUnitPath string
>
>     * recoveryEmail string
>
>     * recoveryPhone string
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * content-type string
>
>     * vary string
>
>     * date string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Delete a User

Delete a user account

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Identifier textField
>
>   The user's primary email address, unique user id, or one of the user's alias email addresses.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * userKey string required
>
> - output object
>
>   * rawResponse string
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * vary string
>
>     * date string
>
>     * content-type string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Get User Information

Get information about a user

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Identifier textField
>
>   The user's primary email address, unique user id, or one of the user's alias email addresses.
>
> - Requested Fields dropDown
>
>   The level of information to request about the user. "Basic" returns a standard set of fields. "Full" returns all fields. "Use Custom Field Schemas" returns the Basic fields as well as specific fields associated with the schemas you enter in "Custom Field Schemas".
>
>   * BASIC
>
>   * CUSTOM
>
>   * FULL
>
> - View Type dropDown
>
>   The type of fields to request. "Admin View" returns publicly visible and administrator-only fields. "Public View" only returns publicly visible fields.
>
>   * Admin View
>
>   * Domain Public
>
> - Output Filter textFieldArrayView
>
>   The list of fields for the connector to output to the flow, such as "emails" or "emails.address". Instead of outputting all of the results from the "Requested Attributes", you can filter the results to a list of specific fields. Type a field name and press Enter to add it. Leave this field blank to include all requested fields in the connector output.
>
> - Custom Field Schemas textFieldArrayView
>
>   The list of schemas to request. This returns all fields associated with the listed schemas. Type a schema name and press Enter to add it.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * userKey string required
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * primaryEmail string
>
>     * password string
>
>     * hashFunction string
>
>     * isAdmin boolean
>
>     * isDelegatedAdmin boolean
>
>     * agreedToTerms boolean
>
>     * suspended boolean
>
>     * changePasswordAtNextLogin boolean
>
>     * ipWhitelisted boolean
>
>     * name object
>
>       * givenName string
>
>       * familyName string
>
>       * fullName string
>
>     * kind string
>
>     * etag string
>
>     * emails array
>
>     * externalIds array
>
>     * relations array
>
>     * aliases array
>
>     * isMailboxSetup boolean
>
>     * customerId string
>
>     * addresses array
>
>     * organizations array
>
>     * lastLoginTime string
>
>     * phones array
>
>     * suspensionReason string
>
>     * thumbnailPhotoUrl string
>
>     * languages array
>
>     * posixAccounts array
>
>     * creationTime string
>
>     * nonEditableAliases array
>
>     * sshPublicKeys array
>
>     * notes object
>
>       * contentType string
>
>       * value string
>
>     * websites array
>
>     * locations array
>
>     * includeInGlobalAddressList boolean
>
>     * keywords array
>
>     * deletionTime string
>
>     * gender object
>
>       * addressMeAs string
>
>       * customGender string
>
>       * type string
>
>     * thumbnailPhotoEtag string
>
>     * ims array
>
>     * customSchemas object
>
>       * somefield string
>
>     * isEnrolledIn2Sv boolean
>
>     * isEnforcedIn2Sv boolean
>
>     * archived boolean
>
>     * orgUnitPath string
>
>     * recoveryEmail string
>
>     * recoveryPhone string
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * content-type string
>
>     * vary string
>
>     * date string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Update a User

Update information about a user

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Identifier textField
>
>   The user's primary email address, unique user id, or one of the user's alias email addresses.
>
> - Other User Attributes variableInputList
>
>   Define additional attributes to add to the user account. Learn more in the User Accounts section of the Google Workspace SDK documentation.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * userKey string required
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * primaryEmail string
>
>     * password string
>
>     * hashFunction string
>
>     * isAdmin boolean
>
>     * isDelegatedAdmin boolean
>
>     * agreedToTerms boolean
>
>     * suspended boolean
>
>     * changePasswordAtNextLogin boolean
>
>     * ipWhitelisted boolean
>
>     * name object
>
>       * givenName string
>
>       * familyName string
>
>       * fullName string
>
>     * kind string
>
>     * etag string
>
>     * emails array
>
>     * externalIds array
>
>     * relations array
>
>     * aliases array
>
>     * isMailboxSetup boolean
>
>     * customerId string
>
>     * addresses array
>
>     * organizations array
>
>     * lastLoginTime string
>
>     * phones array
>
>     * suspensionReason string
>
>     * thumbnailPhotoUrl string
>
>     * languages array
>
>     * posixAccounts array
>
>     * creationTime string
>
>     * nonEditableAliases array
>
>     * sshPublicKeys array
>
>     * notes object
>
>       * contentType string
>
>       * value string
>
>     * websites array
>
>     * locations array
>
>     * includeInGlobalAddressList boolean
>
>     * keywords array
>
>     * deletionTime string
>
>     * gender object
>
>       * addressMeAs string
>
>       * customGender string
>
>       * type string
>
>     * thumbnailPhotoEtag string
>
>     * ims array
>
>     * customSchemas object
>
>       * somefield string
>
>     * isEnrolledIn2Sv boolean
>
>     * isEnforcedIn2Sv boolean
>
>     * archived boolean
>
>     * orgUnitPath string
>
>     * recoveryEmail string
>
>     * recoveryPhone string
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * content-type string
>
>     * vary string
>
>     * date string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Add a User to a Group

Add a user to a group

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Group Identifier textField
>
>   The group's primary email address, unique group id, or alias.
>
> - Member Email textField
>
>   The member's email address. The member can be a user or another group.
>
> - Member Role dropDown
>
>   The role to assign the member in the group.
>
>   * Manager
>
>   * Member
>
>   * Owner
>
> - Member Type dropDown
>
>   The type of member in the group.
>
>   * Customer
>
>   * External
>
>   * Group
>
>   * User
>
> - Member Email Delivery Settings dropDown
>
>   The member's email delivery frequency.
>
>   * ALL\_MAIL
>
>   * DAILY
>
>   * DIGEST
>
>   * DISABLED
>
>   * NONE
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * groupKey string required
>
>     * memberEmail string required
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * email string
>
>     * name string
>
>     * description string
>
>     * adminCreated boolean
>
>     * directMembersCount string
>
>     * kind string
>
>     * etag string
>
>     * aliases array
>
>     * nonEditableAliases array
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * content-type string
>
>     * vary string
>
>     * date string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Remove a User from a Group

Remove a user from a group

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Member Key textField
>
>   Identifies the group member in the API request.
>
> - Group Identifier textField
>
>   The group's primary email address, unique group id, or alias.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * groupKey string required
>
>     * memberKey string required
>
> - output object
>
>   * statusCode integer
>
>   * headers object
>
>     * vary string
>
>     * date string
>
>     * content-type string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### List a User's Devices

Query Google Workspace for a list of devices associated with a user account

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Customer ID textField
>
>   The unique ID for the customer's Google Workspace account, such as "C123abc4d". This ID is available from the "Get User Information" capability.
>
> - Maximum Number of Results textField
>
>   The maximum number of results to return from the query, up to 100.
>
> - Device Order dropDown
>
>   The device property to use for sorting results.
>
>   * DEVICE\_ID
>
>   * EMAIL
>
>   * LAST\_SYNC
>
>   * MODEL
>
>   * NAME
>
>   * OS
>
>   * STATUS
>
>   * TYPE
>
> - Requested Device Fields dropDown
>
>   The level of information to request about the device. "Basic" returns a standard set of fields. "Full" returns all fields.
>
>   * BASIC
>
>   * FULL
>
> - Query String textField
>
>   The query used to search for devices, such as "status:approved" or "os:Android". Learn more in documentation for "Mobile device search fields" section of the Google Workspace SDK Directory API documentation.
>
> - Sort Order dropDown
>
>   The sort order for the list of devices. This is required if you have selected a "Device Order" option.
>
>   * ASCENDING
>
>   * DESCENDING
>
> - Page Token textField
>
>   The token used to specify the next page in the results, such as "3". Use this to get pages of results for queries that return more than the maximum number of results.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * customerId string required
>
>     * maxResults number
>
>     * orderBy string
>
>     * deviceProjection string
>
>     * query string
>
>     * sortOrder string
>
> - output object
>
>   * kind string
>
>   * etag string
>
>   * mobiledevices array
>
>   * nextPageToken string

### Manage a Device

Take administrative action on a device, such as approving, blocking, or wiping data

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Customer ID textField
>
>   The unique ID for the customer's Google Workspace account, such as "C123abc4d". This ID is available from the "Get User Information" capability.
>
> - Device ID textField
>
>   The device ID, such as "AFiQxQ-WO…YM-hf080OZy".
>
> - Action dropDown
>
>   The administrative action to take on the device.
>
>   * Admin remote wipe
>
>   * Admin account wipe
>
>   * Approve
>
>   * Block
>
>   * Cancel remote wipe then activate
>
>   * Cancel remote wipe then block
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * customerId string required
>
>     * resourceId string required
>
>     * action string required
>
> - output object
>
>   * rawResponse string
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * vary string
>
>     * date string
>
>     * content-type string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Assign a License to a User

Grant a user access to a product by assigning a license

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Product ID textField
>
>   The product ID, such as "Google-Apps".
>
> - SKU ID textField
>
>   The SKU ID, such as "Google-Apps-For-Business".
>
> - User ID textField
>
>   The user's primary email address.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * productId string required
>
>     * skuId string required
>
>     * licenseUserId string required
>
> - output object
>
>   * rawResponse object
>
>     * userId string
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * content-type string
>
>     * vary string
>
>     * date string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Revoke a User's License

Remove a user's access to a product by revoking a license

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Product ID textField
>
>   The product ID, such as "Google-Apps".
>
> - SKU ID textField
>
>   The SKU ID, such as "Google-Apps-For-Business".
>
> - User ID textField
>
>   The user's primary email address.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * productId string required
>
>     * skuId string required
>
>     * licenseUserId string required
>
> - output object
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * content-type string
>
>     * vary string
>
>     * date string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string

### Make a Custom API Call

Define and use your own call to the Google Workspace Admin REST API

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Endpoint textField required
>
>   The Workspace API endpoint, such as "https\://admin.googleapis.com/admin/directory/v1/users/user\@example.com".
>
> - HTTP Method dropDown required
>
>   The HTTP method of the API call.
>
>   * GET
>
>   * POST
>
>   * PUT
>
>   * DELETE
>
> - Query Parameters keyValueList
>
>   Query parameters for the request.
>
> - Additional Headers keyValueList
>
>   Define additional headers to send to Workspace. Learn more in the Google Workspace API documentation.
>
> - Body codeEditor
>
>   The body of the API call.
>
> * default object
>
>   * properties object
>
>     * privateKey string required
>
>     * iss string required
>
>     * sub string required
>
>     * endpoint string required
>
>     * method string required
>
> - output object
>
>   * rawResponse object
>
>   * statusCode integer
>
>   * headers object
>
>     * etag string
>
>     * content-type string
>
>     * vary string
>
>     * date string
>
>     * server string
>
>     * content-length string
>
>     * x-xss-protection string
>
>     * x-frame-options string
>
>     * x-content-type-options string
>
>     * alt-svc string
>
>     * connection string
