---
title: Choose persistent or transient federation
description: Decide between persistent federation for permanent account links or transient for temporary session links
component: pingoneaic
page_id: pingoneaic:am-saml2:choose-persistent-or-transient-federation
canonical_url: https://docs.pingidentity.com/pingoneaic/am-saml2/choose-persistent-or-transient-federation.html
llms_txt: https://docs.pingidentity.com/pingoneaic/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
page_aliases: ["saml2-guide:persistent-or-transient-federation.adoc", "saml2-guide:choose-persistent-or-transient-federation.adoc"]
---

# Choose persistent or transient federation

In Advanced Identity Cloud, there are two ways to federate users with SAML 2.0:

* Permanently link identities with ***persistent federation***.

  Persistent federation requires an attribute value that is the same on the IdP and the SP; for example, an email address or another unique user identifier. Use this method to link accounts without user interaction.

  For more information, refer to [Link identities automatically based on an attribute value](auto-federation.html#auto-federate-based-on-attribute).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When accounts are persistently linked, authentication is required **only** by the IdP. Authentication *is* required on the SP side if the SP is unable to map the identity in the assertion from the IdP to a local user account. This can happen the first time accounts are linked, for example, after which the persistent identifier establishes the mapping. When the mapping is established, authentication is required only by the IdP. |

* Maintain no user account on the SP with ***transient federation***.

  Transient federation can be useful when the SP needs no user-specific account to provide a service or when you do not want to retain a user profile on the SP, but you make authorization decisions based on attribute values from the IdP.

  When accounts are transiently linked, authentication to the SP might be required.

  The SP must authenticate the user for every SAML assertion received. This is due to the identifier being used to link identities in a transient way. It doesn't provide a repeatable, durable means to link the identities.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can prevent the ability to link accounts persistently.For an SP, set the `Disable NameID Persistence` property to `true` in the NameID Format section of the Assertion Content tab. For more information, refer to [SP assertion content](saml2-reference.html#sp-assertion-content).For an IdP, set the `Disable NameID Persistence` to `true` in the Account Mapper section of the Assertion processing tab. For more information, refer to [IdP assertion processing](saml2-reference.html#idp-assertion-processing). |

Once you choose how you federate users, enable [persistent](enable-persistent-federation.html) or [transient](enable-transient-federation.html) federation.
