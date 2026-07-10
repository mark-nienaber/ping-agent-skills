---
title: Authentication requirements for SCIM 2.0 requests
description: All System for Cross-domain Identity Management (SCIM) requests on the server must use OAuth 2.0 bearer token authentication. Bearer tokens are evaluated using the SCIM 2.0 servlet extension's configured access token validators. Basic authentication isn't supported.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_authn_reqs_scim_2_requests
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_authn_reqs_scim_2_requests.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
page_aliases: ["pd_proxy_scim_1_1_servlet_ext_authn.adoc"]
---

# Authentication requirements for SCIM 2.0 requests

All System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* requests on the server must use OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* 2.0 bearer token authentication. Bearer tokens are evaluated using the SCIM 2.0 servlet extension's configured access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* validators. Basic authentication isn't supported.

In addition to requiring bearer tokens, the server doesn't process any SCIM requests unless it has at least one `encryption-settings` definition in its `encryption-settings` database. You can create the necessary definitions with the `encryption-settings` command-line tool. Learn more in [Encrypting sensitive data](../pingdirectory_server_administration_guide/pd_ds_encrypt_sensitive_data.html).

|   |                                                                                                               |
| - | ------------------------------------------------------------------------------------------------------------- |
|   | You must define encryption settings and ensure they match on the proxy and all backend PingDirectory servers. |

---

---
title: Configuring an LDAP-mapped SCIM resource type
description: Add a simple mapping System for Cross-domain Identity Management (SCIM) 2.0 resource type backed by the inetOrgPerson LDAP objectclass to a PingDirectoryProxy deployment.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_config_ldap_mapped_scim_resource_type
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_config_ldap_mapped_scim_resource_type.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  result: Result:
---

# Configuring an LDAP-mapped SCIM resource type

Add a simple mapping System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 resource type backed by the `inetOrgPerson` LDAP objectclass to a PingDirectoryProxy deployment.

To configure an LDAP mapped SCIM resource type:

## Steps

1. Set up the PingDirectory backend server.

2. Export the `encryption-settings` definition with the tool's `export` subcommand.

   ### Example:

   For this example, use the default settings to use sample data and configured data encryption.

   ```
   encryption-settings export --output-file exported-key
   ```

3. Set up the PingDirectoryProxy server and import the `encryption-settings` definition file that was created in the previous step.

4. To configure the LDAP external server, use the `create-initial-proxy-config` tool.

5. Create the SCIM schema for the resource type to use.

   ### Example:

   ```
   dsconfig create-scim-schema \
   --schema-name urn:pingidentity:schemas:User:1.0 \
   --set display-name:User
   ```

6. Under this schema, add the following SCIM attributes.

   ```
   dsconfig create-scim-attribute \
   --schema-name urn:pingidentity:schemas:User:1.0 \
   --attribute-name displayName
   dsconfig create-scim-attribute \
   --schema-name urn:pingidentity:schemas:User:1.0 \
   --attribute-name name \
   --set type:complex
   dsconfig create-scim-subattribute \
   --schema-name urn:pingidentity:schemas:User:1.0 \
   --attribute-name name \
   --subattribute-name familyName
   dsconfig create-scim-subattribute \
   --schema-name urn:pingidentity:schemas:User:1.0 \
   --attribute-name name \
   --subattribute-name formatted
   dsconfig create-scim-attribute \
   --schema-name urn:pingidentity:schemas:User:1.0 \
   --attribute-name userName
   ```

7. Create the LDAP mapping SCIM resource type on the PingDirectoryProxy server.

   ### Example:

   ```
   dsconfig create-scim-resource-type \
   --type-name Users \
   --type ldap-mapping \
   --set enabled:true \
   --set endpoint:Users \
   --set structural-ldap-objectclass:inetOrgPerson \
   --set include-base-dn:ou=People,dc=example,dc=com \
   --set lookthrough-limit:500 \
   --set core-schema:urn:pingidentity:schemas:User:1.0
   ```

8. To create the SCIM attribute mappings, run the following commands.

   ```
   dsconfig create-scim-attribute-mapping \
   --type-name Users \
   --mapping-name displayName \
   --set scim-resource-type-attribute:displayName \
   --set ldap-attribute:displayName
   dsconfig create-scim-attribute-mapping \
   --type-name Users \
   --mapping-name name.formatted \
   --set scim-resource-type-attribute:name.formatted \
   --set ldap-attribute:cn \
   --set searchable:true
   dsconfig create-scim-attribute-mapping \
   --type-name Users \
   --mapping-name name.familyName \
   --set scim-resource-type-attribute:name.familyName \
   --set ldap-attribute:sn \
   --set searchable:true
   dsconfig create-scim-attribute-mapping \
   --type-name Users \
   --mapping-name userName \
   --set scim-resource-type-attribute:userName \
   --set ldap-attribute:uid \
   --set searchable:true
   ```

9. Configure the SCIM2 HTTP Servlet Extension to use a Mock Access Token Validator.

   |   |                                                                                           |
   | - | ----------------------------------------------------------------------------------------- |
   |   | Never use Mock Access Token Validators in production environments or with sensitive data. |

   ```
   dsconfig create-access-token-validator \
   --validator-name "SCIM2 Mock Validator" \
   --type mock \
   --set enabled:true
   dsconfig set-http-servlet-extension-prop \
   --extension-name SCIM2 \
   --set "access-token-validator:SCIM2 Mock Validator"
   ```

