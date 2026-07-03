---
title: Link identities automatically with auto-federation
description: Configure PingAM to automatically link identities across SAML 2.0 providers based on matching attribute values
component: pingam
version: 8.1
page_id: pingam:am-saml2:auto-federation
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/auto-federation.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:auto-federation.adoc"]
section_ids:
  auto-federate-based-on-attribute: Link identities automatically based on an attribute value
---

# Link identities automatically with auto-federation

AM lets you configure the SP to automatically link identities based on an attribute value in the assertion returned from the IdP, known as *auto-federation*.

When you know the user accounts on both the IdP and the SP share a common attribute value, such as an email address or other unique user identifier, you can configure AM to map the attributes to each other, and link identities, without the user having to authenticate to the SP.

## Link identities automatically based on an attribute value

This procedure demonstrates how to automatically link identities based on an attribute value that is the same in both accounts.

Before attempting to configure auto-federation, ensure that you have configured AM for SAML 2.0, created the identity and SPs, and configured a circle of trust. You must also have configured AM to support single sign-on. For information on performing those tasks, see [Deployment considerations](saml2-configuration.html) and [Implement SSO and SLO](saml2-sso-slo.html).

Perform the following steps on the hosted IdP(s), and again on the hosted SP(s):

1. Go to Realms > *realm name* > Applications > Federation > Entity Providers, and click on the name of the hosted provider.

AM only displays the configuration of a single role. Click on the labels to select the role view:

![saml-roles](_images/saml-roles.png)

1. On the hosted IdP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration. If the attributes you want to use to link the accounts on the IdP and the SP are not in the map already, add them.

     The IdP will send these attributes in the assertion, and the SP will then map them using its own attribute map.

     > **Collapse: Tips to configure the Attribute Map on the IdP**
     >
     > Before user profile attributes can be mapped, they must be allowed in user profiles and also specified for the identity store. Find more information in [Add custom user profile attributes](../setup/customizing-data-stores.html#sec-maint-datastore-customattr).
     >
     > To see the profile attributes available for an LDAP identity store, log in to the AM admin UI, and go to Realms > *realm name* > Identity Stores > User Configuration. Check the LDAP User Attributes list.
     >
     > By default, you can map single-valued attributes to either user profile attributes or static values.
     >
     > To map a static value, enclose the value in double quotes (`"`), for example:
     >
     > ![The static value is enclosed in double quotes.](_images/static-attr-mapping.png)
     >
     > Figure 1. Example of mapping a static value
     >
     > To map multi-valued attributes, you must implement a [custom IdP attribute mapper](custom-idp-attribute-mapper.html).

   * Save your work.

2. On the hosted SP:

   * Go to the Assertion Processing tab.

   * Review the Attribute Map configuration, and ensure that the attribute mappings you created on the IdP are represented in the map.

     > **Collapse: Tips to Configure the Attribute Map on the SP**
     >
     > The value of Key is a SAML attribute sent in an assertion, and the value of Value is a property in the authenticated session, or an attribute of the user's profile.
     >
     > By default, the SP maps the SAML attributes it receives to equivalent-named session properties. However, when the SP is configured to create identities during autofederation and the identity does not exist yet, the SP maps the SAML attributes to their equivalents in the newly-created user profile.
     >
     > The special mapping `Key: *, Value: *` means that the SP maps each attribute it receives in the assertion to equivalent-named properties or attributes. For example, if the SP receives `mail` and `firstname` in the assertion, it maps them to `mail` and `firstname` respectively.
     >
     > Remove the special mapping and add key pairs to the map if:
     >
     > * (During autofederation) The attributes in the IdP's and the SP's identity stores do not match.
     >
     > * You need control over the names of the session properties.
     >
     > * You need control over which attributes the SP should map, because the IdP adds too many to the assertion.
     >
     > For example, if the SAML attribute is `firstname` and you want the SP to map it to a session property/user profile attribute called `cn`, create a mapping similar to `Key: firstname, Value: cn`.

   * Enable Auto Federation. In the Attribute property, enter the SAML attribute name that the SP will use to link accounts, as configured in the Attribute Map.

   * Save your work.

3. To test your work, initiate single sign-on; for example, as described in [IdP-initiated SSO URLs](saml2-standalone-mode.html#saml2-sso-standalone-idpssoinit).

   Authenticate to the IdP as a test user. Attempt to access the SP. Notice that the user has an authenticated session, and can access their profile page on the SP without having to authenticate again.

---

---
title: Link identities for authentication
description: Link identities between IdP and SP accounts using pseudonym identifiers and authentication trees in PingAM
component: pingam
version: 8.1
page_id: pingam:am-saml2:linking-auth-tree
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/linking-auth-tree.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Authentication", "Accounts", "Nodes &amp; Trees", "Scripts"]
page_aliases: ["saml2-guide:linking-auth-tree.adoc"]
section_ids:
  first_authentication_to_the_sp: First authentication to the SP
  subsequent_authentications_to_the_sp: Subsequent authentications to the SP
  configure-authentication-linking: Configure authentication mechanisms to link accounts
  saml2-integrated-mode-sso-persistent-standard: Link accounts persistently (standalone AM)
  saml2-integrated-mode-sso-persistent-platform: Link accounts persistently (Ping Advanced Identity Software deployment)
---

# Link identities for authentication

IdPs and SPs must be able to communicate information about users. Sometimes the IdP chooses to share a minimum amount of information about an authenticated user.

For example, the IdP can return a generated, opaque `NameID` that can't directly be used to locate an identity in the SP identity store.

AM can use these pseudonym identifiers to establish links between otherwise unrelated accounts, by requiring that the user authenticates to the SP using a linking authentication mechanism.

## First authentication to the SP

The following list describes the sequence of events that occurs the first time a user attempts to authenticate to the AM SP:

1. **Accessing the SP.**

   A user attempts to access a service and is redirected to the AM server acting as the SP.

   The redirect URL specifies an authentication tree containing the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html). For example, `https://www.sp.com:8443/am/XUI/#login/&service=spSAMLTree`.

2. **Authentication at the IdP.**

   AM redirects the user to the IdP. The user authenticates successfully at the IdP. The IdP returns a SAML assertion to the SP.

3. **SP attempts to access a federated identity.**

   AM attempts to locate the identity in its own user store. No link between the IdP identity and a local one is found.

4. **Invocation of the linking authentication node(s).**

   Because no link is found, AM follows the route through the authentication tree that lets the user authenticate on the SP.

5. **Identity federation.**

   After successful authentication at the SP, AM writes the name ID from the assertion into the local user's profile, creating a permanent link between the two identities.

   Find information on creating permanent links between identities in [Persistent or transient federation](persistent-or-transient-federation.html).

   Find an example of an authentication tree that links identities in [Create accounts dynamically during federation](saml2-integrated-mode.html#saml2-integrated-mode-sso-dynamic-standard).

## Subsequent authentications to the SP

The following list describes the sequence of events that occurs during subsequent authentication attempts, after the user's identities on the IdP and SP have been federated:

1. **Accessing the SP.**

   A returning user attempts to access their service and is redirected to the AM server acting as the SP.

   Their login URL specifies the authentication tree containing the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html) and the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html). For example, `https://www.sp.com:8443/am/XUI/#login/&service=spSAMLTree`.

2. **Authentication at the IdP.**

   AM redirects the user to the IdP, and the user authenticates successfully at the IdP. The IdP returns a SAML assertion to the SP.

3. **SP attempts to access a federated identity.**

   AM attempts to locate the name ID in its user store. The search for the name ID succeeds.

   Because there's a match, the user doesn't need to log in to the SP and can access the service.

## Configure authentication mechanisms to link accounts

If you aren't using auto-federation, configure AM to link accounts in one of the following ways, depending on whether AM is standalone or part of an integrated Ping Advanced Identity Software deployment.

### Link accounts persistently (standalone AM)

Configure a tree similar to the following:

![Example tree to link accounts persistently](../am-authentication/_images/trees-node-write-federation-information-example.png)

1. Add a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

   Make sure that the NameID Format specified is `persistent`.

   The node processes the assertion, makes its contents available to the authentication tree's state in the `userInfo` object, and tries to map the assertion's nameID using the `uid` mapping in the SP's assertion map.

   If the node finds a match, the tree continues through the `Account Exists` output. Otherwise, the tree continues through the `No Account Exists` output.

2. On the `No Account Exists` outcome, configure nodes to authenticate the user to the SP.

3. Add a [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html).

### Link accounts persistently (Ping Advanced Identity Software deployment)

Configure a journey similar to the following:

![Example tree to link accounts persistently](_images/link-accounts-platform-example.png)

1. Add a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

   Make sure that the NameID Format specified is `persistent`.

   The node processes the assertion, makes its contents available to the tree's state in the `userInfo` object, and tries to map the assertion's nameID using the `uid` mapping in the SP's assertion map.

   If the node finds a match, the tree continues through the `Account Exists` outcome. Otherwise, the tree continues through the `No Account Exists` outcome.

   Regardless of the outcome, because the node's `nameID` mapping isn't configurable, this example adds nodes to process the `userInfo` object and match it to the managed user's schema.

2. Add a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) to copy the information from the assertion to the authentication tree's shared state.

   > **Collapse: Example next-generation script**
   >
   > ```javascript
   > if (nodeState.get("userInfo")) {
   >   if (nodeState.get("objectAttributes")) {
   >     nodeState.remove("objectAttributes");
   >   }
   >   var userName=null,sn=null,mail=null;
   >
   >   try {
   >     var attribs = nodeState.get("userInfo")["attributes"];
   >
   >     userName=attribs["uid"][0];
   >     sn=attribs["sn"][0];
   >     mail=attribs["mail"][0];
   >
   >   } catch (e) {
   >     logger.error("Error getting userInfo: " + e);
   >   }
   >   nodeState.putShared("username", userName);
   >   nodeState.putShared("objectAttributes", {"userName":userName,"sn":sn,"mail":mail, "givenName": userName});
   > }
   > action.goTo("true");
   > ```
   >
   > |   |                                                                                       |
   > | - | ------------------------------------------------------------------------------------- |
   > |   | You can also query the `samlApplication` binding on the SP side to get the assertion. |

3. Add an [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/8.1/identify-existing-user.html) to search the user with the appropriate attribute.

   For example, `userName`.

4. Authenticate the user to the SP.

5. Add the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html) to the successful outcome of the authentication process to create the link between the accounts.

   If a transient link exists, it is converted into a persistent one.

---

---
title: Link identities to a single, shared account
description: Link identities to a single, shared account on the SP to exchange attributes without creating user-specific accounts using SAML 2.0 federation
component: pingam
version: 8.1
page_id: pingam:am-saml2:auto-federate-using-anonymous
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/auto-federate-using-anonymous.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Accounts"]
page_aliases: ["saml2-guide:auto-federate-using-anonymous.adoc"]
section_ids:
  link_identities_to_an_sp_account: Link identities to an SP account
---

# Link identities to a single, shared account

You temporarily map identities on the IdP to a single account on the SP, for example, the `anonymous` account, to exchange attributes about the user without a user-specific account on the SP.

This approach can be useful when the SP either needs no user-specific account to provide a service, or when you don't want to create or retain identity data on the SP, but instead you make authorization decisions based on attribute values from the IdP.

## Link identities to an SP account

The following steps demonstrate how to auto-federate using a single user account on the SP.

Before attempting these steps, ensure that you have configured AM for SAML 2.0, created the identity and SPs, and configured a circle of trust. You must also have configured AM to support single sign-on. For information on performing those tasks, see [Deployment considerations](saml2-configuration.html) and [Implement SSO and SLO](saml2-sso-slo.html).

1. On the hosted IdP:

   * In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP*.

   * On the Assertion Processing tab, if the attributes you want to access from the SP are not yet included in the Attribute Map property, add the attribute mappings.

     Enter attribute map values using the following format: `SAML Attribute Name=Profile Attribute Name`.

   * Save your work.

2. On the hosted SP:

   * In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted SP*.

   * On the Assertion Processing tab, if the attributes you want to access from the IdP are not yet included in the Attribute Map property, add the attribute mappings.

     Enter attribute map values using the following format: `SAML Attribute Name=Profile Attribute Name`.

     |   |                                                                                                                                                                    |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | You can use a special wildcard mapping of `*=*`, which maps each attribute in the assertion to an identically named attribute on the SP, using the relevant value. |

   * Ensure that the Auto Federation property is not selected.

   * In the Transient User field, add the account name AM will use to link all identities from the IdP, for example; `anonymous`.

   * Save your work.

