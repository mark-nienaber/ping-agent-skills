---
title: $attr.attrName macro
description: The ($attr.attrName) macro extracts a value from a specified attribute in the target entry rather than extracting a value from a field with the same number in the target distinguished name (DN).
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_attr_attrname_macro
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_attr_attrname_macro.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# $attr.attrName macro

The `($attr.attrName)` macro extracts a value from a specified attribute in the target entry rather than extracting a value from a field with the same number in the target distinguished name (DN).

For example, `($attr.description)` is replaced with the value of the `description` attribute in the target entry. If there are multiple values for the specified attribute, then multiple actualized DNs are produced for the bind DN, and the first matching actualized DN is used.

The `($attr.attrName)` macro expands only the attribute's value so that you can extract values from the target DN and build relative distinguished names (RDNs) with different attribute names and types. Because the `($attr.attrName)` macro extracts only the attribute's value, you can combine it with a type other than what is in the target DN.

---

---
title: Access token validator processing
description: You can configure any number of access token validators for the server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_proxy_access_token_validator_proc
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_proxy_access_token_validator_proc.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  processing-steps: Processing steps
---

# Access token validator processing

You can configure any number of access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* validators for the server.

Each access token validator has an evaluation order index, which is an integer that determines the processing priority when multiple access token validators are configured. Lower values are processed before higher values.

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Access tokens issued using the OAuth 2 client credentials grant type are issued directly to a client and do not contain a subject. Such tokens cannot be accepted by PingDirectory server. |

## Processing steps

1. If an incoming HTTP request *(tooltip: \<div class="paragraph">
   \<p>A client transaction sent over HTTP to the server specifying a request method, such as GET, POST, and DELETE, to execute against a resource or resources on the server.\</p>
   \</div>)* contains an access token, the token is sent to the access token validator with the lowest evaluation order index.

2. The access token validator validates the access token. Validation logic varies by access token validator type, but the validator generally verifies the following information:

   * A trusted source issued the token.

   * The token is not expired.

3. If the access token contains a subject, the access token validator uses its identity mapper to find a matching Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
   \<p>An open, cross platform protocol used for interacting with directory services.\</p>
   \</div>)* entry.

4. If the access token validator is unable to validate the access token, it passes the token to the access token validator with the next lowest evaluation order index, and the previous two steps are repeated.

5. HTTP request processing continues, and the policy request is sent to the HTTP service, such as the Directory REST API, for further evaluation.

6. Using either the access token claims parsed by the access token validator or the LDAP entry found by the identity mapper, the HTTP service determines whether the request should be accepted and which access control rules should be applied. This access control behavior varies by each HTTP service.

---

---
title: Access token validator types
description: The server works with a variety of access token validators.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_access_token_validator_types
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_access_token_validator_types.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# Access token validator types

The server works with a variety of access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* validators.

This section contains the following topics:

* [Configuring a sample PingFederate access token validator](pd_ds_config_sample_pf_access_token_validator.html)

* [JWT access token validator](pd_ds_jwt_access_token_validator.html)

* [Mock access token validator](pd_ds_mock_access_token_validator.html)

* [Third-party access token validator](pd_ds_third_party_access_token_validator.html)

---

---
title: Access token validators
description: Access token validators verify the tokens that HTTP client applications submit when they request access to protected resources and associate each token with an identity stored in the directory server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_access_token_validators
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_access_token_validators.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 2, 2024
---

# Access token validators

Access token validators verify the tokens that HTTP client applications submit when they request access to protected resources and associate each token with an identity stored in the directory server.

To authenticate to PingDirectory server's HTTP services, clients use OAuth 2 bearer token authentication to present an access token *(tooltip: \<div class="paragraph">
\<p>A data object by which a client authenticates to a resource server and lays claim to authorizations for accessing particular resources.\</p>
\</div>)* in the HTTP Authorization request header.

To process the incoming access tokens, PingDirectory server uses access token validators, which determine whether to accept an access token and translate it into a set of properties, called claims, which PingDirectory server's HTTP services use to make access control decisions.

Most access tokens identify a user as its subject using the `sub` claim. Access token validators can retrieve the token subject's attributes from the directory using an identity mapper, which correlates the access token subject to an Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* entry.

Access token validators are used by the following services:

* Directory REST API

* SCIM 2

* Delegated Admin

* Consent API

You can configure the PingDirectory server to accept access tokens provided by LDAP clients using the OAUTHBEARER Simple Authentication and Security Layer (SASL) authentication method.

---

---
title: Configuring a sample PingFederate access token validator
description: To verify the access tokens that a PingFederate authorization server issues, the PingFederate access token validator uses HTTP to submit the tokens to PingFederate server's token introspection endpoint.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_config_sample_pf_access_token_validator
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_config_sample_pf_access_token_validator.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
section_ids:
  before-you-begin: Before you begin
  about-this-task: About this task
  steps: Steps
---

# Configuring a sample PingFederate access token validator

To verify the access tokens that a PingFederate authorization server issues, the PingFederate access token validator uses HTTP to submit the tokens to PingFederate server's token introspection endpoint.

## Before you begin

Before using a PingFederate access token validator, create a client that represents the access token validator in the PingFederate configuration. This client must use the Access Token Validation grant type.

## About this task

This step allows the authorization server to determine whether a token is valid.

|   |                                                                                                                                                                                            |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Access tokens issued using the OAuth 2 client credentials grant type are issued directly to a client and do not contain a subject. Such tokens cannot be accepted by the directory server. |

Because this step requires an outgoing HTTP request to the authorization server, the PingFederate access token validator might perform slower than other access token validator types. The validation result is guaranteed to be current, which is an important consideration if the authorization server permits the revocation of access tokens.

## Steps

1. In PingFederate, create a client with the following properties:

   * Client ID: Ping Identity

   * Client authentication: Client Secret

   * Allowed grant types: Access Token Validation

