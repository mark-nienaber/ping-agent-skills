---
title: About account linking
description: Account linking provides a means for a user to log on to disparate sites with just one authentication when the user has established accounts and credentials at each site.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_about_account_link
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_about_account_link.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  processing-steps: Processing steps
---

# About account linking

Account linking provides a means for a user to log on to disparate sites with just one authentication when the user has established accounts and credentials at each site.

All protocols support this method of interconnecting accounts across domains.

Account linking involves a persistent name identifier associated with accounts at each participating site. The assertion conveys the name identifier, which can be an opaque pseudonym. Once established locally, the service provider (SP) can use the account link to look up the user and provide access without re-authentication.

![Diagram illustrating the 4 steps involved in account linking.](_images/bkp1564003101403.jpg)Account linking

## Processing steps

1. David Smith logs on to Site A as *davidsmith*. He then decides to access his account on Site B through Site A.

2. Optionally, the federation server looks up additional attributes from the datastore.

3. The Site A federation server sends a persistent name identifier to Site B, along with any other attributes.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | When using a pseudonym and sending other attributes, be careful not to send attributes that could identify the subject. |

4. The federation server on Site B uses the information to associate the pseudonym with the existing account of *dsmith* and optionally might ask David to provide consent to the linking.

   Once the link has been established, Site B stores the information so that David only has to log on to Site A to access Site B.

---

---
title: About identity federation and SSO
description: Federated identity management, or identity federation, allows enterprises to exchange identity information securely across domains, providing browser-based single sign-on (SSO).
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_about_identity_fed_sso
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_about_identity_fed_sso.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  service-providers-and-identity-providers: Service providers and identity providers
  federation-hub: Federation hub
  related-links: Related links
---

# About identity federation and SSO

Federated identity management, or identity federation, allows enterprises to exchange identity information securely across domains, providing browser-based single sign-on (SSO).

Identity federation also integrates access to applications across distinct business units within a single organization. As organizations grow through acquisitions, or when business units maintain separate user repositories and authentication mechanisms across applications, a federated solution to browser-based SSO is desirable.

This cross-domain, identity-management solution provides numerous benefits, ranging from increased end user satisfaction and enhanced customer relations to reduced cost and greater security and accountability.

For complete information about identity federation and the standards that support it, see [Supported standards](pf_supported_standards.html).

## Service providers and identity providers

Identity federation standards identify two operational roles in an SSO transaction: the identity provider (IdP) and the service provider (SP).

An IdP might be an enterprise that manages accounts for a large number of users who need secure access to the web-based applications or services of customers, suppliers, and business partners. An SP might be a SaaS provider or a business-process outsourcing (BPO) vendor wanting to simplify client access to its services.

![Diagram illustrating secure single sign-on between the workforce identity provider and the cloud service provider.](_images/ydy1564003075854.png)Secure single sign-on

Identity federation allows both types of organizations to define a trust relationship whereby the SP provides access to users from the IdP. The IdP continues to manage its users, and the SP trusts the IdP to authenticate them.

A single instance of PingFederate provides complete support for both roles even when a single organization's business processes encompass both SP and IdP use cases.

## Federation hub

As a federation hub, PingFederate can bridge browser-based SSO between IdPs and SPs, reducing administrative overhead.

Identity federation refers to the negotiation and management of federation settings with partners. Supporting different federation protocols can hinder application development and SSO implementation.

Configuring PingFederate as a federation hub:

* Allows you to simplify application development and SSO implementation by extending federated access across partners supporting different federation standards

* Provides a centralized console to simplify SSO administration

Bridging IdPs and SPs through a federation hub allows you to multiplex a single connection for multiple partners.

![federation hub diagram](_images/ago1564003078226.png)

### Related links

* [Federation hub use cases](pf_fed_hub_use_case.html)

---

---
title: About OAuth
description: Configuring PingFederate as an OAuth authorization server (AS) allows a resource owner (RO), typically an end user, to grant authorization to an OAuth client requesting access to the resource server (RS).
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_about_oauth
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_about_oauth.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# About OAuth

Configuring PingFederate as an OAuth authorization server (AS) allows a resource owner (RO), typically an end user, to grant authorization to an OAuth client requesting access to the resource server (RS).

The OAuth AS issues tokens to clients on behalf of an RO for use in authenticating a subsequent API call to the RS, typically, but not exclusively, a REST API call.

|   |                                                                                                            |
| - | ---------------------------------------------------------------------------------------------------------- |
|   | If your PingFederate license does not include the OAuth AS capabilities, contact <sales@pingidentity.com>. |

You can configure the PingFederate OAuth AS independently or in conjunction with security token service (STS) or browser-based single sign-on (SSO) for either an identity provider (IdP) or a service provider (SP) deployment.

In an IdP deployment, an IdP adapter is used to authenticate and provide user information for the access token. In an SP deployment, the inbound SAML assertion is used to provide authentication information about the user associated with the access token through an OAuth attribute mapping in the IdP connection.

For an STS IdP, PingFederate provides an OAuth token processor that validates incoming OAuth Bearer access tokens.

---

---
title: Account linking
description: Under the standards, use account linking for browser-based single sign-on (SSO) in cases where each domain maintains separate accounts for the same user.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_acc_link
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_acc_link.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2023
section_ids:
  linking-permission-and-defederation: Linking permission and defederation
  sp-affiliations: SP affiliations
---

# Account linking

Under the standards, use account linking for browser-based single sign-on (SSO) in cases where each domain maintains separate accounts for the same user.

Account linking uses the SAML assertion to create a persistent association between these distinct user accounts. The account link, or name identifier, such as an email address or identity provider (IdP)-generated pseudonym, identifies individual users. When privacy is a concern, use pseudonyms because they prevent tracing back to a user's identity at the partner site.

During the user's first SSO request, the service provider (SP) prompts for local credentials, which enables the SP to link the name identifier contained within the assertion—either an open attribute or a pseudonym—with the user's local account. Subsequent SSO events will not prompt the user to authenticate with the SP because the SP federation server keeps a table associating remote users' name identifiers with local user accounts. The SP associates the link to the user's corresponding local account and provides access to the account without separate authentication.

|   |                                                                                                                                                                                                                                                                                                                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Use the built-in HSQLDB only for trial or training environments. For testing and production environments, always use a secured external storage solution for proper functioning in a clustered environment.Testing involving HSQLDB is not a valid test. In both testing and production, it might cause various problems due to its limitations and HSQLDB involved cases are not supported by Ping Identity. |

