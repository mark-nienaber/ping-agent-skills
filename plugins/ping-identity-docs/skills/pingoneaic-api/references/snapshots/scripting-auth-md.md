---
title: Auth scripting
description: "You can use authentication and authorization (auth) scripting to modify default Advanced Identity Cloud behavior in many situations: client-side authentication, policy conditions, handling OpenID Connect claims, and others."
component: pingoneaic-api
page_id: pingoneaic-api::scripting-auth
canonical_url: https://developer.pingidentity.com/pingoneaic-api/scripting-auth.html
keywords: ["Extensibility", "Scripts", "Authentication", "OAuth 2.0", "OpenID Connect (OIDC)", "Policies &amp; Entitlements", "Journeys"]
section_ids:
  auth_script_types: Auth script types
  manage-auth-scripts: Manage auth scripts
  create-a-new-auth-script: Create a new auth script
  decision-scripts: Journey decision node scripts
  create-decision-scripts: Create a new journey decision node script
  more-information: More information
---

# Auth scripting

You can use authentication and authorization (auth) scripting to modify default Advanced Identity Cloud behavior in many situations: client-side authentication, policy conditions, handling OpenID Connect claims, and others.

Use JavaScript for auth scripting in Advanced Identity Cloud. Groovy scripts are deprecated and will eventually be completely replaced with JavaScript scripts.

