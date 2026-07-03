---
title: Access control in AWS using session tags
description: Amazon Web Services (AWS) session tags allow enterprises to use Ping Identity products for attribute-based access control (ABAC) in the AWS Single Sign-On (SSO) service.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_access_control_in_aws_using_session_tags
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_access_control_in_aws_using_session_tags.html
revdate: July 3, 2024
---

# Access control in AWS using session tags

Amazon Web Services (AWS) session tags allow enterprises to use Ping Identity products for attribute-based access control (ABAC) in the AWS Single Sign-On (SSO) service.

For information and configuration steps, see [Amazon Web Services session tags integrations](../amazon_web_services_session_tags_integrations_guide/pf_awssessiontags_integration_amazon_web_services_session_tags_integrations_guide.html) in the Ping Identity integration documentation.

---

---
title: Amazon IdP Adapter settings reference
description: Field descriptions for the Amazon IdP Adapter configuration page.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_amazon_idp_adapter_settings_reference
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_amazon_idp_adapter_settings_reference.html
revdate: October 24, 2025
section_ids:
  standard-fields: Standard fields
  advanced-fields: Advanced fields
---

# Amazon IdP Adapter settings reference

Field descriptions for the Amazon IdP Adapter configuration page.

## Standard fields

> **Collapse: Details**
>
> | Field                               | Description                                                                                                                                                                                                                                                                                                                                                   |
> | ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Client ID**                       | The client ID that you noted in [Registering PingFederate as a security profile in Amazon](pf_amazon_cic_registering_pf_as_a_security_profile_in_amazon.html).                                                                                                                                                                                                |
> | **Client Secret**                   | The client secret that you noted in [Registering PingFederate as a security profile in Amazon](pf_amazon_cic_registering_pf_as_a_security_profile_in_amazon.html).                                                                                                                                                                                            |
> | **Error Redirect URL**              | When an error occurs in the adapter, PingFederate redirects the browser to this URL instead of the default error page.This field is blank by default.                                                                                                                                                                                                         |
> | **Unauthorized Redirect URL**       | When a user denies the requested Amazon permissions, PingFederate redirects the browser to this URL instead of the default error page.This field is blank by default.                                                                                                                                                                                         |
> | **Authorization Callback Endpoint** | The PingFederate endpoint that Amazon uses to respond to authorization requests. If you set a custom endpoint in the **Authorization callback URL** field in [Registering PingFederate as a security profile in Amazon](pf_amazon_cic_registering_pf_as_a_security_profile_in_amazon.html), change this field to match.This default value is `/amazon-authn`. |

## Advanced fields

> **Collapse: Details**
>
> | Field                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
> | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | **Amazon Authorization URL**    | The URL that PingFederate uses to send authentication requests to Amazon. If Amazon changes this endpoint, enter the new URL.The default value is `https://amazon.com/ap/oa`.                                                                                                                                                                                                                                                           |
> | **Amazon Access Token URL**     | The URL that PingFederate uses to retrieve access tokens from Amazon. If Amazon changes this endpoint, enter the new URL.The default value is `https://amazon.com/auth/02/token`.                                                                                                                                                                                                                                                       |
> | **Amazon User Info URL**        | The URL that PingFederate uses to retrieve user data from Amazon.The default value is `https://api.amazon.com/user/profile`.                                                                                                                                                                                                                                                                                                            |
> | **Scopes**                      | The scopes that you want to request from Amazon. Separate scopes with a space.The default value is `profile`.                                                                                                                                                                                                                                                                                                                           |
> | **Amazon Sign-On Presentation** | Determines how the adapter presents the Amazon sign-on form:- Redirect (default)
>
>   The adapter redirects the browser to the Amazon sign-on form.
>
> - Pop-up window
>
>   The adapter opens a new window with the Amazon sign-on form on a PingFederate template. Use this option if automatic redirects are blocked by your users' browsers.This setting has no effect when using the adapter through the PingFederate authentication API. |
> | **Amazon Pop-Up Template**      | The template file that presents the Amazon sign-on form. Applies only when **Amazon Login Presentation** is set to **Pop-up window**.The default value is `amazon-pop-up-template.html`.                                                                                                                                                                                                                                                |
> | **Amazon Post-Auth Template**   | The template file that the adapter presents after the user signs on. Applies only when **Amazon Login Presentation** is set to **Pop-up window**.The default value is `amazon-post-auth-template.html`.                                                                                                                                                                                                                                 |
> | **Amazon Messages File**        | The language-pack file associated with the Amazon pop-up template.The default value is `pingfederate-amazon-adapter-messages`.                                                                                                                                                                                                                                                                                                          |
> | **Retry Request**               | Determines whether PingFederate will retry requests after it receives a response with a failure code.This checkbox is cleared by default.                                                                                                                                                                                                                                                                                               |
> | **Maximum Retries Limit**       | Determines how many times PingFederate retries a request.The default value is `5`.                                                                                                                                                                                                                                                                                                                                                      |
> | **Retry Error Codes**           | A list of response codes that should trigger a retry. Separate response codes with a comma.The default value is `403`.                                                                                                                                                                                                                                                                                                                  |
> | **API Request Timeout**         | The amount of time in milliseconds that PingFederate waits for Amazon to respond to requests. A value of `0` disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                                                          |
> | **Connection Timeout**          | The amount of time in milliseconds that PingFederate allows to establish a connection with Amazon. A value of 0 disables the timeout.The default value is `5000`.                                                                                                                                                                                                                                                                       |
> | **Proxy Settings**              | Defines proxy settings for outbound HTTP requests.The default value is **System Defaults**.                                                                                                                                                                                                                                                                                                                                             |
> | **Custom Proxy Host**           | The proxy server host name to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                          |
> | **Custom Proxy Port**           | The proxy server port to use when **Proxy Settings** is set to **Custom**.This field is blank by default.                                                                                                                                                                                                                                                                                                                               |