3. To test your work:

   * Create a new user on the IdP, including values for any attributes you mapped in the providers.

   * Log out of the AM admin UI, and initiate SSO using transient federation; for example, as described in [Enable transient federation](persistent-or-transient-federation.html#transient-federation).

   * Authenticate to the IdP as the new user you created.

   * After successfully authenticating to the IdP, check that the identity is linked to a transient account by performing the following steps:

     * In a separate browser or private window, log in to the AM admin UI of the SP.

     * Go to Realms > *realm name* > Sessions.

     * Enter the transient user name you configured earlier; for example, `anonymous`.

       You will see one or more sessions of users who have initiated single sign-on and been temporarily linked to the transient user account.

---

---
title: NameID mapper
description: Customize the NameID attribute value returned in SAML assertions using Java or JavaScript extensions
component: pingam
version: 8.1
page_id: pingam:am-saml2:custom-nameid-mapper
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-nameid-mapper.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Java", "Scripts"]
page_aliases: ["saml2-guide:custom-nameid-mapper.adoc"]
section_ids:
  java_example: Java example
  scripted_example: Scripted example
---

# NameID mapper

Use this extension point to customize the value of the NameID attribute returned in the SAML assertion.

These steps assume your environment is already correctly configured for SSO using SAML 2.0, where AM is the hosted IdP.

## Java example

To create a custom NameID mapper in Java, follow these high-level steps:

1. Clone the [am-external](https://github.com/ForgeRock/am-external) Git repository. For example:

   ```bash
   $ git clone https://github.com/ForgeRock/am-external.git
   ```

   Learn about using AM source code in [How do I access the proprietary Maven repositories?](https://support.pingidentity.com/s/article/How-do-I-access-the-proprietary-Maven-repositories).

2. Check out the branch for your release version, for example:

   ```bash
   $ cd am-external
   $ git checkout releases/[.replaceable]##version##
   $ cd openam-federation
   ```

3. Create a new Java project and add the `openam-federation-library` as a Maven dependency, for example:

   ```bash
   <dependency>
     <groupId>org.forgerock.am</groupId>
     <artifactId>openam-federation-library</artifactId>
   </dependency>
   ```

4. Write a Java class that extends the `com.sun.identity.saml2.plugins.DefaultIDPAccountMapper` class.

   Refer to the [com.sun.identity.saml2.plugins.IDPAccountMapper](../_attachments/apidocs/com/sun/identity/saml2/plugins/IDPAccountMapper.html) interface for implementation details.

5. Override the `getNameID()` method to return a customized NameID value. For example:

   ```bash
   public class CustomIDPAccountMapper extends DefaultIDPAccountMapper{

       @Override
       public NameID getNameID(Object session, String hostEntityID, String remoteEntityID,
               String realm, String nameIDFormat) throws SAML2Exception {

           NameID myNameID = super.getNameID(session, hostEntityID, remoteEntityID, realm, nameIDFormat);

           if (remoteEntityID.equals("https://sp.example.com:8443/am") {
               myNameID.setValue(myNameID.getValue() + "@sp.example.com");
           }

           return myNameID;
       }
   }
   ```

6. Package your custom class in a JAR file and copy to the `/WEB-INF/lib` folder where you deployed AM.

7. Configure AM to use the new Java plugin.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP* > Assertion Processing.

   2. In the Account Mapper field, type the fully qualified name of your custom class.

   3. Save your changes.

8. Restart AM or the container in which it runs.

9. Test your changes.

## Scripted example

Learn about NameID mapper scripts from the following resources:

* Next-generation example script

  [SAML2 NameID Mapper Script](../am-scripting/sample-scripts.html#saml2-nameid-mapper-js)

* Scripting API

  [NameID mapper scripting API](../am-scripting/saml2-nameid-mapper-api.html)

Follow these steps to use an example script to customize the NameID value:

1. In the AM admin UI, go to Realms > *realm name* > Scripts, and [create a new script](../am-scripting/manage-scripts-console.html) of type `Saml2 NameID Mapper`.

   |   |                                                                                                                                                   |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The NameID mapper script type is a [next-generation script](../am-scripting/next-generation-scripts.html) only and must be written in JavaScript. |

2. In the Script field, set a custom value for NameID. For example:

   ```javascript
   /*
    * Retrieve nameID value from Java plugin and modify
   */
   function getModifiedNameID() {
     var nameIDValue = nameIDScriptHelper.getNameIDValue();

     if (nameIDValue.includes(".com")) {
         return nameIDValue.replace(".com", ".org");
     }
     return nameIDValue;
   }

   /*
    * Use identity binding to gather attributes
   */
   function getIdentityNameID() {
     var givenName = identity.getAttributeValues("givenName")[0];
     var lastName = identity.getAttributeValues("sn")[0];

     return givenName + "_" + lastName;
   }

   getModifiedNameID();
   //getIdentityNameID();
   ```

3. Validate and save your changes.

4. Configure AM to use the updated NameID mapper script.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *remote SP* > Assertion Processing.

   2. Under Account Mapper, select your script from the SAML2 Name ID Mapper Script drop-down list.

   3. Save your changes.

5. Test your changes using an SP-initiated flow.

   Verify that the SAML 2.0 assertion shows an updated value, for example:

   ```xml
   <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress"
                NameQualifier="idp"
                SPNameQualifier="sp">bjensen@example.org</saml:NameID>
   ```

---

---
title: Persistent or transient federation
description: Configure persistent or transient federation in PingAM SAML 2.0 to link user identities across identity providers and service providers
component: pingam
version: 8.1
page_id: pingam:am-saml2:persistent-or-transient-federation
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/persistent-or-transient-federation.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Accounts"]
page_aliases: ["saml2-guide:persistent-or-transient-federation.adoc"]
section_ids:
  persistent-federation: Persistent federation
  enable-persistent-federation: Enable persistent federation
  to-manage-persistent-federation: Change persistent federation
  initiate_change_from_the_idp: Initiate change from the IdP
  initiate_change_from_the_sp: Initiate change from the SP
  terminate_persistent_federation: Terminate persistent federation
  transient-federation: Transient federation
  enable-transient-federation: Enable transient federation
---

# Persistent or transient federation

You can choose to permanently link identities, known as *persistent federation*. AM lets you configure the SP to persistently link identities, based on an attribute value from the IdP. When you know the user accounts on both the IdP and the SP share a common attribute value, such as an email address or another unique user identifier, you can use this method to link accounts without user interaction. See [Link identities automatically based on an attribute value](auto-federation.html#auto-federate-based-on-attribute).

Sometimes the IdP can choose to communicate a minimum of information about an authenticated user, with no user account maintained on the SP side. This is known as *transient federation*.

Transient federation can be useful when the SP either needs no user-specific account to provide a service, or when you don't want to retain a user profile on the SP, but instead, you make authorization decisions based on attribute values from the IdP.

In a SAML 2.0 federation where accounts have been persistently linked, authentication is required only on the IdP side.

Authentication *is* required on the SP side, however, when the SP is unable to map the identity in the assertion from the IdP to a local user account.

This can happen the first time accounts are linked, for example. After which, the persistent identifier establishes the mapping.

Authenticating to the SP may also be required when transient federation is used when linking identities. The SP must authenticate the user for every SAML assertion received. This is because the identifier used to link the identities is transient; it doesn't provide a repeatable, durable means to link the identities.

|   |                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can prevent the ability to persistently link accounts on the SP side by setting the `spDoNotWriteFederationInfo` property to `true`, and on the IdP side by setting the `idpDisableNameIDPersistence` to `true`. |

## Persistent federation

Both integrated and standalone SAML 2.0 implementations allow you to persistently link accounts.

Before attempting to configure persistent federation, make sure that you have configured AM for SAML 2.0 SSO, created the IdP and SPs, and configured a circle of trust.

Find information about these tasks in [Deployment considerations](saml2-configuration.html) and [Implement SSO and SLO](saml2-sso-slo.html).

### Enable persistent federation

1. If you are using integrated mode:

   * Create an authentication tree that contains the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

     If you haven't created one yet, find an example in [SSO in integrated mode](saml2-integrated-mode.html).

   * In the NameID Format field, specify the value `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`.

     |   |                                                                                                                                                                                                                                                                                                                                     |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can also link accounts together using different nameid formats. For example, you could use the `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified` value, and receive the IdP user's e-mail address in the NameID value. The SP would display the login page to identify the local user account and persistently link them. |

   * Save your work.

   * Initiate single sign-on by accessing a URL that calls an authentication tree that includes the SAML2 node.

     For example, `https://www.sp.com:8443/am/XUI/#login/&realm=alpha&service=mySAML2Tree`.

2. If you are using standalone mode SSO:

   * Initiate SSO with either the `spssoinit` or `idpssoinit` URLs, including `NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` as a query parameter.

     For example, to initiate SSO from the SP, access a URL similar to the following:

     ```
     https://www.sp.com:8443/am/spssoinit
     ?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam
     &metaAlias=/sp
     &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
     ```

     To initiate SSO from AM acting as the IdP, access a URL similar to the following:

     ```
     https://www.idp.com:8443/am/idpssoinit
     ?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam
     &metaAlias=/idp
     &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
     ```

3. To test your work:

   * Authenticate to the IdP as the user you want to persistently link.

     On success, you will be redirected to the SP.

     |   |                                                                                                                                                                                                                                                                                                                                            |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
     |   | If there was no login page displayed at the SP, you might have enabled auto-federation, or AM was able to find a link between the two identities without requiring authentication at the SP.To make sure there are no existing links, create a new identity in the IdP, and initiate SSO again, authenticating to the IdP as the new user. |

   * Authenticate to the SP as the local user to link with.

     The accounts are persistently linked, with persistent identifiers stored in the user's profile on both the IdP and the SP.

     Subsequent attempts to access the SP will only require that the user authenticates to the IdP, as the identities are now permanently linked.

     |   |                                                                                                                                                                                                                     |
     | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | You can prevent the ability to persistently link accounts on the SP side by setting the `spDoNotWriteFederationInfo` property to `true`, and on the IdPside by setting the `idpDisableNameIDPersistence` to `true`. |

### Change persistent federation

The SAML 2.0 Name Identifier management profile lets you change a persistent identifier that federates accounts and lets you terminate federation for an account.

When user accounts are stored in an LDAP directory server, name identifier information is stored on the `sun-fm-saml2-nameid-info` and `sun-fm-saml2-nameid-infokey` attributes of a user's entry.

|   |                                                                                                                          |
| - | ------------------------------------------------------------------------------------------------------------------------ |
|   | To configure these attribute types, go to Configure > Global Services > SAMLv2 Service Configuration in the AM admin UI. |

AM provides two endpoints for managing persistently linked accounts; `IDPMniInit` for initiating changes from the IdP side, and `SPMniInit` for initiating changes from the SP side.

#### Initiate change from the IdP

1. Get the name identifier value on the SP side by checking the value of `sun-fm-saml2-nameid-info`.

   For example, if the user's entry in the directory shows the following:

   ```bash
   sun-fm-saml2-nameid-info: https://www.sp.com:8443/am|
     https://www.idp.com:8443/am|
     ATo9TSA9Y2Ln7DDrAdO3HFfH5jKD|
     https://www.idp.com:8443/am|
     urn:oasis:names:tc:SAML:2.0:nameid-format:persistent|
     9B1OPy3m0ejv3fZYhlqxXmiGD24c|
     https://www.sp.com:8443/am|
     SPRole|
     false
   ```

   The name identifier on the SP side is `9B1OPy3m0ejv3fZYhlqxXmiGD24c`.

2. Call the `/IDPMniInit` endpoint to initiate a change request from the SP. Make sure you URL-encode the parameters. For example:

   ```bash
   https://www.idp.com:8443/am/IDPMniInit
   ?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam
   &metaAlias=/idp
   &requestType=NewID
   &SPProvidedID=9B1OPy3m0ejv3fZYhlqxXmiGD24c
   ```

   > **Collapse: IDPMniInit parameters**
   >
   > * `spEntityID`
   >
   >   (Required) Use this parameter to indicate the remote SP. Make sure you URL-encode the value. For example, specify `spEntityID=https://www.sp.com:8443/am` as `spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam`.
   >
   > * `metaAlias`
   >
   >   (Required) Use this parameter to specify the local alias for the provider; such as, `metaAlias=/myRealm/idp`. This parameter takes the format `/realm-name/provider-name` as described in [MetaAlias](saml2-reference.html#idp-metaalias).
   >
   >   You don't repeat the slash for the Top Level Realm, for example, `metaAlias=/idp`.
   >
   > * `requestType`
   >
   >   (Required) Type of manage name ID request, either `NewID` to change the ID, or `Terminate` to remove the information that links the accounts on the IdP and SP.
   >
   > * `SPProvidedID`
   >
   >   (Required if `requestType=NewID`) Name identifier in use as described above.
   >
   > * `affiliationID`
   >
   >   (Optional) Use this parameter to specify a SAML affiliation identifier.
   >
   > * `binding`
   >
   >   (Optional) Use this parameter to indicate which binding to use for the operation. The full, long-name format is required for this parameter to work.
   >
   >   The value must be one of the following:
   >
   >   * `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`
   >
   >   * `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect`
   >
   >   * `urn:oasis:names:tc:SAML:2.0:bindings:SOAP`
   >
   > * `relayState`
   >
   >   (Optional) Use this parameter to specify where to redirect the user when the process is complete. Make sure you URL-encode the value. For example, `relayState=https%3A%2F%2Fpingidentity.com` takes the user to `https://pingidentity.com`.

#### Initiate change from the SP

1. Get the name identifier value on the IdP side by checking the value of the `sun-fm-saml2-nameid-infokey` property.

   For example, if the user's entry in the directory shows:

   ```bash
   sun-fm-saml2-nameid-infokey:
     https://www.idp.com:8443/am|
     https://www.sp.com:8443/am|
     XyfFEsr6Vixbnt0BSqIglLFMGjR2
   ```

   The name identifier on the IdP side is `XyfFEsr6Vixbnt0BSqIglLFMGjR2`.

2. Call the `/SPMniInit` endpoint to initiate a change request from the SP. Make sure you URL-encode the parameters. For example:

   ```bash
   https://www.sp.com:8443/am/SPMniInit
   ?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam
   &metaAlias=/sp
   &requestType=NewID
   &IDPProvidedID=XyfFEsr6Vixbnt0BSqIglLFMGjR2
   ```

   > **Collapse: SPMniInit parameters**
   >
   > * `idpEntityID`
   >
   >   (Required) Use this parameter to indicate the remote IdP. Make sure you URL-encode the value. For example, specify `idpEntityID=https://www.idp.com:8443/am` as `idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam`.
   >
   > * `metaAlias`
   >
   >   (Required) Use this parameter to specify the local alias for the provider; such as, `metaAlias=/myRealm/sp`. This parameter takes the format `/realm-name/provider-name` as described in [MetaAlias](saml2-reference.html#sp-metaalias).
   >
   >   You don't repeat the slash for the Top Level Realm, for exmaple, `metaAlias=/sp`.
   >
   > * `requestType`
   >
   >   (Required) Type of manage name ID request, either `NewID` to change the ID, or `Terminate` to remove the information that links the accounts on the identity provider and service provider.
   >
   > * `IDPProvidedID`
   >
   >   (Required if `requestType=NewID`) Name identifier in use as described above.
   >
   > * `affiliationID`
   >
   >   (Optional) Use this parameter to specify a SAML affiliation identifier.
   >
   > * `binding`
   >
   >   (Optional) Use this parameter to indicate which binding to use for the operation. The full, long name format is required for this parameter to work.
   >
   >   The value must be one of the following:
   >
   >   * `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`
   >
   >   * `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect`
   >
   >   * `urn:oasis:names:tc:SAML:2.0:bindings:SOAP`
   >
   > * `relayState`
   >
   >   (Optional) Use this parameter to specify where to redirect the user when the process is complete. Make sure you URL-encode the value. For example, `relayState=https%3A%2F%2Fpingidentity.com` takes the user to `https://pingidentity.com`.

### Terminate persistent federation

AM lets you terminate account federation, where the accounts have been linked with a persistent identifier, as described in [Enable persistent federation](#persistent-federation).

The examples below work in an environment where the IdP is `www.idp.example` and the SP is `www.sp.example`. Both providers have deployed AM on port 8443 under deployment URI `/am`.

1. To initiate the process of terminating account federation from the SP, access the following URL with at least the query parameters shown:

   ```
   https://www.sp.com:8443/am/SPMniRedirect
   ?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam
   &metaAlias=/sp
   &requestType=Terminate
   ```

2. To initiate the process of terminating account federation from the IdP, access the following URL with at least the query parameters shown:

   ```
   https://www.idp.com:8443/am/IDPMniRedirect
   ?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam
   &metaAlias=/idp
   &requestType=Terminate
   ```

## Transient federation

Both integrated and standalone SAML 2.0 implementations allow you to temporarily link accounts.

Before you configure transient federation, you must do the following:

* Configure AM for SAML 2.0

* Create the IdP and SPs

* Configure a circle of trust

* Configure AM to support SSO

Find information about these tasks in [Set up IdPs and SPs in a CoT](saml2-providers-and-cots.html) and [Implement SSO and SLO](saml2-sso-slo.html).

### Enable transient federation

1. If you are using integrated mode SSO:

   * Create an authentication tree that contains the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

     If you haven't created one yet, find an example in [SSO in integrated mode](saml2-integrated-mode.html).

   * In the NameID Format field, specify the value `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`.

   * Save your work.

   * Initiate SSO by accessing a URL that calls an authentication tree that includes the SAML 2.0 node:

     For example, `https://www.sp.com:8443/am/XUI/#login/&realm=alpha&service=mySAMLTree`.

2. If you are using standalone mode SSO:

   * Initiate SSO with either the `/spssoinit` or `/idpssoinit` URLs, including `NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:transient` as a query parameter.

     For example, to initiate SSO from the SP, access a URL similar to the following:

     ```
     https://www.sp.com:8443/am/spssoinit
     ?idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam
     &metaAlias=/sp
     &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:transient
     ```

     To initiate SSO from the IdP, access a URL similar to the following:

     ```
     https://www.idp.com:8443/am/idpssoinit
     ?spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam
     &metaAlias=/idp
     &NameIDFormat=urn:oasis:names:tc:SAML:2.0:nameid-format:transient
     ```

3. To test your work:

   * Authenticate to the IdP as the user you want to temporarily link.

     On success, you will be redirected to the SP.

   * Authenticate to the SP as the local user.

     The accounts are only linked temporarily for the duration of the session. Once the user logs out, the accounts are no longer linked.

     Nothing is written in the user's profile on either the IdP and the SP.

     Subsequent attempts to access the SP will require that the user authenticates to the IdP *AND* the SP (assuming no existing session exists), as the identities aren't linked.

---

---
title: Reference
description: SAML 2.0 configuration properties for service providers, identity providers, and circles of trust in PingAM
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-reference
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-reference.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Algorithm"]
page_aliases: ["saml2-guide:saml2-reference.adoc"]
section_ids:
  saml2-hosted-idp-configuration: Hosted IdP configuration
  idp-assertion-content: Assertion content
  signing_and_encryption: Signing and Encryption
  nameid_format: NameID Format
  hosted-idp-authncontext: Authentication Context
  assertion_time: Assertion Time
  assertion-cache: Assertion Cache
  idp-assertion-processing: Assertion processing
  attribute_mapper: Attribute Mapper
  account_mapper: Account Mapper
  local_configuration: Local Configuration
  idp-services: Services
  idp_service_attributes: IDP Service Attributes
  nameid_mapping: NameID Mapping
  idp-advanced: Advanced settings
  sae_configuration: SAE Configuration
  ecp_configuration: ECP Configuration
  session_synchronization: Session Synchronization
  idp_finder_implementation: IDP Finder Implementation
  relay_state_url_list: Relay State URL List
  idp_adapter: IDP Adapter
  application_context: Application Context
  saml2-remote-idp-configuration: Remote IdP configuration
  remote-idp-assertion-content: Assertion content
  signing_and_encryption_2: Signing and Encryption
  nameid_format_2: NameID Format
  secrets: Secrets
  basic_authentication: Basic Authentication
  client_authentication: Client Authentication
  remote-idp-services: Services
  idp_service_attributes_2: IDP Service Attributes
  nameid_mapping_2: NameID Mapping
  saml2-hosted-sp-configuration: Hosted SP configuration
  sp-assertion-content: Assertion content
  signing_and_encryption_3: Signing and Encryption
  nameid_format_3: NameID Format
  hosted-sp-authncontext: Authentication Context
  basic_authentication_2: Basic Authentication
  sp-hosted-client-auth: Client Authentication
  sp-assertion-processing: Assertion processing
  attribute_mapper_2: Attribute Mapper
  auto_federation: Auto Federation
  account_mapper_2: Account Mapper
  artifact_message_encoding: Artifact Message Encoding
  url: URL
  config-redirect-tree: Redirect Tree
  adapter: Adapter
  sp-services: Services
  sp_service_attributes: SP Service Attributes
  sp-advanced: Advanced settings
  sae_configuration_2: SAE Configuration
  ecp_configuration_2: ECP Configuration
  idp_proxy: IDP Proxy
  session_synchronization_2: Session Synchronization
  relay_state_url_list_2: Relay State URL List
  saml2-remote-sp-configuration: Remote SP configuration
  remote-sp-assertion-content: Assertion content
  signing_and_encryption_4: Signing and Encryption
  nameid_format_4: NameID Format
  secrets_2: Secrets
  basic_authentication_3: Basic Authentication
  remote-sp-assertion-processing: Assertion processing
  attribute_mapper_3: Attribute Mapper
  artifact_message_encoding_2: Artifact Message Encoding
  remote-sp-services: Services
  sp_service_attributes_2: SP Service Attributes
  remote-sp-advanced: Advanced settings
  sae_configuration_3: SAE Configuration
  idp_proxy_2: IDP Proxy
  config-treename: Tree Name
  application_context_2: Application Context
  saml2-cot-configuration: CoT configuration
  saml2-advanced-properties: SAML 2.0 advanced properties
---

# Reference

This reference section covers service provider (SP), identity provider (IdP), and circle of trust (CoT) configuration properties. For the global services reference, see [Reference](../am-reference/preface.html).

## Hosted IdP configuration

After you've set up a hosted IdP, you can configure it through the AM admin UI under Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP*.

### Assertion content

The following groups appear on the Assertion Content tab:

#### Signing and Encryption

* Request/Response Signing

  Specifies which parts of messages the IdP requires the SP to sign digitally.

* Encryption

  When selected, the SP must encrypt NameID elements.

* Secret Label and Algorithms

  * Secret Label Identifier

    An identifier for the secret label AM uses for this entity provider when resolving secrets.

    For example, if you set this value to `demo`, the entity provider uses the following secret labels:

    * `am.applications.federation.entity.providers.saml2.demo.signing`

    * `am.applications.federation.entity.providers.saml2.demo.encryption`

  If not specified, AM uses the entity provider role-specific, default global secret labels. Learn more in [Secret label mappings for SAML 2.0 signing and encryption](../security/secret-mapping.html#secrets-saml2-signing-encryption).

  * Signing Algorithm

    The algorithms the provider can use to sign the request/response attributes selected in the Request/Response Signing group.

    These algorithms are exposed in the provider's metadata extension.

    This property has no default.

  * Digest Algorithm

    The digest algorithms the provider can use when signing the requests and responses selected in the Request/Response Signing group.

    These algorithms are exposed in the provider's metadata extension.

    This property has no default.

  * Encryption Algorithm

    This field specifies two types of encryption algorithms for the provider:

    * Symmetric algorithms, which the provider can use to encrypt the objects selected in the Encryption group. Select one or more AES algorithms from the drop-down list.

      Default: `http://www.w3.org/2001/04/xmlenc#aes128-cbc`

    * Asymmetric algorithms, advertised as the provider's transport key algorithm. When SAML 2.0 token encryption is enabled, hosted providers should use the algorithm the remote provider is advertising when encrypting symmetric encryption keys.

      Select one or more algorithms from the list:

      > **Collapse: Key transport algorithms**
      >
      > * <http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p> (default).
      >
      > * [http://www.w3.org/2009/xmlenc11#rsa-oaep](https://www.w3.org/TR/xmlenc-core1/#sec-RSA-OAEP).
      >
      >   When this algorithm is configured, AM will use the Mask Generation Function Algorithm property (Configure > Global Services > Common Federation Configuration) to create the transport key.
      >
      >   You can find a list of supported mask generation function algorithms in [Algorithms](../setup/services-configuration.html#global-federation-common-algorithms).
      >
      > * <http://www.w3.org/2001/04/xmlenc#rsa-1_5>.
      >
      >   For security reasons, you shouldn't use this option.

#### NameID Format

* NameID Format List

  Specifies the supported name identifiers for users that are shared between providers for single sign-on (SSO).

  The following diagram shows how the hosted IdP decides which of the supported NameID formats is used:

  ![Diagram showing how the hosted IdP decides which supported NameID format is used.](_images/nameid-format-flow-hosted-idp.svg)

* NameID Value Map

  Maps a NameID format (Key) to a user profile attribute (Value). The `persistent` and `transient` NameID formats don't have to be mapped.

  The mapped user profile attribute must exist in your identity store. To find available attributes, go to Realms > *realm name* > Identity Stores > *identity store name* > User Configuration and review the list under LDAP User Attributes. Find the default list of user profiles attributes for DS in [LDAP User Attributes](../setup/data-stores-opendj.html#ldap_user_attributes).

  NameID mapping supports Base64-encoded binary values. Select the Binary option to Base64-encode the attribute's value before it's added to the assertion.

#### Authentication Context

* Mapper

  A class that implements the `IDPAuthnContextMapper` interface and sets up the authentication context.

  Default value: `com.sun.identity.saml2.plugins.DefaultIDPAuthnContextMapper`

* Authentication Context

  Maps the authentication context classes supported by the IdP and the authentication mechanisms used by AM when an SP specifies an authentication context class in a SAML 2.0 request.

  * Context Reference

    Select from the following options to define a context reference:

    * Predefined Reference to choose from a list of supported context references.

    * Custom Reference to type your own reference to an authentication context.

  * Key

    Select an authentication mechanism from the list for AM to use when the SP specifies an authentication context class in a SAML 2.0 request.

    > **Collapse: Authentication mechanisms**
    >
    > * Service
    >
    >   Specify an authentication tree for AM to use to authenticate the end user.
    >
    >   For example, in the Value field, enter `HmacOneTimePassword` to use the built-in one-time passcode (OTP) example authentication tree.
    >
    > * Module
    >
    >   This property was used only for authentication with modules and chains and is no longer documented.
    >
    > * Authentication Level
    >
    >   AM authenticates the user with a method that has an associated authentication level equal to or higher than the specified value.
    >
    >   If there is more than one suitable method, AM presents the available options by using a `ChoiceCallback`.
    >
    >   Learn more about using and returning callbacks during authentication in [Authenticate over REST](../am-authentication/authn-rest.html).
    >
    > |   |                                                                        |
    > | - | ---------------------------------------------------------------------- |
    > |   | The `Role` and `User` options are deprecated. Don't use these options. |

  * Value

    The name of the authentication mechanism you selected from the Key list. For example, if you chose `Service` as the authentication mechanism, enter the name of an authentication tree.

  * Level

    The order of precedence of the supported context reference classes as a numeric value.

Classes with higher numbers are considered stronger than lower numbered classes. The values determine which authentication classes can be used when the SP makes an authentication request that uses a comparison attribute; for example, `minimum` or `better`.

The value of this field should match the auth level of the service. For example, if you configured an authentication mechanism as a tree that sets an auth level of 10, set the same value as you specified in the Level field. Because AM compares the current auth level against the level specified in Authentication Context table, if the two values don't match, AM could require a logged-in user to re-authenticate.

> **Collapse: Example**
>
> ![Choose the authentication mechanisms AM uses when receiving authentication requests that specify an authentication context class.](_images/auth-context-mappings.png)

\+ Learn more about authentication context classes in [Authentication Context for the OASIS Security Assertion Markup Language (SAML) 2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-authn-context-2.0-os.pdf) in the *SAML 2.0 Standard*.

\+ Default value: `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`

#### Assertion Time

* Not-Before Time Skew

  Grace period in seconds for the `NotBefore` time in assertions.

* Effective Time

  Validity in seconds of an assertion.

Basic Authentication

* Enabled, User Name, Password

  When enabled, authenticate with the specified user name and password at SOAP endpoints.

#### Assertion Cache

* Enabled

  When enabled, cache assertions.

### Assertion processing

The following properties appear on the Assertion Processing tab:

#### Attribute Mapper

Learn more in [IdP attribute mapper](custom-idp-attribute-mapper.html).

* Attribute Mapper

  The Java class for a custom Attribute Mapper. This class isn't invoked if a script is selected for `Attribute Mapper Script`.

  Default: `com.sun.identity.saml2.plugins.DefaultIDPAttributeMapper`

* Attribute Mapper Script

  The script for a custom Attribute Mapper.

  Select from a list of all the `Saml2 IDP Attribute Mapper` type scripts saved to this realm, including the default template script, `SAML2 IDP Attribute Mapper Script`.

  You can find details in [saml2-idp-attribute-mapper.js](../am-scripting/sample-scripts.html#saml2-idp-attribute-mapper-js).

* Attribute Map

  Map SAML attributes to user profile attributes.

  Before user profile attributes can be mapped, they must be allowed in user profiles and also specified for the identity store. Find more information in [Add custom user profile attributes](../setup/customizing-data-stores.html#sec-maint-datastore-customattr).

  To see the profile attributes available for an LDAP identity store, log in to the AM admin UI, and go to Realms > *realm name* > Identity Stores > User Configuration. Check the LDAP User Attributes list.

  By default, you can map single-valued attributes to either user profile attributes or static values.

  To map a static value, enclose the value in double quotes (`"`), for example:

  ![The static value is enclosed in double quotes.](_images/static-attr-mapping.png)Figure 1. Example of mapping a static value

  To map multi-valued attributes, you must implement a [custom IdP attribute mapper](custom-idp-attribute-mapper.html).

#### Account Mapper

* Account Mapper

  The class that implements an `AccountMapper` to map remote users to local user profiles.

* Disable NameID Persistence

  Disables the storage of the NameID values in the identity store for all NameIDs issued by the IdP instance as long as the NameID format is anything but the persistent NameID format: `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`. That is, you can disable the storage of NameID values with persistent NameID-Format if and only if there is a NameID value mapping set up for the NameID-Format.

  |   |                                                                                                                                                                                                                                                                              |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | By preventing the storage of the NameID values, the `ManageNameID` and the `NameIDMapping` SAML profiles won't work when using any persistent NameID formats. Existing account links that have been established and stored aren't removed when disabling NameID persistence. |

  Default value: `false`

#### Local Configuration

* Auth URL

  An alternative URL for authenticating users, for example, if you have created a custom user interface other than the UI.

  If present, this overrides the default UI login URL used to authenticate users during federation.

  The specified authentication URL is responsible for authenticating the federated user and must establish a session in AM, and return the SSO token value in the configured cookie name, usually `iPlanetDirectoryPro`.

  The domain of the authentication URL must be configured in AM so that the cookie is accepted, and if host cookies are configured in AM, then the fully qualified domain name of the authentication URL must be identical to that of the AM instance.

  Learn more about configuring the domains AM accepts in the SSO cookies in [Change the cookie domain](../security/changing-cookie-domain.html).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | AM redirects users to the URL specified and appends a `goto` parameter. The parameter contains the URL the user must be redirected to after authentication. The specified authentication URL mustn't override the `goto` parameter, as that would redirect the user elsewhere and federation will fail.Learn more in [Success and failure redirection URLs](../am-authentication/redirection-url-precedence.html). |

* Reverse Proxy URL

  The reverse proxy URL if a reverse proxy is used for SAML endpoints.

* External Application Logout URL

  The URL to which to send an HTTP POST including all cookies when receiving a logout request. To add a user session property as a POST parameter, include it in the URL query string as a `appsessionproperty` parameter.

### Services

The following properties appear on the Services tab:

* MetaAlias

  The MetaAlias value used to locate the provider's entity identifier, specified as `[/realm-name]*/provider-name`, where *provider-name* can't contain slash characters (`/`). For example: `/myRealm/mySubrealm/idp`.

  The MetaAlias must be unique for each provider configured in a CoT and in the realm.

#### IDP Service Attributes

* Artifact Resolution Service

  The endpoint to manage artifact resolution. The Index is a unique number identifier for the endpoint.

* Single Logout Service

  The endpoints to manage single logout (SLO), depending on the SAML binding selected.

* Manage NameID Service

  The endpoints to manage name identifiers, depending on the SAML binding selected.

* Single SignOn Service

  The endpoints to manage SSO.

  These endpoints are used only for SP-initiated flows but are included as a requirement of the [SAML 2.0 Metadata specification](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf).

* Assertion ID Request Service

  The endpoints to request for a specific assertion by referring to its assertion ID.

#### NameID Mapping

* URL

  The endpoint to manage name identifier mapping.

### Advanced settings

The following properties appear on the Advanced tab:

#### SAE Configuration

* IDP URL

  The endpoint to manage Secure Attribute Exchange requests.

* Application Security Configuration

  Indicate how encryption for Secure Attribute Exchange operations should be handled.

#### ECP Configuration

* IDP Session Mapper

  The class that finds a valid session from an HTTP servlet request to an IdP with a SAML Enhanced Client or Proxy profile.

#### Session Synchronization

* Enabled

  Select this option to make the IdP send a SOAP logout request over the back channel to all SPs when an authenticated session times out. An authenticated session can time out when the maximum idle time or maximum session time is reached, for example.

#### IDP Finder Implementation

* IDP Finder Implementation Class

  The class that finds the preferred IdP to handle a proxied authentication request.

* IDP Finder JSP

  The JSP that presents the list of IdPs to the user.

* Enable Proxy IDP Finder For All SPs

  Select this option to apply the finder for all remote SPs.

#### Relay State URL List

* Relay State URL List

  A list of URLs permitted for the `RelayState` parameter. For SLO operations, AM validates the redirection URL in the `RelayState` parameter against this list. If the `RelayState` parameter's value is in the list, AM allows redirection to the `RelayState` URL. If it isn't in the list, a browser error occurs.

  Use the pattern matching rules described in [Success and failure redirection URLs](../am-authentication/redirection-url-precedence.html) to specify URLs in the list.

  If you **don't** specify any URLs in this property, AM only allows redirection to `RelayState` URLs that match the domain of the instance. Any other URL causes a browser error.

  |   |                                                                                                                                     |
  | - | ----------------------------------------------------------------------------------------------------------------------------------- |
  |   | This property doesn't apply to IdP-initiated SSO, where the validation of the `RelayState` parameter should be performed on the SP. |

#### IDP Adapter

Learn more in [IdP adapter](custom-idp-adapter.html).

* IDP Adapter Class

  The Java class for a custom IdP Adapter.

  This class isn't invoked if a script is selected for `IDP Adapter Script`.

* IDP Adapter Script

  The script for a custom IdP Adapter.

  Select from a list of all the `Saml2 IDP Adapter` type scripts saved to this realm, including the default template script, `SAML2 IDP Adapter Script`.

  Learn more in [saml2-idp-adapter.js](../am-scripting/sample-scripts.html#saml2-idp-adapter-js).

#### Application Context

* Enable Application Context

  When enabled, this setting makes the application context available in all SAML 2.0 flows through the `samlApplication` binding in [Scripted Decision node scripts](../am-scripting/scripting-api-node.html#samlapp-binding).

  You can override this value by setting [`Application Context Enabled`](#saml-sp-app-context-enabled) in the remote SP configuration.

## Remote IdP configuration

After you've set up a remote IdP, configure it through the AM admin UI under Realms > *realm name* > Applications > Federation > Entity Providers > *remote IdP*.

### Assertion content

The following properties appear under the Assertion Content tab:

#### Signing and Encryption

* Request/Response Signing

  The requests and responses that the IdP requires the SP to sign digitally.

* Encryption

  * NameID Encryption – When selected, the SP must encrypt NameID elements.

* Algorithms

  Select the signing, encryption and digest algorithms that the SP will use.

#### NameID Format

* NameID Format List – The supported name identifiers for users who are shared between providers for single sign-on.

#### Secrets

* Secret Label Identifier – Identifier used to create a secret label for mapping to a secret in the secret store. AM uses this label to create a specific secret label for this entity provider. The secret label takes the form `am.applications.federation.entity.providers.saml2.identifier.basicauth` where identifier is the value of Secret Label Identifier. The label can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If you change the Secret Label Identifier for a specific entity provider, any corresponding mappings are deleted, unless they're referenced by other entity providers.

#### Basic Authentication

* Enabled – Authenticate with the specified username and password when making requests to this entity provider's SOAP endpoints.

* User Name – The username with which to authenticate at SOAP endpoints.

* Password – The password with which to authenticate at SOAP endpoints.

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you set a value for Secret Label Identifier, and AM finds a mapping to this secret label in the secret store, the value of this Password field is ignored. For example, if you set the Secret Label Identifier to demo and AM finds a secret mapping to `am.applications.federation.entity.providers.saml2.demo.basicauth`, AM uses this secret and ignores the value of the Password field. For basic authentication, there is no *default* secret label for the realm, or globally. |

#### Client Authentication

These settings let an SP authenticate to the IdP using mutual TLS (mTLS).

When you enable client authentication for any request type in this section, you must configure a [secret mapping](../security/secret-mapping.html) from one of the following secret labels to a valid certificate in the secret store:

* `am.default.applications.federation.entity.providers.saml2.sp.mtls` – the global or realm-specific mapping for hosted SPs

* `am.applications.federation.entity.providers.saml2.identifier.mtls` – a mapping for a specific SP, where identifier is the value of the Secret Label Identifier you set in the Secrets panel in the SP configuration.

If you configure a global mapping, a realm-specific mapping, and a mapping for a specific SP, the order of precedence is as follows:

* Hosted SP-specific mapping

* Realm-level default

* Global default

The certificates mapped to these labels are included in the SP metadata export with `<KeyDescriptor use="signing">`.

Currently, you can enable mTLS for the following request:

* Artifact Resolve – For artifact resolution requests, the IdP instructs the SP to send a client certificate along with the request.

### Services

The following properties appear under the Services tab:

#### IDP Service Attributes

* Artifact Resolution Service

  The endpoint to manage artifact resolution. The Index is a unique identifier for the endpoint.

* Single Logout Service

  The endpoints to manage single logout, depending on the selected SAML binding.

* Manage NameID Service

  The endpoints to manage name identifiers, depending on the selected SAML binding.

* Single SignOn Service

  The endpoints to manage single sign-on.

  These endpoints are used only for SP-initiated flows but are included as a requirement of the [SAML 2.0 Metadata specification](http://docs.oasis-open.org/security/saml/v2.0/saml-metadata-2.0-os.pdf).

#### NameID Mapping

* Location

  The endpoint to manage name identifier mapping.

## Hosted SP configuration

After you've set up a hosted SP, you can configure it through the AM admin UI under Realms > *realm name* > Applications > Federation > Entity Providers > *hosted SP*.

### Assertion content

The following properties appear under the Assertion Content tab:

#### Signing and Encryption

* Request/Response Signing

  The parts of messages the SP requires the IdP to sign digitally.

* Encryption

  The IdP must encrypt selected elements.

* Secret Label and Algorithms

  * Secret Label Identifier

    An identifier for the secret label AM uses for this entity provider, when resolving secrets.

    For example, if you set this value to `demo`, the entity provider uses the following secret labels:

    * `am.applications.federation.entity.providers.saml2.demo.signing`

    * `am.applications.federation.entity.providers.saml2.demo.encryption`

    If not specified, AM uses the entity provider role-specific, default global secret labels. Learn more in [Secret label mappings for SAML 2.0 signing and encryption](../security/secret-mapping.html#secrets-saml2-signing-encryption).

  * Signing Algorithm

    The algorithms the provider can use to sign the request/response attributes selected in the Request/Response Signing group.

    These algorithms are exposed in the provider's metadata extension.

    This property has no default.

  * Digest Algorithm

    The digest algorithms the provider can use when signing the requests and responses selected in the Request/Response Signing group.

    These algorithms are exposed in the provider's metadata extension.

    This property has no default.

  * Encryption Algorithm

    The two types of encryption algorithms for the provider:

    * Symmetric algorithms, which the provider can use to encrypt the objects selected in the Encryption group. Select one or more AES algorithms from the drop-down list.

      Default: `http://www.w3.org/2001/04/xmlenc#aes128-cbc`

    * Asymmetric algorithms, advertised as the provider's transport key algorithm. When SAML 2.0 token encryption is enabled, hosted providers should use the algorithm the remote provider is advertising when encrypting symmetric encryption keys.

      Select one or more algorithms from the drop-down list:

      > **Collapse: Key transport algorithms**
      >
      > * <http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p> (default).
      >
      > * [http://www.w3.org/2009/xmlenc11#rsa-oaep](https://www.w3.org/TR/xmlenc-core1/#sec-RSA-OAEP).
      >
      >   When this algorithm is configured, AM will use the Mask Generation Function Algorithm property (Configure > Global Services > Common Federation Configuration) to create the transport key.
      >
      >   Learn about the supported mask generation function algorithms in [Algorithms](../setup/services-configuration.html#global-federation-common-algorithms).
      >
      > * <http://www.w3.org/2001/04/xmlenc#rsa-1_5>.
      >
      >   For security reasons, you should *not* use this option.

#### NameID Format

* NameID Format List

  The supported name identifiers for users that are shared between providers for single sign-on.

  The following diagram shows how the hosted SP decides which of the supported NameID formats is used:

  ![Diagram showing how the hosted SP decides which supported NameID format is used.](_images/nameid-format-flow-hosted-sp.svg)

* Disable NameID Persistence

  Disables the storage of ``NameID`s in the user datastore, even if the `NameID`` format is `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent` in the received assertion, and the account mapper has identified the local user.

  You might want to disable storage of NameID values if you're using a read-only datastore, or an external identity store that does not have the AM identity schemas applied.

  |   |                                                                                                                                                                            |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | When local authentication is utilized for account linking purposes, disabling federation persistence requires end users to authenticate locally for each SAML-based login. |

  Default value: `false`

#### Authentication Context

* Mapper

  A class that implements the `SPAuthnContextMapper` interface and maps the incoming request parameters to an authentication context.

  Default: `com.sun.identity.saml2.plugins.DefaultSPAuthnContextMapper`

* Authentication Context

  The authentication context maps the URI references to IdP's supported authentication context classes to authentication levels set on the SP side.

  * Context Reference

    Select from the following options to define a context reference:

    * Predefined Reference to choose from a list of supported context references.

    * Custom Reference to type your own reference to an authentication context.

  * Level

    The order of precedence of the supported context reference classes as a numeric value.

    Classes with higher numbers are considered stronger than lower numbered classes. The values determine which authentication classes can be used when the SP makes an authentication request that uses a comparison attribute; for example, `minimum` or `better`.

    > **Collapse: Example**
    >
    > ![Context reference mappings](_images/auth-context-mappings-sp.png)

    Learn about authentication context classes in [Authentication Context for the OASIS Security Assertion Markup Language (SAML) 2.0](http://docs.oasis-open.org/security/saml/v2.0/saml-authn-context-2.0-os.pdf) in the *SAML 2.0 Standard*.

    Default value: `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`

* Comparison Type

  Used in conjunction with the default authentication context to specify the possible range of authentication mechanisms the IdP can choose from.

  For example, if the Comparison Type field is set to `better`, and the `PasswordProtectedTransport` authentication context class is selected in the Default Authentication Context field, the IdP must select an authentication mechanism with a higher level assigned.

  Default: `exact`

* Include Request Authentication Context

  Whether to include an authentication context class as the Requested Authentication Context in the SAML 2.0 Authentication Request.

  Default: Enabled

* Assertion Time Skew

  Grace period in seconds for the `NotBefore` time in assertions.

#### Basic Authentication

* Enabled, User Name, Password

  When enabled, authenticate with the specified user name and password at SOAP endpoints.

#### Client Authentication

* Exclude Client Certificate from Metadata

  When enabled, don't export the client certificate in the SP metadata.

### Assertion processing

The following properties appear under the Assertion Processing tab:

#### Attribute Mapper

* Attribute Mapper

  A class that implements the attribute mapping.

* Attribute Map

  Maps SAML attributes to session properties, or user profile attributes.

  The value of Key is a SAML attribute sent in an assertion, and the value of Value is a property in the authenticated session, or an attribute of the user's profile.

  By default, the SP maps the SAML attributes it receives to equivalent-named session properties. However, when the SP is configured to create identities during autofederation and the identity does not exist yet, the SP maps the SAML attributes to their equivalents in the newly-created user profile.

  The special mapping `Key: *, Value: *` means that the SP maps each attribute it receives in the assertion to equivalent-named properties or attributes. For example, if the SP receives `mail` and `firstname` in the assertion, it maps them to `mail` and `firstname` respectively.

  Remove the special mapping and add key pairs to the map if:

  * (During autofederation) The attributes in the IdP's and the SP's identity stores do not match.

  * You need control over the names of the session properties.

  * You need control over which attributes the SP should map, because the IdP adds too many to the assertion.

  For example, if the SAML attribute is `firstname` and you want the SP to map it to a session property/user profile attribute called `cn`, create a mapping similar to `Key: firstname, Value: cn`.

#### Auto Federation

* Enabled

  When enabled, automatically federate user's accounts at different providers based on the specified SAML attribute.

* Attribute

  The SAML attribute to match accounts at different providers.

#### Account Mapper

* Account Mapper

  A class that implements `AccountMapper` to map remote users to local user profiles.

* Use Name ID as User ID

  When selected, fall back to using the name identifier from the assertion to find the user.

* Transient User

  The user profile to map all IdP users when sending transient name identifiers.

#### Artifact Message Encoding

* Artifact Message Encoding

  The message encoding format for artifacts.

#### URL

* Local Authentication URL

  Use this property to specify an alternative URL to redirect the user to after validating the SAML2 assertion from the IdP. For example, if you have created a custom user interface other than the AM UI.

  When in integrated mode, the query parameters are appended to the configured URL. Typically, these parameters contain all the information necessary for AM to continue the authentication journey.

  When in standalone mode, AM redirects users to the specified URL, and appends a `goto` parameter. This parameter contains the URL the user must be redirected to next.

  To make sure a valid tree is configured, use [Redirect Tree](#config-redirect-tree) instead. However, if configured, the value for `Local Authentication URL` overrides `Redirect Tree Name`.

* Intermediate URL

  The URL to redirect the user to after authentication but before the original URL requested.

* External Application Logout URL

  The URL to send an HTTP POST to including all cookies when receiving a logout request. To add a user session property as a POST parameter, include it in the URL query string as a `appsessionproperty` parameter.

#### Redirect Tree

* Redirect Tree Name

  If specified, AM redirects to this tree after validating the SAML2 assertion from the IdP.

  For IdP-initiated SSO, you must set either `Redirect Tree Name` or `Local Authentication URL`, otherwise the SP fails to process the assertion and returns an invalid request error.

  If you provide a value for both settings, AM prioritizes `Local Authentication URL`.

  You can't delete a tree if it's set as the value for `Redirect Tree Name`.

  Find information about setting a redirect tree in [Redirect to a tree on the hosted SP](configure-providers.html#config-redirect-tree).

* Default Relay State URL

  The URL to redirect users to after the request has been handled. Used if not specified in the response.

#### Adapter

* Adapter

  A class that implements the `FederationSPAdapter` interface and performs application-specific processing during the federation process.

* Adapter Environment

  Environment variables passed to the adapter class.

### Services

The following properties appear under the Services tab:

* MetaAlias

  Used to locate the hosted provider's entity identifier, specified as `[/realm-name]*/provider-name`, where *provider-name* can't contain slash characters (`/`). For example: `/myRealm/mySubrealm/sp`.

  The MetaAlias must be unique for each provider configured in a CoT and in the realm.

#### SP Service Attributes

* Single Logout Service

  The endpoints to manage single logout, depending on the SAML binding selected.

* Manage NameID Service

  The endpoints to manage name identifiers, depending on the SAML binding selected.

- Assertion Consumer Service

  The endpoints to consume assertions, with Index corresponding to the index of the URL in the standard metadata.

  The scheme, FQDN, and port configured must exactly match those of the SP as they appear in its metadata.

  To determine the SP's endpoint URL, AM uses the Base URL service, if configured.

  If the URL doesn't match, the SAML 2.0 flow will fail and AM logs `Invalid Assertion Consumer Location specified` in the audit log file.

  Set the HTTP-Artifact and HTTP-POST service locations to `AuthConsumer` for [integrated mode](saml2-integrated-mode.html).

### Advanced settings

The following properties appear under the Advanced tab:

#### SAE Configuration

* SP URL

  The endpoint to manage Secure Attribute Exchange requests.

* SP Logout URL

  The endpoint of the SP that can handle global logout requests.

* Application Security Configuration

  How to handle encryption for Secure Attribute Exchange operations.

#### ECP Configuration

* Request IDP List Finder Implementation

  A class that returns a list of preferred IdPs trusted by the SAML Enhanced Client or Proxy profile.

* Request IDP List Get Complete

  A URI reference used to retrieve the complete IdP list if the `IDPList` element is not complete.

* Request IDP List

  A list of IdPs for the SAML Enhanced Client or Proxy to contact, used by the default implementation of the IDP Finder.

#### IDP Proxy

* IDP Proxy

  When enabled, AM includes a `Scoping` element in the authentication request to enable the request to be proxied.

* Introduction

  When enabled, use introductions to find the proxy IdP.

* Proxy Count

  The maximum number of proxy IdPs.

* IDP Proxy List

  A list of URIs identifying preferred proxy IdPs.

#### Session Synchronization

* Enabled

  When enabled, the SP sends a SOAP logout request over the back channel to all IdPs when an authenticated session times out. An authenticated session can time out when the maximum idle time or maximum session time is reached, for example.

#### Relay State URL List

* Relay State URL List

  List of URLs permitted for the `RelayState` parameter. AM validates the redirection URL in the `RelayState` parameter against this list. If the `RelayState` parameter's value is in the list, AM allows redirection to the `RelayState` URL. If it is not in the list, a browser error occurs.

  Use the pattern matching rules described in [Success and failure redirection URLs](../am-authentication/redirection-url-precedence.html) to specify URLs in the list.

  If you **DO NOT** specify any URLs in this property, AM only allows redirection to `RelayState` URLs that match the domain of the instance. Any other URL will cause a browser error.

## Remote SP configuration

After you've set up a remote SP, configure it through the AM admin UI under Realms > *realm name* > Applications > Federation > Entity Providers > *remote SP*.

### Assertion content

The following properties appear under the Assertion Content tab:

#### Signing and Encryption

* Request/Response Signing

  The requests and responses that the SP requires the IdP to sign digitally.

* Encryption

  The elements that the SP requires the IDP to encrypt.

  * Attribute Encryption – When selected, the IDP must encrypt SAML attributes.

  * Assertion Encryption – When selected, the IDP must encrypt SAML assertions.

  * NameID Encryption – When selected, IDP must encrypt NameID elements.

* Algorithms

  * Signing Algorithm – The signing algorithm the SP will use.

  * Digest Algorithm – The digest algorithm the SP will use.

  * Encryption Algorithm – The encryption algorithm the SP will use.

#### NameID Format

* NameID Format List – The supported name identifiers for users who are shared between providers for single sign-on.

* NameID Value Map – Map the NameID format to a user profile attribute, for example:

  `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress=mail` or `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent=objectGUID;binary`.

  * `Key` – The Name ID format to map, for example: `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`

  * `Value` – The profile attribute, for example: `mail`.

  * `Binary` – Indicates that the profile attribute is binary and should be Base64-encoded when used as the NameID value.

  If the specified NameID format is used in the protocol, the corresponding profile attribute value is used as the NameID in the Subject assertion element. This mapping overrides *all* the values defined in the NameID Value Map on the hosted IdP. For example, if a NameID Value Map is defined for the SP and a request is made with a specific NameID Format that only exists on the IdP, it will fail.

* Disable NameID Persistence Disables the storage of NameID values at the IDP when generating an assertion for this remote SP.

  Default value: `false`

#### Secrets

* Secret Label Identifier – Identifier used to create a secret label for mapping to a secret in the secret store.

  AM uses this label to create a specific secret label for this entity provider. The secret label takes the form `am.applications.federation.entity.providers.saml2.identifier.basicauth` where identifier is the value of Secret Label Identifier. The label can only contain characters `a-z`, `A-Z`, `0-9`, and periods (`.`). It can't start or end with a period.

  If you change the Secret Label Identifier for a specific entity provider, any corresponding mappings are deleted, unless they're referenced by other entity providers.

  |   |                                                                                                                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you specify a value for Secret Label Identifier, and AM finds a mapping to this secret label in the secret store, the value of the Password field is ignored. For basic authentication, there is no *default* secret label for the realm, or globally. |

#### Basic Authentication

* Enabled – Require authentication with the specified username and password at SOAP endpoints.

* User Name – The username used to authenticate at SOAP endpoints.

* Password – The password used to authenticate at SOAP endpoints.

  |   |                                                                                                                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | If you specify a value for Secret Label Identifier, and AM finds a mapping to this secret label in the secret store, the value of the Password field is ignored. For basic authentication, there is no *default* secret label for the realm, or globally. |

### Assertion processing

The following properties appear under the Assertion Processing tab:

#### Attribute Mapper

* Attribute Map

  Override any mappings of attributes to user profile attributes at the IdP.

#### Artifact Message Encoding

* Artifact Message Encoding

  The message encoding format for artifacts.

### Services

The following properties appear under the Services tab:

#### SP Service Attributes

* Single Logout Service

  The endpoints to manage single logout, depending on the selected SAML binding.

* Manage NameID Service

  The endpoints to manage name identifiers, depending on the selected SAML binding.

* Assertion Consumer Service

  The endpoints to consume assertions. Index corresponds to the index of the URL in the standard metadata.

### Advanced settings

The following properties appear under the Advanced tab:

* Skip Endpoint Validation For Signed Requests

  When enabled, AM doesn't verify Assertion Consumer Service URL values in SAML authentication requests. For example, this lets the Assertion Consumer Service URL contain dynamic query parameters.

  Because assertion consumer service URL verification is part of the SAML 2.0 specification, you can only skip validation if the authentication request is digitally signed by the SP. To digitally sign authentication requests, in the remote SP configuration go to Assertion Content > Signing and Encryption > Request/Response Signing, and select Authentication Requests Signed.

  |   |                                                                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | You must configure the remote SP to sign the authentication request.AM returns an error if it receives an unsigned authentication request and this option is enabled. |

#### SAE Configuration

* SP URL

  The endpoint to manage Secure Attribute Exchange requests.

* SP Logout URL

  The endpoint of the SP that can handle global logout requests.

#### IDP Proxy

* IDP Proxy enabled

  When enabled, the authentication requests from this SP can be proxied.

* Proxy all requests

  When enabled, AM proxies every authentication request from the SP, whether it contains a `Scoping` element or not.

  IDP Proxy enabled must be set to `true` for this option to take effect.

* Introduction enabled

  When enabled, use introduction cookies to find the proxy IdP.

  |   |                                                                                                                               |
  | - | ----------------------------------------------------------------------------------------------------------------------------- |
  |   | This property only works with a non-default *SAML2IDPProxyFRImpl* implementation, and will be deprecated in a future release. |

* Use IDP Finder

  When enabled, use the IDP finder service to determine the IDP to which authentication requests are proxed.

* Proxy Count

  The maximum number of proxy IdPs. AM sets the specified value in the `Scoping` element of the authentication request it proxies for this SP.

  You must enable Proxy all requests for this option to take effect.

* IDP Proxy List

  A list of URIs identifying preferred proxy IdPs.

#### Tree Name

* Tree Name

  If configured, AM redirects the remote SP to the specified tree, ignoring the configured authentication contexts and existing sessions. The redirect contains a transaction condition advice to ensure the tree is run.

  You can access the requested authentication context and mappings by including a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) in the tree that queries the [samlApplication](../am-scripting/scripting-api-node.html#samlapp-binding) script binding.

  |   |                                                                                                                                                                                                                                                                                                                 |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To prevent users from authenticating directly through this tree, either for security reasons or because the tree is insufficient as a complete authentication service, configure it as a [transactional authentication tree](../am-authentication/configure-auth-trees.html#configure-transactional-auth-tree). |

#### Application Context

* Application Context Enabled

  This setting controls the availability of the application context in SAML 2.0 flows through the `samlApplication` binding in [Scripted Decision node scripts](../am-scripting/scripting-api-node.html#samlapp-binding).

  Choose from the following options:

  * Default: Inherits the value from [`Enable Application Context`](#saml-idp-enable-app-context) in the hosted IdP configuration.

  * Enabled: The application context is always available.

  * Disabled: The application context is never available.

## CoT configuration

Once you have set up a CoT, you can configure it through the AM admin UI under Realms > *realm name* > Applications > Federation > Circle of Trust > *circle of trust name*.

* Name

  String that refers to the circle of trust.

  Once you have set up a circle of trust, the name cannot be configured.

* Description

  Short description of the circle of trust.

* Status

  Whether this circle of trust is operational.

* Entity Providers

  Known hosted and remote identity and service providers participating in this circle of trust.

* SAML2 Writer Service URL

  SAML 2.0 service that writes identity provider entity identifiers to Common Domain cookies after successful authentication, used in identity provider discovery. Example: `https://discovery.example.com:8443/openam/saml2writer`.

* SAML2 Reader Service URL

  SAML 2.0 service that reads identity provider entity identifiers from Common Domain cookies, used in identity provider discovery. Example: `https://discovery.example.com:8443/openam/saml2reader`.

## SAML 2.0 advanced properties

To configure SAML 2.0 advanced properties, in the AM admin UI, go to Configure > Server Defaults > Advanced.

* `openam.saml.decryption.debug.mode`

  When enabled, AM decrypts SAML 2.0 messages that are sent and received, and writes the content to the debug logs.

  Don't enable this property in production environments as these messages may contain user information.

  Default: `False`

* `org.forgerock.openam.saml2.authenticatorlookup.skewAllowance`

  The allowable time difference, in seconds, between any existing session the user may have, and the current time when an authentication request specifies `ForceAuthn`.

  If the authenticated user's session was created outside of the allowable time range, AM rejects the assertion, and re-authentication is required.

  Default: `60`

* `org.forgerock.openam.saml2.tls.handler.cache.size`

  The size of the cache that holds HTTP Client handlers to facilitate mTLS authentication for artifact resolution.

  The default should suffice for most deployments. Increase the cache size if you have a large number of remote IDPs that each use a separate secret alias.

  The entire cache is invalidated when a secret store changes in a realm.

  Default: `50`

---

---
title: SAML 2.0
description: Explore SAML 2.0 concepts, configuration, and usage procedures for PingAM identity providers and service providers, including single sign-on, account linking, and the Fedlet
component: pingam
version: 8.1
page_id: pingam:am-saml2:preface
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/preface.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["index.adoc", "saml2-guide:preface.adoc"]
---

# SAML 2.0

These topics cover concepts, configuration, and usage procedures for working with the Security Assertion Markup Language (SAML) 2.0 features provided by PingAM.

They are intended for anyone using PingAM for SAML 2.0 identity and SPs, or using the Fedlet as a SAML 2.0 SP.

[icon: book, set=fad, size=3x]

#### [About SAML 2.0](saml2-introduction.html)

Learn how AM servers support SAML 2.0.

[icon: handshake, set=fad, size=3x]

#### [Configure SAML 2.0](saml2-configuration.html)

Configure AM's SAML 2.0 support by using the AM admin UI.

[icon: users, set=fad, size=3x]

#### [Configure single sign-on](saml2-sso-slo.html)

Enable SAML 2.0 single sign-on (SSO) and single logout (SLO).

[icon: user-plus, set=fad, size=3x]

#### [Federate identities](saml2-linking-accounts.html)

Learn how to link identities, either permanently or temporarily.

[icon: puzzle-piece, set=fad, size=3x]

#### [SAML 2.0 in Java apps](saml2-implementation-fedlet.html)

Learn how to use the AM *Fedlet*.

[icon: link, set=fad, size=3x]

#### [SAML 2.0 Secure Attribute Exchange](saml2-sae.html)

Deploy AM as a SAML 2.0 gateway to a legacy IdP.

---

---
title: Set up IdPs and SPs in a CoT
description: Configure hosted and remote SAML 2.0 identity providers and service providers in a circle of trust
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-providers-and-cots
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-providers-and-cots.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:saml2-providers-and-cots.adoc"]
section_ids:
  create-hosted-providers: Create a hosted IdP or SP
  saml-export-metadata: Export metadata
  configure-remote-entity: Import a remote IdP or SP
  update-metadata: Update remote SP certificate
  create-cot: Create a circle of trust (CoT)
---

# Set up IdPs and SPs in a CoT

To implement SAML 2.0 in AM, you share metadata for your hosted providers with other remote providers in a circle of trust (CoT).

You must also configure remote providers by importing their metadata.

In AM, a *hosted* provider is one served by the current AM instance; a *remote* provider is one hosted elsewhere.

## Create a hosted IdP or SP

A hosted IdP or SP is a provider hosted by AM. For example, if AM is the authoritative source for users to a downstream application, then you would configure AM to be a hosted IdP.

To create other roles, use the `/realm-config/federation/entityproviders/saml2` REST endpoint. Learn more about this endpoint in the [Online REST API reference](../am-rest/about-api-explorer.html).

Use the AM admin UI to create a hosted IdP or SP.

1. Go to Realms > *realm name* > Dashboard, and click SAML Applications.

2. Click Add Entity Provider, and select Hosted.

3. Enter an Entity ID, and verify the Entity Provider Base URL value is correct.

   |   |                                                                                                                                                                                                                                                                                                                                           |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | AM truncates sequences of whitespace with a single whitespace character in values such as entity IDs. For example, if `MyEntityID value` (with one space) exists already, and you add a new entity, `My Entity ID value` (same name but multiple spaces), then AM will throw an error because the string values are treated as identical. |

   AM uses the Entity Provider Base URL value for all SAML 2.0 related endpoints, so ensure other entities in your SAML deployment are able to access the specified URL.

4. In the Meta Aliases section, provide a URL-friendly value in either the Identity Provider Meta Alias, the Service Provider Meta Alias property, or both.

   Ensure the aliases for providers are unique in a circle of trust and in the realm.

5. Click Create.

   > **Collapse: How do I switch between SP and IdP configuration for a given provider?**
   >
   > AM only displays the configuration of a single role. Click on the labels to select the role view:
   >
   > ![saml-roles](_images/saml-roles.png)

6. On the Assertion Processing tab, in the Attribute Mapper section, map SAML attribute names (Name in Assertion) to local attribute names.

   ![In this example, we map the SalesForce IDPEmail SAML attribute to the local mail attribute.](_images/ui-attribute-mapper-example.png)Figure 1. Example: Map SAML attributes to local attributes

   The default mapping implementation has additional features beyond simply retrieving string attributes from the user profile.

   * Add an attribute that takes a static value by enclosing the profile attribute name in double quotes (`"`).

     For example, you can add a static SAML attribute called `partnerID` with a value of `staticPartnerIDValue` by adding `partnerID` as the SAML Attribute with `"staticPartnerIDValue"` as the Local Attribute Name.

   * Select the binary option when dealing with binary attribute values; for example, values that are Base64-encoded.

   * Use the optional `Name Format Uri` property as required by the remote provider. For example, you may need to specify `urn:oasis:names:tc:SAML:2.0:attrname-format:uri`.

7. Configure other properties to customize your SAML 2.0 application as required, for example:

   * [Sign and encrypt messages](saml2-encryption.html)

   * [Extend SAML 2.0 functionality with scripts](customize-saml2-plugins.html)

   |   |                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn about configuring a hosted provider in:* [Hosted IdP configuration](saml2-reference.html#saml2-hosted-idp-configuration)

   * [Hosted SP configuration](saml2-reference.html#saml2-hosted-sp-configuration) |

8. Save your changes.

9. You can now [export the metadata](#saml-export-metadata) from your hosted provider.

## Export metadata

Export the XML-based metadata from your entity provider to share with other providers in your CoT.

There are two ways you can export a provider's metadata:

* Over REST

  Run the following command, including an output filename, the entity ID, and realm:

  ```bash
  $ curl \
  --output metadata.xml \
  "https://am.example.com:8443/am/ExportSamlMetadata?\
  entityid=myProvider&realm=/alpha"
  ```

  If you have configured your provider in the Top Level Realm, omit the `realm` query parameter.

* In a browser

  Export the XML-based metadata from a hosted or a remote provider if they can access the metadata URL. Open a URL in the following format in a browser:

  `https://am.example.com:8443/am/ExportSamlMetadata?entityid=myProvider&realm=/alpha`

## Import a remote IdP or SP

The following procedure provides steps for importing and configuring one or more remote entity providers:

1. Get the entity provider metadata as an XML-formatted file.

   If the remote entity provider can't export the metadata as an XML file, use one of the following metadata files to create your remote entity provider. Make sure you update the `entityID`, add the X.509 certificates, and update the services before importing.

   > **Collapse: Remote IdP metadata file**
   >
   > ```xml
   > <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
   > <EntityDescriptor entityID="myProvider"
   > 	xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
   > 	xmlns:query="urn:oasis:names:tc:SAML:metadata:ext:query"
   > 	xmlns:mdattr="urn:oasis:names:tc:SAML:metadata:attribute"
   > 	xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
   > 	xmlns:xenc="http://www.w3.org/2001/04/xmlenc#"
   > 	xmlns:xenc11="http://www.w3.org/2009/xmlenc11#"
   > 	xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport"
   > 	xmlns:x509qry="urn:oasis:names:tc:SAML:metadata:X509:query"
   > 	xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
   > 	<IDPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
   > 		<KeyDescriptor use="signing">
   > 			<ds:KeyInfo>
   > 				<ds:X509Data>
   > 					<ds:X509Certificate> paste X.509 certificate here </ds:X509Certificate>
   > 				</ds:X509Data>
   > 			</ds:KeyInfo>
   > 		</KeyDescriptor>
   > 		<KeyDescriptor use="encryption">
   > 			<ds:KeyInfo>
   > 				<ds:X509Data>
   > 					<ds:X509Certificate> paste X.509 certificate here </ds:X509Certificate>
   > 				</ds:X509Data>
   > 			</ds:KeyInfo>
   > 		</KeyDescriptor>
   > <!--
   > 	Delete any lines below that correspond to unwanted services or NameID formats.
   > 	For services you want to keep, update the location to the correct endpoint.
   > -->
   > 		<ArtifactResolutionService index="0" Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="endpoint"/>
   > 		<SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="endpoint"/>
   > 		<SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="endpoint"/>
   > 		<SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="endpoint"/>
   > 		<ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="endpoint"/>
   > 		<ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="endpoint"/>
   > 		<ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="endpoint"/>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName</NameIDFormat>
   > 		<SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="endpoint"/>
   > 		<SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="endpoint"/>
   > 		<SingleSignOnService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="endpoint"/>
   > 	</IDPSSODescriptor>
   > </EntityDescriptor>
   > ```

   > **Collapse: Remote SP metadata file**
   >
   > ```xml
   > <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
   > <EntityDescriptor entityID="myProvider"
   > 	xmlns="urn:oasis:names:tc:SAML:2.0:metadata"
   > 	xmlns:query="urn:oasis:names:tc:SAML:metadata:ext:query"
   > 	xmlns:mdattr="urn:oasis:names:tc:SAML:metadata:attribute"
   > 	xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion"
   > 	xmlns:xenc="http://www.w3.org/2001/04/xmlenc#"
   > 	xmlns:xenc11="http://www.w3.org/2009/xmlenc11#"
   > 	xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport"
   > 	xmlns:x509qry="urn:oasis:names:tc:SAML:metadata:X509:query"
   > 	xmlns:ds="http://www.w3.org/2000/09/xmldsig#">
   > 	<SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
   > 		<KeyDescriptor use="signing">
   > 			<ds:KeyInfo>
   > 				<ds:X509Data>
   > 					<ds:X509Certificate> paste X.509 certificate here </ds:X509Certificate>
   > 				</ds:X509Data>
   > 			</ds:KeyInfo>
   > 		</KeyDescriptor>
   > 		<KeyDescriptor use="encryption">
   > 			<ds:KeyInfo>
   > 				<ds:X509Data>
   > 					<ds:X509Certificate> paste X.509 certificate here </ds:X509Certificate>
   > 				</ds:X509Data>
   > 			</ds:KeyInfo>
   > 		</KeyDescriptor>
   > <!--
   > 	Delete any lines below that correspond to unwanted services or NameID formats.
   > 	For services you want to keep, update the location to the correct endpoint.
   > -->
   > 		<SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="endpoint"/>
   > 		<SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="endpoint"/>
   > 		<SingleLogoutService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="endpoint"/>
   > 		<ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect" Location="endpoint"/>
   > 		<ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="endpoint"/>
   > 		<ManageNameIDService Binding="urn:oasis:names:tc:SAML:2.0:bindings:SOAP" Location="endpoint"/>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:persistent</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos</NameIDFormat>
   > 		<NameIDFormat>urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName</NameIDFormat>
   > 		<AssertionConsumerService index="0" isDefault="true" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact" Location="endpoint"/>
   > 		<AssertionConsumerService index="1" isDefault="false" Binding="urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST" Location="endpoint"/>
   > 		<AssertionConsumerService index="2" isDefault="false" Binding="urn:oasis:names:tc:SAML:2.0:bindings:PAOS" Location="endpoint"/>
   > 	</SPSSODescriptor>
   > </EntityDescriptor>
   > ```

2. Go to Realms > *realm name* > Dashboard, and click SAML Applications.

3. From the Add Entity Provider drop-down menu, select Remote.

4. On the New Remote Entity Provider page, perform one of the following steps to import the XML file:

   1. Drag and drop the XML file into the dotted box.

   2. Click within the dotted box to open a file browser to select the XML file.

   |   |                                                                                                                                                                                                                                                                                                                                                                                                                  |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can import multiple remote entities in a single operation, as long as the entity ID is unique within each.AM truncates sequences of whitespace with a single whitespace character in values such as Entity IDs. For example, if `ID value` (with one space) exists already, a new entity with the same name but multiple spaces would result in an error because the string values are treated as identical. |

5. If you have already [created a circle of trust](#create-cot), you can add the remote providers into one or more of them by using the Circles of Trust property.

6. Leave the Update Type as empty or set to `CREATE`.

7. Click Create.

8. To edit the configuration of an entity provider, go to Realms > *realm name* > Applications > Federation > Entity Providers, and select the entity provider to edit.

   > **Collapse: How do I switch between SP and IdP configuration for a given provider?**
   >
   > AM only displays the configuration of a single role. Click on the labels to select the role view:
   >
   > ![saml-roles](_images/saml-roles.png)

   Customize your SAML 2.0 application as required, for example:

   * [Sign and encrypt messages](saml2-encryption.html)

   * [Customize the NameID attribute in the assertion](custom-nameid-mapper.html)

   * [Configure a SAML 2.0 application tree](configure-providers.html#samlapp-tree)

   |   |                                                                                                                                                                                                                 |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn about remote provider configuration in:* [Remote IdP configuration](saml2-reference.html#saml2-remote-idp-configuration)

   * [Remote SP configuration](saml2-reference.html#saml2-remote-sp-configuration) |

### Update remote SP certificate

To update all the metadata for a remote IdP or SP, you can [import the metadata](#configure-remote-entity) again. Reimporting the metadata deletes and recreates the entity provider, overwriting all existing provider settings with the values in the metadata XML file.

However, if you only want to update the signing and encryption certificate used by the SP to sign the authentication request without losing existing settings, follow these steps:

1. Get the SAML 2.0 SP metadata with the updated signed certificate.

   You can find information about exporting provider metadata XML in [Export metadata](#saml-export-metadata).

2. Update the certificate in one of the following ways:

   * In the AM admin UI

     1. [Import the metadata](#configure-remote-entity).

        On the New Remote Entity Provider page, make sure you choose `UPDATE_CERTIFICATES` as the Update Type.

     2. Click Create.

   * Over REST

     Run the following REST API command, specifying:

     * sso-token: The SSO token of an administrative user

     * base64url-encoded metadata: The SP metadata XML encoded to ***base64url*** format

     ```bash
     $ curl \
     --request POST \
     --header 'accept-api-version: resource=1.0' \
     --header 'content-type: application/json' \
     --header 'iPlanetDirectoryPro: sso-token' \
     --data-raw '{
         "standardMetadata": "base64url-encoded metadata",
         "updateType": "UPDATE_CERTIFICATES"
     }' \
     'https://am.example.com:8443/am/json/realms/root/realm-config/saml2/remote?_action=importEntity'
     {
       "importedEntities":["myProvider"]
     }
     ```

## Create a circle of trust (CoT)

A CoT is an AM concept that groups at least one IdP and at least one SP who agree to share authentication information.

1. Go to Realms > *realm name* > Applications > Federation > Circles of Trust, and click Add Circle of Trust.

2. Provide a name, and click Create.

3. On the Circle of Trust page, in the Entity Providers property, select at least one IdP and one SP.

   You can add entity providers later if you haven't created them yet.

4. Customize any other properties as required and save your changes.

   Learn about configuring a CoT in [CoT configuration](saml2-reference.html#saml2-cot-configuration).

---

---
title: Sign and encrypt messages
description: Configure PingAM to sign and encrypt SAML 2.0 messages using recommended algorithms like RSA-SHA256 and AES encryption for secure federation
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-encryption
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-encryption.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "SHA-256", "RSA", "Encryption", "Algorithms", "Certificates"]
page_aliases: ["saml2-guide:saml2-encryption.adoc"]
section_ids:
  saml-signing: How signing works
  saml-encryption: How encryption works
  saml-advertised-sign-encrypt-algs: Configure the advertised signing and encryption algorithms
  sign-metadata: Configure AM to sign SAML 2.0 metadata
  sign-assertion-content: Configure AM to sign and encrypt SAML 2.0 assertion content
  certificates-and-secrets: Certificates and secrets
---

# Sign and encrypt messages

By default, IdPs and SPs don't sign or encrypt SAML 2.0 messages. Although this is useful for test and demo environments, you should secure your production and production-like environments.

## How signing works

When AM needs to sign a SAML request or response for the consumption of a remote entity provider, it determines the signing algorithm, and optionally, the digest method, based on the following logic, as recommended by the [SAML 2.0 Metadata Profile for AlgorithmSupport Version 1.0](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-metadata-algsupport-v1.0-cs01.pdf) specification:

1. AM retrieves the remote entity provider's metadata, and examines the role-specific extensions for a configured digest method, or signing algorithm. These are extensions defined within the `IDPSSODescriptor` or `SPSSODescriptor` elements.

   > **Collapse: Example**
   >
   > The following example role-specific extensions define the digest method and signing algorithms applicable to the SP role only:
   >
   > ```xml
   > <SPSSODescriptor protocolSupportEnumeration="urn:oasis:names:tc:SAML:2.0:protocol">
   > 	<Extensions xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport">
   > 		<alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha512" />
   > 		<alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512" />
   > 	</Extensions>
   > 	<!-- Other SP specific information -->
   > </SPSSODescriptor>
   > ```

2. If there is no role-specific algorithm configured, AM checks for algorithms configured in the entity provider-level extensions. These are extensions defined within the `EntityDescriptor` element.

   > **Collapse: Example**
   >
   > The following example entity provider-level extensions define the digest method and signing algorithms applicable to the whole entity provider:
   >
   > ```xml
   > <EntityDescriptor entityID="myProvider"
   > 	xmlns="urn:oasis:names:tc:SAML:2.0:metadata">
   > 	<Extensions xmlns:alg="urn:oasis:names:tc:SAML:metadata:algsupport">
   > 		<alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha512" />
   > 		<alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha512" />
   > 	</Extensions>
   > 	<!-- Role specific information -->
   > </EntityDescriptor>
   > ```

3. If signing algorithms are specified at either role-specific level or entity provider-level, but AM can't find a suitable key, it doesn't sign the element, and displays an error.

   Possible reasons include:

   * Algorithm mismatch

     The signing algorithm can't be used with the private key configured in the relevant secret label.

   * Keysize mismatch

     The required key size and actual key size aren't equal.

4. If the entity provider doesn't specify supported signing and digest methods in the standard metadata, AM falls back to the global default algorithm settings.

   To change the global default algorithms AM uses for signing and encrypting different SAML 2.0 components, go to Configure > Global Services > Common Federation Configuration.

5. If the global default algorithms aren't configured, AM examines the configured signing key type, and uses `RSA-SHA256` for RSA keys, `DSA-SHA256` for DSA keys, and `ECDSA-SHA512` for EC keys.

   |   |                                                                                                                                                                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | AM has different default signing algorithm settings for XML signatures, and for query signatures.AM determines the correct default query signing algorithm based on the signing key's algorithm, be it RSA, DSA, or EC. It only falls back to the same defaults for both XML and query signing algorithms when the settings aren't correctly defined. |

After determining the required algorithm, the sender uses their own private key to write the signature on the request. Then, the provider receiving the message uses the public key exposed in the sender's metadata to validate the signature.

## How encryption works

When encrypting SAML 2.0 messages, the sender uses the receiver's public key (exposed in the receiver's metadata) to encrypt the request. The receiver decrypts it with its private key.

As with signing, providers also expose in their metadata the algorithms that they can use to encrypt assertion content.

Since SAML 2.0 messages are in XML format, encrypting them requires an additional key that is transported with the message, as explained in the [XML Encryption Syntax and Processing Version 1.1](https://www.w3.org/TR/xmlenc-core/) specification. AM refers to those keys as *transport keys*.

Consider the following example of an encryption/decryption flow:

1. The IdP generates a random symmetric transport key using the transport key algorithm exposed in the SP's metadata.

2. The IdP encrypts the assertion with the transport key.

3. The IdP encrypts the transport key with the public key of the SP (which is also exposed in its metadata).

4. The SP decrypts the transport key using its private key. Then, it uses the transport key to decrypt the assertion.

This ensures only this SP can decrypt the message.

## Configure the advertised signing and encryption algorithms

1. Configure the required signing algorithms and digests:

   Hosted IdPs and SPs can advertise the algorithms they can use to sign assertion content. This information appears as part of the provider's metadata extension.

   > **Collapse: Signing/digest algorithm metadata example**
   >
   > ```xml
   > <Extensions>
   >  <alg:DigestMethod Algorithm="http://www.w3.org/2001/04/xmlenc#sha256"/>
   >  <alg:SigningMethod Algorithm="http://www.w3.org/2001/04/xmldsig-more#ecdsa-sha256"/>
   > </Extensions>
   > ```

   * In the AM admin UI, go to Applications > Federation > Entity Providers > *hosted entity provider*.

   * On the Assertion Content tab, in the Signing Algorithm drop-down list, select the signing algorithms this provider can use.

     There is no default for this property.

   * On the Assertion Content tab, in the Digest Algorithm drop-down list, select the digest algorithms this provider can use.

     There is no default for this property.

2. Configure the required encryption algorithms:

   Hosted SPs and IdPs advertise their encryption algorithms so that the remote providers know which ones they should use when sending encrypted data.

   > **Collapse: Encryption algorithm metadata example**
   >
   > ```xml
   > <!-- Enable RSA-OAEP key transport with AES-GCM data encryption: -->
   > <KeyDescriptor use="encryption">
   >  <EncryptionMethod Algorithm="http://www.w3.org/2009/xmlenc11#rsa-oaep"/>
   >  <EncryptionMethod Algorithm="http://www.w3.org/2001/04/xmlenc11#aes128-gcm"/>
   > </KeyDescriptor>
   > ```

   * In the AM admin UI, go to Applications > Federation > Entity Providers > *hosted entity provider*.

   * On the Assertion Content tab, in the Encryption Algorithm drop-down list, select the algorithms this provider can use.

     Select one or more AES algorithms from the list to encrypt assertion content, and one or more asymmetric algorithms to encrypt the transport key.

     For assertion encryption algorithms, use AES-GCM rather than the older AES-CBC modes. GCM offers authenticated encryption, which better protects against an attacker tampering with an encrypted assertion. Also sign assertions to make such attacks harder to exploit.

     **Assertion Encryption Algorithms**

     | Algorithm identifier                                    | Recommended |
     | ------------------------------------------------------- | ----------- |
     | `http://www.w3.org/2009/xmlenc11#aes128-gcm`            | ✔           |
     | `http://www.w3.org/2009/xmlenc11#aes192-gcm`            | ✔           |
     | `http://www.w3.org/2009/xmlenc11#aes256-gcm`            | ✔           |
     | `http://www.w3.org/2001/04/xmlenc#aes128-cbc` (default) |             |
     | `http://www.w3.org/2001/04/xmlenc#aes192-cbc`           |             |
     | `http://www.w3.org/2001/04/xmlenc#aes256-cbc`           |             |

     **Key Transport Algorithms**

     | Algorithm identifier                                        | Recommended |
     | ----------------------------------------------------------- | ----------- |
     | `http://www.w3.org/2009/xmlenc11#rsa-oaep`(1)               | ✔           |
     | `http://www.w3.org/2001/04/xmlenc#rsa-oaep-mgf1p` (default) |             |
     | `http://www.w3.org/2001/04/xmlenc#rsa-1_5`(2)               | ✖           |

     (1) When this algorithm is configured, AM uses the Mask Generation Function Algorithm property (Configure > Global Services > Common Federation Configuration) to create the transport key. For a list of supported mask generation function algorithms, refer to [Algorithms](../setup/services-configuration.html#global-federation-common-algorithms).

     (2) For security reasons, you *shouldn't* use this option.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | If you change the signing or encryption algorithms for the hosted entity provider, don't forget to update the algorithms on the remote entity provider to match. To do this in the AM admin UI, go to Applications > Federation > Entity Providers > *Remote Entity Provider* and select the Assertion Content tab. Alternatively, [reimport the metadata](saml2-providers-and-cots.html#configure-remote-entity) to delete and recreate the entity provider with the new details. |

## Configure AM to sign SAML 2.0 metadata

Map the `am.services.saml2.metadata.signing.RSA` secret label to an alias that AM uses to sign exported metadata:

1. In the AM admin UI, go to Configure > Secret Stores.

2. Select the Keystore or HSM store where you want to map the secret.

3. On the Mappings tab, select the `am.services.saml2.metadata.signing.RSA` secret label.

4. In the Edit Mapping pane:

   * To **edit** a mapping, click the pen icon.

   * To **add** a mapping, enter the alias, and click Add.

   * To **delete** a mapping, click the cross icon.

5. Save your changes.

6. Export the XML-based metadata from your hosted provider to share with other providers in your circle of trust, specifying the `sign=true` query parameter:

   ```bash
   $ curl \
   --output metadata.xml \
   "https://am.example.com:8443/am/ExportSamlMetadata\
   ?entityid=myHostedProvider\
   &sign=true\
   &realm=/mySubRealm"
   ```

   If you configure your provider in the Top Level Realm, you can omit the `realm` query parameter.

   The XML output contains a `<ds:Signature>` element that the remote entity uses to verify the authenticity of the metadata.

## Configure AM to sign and encrypt SAML 2.0 assertion content

Consider the following important points when configuring signing and encryption of assertion content:

* **Assertions**

  HTTP-POST bindings require **signed** assertions. If the response isn't signed, AM defaults to signing the assertion and uses the SP configuration to determine encryption settings.

  You must configure signing secret labels on the IdP, as described in [Secret label mappings for SAML 2.0 signing and encryption](../security/secret-mapping.html#secrets-saml2-signing-encryption).

  Failure to configure signing when using HTTP-POST bindings might result in errors such as:

  ```none
  ERROR: UtilProxySAMLAuthenticatorLookup.retrieveAuthenticationFromCache: Unable to do sso or federation.
  com.sun.identity.saml2.common.SAML2Exception: Provider's signing certificate alias is missing.
  ```

  or:

  ```none
  ERROR: SAML2Utils.verifyResponse:Assertion isn't signed or signature isn't valid.
  ```

* **SAML authentication requests**

  Signing is **recommended** to verify the request's authenticity and when using the `ForceAuthn` flag.

* **SAML assertion responses**

  Signing **AND** encrypting is **recommended** because responses can contain user data.

* **SAML logout requests**

  Signing is **recommended** to verify the request's authenticity.

|   |                                                                                                                                                      |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Configure key rollover by mapping more than one secret to the same secret label. Refer to [Map and rotate secrets](../security/secret-mapping.html). |

AM provides global default secrets for signing and encrypting SAML 2.0 assertion content with the following secret labels:

* `am.default.applications.federation.entity.providers.saml2.idp.encryption`

* `am.default.applications.federation.entity.providers.saml2.idp.signing`

* `am.default.applications.federation.entity.providers.saml2.sp.encryption`

* `am.default.applications.federation.entity.providers.saml2.sp.signing`

If you map these secret labels by realm, every provider of the same role uses the same secrets to sign and encrypt assertion content. For more granularity, you can override these settings and use custom secrets for each hosted provider in the realm:

1. In the AM admin UI, go to Applications > Federation > Entity Providers > *hosted entity provider*.

2. On the Assertion Content tab, in the Secret Label Identifier property, enter a string value to identify the secret labels this provider will use.

   For example, `mySamlSecrets`.

   > **Collapse: How do secret label identifiers work?**
   >
   > AM uses a secret identifier to know which secret labels are relevant for a provider. You can reuse the identifier that another provider is already using if you want them to share the same secrets.
   >
   > When a provider is removed from the AM configuration, AM automatically removes the secret labels related to their identifier, unless they're being used by another provider.
   >
   > If you don't specify a value for the secret label identifier, AM uses the global default secrets relative to the entity provider's role, *in the realm*. If they aren't mapped, AM searches for the global default secrets in the global secret stores.

3. Save your changes.

   AM creates two new secret labels, at the realm level, based on the value you specified.

   * `am.applications.federation.entity.providers.saml2.mySamlSecrets.signing`

   * `am.applications.federation.entity.providers.saml2.mySamlSecrets.encryption`

4. If you haven't configured a secret store in the same realm as the entity provider, create one by following the steps in [Secret stores](../security/secret-stores.html).

5. Go to Realms > *realm name* > Secret Stores, and select the secret store in which to map the new secret labels.

6. On the Mappings tab, add mappings for the two custom secret labels.

   ![Adding mappings for SAML entities at the realm level.](_images/realm-level-saml-secrets.png)

   For information on creating mappings, refer to [Map and rotate secrets](../security/secret-mapping.html).

   For information on the types of key pairs and secrets required, refer to [Secret label mappings for SAML 2.0 signing and encryption](../security/secret-mapping.html#secrets-saml2-signing-encryption).

7. In the AM admin UI, go to Applications > Federation > Entity Providers > *hosted entity provider*.

8. On the Assertion Content tab, in the Signing and Encryption section, select the SAML 2.0 elements that AM should sign, and the elements to encrypt.

9. Save your changes.

   AM now uses the key pairs you configured in the realm's secret store to sign or encrypt the elements you selected.

   |   |                                                                                                                                                                                                                    |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | For troubleshooting issues involving encryption, you can enable the `openam.saml.decryption.debug.mode` advanced property.Refer to [SAML 2.0 advanced properties](saml2-reference.html#saml2-advanced-properties). |

## Certificates and secrets

SAML 2.0 secrets for hosted SP or IdP entities are managed by the secrets API, which lets you [rotate certificates using secret mappings](../security/secret-mapping.html). This only applies to *hosted* entities; certificates for remote entities are derived from SAML 2.0 metadata provided by the third party.

The following certificates are used in SAML 2.0 flows with the corresponding secret mappings.

| Certificate                       | AM role    | Third-party role | AM use case                             | Third-party use case                   | Secret                                                                                                                                                            |
| --------------------------------- | ---------- | ---------------- | --------------------------------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hosted IdP signing certificate    | Hosted IdP | Remote SP        | Sign outbound SAML assertions           | Validate inbound signed SAML assertion | `am.applications.federation.entity.providers.saml2.<secret identifier>.signing`(1)(`am.default.applications.federation.entity.providers.saml2.idp.signing`)       |
| Hosted IdP encryption certificate | Hosted IdP | Remote SP        | Decrypt inbound encrypted SAML requests | Encrypt outbound SAML requests         | `am.applications.federation.entity.providers.saml2.<secret identifier>.encryption`(1)(`am.default.applications.federation.entity.providers.saml2.idp.encryption`) |
| Hosted SP signing certificate     | Hosted SP  | Remote IdP       | Sign outbound SAML requests             | Validate inbound signed SAML requests  | `am.applications.federation.entity.providers.saml2.<secret identifier>.signing`(1)(`am.default.applications.federation.entity.providers.saml2.sp.signing`)        |
| Hosted SP encryption certificate  | Hosted SP  | Remote IdP       | Decrypt inbound SAML assertions         | Encrypt outbound SAML assertions       | `am.applications.federation.entity.providers.saml2.<secret identifier>.encryption`(1)(`am.default.applications.federation.entity.providers.saml2.sp.encryption`)  |

(1) If defined, this secret is used; otherwise the default (*in brackets*) is used.

---

---
title: SP account mapper
description: Customize how SAML 2.0 assertions are mapped to user profiles using SP account mappers with Java or scripted implementations
component: pingam
version: 8.1
page_id: pingam:am-saml2:custom-sp-account-mapper
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-sp-account-mapper.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Scripts"]
page_aliases: ["saml2-guide:custom-sp-account-mapper.adoc"]
section_ids:
  java_example: Java example
  example-sp-account-mapper: Scripted example
  prepare-profile-data: Prepare the user profiles
  configure-auto-fed: Configure auto-federation
  use-sp-account-mapper-script: Update the SP account mapper script
  test-sp-account-mapper-script: Try the script
---

# SP account mapper

Use the SP account mapper to customize how SAML 2.0 assertions are mapped to user profiles.

## Java example

* Java interface

  `com.sun.identity.saml2.plugins.SPAccountMapper`

To create a custom SP account mapper in Java, follow the steps described in [How do I create a custom SAML2 SP account mapper in PingAM?](https://support.pingidentity.com/s/article/How-do-I-create-a-custom-SAML2-SP-account-mapper-in-PingAM) in the *Knowledge Base*.

## Scripted example

Learn about SP account mapper scripts from the following resources:

* Next-generation example script

  [SAML2 SP Account Mapper Script](../am-scripting/sample-scripts.html#saml2-sp-account-mapper-js)

* Scripting API

  [SP account mapper scripting API](../am-scripting/saml2-sp-account-mapper-api.html)

This section describes how to implement an example SP account mapper that uses a script to auto-federate user accounts. It assumes that you have configured your environment for SSO using SAML 2.0, where AM is the hosted SP. These example steps use another instance of AM as the remote IdP.

* [Prepare the user profiles](#prepare-profile-data)

* [Configure auto-federation](#configure-auto-fed)

* [Update the SP account mapper script](#use-sp-account-mapper-script)

* [Try the script](#test-sp-account-mapper-script)

### Prepare the user profiles

1. Create a test user on the hosted SP, for example `bjensen`, with an email address set to `bjensen@example.com`.

2. Create a test user on the hosted IdP, for example `babsjensen`, with an email address also set to `bjensen@example.com`.

### Configure auto-federation

In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers and click on the name of the hosted provider.

1. On the hosted SP:

   1. Under Assertion Processing > Auto Federation:

      * Switch on Enabled.

      * Set Attribute to `mail`.

   2. Save your changes.

2. On the hosted IdP:

   1. Under Assertion Processing > Attribute Mapper, add the following Attribute Map:

      * Name Format Uri

        `urn:oasis:names:tc:SAML:2.0:attrname-format:basic`

      * SAML Attribute

        `mail`

      * Local Attribute

        `mail`

   2. Save your changes.

### Update the SP account mapper script

1. In the AM admin UI, go to Realms > *realm name* > Scripts, and click SAML2 SP Account Mapper Script to modify the default script.

2. Update the script to implement any custom behavior for auto-federation. This example adds a logging statement to record the assertion map.

   ```java
   ...
   userID = accountMapperHelper.getAutoFedUser(nameID["value"]);
       if (userID != null && userID.length > 0) {
           //
           // insert custom code here
           //
           // update logging to output assertion and userID
           logger.error("Assertion: " + assertion);
           logger.error(debugMethod + " use AutoFedUser as userID: " + userID);
           return userID;
       } else {
           ...
       }
   ```

   |   |                                                                                                                            |
   | - | -------------------------------------------------------------------------------------------------------------------------- |
   |   | Learn about the available bindings in [SP account mapper scripting API](../am-scripting/saml2-sp-account-mapper-api.html). |

3. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted SP* > Assertion Processing.

4. Under Account Mapper, select the default script (`SAML2 SP Account Mapper Script`) from the Account Mapper Script drop-down list.

5. Save your changes.

### Try the script

1. To verify the script works as expected, test your changes using an SP-initiated flow.

   For example:

   ```none
   https://sp.example.com:8443/am/saml2/jsp/spSSOInit.jsp?realm=/alpha&idpEntityID=idp1&metaAlias=/alpha/sp1&binding=urn%3Aoasis%3Anames%3Atc%3ASAML%3A2.0%3Abindings%3AHTTP-POST
   ```

2. Log into the IdP as `babsjensen`.

   After you have logged into the IdP successfully, you don't need to log into the SP because the script successfully auto-federated the `babsjensen` and `bjensen` accounts.

3. Verify that `bjensen` is logged into the SP.

   You can also check that the SP [debug logs](../monitoring/debug-logging.html) contain the customized logging output, for example:

   ```none
   Assertion:
   {
       "version": "2.0",
       "issueInstant": 1758805815000,
       "subject": {
           "subjectConfirmation": [
               {
       …​
   }
   ScriptedSPAccountMapper.getIdentity::  use AutoFedUser as userID: id=bjensen,ou=user,o=alpha,ou=services,ou=am-config
   ```

---

---
title: SP adapter
description: Customize SP-initiated SAML 2.0 authentication by implementing hooks at key processing points using Java or scripts
component: pingam
version: 8.1
page_id: pingam:am-saml2:custom-sp-adapter
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/custom-sp-adapter.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Customization", "Java", "Scripts"]
page_aliases: ["plugins-sp-adapter.adoc", "saml2-guide:custom-sp-adapter.adoc"]
section_ids:
  java_example: Java example
  scripted_examples: Scripted examples
  example-sp-adapter-legacy: Redirect a journey using a legacy script
  example-sp-adapter-nextgen: Set session properties using a next-generation script
---

# SP adapter

Use the SP adapter to make changes during the processing of the authentication request, such as updating the `SPNameQualifier` attribute, or during assertion processing after a response has been received.

These steps assume your environment is already correctly configured for SSO using SAML 2.0, where AM is the hosted SP.

The SP adapter provides hooks at the following points:

| Extension point            | Description                                                                                           |
| -------------------------- | ----------------------------------------------------------------------------------------------------- |
| preSingleSignOnRequest     | Invoked before AM sends the SSO request to the IdP.                                                   |
| preSingleSignOnProcess     | Invoked before SSO processing begins on the SP side, when AM receives the response from the IdP.      |
| postSingleSignOnSuccess    | Invoked when SSO processing succeeds.                                                                 |
| postSingleSignOnFailure    | Invoked when SSO processing fails.                                                                    |
| postNewNameIDSuccess       | Invoked when the processing of a new name identifier succeeds.                                        |
| postTerminateNameIDSuccess | Invoked when the association of a name identifier between an SP and IdP is successfully terminated.   |
| preSingleLogoutProcess     | Invoked before the SLO process starts on the SP side, while the authenticated session is still valid. |
| postSingleLogoutProcess    | Invoked after the SLO process succeeds when the authenticated session has been invalidated.           |

## Java example

To create a custom SP adapter in Java, follow these high-level steps:

1. Include the `openam-federation-library` as a dependency in your Maven project.

2. Write a Java class that implements the [org.forgerock.openam.saml2.plugins.SPAdapter](../_attachments/apidocs/org/forgerock/openam/saml2/plugins/SPAdapter.html) interface.

3. Add code to one or more of the methods described in the [extension points table](#sp-adapter-points) to customize the authentication journey.

4. Package your custom class in a JAR file and copy to the `/WEB-INF/lib` folder where you deployed AM.

5. Configure AM to use the new Java plugin.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted SP* > Assertion Processing.

   2. In the Adapter field, type the fully qualified name of your custom class.

   3. Save your changes.

6. Restart AM or the container in which it runs.

7. Test your changes.

## Scripted examples

Learn about SP adapter scripts from the following resources:

* Legacy example script

  [SAML2 SP Adapter Script](../am-scripting/sample-scripts.html#saml2-sp-adapter-js)

* Next-generation example script

  [SAML2 SP Adapter Script (Next Gen)](../am-scripting/sample-scripts.html#saml2-sp-adapter-nextgen-js)

* Scripting API

  [SP adapter scripting API](../am-scripting/saml2-sp-adapter-api.html)

### Redirect a journey using a legacy script

Complete the following steps to implement an example SP adapter script that updates the `SPNameQualifier` attribute in the authentication request.

1. In the AM admin UI, go to Realms > *realm name* > Scripts, and click SAML2 SP Adapter Script. Alternatively, [create a new script](../am-scripting/manage-scripts-console.html) of type `Saml2 SP Adapter`.

2. In the Script field, add code to the `preSingleSignOnRequest` function to change the value of `SPNameQualifier` in the authentication request. Optionally, add code to redirect a successful login in the `postSingleSignOnSuccess` function.

   For example:

   ```javascript
   function preSingleSignOnRequest() {
     logger.error("In preSingleSignOnRequest");
     authnRequest.getNameIDPolicy().setSPNameQualifier("mySP-Updated");
   }

   function postSingleSignOnSuccess() {
       logger.error("In postSingleSignOnSuccess");
       response.sendRedirect("https://example.com");
       return true;
   }
   ```

3. Validate and save your changes.

4. Configure AM to use the updated SP adapter script.

   1. In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted SP* > Assertion Processing.

   2. Under Adapter, select your customized script from the Adapter Script drop-down list.

   3. Save your changes.

5. Test your changes using an SP-initiated flow.

   Verify that the SAML2.0 request contains the updated value (`SPNameQualifier="mySP-Updated"`) and that the user is redirected to `https://example.com` on successful login.

### Set session properties using a next-generation script

This example uses a next-generation script to set SAML attributes in the current session and conditionally redirects the authenticated user to a website.

1. In the AM admin UI, [create a new script](../am-scripting/manage-scripts-console.html) on the hosted SP with the following values:

   * Name

     `Example Next-Generation SP Adapter`

   * Script Type

     `Saml2 SP Adapter`

   * Evaluator Version

     `Next Generation`

2. In the Script field, replace the `postSingleSignOnSuccess` function with the following script:

   ```javascript
   function postSingleSignOnSuccess() {

     var redirectOccurred = false;

     try {

       if (!ssoResponse || !session) {
         logger.error("Missing ssoResponse or session object.");
         return false;
       }

       // Set response attributes as session properties
       var issueInstant = ssoResponse.issueInstant;
       var issuer = ssoResponse.issuer ? ssoResponse.issuer.value : "Unknown";
       session.setProperty("issueInstant", issueInstant);
       session.setProperty("issuer", issuer);
       logger.info("[issueInstant]: " + issueInstant + " [issuer]: " + issuer);

       // get address from assertion's attribute statement
       var assertion = ssoResponse.assertion[0];

       if (assertion && assertion.attributeStatements) {
         var statements = assertion.attributeStatements;

         for (var i = 0; i < statements.length; i++) {
           var attributes = statements[i].attribute;

           if (attributes && attributes.length > 0) {
             // Look for the 'Address' attribute
             for (var j = 0; j < attributes.length; j++) {

               if (attributes[j].name === "Address") {
                 var addressValue = attributes[j].attributeValueString;

                 if (addressValue && addressValue.length > 0) {
                   var address = addressValue[0];
                   logger.info("[postaladdress]: " + address);
                   session.setProperty("address", address);

                   // Redirect based on SAML address attribute
                   if (responseHelper) {
                     if (address === 'UK') {
                       responseHelper.sendRedirect("https://loremipsum.io/");
                     } else {
                       responseHelper.sendRedirect("https://example.com/");
                     }
                     redirectOccurred = true;
                   }
                   return redirectOccurred;
                 }
               }
             }
           }
         }
       }
     } catch (e) {
       logger.error("Error in postSingleSignOnSuccess: " + e.toString());
     }
     return redirectOccurred;
   }
   ```

3. On the remote IdP, map the attributes required for the script:

   1. Go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted IdP* > Assertion Processing.

   2. Add the following mapping to the Attribute Map:

      * SAML Attribute

        `Address`

      * Local Attribute

        `postaladdress`

   3. Save your changes.

4. Update a test user and set their address to `UK`:

   1. Click Identities > *test user* and set the following attribute:

      * Home Address

        `UK`

5. To test your changes, perform an SP-initated SSO flow using your UK test user.

   Verify that the user is redirected to `https://loremipsum.io` and that the logging output contains values for the SSO response attributes, for example:

   `INFO: [issueInstant]: 1770649129000 [issuer]: identityprovider1` `INFO: [postaladdress]: UK`

---

---
title: SSO and SLO in standalone mode
description: Configure PingAM to implement SAML 2.0 single sign-on and single logout in standalone mode using servlet URLs for identity provider or service provider initiated flows
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-standalone-mode
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-standalone-mode.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation"]
page_aliases: ["saml2-guide:saml2-standalone-mode.adoc"]
section_ids:
  using-saml2-sso-slo: SSO and SLO URLs
  saml2-sso-standalone-idpssoinit: IdP-initiated SSO URL
  saml2-sso-standalone-idpsloinit: IdP-initiated SLO URL
  saml2-sso-standalone-spssoinit: SP-initiated SSO URL
  saml2-sso-standalone-spsloinit: SP-initiated SLO URL
  saml2-progress: Indicate progress during SSO
  saml2-ecp-config: ECP profile configuration
---

# SSO and SLO in standalone mode

SSO lets users sign in once and remain authenticated as they access services in the circle of trust.

SLO attempts to log out all session participants:

* For hosted IdPs, SLO attempts to log out of all SPs with which the session established SAML federation.

* For hosted SPs, SLO attempts to log out of the IdP that was the source of the assertion for the authenticated session.

## SSO and SLO URLs

With standalone mode, AM SAML 2.0 federation provides servlet URLs that let users perform SSO and SLO across providers in a circle of trust.

|   |                                                                                                                                                                                                                                |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Previous versions of AM provided JSPs as entry points to standalone mode. The JSPs are now deprecated.Any customizations to these JSPs will be lost because they're now mapped to the servlet URLs for backward compatibility. |

AM has two URLs for SSO and two URls for SLO that let you initiate both processes either from the IdP side or from the SP side.

|   |                                                                                                    |
| - | -------------------------------------------------------------------------------------------------- |
|   | Make sure you accurately URL-encode any query parameters that you specify when accessing the URLs. |

### IdP-initiated SSO URL

* `/idpssoinit`

  Use this URL to initiate SSO from the IdP side. Call this on the IdP, not the SP.

  * Example

    * This example performs SSO from the IdP side, leaving the user at `https://pingidentity.com`:

      ```
      https://www.idp.com:8443/am/idpssoinit
      ?metaAlias=/idp
      &spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam
      &RelayState=https%3A%2F%2Fpingidentity.com
      ```

> **Collapse: Query parameters**
>
> * `metaAlias`
>
>   (Required) Use this parameter to specify the local alias for the provider, such as, `metaAlias=/alpha/idp`.
>
>   This parameter takes the format `/realm-name/provider-name`, as described in [MetaAlias](saml2-reference.html#idp-metaalias).
>
>   Don't repeat the slash for the Top Level Realm; for example, `metaAlias=/idp`.
>
> * `spEntityID`
>
>   (Required) Use this parameter to indicate the remote SP.
>
>   Make sure you URL-encode the value. For example, specify `spEntityID=https://www.sp.com:8443/am` as `spEntityID=https%3A%2F%2Fwww.sp.com%3A8443%2Fam`.
>
> * `affiliationID`
>
>   (Optional) Use this parameter to specify a SAML affiliation identifier.
>
> * `binding`
>
>   (Optional) Use this parameter to indicate which binding to use for the operation.
>
>   For example, specify `binding=HTTP-POST` to use HTTP POST binding with a self-submitting form. You can also specify `binding=HTTP-Artifact`.
>
> * `NameIDFormat`
>
>   (Optional) Use this parameter to specify a SAML Name Identifier format identifier.
>
>   For example, `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`, or `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`.
>
> * `RelayState`
>
>   (Optional) Use this parameter to specify where to redirect the user when the process is complete. Make sure you URL-encode the value.
>
>   For example, `RelayState=https%3A%2F%2Fpingidentity.com` takes the user to `https://pingidentity.com`.
>
> * `RelayStateAlias`
>
>   (Optional) Use this parameter to specify the parameter to use as `RelayState`.
>
>   For example, if the query string `target=https%3A%2F%2Fpingidentity.com&RelayStateAlias=target`, is equivalent to `RelayState=https%3A%2F%2Fpingidentity.com`.

### IdP-initiated SLO URL

* `IDPSloInit`

  Use this URL to initiate SLO from the IdP.

Example:

* This example performs SLO from the IdP side using a self-submitting form rather than a redirect, leaving the user at `https://pingidentity.com`:

  ```
  https://www.idp.com:8443/am/IDPSloInit
  ?binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST
  &RelayState=https%3A%2F%2Fpingidentity.com
  ```

> **Collapse: Query parameters**
>
> * `binding`
>
>   (Required) Use this parameter to indicate which binding to use for the operation. You must specify the full name of the binding.
>
>   The value must be one of the following:
>
>   * `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect`
>
>   * `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`
>
>   * `urn:oasis:names:tc:SAML:2.0:bindings:SOAP`
>
> * `Consent`
>
>   (Optional) Use this parameter to specify a URI that is a SAML Consent Identifier.
>
> * `Destination`
>
>   (Optional) Use this parameter to specify a URI Reference indicating the address to which the request is sent.
>
> * `Extension`
>
>   (Optional) Use this parameter to specify a list of Extensions as string objects.
>
> * `goto`
>
>   (Optional) Use this parameter to specify where to redirect the user when the process is complete. `RelayState` takes precedence over this parameter.
>
> * `logoutAll`
>
>   (Optional) Use this parameter to specify that the identity provider should send single logout requests to service providers without indicating a session index.
>
> * `RelayState`
>
>   (Optional) Use this parameter to specify where to redirect the user when the process is complete. Make sure you URL-encode the value.
>
>   For example, `RelayState=https%3A%2F%2Fpingidentity.com` takes the user to `https://pingidentity.com`.
>
>   To ensure the redirect is permitted, add the URL to the `RelayState URL List`. For details of this setting, see the [Reference](saml2-reference.html) section.

### SP-initiated SSO URL

* `spssoinit`

  Use this URL to initiate single SSO from the SP side.

Example:

* This example redirects the user from the SP to authenticate at the IdP and back to their profile page at the SP after successful SSO.

  ```
  https://www.sp.com:8443/am/spssoinit
  ?metaAlias=/sp
  &idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam
  &RelayState=https%3A%2F%2Fwww.sp.com%3A8443%2Fam%2FXUI%2F%23profile%2Fdetails
  ```

> **Collapse: Query parameters**
>
> * `idpEntityID`
>
>   (Required) Use this parameter to indicate the remote IdP. Make sure you URL-encode the value.
>
>   For example, encode `idpEntityID=https://www.idp.com:8443/am` as: `idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam`.
>
> * `metaAlias`
>
>   (Required) Use this parameter to specify the local alias for the provider, such as `metaAlias=/alpha/sp`.
>
>   This parameter takes the format `/realm-name/provider-name` as described in [MetaAlias](saml2-reference.html#sp-metaalias). Don't repeat the slash for the Top Level Realm, for example `metaAlias=/sp`.
>
> * `affiliationID`
>
>   (Optional) Use this parameter to specify a SAML affiliation identifier.
>
> * `AllowCreate`
>
>   (Optional) When set to `true`, the identity provider can create a new identifier for the principal if none exists.
>
> * `AssertionConsumerServiceIndex`
>
>   (Optional) Use this parameter to specify an integer that indicates the location to which the Response message should be returned to the requester.
>
> * `AuthComparison`
>
>   (Optional) Use this parameter to specify a comparison method to evaluate the requested context classes or statements.
>
>   AM accepts the following values:
>
>   * **better**. Specifies that the authentication context statement in the assertion must be better (stronger) than one of the provided authentication contexts.
>
>   * **exact**. Specifies that the authentication context statement in the assertion must exactly match at least one of the provided authentication contexts.
>
>   * **maximum**. Specifies that the authentication context statement in the assertion must not be stronger than any of the other provided authentication contexts.
>
>   * **minimum**. Specifies that the authentication context statement in the assertion must be at least as strong as one of the provided authentication contexts.
>
> * `AuthnContextClassRef`
>
>   (Optional) Use this parameter to specify authentication context class references. Separate multiple values with pipe (`|`) characters.
>
> * `AuthnContextDeclRef`
>
>   (Optional) Use this parameter to specify authentication context declaration references. Separate multiple values with pipe (`|`) characters.
>
> * `AuthLevel`
>
>   (Optional) Use this parameter to specify the authentication level of the authentication context that AM should use to authenticate the user.
>
> * `binding`
>
>   (Optional) Use this parameter to indicate which binding to use for the operation.
>
>   For example, specify `binding=HTTP-POST` to use HTTP POST binding with a self-submitting form. You can also specify `binding=HTTP-Artifact`.
>
> * `Destination`
>
>   (Optional) Use this parameter to specify a URI Reference indicating the address to which the request is sent.
>
> * `ForceAuthn`
>
>   (Optional) When set to `true` the identity provider should force authentication.
>
>   |   |                                                                                                                                                                                                                                                             |
>   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | Configure the `org.forgerock.openam.saml2.authenticatorlookup.skewAllowance` advanced property to specify the maximum permissible time since authentication by the IdP. See [SAML 2.0 advanced properties](saml2-reference.html#saml2-advanced-properties). |
>
>   When false, the IdP can reuse existing security contexts.
>
> * `isPassive`
>
>   (Optional) When set to `true` the IdP authenticates passively.
>
>   |   |                                                                                                                                                                                         |
>   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>   |   | A value of `true` is not honored if you have [configured an application tree](saml2-providers-and-cots.html#samlapp-tree), and the tree includes a node that requires user interaction. |
>
> * `NameIDFormat`
>
>   (Optional) Use this parameter to specify a SAML Name Identifier format identifier.
>
>   For example, `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`, or `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`.
>
> * `RelayState`
>
>   (Optional) Use this parameter to specify where to redirect the user when the process is complete. Make sure you URL-encode the value.
>
>   For example, `RelayState=https%3A%2F%2Fpingidentity.com` takes the user to `https://pingidentity.com`.
>
>   To ensure the redirect is permitted, add the URL to the `RelayState URL List`. For details of this setting, see the [Reference](saml2-reference.html) section.
>
> * `RelayStateAlias`
>
>   (Optional) Use this parameter to specify the parameter to use as the `RelayState`.
>
>   For example, the query string `target=https%3A%2F%2Fpingidentity.com&RelayStateAlias=target`, is the same as `RelayState=https%3A%2F%2Fpingidentity.com`.
>
> * `reqBinding`
>
>   (Optional) Use this parameter to indicate the binding to use for the authentication request.
>
>   Valid values in include `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect` (default) and `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`.
>
> * `sunamcompositeadvice`
>
>   (Optional) Use this parameter to specify a URL-encoded XML blob that specifies the authentication level advice.
>
>   For example, the following XML indicates a requested authentication level of 1. Notice the required `:` before the `1`:
>
>   ```xml
>   <Advice>
>     <AttributeValuePair>
>       <Attribute name="AuthLevelConditionAdvice"/>
>       <Value>/:1</Value>
>     </AttributeValuePair>
>   </Advice>
>   ```

### SP-initiated SLO URL

* `SPSloInit`

  Use this URL to initiate SLO from the SP.

  * Example

    * This example performs SLO from the SP side, leaving the user at `https://pingidentity.com`:

      ```
      https://www.sp.com:8443/am/SPSloInit
      ?binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect
      &RelayState=https%3A%2F%2Fpingidentity.com
      ```

> **Collapse: Query parameters**
>
> * `binding`
>
>   (Required) Use this parameter to indicate which binding to use for the operation. You must specify the full name of the binding.
>
>   For example, specify `binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST` to use HTTP POST binding with a self-submitting form, rather than the default HTTP redirect binding. You can also specify `binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Artifact`.
>
> * `idpEntityID`
>
>   (Required for Fedlets) Use this parameter to indicate the remote identity provider. If the `binding` property is not set, then AM uses this parameter to find the default binding. Make sure you URL-encode the value.
>
>   For example, specify `idpEntityID=https://www.idp.com:8443/am` as `idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fam`.
>
> * `NameIDValue`
>
>   (Required for Fedlets) Use this parameter to indicate the SAML Name Identifier for the user.
>
> * `SessionIndex`
>
>   (Required for Fedlets) Use this parameter to indicate the `sessionIndex` of the authenticated session to terminate.
>
> * `Consent`
>
>   (Optional) Use this parameter to specify a URI that is a SAML Consent Identifier.
>
> * `Destination`
>
>   (Optional) Use this parameter to specify a URI Reference indicating the address to which the request is sent.
>
> * `Extension`
>
>   (Optional) Use this parameter to specify a list of extensions as string objects.
>
> * `goto`
>
>   (Optional) Use this parameter to specify where to redirect the user when the process is complete.
>
>   The `RelayState` parameter takes precedence over this parameter.
>
> * `RelayState`
>
>   (Optional) Use this parameter to specify where to redirect the user when the process is complete. Make sure you URL-encode the value.
>
>   For example, `RelayState=https%3A%2F%2Fpingidentity.com` takes the user to `https://pingidentity.com`.
>
>   To ensure the redirect is permitted, add the URL to the `RelayState URL List`. For details of this setting, see the [Reference](saml2-reference.html) section.
>
> * `spEntityID`
>
>   (Optional, for Fedlets) Use this parameter to indicate the Fedlet entity ID.
>
>   When missing, AM uses the first entity ID in the metadata.

### Indicate progress during SSO

During SSO in standalone mode, AM presents users with a self-submitting form when access has been validated. This page is otherwise blank.

You can customize this page to indicate that SSO is in progress, for example, by adding an image or presentation element.

To do this, edit the source of the `autosubmitaccessrights.jsp` file in the AM `.war` file:

1. Unpack the AM-8.1.1.war file.

2. Edit or overwrite the `saml2/jsp/autosubmitaccessrights.jsp` file in the directory where you unpacked the `.war` file.

   |   |                                                    |
   | - | -------------------------------------------------- |
   |   | Make sure you retain the form and Java code as-is. |

3. Include any images referenced in your customized file.

4. Pack up your custom version of AM and deploy it in your web container.

## ECP profile configuration

The SAML 2.0 Enhanced Client or Proxy (ECP) profile is intended for use when accessing services over devices like simple phones, medical devices, and set-top boxes that lack the capabilities needed to use the more widely used SAML 2.0 Web Browser single sign-on profile.

The ECP knows which IdP to contact for the user, and is able to use the reverse SOAP (PAOS) SAML 2.0 binding for the authentication request and response. The PAOS binding uses HTTP and SOAP headers to pass information about processing SOAP requests and responses, starting with a PAOS HTTP header that the ECP sends in its initial request to the server. The PAOS messages continue with a SOAP authentication request in the server's HTTP response to the ECP's request for a resource, followed by a SOAP response in an HTTP request from the ECP.

An enhanced client, such as a browser with a plugin or an extension, can handle these communications on its own. An enhanced proxy is an HTTP server, such as a WAP gateway, that can support the ECP profile on behalf of client applications.

AM supports the SAML 2.0 ECP profile on the server side for IdPs and SPs. You must build the ECP.

By default, an AM IdP uses the `com.sun.identity.saml2.plugins.DefaultIDPECPSessionMapper` class to find an authenticated session for requests to the IdP from the ECP. The default session mapper uses AM cookies as it would for any other client application. If you *must* change the mapping after writing and installing your own session mapper, you can change the class under Realms > *realm name* > Applications > Federation > Entity Providers > *IdP name* > IDP > Advanced > ECP Configuration.

By default, an AM SP uses the `com.sun.identity.saml2.plugins.ECPIDPFinder` class to return IdPs from the list under Realms > *realm name* > Applications > Federation > Entity Providers > *SP name* > SP > Advanced > ECP Configuration > Request IDP List. You must populate the list with IdP entity IDs.

The endpoint for the ECP to contact on the AM SP is `/SPECP` as in `https://www.sp.com:8443/am/SPECP`.

The ECP provides two query string parameters to identify the SP and to specify the URL of the resource to access.

* `metaAlias`

  This specifies the SP, by default, `metaAlias=/realm-name/sp`, as described in [MetaAlias](saml2-reference.html#sp-meta-alias).

* `RelayState`

  This specifies the resource the client aims to access, such as `RelayState=https%3A%2F%2Fforgerock.org%2Findex.html`. Make sure this parameter is URL-encoded.

  For example, to access the SP followed by the resource at `https://forgerock.org/index.html`, use `https://www.sp.com:8443/am/SPECP?metaAlias=/sp&RelayState=https%3A%2F%2Fforgerock.org%2Findex.html`.

  |   |                                                                                                                                                                |
  | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | To ensure the redirect is permitted, add the URL to the `RelayState URL List`. For details of this setting, see the [Reference](saml2-reference.html) section. |

---

---
title: SSO in integrated mode
description: Use trees with a SAML2 Authentication node to handle SAML 2.0 single sign-on flows in integrated mode for SP-initiated and IdP-initiated authentication
component: pingam
version: 8.1
page_id: pingam:am-saml2:saml2-integrated-mode
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/saml2-integrated-mode.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Authentication"]
page_aliases: ["saml2-guide:saml2-integrated-mode.adoc"]
section_ids:
  spinit-sso-integrated-mode: SP-initiated SSO in integrated mode
  idpinit-sso-integrated-mode: IdP-initiated SSO in integrated mode
  saml2-integrated-mode-sso-trees: Implement SAML 2.0 SSO in integrated mode
  saml2-integrated-mode-sso-trees-procedure: Configure AM for integrated mode
  saml2-integrated-mode-sso-dynamic-standard: Create accounts dynamically during federation
---

# SSO in integrated mode

Integrated mode uses trees to handle the SAML 2.0 authentication flow.

|   |                                    |
| - | ---------------------------------- |
|   | Integrated mode supports SSO only. |

## SP-initiated SSO in integrated mode

This flow uses a SAML2 Authentication node in a tree on the SP. The node handles the SAML 2.0 protocol details for you.

When an end user initiates a SAML SSO flow, for example, by clicking a link to a resource on the SP's website, they're redirected to the IdP for authentication. On successful authentication, the flow returns to the SP for completion of the authentication journey.

To enable an SP-initiated SSO flow in integrated mode:

* Configure `AuthConsumer` as the consumer service location

* Define a tree with a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html)

Learn more about these prerequisites in [Configure AM for integrated mode](#saml2-integrated-mode-sso-trees-procedure).

> **Collapse: Example SP-initiated SSO flow in integrated mode**
>
> ![In this diagram, AM is configured as a SAML 2.0 SP. A user requests authentication to an AM authentication tree that contains the SAML2 Authentication node.](_images/saml2-integrated-node-flow.svg)
>
> Figure 1. SAML 2.0 SP-initiated SSO integrated mode flow
>
> 1. An end user initiates authentication to an AM SAML 2.0 SP. The login URL references a tree that includes a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html). For example, `https://am.example.com:8443/am/XUI/?service=mySAML2Tree.`
>
> 2. AM runs the authentication tree until it reaches the SAML2 Authentication node, which it then starts to process.
>
> 3. The node requests an assertion from the IdP. The configuration of the SAML2 Authentication node determines the details of the request.
>
> 4. If the user isn't authenticated in the IdP, the IdP will request them to authenticate.
>
>    The user provides their credentials for validation.
>
> 5. Authentication is successful.
>
> 6. The IdP responds to the SP with a SAML assertion.
>
> 7. If the SAML assertion contains a non-transient name ID, AM searches the identity store, attempting to locate a user with the same name ID.
>
> 8. **If the name ID for the account exists**, the tree continues.
>
> 9. **If the name ID doesn't exist** and the tree has a Create Object node (or a Provision Dynamic Account node for standalone AM environments), it creates a new account in the SP using auto-federation, including the name ID in the user profile.
>
> 10. **If the name ID doesn't exist**, and the following is configured:
>
>     * The name ID format is persistent
>
>     * The tree has a method of authenticating the user
>
>     * The tree has a Write Federation Information node
>
>     Then the node authenticates the user...
>
> 11. ... and writes the persistent name ID in the user profile.
>
>     Learn more about linking when auto-federation isn't configured in [Link identities for authentication](linking-auth-tree.html).
>
> 12. AM continues to process the remaining nodes in the tree...
>
> 13. ... and authentication is successful.

## IdP-initiated SSO in integrated mode

In an IdP-initiated SSO flow using integrated mode, an end user authenticates with the IdP and is redirected to the SP. When the SP receives the SAML response, the flow continues to the [authentication tree configured on the hosted SP](configure-providers.html#config-redirect-tree). If no tree is set, the flow results in an error.

You still need to *trigger* IdP-initiated SSO using a [URL](saml2-standalone-mode.html#saml2-sso-standalone-idpssoinit).

To enable an IdP-initiated SSO flow in integrated mode:

* Configure `AuthConsumer` as the consumer service location

* Define a redirect tree

Learn more about these prerequisites in [Configure AM for integrated mode](#saml2-integrated-mode-sso-trees-procedure).

> **Collapse: Example IdP-initiated SSO flow in integrated mode**
>
> ![In this diagram, AM is configured as a SAML 2.0 SP. An authenticated user is redirected to an AM authentication tree.](_images/saml2-integrated-node-flow-idpinit.svg)
>
> Figure 2. SAML 2.0 IdP-initiated SSO integrated mode flow
>
> 1. An end user initiates authentication to a third-party SAML 2.0 remote IdP.
>
> 2. If the user isn't authenticated in the IdP, the IdP requests their credentials.
>
>    The user provides their credentials for validation.
>
> 3. Authentication is successful.
>
> 4. The IdP creates a SAML response containing a signed SAML assertion and sends it to the SP's assertion consumer service URL, typically using the HTTP POST binding.
>
> 5. The SP processes the assertion and redirects the SAML flow to the URL set as Redirect Tree Name or Local Authentication URL in the hosted SP configuration.
>
> 6. If the tree has a Scripted Decision node, AM runs the script, including any logic to validate the assertion.
>
>    You can use the `getAssertion` method of the [`samlApplication` binding](../am-scripting/scripting-api-node.html#samlapp-binding) to check details in the assertion.
>
> 7. If the tree has a SAML2 Authentication node, it checks whether the IdP entity ID in the assertion matches the one set in configuration.
>
> 8. The SAML2 Authentication node can also use the nameID to locate a user in the identity store.
>
>    You can also temporarily federate accounts with an [SP account mapper script](custom-sp-account-mapper.html).
>
> 9. AM continues to process the remaining nodes in the tree...
>
> 10. ... and authentication is successful.

## Implement SAML 2.0 SSO in integrated mode

Complete the following tasks to implement SAML 2.0 SSO in integrated mode:

1. Prepare entity providers and a circle of trust, and update endpoints in the SP configuration.

   Learn more in [Configure AM for integrated mode](#saml2-integrated-mode-sso-trees-procedure).

2. Configure a tree that includes the SAML2 authentication node.

   * For IdP-initiated SSO, configure a redirect tree. Learn more in [configure a redirect tree](configure-providers.html#config-redirect-tree).

Find an example of a SAML tree in [Create accounts dynamically during federation](#saml2-integrated-mode-sso-dynamic-standard).

### Configure AM for integrated mode

1. If you haven't already done so, configure SAML 2.0 by performing the tasks listed in [Deployment considerations](saml2-configuration.html).

2. In the AM admin UI, create a hosted SP by following the steps in [Create a hosted IdP or SP](saml2-providers-and-cots.html#create-hosted-providers).

   Make sure you have configured the attribute map (Assertion Processing > Attribute Mapper). It determines how AM maps assertion attributes from the IdP to the user's profile on the SP.

   During the authentication process, the mapping is used to find existing users on the SP, and to create or update user accounts on the SP.

   For IdP-initiated SSO, you must configure a [redirect tree](configure-providers.html#config-redirect-tree) for the hosted SP to run after validating the IdP response.

3. Configure a remote IdP by following the steps in [Import a remote IdP or SP](saml2-providers-and-cots.html#configure-remote-entity).

   When you specify the circle of trust for the IdP, use the Add to Existing option and specify the circle of trust that you created when you created the hosted SP.

4. Change the Assertion Consumer Service locations in the hosted SP configuration.

   The default locations support standalone mode only, so you must update them when implementing integrated mode:

   * In the AM admin UI, go to Realms > *realm name* > Applications > Federation > Entity Providers > *hosted SP* > Services > Assertion Consumer Service.

   * Change the location of the HTTP-Artifact consumer service to use `AuthConsumer`, rather than `Consumer`.

     For example, if the location is `https://www.sp.com:8443/am/Consumer/metaAlias/sp`, change it to `https://www.sp.com:8443/am/AuthConsumer/metaAlias/sp`.

   * Similarly, change the location for the HTTP-POST consumer service to use `AuthConsumer` rather than `Consumer`.

     You don't need to change the location for the PAOS service because integrated mode doesn't support the PAOS binding.

   * The results will resemble the following:

     ![Editing the Consumer Service URLs for Integrated Mode.](_images/edit-consumer-for-integrated-mode.png)

     Save your changes.

You can now configure authentication trees for your SAML flow, for example, to dynamically create end user accounts.

### Create accounts dynamically during federation

In integrated mode, you can create complex trees to tailor the authentication experience to the requirements of your organization.

If you aren't using auto-federation, you can also use trees to create persistent links between user accounts.

Configure a tree similar to the following to create accounts dynamically:

* Standalone AM

* Ping Advanced Identity Software

![Example tree with SAML2 Authentication node](../am-authentication/_images/trees-node-saml2-example.png)Figure 3. Example tree with SAML2 Authentication node

1. Add a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

   The node processes the assertion, makes its contents available to the tree's state in the `userInfo` object, and tries to map the assertion's nameID using the `uid` mapping in the SP's assertion map.

   If the node finds a match, the tree continues through the `Account Exists` outcome. Otherwise, the tree continues through the `No Account Exists` outcome.

   |   |                                                                                                                                                                                                                             |
   | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | You can verify or inspect the SAML flow by including a Scripted Decision node to query the `samlApplication` binding.For SP-initiated flows, the Scripted Decision node must be placed after the SAML2 Authentication node. |

2. Add a [Provision Dynamic Account node](https://docs.pingidentity.com/auth-node-ref/8.1/am-only/provision-dynamic-account.html) to the `No account exists` outcome.

3. (Optional) If you haven't configured [auto-federation](auto-federation.html), you can add the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html) to create a persistent link between the accounts.

   Find examples in [Link identities by using authentication trees](linking-auth-tree.html#linking-auth-tree).

![Example tree for creating accounts dynamically](_images/saml-dynamic-journey.png)Figure 4. Example tree to create accounts dynamically

1. Add a [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html).

   The node processes the assertion, makes its contents available to the tree's state in the `userInfo` object, and tries to map the assertion's nameID using the `uid` mapping in the SP's assertion map.

   If the node finds a match, the tree continues through the `Account Exists` outcome. Otherwise, the tree continues through the `No Account Exists` outcome.

   Regardless of the outcome, because the node's `nameID` mapping isn't configurable, this example adds nodes to process the `userInfo` object and match it to the managed user's schema.

2. Add a [Scripted Decision node](https://docs.pingidentity.com/auth-node-ref/8.1/scripted-decision.html) to copy the information from the assertion to the authentication tree's shared state.

   > **Collapse: Example next-generation script**
   >
   > ```javascript
   > if (nodeState.get("userInfo")) {
   >   if (nodeState.get("objectAttributes")) {
   >     nodeState.remove("objectAttributes");
   >   }
   >   var userName=null,sn=null,mail=null;
   >
   >   try {
   >     var attribs = nodeState.get("userInfo")["attributes"];
   >
   >     userName=attribs["uid"][0];
   >     sn=attribs["sn"][0];
   >     mail=attribs["mail"][0];
   >
   >   } catch (e) {
   >     logger.error("Error getting userInfo: " + e);
   >   }
   >   nodeState.putShared("username", userName);
   >   nodeState.putShared("objectAttributes", {"userName":userName,"sn":sn,"mail":mail, "givenName": userName});
   > }
   > action.goTo("true");
   > ```
   >
   > |   |                                                                                       |
   > | - | ------------------------------------------------------------------------------------- |
   > |   | You can also query the `samlApplication` binding on the SP side to get the assertion. |

3. Add an [Identify Existing User node](https://docs.pingidentity.com/auth-node-ref/8.1/identify-existing-user.html) to search for the user with the appropriate attribute, for example, `userName`.

   If AM finds an existing matching user, the tree succeeds and the user is authenticated.

4. Add nodes to create the new account if AM doesn't find a matching user on the SP.

   The Scripted Decision node adds the attributes collected from the SAML assertion to the tree's shared state. If additional attributes are required to create an account, use the [Required Attributes Present node](https://docs.pingidentity.com/auth-node-ref/8.1/required-attributes-present.html) to identify missing ones and the [Attribute Collector node](https://docs.pingidentity.com/auth-node-ref/8.1/attribute-collector.html) to collect them.

   Finally, to create the account, use the [Create Object node](https://docs.pingidentity.com/auth-node-ref/8.1/create-object.html).

   Ensure that you configure the appropriate identity resource in this node, for example, `managed/alpha_user`.

5. (Optional) If you haven't configured [auto-federation](auto-federation.html), you can add the [Write Federation Information node](https://docs.pingidentity.com/auth-node-ref/8.1/write-federation-information.html) to create a persistent link between the accounts.

   Find examples in [Link identities by using authentication trees](linking-auth-tree.html#linking-auth-tree).

---

---
title: Web or Java agents SSO and SLO
description: Configure web or Java agents to perform SAML 2.0 single sign-on and single logout with PingAM identity provider and service provider deployments
component: pingam
version: 8.1
page_id: pingam:am-saml2:using-saml2-with-policy-agents
canonical_url: https://docs.pingidentity.com/pingam/8.1/am-saml2/using-saml2-with-policy-agents.html
llms_txt: https://docs.pingidentity.com/pingam/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["SAML 2.0", "Single Sign-on (SSO)", "Federation", "Java", "Agents"]
page_aliases: ["saml2-guide:using-saml2-with-policy-agents.adoc"]
section_ids:
  policy-agent-with-saml2: Use web or Java agents with a SAML 2.0 SP
---

# Web or Java agents SSO and SLO

You can use web agents and Java agents in a SAML 2.0 Federation deployment.

Configuring agents to work alongside AM when performing SAML 2.0 single sign-on and single logout involves altering the URLs the agents use for logging in unauthenticated users, and logging users out.

## Use web or Java agents with a SAML 2.0 SP

This procedure applies when AM is configured as an IdP in one domain, and a web or Java agent protects resources on behalf of a second AM server, configured as an SP, on a second domain.

1. Install the web or Java agent, as described in the [Web Agents documentation](https://docs.pingidentity.com/web-agents/2025.3/installation-guide/preface.html) or the [Java Agents documentation](https://docs.pingidentity.com/java-agents/2025.3/installation-guide/preface.html).

   The following steps will guide you to configure the agent through the AM admin UI. If your agent is not using the centralized configuration mode, make the changes to the noted properties in the configuration file of the agent instead: `agent.conf` for the web agent or `AgentConfiguration.properties` for the Java agent.

2. When using *web* agents:

   * In the AM admin UI of the SP, go to Realms > *realm name* > Applications > Agents > Web > *agent name* > AM Services.

   * When using [integrated mode SSO](saml2-integrated-mode.html):

     * Set the AM Login URL List property (`com.sun.identity.agents.config.login.url`) to the authentication tree that contains the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html). For example:

       ```
       https://www.sp.com:8443/am/XUI/#login/&service=mySAMLTree
       ```

   * When using [standalone mode SSO](saml2-standalone-mode.html):

     * Set the AM Login URL List property (`com.sun.identity.agents.config.login.url`) to the URL of the SP-initiated SSO URL, including the parameters necessary for initiating SSO. For example:

       ```
       https://www.sp.com:8443/am/spssoinit
       ?metaAlias=/sp
       &idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fopenam
       ```

     * Add the SP-initiated SLO URL to the AM Logout URL property (`com.sun.identity.agents.config.logout.url`). For example:

       ```
       https://www.sp.com:8443/am/SPSloInit
       ?binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect
       &RelayState=http%3A%2F%2Fwww.sp.com
       ```

   * Save your changes.

3. Set the Enable Custom Login Mode (`org.forgerock.openam.agents.config.allow.custom.login`) property to `1`.

4. Disable the Invalidate Logout Session property (`org.forgerock.agents.config.logout.session.invalidate` set to `false`).

5. When using *Java* agents:

   * In the AM admin UI of the SP, go to Realms > *realm name* > Applications > Agents > Java > *agent name* > AM Services.

   * When using [integrated mode SSO](saml2-integrated-mode.html):

     * Set the AM Login URL List property (`com.sun.identity.agents.config.login.url`) to the authentication tree that contains the [SAML2 Authentication node](https://docs.pingidentity.com/auth-node-ref/8.1/saml2.html). For example:

       ```
       https://www.sp.com:8443/am/XUI/#login/&service=mySAMLTree
       ```

   * When using [standalone mode SSO](saml2-standalone-mode.html):

     * Set the AM Login URL List property (`com.sun.identity.agents.config.login.url`) to the SP-initiated SSO URL, including the parameters necessary for initiating SSO. For example:

       ```
       https://www.sp.com:8443/am/spssoinit
       ?metaAlias=/sp
       &idpEntityID=https%3A%2F%2Fwww.idp.com%3A8443%2Fopenam
       ```

     * Add the SP-initiated SLO URL to the AM Logout URL property (`com.sun.identity.agents.config.logout.url`). For example:

       ```
       https://www.sp.com:8443/am/SPSloInit
       ?binding=urn:oasis:names:tc:SAML:2.0:bindings:HTTP-Redirect
       &RelayState=http%3A%2F%2Fwww.sp.com
       ```

   * Enable the Enable Custom Login Mode property (set the `org.forgerock.openam.agents.config.allow.custom.login` to `true`).

   * Enable the Convert SSO Tokens Into OIDC JWTs property (set the `org.forgerock.agents.accept.ipdp.cookie.enabled` to `true`).

   * Save your changes.