10. To confirm that the new resource type is successfully added, send the following request to the PingDirectoryProxy server's SCIM `/ResourceTypes` endpoint.

    |   |                                                                   |
    | - | ----------------------------------------------------------------- |
    |   | The HTTP port can vary depending on the deployment configuration. |

    ```shell
    curl -k -X GET \
    https://localhost:8443/scim/v2/ResourceTypes \
    -H 'Authorization: Bearer {"active":true}'
    ```

    ### Result:

    The following JSON object is displayed in the response in the `"Resources"` array.

    ```json
    {
    ...
    "Resources": [{
    "schemas":["urn:ietf:params:scim:schemas:core:2.0:ResourceType"],
    "id":"Users",
    "name":"Users",
    "endpoint":"Users",
    "schema":"urn:pingidentity:schemas:Users:1.0",
    "meta":{
    "resourceType":"ResourceType",
    "location":"https://localhost:8443/scim/v2/ResourceTypes/Users"
    }
    }]
    ...
    }
    ```

---

---
title: Configuring permissions for SCIM 2.0 operations
description: Configure permissions so that POST requests with the userAdd scope succeed on a PingDirectoryProxy deployment.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_config_perms_scim_2_ops_proxy
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_config_perms_scim_2_ops_proxy.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  choose-from: Choose from:
  example: Example:
  example-2: Example:
  result: Result:
---

# Configuring permissions for SCIM 2.0 operations

Configure permissions so that POST requests with the `userAdd` scope succeed on a PingDirectoryProxy deployment.

## Before you begin

Set up an LDAP mapping System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 resource type for the `inetOrgPerson` object class. Learn more in [Configuring an LDAP-mapped SCIM resource type](pd_proxy_config_ldap_mapped_scim_resource_type.html).

To configure permissions:

## Steps

1. Set the SCIM resource type property:

   ### Choose from:

   * If the SCIM resource type being targeted already has a value for the `create-dn-pattern` property, skip to step 2.

   * To set the SCIM resource type property, run the following `dsconfig` command on the PingDirectoryProxy server.

     ```
     dsconfig set-scim-resource-type-prop \
     --type-name Users \
     --set create-dn-pattern:entryUUID=generated,ou=People,dc=example,dc=com
     ```

2. Send the following request to the PingDirectoryProxy server's SCIM `/Users` endpoint.

   ```shell
   curl -k -X POST \
   https://localhost:8443/scim/v2/Users/ \
   -H 'Authorization: Bearer {"active":true}' \
   -H 'Content-type: application/json' \
   --data '{"username":"user.test", "name":{"formatted":"Test",
   "familyName":"User"}, "schemas":["urn:pingidentity:schemas:User:1.0"]}'
   ```

   |   |                                                                   |
   | - | ----------------------------------------------------------------- |
   |   | The HTTP port can vary depending on the deployment configuration. |

   ### Example:

   The response from the server should have a status of `403` and should contain a correlation ID similar to the following.

   ```json
   {
   "schemas":["urn:ietf:params:scim:api:messages:2.0:Error"],
   "status":"403",
   "detail":"Request failed:
   correlationID='faa707b3-5d48-42e6-9e78-2c8dbb1e2cac'"
   }
   ```

   This is the expected response since this SCIM request doesn't have the permission needed to write to an entry. Learn how to access the full server error message in [Troubleshooting the SCIM 2.0 servlet extension](pd_proxy_troubleshoot_scim_2_servelet_ext.html).

3. Add an access control instruction (ACI) to the backend server's `ou=People,dc=example,dc=com` subtree.

   Run the following `ldapmodify` command to create the ACI on the backend PingDirectory server endpoint, not the PingDirectoryProxy endpoint.

   ```shell
   $ ldapmodify
   dn:ou=People,dc=example,dc=com
   changetype:modify
   add:aci
   aci:(version 3.0; acl "ACI for userAdd scope"; allow (add)
   oauthscope="userAdd";)
   ```

   |   |                                                                                                                                                                                                                                                                                                                                                             |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | This ACI grants permission to add entries to the specified subtree as long as the SCIM request contains the `userAdd` scope. The ACI doesn't grant write access to attributes, which means modify operations will fail. Learn more about ACI configurations in [Overview of access control](../managing_access_control/pd_ds_overview_access_control.html). |

4. Send the POST request to the SCIM `/Users` endpoint again, and include the `userAdd` scope in the bearer token.

   ### Example:

   ```shell
   curl -k -X POST \
   https://localhost:8443/scim/v2/Users \
   -H 'Authorization: Bearer {"active":true, "scope":"userAdd"}' \
   -H 'Content-type: application/json' \
   --data '{"username":"user.test", "name":{"formatted":"Test",
   "familyName":"User"}, "schemas":["urn:pingidentity:schemas:User:1.0"]}'
   ```

   ### Result:

   The response from the server contains the created SCIM resource, which also contains values for the name and username attributes similar to the following.

   ```json
   {
   "name":{
   "familyName":"User",
   "formatted":"Test"
   },
   "username":"user.test",
   "id":"6f9a89b8-e766-478c-9667-def049daf6bc",
   "meta":{
   "resourceType":"Users",
   "location":"https://localhost:8443/scim/v2/Users/6f9a89b8-e766-478c-9667-
   def049daf6bc"
   },
   "schemas":["urn:pingidentity:schemas:User:1.0"]
   }
   ```

---

---
title: Correlated LDAP data views
description: Correlated LDAP data views can be attached to a System for Cross-domain Identity Management (SCIM) resource type to allow that resource type to use attributes from other LDAP entries. A SCIM resource type can have multiple data views configured.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_correlated_ldap_data_views
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_correlated_ldap_data_views.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2024
section_ids:
  configuring-a-correlated-ldap-data-view: Configuring a correlated LDAP data view
  about-this-task: About this task
  steps: Steps
---

# Correlated LDAP data views

Correlated LDAP data views can be attached to a System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* resource type to allow that resource type to use attributes from other LDAP entries. A SCIM resource type can have multiple data views configured.

Correlated LDAP data views share many configuration settings with SCIM resource types. The following are exceptions:

* `primary-correlation-attribute`: The LDAP attribute from the SCIM resource type whose value will be used to match entries in the data view. This property must be defined.