---

---
title: Amazon integrations
description: The Amazon Login Integration Kit allows PingFederate to use Amazon as an identity provider (IdP). This allows users to access service provider (SP) applications by signing on to Amazon.
component: amazon
page_id: amazon::pf_is_overview_of_amazon_integrations
canonical_url: https://docs.pingidentity.com/integrations/amazon/pf_is_overview_of_amazon_integrations.html
revdate: October 24, 2025
section_ids:
  amazon-login-integration-kit-formerly-the-amazon-cloud-identity-connector: Amazon Login Integration Kit (formerly the Amazon Cloud Identity Connector)
  aws-connector: AWS Connector
  aws-iam-identity-center-provisioner-aws-single-sign-on-connector: AWS IAM Identity Center Provisioner (AWS Single Sign-On Connector)
  amazon-web-services-session-tags-integrations-for-pingfederate-and-pingone: Amazon Web Services session tags integrations for PingFederate and PingOne
---

# Amazon integrations

## Amazon Login Integration Kit (formerly the Amazon Cloud Identity Connector)

The Amazon Login Integration Kit allows PingFederate to use Amazon as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*. This allows users to access service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications by signing on to Amazon.

## AWS Connector

The Amazon Web Services (AWS) Connector allows PingFederate to integrate with Amazon's AWS Identity and Access Management service for provisioning and single sign-on (SSO) *(tooltip: \<div class="paragraph">
\<p>The process of authenticating an identity (signing on) at one website (usually with a user ID and password) and then accessing resources secured by other domains without reauthenticating.\</p>
\</div>)*.

## AWS IAM Identity Center Provisioner (AWS Single Sign-On Connector)

The AWS IAM Identity Center Provisioner allows PingFederate to integrate with Amazon's AWS IAM Identity Center service for provisioning and SSO.

## Amazon Web Services session tags integrations for PingFederate and PingOne

AWS session tags allow enterprises to use Ping Identity products for attribute-based access control (ABAC) *(tooltip: \<div class="paragraph">
\<p>Access control based on attributes of a user, such as how old a user is or whether the user is a paying customer.\</p>
\</div>)* in AWS. Includes instructions for PingFederate and PingOne for Customers using Security Assertion Markup Language (SAML) *(tooltip: \<div class="paragraph">
\<p>A standard, XML-based, message-exchange framework enabling the secure transmittal of authentication tokens and other user attributes across domains.\</p>
\</div>)* or OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)*.

---

---
title: Amazon Login Integration Kit
description: The Amazon Login Integration Kit (formerly the Amazon Cloud Identity Connector) allows PingFederate to use Amazon as an identity provider (IdP). This allows users to access service provider (SP) applications by signing on to Amazon.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic.html
revdate: October 24, 2025
section_ids:
  features: Features
  components: Components
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Amazon Login Integration Kit

The Amazon Login Integration Kit (formerly the Amazon Cloud Identity Connector) allows PingFederate to use Amazon as an identity provider (IdP) *(tooltip: \<div class="paragraph">
\<p>A service that manages identity information and provides authentication services to relying clients or SPs within a federated or distributed network.\</p>
\</div>)*. This allows users to access service provider (SP) *(tooltip: \<div class="paragraph">
\<p>In SAML, an entity that receives and accepts an authentication assertion issued by an IdP, typically for the purpose of allowing access to a protected resource.\</p>
\</div>)* applications by signing on to Amazon.

## Features

* Supports the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Supports the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Components

* Amazon IdP Adapter

  * Allows PingFederate to communicate with the Amazon API to process sign-on requests and get user information.

* Templates

  * Allows the adapter to prompt the user to sign on. The template can be presented with a browser redirect or as a pop-up window.

  * Allows you to modify the appearance of the sign-on prompt.

* Language packs

  * Allows you to customize or localize the messages returned by the PingFederate authentication API and shown on the templates during authentication.

    Learn more in [Localizing messages for end users](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_local_message_end_users.html) in the PingFederate documentation.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following sections of the PingFederate documentation:

* [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html)

* [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html)

* [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html)

* [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html)

## System requirements

* PingFederate 11.3 or later

* An Amazon developer account

---

---
title: Amazon Web Services Connector
description: The Amazon Web Services (AWS) Connector allows PingFederate to integrate with Amazon's AWS Identity and Access Management service for provisioning and single sign-on (SSO).
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector.html
revdate: July 3, 2024
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# Amazon Web Services Connector