2. Take note of the client secret and use the directory server's `dsconfig` command to create an access token validator, as shown.

   ```
   # Create an identity mapper that expects the token subject to be a uid
   dsconfig create-identity-mapper \
   	--mapper-name "User ID Identity Mapper" \
   	--type exact-match \
   	--set enabled:true \
   	--set match-attribute:uid \
   	--set match-base-dn:ou=people,dc=example,dc=com
   # Change the host name and port below, as needed
   dsconfig create-external-server \
     --server-name "PingFederate External Server" \
     --type http \
     --set base-url:https://example.com:9031
   # Create the Access Token Validator
   dsconfig create-access-token-validator \
     --validator-name "PingFederate Access Token Validator" \
     --type ping-federate \
     --set enabled:true \
     --set "authorization-server:PingFederate External Server" \
     --set client-id:PingDirectory \
     --set "client-secret:<client secret>"
     --set evaluation-order-index:2000
     --set "identity-mapper:User ID Identity Mapper"
   ```

   Learn more about the configuration options for a PingFederate access token validator in the [PingDirectory Configuration Reference Guide](https://developer.pingidentity.com/reference/pingdirectory/10.2.0.0/config-guide/ping-federate-access-token-validator.html).

3. Replace *\<client secret>* with the client secret value generated by the PingFederate client.

---

---
title: Configuring proxied authorization
description: Configuring proxied authorization requires a combination of access control instructions (ACIs) and the proxied-auth privilege to the entry that will perform operations as another user.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_config_proxied_authn
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_config_proxied_authn.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  example-4: Example:
---

# Configuring proxied authorization

## About this task

Configuring proxied authorization requires a combination of access control instructions (ACIs) and the `proxied-auth` privilege to the entry that will perform operations as another user.

|   |                                                                                                                                                                                                                                                        |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | You cannot use the `cn=Directory Manager` root DN as a proxying DN. Unless your use case requires proxying root users and administrators, consider restricting proxy users as described in [Restricting proxy users](pd_ds_restrict_proxy_users.html). |

## Steps

1. Open a text editor and create a user entry that will request operations as another user. Include the `proxied-auth` privilege. Save the file as `add-user.ldif`.

   ### Example:

   In this example, the user entry `uid=clientApp` will request operations as `uid=admin,dc=example,dc=com`.

   ```
   dn: ou=Applications,dc=example,dc=com
   objectClass: top
   objectClass: organizationalUnit
   objectClass: extensibleObject
   ou: Admins
   ou: Applications

   dn: uid=clientApp,ou=Applications,dc=example,dc=com
   objectClass: top
   objectClass: person
   objectClass: organizationalPerson
   objectClass: inetOrgPerson
   givenName: Client
   uid: clientApp
   cn: Client App
   sn: App
   userPassword: password
   ds-privilege-name: proxied-auth
   ```

2. Add the file using `ldapmodify`.

   ### Example:

   ```shell
   $ bin/ldapmodify --defaultAdd --filename add-user.ldif
   ```

3. To allow the target, open a text editor and create an LDIF file to assign an ACI to that branch so that the client app user can access it as a proxy auth user. Add the file using the`ldapmodify`.

   The client application targets a specific subtree in the Directory Information Tree (DIT) for its operations. For example, a client might need access to an accounts subtree to retrieve customer information while another client might need access to another subtree, such as a subscriber subtree.

   ### Example:

   In this example, the client application targets the `ou=People,dc=example,dc=com` subtree.

   |   |                                                                                                            |
   | - | ---------------------------------------------------------------------------------------------------------- |
   |   | The ACI should be on a single line of text. The example shows the ACI over multiple lines for readability. |

   ```
   dn: ou=People,dc=example,dc=com
   changetype: modify
   add: aci
   aci:  (version 3.0; acl "People Proxy Access"; allow(proxy)
     userdn="ldap:///uid=clientApp,ou=Applications,dc=example,dc=com";)
   ```

4. Run a search to test the configuration using the bind DN `uid=clientApp` and the `proxyAs` option.

   Prefix `dn:` to the proxying entry or `u:` to the username.

   ### Example:

   The `uid=clientApp` binds to the server and proxies as `uid=admin` to access the `ou=People,dc=example,dc=com` subtree.

   ```shell
   $ bin/ldapsearch --port 1389 \
     --bindDN "uid=clientApp,ou=Applications,dc=example,dc=com" \
     --bindPassword password \
     --proxyAs "dn:uid=admin,dc=example,dc=com" \
     --baseDN ou=People,dc=example,dc=com \
     "(objectclass=*)"
   ```

---

---
title: Examples of common access control rules
description: This section demonstrates access controls that are commonly used in your environment.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_common_access_control_rules
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_common_access_control_rules.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
page_aliases: ["pd_ds_proxy_admin_access.adoc", "pd_ds_anon_and_authn_access.adoc", "pd_ds_delegated_access_to_manager.adoc", "pd_ds_proxy_authn.adoc"]
section_ids:
  administrator-access: Administrator access
  anonymous-and-authenticated-access: Anonymous and authenticated access
  delegated-access-to-a-manager: Delegated access to a manager
  proxy-authorization: Proxy authorization
---

# Examples of common access control rules

This section demonstrates access controls that are commonly used in your environment.

To modify access control definitions in the server, a user must have the `modify-acl` privilege.

## Administrator access

The following access control instructions (ACIs) grant members of the `cn=admins,ou=groups,dc=example,dc=com` group the following permissions:

* Add, modify, and delete entries

* Reset passwords

* Read operational attributes, such as `isMemberOf` and password policy state

```
aci: (targetattr="+")(version 3.0; acl "Administrators can read, search or compare operational attributes";
allow (read,search,compare) groupdn="ldap:///cn=admins,ou=groups,dc=example,dc=com";)
aci: (targetattr="*")(version 3.0; acl "Administrators can add, modify and delete entries";
allow (all) groupdn="ldap:///cn=admins,ou=groups,dc=example,dc=com";)
```

## Anonymous and authenticated access

The following ACIs allow anonymous read, search, and compare on select attributes of `inetOrgPerson` entries while authenticated users can access several more. An authenticated user inherits the privileges of the anonymous ACI and can also change `userPassword`.

```
aci: (targetattr="objectclass || uid || cn || mail || sn || givenName")(targetfilter="(objectClass=inetorgperson)")
(version 3.0; acl "Anyone can access names and email addresses of entries representing people";
allow (read,search,compare) userdn="ldap:///anyone";)
aci: (targetattr="departmentNumber || manager || isMemberOf")(targetfilter="(objectClass=inetorgperson)")
(version 3.0; acl "Authenticated users can access these fields for entries representing people";
allow (read,search,compare) userdn="ldap:///all";)
aci: (targetattr="userPassword")(version 3.0; acl "Authenticated users can change password";
allow (write) userdn="ldap:///all";)
```

To prevent anonymous access to the directory server, set the global configuration property `reject-unauthenticated-requests` to `true`.

## Delegated access to a manager

The following ACI allows an employee's manager to edit the value of the employee's `telephoneNumber` attribute. This ACI uses the `userattr` keyword with a bind type of `USERDN`, which indicates that the target entry's manager attribute must have a value equal to the distinguished name (DN) of the authenticated user.

```
aci: (targetattr="telephoneNumber")
(version 3.0; acl "A manager can update telephone numbers of her direct reports";
allow (read,search,compare,write) userattr="manager#USERDN";)
```

## Proxy authorization

The following ACI allows the application `cn=OnBehalf,ou=applications,dc=example,dc=com` to use the proxied authorization V2 control to request that operations be performed using an alternate authorization identity.

```
aci: (version 3.0;acl "Application OnBehalf can proxy as another entry";
allow (proxy) userdn="ldap:///cn=OnBehalf,ou=applications,dc=example,dc=com";)
```

|   |                                                              |
| - | ------------------------------------------------------------ |
|   | The application user must have the `proxied-auth` privilege. |

---

---
title: General format of the access control rules
description: Access control instructions (ACIs) are represented as strings that are applied to one or more entries within the directory information tree (DIT).
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_general_format_access_control_rules
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_general_format_access_control_rules.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
---

# General format of the access control rules

Access control instructions (ACIs) are represented as strings that are applied to one or more entries within the directory information tree (DIT).

Typically, an ACI is placed on a subtree, such as `dc=example,dc=com`, and applies to that base entry and all entries below it in the tree. The directory server iterates through the DIT to compile the access control rules into an internally-used list of denied and allowed targets and their permissible operations. When a client application, such as `ldapsearch`, enters a request, the server checks that the user who binds with the server has the necessary access rights to the requested search targets. ACIs are cumulatively applied so that a user who has an ACI at an entry can also have other access rights available if ACIs are defined higher in the DIT and are applicable to the user. In most environments, ACIs are defined at the root of a main branch or a subtree, and not on individual entries unless absolutely required.

![A diagram showing the components of an ACI string.](_images/hez1564011764517.png)ACI

An access control rule has the following basic syntax:

```
    aci : (targets) (version 3.0; acl "name";
            permissions
            bind rules
            ;)
```

**Access Control Components**

| Access Control Component | Description                                                                                                                                                                                                                                      |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| targets                  | Specifies the set of entries and attributes to which an access control rule applies. Use the following syntax: `(target keyword = \|\| != expression)`                                                                                           |
| name                     | Specifies the name of the ACI                                                                                                                                                                                                                    |
| permissions              | Specifies the type of operations to which an access control rule might apply. Use the following syntax: `allow\|\|deny (permission)`                                                                                                             |
| bind rules               | Specifies the criteria that indicate whether an access control rule should apply to a given requester. Use the following syntax: `bind rule keyword = \|\|!= expression;`&#xA;&#xA;The bind rule syntax requires that it be terminated with a ;. |

---

---
title: Handling encrypted tokens
description: Configure the JSON web token (JWT) access token validator to accept encrypted access tokens. You must configure the access token validator with a private and public key pair and provide the public key to the token issuer.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_handle_encrypted_tokens
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_handle_encrypted_tokens.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
section_ids:
  steps: Steps
  choose-from: Choose from:
  example: Example
---

# Handling encrypted tokens

Configure the JSON web token (JWT) access token validator to accept encrypted access tokens. You must configure the access token validator with a private and public key pair and provide the public key to the token issuer.

## Steps

1. Create an encryption key pair.

2. Create the JWT access token validator.

3. Export the public encryption key from the PingDirectory server and provide it to your token issuer.

   ### Choose from:

   * To copy the public key to a file, run `dsconfig`.

   * Copy the value of the key pair's `certificate-chain` property in the admin console.

     |   |                                                                                                                               |
     | - | ----------------------------------------------------------------------------------------------------------------------------- |
     |   | Without this public encryption key, the issuer cannot encrypt tokens that can be decrypted by the JWT access token validator. |

## Example

The following example configures a JWT access token validator to handle access tokens signed and encrypted using elliptic curve algorithms.

For RSA signing and encryption algorithms, the configuration is similar, but you choose different values for the `allowed-signing-algorithm` and `allowed-encryption-algorithm` properties.

1. Create an encryption key pair.

   ```
   # Create an encryption key pair
   	dsconfig create-key-pair \
   	--pair-name "JWT Elliptic Curve Encryption Key Pair" \
   	--set key-algorithm:EC_256
   ```

2. Create the JWT access token validator.

   ```
   # Create an identity mapper that expects the token subject to be a uid
   dsconfig create-identity-mapper \
   	--mapper-name "User ID Identity Mapper" \
   	--type exact-match \
   	--set enabled:true \
   	--set match-attribute:uid \
   	--set match-base-dn:ou=people,dc=example,dc=com

   # Change the host name and port below, as needed
   dsconfig create-external-server \
   	--server-name "PingFederate External Server" \
   	--type http \
   	--set base-url:https://example.com:9031

   # Create the Access Token Validator
   dsconfig create-access-token-validator \
   	--validator-name "JWT Access Token Validator" \
   	--type jwt \
   	--set enabled:true \
   	--set evaluation-order-index:1000 \
   	--set allowed-signing-algorithm:ES256 \
   	--set "authorization-server:PingFederate External Server" \
   	--set jwks-endpoint-path:/ext/oauth/jwks \
   	--set "encryption-key-pair:JWT Elliptic Curve Encryption Key Pair" \
   	--set allowed-key-encryption-algorithm:ECDH_ES
   	--set "identity-mapper:User ID Identity Mapper"
   ```

3. Export the public encryption key from the PingDirectory server and provide it to your token issuer.

   The following command copies the key to a file.

   ```
   dsconfig get-key-pair-prop \
   	--pair-name "JWT Elliptic Curve Encryption Key Pair" \
   	--property certificate-chain \
   	--no-prompt \
   	--script-friendly > jwt-public-encryption-key.pem
   ```

---

---
title: Handling signed tokens
description: The token issuer must cryptographically sign all access tokens that the JSON web token (JWT) access token validator handles. The JWT access token validator validates a token's signature using a public signing key provided by the issuer.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_handle_signed_tokens
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_handle_signed_tokens.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 28, 2024
page_aliases: ["pd_ds_use_locally_config_trusted_cert.adoc", "pd_ds_use_issuer_jwks_endpoint.adoc"]
section_ids:
  steps: Steps
  choose-from: Choose from:
  example-use-a-locally-configured-trusted-certificate: "Example: Use a locally configured trusted certificate"
  example-use-the-issuers-jwks-endpoint: "Example: Use the issuer's JWKS endpoint"
---

# Handling signed tokens

The token issuer must cryptographically sign all access tokens that the JSON web token (JWT) access token validator handles. The JWT access token validator validates a token's signature using a public signing key provided by the issuer.

## Steps

* Configure the JWT access token validator with the issuer's public signing key:

  ### Choose from:

  * Store the public key as a trusted certificate in the server's local configuration using the `trusted-certificate` property.

  * Provide the issuer's JSON Web Key Set (JWKS) endpoint using the `jwks-endpoint-path` property.

    |   |                                                                                                                                                                                                                                                                                                    |
    | - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    |   | To ensure that the JWT access token validator uses updated copies of the issuer's public keys, the validator checks the configured JWKS endpoint in the following cases:- When the validator initializes

    - If the validator can't find a suitable key for verification in its current set of keys |

## Example: Use a locally configured trusted certificate

The following example configures a JWT access token validator to use a locally stored public signing certificate to validate access token signatures. The signing certificate is assumed to have been obtained out-of-band and must be a PEM-encoded X.509v3 certificate.

```
# Create an identity mapper that expects the token subject to be a uid
dsconfig create-identity-mapper \
	--mapper-name "User ID Identity Mapper" \
	--type exact-match \
	--set enabled:true \
	--set match-attribute:uid \
	--set match-base-dn:ou=people,dc=example,dc=com

# Add the public signing certificate to the server configuration
dsconfig create-trusted-certificate \
	--certificate-name "JWT Signing Certificate" \
	--set "certificate</path/to/signing-certificate.pem"

# Create the Access Token Validator
dsconfig create-access-token-validator \
	--validator-name "JWT Access Token Validator" \
	--type jwt \
	--set enabled:true \
	--set evaluation-order-index:1000 \
	--set allowed-signing-algorithm:RS256 \
	--set "trusted-certificate:JWT Signing Certificate"
	--set "identity-mapper:User ID Identity Mapper"
```

## Example: Use the issuer's JWKS endpoint

The following example configures a JWT access token validator to retrieve public keys from a PingFederate authorization server's JWKS endpoint.

```
# Create an identity mapper that expects the token subject to be a uid
dsconfig create-identity-mapper \
	--mapper-name "User ID Identity Mapper" \
	--type exact-match \
	--set enabled:true \
	--set match-attribute:uid \
	--set match-base-dn:ou=people,dc=example,dc=com

# Change the host name and port below, as needed
dsconfig create-external-server \
	--server-name "PingFederate External Server" \
	--type http \
	--set base-url:https://example.com:9031

# Create the Access Token Validator
dsconfig create-access-token-validator \
	--validator-name "JWT Access Token Validator" \
	--type jwt \
	--set enabled:true \
	--set evaluation-order-index:1000 \
	--set allowed-signing-algorithm:RS256 \
	--set "authorization-server:PingFederate External Server" \
	--set jwks-endpoint-path:/ext/oauth/jwks
	--set "identity-mapper:User ID Identity Mapper"
```

---

---
title: JWT access token validator
description: The JWT access token validator verifies access tokens that are encoded in JSON Web Token (JWT) format, which can be signed in JSON web signature (JWS) format or signed and encrypted in JSON web encryption (JWE) format.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_jwt_access_token_validator
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_jwt_access_token_validator.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
section_ids:
  supported-jwsjwe-features: Supported JWS/JWE features
---

# JWT access token validator

The JWT access token validator verifies access tokens that are encoded in JSON Web Token (JWT) format, which can be signed in JSON web signature (JWS) format or signed and encrypted in JSON web encryption (JWE) format.

The JWT access token validator inspects the JWT token without presenting it to an authorization server for validation. Because the JWT access token validator does not make a token introspection request for every access token that it processes, it performs faster than the PingFederate access token validator. The access token is self-validated, so the JWT access token validator cannot determine whether the token has been revoked.

## Supported JWS/JWE features

For signed tokens, the JWT access token validator supports the following JWT web algorithm (JWA) types:

* RS256

* RS384

* RS512

* ES256

* ES384

* ES512

For encrypted tokens, the JWT access token validator supports the following key-encryption algorithms:

* RSA-OAEP

* ECDH-ES

* ECDH-ES+A128KW

* ECDH-ES+A192KW

* ECDH-ES+A256KW

For encrypted tokens, the JWT access token validator supports the following content-encryption algorithms:

* A128CBC-HS256

* A192CBC-HS384

* A256CBC-HS512

The JWT access token validator configuration defines three allow lists for the JWS/JWE signing and encryption algorithms that it accepts. Customize these allow lists to reflect only the signing and encryption algorithms used by your access token issuer and no others. This minimizes the access token validator's security threat surface.

Configure these allow lists using the following configuration properties:

* `allowed-signing-algorithm`

  Specifies the signing algorithms that the access token validator accepts.

* `allowed-key-encryption-algorithm`

  Specifies the key-encryption algorithms that the access token validator accepts.

* `allowed-content-encryption-algorithm`

  Specifies the content-encryption algorithms that the access token validator accepts.

Learn more about the configuration options for a [JWT access token validator](https://docs.ping.directory/PingDirectory/latest/config-guide/jwt-access-token-validator.html).

---

---
title: Key access control features
description: The directory server provides important access control features that provide added security for its entries.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_key_access_control_features
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_key_access_control_features.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
page_aliases: ["pd_ds_improved_validation_security.adoc", "pd_ds_global_acis.adoc", "pd_ds_key_access_controls_for_public_private_backends.adoc"]
section_ids:
  improved-validation-and-security: Improved validation and security
  global-acis: Global ACIs
  access-controls-for-public-or-private-backends: Access controls for public or private backends
---

# Key access control features

The directory server provides important access control features that provide added security for its entries.

## Improved validation and security

The server provides an access control model with strong validation to help ensure that invalid access control instructions (ACIs) are not allowed into the server.

The server ensures that all access control rules (ACRs) added over LDAP are valid and can be fully parsed. The server rejects any operation that attempts to store one or more invalid ACIs. It also validates ACIs contained in data imported from an LDIF file. The server rejects any entry containing a malformed `aci` value.

As an additional level of security, the server examines and validates all ACIs stored in the data whenever a backend is brought online. If the server finds any malformed ACIs in the backend, it generates an administrative alert to notify administrators of the problem and places itself in lockdown mode. While in lockdown mode, the server only allows requests from users who have the `lockdown-mode` privilege. This action allows administrators to correct the malformed ACI while ensuring that no sensitive data is inadvertently exposed because of an ACI not being enforced. When the problem has been corrected, the administrator can use the `leave-lockdown-mode` tool or restart the server to allow it to resume normal operation.

## Global ACIs

Global ACIs are a set of ACIs that apply to entries anywhere in the server or scoped to only apply to a specific set of entries.

Global ACIs work in conjunction with ACRs stored in user data and provide a convenient way to define ACIs that span disparate portions of the directory information tree (DIT).

In the Server, global ACIs are defined within the server configuration, in the `global-aci` property of the configuration object for the access control handler. To view and manage global ACIs, use configuration tools like `dsconfig` and the admin console.

The global ACIs available by default in the Server include:

* Allow anyone, including unauthenticated users, to access key attributes of the root DSA-specific entry (DSE), including:

  * `namingContexts`

  * `subschemaSubentry`

  * `supportedAuthPasswordSchemes`

  * `supportedControl`

  * `supportedExtension`

  * `supportedFeatures`

  * `supportedLDAPVersion`

  * `supportedSASLMechanisms`

  * `vendorName`

  * `vendorVersion`

* Allow anyone, including unauthenticated users, to access key attributes of the subschema subentry, including:

  * `attributeTypes`

  * `dITContentRules`

  * `dITStructureRules`

  * `ldapSyntaxes`

  * `matchingRules`

  * `matchingRuleUse`

  * `nameForms`

  * `objectClasses`

* Allow anyone, including unauthenticated users, to include the following controls in requests made to the server:

  * Authorization identity request

  * Manage DSA IT

  * Password policy

  * Real attributes only

  * Virtual attributes only

* Allow anyone, including unauthenticated users, to request the following extended operations:

  * Get symmetric key

  * Password modify request

  * Password policy state

  * StartTLS

  * Who Am I?

## Access controls for public or private backends

Depending on their intended purpose, the PingDirectory server classifies backends as either public or private.

A backend is private if one of the following applies:

* Its content is generated by the server itself, such as the root DSE, monitor, and backup backends.

* It is used in the operation of the server, such as the configuration, schema, task, and trust store backends.

* Its content is maintained by the server, such as the LDAP changelog backend.

A public backend is intended to hold user-defined content, such as user accounts, groups, application data, and device data.

The server access control model also supports the distinction between public backends and private backends. Many private backends do not allow writes of any kind from clients, and some of the private backends that do allow writes only allow changes to a specific set of attributes. As a result, you should define any ACI intended to permit or restrict access to information in private backends as global ACIs, rather than attempting to add those instructions to the data for that private backend.

---

---
title: Managing access control
description: The PingDirectory and PingDirectoryProxy servers provide a fine-grained access control model to ensure that users are able to access the information they need but are prevented from accessing information that they shouldn't see.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_manage_access_control
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_manage_access_control.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
---

# Managing access control

The PingDirectory and PingDirectoryProxy servers provide a fine-grained access control model to ensure that users are able to access the information they need but are prevented from accessing information that they shouldn't see.

The access control model includes a privilege subsystem that provides even greater flexibility and protection.

This section presents the access control model and provides examples that illustrate the use of key access control functionality.

---

---
title: Migrating ACIs from Oracle to the PingDirectory server
description: This section describes the most important differences in access control evaluation between Oracle and the server.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_migrate_acis_oracle_server
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_migrate_acis_oracle_server.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 13, 2024
page_aliases: ["pd_ds_support_macro_acis.adoc", "pd_ds_support_roledn_bind_rule.adoc", "pd_ds_targeting_operational_attributes.adoc", "pd_ds_return_user_operational_attributes.adoc", "pd_ds_exclude_attributes.adoc", "pd_ds_spec_global_acis.adoc", "pd_ds_define_acis_non_user_content.adoc", "pd_ds_limit_access_controls_ext_ops.adoc", "pd_ds_tolerance_for_malformed_acis.adoc", "pd_ds_about_privilege_subsystem.adoc", "pd_ds_identify_unsupported_acis.adoc"]
section_ids:
  support-for-macro-acis: Support for macro ACIs
  support-for-the-roledn-bind-rule: Support for the roleDN bind rule
  targeting-operational-attributes: Targeting operational attributes
  example: Example
  example-2: Example
  returning-all-user-and-operational-attributes-in-a-schema-search: Returning all user and operational attributes in a schema search
  about-this-task: About this task
  steps: Steps
  example-3: Example:
  exclude-attributes: Exclude attributes
  about-this-task-2: About this task
  steps-2: Steps
  example-4: Example:
  example-5: Example:
  specification-of-global-acis: Specification of global ACIs
  defining-acis-for-non-user-content: Defining ACIs for non-user content
  limiting-access-to-controls-and-extended-operations: Limiting access to controls and extended operations
  tolerance-for-malformed-aci-values: Tolerance for malformed ACI values
  about-the-privilege-subsystem: About the privilege subsystem
  identifying-unsupported-acis: Identifying unsupported ACIs
---

# Migrating ACIs from Oracle to the PingDirectory server

This section describes the most important differences in access control evaluation between Oracle and the server.

## Support for macro ACIs

Oracle supports macro access control instructions (ACIs), making it possible to define a single ACI that you can use to apply the same access restrictions to multiple branches in the same basic structure.

Macro ACIs are infrequently used and can cause severe performance degradation, so the server does not support them. However, you can achieve the same result by creating the same ACIs in each branch.

## Support for the roleDN bind rule

Oracle roles are a proprietary, non-standard grouping mechanism that provide little value over standard grouping mechanisms.

The server does not support Oracle Directory Server Enterprise Edition (DSEE) roles and does not support the use of the `roleDN` ACI bind rule. However, you can achieve the same behavior by converting the DSEE roles to standard groups and using the `groupDN` ACI bind rule.

## Targeting operational attributes

The Oracle access control model doesn't differentiate between user attributes and operational attributes.

In the Oracle access control model, using `targetattr="*"` automatically targets both user and operational attributes. Using an exclusion list like `targetattr!="userPassword"` automatically targets all operational attributes in addition to all user attributes except `userPassword`. This presents several significant security holes here users are unintentionally given access to operational attributes. In some cases, it could allow users to exempt themselves from password policy restrictions.

The server treats operational attributes differently from user attributes and never automatically includes operational attributes. For example, `targetattr="*"` targets all user attributes but no operational attributes, and `targetattr!="userPassword"` targets all user attributes except `userPassword` but no operational attributes.

You can target specific operational attributes by including the names in the list, such as `targetattr="creatorsName||modifiersName"`. You can target all operational attributes by using the `"+"` character. For example, `targetattr="+"` targets all operational attributes but no user attributes, and `targetattr="*||+"` targets all user and operational attributes.

### Example

The following example searches for all immediate children of `ou=People,dc=example,dc=com`. The attributes returned are restricted to `sn`, `givenName`, and all operational attributes.

```
ldapsearch --bindDN uid=admin,dc=example,dc=com --bindPassword password \
     --baseDN ou=People,dc=example,dc=com --searchScope one '(objectclass=*)' \
     sn givenName "+"
```

### Example

You can use compound filters to search for a subset of the entries in the `ou=People,dc=example,dc=com` subtree. The following example limits the returned entry amount to 200, and the server will spend no more than 5 seconds processing the request.

```
ldapsearch --bindDN uid=admin,dc=example,dc=com --bindPassword password \
     --baseDN ou=People,dc=example,dc=com --searchScope sub --sizeLimit 200 \
     --timeLimit 5 "(&(sn<=Doe)(employeeNumber<=1000))" ds-entry-unique-id \
     entryUUID
```

### Returning all user and operational attributes in a schema search

Specify `"*"` in a search attribute list to represent all user attributes. Specifying `"+"` retrieves all operational attributes.

#### About this task

The following standards are used in PingDirectory as part of the LDAP specification.

| Standard                                                  | Overview                                                           |
| --------------------------------------------------------- | ------------------------------------------------------------------ |
| [RFC 3673](https://datatracker.ietf.org/doc/html/rfc3673) | Describes the use of `"+"` to represent all operational attributes |
| [RFC 4511](https://datatracker.ietf.org/doc/html/rfc4511) | Describes the use of `"*"` to represent all user attributes        |

#### Steps

* To search the `cn=schema` entry and return all user and operational attributes, run `ldapsearch`.

  ##### Example:

  ```
  bin/ldapsearch --baseDN cn=schema --searchScope base "(objectclass=*)" "*" "+"
  ```

### Exclude attributes

The server accepts syntax, in addition to the [RFC 3673](https://tools.ietf.org/html/rfc3673), [RFC 4511](https://tools.ietf.org/html/rfc4511), and [RFC 4529](https://tools.ietf.org/html/rfc4529) standards, that allows you to exclude attributes from search results.

#### About this task

To exclude an attribute from the search results in PingDirectory:

#### Steps

* Prefix the attribute name with either `"^"` or `"!"`

  ##### Example:

  The following example returns organizational units (OUs) that are part of the object class `group` in Colorado with the exception of OUs in Denver.

  ```
  (&(objectClass=group)(&(ou:dn:=Colorado)(!(ou:dn:=Denver))))
  ```

  ##### Example:

  The following example returns all users that aren't `device`.

  ```
  (&(objectClass=user)(!(objectClass=device)))
  ```

  |   |                                                                                                                       |
  | - | --------------------------------------------------------------------------------------------------------------------- |
  |   | To exclude all attributes associated with an object class, prefix the object class name with either `"^@"` or `"!@"`. |

## Specification of global ACIs

Both Oracle Directory Server Enterprise Edition (DSEE) and the server support global ACIs, which you can use to define ACIs that apply throughout the server.

In servers with multiple naming contexts, this feature allows you to define a rule once as a global ACI rather than maintaining an identical rule in each naming context.

In DSEE, global ACIs are created by modifying the root DSA-specific entry (DSE) to add values of the `aci` attribute. In the server, you manage global ACIs with `dsconfig` referenced in the `global-aci` property of the access control handler.

## Defining ACIs for non-user content

In Oracle Directory Server Enterprise Edition (DSEE), you can write to the following backends to define ACIs:

* Configuration

* Monitor

* Changelog

* Tasks

In the server, you should define access control for private backends as global ACIs, such as the following backends:

* Configuration

* Monitor

* Schema

* Changelog

* Tasks

* Encryption settings

* Backups

* Alerts

## Limiting access to controls and extended operations

Oracle Directory Server Enterprise Edition (DSEE) provides limited support for restricting access to controls and extended operations.

To the extent that you can control access to controls and extended operations with access control instructions (ACIs), DSEE defines entries with a distinguished name (DN), such as `oid={oid},cn=features,cn=config`, where `{oid}` is the OID of the associated control or extended operation. For example, the following DSEE entry defines ACIs for the persistent search control.

```
oid=2.16.840.1.113730.3.4.3,cn=features,cn=config
```

In the server, you can use the `targetcontrol` keyword to define ACIs that grant or deny access to controls. You can use the `extop` keyword to define ACIs that grant or deny access to extended operation requests.

## Tolerance for malformed ACI values

If the server is running with less than the intended set of access control instructions (ACIs), it might prevent access to data that should be allowed or grant access to data that should be restricted. In Oracle Directory Server Enterprise Edition (DSEE), if the server encounters a malformed access control rule (ACR), it ignores the rule. This can cause the server to run with less than the intended set of ACIs. To guard against this, the server is more strict about the ACRs that it accepts.

When performing an LDIF import, the server rejects any entry containing a malformed or unsupported ACR. The server also rejects any `add` or `modify` request that attempts to create an invalid ACI.

In the unlikely event that a malformed ACI is accepted into the data, the server immediately places itself in lockdown mode. In lockdown mode, the server terminates connections and rejects requests from users without the `lockdown-mode` privilege. Lockdown mode allows an administrator to correct the problem without risking exposure to user data.

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | To review any rejected ACIs, run the `import-ldif` tool with the `--rejectFile` option. |

## About the privilege subsystem

In Oracle Directory Server Enterprise Edition (DSEE), only the root user is exempt from access control evaluation.

While administrators can create access control instructions (ACIs) that give normal users full access to any content, they can also create ACIs that would make a portion of the data inaccessible to those users. Additionally, some tasks can only be accomplished by the root user and the capabilities assigned to the root user can't be restricted.

The server uses a privilege subsystem to control the capabilities available to various users. Non-root users can be granted limited access to certain administrative capabilities, and restrictions can be enforced on root users. Additionally, certain risky actions require that the requester have certain privileges in addition to the sufficient access control rights to process the operation.

These risky actions include:

* Interacting with the server configuration

* Changing another user's password

* Impersonating another user

* Shutting down and restarting the server

## Identifying unsupported ACIs

To determine whether access control instructions (ACIs) are suitable for use, the server provides a `validate-acis` tool that you can use to examine content in an LDIF file or data in another directory server, such as an Oracle Directory Server Enterprise Edition (DSEE) instance.

When migrating data from a DSEE deployment into a server instance, use the `validate-acis` tool to determine whether ACIs contained in the data are acceptable. If any problems exist, update the data to redefine the ACIs so they are suitable for use in the server.

For more information, see [Validating ACIs before migrating data](pd_ds_validate_acis_before_mig_data.html).

---

---
title: Mock access token validator
description: A mock access token validator is a special access token validator type for development or testing purposes.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_mock_access_token_validator
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_mock_access_token_validator.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
section_ids:
  sample-configuration: Sample configuration
---

# Mock access token validator

A mock access token validator is a special access token validator type for development or testing purposes.

A mock access token validator accepts arbitrary tokens without validating whether a trusted source issued them. This allows you to make bearer token-authenticated requests without first setting up an authorization server.

Mock access tokens are formatted as plain-text JSON objects using standard JSON web token (JWT) claims.

Always provide the boolean `active` claim when creating a mock token. If this value is `true`, the token is accepted. If this value is `false`, the token is rejected.

If the `sub` claim is provided, a token owner lookup populates the `TokenOwner` policy request attribute as with the other access token validator types.

The following example cURL command shows a mock access token in an HTTP request.

```shell
curl -k -X GET https://localhost:1443/directory/v1/Me -H 'Authorization: Bearer {"active": true, "sub":"user.1", "scope":"email profile", "client_id":"client1"}'
```

|   |                                                                                                                                                |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Never use mock access token validators in a production environment because they do not verify whether a trusted source issued an access token. |

## Sample configuration

The configuration for a mock access token validator resembles the configuration for a JWT access token validator. However, the JSON web signature (JWS) signatures require no configuration because mock tokens are not authenticated.

```
# Create an identity mapper that expects the token subject to be a uid
dsconfig create-identity-mapper \
  --validator-name "User ID Identity Mapper" \
  --type exact-match \
  --set enabled:true \
  --set match-attribute:uid \
  --set match-base-dn:ou=people,dc=example,dc=com

# Create the Access Token Validator
dsconfig create-access-token-validator \
  --validator-name "Mock Access Token Validator" \
  --type mock --set enabled:true \
  --set evaluation-order-index:9999 \
  --set "identity-mapper:User ID Identity Mapper"
```

Learn more about the configuration options for a [mock access token validator](https://docs.ping.directory/PingDirectory/latest/config-guide/mock-access-token-validator.html).

---

---
title: Overview of access control
description: The access control model uses access control instructions (ACIs) to determine what a user or a group of users can do with a set of entries, down to the attribute level.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_overview_access_control
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_overview_access_control.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 12, 2024
---

# Overview of access control

The access control model uses access control instructions (ACIs) to determine what a user or a group of users can do with a set of entries, down to the attribute level.

The ACIs are stored in the `aci` operational attribute. The operational attribute can appear on any entry and affects the entry or any subentries within that branch of the directory information tree (DIT).

Access control instructions specify four items:

* Resources

  Resources are the targeted items or objects that specifies the set of entries and operations to which the access control instruction applies. For example, you can specify access to certain attributes, such as the `cn` or `userPassword` password.

* Name

  Name is the descriptive label for each ACI. Typically, you have multiple ACIs for a given branch of your DIT. The access control name helps describe its purpose. For example, you can configure an ACI labeled "ACI to grant full access to administrators."

* Clients

  Clients are the users or entities to which you grant or deny access. You can specify individual users or groups of users using an LDAP URL. For example, you can specify a group of administrators using the LDAP URL: `groupdn="ldap:///cn=admins,ou=groups,dc=example,dc=com."`

* Rights

  Rights are permissions granted to users or client applications. You can grant or deny access to certain branches or operations. For example, you can grant `read` or `write` permission to a `telephoneNumber` attribute.

---

---
title: Restricting proxied authorization for specific users
description: Use the following example scenario with proxied users to restrict proxied authorization.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_restrict_proxied_authn_users
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_restrict_proxied_authn_users.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: May 10, 2024
section_ids:
  about-this-task: About this task
  steps: Steps
  example: Example:
  example-2: Example:
  example-3: Example:
  example-4: Example:
  example-5: Example:
  example-6: Example:
  example-7: Example:
  example-8: Example:
  example-9: Example:
  result: Result:
  example-10: Example:
  result-2: Result:
---

# Restricting proxied authorization for specific users

Use the following example scenario with proxied users to restrict proxied authorization.

## About this task

To illustrate how the proxied authorization operational attributes work, set up a simple example where two LDAP clients, `uid=clientApp1` and `uid=clientApp2`, can freely proxy two administrator accounts, `uid=admin1` and `uid=admin2`. Add the `ds-auth-may-proxy-as-*` and `ds-auth-is-proxyable-*` attributes to these entries to restrict how each account can use proxied authorization.

For example, the two client applications can continue to proxy the `uid=admin1` account but the `uid=admin2` account are no longer able to be used as a proxied entry.

![A flowchart showing an example configuration of restricting proxied authorization for specific users. In the first configuration, both client apps can proxy as either of the admins to perform operations. In the second configuration, both client apps must proxy as the first admin to perform operations.](_images/hyl1689877195250.jpg)Proxy Users Example Scenario

## Steps

1. Set up two user entries, `uid=clientApp1`and `uid=clientApp2`, with the `proxied-auth` privilege assigned to them.

   The user entries will proxy as the `uid=admin1` and `uid=admin2` accounts to access the `ou=People,dc=example,dc=com` subtree.

   1. Open a text editor and create an LDIF file.

   2. Add the file using the `ldapmodify` tool.

      ### Example:

      |   |                                                                                                                      |
      | - | -------------------------------------------------------------------------------------------------------------------- |
      |   | In this example, `…` indicates that other attributes present in the entry are not included for readability purposes. |

      ```
      dn: uid=clientApp1,ou=Applications,dc=example,dc=com
      objectClass: top
      ...
      ds-privilege-name: proxied-auth

      dn: uid=clientApp2,ou=Applications,dc=example,dc=com
      objectClass: top
      ...
      ds-privilege-name: proxied-auth
      ```

2. Assign the access control instruction (ACI) for each client application to the subtree, `ou=People,dc=example,dc=com`.

   |   |                                                                                                              |
   | - | ------------------------------------------------------------------------------------------------------------ |
   |   | ACIs should be on one line of text. The following example displays ACIs over multiple lines for readability. |

   ### Example:

   ```
   dn: ou=People,dc=example,dc=com
   aci: (version 3.0; acl "People Proxy Access"; allow(proxy)
          userdn="ldap:///uid=clientApp1,ou=Applications,dc=example,dc=com";)
   aci: (version 3.0; acl "People Proxy Access"; allow(proxy)
          userdn="ldap:///uid=clientApp2,ou=Applications,dc=example,dc=com";)
   ```

3. Run a search for each entry.

   ### Example:

   In this example, assume that there are two admin accounts, `admin1` and `admin2`, that have full access rights to user attributes. You should be able to proxy as the `uid=admin1` and `uid=admin2` entries to access the subtree for both clients.

   ```shell
   $ bin/ldapsearch --port 1389 \
     --bindDN "uid=clientApp1,ou=Applications,dc=example,dc=com" \
     --bindPassword password \
     --proxyAs "dn:uid=admin1,dc=example,dc=com" \
     --baseDN ou=People,dc=example,dc=com \
     "(objectclass=*)"

   $ bin/ldapsearch --port 1389 \
     --bindDN "uid=clientApp2,ou=Applications,dc=example,dc=com" \
     --bindPassword password \
     --proxyAs "dn:uid=admin2,dc=example,dc=com" \
     --baseDN ou=People,dc=example,dc=com \
     "(objectclass=*)"
   ```

4. Limit the proxied authorization capabilities for each client application.

   In the following example, the `ds-auth-may-proxy-as` attribute specifies that `uid=clientApp1` can proxy as the `uid=admin1` entry.

   1. Open a text editor and create the following LDIF file.

   2. Update the `uid=clientApp1` entry to add the `ds-auth-may-proxy-as` attribute.

      |   |                                         |
      | - | --------------------------------------- |
      |   | `ds-auth-may-proxy-as` is multi-valued. |

   3. Save the file and add it using `ldapmodify`.

      ### Example:

      ```
      dn: uid=clientApp1,ou=Applications,dc=example,dc=com
      changetype: modify
      add: ds-auth-may-proxy-as
      ds-auth-may-proxy-as: uid=admin1,dc=example,dc=com
      ```

5. Repeat the previous step for the `uid=clientApp2` entry, but specify the `ds-auth-may-proxy-as-url` attribute.

   The client entry can proxy as any distinguished name (DN) that matches the LDAP URL.

   ### Example:

   ```
   dn: uid=clientApp2,ou=Applications,dc=example,dc=com
   changetype: modify
   add: ds-auth-may-proxy-as-url
   ds-auth-may-proxy-as-url: ldap:///dc=example,dc=com??sub?(uid=admin*)
   ```

6. To illustrate the `ds-auth-proxyable-by-group` attribute, create a group of client applications that has `uid=clientApp1` and `uid=clientApp2` as its `uniquemembers`.

   ### Example:

   This example sets up a static group using the `groupOfUniqueNames` object class.

   ```
   dn: ou=Groups,dc=example,dc=com
   objectClass: top
   objectClass: organizationalunit
   ou: groups

   dn: cn=Client Applications,ou=Groups,dc=example,dc=com
   objectClass: top
   objectClass: groupOfUniqueNames
   cn: Client Applications
   ou: groups
   uniquemember: uid=clientApp1,ou=Applications,dc=example,dc=com
   uniquemember: uid=clientApp2,ou=Applications,dc=example,dc=com
   ```

7. Update the `uid=admin1` entry to provide the DN that it can be proxied as.

   1. Open a text editor and create the following LDIF file.

   2. Use the `ds-auth-is-proxyable` to make the `uid=admin1` a required proxyable entry, meaning that it can only be accessed by some form of proxied authorization.

   3. Use the `ds-auth-is-proxyable-by` attribute to specify each DN that can proxy as `uid=admin1`.

   4. Save the LDIF file and add it using `ldapmodify`.

      ### Example:

      ```
      dn: uid=admin1,dc=example,dc=com
      changetype: modify
      add: ds-auth-is-proxyable
      ds-auth-is-proxyable: required
      -
      add: ds-auth-is-proxyable-by
      ds-auth-is-proxyable-by: ou=clientApp1,ou=Applications,dc=example,dc=com
      ds-auth-is-proxyable-by: ou=clientApp2,ou=Applications,dc=example,dc=com
      -
      add: ds-auth-is-proxyable-by-group
      ds-auth-is-proxyable-by-group: cn=Client Applications,ou=Groups,dc=example,dc=com
      -
      add: ds-auth-is-proxyable-by-url
      ds-auth-is-proxyable-by-url: ldap:///ou=Applications,dc=example,dc=com??sub?(uid=clientApp*)
      ```

      |   |                                                                                                                                                                                    |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The example includes all three types of `ds-auth-is-proxable-by-*` attributes as an illustration, but only one type of attribute is necessary if they all target the same entries. |

8. Prohibit proxying for the `uid=admin2` entry.

   1. Open a text editor and create the following LDIF file.

   2. Set the `ds-auth-is-proxyable` attribute to `prohibited`.

   3. Save the LDIF file and add it using `ldapmodify`.

      ### Example:

      ```
      dn: uid=admin2,dc=example,dc=com
      changetype: modify
      add: ds-auth-is-proxyable
      ds-auth-is-proxyable: prohibited
      ```

9. Run a search using the proxied account.

   1. To return a successful operation, run a search with `uid=clientApp1` or `uid=clientApp2` that proxies as `uid=admin1`.

   2. To return an unsuccessful operation, run a search for `uid=clientApp1` that proxies as `uid=admin2`.

      ### Example:

      ```shell
      $ bin/ldapsearch --port 1389 \
        --bindDN "uid=clientApp1,ou=Applications,dc=example,dc=com" \
        --bindPassword password \
        --proxyAs "dn:uid=admin2,dc=example,dc=com" \
        --baseDN ou=People,dc=example,dc=com \
        "(objectclass=*)"
      ```

      ### Result:

      The operation is unsuccessful because `uid=admin2` does not match the list of potential entries that can be proxied. The `ds-auth-may-proxy-as-*` attributes specify that the client can only proxy as `uid=admin1`.

      ```
      One of the operational attributes (ds-auth-may-proxy-as,
      ds-auth-may-proxy-as-group, ds-auth-may-proxy-as-url) in user entry
      'uid=clientApp1,ou=Applications,dc=example,dc=com' does not allow
      that user to be proxied as user 'uid=admin2,dc=example,dc=com'

      Result Code: 123 (Authorization Denied)

      Diagnostic Message: One of the operational attributes (ds-auth-may-proxy-as,
      ds-auth-may-proxy-as-group, ds-auth-may-proxy-as-url) in user entry
      'uid=clientApp1,ou=Applications,dc=example,dc=com' does not allow that
      user to be proxied as user 'uid=admin2,dc=example,dc=com'
      ```

10. Run another search using `uid=clientApp2`, which attempts to proxy as `uid=admin2`.

    ### Example:

    ```shell
    $ bin/ldapsearch --port 1389 \
      --bindDN "uid=clientApp2,ou=Applications,dc=example,dc=com" \
      --bindPassword password \
      --proxyAs "dn:uid=admin2,dc=example,dc=com" \
      --baseDN ou=People,dc=example,dc=com \
      "(objectclass=*)"
    ```

    ### Result:

    The operation is unsuccessful because the `ds-auth-is-proxyable:prohibited` operational attribute states that `uid=admin2` is not available for proxied authorization.

    ```
    The 'ds-auth-is-proxyable' operational attribute
    in user entry 'uid=admin2,dc=example,dc=com' indicates that
    user may not be accessed via proxied authorization

    Result Code: 123 (Authorization Denied)

    Diagnostic Message: The 'ds-auth-is-proxyable' operational
    attribute in user entry 'uid=admin2,dc=example,dc=com' indicates
    that user may not be accessed via proxied authorization
    ```

---

---
title: Restricting proxy users
description: The PingDirectory server provides a set of operational attributes that restrict the proxied authorization capabilities of a client application and its proxyable target entry.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_restrict_proxy_users
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_restrict_proxy_users.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
page_aliases: ["pd_ds_ds_auth_may_proxy_as_op_attribute.adoc", "pd_ds_ds_auth_is_proxyable_op_attribute.adoc"]
section_ids:
  about-the-ds-auth-may-proxy-as-operational-attributes: About the ds-auth-may-proxy-as-* operational attributes
  about-the-ds-auth-is-proxyable-operational-attributes: About the ds-auth-is-proxyable-* operational attributes
---

# Restricting proxy users

The PingDirectory server provides a set of operational attributes that restrict the proxied authorization capabilities of a client application and its proxyable target entry.

When present in an entry, the PingDirectory server evaluates each operational attribute together to form a whitelist of potential users that can be proxied. If none of those attributes are present, the user can potentially proxy as anyone.

The PingDirectory server supports a two-tier provision system that can restrict specific users for proxied authorization:

* The first tier is a set of `ds-auth-may-proxy-as-*` operational attributes on the client entry that binds to the server and carries out operations under the identity of another user.

* The second tier is a set of `ds-auth-is-proxyable-*` operational attributes on the user entry that defines whether access is allowed, prohibited, or required through proxied authorization. If proxied authorization is allowed or required, the attributes define which client entries can proxy as the user.

![A flowchart showing the process of proxying operational attributes. The client application proxies as uid=admin to perform operations.](_images/pej1689876400281.jpg)Proxying operational attributes

For example, the following command demonstrates the client application `uid=clientApp` requesting to search the `ou=People,dc=example,dc=com` branch as the user `uid=admin`.

```
ldapsearch --bindDN uid=clientApp,dc=example,dc=com \
--bindPassword password \
--proxyAs uid=admin,dc=example,dc=com \
--baseDN ou=People,dc=example,dc=com \
"(object-class=*)
```

At bind, the PingDirectory server evaluates the list of users in the `uid=clientApp` entry based on the presence of any `ds-auth-may-proxy-as-*` attributes.

In the previous figure, the `uid=clientApp` entry has a `ds-auth-may-proxy-as` attribute with a value of `uid=admin`, meaning the client app user can proxy only as the `uid=admin` account.

Next, the server confirms that `uid=admin` is in the list of proxyable users and then evaluates the `ds-auth-is-proxyable-*` attributes present in the `uid=admin` entry. These attributes determine the list of restricted users that either are allowed, prohibited, or required to proxy as the `uid=admin` entry. In this case, the `uid=admin` entry has the `ds-auth-is-proxyable` attribute with a value of `required`, meaning the entry can only be accessed by means of proxied authorization.

The `uid=admin` entry also has the `ds-auth-is-proxyable-by` attribute with a value of `uid=clientApp`, meaning it can only be requested by the `uid=clientApp` entry. When both sets of attributes have been satisfied, the `uid=clientApp` can bind to the server as the authenticated user.

Next, the PingDirectory server performs access control instruction (ACI) evaluation on the branch and determines if the requested user has access rights to the branch. If the `uid=clientApp` entry can access the branch, the search request is processed.

## About the ds-auth-may-proxy-as-\* operational attributes

The PingDirectory server first evaluates the list of potential users that can be proxied for the authenticated user depending on the presence of the `ds-auth-may-*` operational attributes in the entry.

These operational attributes are multi-valued and are evaluated together if all are present in an entry:

* `ds-auth-may-proxy-as`

  Specifies the user distinguished names (DNs) that the associated user can proxy as. For example, you can specify in the `uid=clientApp` entry that it can proxy operations as `uid=admin` and `uid=agent1`.

  ```
  dn: uid=clientApp,ou=Applications,dc=example,dc=com
  objectClass: top
  ...
  ds-privilege-name: proxied-auth
  ds-auth-may-proxy-as: uid=admin,dc=example,dc=com
  ds-auth-may-proxy-as: uid=agent1,ou=admins,dc=example,dc=com
  ```

* `ds-auth-may-proxy-as-group`

  Specifies the group DNs and its group members that the associated user can proxy as. For example, you can specify that the potential users that the `uid=clientApp` entry can proxy as are those members who are present in the group `cn=Agents,ou=Groups,dc=example,dc=com`. This attribute is multi-valued, so you can specify more than one group. Nested static and dynamic groups are also supported.

  ```
  dn: uid=clientApp,ou=Applications,dc=example,dc=com
  objectClass: top
  ...
  ds-privilege-name: proxied-auth
  ds-auth-may-proxy-as-group: cn=Agents,ou=Groups,dc=example,dc=com
  ```

* `ds-auth-may-proxy-as-url`

  Specifies the DNs that are returned based on the criteria defined in an LDAP URL that the associated user can proxy as. For example, the attribute specifies that the client can proxy as those entries that match the criteria in the LDAP URL. This attribute is multi-valued, so you can specify more than one LDAP URL.

  ```
  dn: uid=clientApp,ou=Applications,dc=example,dc=com
  objectClass: top
  ...
  ds-privilege-name: proxied-auth
  ds-auth-may-proxy-as-url: ldap:///ou=People,dc=example,dc=com??sub?(l=austin)
  ```

## About the ds-auth-is-proxyable-\* operational attributes

After the PingDirectory server evaluates the list of users that the authenticated user can proxy as, the server checks to see if the requested authorized user is in the list.

If the requested authorized user is present in the list, then the server continues processing the proxable attributes in the entry. If the requested authorized user is not present in the list, the bind fails.

The operational attributes on the proxying entry are as follows:

* `ds-auth-is-proxyable`

  Specifies whether the entry is proxyable or not. Possible values are:

  * `allowed`

    Operations can be proxied as this user.

  * `prohibited`

    Operations can't be proxied as this user.

  * `required`

    The account cannot authenticate directly but can only be accessed by some form of proxied authorization.

* `ds-auth-is-proxyable-as`

  Specifies any users allowed to use this entry as a target of proxied authorization.

* `ds-auth-is-proxyable-as-group`

  Specifies any groups allowed to use this entry as a target of proxied authorization. Nested static and dynamic groups are also supported.

* `ds-auth-is-proxyable-as-url`

  Specifies the LDAP URLs that are used to determine any users that are allowed to use this entry as a target of proxied authorization.

---

---
title: Summary of access control keywords
description: This section provides an overview of the supported keywords in the server access control implementation.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_summary_access_control_keywords
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_summary_access_control_keywords.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 3, 2024
page_aliases: ["pd_ds_targets.adoc", "pd_ds_permissions.adoc", "pd_ds_bind_rules.adoc"]
section_ids:
  targets: Targets
  permissions: Permissions
  bind-rules: Bind rules
---

# Summary of access control keywords

This section provides an overview of the supported keywords in the server access control implementation.

## Targets

A target expression specifies the set of entries and attributes to which an access control rule applies.

A target expression has three components:

```
(keyword[=||!=]expression)
```

* Keyword

  The keyword specifies the type of target element.

* Expression

  The expression specifies the items that are targeted by the access control rule.

* Operator

  The operator is either equal, `=`, or not-equal, `!=`.

  |   |                                                                                         |
  | - | --------------------------------------------------------------------------------------- |
  |   | You cannot use the `!=` operator with the `targattrfilters` and `targetscope` keywords. |

You can use the following keywords in the target portion of ACIs:

**Summary of Access Control Target Keywords**

| Target Keyword    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Wildcards |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `extop`           | Specifies the OIDs for any extended operations to which the access control rule should apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No        |
| `requestcriteria` | Determines whether an access control rule applies to an operation based on whether that operation matches a given request criteria definition.If present in an access control rule, the operator must be either "=" or "!=". The value must be enclosed in quotation marks and it must be the name or full DN of the configuration object that defines the desired request criteria.For example, let's say that you want to allow members of the `cn=Sales Administrators,ou=Groups,dc=example,dc=com` group to be able to read from and write to the entries for the users that are members of the `cn=Sales Employees,ou=Groups,dc=example,dc=com` group. To do this, you must first create a request criteria object that will match entries for users in the `cn=Sales Employees,ou=Groups,dc=example,dc=com` group. You can do this with the following configuration change:```
dsconfig create-request-criteria \
     --criteria-name "Requests Targeting Sales Employees" \
     --type simple \
     --set "any-included-target-entry-group-dn:cn=Sales Employees,ou=Groups,dc=example,dc=com"
```With that request criteria defined, you can use a modification like the following to create the corresponding access control rule:```
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr="*")(requestcriteria="Requests Targeting Sales
  Employees")(version 3.0; acl "Allow sales administrators to manage
  sales employees"; allow (read,search,compare,write)
  groupdn="ldap:///cn=Sales Administrators,ou=Groups,dc=example,dc=com";)
``` |           |
| `target`          | Specifies the set of entries, identified using LDAP URLs, to which the access control rule applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Yes       |
| `targattrfilters` | Identifies specific attribute values based on filters that can be added to or removed from entries to which the access control rule applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Yes       |
| `targetattr`      | Specifies the set of attributes to which the access control rule should apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes       |
| `targetcontrol`   | Specifies the OIDs for any request controls to which the access control rule should apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No        |
| `targetfilter`    | Specifies one or more search filters that can be used to indicate the set of entries to which the access control should apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Yes       |
| `targetscope`     | Specifies the scope of entries, relative to the defined target entries or the entry containing the ACI if there is no target, to which the access control rule should apply.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No        |

|   |                                                                                           |
| - | ----------------------------------------------------------------------------------------- |
|   | Learn more about target keywords in [Working with targets](pd_ds_work_with_targets.html). |

## Permissions

Permissions indicate the types of operations to which an access control rule could apply.

You can specify if the user or group of users are allowed or not allowed to carry out a specific operation. For example, you can grant read access to targeted entries using the `allow (read)` permission. You can also deny access to the target entries and attributes using the `deny (read)` permission. You can list multiple permissions as required in the ACI.

```
allow(permission1...,permission2,...permissionN)
```

```
deny(permission1...,permission2,...permissionN)
```

You can use the following keywords in the permissions portion of ACIs:

| Keyword     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `add`       | Indicates that the access control applies to `add` operations. Learn more about [Changing the allow add ACI behavior for entries](../pingdirectory_security_guide/pd_sec_aci_rights.html#allow_add_aci).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `compare`   | Indicates that the access control applies to `compare` operations and to search operations with a base-level scope that targets a single entry.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `delete`    | Indicates that the access control applies to `delete` operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `export`    | Indicates that the access control applies only to `modify DN` operations in which an entry is moved below a different parent by specifying a new superior distinguished name (DN) in the `modify DN` request. The requestor must have the `export` permission for operations against the entry's original DN. The requestor must have the `import` permission for operations against the entry's new superior DN.For `modify DN` operations that alter the relative distinguished name (RDN) of an entry but keeps it below the same parent, such as renaming the entry, only the `write` permission is required. This is true regardless of whether the entry being renamed is a leaf entry or has subordinate entries. |
| `import`    | See the description for the `export` permission.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `proxy`     | Indicates that the access control rule applies to operations that attempt to use an alternate authorization identity, such as operations that include a proxied authorization request control, an intermediate client request control with an alternate authorization identity, or a client that has authenticated with a Simple Authentication and Security Layer (SASL) mechanism that allows an alternate authorization identify to be specified.                                                                                                                                                                                                                                                                     |
| `read`      | Indicates that the access control rule applies to search result entries returned by the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `search`    | Indicates that the access control rule applies to `search` operations with a non-base scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `selfwrite` | Indicates that the access control rule applies to operations in which a user attempts to add or remove their own DN to the values for an attribute, such as users adding or removing themselves from groups.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `write`     | Indicates that the access control rule applies to `modify` and `modify DN` operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `all`       | An aggregate permission that includes all other permissions except `import`, `export`, and `proxy`. This is equivalent to providing a permission of `add`, `compare`, `delete`, `read`, `search`, `selfwrite`, and `write`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## Bind rules

The bind rules indicate whether an access control rule should apply to a given requester.

The syntax for the target keyword has three components:

* Keyword

  The keyword specifies the type of target element.

* Expression

  The expression specifies the items that are targeted by the access control rule.

* Operator

  The operator is either equal, `=`, or not-equal, `!=`.

You must use the semicolon delimiter symbol, `;`, after the end of the final bind rule.

```
keyword[=||!=]expression;
```

For added access control precision, you can combine multiple bind rules using the Boolean operations `AND`, `OR`, and `NOT`. The standard Boolean rules for evaluation apply:

* Innermost to outer parentheses first

* Left to right expressions

* `NOT` before `AND` or `OR`

For example, an access control instruction (ACI) with the following bind rule targets all users who are not `uid=admin,dc=example,dc=com` and use simple authentication.

```
(userdn!="ldap:///uid=admin,dc=example,dc=com" and authmethod="simple");
```

The following bind rule targets users that are `uid=admin,dc=example,dc=com` and authenticate using Simple Authentication and Security Layer (SASL) EXTERNAL or access the server from a loopback interface.

```
(userdn="ldap:///uid=admin,dc=example,dc=com and (authmethod="SSL" or ip="127.0.0.1"));
```

You can use the following keywords in the bind rule portion of ACIs:

| Bind Rule Keyword    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `authmethod`         | Indicates that the requester's authentication method is taken into account when determining whether the access control rule should apply to an operation. You cannot use wildcards in this expression.Use the syntax `authmethod = method` where *method* is one of the following representations:- `none`

- `simple` indicates that the client is authenticated to the server using a bind DN and password.

- `ssl` indicates that the client is authenticated with an SSL/TLS certificate (for example, via SASL EXTERNAL), and not just over a secure connection to the server.

- `sasl \{sasl_mechanism}` indicates that the client is authenticated to the server using a specified SASL mechanism.The following example allows users who authenticate with an SSL/TLS certificate (for example, using SASL EXTERNAL) to update their own entries.```
aci: (targetattr="*")
(version 3.0; acl "Allow users to update their own entries";
allow (write) (userdn="ldap:///self" and authmethod="ssl");)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `connectioncriteria` | Allows or denies an operation based on whether the client connection matches a given connection criteria definition.If present in an access control rule, the operator must be either "`=`" or "`!=`". The value must be enclosed in quotation marks, and it must be the name or full DN of the configuration object that defines the desired connection criteria.For example, you can use a modification like the following to allow any client matching the "Root Users and Topology Administrators" connection criteria to have full read and write access to entries below `dc=example,dc=com`:```
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr="*")(version 3.0; acl "Full read and write access for
  administrators"; allow (read,search,compare,write)
  connectioncriteria="Root Users and Topology Administrators";)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `dayofweek`          | Indicates that the day of the week is taken into account when determining whether the access control rule should apply to an operation. You cannot use wildcards in this expression.You can separate multiple day of week values by commas. Use the following syntax.```
dayofweek =  day1,  day2, ...
```*day* is one of the following:- `sun`

- `mon`

- `tues`

- `wed`

- `thu`

- `fri`

- `sat`The following example allows users who authenticate on weekdays with an SSL/TLS certificate, such as SASL EXTERNAL, to update their own entries.```
aci: (targetattr="*")
(version 3.0; acl "Allow users to update their own entries";
allow (write) (dayofweek!="sun,sat" and userdn="ldap:///self"
and authmethod="ssl");)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `dns`                | Indicates that the requester's DNS-resolvable host name is taken into account when determining whether the access control rule should apply to an operation. You can use wildcards in this expression.You can separate multiple DNS patterns by commas. Use the following syntax.```
dns =  dns-host-name
```The following example allows users on host name `server.example.com` to update their own entries.```
aci: (targetattr="*")
(version 3.0; acl "Allow users to update their own entries";
allow (write) (dns="server.example.com" and userdn="ldap:///self");)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `groupdn`            | Indicates that the requester's group membership is taken into account when determining whether the access control rule should apply to any operation. You cannot use wildcards in this expression.```
groupdn [ = || != ] "ldap:///groupdn [ || ldap:///groupdn ] ..."
```The following example allows users in the managers group to update their own entries.```
aci: (targetattr="*")
(version 3.0; acl "Allow users to update their own entries";
allow (write)
(groupdn="ldap:///cn=managers,ou=groups,dc=example,dc=com");)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `ip`                 | Indicates that the requester's IP address is taken into account when determining whether the access control rule should apply to an operation. You can use wildcards in this expression.You can separate multiple IP address patterns by commas. Use the following syntax.```
ip [ = || != ]  <ipAddressList>
```*ipAddressList* is one of the following:- A specific IPv4 address: 127.0.0.1

- An IPv4 address with wildcards to specify a subnetwork: 127.0.0.\*

- An IPv4 address or subnetwork with subnetwork mask: 123.4.5.0+255.255.255.0

- An IPv4 address range using CIDR notation: 123.4.5.0/24

- An IPv6 address as defined by RFC 2373.The following example allows users on 10.130.10.2 and localhost to update their own entries.```
aci: (targetattr="*")
(version 3.0; acl "Allow users to update their own entries";
allow (write) (ip="10.130.10.2,127.0.0.1" and userdn="ldap:///self");)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `oauthscope`         | Indicates that the scopes associated with any OAuth 2.0 access token presented by a SCIMv2 client is taken into account when determining whether the access control rule applies to an operation.Use the following syntax.```
oauthscope [ = || != ] "<scopeIdentifier>"
```*scopeIdentifier* is one of the following:- The name of a single scope to match. The name will be treated as case-sensitive.

- A substring assertion that contains one or more asterisks as wildcards.

- A single asterisk by itself, which will match any scope.The following example grants all rights to any client that presented an OAuth 2.0 token that is associated with the `scim_admin` scope.```
aci: (targetattr="*")
(version 3.0; acl "Full rights for users with the scim_admin OAuth 2.0 scope";
allow (all) oauthscope="scim_admin";)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `secure`             | Allows or denies an operation based on whether the client is communicating with the server over a secure connection; for example, using LDAPS or StartTLS over LDAP.If present in an access control rule, the operator must be either "`=`" or "`!=`", and the value must be either `"true"` or `"false"` including the quotation marks. With this in mind, the `secure` bind rule takes the following forms:- `secure="true"` indicates that the ACI will apply only if the connection was received over a secure connection.

- `secure="false"` indicates that the ACI will only apply if the connection was received over a non-secure connection.

- `secure!="true"` indicates that the ACI will apply only if the connection was received over a non-secure connection.

- `secure!="false"` indicates that the ACI will apply only if the connection was received over a secure connection.For example, you can use a modification like the following to allow users below `dc=example,dc=com` to update their own passwords over a secure connection:```
dn: dc=example,dc=com
changetype: modify
add: aci
aci: (targetattr="userPassword")(version 3.0; acl "Allow users to update
  their own passwords over a secure connection"; allow (write)
  userdn="ldap:///self" and secure="true";)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `timeofday`          | Indicates that the time of day is taken into account when determining whether the access control rule should apply to an operation. You cannot use wildcards in this expression.Use the following syntax.```
timeofday [ = || != || >= || > || <= || < ]  <time>
```*time* is one of the following:- 4-digit 24-hour time format (0000 to 2359, where the first two digits represent the hour of the day and the last two represent the minute of the hour)

- You cannot use wildcards in this expressionThe following example allows users to update their own entries if the request is received before 12 noon.```
aci: (targetattr="*")
(version 3.0; acl "Allow users who authenticate before noon
to update their own entries";
allow (write) (timeofday<1200 and userdn="ldap:///self"
and authmethod="simple");)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `userattr`           | Indicates that the requester's relation to the value of the specified attribute is taken into account when determining whether the access control rule should apply to an operation.Use the following syntax.```
userattr =  "<attrName># [ <bindType> || <attrValue> ]"
```Where:- *attrName* = name of the attribute for matching

- *bindType*= `USERDN`, `GROUPDN`, `LDAPURL`

- *attrValue* = an attribute value. The *attrVALUE* of the attribute must match on both the bind entry and the target of the ACI.A *bindType* value of `USERDN` indicates that the target attribute should have a value which matches the DN of the authenticated user. A *bindType* value of `GROUPDN` indicates that the target attribute should have a value which matches the DN of a group in which the authenticated user is a member. A *bindType* value of `LDAPURL` indicates that the target attribute should have a value that is an LDAP URL whose criteria matches the entry for the authenticated user.Any value other than `USERDN`, `GROUPDN`, or `LDAPURL` is expected to be present in the target attribute of the authenticated user's entry.The following example allows a manager to change employee's entries. If the bind DN is specified in the manager attribute of the targeted entry, the bind rule is evaluated to `TRUE`.```
aci: (targetattr="*")
(version 3.0; acl "Allow a manager to change employee entries";
allow (write) userattr="manager#USERDN";)
```The following example allows any member of a group to change employee's entries. If the bind DN is a member of the group specified in the `allowEditors` attribute of the targeted entry, the bind rule is evaluated to `TRUE`.```
aci: (targetattr="*")
(version 3.0; acl "Allow allowEditors to change employee entries";
allow (write) userattr="allowEditors#GROUPDN";)
```The following example allows a user's manager to edit that user's entry and any entries below the user's entry up to two levels deep. You can specify up to five levels (`0`, `1`, `2`, `3`, `4`) below the targeted entry, with zero `0` indicating the targeted entry.```
aci: (targetattr="*")
(version 3.0; acl "Allow managers to change employees entries two levels below";
allow (write) userattr="parent[0,1,2].manager#USERDN";)
```The following example allows any member of the engineering department to update any other member of the engineering department at or below the specified ACI.```
aci: (targetattr="*")
(version 3.0; acl "Allow any member of Eng Dept to update any other member of the
enginering department at or below the ACI";
allow (write) userattr="department#ENGINEERING";)
```The following example allows an entry to be updated by any user whose entry matches the criteria defined in the LDAP URL contained in the `allowedEditorCriteria` attribute of the target entry.```
aci: (targetattr="*")
(version 3.0; acl "Allow a user that matches the filter to change entries";
allow (write) userattr="allowedEditorCriteria#LDAPURL";)
``` |
| `userdn`             | Indicates that the user's DN is taken into account when determining whether the access control rule should apply to an operation.Use the following syntax.```
userdn [ = || != ] "ldap:///<value>"  [ || "ldap:///<value>  ..."]
```Where *value* is one of the following representations:- The DN of the target user

- A value of `anyone` to match any client, including unauthenticated clients.

- A value of `all` to match any authenticated client.

- A value of `parent` to match the client authenticated as the user defined in the immediate parent of the target entry.

- A value of `self` to match the client authenticated as the user defined in the target entry.If the value provided is a DN, then that DN can include wildcard characters to define patterns. A single asterisk will match any content within the associated DN component, and two consecutive asterisks can be used to match zero or more DN components.The following example allows users to update their own entries.```
aci: (targetattr="*")
(version 3.0; acl "Allow users to update their own entries";
allow (write) userdn="ldap:///self";)
```                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

---

---
title: Third-party access token validator
description: To create custom access token validators, use the Server SDK. Learn more about the configuration options for a third-party access token validator.
component: pingdirectory
version: 11.1
page_id: pingdirectory:managing_access_control:pd_ds_third_party_access_token_validator
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/managing_access_control/pd_ds_third_party_access_token_validator.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
---

# Third-party access token validator

To create custom access token validators, use the Server SDK. Learn more about the configuration options for a [third-party access token validator](https://docs.ping.directory/PingDirectory/latest/config-guide/third-party-access-token-validator.html).