* `secondary-correlation-attribute`: The LDAP attribute from the data view whose value will be matched with the primary-correlation-attribute. This property must be defined.

* `ldap-correlation-attribute-pair`: Optional correlation attribute pairs. If these are configured, entries between the SCIM resource type and the correlated LDAP data view must also have matching values for the specified attributes for them to be returned together.

|   |                                                                                                                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | A correlated LDAP data view can't provide attributes from more than one LDAP entry at a time. If there are multiple LDAP entries with secondary-correlation-attribute values that match the primary-correlation-attribute from the SCIM resource type's entry, the server throws an error. |

If the correlated LDAP data view is attached to a pass-through SCIM resource type, its attributes will appear as schema extensions, similar to the following:

```json
{
      ...
	"uid": [
    	"user.8"
	],
	"entryDN": "uid=user.8,ou=people,dc=example,dc=com",
	"urn:pingidentity:schemas:correlated:Document": {
    	    "documentIdentifier": [
        	    "user.8"
    	    ],
    	    "description": [
        	    "This is the description for the document user.8 under ou=Documents,dc=example,dc=com."
    	    ],
    	    ...
	},
	...
	"schemas": [
    	"urn:pingidentity:schemas:correlated:Document",
    	"urn:pingidentity:schemas:passthrough:PassthroughUsers"
	]
}
```

If the correlated LDAP data view is attached to a Mapping SCIM resource type, its attributes must be mapped to a schema used by the SCIM resource type. This is done through the correlated-ldap-data-view property in a SCIM attribute mapping *(tooltip: \<div class="paragraph">
\<p>Matching corresponding attributes between an IdP and an SP to identify federated users or add supplemental user information.\</p>
\</div>)*.

## Configuring a correlated LDAP data view

### About this task

The following example shows how to add a correlated LDAP data view to a LDAP mapping SCIM resource type on a PingDirectory server. The SCIM resource type will be a user, and the correlated LDAP data view will allow access to a document that matches their user ID.

In this example, a new PingDirectory server is set up using custom sample data. When configuring the correlation, administrators should use attributes that are inherently either immutable or non-volatile, such as `uid` or `entryUUID`. This prevents errors produced by a conflict between the values of primary and secondary correlation attributes.

|   |                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Administrators can make the correlation SCIM attributes immutable by setting the `--set mutability:read-only` property when defining an attribute in the SCIM schema configuration. That way, SCIM requests can't modify the values of those attributes. |

### Steps

1. Copy the following text into the server root directory and save it as `entries.ldif.template`:

   ```
   define suffix=dc=example,dc=com
   define maildomain=example.com
   define numusers=101

   branch: [suffix]
   subordinateTemplate: admin:1
   aci: (targetattr="*")(version 3.0; acl "Grant full access for the scim2allaccess OAuth 2 scope"; allow (all) oauthscope="scim2allaccess";)

   branch: ou=People,[suffix]
   subordinateTemplate: person:[numusers]

   branch: ou=Documents,[suffix]
   subordinateTemplate: document:[numusers]

   template: admin
   rdnAttr: uid
   objectClass: top
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   uid: admin
   givenName: Admin
   sn: User
   cn: Admin User
   userPassword: password

   template: person
   rdnAttr: uid
   objectClass: top
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   employeeNumber: <sequential:0>
   uid: user.{employeeNumber}
   sn: {uid}
   cn: {uid}
   userPassword: password

   template: document
   rdnAttr: documentIdentifier
   objectClass: top
   objectClass: document
   documentIdentifier: user.<sequential:0>
   description: This is the description for the document {documentIdentifier} under ou=Documents,dc=example,dc=com.
   ```

2. Run the following command:

   ```shell
   $ bin/make-ldif --templateFile entries.ldif.template --ldifFile entries.ldif
   ```

3. Run setup for the PingDirectory server.

   Make sure to import the created `entries.ldif` file and set up encryption settings. After this is done, set up the SCIM resource type and the correlated LDAP data view.

4. Run the following command to define the SCIM schema:

   ```
   "dsconfig create-scim-schema --schema-name urn:example:Users \
     --set "description:Users schema" --set display-name:Users
   dsconfig create-scim-attribute --schema-name urn:example:Users \
     --attribute-name email --set required:true --set multi-valued:true
   dsconfig create-scim-attribute --schema-name urn:example:Users \
     --attribute-name uid --set required:true --set mutability:read-only
   dsconfig create-scim-attribute --schema-name urn:example:Users \
     --attribute-name documentId
   dsconfig create-scim-attribute --schema-name urn:example:Users \
     --attribute-name documentDescription"
   ```

5. Run the following command to create the SCIM resource type:

   ```
   dsconfig create-scim-resource-type \
     --type-name Users \
     --type ldap-mapping \
     --set core-schema:urn:example:Users \
     --set enabled:true \
     --set endpoint:Users \
     --set structural-ldap-objectclass:inetOrgPerson \
     --set include-base-dn:ou=people,dc=example,dc=com \
     --set create-dn-pattern:entryUUID=generated,ou=people,dc=example,dc=com
   ```

6. Run the following command to create the correlated LDAP data view:

   ```
   dsconfig create-correlated-ldap-data-view \
     --type-name Users \
     --view-name Document \
     --set structural-ldap-objectclass:document \
     --set include-base-dn:ou=documents,dc=example,dc=com \
     --set create-dn-pattern:entryUUID=generated,ou=documents,dc=example,dc=com \
     --set primary-correlation-attribute:uid \
     --set secondary-correlation-attribute:documentIdentifier
   ```