The name identifier optionally includes additional attributes. When using a pseudonym as the account link, take care to send only general attributes, such as a user's organizational role or department, that will not compromise privacy.

## Linking permission and defederation

The SAML specification also allows the SP application to build in user verification and approval of account linking and provides a means for the user to permanently cancel the linking, known as defederation. For more information, see [/sp/defederate.ping](../developers_reference_guide/pf_sp_services.html#spDefederatePing). A defederated user might later elect to re-associate with a local user account.

## SP affiliations

Under the SAML 2.0 specifications, an IdP configures PingFederate to enable a group of SPs, called an SP affiliation, to share the same persistent name identifier. For more information, see [SP affiliations](../administrators_reference_guide/pf_sp_affiliat.html). An SP affiliation facilitates the use case where a number of business partners have an existing relationship and where sharing a single name identifier among all parties reduces the federation integration effort.

---

---
title: Account mapping
description: Account mapping, also called attribute mapping, enables a service provider (SP) to use PingFederate to perform a user lookup and map a user's identity dynamically based on one or more attributes received in the assertion.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_acc_mapp
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_acc_mapp.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Account mapping

Account mapping, also called attribute mapping, enables a service provider (SP) to use PingFederate to perform a user lookup and map a user's identity dynamically based on one or more attributes received in the assertion.

Looking up the user always exposes the attributes. In other words, both the identity provider (IdP) and the SP know these attributes, such as an email address.

Account mapping achieves one-to-one mapping where individual user accounts exist on both sides of a federated connection or many-to-few mapping where IdP users without accounts at destination sites map to guest accounts or to a role-based general account.

For browser-based single sign-on (SSO), transient identifiers provide an additional level of privacy—virtual anonymity—by generating a different opaque ID each time the user initiates SSO. Transient IDs are often used in conjunction with federation role mapping to map the user to a guest account or to a role-based account based on the user's association with the IdP organization rather than personal attributes.

As with pseudonyms, additional attributes might be sent with the transient identifier. Again, take care to preserve privacy.

In B-to-B or B-to-E use cases where an administrator might create a user lookup on behalf of the user, the administrator might implement account mapping.

---

---
title: Adapter contracts
description: An adapter contract represents an agreement between the PingFederate server and an external application.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_adapt_contract
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_adapt_contract.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  extended-adapter-contract: Extended adapter contract
---

# Adapter contracts

An adapter contract represents an agreement between the PingFederate server and an external application.

In concert with the attribute contract between partners, adapter contracts specify the transfer of attributes. Adapter contracts consist of a list of case-sensitive attribute names.

On the identity provider (IdP) side of a federation, an IdP adapter supplies attributes to PingFederate for more information, see [Managing IdP adapters](../administrators_reference_guide/pf_managing_idp_adapters.html).

On the service provider (SP) side, adapters require adapter contract attributes to start a session with an application. Each security domain requires at least one adapter type. Then, you must configure an adapter instance for each target application. For more information, see [Managing SP adapters](../administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html).

Attributes from the attribute contract fulfill the adapter contracts on the SP side, possibly enhanced with other attributes from local data stores. For example, if the same security context controls several target applications and provides the same set of attributes to start a session for the user, you would deploy an adapter type and configure an adapter instance for each protected application. For more information, see [Managing target session mappings](../administrators_reference_guide/help_usersessioncreationtasklet_configadaptermappingstate.html).

## Extended adapter contract

When PingFederate deploys an adapter type, it creates adapter contracts. Developing these adapters "hard-wires" them to look up or set a specific set of attributes. Attribute requirements might change after deployment. To streamline adjustment of adapter contracts, PingFederate allows an administrator to add additional attributes to the adapter instance through the administrative console, called extended adapter contracts.

---

---
title: Additional features
description: PingFederate's lightweight, standalone architecture allows server integration and partnering with existing home-grown and commercial identity management (IdM) systems and applications providing standards-based single sign-on (SSO) and API security integration benefits.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_add_feat
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_add_feat.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  pingone: PingOne
  integration-kits: Integration kits
  token-translators: Token translators
  saas-connectors: SaaS connectors
  cloud-identity-connectors: Cloud identity connectors
---

# Additional features

PingFederate's lightweight, standalone architecture allows server integration and partnering with existing home-grown and commercial identity management (IdM) systems and applications providing standards-based single sign-on (SSO) and API security integration benefits.

## PingOne

The PingOne Cloud Platform offers one platform for unifying all your digital identities and allowing your users and devices to securely access cloud, mobile, SaaS and on-premises applications and APIs. With PingFederate, you can leverage these services to accelerate the digital transformation of your environment for better security and compliance.

## Integration kits

Use PingFederate's software development kit (SDK) for creating custom integrations with existing authentication services and target applications as well as quick connections to various partners. You can download the PingFederate integration kits from the Ping Identity [Downloads](https://www.pingidentity.com/en/resources/downloads/pingfederate.html) website.

![Diagram depicting multiple security-domain, multi-protocol federation between the IdP, , and SP.](_images/rtc1564003082462.png)Multiple security-domain, multi-protocol federation

## Token translators

Ping Identity offers special token processors for an IdP and token generators for a SP that enable the WS-Trust security token service (STS) to validate and issue a variety of token types. These plug-ins supplement built-in SAML token processing and generation and handle the local identity tokens required in many security contexts. For more information, see [Token processors and generators](pf_token_proc_and_gen.html).

## SaaS connectors

SaaS connectors offer a streamlined approach for browser-based SSO to selected SaaS providers, including automatic user provisioning and deprovisioning. The connector packages include quick-connection templates, which automatically configure endpoints and other connection information for each provider. For more information, see [Outbound provisioning for IdPs](pf_outboun_provis_for_idp.html).

## Cloud identity connectors

Offer your users the option to login, register, and access your cloud-based applications with their social identity from sites like Apple, Facebook, Google, LinkedIn, Microsoft, and Twitter.

---

---
title: Additional integrations
description: In addition to the bundle integrations and authenticators, Ping Identity provides identity and access management (IAM) integrations with a wide range of cloud, mobile, software as a service (SaaS), APIs, and on-premises applications.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_additional_integr
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_additional_integr.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 21, 2025
---

# Additional integrations

In addition to the bundle integrations and authenticators, Ping Identity provides identity and access management (IAM) integrations with a wide range of cloud, mobile, software as a service (SaaS), APIs, and on-premises applications.

To discover integrations, including downloads and documentation, visit the [Ping Identity Marketplace](https://marketplace.pingone.com).

The following describes our most common types of integrations:

* Single sign-on (SSO)

  Integration kits allow PingFederate to coordinate SSO for a variety of platforms and applications, such as Atlassian and Citrix.

For select platforms, [configuration guides](https://docs.pingidentity.com/configuration_guides/config_configuration_guides.html) are provided to help you configure SSO without any additional downloads.

* User and group provisioning

  Connectors allow PingFederate to provision and synchronize users and groups from an attached datastore to a directory in a cloud service, such as PingOne, Salesforce, or Zoom.

  Connectors also let you set up optional SSO between PingFederate and the cloud service.

  These typically include a connection template for the PingFederate provisioning engine.

* Multi-factor authentication (MFA)

  MFA integrations allow PingFederate to include third-party MFA providers, such as PingOne MFA and RSA SecurID, as part of the sign-on flow.

* Mobile device management

  Mobile device management integrations allow PingFederate to adjust the sign-on flow based on device information from services such as MobileIron and AirWatch.

  These typically include an IdP adapter.

* Risk-based intelligent authentication

  Risk intelligence integration kits allows PingFederate to retrieve a security risk assessment from third parties, such as PingOne Protect and ThreatMetrix, when a user signs on. You can use this information to dynamically adjust authentication requirements based on the risk level for each sign-on event.

  These typically include an IdP adapter. For more information, see [PingOne Protect Integration Kit](https://docs.pingidentity.com//integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik.html).

* Custom application integration

  The [Agentless Integration Kit](https://support.pingidentity.com/s/marketplace-integration/a7i1W0000004ICWQA2/agentless-integration-kit) can integrate any application with PingFederate for SSO. This uses API calls with no need for agent software. We provide sample code for a variety of programming languages.

  Specific integrations are available for the language your application uses, such as Java, .NET, and PHP. These include an IdP and SP adapter, an agent file, and sample code.

* Web server agents

  PingFederate to extend single sign-on abilities to applications running on web servers, such as Apache and IIS.

* Social sign-on

  Cloud identity connectors (CIC) allow PingFederate to coordinate SSO by using third-party services as identity providers (IdP). This allows a user to access a service provider (SP), such your web application, by signing into a popular service, such as LinkedIn, Google, or Facebook.

  These typically include a PingFederate IdP adapter.

* Checking user credentials

  Password credential validator (PCV) integrations let PingFederate validate user credentials against a directory service, such as PingOne and Azure, when a user signs on.

  These include a PCV add-on for PingFederate.

* Converting identity tokens

  Token translators allow PingFederate to convert or validate IdP tokens in a variety of formats, such as the WS-Trust security token service (STS).

  These typically include token processor and token generator files.

* Custom integrations

  PingFederate also includes an SDK that software you can use to write custom interfaces for specific systems. For more information, see the [SDK Developer's Guide](../sdk_developers_guide/pf_sdk_developers_guide.html).

* Specific use cases

  Find comprehensive guides for specific use cases in the [use case documentation](https://docs.pingidentity.com/solution-guides/htg_overview.html).

---

---
title: Assertion grant profile for OAuth 2.0 authorization grants
description: The assertion grant profile process takes place between the user or requesting application. client application, PingFederate identity provider (IdP), PingFederate authorization server (AS) and resource server (RS).
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_assertion_grant_profile_oauth_20_authorization_grants
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_assertion_grant_profile_oauth_20_authorization_grants.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 8, 2024
section_ids:
  processing-steps: Processing steps
  related-links: Related links
---

# Assertion grant profile for OAuth 2.0 authorization grants

The assertion grant profile process takes place between the user or requesting application. client application, PingFederate identity provider (IdP), PingFederate authorization server (AS) and resource server (RS).

In this scenario, a client obtains an assertion, either a SAML 2.0 bearer assertion or a JSON Web Token (JWT) bearer token, and makes an HTTP request to the PingFederate OAuth AS to exchange the assertion for an access token. The OAuth AS validates the assertion and returns an access token. The client uses the token in an API call to the RS to obtain data.

Flowchart depicting the assertion grant profile process between the User or Requesting Application, Client application, IdP, AS, and RS.Assertion grant profile

## Processing steps

1. A user-initiated or client-initiated event, such as a mobile application or a scheduled task, requests access to software as a service (SaaS) protected resources from an OAuth client application.

2. The client application obtains an assertion from an IdP.

   |   |                                                                                                                                                                                                                                                                                         |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | When using SAML assertions as authorization grants, client applications must obtain assertions that meet the requirements defined in [RFC 7522](https://datatracker.ietf.org/doc/html/rfc7522). Do not use SAML assertions acquired through browser single sign-on (SSO) profiles here. |

3. The client application makes an HTTP request to the PingFederate OAuth AS to exchange the assertion for an access token. The OAuth AS validates the assertion and returns the access token.

4. The client application adds the access token to its API call to the RS. The RS returns the requested data to the client application.

## Related links

* [JSON Web Token (JWT) Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7523)

* [Security Assertion Markup Language (SAML) 2.0 Profile for OAuth 2.0 Client Authentication and Authorization Grants](https://datatracker.ietf.org/doc/html/rfc7522)

* [Configuring an OAuth assertion grant IdP connection](../administrators_reference_guide/help_idpconnectionconfigtasklet_oauthsamlgrantattributemappingstate.html)

---

---
title: Attribute contracts
description: An attribute contract represents an agreement between partners about user attributes sent in a SAML assertion, a JSON web token (JWT), or an OpenID Connect ID token.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_attr_contract
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_attr_contract.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  name-formats: Name formats
  sts-namespaces: STS namespaces
---

# Attribute contracts

An attribute contract represents an agreement between partners about user attributes sent in a SAML assertion, a JSON web token (JWT), or an OpenID Connect ID token.

The contract is a list of case-sensitive attribute names. Partners must configure attribute contracts to match.

|   |                                                                                                                                                                                             |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When privacy is required for sensitive attributes, you can configure PingFederate to mask their values in log files. For more information, see [Attribute masking](pf_attrib_masking.html). |

For an identity provider (IdP) or an OpenID Provider (OP), the attribute contract defines which attributes PingFederate sends in an assertion, a JWT, or an ID token. While all users authenticate to the partner through this fixed contract, the values used to fulfill the contract might differ from one user to the next. Relying on a combination of different data sources might also fulfill the attribute contract:

* The IdP adapter or security token service (STS) token processor

* An IdP attribute source, which identifies the location of individual attributes in a datastore

* Static text values for some attributes, or text values combined with variables

* Expressions (see [Attribute mapping expressions](../administrators_reference_guide/pf_attribute_mapping_expressions.html))

For a service provider (SP) or an OpenID Connect Relying Party, the attribute contract defines the attributes PingFederate expects in a SAML assertion, an ID token, or from the UserInfo endpoint at the OP. To pass these attributes to the SP adapter or, for web services, to the SP token generator, configure PingFederate accordingly. For more information, see [Managing SP adapters](../administrators_reference_guide/help_adaptermanagementtasklet_spadaptermanagementstate.html) or [Managing token generators](../administrators_reference_guide/help_tokengeneratortasklet_tokenpluginmgmtstate.html). In addition, you can configure PingFederate to use attributes to look up additional attributes in local data stores, which often help start a user session or create a local security token for web services. For more information, see [Adapter contracts](pf_adapt_contract.html) or [STS token contracts](pf_sts_token_contract.html).

The attribute contract always contains the user identifier `SAML_SUBJECT` in a SAML assertion and `sub` in a JWT or an ID token unless you are using account linking for browser-based single sign-on (SSO). This attribute is automatically included when creating a new contract.

|   |                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You create attribute contracts on a per-connection basis. For example, if an SP has deployed two session-creation adapters for two separate applications, the IdP connection partner creates a single attribute contract. This single contract supplies all the attributes required by both SP adapters. |

## Name formats

By agreement with an SP partner, an IdP might specify a format, such as email, associated with the `SAML_SUBJECT`. The SP might further require this information to facilitate handling of the format.

The partner agreement might also include a requirement for the IdP to provide format specifications associated with other attributes.

PingFederate provides a means for an IdP administrator to select from among standard subject, attribute formats, or both, depending on the relevant SAML specifications. An administrator also defines a customized selection of additional attribute formats. For more information, see [Setting up an attribute contract](../administrators_reference_guide/help_assertioncreationtasklet_createattributecontractstate.html).

|   |                                                                                                                                                                                                                                   |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The designation of formats does not apply to SP administrators. The information about formats remains available in the incoming assertion to an SP application that needs the information for particular processing requirements. |

For the WS-Trust IdP configuration, attribute-name formats remain unspecified. If needed however, an administrator might user a special variable in the attribute contract to set the subject-name format. For more information, see [Defining an attribute contract for IdP STS](../administrators_reference_guide/help_wstrustsptokencreationtasklet_wstrustattributecontractstate.html). Browser-based SSO attribute contracts also use the same variable, but the feature has deprecated.

## STS namespaces

By agreement with an SP partner for a WS-Trust STS connection, an IdP specifies an XML namespace to associate with an attribute, for example, to use claims-based authorization with WIF clients. For more information, see [WSC and WSP support](pf_wsc_and_wsp_supp.html). The only attributes that allow specified namespaces belong to a WS-Trust IdP configuration using`SAML 1.1` or `SAML 1.1 for Office 365` as the default token type. For more information, see [Defining an attribute contract for IdP STS](../administrators_reference_guide/help_wstrustsptokencreationtasklet_wstrustattributecontractstate.html).

---

---
title: Attribute masking
description: At runtime PingFederate logs user attributes. To preserve user privacy, you can mask the values of logged attributes.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_attrib_masking
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_attrib_masking.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2023
---

# Attribute masking

At runtime PingFederate logs user attributes. To preserve user privacy, you can mask the values of logged attributes.

For more information about log files, see [PingFederate log files](../administrators_reference_guide/pf_log_files.html). PingFederate provides this masking capability at all points where the server logs attributes. These points include:

* Datastore lookup at either the identity provider (IdP) or service provider (SP) site. For more information, see [Managing datastores](../administrators_reference_guide/pf_managing_datastores.html).

* Retrieval of attributes from an IdP adapter or token processor. For more information, see [Setting pseudonym and masking options](../administrators_reference_guide/pf_setting_pseudonym_masking_options.html) and [Setting attribute masking](../administrators_reference_guide/help_tokenprocessorinstancetasklet_attributevaluemaskstate.html).

* SP-server processing of incoming attributes based on the single sign-on (SSO) attribute contract. For more information, see [Defining an attribute contract](../administrators_reference_guide/help_usersessioncreationtasklet_createattributecontractstate.html).

  |   |                                                                                                                                                                                                                                              |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The SAML Subject ID is not masked; the SAML specifications provide for either pseudonymous account linking or transient identification to support privacy for the Subject ID. For more information, see [Account linking](pf_acc_link.html). |

* SP-server processing of incoming attributes in response to an Attribute Request under X.509 Attribute Sharing Profile (XASP). For more information, see [Configuring security policy for Attribute Query](../administrators_reference_guide/help_idpxasptasklet_attrauthsecuritypolicystate.html).

  For information about XASP, see [Attribute Query and XASP](pf_attrib_query_xasp.html).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                 |
  | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Many adapter implementations, along with other product extensions, can independently write unmasked attribute values to the PingFederate server log. PingFederate does not control these implementations. If using such a component raises a concern about sensitive attribute values, you can adjust the component's logging threshold in `log4j2.xml` to prevent the recording of attributes. |

---

---
title: Attribute Query and XASP
description: The SAML 2.0 Attribute Query profile allows a service provider (SP) to request user attributes from an identity provider (IdP) in a secure transaction separate from single sign-on (SSO).The X.509 Attribute Sharing Profile (XASP) defines a specialized extension of the general Attribute Query profile.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_attrib_query_xasp
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_attrib_query_xasp.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  related-links: Related links
---

# Attribute Query and XASP

The SAML 2.0 Attribute Query profile allows a service provider (SP) to request user attributes from an identity provider (IdP) in a secure transaction separate from single sign-on (SSO).The X.509 Attribute Sharing Profile (XASP) defines a specialized extension of the general Attribute Query profile.

The IdP, acting as an attribute authority, accepts attribute queries, performs a datastore lookup into a user repository such as an LDAP directory, provides values to the requested attributes, and generates an attribute response back to the originating SP requester. The SP then returns the attributes to the requesting application.

|   |                                                                                                                                                           |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When privacy is required for sensitive attributes, you can configure PingFederate to obfuscate, or mask, their values in the server and transaction logs. |

Web SSO is distinct from the Attribute Query use case. You can configure PingFederate servers to implement either of these profiles without regard to the other.

The XASP specification enables organizations with an investment in Public Key Infrastructure (PKI) to issue and receive Attribute Queries based on user-certificate authentication.

Under XASP a user authenticates directly with an SP application by providing their X.509 certificate. After the user is authenticated, the SP application requests additional user attributes by contacting the SP PingFederate server. A portion of the user's X.509 certificate is included in the request and can be used to determine the correct IdP to use as the source of the requested attributes. Finally, the SP generates an Attribute Query and transmits it to the IdP over the SOAP back channel.

Because the user arrives at the SP server already authenticated, no PingFederate adapter is used in this case.

## Related links

* [Configuring the Attribute Query profile in an SP connection](../administrators_reference_guide/help_spconnectionconfigtasklet_attributerequesterstate.html)

* [Manage the Attribute Query profile in an IdP connection](../administrators_reference_guide/help_idpconnectionconfigtasklet_attributeauthoritystate.html)

---

---
title: Bridging an IdP to an SP
description: PingFederate bridges single sign-on (SSO) and single log-out (SLO) transactions between an identity provider (IdP) and a service provider (SP).
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_bridg_idp_to_sp
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_bridg_idp_to_sp.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Bridging an IdP to an SP

PingFederate bridges single sign-on (SSO) and single log-out (SLO) transactions between an identity provider (IdP) and a service provider (SP).

## About this task

If you have a legacy IdP system only capable of sending SAML 1.1 assertions through POST and an SP that requires SAML 2.0 assertions through the artifact binding, configuring the federation hub allows PingFederate to consume inbound SAML 1.1 assertions by POST, translate them to SAML 2.0 assertions, and send them through the artifact binding the SP.

![Diagram depicting the process of bridging an IdP to an SP.](_images/zkm1564003195727.png)

## Steps

1. Create a contract to bridge the attributes between the IdP and the SP. For more information, see [Federation hub and authentication policy contracts](pf_fed_hub_auth_polic_contract.html).

2. Create an IdP connection between the IdP and PingFederate, the federation hub as the SP, and add the applicable authentication policy contracts to the IdP connection on the **Target Session Mapping** tab.

3. Create an SP connection between PingFederate, the federation hub as the IdP, and the SP and add to the SP connection the corresponding authentication policy contract on the **Authentication Source Mapping** window.

4. Work with the IdP to connect to PingFederate, the federation hub, as the SP.

5. Work with the SP to connect to PingFederate, the federation hub, as the IdP.

---

---
title: Bridging an IdP to multiple SPs
description: PingFederate bridges single sign-on (SSO) and single log-out (SLO) transactions between an identity provider (IdP) and multiple service providers (SPs).
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_bridg_idp_to_multipl_sp
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_bridg_idp_to_multipl_sp.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Bridging an IdP to multiple SPs

PingFederate bridges single sign-on (SSO) and single log-out (SLO) transactions between an identity provider (IdP) and multiple service providers (SPs).

## About this task

For example, your company wants to route federation requests from a recently acquired subsidiary through its federation infrastructure. PingFederate multiplexes one IdP connection to multiple SP connections to the desired SPs. The federation hub consumes assertions from the subsidiary and creates new assertions to the respective SPs.

![diagram depicting the Federation hub with an IdP bridged to multiple SPs.](_images/aum1564003196667.png)

## Steps

1. For each SP, create a contract to the IdP. For more information, see [Federation hub and authentication policy contracts](pf_fed_hub_auth_polic_contract.html). Because each SP likely requires a unique set of attributes, you will need to create multiple contracts.

2. Create an IdP connection between the IdP and PingFederate, the federation hub as the SP.

3. Add the applicable authentication policy contract(s) to the IdP connection on the **Target Session Mapping** window.

4. For each SP, create an SP connection between PingFederate, the federation hub as the IdP, and the SP.

5. Add the corresponding authentication policy contract to the SP connection on the **Authentication Source Mapping** window.

6. For each SP supporting the SAML IdP-initiated SSO profile, map the expected target resources to the corresponding SP connections on the **Applications > Integration > Target URL Mapping** window.

7. Work with the IdP to connect to PingFederate , the federation hub as the SP.

8. Work with each SP to connect to PingFederate, the federation hub as the IdP.

---

---
title: Bridging multiple IdPs to an SP
description: How PingFederate can act as a bridge to allow a single SP to accept SAML assertions from multiple IdPs.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_bridg_multi_idp_to_sp
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_bridg_multi_idp_to_sp.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 26, 2025
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Bridging multiple IdPs to an SP

With PingFederate, you can bridge single sign-on (SSO) and single log-out (SLO) transactions between multiple identity providers (IdPs) and a service provider (SP).

## About this task

For example, you're tasked with providing federated access to resources on a target SP for various business partners. With PingFederate, you can multiplex one SP connection, to your target SP, to multiple IdP connections for all your business partners. The federation hub can also translate SAML assertions from the business partners to WS-Federation security tokens and send them to your target SP.

![Diagram depicting the Federation Hub with multiple IdPs bridging to a single SP.](_images/zof1564003197650.png)

## Steps

1. Create a contract to bridge the attributes between the IdPs and the SP. For more information, see [Federation hub and authentication policy contracts](pf_fed_hub_auth_polic_contract.html).

   You likely need only one contract unless the SP requires a different set of attributes from each IdP.

2. For each IdP, create an IdP connection between the IdP and PingFederate, the federation hub as the SP.

3. On the **Target Session Mapping** window, add the applicable authentication policy contracts to the IdP connection.

4. On the **Selectors** window, configure an authentication selector. For example, see an instance of the [Identifier First Adapter](../administrators_reference_guide/pf_identifier_first_adapter.html) to map each IdP to the corresponding IdP connection in an authentication policy.

5. Create an SP connection between PingFederate, the federation hub as the IdP, and the SP.

6. Add the corresponding authentication policy contract to the SP connection on the **Authentication Source Mapping** window.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingFederate includes the Entity ID of the original IdP (`Authenticating Authority`) in SAML 2.0 assertions so that the SP can determine the original issuer of the assertions. This is especially important when bridging multiple IdPs to one SP—the SP should take the information about the original issuer into consideration before granting access to protected resources.For SAML 1.x assertions and WS-Federation security tokens, you can add an attribute on the **Attribute Contract** window and then map **Context: Authenticating Authority** as the attribute value on the **Attribute Contract Fulfillment** window\.For information about `Authenticating Authority`, see section in the SAML 2.0 specification. |

   |   |                                                                                                                                                                                                                                        |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the SP does not take action based on `Authenticating Authority`, depending on the attributes from the IdPs, you can define validation rules on the **Issuance Criteria** window to protect against user impersonation between IdPs. |

7. Work with each IdP to connect to PingFederate, the federation hub as the SP.

8. Work with the SP to connect to PingFederate, the federation hub as the IdP.

---

---
title: Bridging multiple IdPs to multiple SPs
description: PingFederate can bridge single sign-on (SSO) and single log-out (SLO) transactions between multiple identity providers (IdPs) and service providers (SPs).
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_bridg_multi_idp_to_multi_sp
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_bridg_multi_idp_to_multi_sp.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  about-this-task: About this task
  steps: Steps
---

# Bridging multiple IdPs to multiple SPs

PingFederate can bridge single sign-on (SSO) and single log-out (SLO) transactions between multiple identity providers (IdPs) and service providers (SPs).

## About this task

This PingFederate federation hub use case is a combination of [Bridging an IdP to multiple SPs](pf_bridg_idp_to_multipl_sp.html) and [Bridging multiple IdPs to an SP](pf_bridg_multi_idp_to_sp.html).

![Diagram depicting the Federation Hub and how it bridges multiples IdPs to multiple SPs.](_images/ago1564003078226.png)

## Steps

1. Create multiple contracts to bridge the attributes between the IdPs and the SPs. For more information, see [Federation hub and authentication policy contracts](pf_fed_hub_auth_polic_contract.html).

2. For each identity provider, create an IdP connection between the IdP and PingFederate, the federation hub as the SP.

3. Add the applicable authentication policy contracts to the IdP connection in the **Target Session Mapping** window.

4. In the **Selectors** window, configure an authentication selector to map each IdP to the corresponding IdP connection in an authentication policy. For example, see an instance of the [Identifier First Adapter](../administrators_reference_guide/pf_identifier_first_adapter.html).

5. For each service provider, create an SP connection between PingFederate, the federation hub as the IdP, and the SP.

6. Add the corresponding authentication policy contract to the SP connection in the **Authentication Source Mapping** window.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | PingFederate includes the Entity ID of the original IdP, `Authenticating Authority`, in SAML 2.0 assertions so that the SP can determine the original issuer of the assertions. This is especially important when bridging multiple IdPs to one SP—the SP should take the information about the original issuer into consideration before granting access to protected resources.In the **Attribute Contract** window, add an attribute for SAML 1.x assertions and WS-Federation security tokens. Then, in the **Attribute Contract Fulfillment**, map **Context: Authenticating Authority** as the attribute value.For information about `Authenticating Authority`, see section in the SAML 2.0 specification. |

   |   |                                                                                                                                                                                              |
   | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If the SP does not take action based on `Authenticating Authority`, in the **Issuance Criteria** window, you can define validation rules to protect against user impersonation between IdPs. |

7. For each SP supporting the SAML IdP-initiated SSO profile, map the expected target resources to the corresponding SP connections in the **Applications > Integration > Target URL Mapping** window.

8. Work with each IdP to connect to the federation hub as the SP.

9. Work with each SP to connect to the federation hub as the IdP.

---

---
title: Browser-based SSO
description: Browser-based single sign-on (SSO) includes SAML 1.x profiles, SAML 2.0 profiles, WS-Federation, and OpenID Connect and provides standards-based SSO, single logout (SLO), attribute query and X.509 attribute sharing profile (XASP), and the WS-Federation Passive Requestor Profile for service provider (SP)-initiated SSO.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_browser_sso
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_browser_sso.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
---

# Browser-based SSO

Browser-based single sign-on (SSO) includes [SAML 1.x profiles](pf_saml_1x_profiles.html), [SAML 2.0 profiles](pf_saml20_profile.html), [WS-Federation](pf_ws_fed.html), and [OpenID Connect](pf_openid_connect.html) and provides standards-based SSO, single logout (SLO), attribute query and X.509 attribute sharing profile (XASP), and the WS-Federation Passive Requestor Profile for service provider (SP)-initiated SSO.

---

---
title: Bundled adapters and authenticators
description: PingFederate comes bundled with the following adapters and authenticators to enable common deployment scenarios.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_bundled_adapt_auth
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_bundled_adapt_auth.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: December 12, 2023
section_ids:
  bundled-adapters: Bundled adapters
  bundled-authentication-selectors: Bundled authentication selectors
  software-development-kit-sdk: Software development kit (SDK)
---

# Bundled adapters and authenticators

PingFederate comes bundled with the following adapters and authenticators to enable common deployment scenarios.

## Bundled adapters

* Composite Adapter

  Allows multiple configured identity provider (IdP) adapters to execute in sequence. Depending on the authentication context, use this capability, called adapter chaining, for either single-adapter usage or to support multi-factor authentication through a series of adapters. Learn more in [Composite Adapter](../administrators_reference_guide/pf_composite_adapt.html).

* HTML Form Adapter

  Used in conjunction with Password Credential Validators. These adapters provide integration with user-datastores in directory servers or locally. Learn more in [HTML Form Adapter](../administrators_reference_guide/pf_html_form_adapt.html).

* HTTP Basic Adapter

  Used in conjunction with Password Credential Validators. These adapters provide integration with user-data stores in directory servers or locally. Learn more in [HTTP Basic Adapter](../administrators_reference_guide/pf_http_basic_adapt.html).

* Identifier First Adapter

  When a variety of user types authenticate at PingFederate, it is often better to ask the user for their identifier first, determine their user population, and prompt the user with the desired authentication requirements and experience. The Identifier First Adapter is designed to handle this use case. Learn more in [Identifier First Adapter](../administrators_reference_guide/pf_identifier_first_adapter.html).

* Kerberos Adapter

  Provides a seamless desktop SSO experience for Windows environments and supports authentication mechanism assurance from the Active Directory domain service. For new configurations and as a simpler alternative to the separately-available IWA Integration Kit, use this adapter. Learn more in [Kerberos Adapter](../administrators_reference_guide/pf_kerberos_adapt.html).

* OpenToken Adapter

  Provides a generic interface for integrating with various applications, including Java- and .NET-based applications. Learn more in [OpenToken Adapter](../administrators_reference_guide/pf_opentoken_adapt.html).

* Passthrough IdP Adapter

  The Passthrough IdP Adapter allows a user key to be associated with a user's authentication sessions. By placing the Passthrough IdP Adapter downstream from an IdP connection in a policy tree, you can take advantage of additional capabilities associated with defining a user key. Learn more in [Configuring a Passthrough IdP Adapter](../administrators_reference_guide/pf_passthrough_adapt.html).

* PingID Adapter

  PingID is a cloud-based authentication service that binds user identities to their devices, making it an effective multi-factor authentication solution. Learn more in the [PingID documentation](https://docs.pingidentity.com//pingid/pid_landing_page.html).

* PingOne DaVinci Adapter

  Allows PingFederate to use PingOne as an IdP as part of your PingFederate authentication policy. You can find detailed information in the [PingOne DaVinci Integration Kit](https://docs.pingidentity.com//integrations/pingone/pingone_davinci_integration_kit/pf_p1_davinci_ik.html).

* PingOne MFA Adapter

  Allows PingFederate to use the PingOne MFA service for multi-factor authentication (MFA). You can find detailed information in the [PingOne MFA Integration Kit](https://docs.pingidentity.com//integrations/pingone/pingone_mfa_integration_kit/pf_p1_mfa_ik.html).

* PingOne Protect Adapter

  When a user signs on through PingFederate, the adapter sends the transaction information to the PingOne Protect service and retrieves a risk evaluation and other information about the user's current and previous transactions. You can find detailed information in the [PingOne Protect Integration Kit](https://docs.pingidentity.com//integrations/pingone/pingone_protect_integration_kit/pf_p1_protect_ik.html).

* PingOne Verify Adapter

  Allows PingFederate to use the PingOne Verify service to trigger an identity verification challenge as part of the PingFederate authentication policy or registration flow. For example, you can use this adapter for personal identity verification based on a government issued photo ID. You can find detailed information in the [PingOne Verify Integration Kit](https://docs.pingidentity.com//integrations/pingone/pingone_verify_integration_kit/pf_p1_verify_ik.html).

## Bundled authentication selectors

PingFederate provides plugin authentication selectors, which enable dynamic selection of authentication sources based on administrator-specified criteria. Along with the Composite Adapter and token authorization, the selectors enable dynamic integration with an organization's authentication or authorization policies, also known as adaptive federation.

|   |                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | To select subsequent selectors or authentication sources for handling complex hierarchical access-policy decisions, use the results of authentication-selection criteria evaluation. Learn more in [Authentication policies](../administrators_reference_guide/pf_authentication_policies.html). |

* CIDR Authentication Selector

  Provides a means of choosing authentication sources or other authentication sources at runtime based on whether an end-user's IP address falls within specified ranges using Classless Inter-Domain Routing notation. This selector allows administrators to determine, for example, whether an SSO request originates inside or outside the corporate firewall and use different authentication integration accordingly. Learn more in [Configuring the CIDR Authentication Selector](../administrators_reference_guide/pf_config_cidr_auth_selector.html).

* Cluster Node Authentication Selector

  Provides a means of picking authentication sources or other authentication sources at runtime based on the PingFederate cluster node that is servicing the request. For example, you can configure this selector to choose whether PingFederate attempts Integrated Windows Authentication based on the PingFederate cluster node with which a Key Distribution Center is associated. Learn more in [Configuring the Cluster Node Authentication Selector](../administrators_reference_guide/pf_config_cluster_node_auth_selector.html).

* Connection Set Authentication Selector

  Provides a means of selecting authentication sources or other authentication sources at runtime based on a match found between the target SP connection used in an SSO request and SP connections configured within PingFederate. For example, administrators with different requirements for SP connections can override connection adapter selection on an individual connection basis. Learn more in [Configuring the Connection Set Authentication Selector](../administrators_reference_guide/pf_config_connection_set_auth_selector.html).

* Extended Property Authentication Selector

  Enables PingFederate to choose configured authentication sources or other selectors based on a match found between a selector result value and an extended property value from the invoking browser-based SSO connections or OAuth client. Learn more in [Configuring the Extended Property Authentication Selector](../administrators_reference_guide/pf_config_extended_property_auth_selector.html).

* HTTP Header Authentication Selector

  Provides a means of choosing authentication sources or other authentication sources at runtime based on a match found using wildcard expressions in an HTTP header. This selector allows administrators to determine, for example, authentication behavior based on the type of browser. Learn more in [Configuring the HTTP Header Authentication Selector](../administrators_reference_guide/pf_config_http_header_auth_selector.html).

* HTTP Request Parameter Authentication Selector

  Provides a means of selecting authentication sources or other authentication sources at runtime based on query parameter values in the HTTP request. Learn more in [Configuring the HTTP Request Parameter Authentication Selector](../administrators_reference_guide/pf_configuring_http_request_parameter_authentication_selector.html).

* OAuth Client Set Authentication Selector

  Enables PingFederate to choose configured authentication sources or other selectors based on a match found between the client information in an OAuth request and the OAuth clients configured in the PingFederate OAuth authorization server (AS). This selector allows you to override client authentication selection on an individual client basis in one or more authentication policies. Learn more in [Configuring the OAuth Client Set Authentication Selector](../administrators_reference_guide/pf_config_oauth_client_set_auth_selector.html).

* OAuth Scope Authentication Selector

  Provides a means of selecting authentication sources or other authentication sources at runtime based on a match found between the scopes of an OAuth authorization request and scopes configured in the PingFederate OAuth authorization server (AS). For example, if a client requires write access to a resource, administrators can configure the selector to choose an adapter that offers a stronger form of authentication such as the X.509 client certificate rather than username and password. Learn more in [Configuring the OAuth Scope Authentication Selector](../administrators_reference_guide/pf_config_oauth_scope_auth_selector.html).

* Requested AuthN Context Authentication Selector

  Provides a means of picking authentication sources or other authentication sources at runtime based on the authentication context requested by an SP, for SP-initiated SSO. Configured authentication sources are mapped either to SAML-specified contexts or any ad-hoc context agreed upon between the IdP and SP partners. Learn more in [Configuring the Requested AuthN Context Authentication Selector](../administrators_reference_guide/pf_config_request_authn_context_auth_selector.html).

* Session Authentication Selector

  Enables PingFederate to choose a policy path at runtime based on whether the user already has a PingFederate authentication session for a particular source. Learn more in [Configuring the Session Authentication Selector](../administrators_reference_guide/pf_config_sess_auth_selector.html).

  |   |                                                                                                                                                                                                            |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | Authentication selectors rely on HTTP requests, HTTP headers, POST data, or a combination of these authentication sources. Ensure that standard security measures are in place when using these selectors. |

## Software development kit (SDK)

The PingFederate SDK provides a flexible means of creating custom adapters to integrate federated identity management into your system environment. Learn more in the PingFederate [SDK Developer's Guide](../sdk_developers_guide/pf_sdk_developers_guide.html).

---

---
title: Certificate validation
description: PingFederate always checks certificates to see if they've expired when they're initially imported. It also checks certificates at runtime when they're used to verify incoming signed assertions.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_cert_validat
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_cert_validat.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  crl-revocation-checking: CRL revocation checking
  ocsp-revocation-checking: OCSP revocation checking
---

# Certificate validation

PingFederate always checks certificates to see if they've expired when they're initially imported. It also checks certificates at runtime when they're used to verify incoming signed assertions.

PingFederate also checks to see whether a certificate has been revoked, using either certificate revocation lists (CRLs) or the online certificate status protocol (OCSP). Depending on the content of the certificate in question and your requirements, the server will perform either of these checks during single sign-on (SSO) or single log-out (SLO) processing for the following cases:

* Signature verification

* Validation of a client certificate used for authentication to PingFederate when the server is handling direct client requests

* Validation of the server SSL certificate when PingFederate acts as the client making an HTTPS request to a separate server

If the system encounters an expired or revoked certificate, the associated SSO or SLO transaction fails at runtime and writes an error to the transaction log. In the administrative console, the Status column of the respective Certificate Management list identifies the expired or revoked certificate.

In PingFederate, by default, OCSP revocation checking is enabled and CRL revocation checking is disabled. However, you can configure PingFederate to use only CRL checking or as a backup to OCSP checking.

For more information, see [Configuring certificate revocation](../administrators_reference_guide/help_certificaterevocationcheckingtasklet_managecertificaterevocationstate.html).

## CRL revocation checking

CRL revocation checking involves querying a CRL distribution-point URL and ensuring that a certificate is not on the returned revocation list maintained at the site. The certificate specifies the URL.

## OCSP revocation checking

OCSP revocation checking provides a more centralized and potentially more reliable means of checking certificate status than CRL revocation checking provides. In this scenario, the incoming certificate embeds an OCSP Responder URL or a configured default URL to query the certificate status.

The primary difference between OCSP and CRL checking is how the verification occurs. CRL checking requires the requesting client to determine if the certificate has been revoked, or if any of the certificates in the chain of issuer certificates has been revoked, based on the returned CRL. With OCSP, the client sends the certificate itself, and the Responder server handles revocation checking to return the certificate status.

Learn more about OCSP in [the RFC2560](https://datatracker.ietf.org/doc/html/rfc2560) specification.

---

---
title: CIBA by ping
description: The OAuth Client Initiated Backchannel Authentication (CIBA) grant by ping process takes place between the client, user, authentication device, PingFederate, and resource server (RS).
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_ciba_by_ping
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_ciba_by_ping.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  processing-steps: Processing steps
  related-links: Related links
---

# CIBA by ping

The OAuth Client Initiated Backchannel Authentication (CIBA) grant by ping process takes place between the client, user, authentication device, PingFederate, and resource server (RS).

After receiving an authentication request acknowledgment, the client waits for a ping callback message from the OpenID Provider (OP). When the OP receives the authorization granted by the user through the authentication device, it sends a ping callback message to the client's notification endpoint. The client then sends a token request to retrieve an access token.

Flowchart depicting the CIBA by poll process between the Client, User, Authentication Device, AS/OP and RS.OAuth CIBA grant by ping

## Processing steps

1. The client sends an authentication request to PingFederate at its client-initiated backchannel authentication endpoint.

   The client must include in its authentication request the desired scope of permissions, one identity hint for PingFederate to identify the user, and a bearer token that PingFederate can use to authenticate the ping callback message. When providing an identity hint, the client has three options:

   * `login_hint`

   * `login_hint_token`

   * `id_token_hint`

     For the bearer token, the client must follow the syntax as defined in [RFC 6750, section 2.1](https://datatracker.ietf.org/doc/html/rfc6750/#autoid-6) and transmit it using the `client_notification_token` parameter.

     The client can include a user code using the `user_code` parameter, transmit all request parameters of the authentication request in a signed request object, or do both.

   The authentication request can be signed or unsigned.

2. PingFederate validates the authentication request and identifies the user based on the hint provided by the client.

3. PingFederate returns an authentication request acknowledgment to the client. The response contains the identifier, `auth_req_id`, that PingFederate assigns to the authentication request.

4. PingFederate invokes a CIBA authenticator based on the applicable CIBA request policy to reach out to the user with the information (for example, the requested scopes) that the user needs to obtain authorization.

5. The authentication device presents the information and works with the user to obtain authorization.

6. The user reviews the information presented by the authentication device and then approves or denies the scopes requested by the client.

7. The authentication device sends the authorization result back to PingFederate.

8. PingFederate sends a ping callback message using the HTTP POST method to the client at its notification endpoint.

   Per specification, PingFederate includes the `client_notification_token` value in the Authorization HTTP request header and the `auth_req_id` value in the message body.

9. The client sends a token request to PingFederate at its token endpoint.

   The client must include in its token request the CIBA grant type, `urn:openid:params:grant-type:ciba`, and the corresponding `auth_req_id` value.

10. PingFederate returns an access token in a token response to the client.

    If the user denies the requested scopes, PingFederate provides the client with a relevant error message in the token response.

11. The client provides the access token to the RS to access protected resources.

12. The RS validates the access token.

13. The RS provides the requested data to the client.

## Related links

* [OpenID Connect Client Initiated Backchannel Authentication Flow](https://openid.net/specs/openid-client-initiated-backchannel-authentication-core-1_0.html)