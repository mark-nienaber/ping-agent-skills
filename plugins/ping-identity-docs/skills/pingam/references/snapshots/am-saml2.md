---
title: Configure IdPs and SPs with trees
description: Configure authentication trees for SAML 2.0 identity and service providers to customize single sign-on flows and enforce additional security requirements
component: pingam
version: 8.1
page_id: pingam:am-saml2:configure-providers
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/configure-providers.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
section_ids:
  config-redirect-tree: Redirect to a tree on the hosted SP
  samlapp-tree: Set a SAML 2.0 application tree for a remote SP
---

# Configure IdPs and SPs with trees

After you have set up the entity providers, you can tailor the SAML 2.0 flow to your business needs by configuring the provider settings.

## Redirect to a tree on the hosted SP

For [IdP-initiated SSO in integrated mode](saml2-integrated-mode.html#idpinit-sso-integrated-mode), you must configure the hosted SP to send the user to an authentication tree after validating the SAML 2.0 assertion from the IdP. This lets you perform SAML 2.0 authentication on the SP side.

You can also define additional actions the user must fulfill, such as performing multi-factor authentication or checking organizational details before accessing the SAML 2.0 application.

|   |                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------- |
|   | Include a Scripted Decision node in the tree and query the `samlApplication` binding to access the assertion and response details. |

If a `local authentication URL` is configured, it takes precedence, but AM doesn't validate that the specified tree exists on the hosted SP.

If you haven't configured a tree in either setting, an IdP-initiated SSO SAML flow results in an invalid request error.

For SP-initiated SSO, the flow continues in the originating tree, ignoring any redirect tree configured on the hosted SP.

To configure a redirect tree:

1. Go to Realms > *realm name* > Applications > Federation > Entity Providers > *Hosted SP Name*.

2. Under Assertion Processing > Redirect Tree, select the name of your authentication tree from the Redirect Tree Name list.

   Learn about the `Redirect Tree Name` property in the [hosted SP configuration](saml2-reference.html#config-redirect-tree).

3. Save your changes.

|   |                                                                            |
| - | -------------------------------------------------------------------------- |
|   | You can't delete a tree if it's set as the redirect tree in the hosted SP. |

## Set a SAML 2.0 application tree for a remote SP

Configure the remote SP so that a specific authentication tree is always run for users authenticating with your SAML 2.0 app. The SAML flow invokes the associated tree regardless of any existing sessions or requested or configured authentication contexts.

To configure a SAML 2.0 app tree:

1. Go to Realms > *realm name* > Applications > Federation > Entity Providers > *Remote SP Name*.

2. Under Advanced > Tree Name, select the name of your authentication tree from the list.

   Learn about the `Tree Name` property in the [remote SP configuration](saml2-reference.html#config-treename).

3. Save your changes.

When you configure an app tree, the processing of the SAML request depends on the authentication context requested by the SP. The following table shows the SAML response for a configured comparison type and the requested authentication context.

| Authentication context                     | Comparison type                  | Response                         |
| ------------------------------------------ | -------------------------------- | -------------------------------- |
| SP requested authn context                 | `Exact` / `None`                 | Requested authn context included |
| SP requested authn context                 | `Better` / `Maximum` / `Minimum` | `UNSPECIFIED`                    |
| SP doesn't request authn context           | -                                | `UNSPECIFIED`                    |
| IdP-initiated (no requested authn context) | -                                | `UNSPECIFIED`                    |

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * To prevent users from authenticating directly through this tree, either for security reasons or because the tree is insufficient as a complete authentication service, configure it as a [transactional authentication tree](../am-authentication/configure-auth-trees.html#configure-transactional-auth-tree).

* You can't delete a tree if it's referenced by a SAML 2.0 app. |