7. Run the following command to create the attribute mappings for the SCIM resource type attributes.

   Note that the `correlated-ldap-data-view` property isn't set.

   ```
   # The uid attribute, provided by the base SCIM resource type
   dsconfig create-scim-attribute-mapping --type-name Users \
     --mapping-name uid \
     --set scim-resource-type-attribute:uid --set ldap-attribute:uid \
     --set writable:false --set searchable:true

   # The email attribute, provided by the base SCIM resource type
   dsconfig create-scim-attribute-mapping --type-name Users \
     --mapping-name email \
     --set scim-resource-type-attribute:email --set ldap-attribute:mail \
     --set searchable:true
   ```

8. Run the following command to create the `DocumentId` attribute mapping for the correlated LDAP data view attributes.

   |   |                                                                                                                                                                                      |
   | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
   |   | The only meaningful difference between mappings for SCIM resource type attributes and correlated LDAP data view attributes is the value of the `correlated-ldap-data-view` property. |

   ```
   # The documentId attribute
   dsconfig create-scim-attribute-mapping --type-name Users \
     --mapping-name document.id \
     --set correlated-ldap-data-view:Document \
     --set scim-resource-type-attribute:documentId --set ldap-attribute:documentIdentifier

   # The documentDescription attribute
   dsconfig create-scim-attribute-mapping --type-name Users \
     --mapping-name description \
     --set correlated-ldap-data-view:Document \
     --set scim-resource-type-attribute:documentDescription \
     --set ldap-attribute:description
   ```

9. Run the following command to send a SCIM request:

   ```shell
   curl -k -X GET \
     https://localhost:8443/scim/v2/Users \
     -H 'Authorization: Bearer {"active":true, "scope":"scim2allaccess"}'
   ```

   The response should look similar to the following. Notice that `uid` and `documentId` have the same value, as they are in a correlation attribute pair.

   ```json
   {
       "schemas": [
           "urn:ietf:params:scim:api:messages:2.0:ListResponse"
       ],
       "totalResults": 101,
       "Resources": [
           {
               "uid": "user.8",
               "id": "3715c022-1f34-36d9-bebc-7e74912106ec",
               "documentDescription": "This is the description \
               for the document user.8 under ou=Documents,dc=example,dc=com.,
               "documentId": "user.8",
               "meta": {
                   "resourceType": "Users",
                   "location": "https://localhost:8443/scim/v2/Users/3715c022-1f34-36d9-bebc-7e74912106ec"
               },
               "schemas": [
                   "urn:example:Users"
               ]
           },
       ...
   }
   ```

---

---
title: Defining permissions for SCIM 2.0 requests
description: Successfully executing a System for Cross-domain Identity Management (SCIM) request on a server depends on both the configured access control instruction (ACI) in the server and the scopes present in the OAuth bearer token used to authenticate the request.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_define_perms_scim_2_requests
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_define_perms_scim_2_requests.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# Defining permissions for SCIM 2.0 requests

Successfully executing a System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* request on a server depends on both the configured access control instruction (ACI) *(tooltip: \<div class="paragraph">
\<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
\</div>)* in the server and the scopes present in the OAuth *(tooltip: \<div class="paragraph">
\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>
\</div>)* bearer token used to authenticate the request.

|   |                                                                                                                |
| - | -------------------------------------------------------------------------------------------------------------- |
|   | You must define ACIs on the backend PingDirectory servers. Don't define ACIs on the PingDirectoryProxy server. |

The server can authorize SCIM 2.0 requests in one of the following ways:

* Internally, the server processes all SCIM 2.0 requests using the `cn=SCIM2 Servlet,cn=Root DNs,cn=config` service account. Allowing a requested operation depends on the relevant ACIs, which can include both the rights granted to that service account and any rights granted to scopes contained in the OAuth bearer token. The `oauthscope` bind rule is useful because it allows the administrator to use the supplied OAuth scopes in ACI logic.

* If user mapping is enabled, the subject of the OAuth bearer token is mapped to an account in the server. In this case, whether a requested operation is allowed depends on the ACIs that apply to the mapped user for the requested operation. You can also use the `oauthscope` bind rule to grant rights based on scopes in the presented token.

Because of implementation details, access to the `objectclass` operational LDAP attribute is necessary for SCIM requests to properly execute. Don't give the service account access to `objectclass` on a global level. Instead, add the ACI granting `objectclass` access to the LDAP subtree to expose to clients. Learn more in [Configuring permissions for SCIM 2.0 operations](pd_proxy_config_perms_scim_2_ops_proxy.html).

|   |                                                                                                                                                                                                                                                                                                                                                          |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | ACIs that don't use the `oauthscope` bind rule can still apply to requested operations. For example, an ACI that grants unconditional read access to any authenticated LDAP user also grants unconditional read access to SCIM requests regardless of the provided OAuth scopes. This is because the requests are processed through the service account. |

---

---
title: Disabling the SCIM 2.0 servlet extension
description: If you don't need to expose data through the System for Cross-domain Identity Management (SCIM) 2 servlet, you can disable the SCIM 2.0 servlet extension.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_disable_scim_2_servelet_ext
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_disable_scim_2_servelet_ext.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  steps: Steps
  example: Example
---

# Disabling the SCIM 2.0 servlet extension

If you don't need to expose data through the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2 servlet, you can disable the SCIM 2.0 servlet extension.

## Steps

1. Remove the SCIM 2 HTTP servlet extension from the HTTPS connection handler as well as from any other HTTP connection handlers.

2. Restart the handler.

## Example

```
dsconfig set-connection-handler-prop \
	--handler-name "HTTPS Connection Handler" \
	--remove http-servlet-extension:SCIM2 \
	--set enabled:false

	dsconfig set-connection-handler-prop \
	--handler-name "HTTPS Connection Handler" \
	--set enabled:true
```

---

---
title: Enabling user mapping for SCIM 2.0 operations
description: Access token validator identity mapping ties a local user account to an operation performed in the System for Cross-domain Identity Management (SCIM) 2.0 servlet in the PingDirectory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_ds_enable_user_mapping_scim2
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_ds_enable_user_mapping_scim2.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 4, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
---

