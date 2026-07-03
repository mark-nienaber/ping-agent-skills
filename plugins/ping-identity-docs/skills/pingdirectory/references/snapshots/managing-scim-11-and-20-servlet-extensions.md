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