For JavaScript examples of all [auth script types](#auth_script_types), review the [sample scripts](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/sample-scripts.html). Each sample script includes a list of available variables.

|   |                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Scripts can potentially emit the personally identifiable information (PII) of your end users into Advanced Identity Cloud logs, and then into external services that consume Advanced Identity Cloud logs.Ping Identity recommends that you establish a review and testing process for all scripts to prevent PII leaking out of your Advanced Identity Cloud tenant environments. |

## Auth script types

The auth script types available in Advanced Identity Cloud include the following:

> **Collapse: Journeys**
>
> | Script type                 | Description                                                                                                                                           | Information                                                                                                        |
> | --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
> | Configuration Provider Node | Runs in a Configuration Provider node as a step in an authentication journey.                                                                         | [Configuration Provider node](https://docs.pingidentity.com/auth-node-ref/latest/config-provider.html)             |
> | Journey Decision Node       | Runs in a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html) as a step in an authentication journey. | [Scripted Decision node API](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/scripting-api-node.html) |

> **Collapse: OAuth2 / OIDC**
>
> | Script type                      | Description                                                                                                 | Information                                                                                                             |
> | -------------------------------- | ----------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
> | OAuth2 Access Token Modification | Modifies the key-value pairs contained within access tokens before they're issued to a client.              | [Access tokens](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/plugins-access-token-modifier.html)           |
> | OAuth2 Evaluate Scope            | Retrieves and modifies scopes for OAuth 2.0 access token introspection.                                     | [Scope evaluation](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/plugins-scope-evaluator.html)              |
> | OAuth2 May Act                   | Adds the `may_act` claim to tokens when performing token exchanges.                                         | [Token exchange](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/token-exchange.html)                         |
> | OAuth2 Trusted JWT Issuer        | Dynamically retrieves the details of an issuer during the JWT profile for authorization grant.              | [JWT profile for authorization](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/oauth2-jwt-bearer-grant.html) |
> | OAuth2 Validate Scope            | Modifies how Advanced Identity Cloud validates requested OAuth 2.0 scopes.                                  | [Scope validation](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/plugins-scope-validator.html)              |
> | OIDC Claims                      | Modifies or overrides OIDC claims when issuing an ID token or in the response from the `userinfo` endpoint. | [OIDC claims](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/plugins-user-info-claims.html)                  |

> **Collapse: SAML**
>
> | Script type                | Description                                                                              | Information                                                                                                        |
> | -------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
> | SAML2 SP Adapter           | Modifies the processing of the authentication request on the SP.                         | [SP adapter](https://docs.pingidentity.com/pingoneaic/latest/am-saml2/custom-sp-adapter.html)                      |
> | SAML2 IDP Adapter          | Modifies the processing of the authentication request on the IDP.                        | [IdP adapter](https://docs.pingidentity.com/pingoneaic/latest/am-saml2/custom-idp-adapter.html)                    |
> | SAML2 IDP Attribute Mapper | Maps user-configured attributes to SAML attributes in the assertion returned by the IDP. | [IdP attribute mapper](https://docs.pingidentity.com/pingoneaic/latest/am-saml2/plugins-idp-attribute-mapper.html) |
> | SAML2 NameID Mapper        | Customize the value of the NameID attribute in the SAML assertion on the remote SP.      | [NameID mapper](https://docs.pingidentity.com/pingoneaic/latest/am-saml2/custom-nameid-mapper.html)                |

> **Collapse: Other**
>
> | Script type                                     | Description                                                                                                                                                                                                                                                   | Information                                                                                                                                                |
> | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
> | Client-side Authentication                      | Runs on the client during authentication.                                                                                                                                                                                                                     |                                                                                                                                                            |
> | Library                                         | Contains reusable functionality that can be imported into journey decision node scripts or other library scripts.                                                                                                                                             | [Library scripts](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/library-scripts.html)                                                       |
> | Policy Condition                                | Modifies authorization policy decisions.                                                                                                                                                                                                                      | [Scripted policy conditions](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/scripted-policy-condition.html)                              |
> | Social Identity Provider Profile Transformation | Runs in a [Social Provider Handler node](https://docs.pingidentity.com/auth-node-ref/latest/auth-node-social-provider-handler.html). Adapts the fields received from a social identity provider to align with the fields expected by Advanced Identity Cloud. | [Social IdP profile transformation scripting API](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/social-idp-profile-transformation-api.html) |
> | PingOne Verify Completion Decision Node         | Runs in a [PingOne Verify Completion Decision node](https://docs.pingidentity.com/auth-node-ref/latest/auth-node-pingone-verify-completion-decision.html) so that you can access information about the user's PingOne Verify transactions.                    | [PingOne Verify Completion Decision node API](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/p1verify-completion-decision-api.html)          |

|   |                                                                                                                                                                                                                                     |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Some script types aren't yet available in the Advanced Identity Cloud admin console. To view a list of all the script types, under Native Consoles > Access Management, go to Realms > *Realm Name* > Scripts and click New Script. |

## Manage auth scripts

To manage your auth scripts, go to *Realm* > Scripts > Auth Scripts.

On the Scripts page, you can view a list of existing scripts. To edit, duplicate, or delete a script, click its More ([icon: ellipsis-h, set=fa]) menu.

The edit option in the More menu opens the script in a lightweight editor that features syntax highlighting and validation checking. You can maximize the editor to full screen to edit larger scripts:

![Script editor](_images/idcloudui-scripts-editor.png)

① JavaScript editor\
② Fullscreen option\
③ Syntax highlighting\
④ Syntax error highlighting and validation checking

## Create a new auth script

1. Go to *Realm* > Scripts > Auth Scripts, then click + New Script.

2. Choose an auth [script type](#auth_script_types).

   After you select a script type, the editor opens. The editor is prepopulated with a default script for that type, which is intended as a starting point for your custom script.

   If you selected the wrong script type, click Previous to select a different script type.

3. If the [next-generation script engine](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/next-generation-scripts.html) is available for the script type, such as for [journey decision node scripts](#create-decision-scripts), Advanced Identity Cloud displays the Choose Script Engine page.

   Select Legacy or Next Generation to set the script engine for your script.

4. Enter a unique Name and optional Description for the script, then click Save.

   After you save a script, you can't change its type.

## Journey decision node scripts

Learn more about journeys in [Journeys](https://docs.pingidentity.com/pingoneaic/latest/journeys/journeys.html).

You can also create, edit, and validate journey decision node scripts directly from within a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/latest/scripted-decision.html).

1. Go to *Realm* > Journeys.

2. Open a journey in the journey editor.

3. Find an existing scripted decision node or add a new one.

4. Select the scripted decision node to open the context pane on the right side.

5. The following screenshot shows where you can create a new journey decision node script ④ or edit an existing one ⑤:

   ![Journey editor with Scripted Decision node](_images/idcloudui-journeys-scripted-decision-script-options.png)

   ① Scripted decision node\
   ② Context pane\
   ③ Journey decision node script drop-down\
   ④ Add new journey decision node script\
   ⑤ Edit existing journey decision node script

### Create a new journey decision node script

Add a new journey decision node script in the journey editor or from *Realm* > Scripts > Auth Scripts.

1. Select Legacy or Next Generation on the Choose Script Engine page.

   Learn more about the enhanced scripting engine in [Next-generation scripts](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/next-generation-scripts.html).

2. If you create or edit a Next Generation script, click the Libraries icon in the top right to display the following side panel:

   ![Next generation journey decision node script editor](_images/nextgen-editor.png)

   ① View and search library scripts to import in your script.\
   ② Click to expand a library script and view its exported methods and constants.\
   The font colors indicate the exported types:

   * Blue for functions

   * Red for numbers

   * Green for strings

   * Orange for boolean types

   * Purple for objects / properties

   ③ Click the Docs icon to view links to context-related documentation.\
   A red dot denotes documentation updates.\
   ④ Edit your script and import library scripts as necessary.

3. Enter a unique Name and optional Description for the script, then click Save.

## More information

* [User identity attributes and properties reference](https://docs.pingidentity.com/pingoneaic/latest/identities/user-identity-properties-attributes-reference.html)

* [Scripting environment](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/scripting-env.html)

* [Scripting API](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/scripting-api.html)

* [Sample scripts](https://docs.pingidentity.com/pingoneaic/latest/am-scripting/sample-scripts.html)

* [Customize OAuth 2.0 using JavaScript extensions](https://docs.pingidentity.com/pingoneaic/latest/am-oauth2/plugins-customize.html)