# Enabling user mapping for SCIM 2.0 operations

Access token validator identity mapping ties a local user account to an operation performed in the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 servlet in the PingDirectory server.

|   |                                                      |
| - | ---------------------------------------------------- |
|   | This topic applies only to the PingDirectory server. |

The default configuration for the PingDirectory server for the SCIM 2.0 servlet doesn't require an access token to map to a local user, and operations are recorded in the logs as the `SCIM2 Servlet` user. For more detailed logging and auditing, enable the `map-access-tokens-to-local-users` property to require access tokens to map to a local user.

|   |                                                                                                                                                                                                                                                                                                                                                         |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The users that are being mapped to the access tokens must have the necessary access control rights required to perform the operations that the SCIM 2.0 servlet will invoke on their behalf. You should update the authorization server to issue tokens that include the `scim2` scope alongside any other scopes you need for access control purposes. |

The `map-access-tokens-to-local-users` property is an optional configuration with the three settings shown in the following table.

| Setting              | Definition                                                                                                                                                                                                                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Disabled` (default) | The server doesn't attempt to map SCIM 2.0 access tokens to local users and operations are processed under the authority of the `SCIM2 Servlet` user.                                                                                                                                          |
| `Optional`           | The server attempts to map SCIM 2.0 access tokens to local users and, if successful, the operations are processed under the authority of that user. The distinguished name (DN) of the mapped user appears in the access logs. If unsuccessful, the server falls back to the default behavior. |
| `Required`           | The server must map the SCIM 2.0 access token to one local user or the operation is rejected.                                                                                                                                                                                                  |

To set the `map-access-tokens-to-local-users` property:

## Steps

* Run `dsconfig` with the `set-http-servlet-extension-prop` option.

  ### Choose from:

  * To set the property to `required`, run the following command.

    ```
    dsconfig set-http-servlet-extension-prop \
      --extension-name SCIM2 \
      --set map-access-tokens-to-local-users:required
    ```

  * To set property to `optional`, run the following command.

    ```
    dsconfig set-http-servlet-extension-prop \
      --extension-name SCIM2 \
      --set map-access-tokens-to-local-users:optional
    ```

  * To reset the property to the default setting, `disabled`, run the following command.

    ```
    dsconfig set-http-servlet-extension-prop \
      --extension-name SCIM2 \
      --set map-access-tokens-to-local-users:disabled
    ```

---

---
title: Managing the SCIM 2.0 servlet extension
description: The PingDirectory and PingDirectoryProxy servers provide a System for Cross-domain Identity Management (SCIM) servlet extension to move users between cloud-based Software-as-a-Service (SaaS) applications securely and quickly. SCIM is an alternative to LDAP that lets you provision identity data over HTTPS.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_ds_scim_servlet_ext_mgmt
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_ds_scim_servlet_ext_mgmt.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 15, 2024
page_aliases: ["pingdirectory_server_administration_guide:pd_ds_manage_scim_servlet_exts.adoc", "pingdirectory_server_administration_guide:pd_proxy_scim_1_1_2_servlet_exts_mgmt.adoc", "pd_ds_scim_1_1_2_servlet_exts_mgmt.adoc", "pingdirectory_server_administration_guide:pd_ds_config_scim_2_server.adoc", "pingdirectory_server_administration_guide:pd_ds_manage_scim_2_servlet_ext.adoc", "pingdirectory_server_administration_guide:pd_ds_supported_scim_2_endpoints.adoc", "pd_proxy_manage_scim_2_servlet_ext.adoc", "pd_proxy_overview_scim_1_1_fund.adoc", "pd_proxy_identity_access_api.adoc", "pd_proxy_push_replace_before_you_begin.adoc", "pd_proxy_config_scim_1_1.adoc", "pd_proxy_config_scim_1_1_servlet_ext.adoc", "pd_proxy_config_scim_servlet_extension.adoc", "pd_proxy_verify_scim_1_1_servlet_ext_config.adoc", "pd_proxy_config_identity_access_api.adoc", "pd_proxy_monitor_scim_servlet_ext.adoc", "pd_proxy_config_adv_scim_1_1_ext_features.adoc", "pd_proxy_scim_1_1_schema.adoc", "pd_proxy_validate_updated_scim_schema.adoc", "pd_proxy_map_scim_resource_ids.adoc", "pd_proxy_use_pre_defined_transformations.adoc", "pd_proxy_map_ldap_entries_scim_ldap_api.adoc", "pd_proxy_scim_authn.adoc", "pd_proxy_scim_logging.adoc", "pd_proxy_scim_monitoring.adoc", "pd_proxy_create_scim_2_app.adoc", "pd_proxy_create_scim_1_1_app.adoc"]
section_ids:
  configuration-endpoints: Configuration endpoints
  create-an-application: Create an application
---

# Managing the SCIM 2.0 servlet extension

The PingDirectory and PingDirectoryProxy servers provide a System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* servlet extension to move users between cloud-based Software-as-a-Service (SaaS) applications securely and quickly. SCIM is an alternative to LDAP that lets you provision identity data over HTTPS.

The SCIM extension implements version 2.0 of the SCIM specification. Familiarize yourself with this specification to make efficient use of the SCIM extension and the SCIM SDK. Learn more in the [SCIM documentation](https://www.simplecloud.info).

You can use the SCIM extension to do the following:

* **Provision identities**: Through the API, you have access to the basic create, read, update, and delete functions, as well as other special functions.

* **Provision groups**: SCIM also allows you to manage groups.

* **Interoperate using a common schema**: SCIM provides a well-defined, platform-neutral user and group schema, as well as a simple mechanism to extend it.

## Configuration endpoints

PingDirectory and PingDirectoryProxy support the SCIM 2.0 endpoints listed in the following table.

|   |                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * For topologies with PingDirectoryProxy, configure your SCIM settings on the PingDirectoryProxy server instead of on the backend PingDirectory servers.

* There's a known issue with [dot notation support for SCIM 2.0 sub-attributes](../pingdatasync_server_administration_guide/pd_ds_scim_dot_notation.html). |

| Endpoint                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Supported HTTP methods  |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| `/ServiceProviderConfig`        | Provides metadata that indicates the server's authentication scheme (OAuth *(tooltip: \<div class="paragraph">&#xA;\<p>A standard framework that enables an application (OAuth client) to obtain access tokens from an OAuth authorization server for the purpose of retrieving protected resources on a resource server.\</p>&#xA;\</div>)* 2.0) and its support for features that are optional in the SCIM standard.This endpoint is a metadata endpoint and isn't subject to ACI restrictions. | GET                     |
| `/Schemas`                      | Lists the SCIM schemas that are configured for use on the server, and defines the various attributes available to resource types.This endpoint is a metadata endpoint and isn't subject to ACI restrictions.                                                                                                                                                                                                                                                                                      | GET                     |
| `/Schemas/<schema>`             | Retrieves a specific SCIM schema, as specified by the schema ID.This endpoint is a metadata endpoint and isn't subject to ACI restrictions.                                                                                                                                                                                                                                                                                                                                                       | GET                     |
| `/ResourceTypes`                | Lists all of the SCIM resource types that are configured for use on the server. Clients can use this information to determine the endpoint, core schema, and extension schemas of any resource types that the server supports.This endpoint is a metadata endpoint and isn't subject to ACI restrictions.                                                                                                                                                                                         | GET                     |
| `/ResourceTypes/<resourceType>` | Retrieves a specific SCIM resource type, as specified by its ID.This endpoint is a metadata endpoint and isn't subject to ACI restrictions.                                                                                                                                                                                                                                                                                                                                                       | GET                     |
| `/<resourceType>`               | Creates a new resource (POST), or lists and filters resources (GET).                                                                                                                                                                                                                                                                                                                                                                                                                              | GET, POST               |
| `/<resourceType>/.search`       | Lists and filters resources.This is used as an alternative to passing query parameters in the URL.                                                                                                                                                                                                                                                                                                                                                                                                | POST                    |
| `/<resourceType>/<resourceId>`  | Retrieves a single resource (GET), modifies a single resource (PUT, PATCH), or deletes a single resource (DELETE).                                                                                                                                                                                                                                                                                                                                                                                | GET, PUT, PATCH, DELETE |

## Create an application

To create a SCIM 2.0 application, you must [download the SCIM 2 SDK](https://github.com/pingidentity/scim2). The SCIM 2 SDK is a pre-packaged collection of libraries and extensible classes that provides developers with a simple, concrete API to interact with a SCIM service provider.

---

---
title: SCIM 2.0 components
description: The System for Cross-domain Identity Management (SCIM) 2.0 system is configured through the admin console or with the dsconfig command-line tool and includes the following components:
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_scim_2_components
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_scim_2_components.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# SCIM 2.0 components

The System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 system is configured through the admin console or with the `dsconfig` command-line tool and includes the following components:

* SCIM resource type

  A SCIM resource type defines a class of resources, such as users or devices. Every SCIM resource type features at least one SCIM schema, which defines the attributes available to each resource. If you enable a SCIM resource type, it must have a designated LDAP structural objectclass and an associated base distinguished name (DN).The two types of SCIM resource types, mapping and pass-through, differ based on the definitions of the SCIM schema the resource types use:

  * LDAP mapping SCIM

    Requires an explicitly defined SCIM schema with explicitly defined mappings of SCIM attributes to LDAP attributes. Use a mapping SCIM resource type to exercise detailed control over the SCIM schema and its attributes and mappings.

  * LDAP pass-through SCIM

    Doesn't use an explicitly defined SCIM schema. Instead, an implicit schema is generated dynamically based on the underlying LDAP schema. Use a pass-through SCIM resource type when you need to get started quickly

* SCIM schemas

  Defines a collection of SCIM attributes, grouped under an identifier called a schema URN. Each SCIM resource type possesses a single core schema and can feature schema extensions, which act as secondary attribute groupings that the schema URN namespaces. SCIM Schemas are defined independently of SCIM resource types, and multiple SCIM resource types can use a single SCIM schema as a core schema or schema extension.

* SCIM attributes

  Defines an attribute that is available under a SCIM schema. The configuration for a SCIM attribute defines its data type, regardless of whether it's required, single-valued, or multivalued.

* SCIM sub-attributes

  When a SCIM attribute consists of SCIM sub-attributes, it's defined as a complex attribute.

* SCIM attribute mappings (mapping resource types only)

  Defines the manner in which a SCIM resource type maps the attributes in its SCIM schemas to native LDAP attributes of the PingDirectoryProxy server.

* Correlated LDAP Data Views

  Allows a single SCIM resource that consists of attributes that are retrieved from multiple LDAP entries. Learn more in [Correlated LDAP data views](pd_proxy_correlated_ldap_data_views.html).

---

---
title: SCIM 2.0 PATCH operations
description: You can use a PATCH request to modify a System for Cross-domain Identity Management (SCIM) 2.0 resource that has one or more required SCIM 2.0 attributes.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_scim_2_patch_ops
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_scim_2_patch_ops.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  example: Example
---

# SCIM 2.0 PATCH operations

You can use a PATCH request to modify a System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 resource that has one or more required SCIM 2.0 attributes.

The requester needs permissions to read the values of these required attributes and to write permissions for the attributes being modified, even if the PATCH request doesn't alter the requirements.

## Example

You can modify an LDAP Mapping SCIM 2.0 resource type using the following schema definition, where `uid` and `cn` are mapped to their LDAP equivalents.

```json
{
	"schemas": ["urn:ietf:params:scim:schemas:core:2.0:Schema"],
	"id": "urn:test:schema:person",
	"attributes": [
	{
	"name": "uid",
	"type": "string",
	"multiValued": false,
	"required": true,
	"caseExact": false,
	"mutability": "readWrite",
	"returned": "default",
	"uniqueness": "none"
	},
	{
	"name": "cn",
	"type": "string",
	"multiValued": false,
	"required": false,
	"caseExact": false,
	"mutability": "readWrite",
	"returned": "default",
	"uniqueness": "none"
	}
		],
		...
			}