The Amazon Web Services (AWS) Connector allows PingFederate to integrate with Amazon's AWS Identity and Access Management service for provisioning and single sign-on (SSO).

## Features

* Manages users in Amazon Web Services based on changes in an external data store that is attached to PingFederate.

  * Creates, updates, and deletes users.

  * Allows you to enable the create, update, and delete capabilities independently.

* Manages groups

  * Creates groups

  * Updates group memberships and names.

* Enables browser-based SSO initiated by the identity provider (IdP).

* Pre-populates some connection settings with the included quick connection template.

* Supports the following attributes: `UserName`, `Password`, and `PasswordResetRequired`.

* Pre-populates some connection settings with the included quick connection template.

## Intended audience

This document is intended for PingFederate administrators.

Before you start, you should be familiar with the following:

* The following sections of the Amazon Web Services documentation:

  * [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)

  * [IAM Users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html)

* The following sections of the PingFederate documentation:

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_managedatasourcestasklet_managedatasourcesstate.html)

  * [Managing IdP adapters](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_managing_idp_adapters.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 8.0 or later.

* To allow PingFederate to make outbound connections to Amazon Web Services, you might need to allow the following endpoint in your firewall:

  * https\://iam.amazonaws.com

---

---
title: Amazon Web Services Session Tags Integrations Guide
description: Amazon Web Services (AWS) session tags allow enterprises to use Ping Identity products for attribute-based access control (ABAC) in the AWS Identity and Access Management (IAM) and AWS IAM Identity Center services.
component: amazon
page_id: amazon:amazon_web_services_session_tags_integrations_guide:pf_awssessiontags_integration_amazon_web_services_session_tags_integrations_guide
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_session_tags_integrations_guide/pf_awssessiontags_integration_amazon_web_services_session_tags_integrations_guide.html
revdate: July 3, 2024
---

# Amazon Web Services Session Tags Integrations Guide

Amazon Web Services (AWS) session tags allow enterprises to use Ping Identity products for attribute-based access control (ABAC) in the AWS Identity and Access Management (IAM) and AWS IAM Identity Center services.

ABAC helps enterprises simplify fine-grained access to AWS resources by using attributes from their corporate directories in permissions rules.

When an employee federates into AWS from a standards-compliant identity provider (IdP) such as PingFederate or PingOne for Enterprise, the administrator can include attributes such as cost center, job title, and email address in the AWS session. These attributes function as session tags and can be matched to tags on AWS resources to control their access to resources during their AWS session.

For example, an employee with job title "Systems Engineer" and cost center "Stratford" could be granted write access to an Amazon EC2 table that is also tagged with cost center "Stratford."

You can configure PingFederate or PingOne for Enterprise to send attributes in the AWS sessions when your users federate into AWS. Then, you can implement a policy in AWS that evaluates the attributes from PingFederate or PingOne for Enterprise to control access to AWS resources.

For more information, see the following:

* [Attributes for Access Control](https://docs.aws.amazon.com/singlesignon/latest/userguide/attributesforaccesscontrol.html) in the AWS IAM Identity Center documentation.

* [IAM Tutorial: Use SAML session tags for ABAC](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_abac-saml.html) in the AWS IAM documentation.

To use AWS session tags for ABAC, complete the steps in one or more of the following topics.

---

---
title: Authentication API Support
description: You can use the PingFederate authentication API to integrate the Amazon IdP Adapter into your application.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_authentication_api_support
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_authentication_api_support.html
revdate: June 10, 2024
---

# Authentication API Support

You can use the PingFederate authentication API to integrate the Amazon IdP Adapter into your application.

The PingFederate Authentication API provides access to the current state of the authentication flow as a user steps through the PingFederate authentication policy. You can find more information in [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html) in the PingFederate documentation.

To integrate the Amazon IdP Adapter into your authentication flow, configure your application based on the states, actions, and models available in the PingFederate Authentication API Explorer. Learn more in [Exploring the Authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_exploring_authentication_api.html) in the PingFederate documentation.

---

---
title: Available user attributes
description: The following table lists the attributes Amazon supports.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_available_user_attributes
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_available_user_attributes.html
revdate: October 24, 2025
---

# Available user attributes

The following table lists the attributes Amazon supports.

| Attribute      | Description                                                |
| -------------- | ---------------------------------------------------------- |
| `access_token` | The access token that Amazon provides to your application. |
| `email`        | The user's email address.                                  |
| `name`         | The user's name.                                           |
| `postal_code`  | The user's shipping postal code for the Amazon account.    |
| `user_id`      | The user's Amazon ID.                                      |

---

---
title: AWS IAM Identity Center Provisioner
description: The AWS IAM Identity Center Provisioner allows PingFederate to integrate with Amazon's AWS IAM Identity Center service for provisioning and single sign-on (SSO).
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector.html
revdate: January 20, 2026
section_ids:
  features: Features
  intended-audience: Intended audience
  system-requirements: System requirements
---

# AWS IAM Identity Center Provisioner

The AWS IAM Identity Center Provisioner allows PingFederate to integrate with Amazon's AWS IAM Identity Center service for provisioning and single sign-on (SSO).

## Features

* Manages users in AWS IAM Identity Center based on changes in a datastore that is attached to PingFederate.

  * Creates, updates, disables, and deletes users.

  * Allows you to enable the create, update, disable, and delete capabilities independently.

  * Allows you to provision disabled users.

  * Allows you to choose whether to disable or delete users when deprovisioning.

* Manages groups in AWS IAM Identity Center based on changes in an external data store that is attached to PingFederate.

  * Creates and deletes groups.

  * Updates group memberships.

* Enables browser-based SSO initiated by the service provider (SP) or identity provider (IdP).

* Pre-populates some connection settings with the included quick connection template.

## Intended audience

This document is intended for PingFederate administrators.

If you need help during the setup process, see the following resources:

* AWS IAM Identity Center documentation:

  * [What Is AWS Single Sign-On?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)

  * [IAM Identity Center prerequisites and considerations](https://docs.aws.amazon.com/singlesignon/latest/userguide/identity-center-prerequisites.html)

  * [Users, Groups, and Provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/users-groups-provisioning.html)

  * [SCIM Profile and SAML 2.0 Implementation](https://docs.aws.amazon.com/singlesignon/latest/userguide/scim-profile-saml.html)

  * [Automatic Provisioning](https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html)

  * [Using Ping Identity products with IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/pingidentity.html)

* PingFederate documentation:

  * [SP connection management](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_sp_connect_management.html)

  * [Identity provider SSO configuration](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_ident_provid_sso_config.html)

  * [Managing digital signing certificates and decryption keys](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_certmanagementtasklet_dsigsigningcert_certmanagementstate.html)

  * [Datastores](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_datastores.html)

  * [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html)

  * [Configuring outbound provisioning settings](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_protocolsettingstasklet_saasglobalprovisioningsettingsstate.html)

## System requirements

* PingFederate 9.0 or later.

* An AWS IAM Identity Center administrator account.

* To allow PingFederate to make outbound connections to the AWS IAM Identity Center API, you might need to allow the following domain in your firewall:

  * https\://aws.amazon.com

---

---
title: Changelog
description: The following is the change history for the Amazon Login Integration Kit (formerly the Amazon Cloud Identity Connector).
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_changelog
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_changelog.html
revdate: February 19, 2026
section_ids:
  version-1-1-2-january-2026: Version 1.1.2 - January 2026
  version-1-1-1-november-2025: Version 1.1.1 – November 2025
  version-1-1-november-2020: Version 1.1 – November 2020
  version-1-0-october-2019: Version 1.0 – October 2019
---

# Changelog

The following is the change history for the Amazon Login Integration Kit (formerly the Amazon Cloud Identity Connector).

## Version 1.1.2 - January 2026

* Removed third-party fonts and the `authn-api-messages.properties` file.

## Version 1.1.1 – November 2025

* Updated Apache Commons Text library version to address a potential security vulnerability.

## Version 1.1 – November 2020

* Added a setting to use browser redirect or pop-up window for the sign-on presentation.

* Added customizable sign-on templates for the pop-up window presentation.

* Added customizable user-facing language-pack messages.

* Added support for the [PingFederate authentication API](https://docs.pingidentity.com/pingfederate/latest/developers_reference_guide/pf_authentication_api.html).

* Added support for the [JavaScript Widget for the PingFederate Authentication API](https://github.com/pingidentity/pf-authn-js-widget).

## Version 1.0 – October 2019

* Initial release.

* Added support for social login using Amazon credentials.

* Added support for retrieving Amazon user information.

* Added settings for retrying failed request and maximum number of retries.

* Added an adapter setting to override system-default proxy settings.

* Added API connection timeout settings.

* Added Amazon API endpoints override settings.

* Added custom **Error Redirect** and **Unauthorized Redirect URL** settings.

---

---
title: Changelog
description: Amazon Web Services (AWS) Connector 2.0 – April 2019 (current release)
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_changelog.html
revdate: July 3, 2024
---

# Changelog

**Amazon Web Services (AWS) Connector 2.0 – April 2019 (current release)**

* Added support for the AWS 2.0 API.

* Added support for the `Password` and `PasswordResetRequired` attributes.

* Added the ability to update group names.

* Added the ability to disable the "create", "update", and "delete" capabilities individually.

* Added the ability to show debug information from the AWS API in the PingFederate server log. See [Show Amazon API errors in the server log](pf_aws_connector_show_amazon_api_errors_in_the_server_log.html).

* Added support for proxy connections.

* Improved error-handling and reporting behavior.

**Amazon Web Services Connector 1.0 – January 2014**

* Initial release.

* Added support for user and group provisioning.

* Added support for browser-based single sign-on.

---

---
title: Changelog
description: The following is the change history for the AWS IAM Identity Center Provisioner.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_changelog
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_changelog.html
revdate: January 20, 2025
section_ids:
  version-1-1-0-6-january-2026: Version 1.1.0.6 - January 2026
  version-1-1-0-5-january-2026: Version 1.1.0.5 - January 2026
  version-1-1-0-4-december-2025: Version 1.1.0.4 - December 2025
  version-1-1-0-3-november-2025: Version 1.1.0.3 - November 2025
  version-1-1-october-2024: Version 1.1 – October 2024
  version-1-0-october-2020: Version 1.0 – October 2020
---

# Changelog

The following is the change history for the AWS IAM Identity Center Provisioner.

## Version 1.1.0.6 - January 2026

* Fixed an issue with the SCIM API URL format for group members and users that caused `404` errors during provisioning. The adapter now adds a trailing slash between the base URL and the endpoint if it's missing.

## Version 1.1.0.5 - January 2026

* Replaced deprecated AWS IAM Identity Center PatchGroup `Remove All` and `Replace` operations with incremental `add` or `remove` `PATCH` updates. This change aligns with AWS requirements and prevents access disruptions and throttling issues when synchronizing large group memberships.

## Version 1.1.0.4 - December 2025

* Added the ability to retry `PATCH` requests automatically with an exponential delay to improve HTTP `429` error handling.

## Version 1.1.0.3 - November 2025

* The AWS IAM Identity Center Provisioner now sets the `User-Agent` HTTP header with a value of `PingFederate` when making `PATCH` requests.

  |   |                                                                                             |
  | - | ------------------------------------------------------------------------------------------- |
  |   | By default, AWS IAM Identity Center blocks `PATCH` requests that don't include this header. |

## Version 1.1 – October 2024

* Fixed an issue that prevented updates made to an existing user's `sAMAccountName` in the LDAP source from synchronizing with the [nickName](pf_aws_singlesignon_connector_supported_attributes_reference.html) attribute in the AWS platform.

## Version 1.0 – October 2020

* Initial release.

* Added support for user and group provisioning.

* Added support for AWS IAM Identity Center attributes.

* Added support for provisioning disabled users.

* Added configuration options for the create, update, and disable or delete capabilities.

* Added configuration options for deprovisioning actions.

---

---
title: Configuring an adapter instance
description: Configure the Amazon IdP Adapter to determine how PingFederate communicates with the Amazon authentication service.
component: amazon
page_id: amazon:amazon_login_integration_kit:pf_amazon_cic_configuring_an_adapter_instance
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_login_integration_kit/pf_amazon_cic_configuring_an_adapter_instance.html
revdate: October 24, 2025
section_ids:
  steps: Steps
---

# Configuring an adapter instance

Configure the Amazon IdP Adapter to determine how PingFederate communicates with the Amazon authentication service.

## Steps

1. Sign on to the PingFederate admin console.

2. On the **Identity Provider > Adapters** page, click **Create New Instance**.

3. On the **Type** tab, set the basic adapter instance attributes:

   1. In the **Instance Name** field, enter a name for the adapter instance.

   2. In the **Instance ID** field, enter a unique identifier for the adapter instance.

   3. In the **Type** list, select **Amazon IdP Adapter *\<version\_number>***. Click **Next**.

4. On the **IdP Adapter** tab, configure the adapter instance by referring to the [Amazon IdP Adapter settings reference](pf_amazon_cic_amazon_idp_adapter_settings_reference.html). Click **Next**.

5. On the **Actions** tab, click **Test Connection**. Resolve any issues, and then click **Next**.

6. On the **Extended Contract** tab, add any non-core attributes you want to include in the contract. Click **Next**.

   You can find a list of core contract attributes in [Available user attributes](pf_amazon_cic_available_user_attributes.html).

7. On the **Adapter Attributes** page, set pseudonym and masking options as shown in [Set pseudonym and masking options](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_setting_pseudonym_masking_options.html) in the PingFederate documentation. Click **Next**.

8. On the **Adapter Contract Mapping** page, configure the contract fulfillment details for the adapter as shown in [Define the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation. Click **Next**.

9. On the **Summary** tab, verify your configuration. Click **Done**.

10. On the **Manage IdP Adapter Instances** page, click **Save**.

---

---
title: Configuring AWS session tags for PingFederate OIDC connections
description: You can configure AWS Session Tag support for OpenID Connect (OIDC) connections in PingFederate.
component: amazon
page_id: amazon:amazon_web_services_session_tags_integrations_guide:pf_awssessiontags_integration_configuring_aws_session_tags_for_pf_oidc_connections
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_session_tags_integrations_guide/pf_awssessiontags_integration_configuring_aws_session_tags_for_pf_oidc_connections.html
revdate: July 3, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  result: Result
---

# Configuring AWS session tags for PingFederate OIDC connections

You can configure AWS Session Tag support for OpenID Connect (OIDC) connections in PingFederate.

## Before you begin

* If you want to use OGNL expressions to populate the values of the AWS session tags, see [Enabling and disabling expressions](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enable_disable_express.html) in the PingFederate documentation.

* Create an Amazon Web Services (AWS) console account and policy that uses session tags. For help, see [AWS prerequisites (page 241)](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-52.pdf#page=242) in the PingAccess documentation.

* Configure your PingFederate OAuth client for AWS console authentication.

* Define a PingFederate OpenID Connect policy. For help, see [Configuring OpenID Connect policies](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_configuring_oidc_policies.html) in the PingFederate documentation.

## Steps

1. Open your OpenID Connect policy.

   ### Choose from:

   * For PingFederate 10.1 or later: go to **Applications > OAuth > OpenID Connect Policy Management**.

   * For PingFederate 10.0 or earlier: go to **OAuth Server > OpenID Connect Policy Management**.

2. Select the client that you want to edit. Click **Attribute Contract**.

3. Create a new attribute and name it `http://aws.amazon.com/tags`. Click **Add**.

4. Click **Contract Fulfillment** and enter the required OGNL expression for the session tag.

   |   |                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------- |
   |   | You must construct the OGNL expression for the specific source data structure, as shown in the following example. |

   ![Screen capture of the Contract Fulfillment tab showing the appropriate values in the Attribute Contract, Source and value columns.](_images/joe1571947495981.png)

5. Click **Save**, then from **Policy** drop-down list, select the OpenID Connect policy you just created.

## Result

The ID token generated by PingFederate will include the following AWS Tags value:

```
https://aws.amazon.com/Tags:
{
"principal_tags ": {
          "project  ":["Project1],
          "cost_center": ["1234"]
        }
"transitive_tags": ["cost_center"]
}
```

---

---
title: Configuring AWS session tags for PingFederate SAML connections
description: You can configure AWS Identity and Access Management (IAM) and AWS IAM Identity Center session tag support for SAML connections in PingFederate.
component: amazon
page_id: amazon:amazon_web_services_session_tags_integrations_guide:pf_awssessiontags_integration_configuring_aws_session_tags_for_pf_saml_connections
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_session_tags_integrations_guide/pf_awssessiontags_integration_configuring_aws_session_tags_for_pf_saml_connections.html
revdate: July 3, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  result: Result
---

# Configuring AWS session tags for PingFederate SAML connections

You can configure AWS Identity and Access Management (IAM) and AWS IAM Identity Center session tag support for SAML connections in PingFederate.

## Before you begin

* If you want to use OGNL expressions to populate the values of the AWS session tags, see [Enabling and disabling expressions](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/pf_enable_disable_express.html) in the PingFederate documentation.

* Create an Amazon Web Services (AWS) console account and policy that uses session tags. For help, see [AWS prerequisites (page 241)](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-52.pdf#page=242) in the PingAccess documentation.

## Steps

1. Open your service provider (SP) connection. Go to **SP Connection > Browser SSO > Assertion Creation > Attribute Contract**.

2. Extend the contract of the AWS SP connection.

   ### Choose from:

   * If you are using AWS SSO, include the access control tags based on the following format:

     * `https://aws.amazon.com/SAML/Attributes/AccessControl:{attribute}`

       ![This screen capture shows the Attribute Contract tab with several example AWS SSO access control attributes.](_images/qld1605284905064.jpg)

   * If you are using AWS IAM, include the AWS Principal Tags and TransitiveTagKeys, based on the following examples:

     * `https://aws.amazon.com/SAML/Attributes/AccessControl:{attribute}`

     * `https://aws.amazon.com/SAML/Attributes/PrincipalTag:project`

     * `https://aws.amazon.com/SAML/Attributes/Role`

     * `https://aws.amazon.com/SAML/Attributes/RoleSessioName`

     * `https://aws.amazon.com/SAML/Attributes/TransitiveTagKeys`

   ![This screen capture shows the Attribute Contract tab with the example AWS IAM PrincipalTag and TransitiveTagKeys attributes.](_images/kwg1571947883022.png)

3. Go to **SP Connection > Browser SSO > Assertion Creation > IdP Adapter Mapping > Attribute Sources & User Lookup > Attribute Contract Fulfillment**.

4. Configure the attribute contract fulfillment for the AWS attributes.

   Example 1: This example shows AWS IAM Identity Center attributes mapped directly from an HTML Form Adapter instance.

   ![This screen capture shows the Attribute Contract Fulfillment tab with AWS IAM Identity Center attributes mapped to Adapter sources.](_images/jmq1605288110796.jpg)

   Example 2: This example shows AWS IAM attributes mapped from a data source and manipulated by the OGNL expression language available in PingFederate.

   ![This screen capture shows the Attribute Contract Fulfillment tab with AWS IAM attributes mapped to Adapter and LDAP sources.](_images/vaw1571948042845.png)

5. Click **Save**.

## Result

The AWS session tags are now included in the SAML assertion created by PingFederate.

---

---
title: Configuring AWS session tags for PingOne OIDC connections
description: You can configure AWS session tag support for OpenID Connect (OIDC) connections in PingOne by changing the attribute mappings in your OIDC application.
component: amazon
page_id: amazon:amazon_web_services_session_tags_integrations_guide:pf_awssessiontags_integration_configuring_aws_session_tags_for_p1_oidc_connections
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_session_tags_integrations_guide/pf_awssessiontags_integration_configuring_aws_session_tags_for_p1_oidc_connections.html
revdate: July 3, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
---

# Configuring AWS session tags for PingOne OIDC connections

You can configure AWS session tag support for OpenID Connect (OIDC) connections in PingOne by changing the attribute mappings in your OIDC application.

## Before you begin

* Create an Amazon Web Services (AWS) console account and policy that uses session tags. For help, see [AWS prerequisites (page 241)](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-52.pdf#page=242) in the PingAccess documentation.

* Sign on to your [PingOne account](https://admin.pingone.com/web-portal/login) as an administrator.

* Configure an external identity provider, such as PingFederate, with a `Tags` attribute. The value must be in JSON format as specified by the AWS session tag feature.

## Steps

1. Go to **Applications > OIDC.**

2. Select the application you want to edit and click **Edit**.

3. In the **Default User Profile Attribute Contract** section, click **Add Attribute**.

4. Enter `http://aws.amazon.com/tags` as shown, then click **Next**.

   ![This screen capture shows the Default User Profile Attribute Contract section with the AWS tag entered as an attribute.](_images/bej1571949193322.png)

5. In the **Attribute Mapping** section, map the `http://aws.amazon.come/tags` attribute to the external identity provider attribute that contains the JSON formatted session tags data as shown.

   ![This screen capture shows the Attribute Mapping section with the newly-created AWS attribute mapped to the external identity provider attribute.](_images/xmv1571949306074.png)

---

---
title: Configuring AWS session tags for PingOne SAML connections
description: You can create a custom SAML application to support AWS Identity and Access Management (IAM) and AWS IAM Identity Center session tags for SAML connections in PingOne.
component: amazon
page_id: amazon:amazon_web_services_session_tags_integrations_guide:pf_awssessiontags_integration_configuring_aws_session_tags_for_p1_saml_connections
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_session_tags_integrations_guide/pf_awssessiontags_integration_configuring_aws_session_tags_for_p1_saml_connections.html
revdate: July 3, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
  choose-from: Choose from:
---

# Configuring AWS session tags for PingOne SAML connections

You can create a custom SAML application to support AWS Identity and Access Management (IAM) and AWS IAM Identity Center session tags for SAML connections in PingOne.

## Before you begin

* Create an Amazon Web Services (AWS) console account and policy that uses session tags. For help, see [AWS prerequisites (page 241)](https://cdn-docs.pingidentity.com/archive/pdf/pingaccess/pingaccess-52.pdf#page=242) in the PingAccess documentation.

* Sign on to your [PingOne account](https://admin.pingone.com/web-portal/login) as an administrator.

* Configure an external identity provider, such as PingFederate, that will provide the values for the AWS attributes.

## About this task

|   |                                                                                                                                                                                                                                                                     |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In the PingOne App Catalog, PingOne provides a ready-made AWS application template. That template uses static SAML attributes, and cannot be used for session tags. The following steps allow you to create a custom SAML application to use with AWS session tags. |

## Steps

1. On the PingOne console, go to **Applications > My Applications > Add Application > New SAML Application**.

2. Enter an application name, such as `AWS with Session Tags`.

3. Enter the application description, category, and application icon and then click **Continue to Next Step**.

4. In the **Application Configuration** section, enter the following:

   1. In the **Assertion Consumer Service (ACS)**field, enter `https://signin.aws.amazon.com/saml`.

   2. In the **Entry ID** field, enter `urn:amazon:webservices`.

5. Click **Continue to Next Step**.

6. In the **SSO Mapping Attributes**section, click **Add new attribute**. Enter the session tags attributes that you plan to use.

   ### Choose from:

   * If you are using AWS IAM Identity Center, include the access control tags based on the following format: `https://aws.amazon.com/SAML/Attributes/AccessControl:{attribute}`

   * If you are using AWS IAM, enter the AWS Principal Tags and TransitiveTagKeys, based on the following examples:

   * `https://aws.amazon.com/SAML/Attributes/AccessControl:{attribute}`

   * `https://aws.amazon.com/SAML/Attributes/PrincipalTag:project`

   * `https://aws.amazon.com/SAML/Attributes/Role`

   * `https://aws.amazon.com/SAML/Attributes/RoleSessioName`

   * `https://aws.amazon.com/SAML/Attributes/TransitiveTagKeys`

     ![This screen capture shows the SSO Attribute Mapping section with examples of potential Principal Tags and TransitiveTagKeys for AWS IAM.](_images/onu1571948983354.png)

7. Click **Continue to Next Step** twice and then click **Finish** to create the AWS Session Tag SAML application.

---

---
title: Configuring single sign-on
description: To allow PingFederate to act as an identity provider for Amazon Web Services (AWS), enable single sign-on (SSO) in PingFederate and AWS, and create a connection.
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_configuring_single_sign_on
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_configuring_single_sign_on.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Configuring single sign-on

To allow PingFederate to act as an identity provider for Amazon Web Services (AWS), enable single sign-on (SSO) in PingFederate and AWS, and create a connection.

## About this task

|   |                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Single sign-on integration is an optional part of this integration. If you only want to use the Atlassian Connector for provisioning, skip these steps. |

## Steps

1. Complete the steps in [Exporting connection-specific SAML metadata](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_exportmetadatatasklet_exportconnectionstate.html).

2. Create an identity provider profile to represent PingFederate in Amazon Web Services (AWS).

   Complete the steps in [Creating and Managing an IAM SAML Identity Provider (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html) in the AWS documentation.

3. Create a federation role in Amazon Web Services (AWS) that uses PingFederate as an identity provider.

   Complete the steps in [Creating a Role for SAML 2.0 Federation (Console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_saml.html) in the AWS documentation.

4. Complete the steps in [Creating a single sign-on connection](pf_aws_connector_creating_a_single_sign_on_connection.html).

---

---
title: Create security credentials in Amazon Web Services
description: PingFederate needs credentials to manage users and groups in Amazon Web Services (AWS). You can create these credentials in the AWS management console. For more details, see Managing Access Keys for Your AWS Account Root User in the AWS documentation.
component: amazon
page_id: amazon:amazon_web_services_connector:pf_aws_connector_create_security_credentials_in_amazon_web_services
canonical_url: https://docs.pingidentity.com/integrations/amazon/amazon_web_services_connector/pf_aws_connector_create_security_credentials_in_amazon_web_services.html
revdate: July 3, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Create security credentials in Amazon Web Services

## About this task

PingFederate needs credentials to manage users and groups in Amazon Web Services (AWS). You can create these credentials in the AWS management console. For more details, see [Managing Access Keys for Your AWS Account Root User](https://docs.aws.amazon.com/general/latest/gr/managing-aws-access-keys.html) in the AWS documentation.

## Steps

1. Sign on to the [AWS Management Console](https://console.aws.amazon.com/) as the root user for the AWS account.

2. On the navigation menu, click your account name, and then click **My Security Credentials**.

3. If you receive a warning about accessing the security credentials for your AWS account, click **Continue to Security Credentials**.

4. Expand the **Access keys (access key ID and secret access key)** section.

5. Click **Create New Access Key**.

   |   |                                                                                                                                                                                                                |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You might need to delete an existing access key before you can create a new key. See [IAM Object Limits](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html) in the AWS documentation. |

6. Note the access key ID and the access key secret.

   |   |                                                                          |
   | - | ------------------------------------------------------------------------ |
   |   | This is your only opportunity to view or download the secret access key. |

---

---
title: Creating a connection
description: To allow PingFederate to act as an identity provider and manage users in AWS IAM Identity Center, create a service provider (SP) connection.
component: amazon
page_id: amazon:aws_iam_identity_center_provisioner:pf_aws_singlesignon_connector_creating_a_connection
canonical_url: https://docs.pingidentity.com/integrations/amazon/aws_iam_identity_center_provisioner/pf_aws_singlesignon_connector_creating_a_connection.html
revdate: July 3, 2024
section_ids:
  steps: Steps
---

# Creating a connection

To allow PingFederate to act as an identity provider and manage users in AWS IAM Identity Center, create a service provider (SP) connection.

## Steps

1. In the PingFederate administrator console, create a new SP connection:

   Choose from:

   * For PingFederate 10.1 or later: go to **Applications > Integration > SP Connections**. Click **Create Connection**.

   * For PingFederate 10.0 or earlier: go to **Identity Provider > SP Connections**. Click **Create Connection**.

2. Configure the basic connection details with the AWS IAM Identity Center quick connection template.

   1. On the **Connection Template** tab, select **Use a template for this connection**.

   2. From the **Connection Template** list, select **AWS SSO Cloud Connector**.

   3. On the **Metadata File** row, upload the sp-saml-metadata.xml file that you saved in [Registering PingFederate as an identity provider in AWS Single Sign-On](pf_aws_singlesignon_connector_registering_pf_as_an_identity_provider_in_aws_single_sign_on.html). Click **Next**.

   4. On the **Connection Type** tab select **Browser SSO Profiles** and **Outbound Provisioning**. Click **Next**.

   5. On the **Connection Options** tab, click **Next**.

   6. On the **General Info** tab, in the **Connection Name** field, enter a name of your choosing. Click **Next**.

3. On the **Browser SSO** tab, configure your assertion creation settings and customize the defaults set by the metadata file.

   For help, see [Configuring IdP Browser SSO](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_spbrowserssostate.html) in the PingFederate documentation.

4. On the **Credentials** tab, configure the connection credentials as shown in [Configuring credentials](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_credentialsstate.html) in the PingFederate documentation. Click **Next**.

5. On the **Outbound Provisioning** tab, configure provisioning with the following details.

   For help, see [Configuring outbound provisioning](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_spconnectionconfigtasklet_saasprovisioningstate.html) in the PingFederate documentation.

   1. On the **Target** tab, complete the **SCIM URL** and **Access Token** fields with the values that you noted in [Registering PingFederate as an identity provider in AWS Single Sign-On](pf_aws_singlesignon_connector_registering_pf_as_an_identity_provider_in_aws_single_sign_on.html).

   2. Under **Provisioning Options**, customize the provisioning connector behavior by referring to [Provisioning options reference](pf_aws_singlesignon_connector_provisioning_options_reference.html). Click **Next**.

   3. On the **Manage Channels > Attribute Mapping** tab, at the bottom of the attribute list, click **Refresh Fields** to get fields and specifications from your AWS IAM Identity Center site. Complete the attribute mappings by referring to [Supported attributes reference](pf_aws_singlesignon_connector_supported_attributes_reference.html).

      For help, see [Managing channels](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_saasmanagementtasklet_saasmanagementstate.html) in the PingFederate documentation.

6. On the **Activation and Summary** tab, above the **Summary** section, click the toggle to turn on the connection. Click **Save**.