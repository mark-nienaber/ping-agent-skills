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

---

---
title: Administrator MFA
description: Submit your requests to manage customer IAM Administrator MFA through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_admin_mfa
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_admin_mfa.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Administrator MFA

Submit your requests to manage customer IAM Administrator MFA through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **Platform service requests → Administrator MFA**.

3. In the**Administrator(s)** field, enter the administrator name.

4. In the **Desired MFA setting** field, indicate whether you want to enable or disable MFA.

5. In the **MFA contact method** field, indicate whether the MFA contact method will be email or phone number.

6. In the **MFA contact info** field, provide the MFA information (email address or phone number).

7. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

8. Enter a description of your request in the **Description** field.

9. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

10. Click **Save** to submit your request.

---

---
title: Backup and restoration
description: PingFederate and PingDirectory support full and incremental backups, which can be customized to meet your needs. Submit your backup and restoration requests through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_backup_restore
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_backup_restore.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Backup and restoration

PingFederate and PingDirectory support full and incremental backups, which can be customized to meet your needs. Submit your backup and restoration requests through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **Platform service requests > Backup and restoration**.

3. In the **Product** field, indicate whether your request is regarding PingAccess, PingDirectory, or PingFederate.

4. Select the appropriate description in the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Certificates
description: The administrative console provides a suite of configuration wizards for you to manage keys and certificates for various purposes. Learn more in Certificate and key management in the PingFederate documentation.
component: pgic
page_id: pgic:service_requests:p14g_certificates
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_certificates.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Certificates