```

The following PATCH operation fails if the SCIM 2.0 service account doesn't have access to both `uid` and `cn`.

```json
{
	"schemas": ["urn:ietf:params:scim:api:messages:2.0:PatchOp"],
	"Operations":[{
	"op":"add",
	"path":"cn",
	"value": "new cn value"
	}]
		}
```

---

---
title: SCIM 2.0 searches
description: You can cap the total number of resources that are matched by a search to prevent exhausting server resources.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_scim_2_searches
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_scim_2_searches.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# SCIM 2.0 searches

You can cap the total number of resources that are matched by a search to prevent exhausting server resources.

The configuration for each System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 resource type contains a `lookthrough-limit` property that defines this limit. The default `lookthrough-limit` value is 500. If a search request exceeds the lookthrough limit, the client receives a `400` response with an error message similar to the following:

```
{
    "detail": "The search request matched too many results",
    "schemas": ["urn:ietf:params:scim:api:messages:2.0:Error"],
    "scimType": "tooMany",
    "status": "400"
}
```

To prevent this error:

* The client must refine its search filter to return fewer matches.

* You should configure paged searches as shown in [Using paged SCIM searches](pd_proxy_use_paged_scim_searches.html).

---

---
title: Troubleshooting a multiple correlation entry error
description: For environments that use correlated Lightweight Directory Access Protocol (LDAP) data views with the System for Cross-domain Identity Management (SCIM) 2.0 implementation, the SCIM response can include an error if multiple entries have a secondary correlation attribute value that matches the primary correlation attribute value. The error is applicable to both PingDirectory and PingDirectoryProxy.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_ds_troubleshoot_correlation_error
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_ds_troubleshoot_correlation_error.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Troubleshooting a multiple correlation entry error

For environments that use correlated Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* data views with the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 implementation, the SCIM response can include an error if multiple entries have a secondary correlation attribute value that matches the primary correlation attribute value. The error is applicable to both PingDirectory and PingDirectoryProxy.

There are three options for resolving this error:

* Configure one or more correlation attribute pairs on the correlated LDAP data view so that for each primary entry, there is only one other entry with matching secondary correlation attribute values. This is the recommended option.

* Modify the server data so that for each primary entry, there is only one other entry with a matching secondary correlation attribute value. This option isn't efficient for larger servers because it requires making changes to individual entries.

* If the other options don't resolve the issue, remove the correlated LDAP data view.

---

---
title: Troubleshooting the SCIM 2.0 servlet extension
description: To troubleshoot the System for Cross-domain Identity Management (SCIM) 2.0 servlet extension, you must enable the Debug Trace Logger.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_troubleshoot_scim_2_servelet_ext
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_troubleshoot_scim_2_servelet_ext.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
section_ids:
  steps: Steps
  example: Example:
  result: Result:
---

# Troubleshooting the SCIM 2.0 servlet extension

To troubleshoot the System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">
\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>
\</div>)* 2.0 servlet extension, you must enable the Debug Trace Logger.

For security reasons, error messages specifically regarding LDAP systems are suppressed and don't appear in the HTTP responses from the server. Instead, the response displays something like the following.

```json
{
	"schemas": [
	"urn:ietf:params:scim:api:messages:2.0:Error"
	],
	"status": "400",
	"detail": "Request failed: correlationID='073eb1a8-8c51-48b3-83a0-380e1d4b4ab9'"
}
```

## Steps

* To access these messages, enable the Debug Trace Logger through the admin console or with the following `dsconfig` command.

  ### Example:

  ```
  dsconfig set-log-publisher-prop --publisher-name "Debug Trace Logger" \
  			--set enabled:true --add scim-message-type:error
  ```

  ### Result:

  After you enable the Debug Trace Logger, the server begins logging information related to SCIM operations to the `/logs/debug-trace` file, as in the following example.

  ```
  [09/Jun/2020:05:23:10.992 -0500] HTTP REQUEST requestID=3
  correlationID="073eb1a8-8c51-48b3-83a0-380e1d4b4ab9" product="Ping Identity
  Directory Server" instanceName="example" startupID="Xt9fJg==" threadID=173
  from=[0:0:0:0:0:0:0:1]:53978 method=POST
  url="https://0:0:0:0:0:0:0:1:9443/scim/v2/Users"
  ```

  |   |                                                                                                                                                                                                           |
  | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | The presence of `correlationID` in these messages allows for matching the ID in the HTTP responses to the messages in the `debug-trace` log so that the appropriate LDAP error message can be determined. |

---

---
title: Using paged SCIM searches
description: When searching large data sets, the results can be numerous and produce errors about a request matching too many results relative to the lookthrough limit. Paged searches avoid these errors and reduce memory usage.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_scim_11_and_20_servlet_extensions:pd_proxy_use_paged_scim_searches
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_scim_11_and_20_servlet_extensions/pd_proxy_use_paged_scim_searches.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  before-you-begin: Before you begin
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
---

# Using paged SCIM searches

When searching large data sets, the results can be numerous and produce errors about a request matching too many results relative to the lookthrough limit. Paged searches avoid these errors and reduce memory usage.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The paged System for Cross-domain Identity Management (SCIM) *(tooltip: \<div class="paragraph">&#xA;\<p>An application-level, HTTP-based protocol for provisioning and managing user identity information. SCIM supplies a common schema for representing users and groups and provides a REST API.\</p>&#xA;\</div>)* searches feature isn't available for entry-balanced data sets. To use paged SCIM searches, your SCIM service's backend servers must be LDAP directory servers. |

## Before you begin

Complete the following one-time operation. You only need to run the command once per PingDirectoryProxy. If you're not sure if you've run the command, you can run it again safely.

```shell
$ dsconfig set-request-processor-prop \
--processor-name  <proxying-request-processor>  \
--set supported-control-oid:2.16.840.1.113730.3.4.9 \
--set supported-control-oid:1.2.840.113556.1.4.473
```

`<proxying-request-processor>` is the request processor handling the entries targeted by the search.

The PingDirectoryProxy server does SCIM searches using LDAP requests. After you complete the following steps, the PingDirectoryProxy server creates LDAP requests that include request controls that ask the backend servers to sort and page the search results before returning the results.

These request controls are marked noncritical, meaning that if the backend server can't page the results, the backend server still returns the results. In this case, the PingDirectoryProxy server handles the sorting and paging itself.

If your SCIM searches result in an error because the request matched too many results, you can avoid the error by using paged searches. Learn more in [SCIM 2.0 searches](pd_proxy_scim_2_searches.html).

For each search:

## Steps

1. Decide your SCIM search.

   |   |                                                                                                                      |
   | - | -------------------------------------------------------------------------------------------------------------------- |
   |   | To get paged results, your search must include at least one of these parameters: `startIndex`, `count`, or `sortBy`. |

   ### Example:

   Your search might look like the following.

   ```
   https://<proxy-hostname>:<proxy-port>/scim/v2/Users/?filter=st eq "TX"&sortBy=sn&sortOrder=ascending
   ```

   This is the corresponding encoded version.

   ```
   https://<proxy-hostname>:<proxy-port>/scim/v2/Users/?filter=st%20eq%20%22TX%22&sortBy=sn&sortOrder=ascending
   ```

   On your PingDirectoryProxy server, collect some information to use later. To find the SCIM resource type, `structural-ldap-objectclass`, `include-base-dn`, and `include-filter` values, run the following command.

   ```shell
   $ dsconfig get-scim-resource-type-prop --type-name  <SCIM-resource-type-name>  \
   --property structural-ldap-objectclass \
   --property include-base-dn \
   --property include-filter
   ```

2. For each backend server:

   1. Create a Virtual List View (VLV) index for your search using `dsconfig create-local-db-vlv-index` with the following options.

      | Option             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      | `--index-name`     | Names the index                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
      | `--backend-name`   | Specifies the name of the local database backend in which to place the index.The default database backend for PingDirectory is userRoot.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      | `--set base-dn`    | Specifies the desired base distinguished name (DN). This value must match the value of the `include-base-dn` property that you found in the previous step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      | `--set scope`      | Is always `whole-subtree`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      | `--set filter`     | Specifies the filter.Specify `(objectclass=<name-of-SCIM-resource-type-objectclass>)`where `<name-of-SCIM-resource-type-objectclass>` is the name of the objectclass used by the SCIM resource type property, which you found in the previous step.If the SCIM resource type has the `include-filter` property set, also specify that property value in the filter. For example, if the filter for the objectclass is `(objectclass=inetorgperson)` and the `include-filter` value is `(st=CA)`, specify the `--set filter` argument as `(&(objectclass=inetorgperson)(st=CA))`.Specify the LDAP attributes for all the components of your SCIM search filter.For example, if a mapping SCIM resource type maps the LDAP attribute `st` to the SCIM attribute `address.region` and the SCIM search filter requires that `address.region eq TX`, then this filter must include `(st = TX)` instead of `(address.region = TX)`. |
      | `--set sort-order` | Specifies whether to sort ascending (+) or descending (-) and the LDAP attribute to sort by.If the SCIM search doesn't specify the `sortBy` parameter, specify the sort order as `+entryUUID`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

      ### Example:

      Each SCIM search that you want to produce paged results must have its own VLV index.

      Recall the original, decoded SCIM search, shown here.

      ```
      https://<proxy-hostname>:<proxy-port>/scim/v2/Users/?filter=st eq "TX"&sortBy=sn&sortOrder=ascending
      ```

      To create a VLV index for that search, run the following command:

      ```shell
      $ dsconfig create-local-db-vlv-index --index-name sn \
      --backend-name userRoot --set base-dn:ou=people,dc=example,dc=com \
      --set scope:whole-subtree \
      --set filter:"(&(objectclass=inetorgperson)(st=TX))" --set sort-order:+sn
      ```

   2. Using the command line, stop the server, rebuild the index, start the server, and run the `rebuild-index` command specifying the base DN and the name of the index.

      ```shell
      $ rebuild-index --baseDN  <baseDN-value>  --index  <name-of-index>
      ```

      ### Example:

      ```shell
      $ stop-server
      $ rebuild-index --baseDN dc=example,dc=com --index vlv.sn
      $ start-server
      ```

3. Run your SCIM search filter.

   |   |                                                                                                                                                                              |
   | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The search can include only the filter you specified with `--set filter` in the earlier step without the `"(objectclass=<name-of-SCIM-resource-type-objectclass>)"` portion. |

   In addition to the Virtual List View request control, PingDirectoryProxy server adds a Server Side request control to the LDAP request. These request controls require certain parameters be set. To satisfy this requirement, PingDirectoryProxy server uses the following parameters.

   | Parameter    | Default                                                                                                      |
   | ------------ | ------------------------------------------------------------------------------------------------------------ |
   | `startIndex` | 1                                                                                                            |
   | `count`      | The value of the `lookthrough-limit` property of the SCIM resource type being searched. That default is 500. |
   | `sortBy`     | entryUUIDWith this default, the results appear unsorted.                                                     |
   | `sortOrder`  | ascending                                                                                                    |

   If the client doesn't provide values for one of the parameters, the search uses the corresponding default value shown in the table.