The administrative console provides a suite of configuration wizards for you to manage keys and certificates for various purposes. Learn more in [Certificate and key management](http://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_certificate_key_management.html) in the PingFederate documentation.

However, if infrastructure changes are required, submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingFederate service requests → Certificates**.

3. Select the appropriate description in the **Certificate type** list:

   * Client certificate

   * SSL server certificate

   * Trusted certificate authorities

   * Other

4. Select the appropriate description in the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Certificates
description: You can import certificates into PingAccess to establish anchors used to define trust to certificates presented during secure HTTPS connections. Refer to Certificates for additional information. However, if infrastructure changes are required, submit a request through the service request form. This form is accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_pa_certificates
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_pa_certificates.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Certificates

You can import certificates into PingAccess to establish anchors used to define trust to certificates presented during secure HTTPS connections. Refer to [Certificates](http://docs.pingidentity.com/pingaccess/latest/pingaccess_user_interface_reference_guide/p14g_pa_certificates.html) for additional information. However, if infrastructure changes are required, submit a request through the service request form. This form is accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingAccess service requests → Certificates**.

3. Select the appropriate description from the **Certificate type** list:

   * SSL client keys and certificate

   * Signing and decryption keys and certificates

   * Other

4. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Certificates
description: To add or replace a server certificate (an LDAPS/HTTPS certificate), submit a request through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_server_certificate
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_server_certificate.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Certificates

To add or replace a server certificate (an LDAPS/HTTPS certificate), submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

Administrators have the option of using self-signed certificates or CA-signed certificates for the server certificate. Where possible, we encourage the use of CA-signed certificates. Self-signed certificates are only recommended for demonstration and proof-of-concept environments. The certificate can also be generated automatically.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingDirectory service requests → Certificates**.

3. In the **Certificate to add or replace** field, enter the name of the certificate you want to add or replace.

4. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save**.

8. Click the **Attachments** tab and upload the certificate you want to add or replace.

---

---
title: Client connection policies
description: To modify client connection policies, submit a request through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_client_connection_policies
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_client_connection_policies.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Client connection policies

To modify client connection policies, submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

Client connection policies specify criteria for membership based on information about the client connection, including client address, protocol, communication security, and authentication state and identity. The client connection policy, however, does not control membership based on the type of request being made.

Client connection policies are based on two things:

* **Connection criteria**: Connection criteria is used by the client connection policies, but it is also used when the server needs to match connection-level properties, such as filtered logging. A single connection can match multiple connection criteria definitions.

* **Evaluation order index**: If multiple client connection policies are defined in the server, then each of them must have a unique value for the evaluation-order-index property. Client connection policies are evaluated in order of ascending evaluation order index. If a client connection does not match the criteria for any defined client connection policy, that connection is terminated.

  If the connection policy matches a connection, the connection is assigned to that policy and no further evaluation occurs. If, after evaluating all the defined client connection policies, no match is found, the connection is terminated.

  Learn more in [Configuring a client connection policy using the console](http://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_config_client_connection_policy_console.html) or [Configuring a client connection policy using disconfig](http://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_config_client_connection_policy_dsconfig.html) in the PingDirectory documentation.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingDirectory service requests > Client connection policies**.

3. In the **Client connection policy** field, describe the change you want to make.

4. Select the appropriate description in the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Conditional DNS Forwarding
description: Submit requests to change your Conditional Forwarders through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_conditional_dns_forwarding
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_conditional_dns_forwarding.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Conditional DNS Forwarding

Submit requests to change your Conditional Forwarders through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

DNS forwarding is the process by which particular sets of DNS queries are handled by a designated server, rather than being handled by the initial server contacted by the client. Usually, all DNS servers that handle address resolution within the network are configured to forward requests for addresses that are outside the network to a dedicated forwarder.

You can find additional information in [DNS Forwarding and Conditional Forwarding](https://medium.com/tech-jobs-academy/dns-forwarding-and-conditional-forwarding-f3118bc93984) on Medium.com.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **Platform service requests → Conditional DNS forwarding**.

3. In the **DNS rules** field, provide information regarding the request.

4. Select the appropriate description in the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Customer network connection
description: To modify connectivity settings between the platform and your on-premise directory, move endpoints, or review network-level routing, submit your request through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_customer_network_connection
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_customer_network_connection.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Customer network connection

To modify connectivity settings between the platform and your on-premise directory, move endpoints, or review network-level routing, submit your request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **Platform service requests → Customer network connection**.

3. In the **Connectivity setting request** field, provide information regarding your request.

4. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Deployment scaling
description: To scale deployments or down for testing purposes, or if you expect an increase in usage, submit a request through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_deployment_scaling
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_deployment_scaling.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Deployment scaling

To scale deployments or down for testing purposes, or if you expect an increase in usage, submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **Platform service requests → Deployment scaling**.

3. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

4. Provide a description of your request in the **Description** field.

5. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

6. Click **Save** to submit your request.

---

---
title: DNS routing
description: Submit your routing policy requests through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_dns_routing
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_dns_routing.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# DNS routing

Submit your routing policy requests through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **Platform service requests → DNS routing**.

3. In the **Routing rules** field, provide information regarding your request.

4. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Elevate admin
description: To request additional permissions for your administrators, such as managing certificates or users, submit a request through the service request form, accessible from the Support & Community page. You can also request that administrators receive full administration permissions, which will allow them to perform all administrative tasks.
component: pgic
page_id: pgic:service_requests:p14g_elevate_admin
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_elevate_admin.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Elevate admin

To request additional permissions for your administrators, such as managing certificates or users, submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/). You can also request that administrators receive full administration permissions, which will allow them to perform all administrative tasks.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingFederate service requests > Elevate admin**.

3. In the **Admin Name(s)** field, provide the names of the administrators who you want to be granted the requested permissions.

4. In the **Permissions** field, select all the permissions that you want to grant to these administrators.

   * **Crypto Administration**: Administrators can manage certificates.

   * **User Administration**: Administrators can manage users.

   * **Full Administration**: Administrators can perform all administrative tasks.

   |   |                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------- |
   |   | If you want administrators to be granted different permissions, submit separate requests for each. |

5. Enter a description of your request in the **Description** field.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save** to submit your request.

---

---
title: Email notifications
description: To customize email notifications, perhaps for branding purposes, submit a request through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_email_notifications
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_email_notifications.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Email notifications

To customize email notifications, perhaps for branding purposes, submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

PingFederate delivers messages to administrators and end users based on notification publisher settings. Each component that is capable of triggering or handling events might use a different notification publisher instance to deliver its messages. For example, you could select an SMTP Notification Publisher instance to deliver messages to your end users in an HTML Form Adapter instance and another SMTP Notification Publisher instance to deliver licensing messages to other administrators.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingFederate service requests → Email notifications**.

3. Specify the type of event for which email notifications should be sent in the **Event type** field. For example:

   * Local administrative account management events

   * Certificate events

   * SAML metadata update events

   * Licensing events

   * HTML form adapter events

4. Specify the subject for the email notification in the **Email subject** field.

5. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

6. Enter a description of your request in the **Description** field.

7. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

8. Click **Save**.

9. Click the **Attachments** tab and upload a `.zip` archive that contains all files in the template directory you are updating. Request the latest instance of these files before making your update, if necessary.

---

---
title: Email templates
description: To modify email templates, submit a request through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_email_templates
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_email_templates.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Email templates

To modify email templates, submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

You can use PingDirectory email templates in a variety of ways. An example email template is provided in the Delegated Admin package at the top level in the `delegated-admin-account-created.template` file. This template provides a multipart text and HTML email to the user with their username and initial password, along with a self-service link they can use to log on to PingFederate and change their password and profile information.

Learn morein [Editing and copying the email template to the PingDirectory server](http://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/.html) in the PingDirectory documentation.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingDirectory service requests > Email templates**.

3. In the **State of template** field, indicate whether you want to enable or disable the template.

4. (Optional) If your PingFederate local identity profile is used, provide the externally accessible URL of the profile management endpoint in the **Profile management URL** field.

5. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

6. Enter a description of your request in the **Description** field.

7. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

8. Click **Save**.

9. Click the **Attachments** tab and upload a `.zip` archive that contains all files in the template directory you are updating. Request the latest instance of these files before making your update, if necessary.

---

---
title: Indexes
description: Submit your index change requests through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_indexes
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_indexes.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Indexes

Submit your index change requests through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

Indexes improve database search performance and provide consistent search rates, regardless of the number of database objects stored in the Directory Information Tree (DIT), and are associated with attributes within your schema. To add an index, attributes must already exist in the schema defined for your directory. To delete an index, ensure that data is removed from user entries prior to it being deleted or data modification issues and application errors will exist.

Learn more in [Working with indexes](http://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_work_with_indexes.html) in the PingDirectory documentation.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingDirectory service requests → Indexes**.

3. In the **Index name** field, provide the name of the index.

4. Select the appropriate type of index from the **Index type(s)** list:

   * Equality

   * Substring

   * Ordering

   * Approximate

   * Presence

5. In the **Purpose** field, explain what you want to achieve by making this change.

6. (Optional) In the **Other** field, provide additional information about your indexing requirements that might require followup.

7. Select the appropriate description in the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

8. Enter a description of your request in the **Description** field.

9. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

10. Click **Save** to submit your request.

---

---
title: JSON field constraints
description: Submit your requests to define JSON field constraints through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_json_field_constraint
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_json_field_constraint.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# JSON field constraints

Submit your requests to define JSON field constraints through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

You can define a number of constraints for the fields included in JSON objects stored in values of a specified attribute type. For example, you can require that a field value is a specific data type and specify whether a field is required or optional. You can also specify whether a field can have multiple values or restrict values of string fields to a predefined set of values.

Learn more in [About managing JSON attribute values](http://docs.pingidentity.com/pingdirectory/latest/pingdirectory_server_administration_guide/pd_ds_manage_json_attr_values.html) in the PingDirectory documentation.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. In the **Capability** list, select **PingDirectory service requests > JSON field constraints**.

3. In the **Attribute type** field, enter the name or OID of the LDAP attribute type whose values will be subject to the associated field constraints. This attribute type must be defined in the server schema, and it must have a `JSON object` syntax.

4. (Optional) Select the **Allow unnamed fields** checkbox to indicate whether JSON objects stored as values of attributes with the associated attribute type are permitted to include fields for which there is no subordinate JSON field constraints definition. If unnamed fields are allowed, no constraints are imposed on the values of those fields.

5. In the **JSON** field, specify the path to the target field as a string with the hierarchy levels separated by periods. If a field name in the hierarchy includes a period, replace the period with a backslash.

6. In the **Value type** field, select the expected data type for the target field:

   * String

   * Number

   * Object

   * Boolean

   * Integer

   * Any

7. (Optional) Select the **Is required** checkbox to indicate that the target field must be present.

8. In the **Is array** field, specify whether the target field can be an array. If so, all the elements of the array must be of the type specified in the **Value type** field.

   * Required

   * Optional

   * Prohibited

9. (Optional) Select the **Allow null value** checkbox if the target field can have a value of `null` as an alternative to the specified value type.

10. (Optional) Select the **Allow empty object** checkbox if the value of the target field is a JSON object (or an array of JSON objects) and empty objects are permitted.

11. (Optional) Select the **Index values** checkbox if the target field should be indexed.

12. Select the appropriate description from the **Business Priority** list:

    * Change needed by deadline to avoid business impact

    * Change modifies existing functionality

    * Change adds new functionality

13. Enter a description of your request in the **Description** field.

14. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

15. Click **Save** to submit your request.

---

---
title: Launch and terminate environments
description: When the platform initially opens, you will see your environments and the status of those environments. Submit your requests to launch and terminate environments through the service request form, accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_launch_term_environments
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_launch_term_environments.html
revdate: May 6, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Launch and terminate environments

When the platform initially opens, you will see your environments and the status of those environments. Submit your requests to launch and terminate environments through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## About this task

You can have up to four environments active at one time (one per stage), but trial accounts are limited to two. If you exceed your limit, the system displays a message informing you that you have reached the maximum number of active environments allowed for your account. NOTE: Deployed environments are automatically deleted after two hours of inactivity.

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Indicate whether the environment is a development, test, staging, or production environment.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **Platform service requests → Launch/terminate environments**.

3. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

4. Enter a description of your request in the **Description** field.

5. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

6. Click **Save** to submit your request.

---

---
title: Localization
description: Administrators can provide localized versions of user-facing status messages generated by PingAccess. To change messages for localization purposes, submit a request through the service request form. This form is accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_localization
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_localization.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Localization

Administrators can provide localized versions of user-facing status messages generated by PingAccess. To change messages for localization purposes, submit a request through the service request form. This form is accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingAccess service requests → Localization**.

3. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

4. In the **Description** field, describe the localization update request.

5. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

6. Click **Save**.

7. Click the **Attachments** tab and upload a `.zip` file that contains all files in the language-packs directory you are updating. Request the latest instance of these files from us before making your update, if necessary.

---

---
title: Localization
description: "PingFederate supports localization for three types of end-user messages: on-screen messages, email messages, and text messages (SMS). To change any of these messages for localization purposes, submit a request through the service request form, accessible from the Support & Community page."
component: pgic
page_id: pgic:service_requests:p14g_pf_localization
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_pf_localization.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Localization

PingFederate supports localization for three types of end-user messages: on-screen messages, email messages, and text messages (SMS). To change any of these messages for localization purposes, submit a request through the service request form, accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingFederate service requests → Localization**.

3. Select the type of message you want to localize from the **Message type** list:

   * Email messages

   * On-screen messages

   * Text messages (SMS)

4. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

5. In the **Description** field, describe the localization update request.

6. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

7. Click **Save**.

8. Click the **Attachments** tab and upload a `.zip` file that contains all the files in the language-packs directory you are updating. Request the latest instance of these files from us before making your update, if necessary.

---

---
title: Logging settings
description: PingAccess generates logs that record server events. To change the log settings so that more or less data is obtained in the log files, submit a request through the service request form. This form is accessible from the Support & Community page.
component: pgic
page_id: pgic:service_requests:p14g_logging_settings
canonical_url: http://docs.pingidentity.com/pgic/service_requests/p14g_logging_settings.html
revdate: May 6, 2024
section_ids:
  steps: Steps
---

# Logging settings

PingAccess generates logs that record server events. To change the log settings so that more or less data is obtained in the log files, submit a request through the service request form. This form is accessible from the [Support & Community page](https://support.pingidentity.com/s/).

## Steps

1. Complete the following fields:

   * **Subject**: Enter a description of your request, including the action to be taken.

   * **Environment Type**: Specify the type of environment affected by this request.

   * **Proposed Change Window**: Specify the dates or times in which you want the work complete.

2. From the **Capability** list, select **PingAccess service requests → Logging settings**.

3. In the **Logging files** field, provide the name of the affected logging files. For example, `pingaccess-engine_audit.log` or `pingaccess_agent_audit.log`.

4. In the**Log level** field, select the level of logging you want to obtain:

   * Trace

   * Debug

   * Error

   * Info

   * Warn

5. In the **Logging events** field, specify affected logging events.

6. Select the appropriate description from the **Business Priority** list:

   * Change needed by deadline to avoid business impact

   * Change modifies existing functionality

   * Change adds new functionality

7. Enter a description of your request in the **Description** field.

8. If you are tracking your request within your organization, enter the tracking ID or ticket number associated with it in the **Customer Tracking ID** field.

9. Click **Save** to submit your request.