---
title: Policies over REST
description: You can manage authorization policies over REST at the policies endpoint.
component: pingoneaic-api
page_id: pingoneaic-api:am-authorization:rest-api-authz-policies
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authorization/rest-api-authz-policies.html
keywords: ["Authorization", "Policy", "REST API", "Configuration"]
section_ids:
  policy-resource-objects: Policy resource objects
  environment-conditions: Environment conditions
  subject-conditions: Subject conditions
  access-the-endpoints: Access the endpoints
  rest-api-authz-policies-query: Query policies
  rest-api-authz-policies-read: Read a policy
  rest-api-authz-policies-create: Create a policy
  rest-api-authz-policies-update: Update a policy
  rest-api-authz-policies-delete: Delete a policy
  rest-api-authz-policies-copy-move-policies: Copy and move policies
  rest-api-authz-condition-types: Environment conditions
  rest-api-authz-subject-types: Subject conditions
  rest-api-authz-decision-combiners: Decision combiners
---

# Policies over REST

You can manage authorization policies over REST at the `policies` endpoint.

Policies belong to a [policy set](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/configuring-policy-sets.html).

## Policy resource objects

The policy resources are JSON objects. A policy object can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Policy field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `name`(1)      | A string identifying the policy.This string matches the policy name part of the URL path to the resource.Don't use any of the following characters in policy, policy set, or resource type names:- Double quotes (`"`)

- Plus sign (`+`)

- Comma (`,`)

- Less than (`<`)

- Equals (`=`)

- Greater than (`>`)

- Backslash (`\`)

- Forward slash (`/`)

- Semicolon (`;`)

- Null (`\u0000`)                                                                                                                                                                                                                    |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `actionValues`        | An object where each field is an action name.The [resource type](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/configuring-resource-types.html) of the [policy set](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/configuring-policy-sets.html) governs the available actions.The value for each action name field is a boolean indicating whether to allow the action by default. (Advanced Identity Cloud also accepts `0` for `false` and any non-zero numeric value for `true`.)                                                                                           |
| `active`              | A boolean indicating whether Advanced Identity Cloud considers the policy active for evaluation purposes.Default: `false`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `applicationName`     | A string identifying the policy set that contains the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `condition`           | An optional object specifying the [environment conditions](#environment-conditions) where the policy applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `description`         | A string describing the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `resourceAttributes`  | An optional array of response attribute objects; does not apply to `OAuth2 Scope` resource types.The default implementation returns statically defined attributes and attributes from user profiles. A response attribute object has these fields:- `type`

  The implementation type:

  * `Static` for statically defined attributes

  * `User` for attributes from the user profile

- `propertyName`

  The attribute name.

- `propertyValues`

  * For static attributes, the attribute values.

  * For user attributes, not used; Advanced Identity Cloud determines the values when evaluating the policy. |
| `resources`           | An array of the resource name pattern strings to which the policy applies.The [resource type](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/configuring-resource-types.html) must allow the patterns.                                                                                                                                                                                                                                                                                                                                                                                             |
| `resourceTypeUuid`    | An optional string identifying the resource type that governs the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `subject`             | An optional object specifying the [subject conditions](#subject-conditions) where the policy applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `createdBy`(1)        | A string indicating who created the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `lastModifiedBy`(1)   | A string indicating who last changed the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

(1) Do not change the value of this field.

### Environment conditions

Environment conditions clarify where the policy applies.

Express environment conditions as single conditions or combine them using boolean operators. The following example demonstrates a single environment condition that requires an `access` OAuth 2.0 scope:

```json
{
  "condition": {
    "type": "OAuth2Scope",
    "requiredScopes": ["access"]
  }
}
```

The following example demonstrates a combined environment condition that excludes Saturday, Sunday, and a range of IP addresses:

```json
{
  "type": "NOT",
  "condition": {
    "type": "OR",
    "conditions": [{
      "type": "SimpleTime",
      "startTime": "",
      "endTime": "",
      "startDay": "sat",
      "endDay": "sun",
      "enforcementTimeZone": "US/Mountain"
    }, {
      "type": "IPv4",
      "startIp": "192.168.0.1",
      "endIp": "192.168.0.255",
      "ipRange": [],
      "dnsName": []
    }]
  }
}
```

The boolean operator strings to combine conditions in JSON correspond to these properties in the UI:

* `AND` is All of.

* `OR` is Any of.

* `NOT` is Not.

Use the following environment conditions in your policies:

* `AMIdentityMembership`

  Applies to this array of users and groups.

  ```json
  {
    "type": "AMIdentityMembership",
    "amIdentityName": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  }
  ```

  The ForgeRock Java and web agents do not support the `AMIdentityMembership` environment condition. Use the `Identity` subject condition instead.

* `AuthLevel`

  Requires at least the specified authentication level.

  ```json
  {
    "type": "AuthLevel",
    "authLevel": 2
  }
  ```

* `AuthenticateToRealm`

  Requires authentication to the specified realm.

  ```json
  {
    "type": "AuthenticateToRealm",
    "authenticateToRealm": "alpha"
  }
  ```

* `AuthenticateToService`

  Requires authentication with the specified journey (tree).

  ```json
  {
      "type": "AuthenticateToService",
      "authenticateToService": "PushAuthentication"
  }
  ```

* `IdmUser`

  Lets you query an IDM resource to form the basis of the policy evaluation.

  ```json
  {
      "type": "IdmUser",
      "identityResource": "managed/alpha_user",
      "queryField": "userName",
      "decisionField": "effectiveRoles",
      "comparator": "CONTAINS",
      "value": "manager"
  }
  ```

* `IPv4` or `IPv6`

  Requires a request from the specified IP address range or domain name.

  ```json
  {
    "type": "IPv4",
    "startIp": "127.0.0.1",
    "endIp": "127.0.0.255"
  }
  ```

  Omit `startIp` and `endIp` and use the `dnsName` field to specify an array of domain name strings:

  ```json
  {
    "type": "IPv4",
    "dnsName": ["*.example.com"]
  }
  ```

* `LDAPFilter`

  Requires the LDAP representation of the user's profile matches the specified LDAP search filter.

  ```json
  {
    "type": "LDAPFilter",
    "ldapFilter": "(&(c=US)(preferredLanguage=en-us))"
  }
  ```

* `LEAuthLevel`

  Requires at most the specified authentication level.

  ```json
  {
    "type": "LEAuthLevel",
    "authLevel": 2
  }
  ```

* `OAuth2Scope`

  Requires the specified OAuth 2.0 scopes.

  ```json
  {
    "type": "OAuth2Scope",
    "requiredScopes": ["access"]
  }
  ```

* `ResourceEnvIP`

  Requires a complex condition.

  The following example requires an authentication level of at least 4 for requests from an IP address in `127.168.10.*`:

  ```json
  {
    "type": "ResourceEnvIP",
    "resourceEnvIPConditionValue": ["IF IP=[127.168.10.*] THEN authlevel=4"]
  }
  ```

  Each `resourceEnvIPConditionValue` has one or more `IF...THEN...[ELSE...THEN]` statements.

  When the `IF` statement is true, a true `THEN` statement fulfills the condition.

  The `IF` statement specifies either:

  * An IPv4, IPv6, or hybrid address to match the IP address. The IP address can include wildcards.

  * A `dnsName` to match DNS name. The IP address can be IPv4 or IPv6 format, or a hybrid of the two, and can include wildcard characters.

  | `THEN` parameter | Description                               |
  | ---------------- | ----------------------------------------- |
  | `authlevel`      | The minimum required authentication level |
  | `realm`          | The realm where authentication completed  |
  | `redirectURL`    | The URL the user was redirected from      |
  | `role`           | The role of the authenticated user        |
  | `service`        | The authentication journey                |
  | `user`           | The name of the authenticated user        |

* `Script`

  Lets you customize the policy decision with a script. Reference the script using the script ID.

  ```json
  {
    "type": "Script",
    "scriptId": "9de3eb62-f131-4fac-a294-7bd170fd4acb"
  }
  ```

  Find more information about using a script to evaluate policies in [Scripted policy conditions](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/scripted-policy-condition.html).

* `Session`

  Sets the maximum age of the authenticated session, and whether to terminate old sessions, forcing reauthentication.

  ```json
  {
    "type": "Session",
    "maxSessionTime": "10",
    "terminateSession": false
  }
  ```

* `SessionProperty`

  Require attributes set in the authenticated session.

  ```json
  {
    "type": "SessionProperty",
    "ignoreValueCase": true,
    "properties": {
      "CharSet": ["UTF-8"],
      "clientType": ["genericHTML"]
    }
  }
  ```

* `SimpleTime`

  Set a time range. The `type` is the only required field.

  ```json
  {
    "type": "SimpleTime",
    "startTime": "07:00",
    "endTime": "19:00",
    "startDay": "mon",
    "endDay": "fri",
    "startDate": "2023:01:01",
    "endDate": "2023:12:31",
    "enforcementTimeZone": "GMT+0:00"
  }
  ```

### Subject conditions

Subject conditions specify who the policy targets.

Express subject conditions as single conditions or combine them using boolean operators. The following example of a single subject condition means the policy applies to all authenticated users:

```json
{
  "subject": {
    "type": "AuthenticatedUsers"
  }
}
```

The following example of a combined subject condition means the policy applies to either of two users:

```json
{
  "type": "OR",
  "subjects": [{
    "type": "Identity",
    "subjectValues": ["id=014c54bd-6078-4639-8316-8ce0e7746fa4,ou=user,o=alpha,ou=services,ou=am-config"]
  }, {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  }]
}
```

The boolean operator strings to combine conditions in JSON correspond to these properties in the UI:

* `AND` is All of.

* `OR` is Any of.

* `NOT` is Not.

The `type` field specifies the subject:

* `AuthenticatedUsers`

  Applies to any user that successfully authenticated to Advanced Identity Cloud regardless of the realm.

  To limit this to a specific realm, add an `AuthenticateToRealm` environment condition to the policy.

* `Identity`

  Applies to the specified users or groups.

  The following example means the policy applies to members of the account administrators group:

  ```json
  {
    "type": "Identity",
    "subjectValues": ["id=account-administrators,ou=group,o=alpha,ou=services,ou=am-config"]
  }
  ```

* `JwtClaim`

  Applies based on a claim in a user's JSON web token (JWT).

  ```json
  {
    "type": "JwtClaim",
    "claimName": "sub",
    "claimValue": "1dff18dc-ac57-4388-8127-dff309f80002"
  }
  ```

* `NONE`

  Never applies; Advanced Identity Cloud never evaluates the policy as part of a decision.

## Access the endpoints

The REST calls to manage policies rely on an account with the appropriate privileges:

1. Create a policy administrator.

   In the Advanced Identity Cloud admin console, select Identities > Manage > *Realm Name* Realm - Users > + New *Realm Name* Realm - User and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the policy administrator.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-admins`

   * Members

     The policy administrator whose username you recorded

   * Privileges

     Policy Admin\
     Condition Types Read Access\
     Decision Combiners Read Access\
     Entitlement Rest Access\
     Subject Types Read Access

3. Before making REST calls to manage policies, authenticate as the policy administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <policy-admin-username>' \
   --header 'X-OpenAM-Password: <policy-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<policy-admin-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   Learn more in [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<policy-admin-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Query policies

To list all the policy sets defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_queryFilter=true
{
  "result": [{
    "_id": "myExamplePolicy",
    "_rev": "1669650078159",
    "name": "myExamplePolicy",
    "active": true,
    "description": "",
    "resources": ["*://*:*/*", "*://*:*/*?*"],
    "applicationName": "myPolicySet",
    "actionValues": {
      "GET": true,
      "PUT": true
    },
    "subject": {
      "type": "Identity",
      "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
    },
    "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "lastModifiedDate": "2022-11-28T15:41:18.159Z",
    "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "creationDate": "2022-11-28T15:39:04.82Z"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../crest/query.html) to refine the results.

| Field              | Supported `_queryFilter` operators                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `name`             | Equals (`eq`)                                                                                                      |
| `applicationName`  |                                                                                                                    |
| `description`      |                                                                                                                    |
| `createdBy`        |                                                                                                                    |
| `lastModifiedBy`   |                                                                                                                    |
| `creationDate`     | Equals (`eq`)(1) Greater than or equal to (`ge`) Greater than (`gt`) Less than or equal to (`le`) Less than (`lt`) |
| `lastModifiedDate` |                                                                                                                    |

(1) Do not use regular expression patterns with `eq`.

To list policies that explicitly reference a user or group as part of a subject condition, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies` endpoint with the query string parameters `_queryId=queryByIdentityUid` and `uid=universal-uid`, where *universal-uid* is the universal ID for the user or group.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_queryId=queryByIdentityUid&uid=id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config'
{
  "result": [{
    "_id": "myExamplePolicy",
    "_rev": "1669650078159",
    "name": "myExamplePolicy",
    "active": true,
    "description": "",
    "resources": ["*://*:*/*", "*://*:*/*?*"],
    "applicationName": "myPolicySet",
    "actionValues": {
      "GET": true,
      "PUT": true
    },
    "subject": {
      "type": "Identity",
      "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
    },
    "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "lastModifiedDate": "2022-11-28T15:41:18.159Z",
    "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "creationDate": "2022-11-28T15:39:04.82Z"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

The following caveats apply when querying policies by user or group:

* Advanced Identity Cloud does not evaluate group membership.

  When you specify only groups in the condition, Advanced Identity Cloud does not also return policies for users who are members of the specified groups.

* Advanced Identity Cloud supports only exact matches for users and groups; you cannot use wildcards.

* Advanced Identity Cloud only returns policies with `Identity` subject conditions—​not `AMIdentityMembership` environment conditions.

* Advanced Identity Cloud does not return policies with subject conditions that only contain the user or group in a logical *NOT* operator.

## Read a policy

To read an individual policy in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myExamplePolicy'
{
  "_id": "myExamplePolicy",
  "_rev": "1669650078159",
  "name": "myExamplePolicy",
  "active": true,
  "description": "",
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "GET": true,
    "PUT": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "lastModifiedDate": "2022-11-28T15:41:18.159Z",
  "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "creationDate": "2022-11-28T15:39:04.82Z"
}
```

## Create a policy

To create a policy in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies` endpoint with `_action=create` as the query string parameter and a JSON representation of the policy as the POST data.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--data '{
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": false,
    "GET": true
  },
  "resources": ["https://www.example.com:443/*", "https://www.example.com:443/*?*"],
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "resourceTypeUuid": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/?_action=create'
{
  "_id": "myExamplePolicy",
  "_rev": "1669650078159",
  "name": "myExamplePolicy",
  "active": true,
  "description": "",
  "resources": ["https://www.example.com:443/*", "https://www.example.com:443/*?*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "GET": true,
    "POST": false
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "lastModifiedDate": "2022-11-28T15:41:18.159Z",
  "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "creationDate": "2022-11-28T15:39:04.82Z"
}
```

|   |                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Before testing OAuth 2.0 policies, configure the `OAuth2 Provider` service for the realm to Use Policy Engine for Scope decisions.Learn to [Dynamic OAuth 2.0 authorization](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/oauth2-authorization.html). |

## Update a policy

To update an individual policy in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint with a JSON representation of the updated policy as the PUT data.

```bash
$ curl \
--request PUT \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--header "Content-Type: application/json" \
--data '{
  "_id": "myNewExamplePolicy",
  "_rev": "1669721075177",
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "resources": ["https://www.example.com:443/*?*", "https://www.example.com:443/*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": true,
    "GET": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  }
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myNewExamplePolicy'
{
  "_id": "myNewExamplePolicy",
  "_rev": "1669721293147",
  "name": "myNewExamplePolicy",
  "active": true,
  "description": "Example policy",
  "resources": ["https://www.example.com:443/*?*", "https://www.example.com:443/*"],
  "applicationName": "myPolicySet",
  "actionValues": {
    "POST": true,
    "GET": true
  },
  "subject": {
    "type": "Identity",
    "subjectValues": ["id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config"]
  },
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": "2022-11-29T11:28:13.147Z",
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": "2022-11-29T11:24:35.177Z"
}
```

## Delete a policy

To delete an individual policy in a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/policies/policy-name` endpoint.

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myNewExamplePolicy'
{"_id":"myNewExamplePolicy","_rev":"0"}
```

## Copy and move policies

To copy or move an individual policy, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies/policyName` endpoint. Include the appropriate parameters and POST data.

The appropriate parameters for copying and moving policies take the following into account:

* The realm in the URL is the realm of the policy or policies to copy or to move.

* The policy name in the URL is the name of an individual policy to copy or to move.

* Specify either `_action=copy` or `_action=move` as the query string parameter.

* When moving policies from one realm to another, use a tenant administrator's AM session cookie to authenticate.

  The policy administrator is a member of a realm, and does not have access to change another realm's settings.

The following example copies `myExamplePolicy` from the `alpha` realm to `Copied policy` in the `bravo` realm.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <tenant-admin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "to": {
    "name": "Copied policy",
    "realm": "/bravo",
    "resourceType": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myExamplePolicy?_action=copy'
{
  "name": "Copied policy",
  "...": "..."
}
```

The POST data JSON object for copying and moving individual policies has these fields:

| Outer field | Inner field    | Description                                                                                                                                                             |
| ----------- | -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `to`        | `name`         | The target policy.Required unless you are copying or moving a policy to a different realm, and you want the target policy to have the same name as the original policy. |
|             | `application`  | The target policy set.Required when copying or moving a policy to a different policy set.                                                                               |
|             | `realm`        | The target realm.Required when copying or moving a policy to a different realm.                                                                                         |
|             | `resourceType` | The resource type UUID for the target policy.The resource type must exist in the target realm.Required when copying or moving a policy to a different realm.            |

The following example moves `myExamplePolicy` to `Moved policy` in the same realm. The policy administrator can complete this request because the target is in the same realm.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "to": {
    "name": "Moved policy",
    "realm": "/alpha",
    "resourceType": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/myExamplePolicy?_action=move'
{
  "name": "Moved policy",
  "...": "..."
}
```

To copy or move multiple policies, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/policies` endpoint with the appropriate parameters and POST data.

The following example copies all the policies in `myPolicySet` to the `bravo` realm:

* The target policy set already exists in the `bravo` realm. It allows the same policies as its counterpart in the `alpha` realm.

* The `bravo` realm has resource types matching those in the `alpha` realm.

```bash
$ curl \
--request POST \
--header "<session-cookie-name>: <tenant-admin-tokenId>" \
--header "Accept-API-Version: resource=2.1" \
--header "Content-Type: application/json" \
--data '{
  "from": {
    "application": "myPolicySet"
  },
  "to": {
    "realm": "/bravo",
    "namePostfix": "-copy"
  },
  "resourceTypeMapping": {
    "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "76656a38-5f8e-401b-83aa-4ccb74ce88d2": "76656a38-5f8e-401b-83aa-4ccb74ce88d2"
  }
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies?_action=copy'
[{
  "name": "Moved policy-copy",
  "...": "..."
}]
```

The POST data JSON object for copying and moving multiple policies has these fields:

| Outer field           | Inner field                                   | Description                                                                                                                                                                |
| --------------------- | --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `from`                | `application`                                 | The policy set to copy or move policies from.Required.                                                                                                                     |
| `to`                  | `application`                                 | The target policy set.Required when copying or moving policies to a different policy set.                                                                                  |
|                       | `realm`                                       | The target realm.Required when copying or moving policies to a different realm.                                                                                            |
|                       | `namePostfix`                                 | A string appended to target policy names to prevent clashes.Required.                                                                                                      |
| `resourceTypeMapping` | The UUID(s) of the original resource type(s). | The UUID(s) of the target resource type(s).Each pair of resource types must have the same resource patterns.Required when copying or moving policies to a different realm. |

## Environment conditions

You can read and query [environment condition](#environment-conditions) schema over REST.

The schemas describe the environment condition JSON objects that you include in authorization policies. Each environment condition schema has these fields:

* `title`

  The short name for the environment condition.

* `logical`

  Whether the type is a logical operator or takes a predicate.

* `config`

  The layout of the environment condition object.

Environment conditions have these characteristics:

* Environment conditions are the same for each realm.

* The only environment condition for OAuth 2.0 policies is `Script`. Use scripts to capture the `ClientId` environment attribute.

To list all environment condition schemas, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/conditiontypes` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/conditiontypes?_queryFilter=true'
```

> **Collapse: Display output**
>
> ```json
> {
>   "result": [{
>     "_id": "AMIdentityMembership",
>     "title": "AMIdentityMembership",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "amIdentityName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "AND",
>     "title": "AND",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "conditions": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthLevel",
>     "title": "AuthLevel",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authLevel": {
>           "type": "integer"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthScheme",
>     "title": "AuthScheme",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authScheme": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         },
>         "applicationIdleTimeout": {
>           "type": "integer"
>         },
>         "applicationName": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticateToRealm",
>     "title": "AuthenticateToRealm",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticateToRealm": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticateToService",
>     "title": "AuthenticateToService",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticateToService": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "IPv4",
>     "title": "IPv4",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startIp": {
>           "type": "string"
>         },
>         "endIp": {
>           "type": "string"
>         },
>         "dnsName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "IPv6",
>     "title": "IPv6",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startIp": {
>           "type": "string"
>         },
>         "endIp": {
>           "type": "string"
>         },
>         "dnsName": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "LDAPFilter",
>     "title": "LDAPFilter",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "ldapFilter": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "LEAuthLevel",
>     "title": "LEAuthLevel",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authLevel": {
>           "type": "integer"
>         }
>       }
>     }
>   }, {
>     "_id": "NOT",
>     "title": "NOT",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "condition": {
>           "type": "object",
>           "properties": {}
>         }
>       }
>     }
>   }, {
>     "_id": "OAuth2Scope",
>     "title": "OAuth2Scope",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "requiredScopes": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "OR",
>     "title": "OR",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "conditions": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "Policy",
>     "title": "Policy",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "className": {
>           "type": "string"
>         },
>         "properties": {
>           "type": "object"
>         }
>       }
>     }
>   }, {
>     "_id": "ResourceEnvIP",
>     "title": "ResourceEnvIP",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "resourceEnvIPConditionValue": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "Script",
>     "title": "Script",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "scriptId": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "Session",
>     "title": "Session",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "maxSessionTime": {
>           "type": "number"
>         },
>         "terminateSession": {
>           "type": "boolean",
>           "required": true
>         }
>       }
>     }
>   }, {
>     "_id": "SessionProperty",
>     "title": "SessionProperty",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "ignoreValueCase": {
>           "type": "boolean",
>           "required": true
>         },
>         "properties": {
>           "type": "object"
>         }
>       }
>     }
>   }, {
>     "_id": "SimpleTime",
>     "title": "SimpleTime",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "startTime": {
>           "type": "string"
>         },
>         "endTime": {
>           "type": "string"
>         },
>         "startDay": {
>           "type": "string"
>         },
>         "endDay": {
>           "type": "string"
>         },
>         "startDate": {
>           "type": "string"
>         },
>         "endDate": {
>           "type": "string"
>         },
>         "enforcementTimeZone": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "Transaction",
>     "title": "Transaction",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "authenticationStrategy": {
>           "type": "string"
>         },
>         "strategySpecifier": {
>           "type": "string"
>         }
>       }
>     }
>   }],
>   "resultCount": 20,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": 0
> }
> ```

To read an environment condition schema, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/conditiontypes/condition-type` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/conditiontypes/IPv4'
{
  "_id": "IPv4",
  "_rev": "1669721841603",
  "title": "IPv4",
  "logical": false,
  "config": {
    "type": "object",
    "properties": {
      "startIp": {
        "type": "string"
      },
      "endIp": {
        "type": "string"
      },
      "dnsName": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
```

## Subject conditions

You can read and query [subject condition](#subject-conditions) schema over REST.

The schemas describe the subject condition JSON objects that you include in authorization policies. Each environment condition schema has these fields:

* `title`

  The short name for the subject condition.

* `logical`

  Whether the type is a logical operator or takes a predicate.

* `config`

  The layout of the subject condition object.

Subject conditions are the same for each realm.

To list all subject condition schemas, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/subjecttypes` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/subjecttypes?_queryFilter=true'
```

> **Collapse: Display output**
>
> ```json
> {
>   "result": [{
>     "_id": "AND",
>     "title": "AND",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjects": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "AuthenticatedUsers",
>     "title": "AuthenticatedUsers",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {}
>     }
>   }, {
>     "_id": "Identity",
>     "title": "Identity",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjectValues": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }, {
>     "_id": "JwtClaim",
>     "title": "JwtClaim",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "claimName": {
>           "type": "string"
>         },
>         "claimValue": {
>           "type": "string"
>         }
>       }
>     }
>   }, {
>     "_id": "NONE",
>     "title": "NONE",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {}
>     }
>   }, {
>     "_id": "NOT",
>     "title": "NOT",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subject": {
>           "type": "object",
>           "properties": {}
>         }
>       }
>     }
>   }, {
>     "_id": "OR",
>     "title": "OR",
>     "logical": true,
>     "config": {
>       "type": "object",
>       "properties": {
>         "subjects": {
>           "type": "array"
>         }
>       }
>     }
>   }, {
>     "_id": "Policy",
>     "title": "Policy",
>     "logical": false,
>     "config": {
>       "type": "object",
>       "properties": {
>         "name": {
>           "type": "string"
>         },
>         "className": {
>           "type": "string"
>         },
>         "values": {
>           "type": "array",
>           "items": {
>             "type": "string"
>           }
>         }
>       }
>     }
>   }],
>   "resultCount": 8,
>   "pagedResultsCookie": null,
>   "totalPagedResultsPolicy": "NONE",
>   "totalPagedResults": -1,
>   "remainingPagedResults": 0
> }
> ```

To read a subject condition schema, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/subjecttypes/subject-type` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/subjecttypes/Identity'
{
  "_id": "Identity",
  "_rev": "1669721896953",
  "title": "Identity",
  "logical": false,
  "config": {
    "type": "object",
    "properties": {
      "subjectValues": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    }
  }
}
```

## Decision combiners

Decision combiners describe how to resolve policy decisions when multiple policies apply.

Decision combiners are the same for each realm.

To list all decision combiners, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/decisioncombiners` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0, protocol=2.1" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/decisioncombiners?_queryFilter=true'
{
  "result": [{
    "_id": "DenyOverride",
    "title": "DenyOverride"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

To read a decision combiner, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/decisioncombiners/decision-combiner` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/decisioncombiners/DenyOverride'
{"_id":"DenyOverride","_rev":"1669722054745","title":"DenyOverride"}
```

---

---
title: Policy sets over REST
description: "You can manage policy sets over REST at the applications endpoint. (\"Application\" is the internal name for a policy set.)"
component: pingoneaic-api
page_id: pingoneaic-api:am-authorization:rest-api-authz-applications
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authorization/rest-api-authz-applications.html
keywords: ["Authorization", "Policy", "Resource", "Configuration", "REST API"]
section_ids:
  access-the-endpoint: Access the endpoint
  rest-api-authz-applications-query: Query policy sets
  rest-api-authz-applications-read: Read a policy set
  rest-api-authz-applications-create: Create a policy set
  rest-api-authz-applications-update: Update a policy set
  rest-api-authz-applications-delete: Delete a policy set
---

# Policy sets over REST

You can manage policy sets over REST at the `applications` endpoint. ("Application" is the internal name for a policy set.)

Advanced Identity Cloud stores policy sets as JSON objects. A policy set can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Policy set field      | Description                                                                                                                                                                                                                                                                                                                         |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `name`         | A unique string identifying the policy set.Don't use any of the following characters in policy, policy set, or resource type names:- Double quotes (`"`)

- Plus sign (`+`)

- Comma (`,`)

- Less than (`<`)

- Equals (`=`)

- Greater than (`>`)

- Backslash (`\`)

- Forward slash (`/`)

- Semicolon (`;`)

- Null (`\u0000`) |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                 |
| `actions`             | An object where each field is an action name.The value for each action name field is a boolean indicating whether to allow the action by default.                                                                                                                                                                                   |
| `applicationType`     | A string containing the application type name.Use `"iPlanetAMWebAgentService"`.                                                                                                                                                                                                                                                     |
| `attributeNames`      | An optional array of response attribute name strings restricting what policies in this set can return.                                                                                                                                                                                                                              |
| `conditions`          | An array of environment condition identifier strings defining environment conditions allowed for policies in this set.                                                                                                                                                                                                              |
| `description`         | An optional text string to help identify the policy set.                                                                                                                                                                                                                                                                            |
| `editable`            | A boolean indicating whether you can edit this policy set definition after creation.                                                                                                                                                                                                                                                |
| `entitlementCombiner` | An optional string identifying how Advanced Identity Cloud evaluates multiple policies for a resource.Use `"DenyOverride"`.                                                                                                                                                                                                         |
| `realm`               | A string identifying the realm for this policy set.                                                                                                                                                                                                                                                                                 |
| `resources`           | An array of resource pattern strings for resources governed by policies in this set.                                                                                                                                                                                                                                                |
| `resourceComparator`  | An optional string identifying the fully qualified class name of the implementation to match resources for policies.                                                                                                                                                                                                                |
| `saveIndex`           | An optional string identifying the fully qualified class name of the implementation to save indexes for policies.                                                                                                                                                                                                                   |
| `searchIndex`         | An optional string identifying the fully qualified class name of the implementation to index policies.                                                                                                                                                                                                                              |
| `subjects`            | Array of subject type identifier strings defining subject types allowed for policies in this set.                                                                                                                                                                                                                                   |
| `createdBy`(1)        | A string indicating who created the policy set.                                                                                                                                                                                                                                                                                     |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                      |
| `lastModifiedBy`(1)   | A string indicating who last changed the policy set.                                                                                                                                                                                                                                                                                |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                 |

(1) Do not change the value of this field.

## Access the endpoint

The REST calls to manage policy sets rely on an account with the appropriate privileges:

1. Create a policy set administrator.

   In the Advanced Identity Cloud admin console, select Identities > Manage > *Realm Name* Realm - Users > + New *Realm Name* Realm - User and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the policy set administrator.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group. Create a group with the following settings:

   * Group ID

     `am-policy-set-admins`

   * Members

     The policy set administrator whose username you recorded

   * Privileges

     Policy Admin\
     Application Modify Access\
     Application Read Access

3. Before making REST calls to manage policy sets, authenticate as the policy set administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <policy-set-admin-username>' \
   --header 'X-OpenAM-Password: <policy-set-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<policy-set-admin-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   Learn more in [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<policy-set-admin-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Query policy sets

To list all the policy sets defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/applications` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications?_queryFilter=true'
{
  "result": [{
    "_id": "oauth2Scopes",
    "name": "oauth2Scopes",
    "description": "The built-in Application used by the OAuth2 scope authorization process.",
    "attributeNames": [],
    "createdBy": "id=dsameuser,ou=user,ou=am-config",
    "conditions": ["Script", "AMIdentityMembership", "IPv6", "SimpleTime", "IPv4", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "SessionProperty", "OAuth2Scope", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
    "lastModifiedBy": "id=dsameuser,ou=user,ou=am-config",
    "creationDate": 1578580064992,
    "lastModifiedDate": 1595479030629,
    "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "JwtClaim"],
    "saveIndex": null,
    "searchIndex": null,
    "entitlementCombiner": "DenyOverride",
    "resourceComparator": null,
    "editable": true,
    "applicationType": "iPlanetAMWebAgentService",
    "actions": {
      "GRANT": true
    },
    "resources": ["*://*:*/*", "*://*:*/*?*", "*"],
    "realm": "/alpha"
  }],
  "resultCount": 1,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../crest/query.html) to refine the results.

| Field              | Supported `_queryFilter` operators                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `name`             | Equals (`eq`)                                                                                                      |
| `description`      |                                                                                                                    |
| `createdBy`        |                                                                                                                    |
| `lastModifiedBy`   |                                                                                                                    |
| `creationDate`     | Equals (`eq`)(1) Greater than or equal to (`ge`) Greater than (`gt`) Less than or equal to (`le`) Less than (`lt`) |
| `lastModifiedDate` |                                                                                                                    |

(1) Don't use regular expression patterns with `eq`.

## Read a policy set

To read a specific policy set in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint.

```bash
$ curl \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/oauth2Scopes'
{
  "_id": "oauth2Scopes",
  "_rev": "1595479030629",
  "name": "oauth2Scopes",
  "description": "The built-in Application used by the OAuth2 scope authorization process.",
  "attributeNames": [],
  "createdBy": "id=dsameuser,ou=user,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "SimpleTime", "IPv4", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "SessionProperty", "OAuth2Scope", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=dsameuser,ou=user,ou=am-config",
  "creationDate": 1578580064992,
  "lastModifiedDate": 1595479030629,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "GRANT": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*", "*"],
  "realm": "/alpha"
}
```

## Create a policy set

To create a policy set in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/applications` endpoint with `_action=create` as the query string parameter and a JSON representation of the policy set as the POST data.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "entitlementCombiner": "DenyOverride",
  "attributeNames": [],
  "saveIndex": null,
  "searchIndex": null,
  "resourceComparator": null,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": true,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": true,
    "PATCH": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/?_action=create'
{
  "_id": "samplePolicySet",
  "_rev": "1669134131264",
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "attributeNames": [],
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669134131264,
  "lastModifiedDate": 1669134131264,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": true,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": true,
    "PATCH": true
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}
```

## Update a policy set

To update a specific policy set in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint with a JSON representation of the updated policy set as the PUT data.

```bash
$ curl \
--request PUT \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "entitlementCombiner": "DenyOverride",
  "attributeNames": [],
  "saveIndex": null,
  "searchIndex": null,
  "resourceComparator": null,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": false,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PUT": false,
    "PATCH": false
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/samplePolicySet'
{
  "_id": "samplePolicySet",
  "_rev": "1669134221194",
  "name": "samplePolicySet",
  "description": "Sample policy set",
  "attributeNames": [],
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "conditions": ["Script", "AMIdentityMembership", "IPv6", "IPv4", "SimpleTime", "LEAuthLevel", "LDAPFilter", "AuthScheme", "Session", "AND", "AuthenticateToRealm", "ResourceEnvIP", "Policy", "OAuth2Scope", "SessionProperty", "OR", "Transaction", "NOT", "AuthLevel", "AuthenticateToService"],
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669134131264,
  "lastModifiedDate": 1669134221194,
  "subjects": ["AuthenticatedUsers", "NOT", "Identity", "OR", "AND", "NONE", "Policy", "JwtClaim"],
  "saveIndex": null,
  "searchIndex": null,
  "entitlementCombiner": "DenyOverride",
  "resourceComparator": null,
  "editable": true,
  "applicationType": "iPlanetAMWebAgentService",
  "actions": {
    "HEAD": true,
    "DELETE": false,
    "POST": true,
    "GET": true,
    "OPTIONS": true,
    "PATCH": false,
    "PUT": false
  },
  "resources": ["*://*:*/*", "*://*:*/*?*"],
  "realm": "/alpha"
}
```

## Delete a policy set

To delete a policy set in a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/applications/policy-set-name` endpoint.

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/samplePolicySet'
{"_id":"samplePolicySet","_rev":"0"}
```

You cannot delete a policy set that contains policies. If you attempt to delete the policy set, Advanced Identity Cloud returns an HTTP 409 Conflict status code and a message like the one in the following example:

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <policy-set-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/applications/oauth2Scopes'
{
  "code": 409,
  "reason": "Conflict",
  "message": "Application cannot be altered because policies exist within the Application. Remove all policies from the Application before attempting to delete the Application."
}
```

Remove the policies from the set before you delete it.

---

---
title: Request policy decisions over REST
description: You can request policy decisions from Advanced Identity Cloud by using the REST API. Advanced Identity Cloud evaluates requests based on the context and the policies configured and returns decisions that indicate what actions are allowed or denied, as well as any attributes or advice for the resources specified.
component: pingoneaic-api
page_id: pingoneaic-api:am-authorization:rest-api-authz-policy-decisions
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authorization/rest-api-authz-policy-decisions.html
keywords: ["Authorization", "Policy", "REST API", "Evaluation"]
section_ids:
  access-the-endpoint: Access the endpoint
  rest-api-authz-policy-decision-concrete: Request policy decisions for specific resources
  rest-api-authz-policy-decision-advice: Policy decision advice
  rest-api-authz-policy-decision-subtree: Request policy decisions for a tree of resources
---

# Request policy decisions over REST

You can request policy decisions from Advanced Identity Cloud by using the REST API. Advanced Identity Cloud evaluates requests based on the context and the policies configured and returns decisions that indicate what actions are allowed or denied, as well as any attributes or advice for the resources specified.

|   |                                                   |
| - | ------------------------------------------------- |
|   | This section doesn't apply to OAuth 2.0 policies. |

Use the `/json/realms/root/realms/realm-name/policies` endpoints to request policy evaluation.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/alpha`.

Learn to request decisions for specific resources in [Request policy decisions for specific resources](#rest-api-authz-policy-decision-concrete).

Learn to request decisions for a resource and all resources beneath it in [Request policy decisions for a tree of resources](#rest-api-authz-policy-decision-subtree).

## Access the endpoint

The REST calls to request policy decisions require that the subjects have the appropriate privileges:

1. Create a group that grants the privileges required to request policy decisions.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-policy-evaluators`

   * Members

     Users that will perform policy evaluations

   * Privileges

     Entitlement Rest Access

2. Before making REST calls to evaluate policies, authenticate as the user whose access you want to evaluate:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <subject-username>' \
   --header 'X-OpenAM-Password: <subject-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<subject-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   Learn more in [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<subject-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Request policy decisions for specific resources

To request policy decisions for specific resources, send an HTTP POST request to the `policies` endpoint with the `evaluate` action, for example: `/json/realms/root/realms/alpha/policies?_action=evaluate`.

The payload for the HTTP POST is a JSON object that specifies at least the resources and takes the following form.

```none
{
    "resources": [
        "resource1",
        "resource2",
        ...,
        "resourceN"
    ],
    "application": "The policy set that contains the policies to evaluate against",
    "subject": {
        "ssoToken": "SSO token ID string",
        "jwt": "JSON Web Token string",
        "claims": {
            "key": "value",
            ...
        }
    },
    "environment": {
        "optional key1": [
            "value",
            "another value",
            ...
        ],
        "optional key2": [
            "value",
            "another value",
            ...
        ],
        ...
    }
}
```

The values for the fields shown above are explained below:

* `resources`

  This required field specifies the list of resources for which to return decisions.

  For example, depending on the patterns defined in the policy set, you could request decisions for resource URLs.

  ```json
  {
      "resources": [
          "http://www.example.com/index.html",
          "http://www.example.com/do?action=run"
      ]
  }
  ```

* `application`

  This field holds the name of the policy set, for example, `samplePolicySet`.

  For more on policy sets, refer to [Policy sets over REST](rest-api-authz-applications.html).

* `subject`

  This optional field holds an object that represents the subject.

  If you do not specify the subject, Advanced Identity Cloud uses the SSO token ID of the subject making the request.

  You can specify one or more of the following keys. If you specify multiple keys, the subject can have multiple associated principals, and you can use subject conditions corresponding to any type in the request.

  * `ssoToken`

    The value is the SSO token ID string for the subject, returned for example on successful authentication as described in [Authenticate over REST](../am-authentication/authn-rest.html).

    You can use an OpenID Connect ID token if the client that the token was issued for is authorized to use ID tokens as session tokens. Learn more in [ID tokens as session tokens](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-additional-use-cases.html#idtokens-as-session-tokens).

  * `jwt`

    The value is a JWT string.

  * `claims`

    The value is an object (map) of JWT claims to their values. Any string is permitted, but you must include the `sub` claim.

* `environment`

  This optional field holds a map of keys to lists of values.

  If you don't specify the environment, the default is an empty map.

The example below requests policy decisions for two URL resources. The `<session-cookie-name>` header sets the SSO token for a user who has access to perform the operation.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "Accept-API-Version: resource=2.1" \
--header "<session-cookie-name>: AQIC5..." \
--data '{
    "resources":[
        "http://www.example.com/index.html",
        "http://www.example.com/do?action=run"
    ],
    "application":"iPlanetAMWebAgentService"
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/?_action=evaluate"
[
    {
        "resource":"http://www.example.com/do?action=run",
        "actions":{

        },
        "attributes":{

        },
        "advices":{
            "AuthLevelConditionAdvice":[
                "3"
            ]
        }
    },
    {
        "resource":"http://www.example.com/index.html",
        "actions":{
            "POST":false,
            "GET":true
        },
        "attributes":{
            "cn":[
                "babs"
            ]
        },
        "advices":{

        }
    }
]
```

In the JSON list of decisions returned for each resource, Advanced Identity Cloud includes these fields.

* `resource`

  A resource specified in the request.

  The decisions returned are not guaranteed to be in the same order as the resources were requested.

* `actions`

  A map of action name keys to Boolean values that indicate whether the action is allowed (`true`) or denied (`false`) for the specified resource.

  In the example, for resource `http://www.example.com:80/index.html` HTTP GET is allowed, whereas HTTP POST is denied.

* `attributes`

  A map of attribute names to their values if any response attributes are returned according to applicable policies.

  In the example, the policy that applies to `http://www.example.com:80/index.html` causes the value of the subject's "cn" profile attribute to be returned.

* `advices`

  A map of advice names to their values if any advice is returned according to applicable policies.

  The `advices` field can provide hints regarding what Advanced Identity Cloud needs to take the authorization decision.

  In the example, the policy that applies to `http://www.example.com:80/do?action=run` requests that the subject be authenticated at an authentication level of at least 3.

  ```json
  {
      "advices": {
          "AuthLevelConditionAdvice": [
              "3"
          ]
      }
  }
  ```

  Refer to [Policy decision advice](#rest-api-authz-policy-decision-advice) for details.

You can use the query string parameters `_prettyPrint=true` to make the output easier to read, and `_fields=field-name[,field-name...]` to limit the fields returned in the output.

## Policy decision advice

When Advanced Identity Cloud returns a policy decision, the JSON for the decision can include an "advices" field. This field contains hints for the policy enforcement point.

```json
{
    "advices": {
        "type": [
            "advice"
        ]
    }
}
```

The "advices" returned depend on policy conditions. For more information about policy conditions, refer to [Policies over REST](rest-api-authz-policies.html).

This section shows examples of the different types of policy decision advice and the conditions that cause Advanced Identity Cloud to return the advice.

`AuthLevel` and `LEAuthLevel` condition failures can result in advice showing the expected or maximum possible authentication level. For example, failure against the following condition:

```json
{
    "type": "AuthLevel",
    "authLevel": 2
}
```

Leads to this advice:

```json
{
    "AuthLevelConditionAdvice": [
        "2"
    ]
}
```

An `AuthenticateToRealm` condition failure can result in advice showing the name of the realm to which authentication is required. For example, failure against the following condition:

```json
{
    "type": "AuthenticateToRealm",
    "authenticateToRealm": "alpha"
}
```

Leads to this advice:

```json
{
    "AuthenticateToRealmConditionAdvice": [
        "/alpha"
    ]
}
```

An `AuthenticateToService` condition failure can result in advice showing the name of the required authentication journey. For example, failure against the following condition:

```json
{
    "type": "AuthenticateToService",
    "authenticateToService": "MyIdentityCloudJourney"
}
```

Leads to this advice:

```json
{
    "AuthenticateToServiceConditionAdvice": [
        "MyIdentityCloudJourney"
    ]
}
```

A `ResourceEnvIP` condition failure can result in advice that indicates corrective action to be taken. The advice varies, depending on what the condition tests. For example, failure against the following condition:

```json
{
    "type": "ResourceEnvIP",
    "resourceEnvIPConditionValue": [
        "IF IP=[127.0.0.12] THEN authlevel=4"
    ]
}
```

Leads to this advice:

```json
{
    "AuthLevelConditionAdvice": [
        "4"
    ]
}
```

Failure against a different type of `ResourceEnvIP` condition, such as the following:

```json
{
    "type": "ResourceEnvIP",
    "resourceEnvIPConditionValue": [
        "IF IP=[127.0.0.11] THEN service=MyIdentityCloudJourney"
    ]
}
```

Leads to this advice:

```json
{
    "AuthenticateToServiceConditionAdvice": [
        "MyIdentityCloudJourney"
    ]
}
```

A `Session` condition failure can result in advice showing that access was denied because the user's session was active longer than allowed by the condition. The advice also shows if the user's session was terminated and reauthentication is required. For example, failure against the following condition:

```json
{
    "type": "Session",
    "maxSessionTime": "10",
    "terminateSession": false
}
```

Leads to this advice:

```json
{
    "SessionConditionAdvice": [
        "deny"
    ]
}
```

When policy evaluation denials occur against the following conditions, Advanced Identity Cloud does not return any advice:

* `IPv4`

* `IPv6`

* `LDAPFilter`

* `OAuth2Scope`

* `SessionProperty`

* `SimpleTime`

When policy evaluation is requested for a nonexistent or inactive subject, Advanced Identity Cloud returns an HTTP 200 code and a response that contains no actions or advice. Access to the resource is denied.

## Request policy decisions for a tree of resources

This section shows how you can request policy decisions over REST for a resource and all other resources in the subtree beneath it.

When making a REST API call, specify the realm in the path component of the endpoint. You must specify the entire hierarchy of the realm. Prefix each realm in the hierarchy with the `realms/` keyword. For example, `/realms/root/realms/alpha`.

To request policy decisions for a tree of resources, send an HTTP POST request to the `policies` endpoint with the `evaluateTree` action; for example `/json/realms/root/realms/alpha/policies?_action=evaluateTree`. The payload for the HTTP POST is a JSON object that specifies at least the root resource and takes the following form.

```none
{
    "resource": "resource string",
    "application": "policy set that contains the policies to evaluate against",
    "subject": {
        "ssoToken": "SSO token ID string",
        "jwt": "JSON Web Token string",
        "claims": {
            "key": "value",
            ...
        }
    },
    "environment": {
        "optional key1": [
            "value",
            "another value",
            ...
        ],
        "optional key2": [
            "value",
            "another value",
            ...
        ],
        ...
    }
}
```

The values for the fields shown above are explained below:

* `resource`

  This required field specifies the root resource for the decisions to return.

  For example, depending on the patterns defined in the policy set, you could request decisions for resource URLs.

  ```json
  {
      "resource": "http://www.example.com/"
  }
  ```

* `application`

  This field holds the name of the policy set, for example, `samplePolicySet`.

  For more on policy sets, refer to [Policy sets over REST](rest-api-authz-applications.html).

* `subject`

  This optional field holds an object that represents the subject. You can specify one or more of the following keys. If you specify multiple keys, the subject can have multiple associated principals, and you can use subject conditions corresponding to any type in the request.

  * `ssoToken`

    The value is the SSO token ID string for the subject, returned for example on successful authentication as described in [Authenticate over REST](../am-authentication/authn-rest.html).

  * `jwt`

    The value is a JWT string.

  * `claims`

    The value is an object (map) of JWT claims to their values. If you do not specify the subject, Advanced Identity Cloud uses the SSO token ID of the subject making the request.

* `environment`

  This optional field holds a map of keys to lists of values.

  If you do not specify the environment, the default is an empty map.

The example below requests policy decisions for `http://www.example.com/`. The `<session-cookie-name>` header sets the SSO token for a user who has access to perform the operation, and the subject takes the SSO token of the user who wants to access a resource.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: AQIC5...NDU1*" \
--header "Accept-API-Version: resource=1.0" \
--data '{
    "resource": "http://www.example.com/",
    "subject": { "ssoToken": "AQIC5...zE4*" }
}' \
"https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/policies/?_action=evaluateTree"
[
    {
        "resource":"http://www.example.com/",
        "actions":{
            "GET":true,
            "OPTIONS":true,
            "HEAD":true
        },
        "attributes":{

        },
        "advices":{

        }
    },
    {
        "resource":"http://www.example.com/",
        "actions":{
            "POST":false,
            "PATCH":false,
            "GET":true,
            "DELETE":true,
            "OPTIONS":true,
            "HEAD":true,
            "PUT":true
        },
        "attributes":{
            "myStaticAttr":[
                "myStaticValue"
            ]
        },
        "advices":{

        }
    },
    {
        "resource":"http://www.example.com/?*",
        "actions":{
            "POST":false,
            "PATCH":false,
            "GET":false,
            "DELETE":false,
            "OPTIONS":true,
            "HEAD":false,
            "PUT":false
        },
        "attributes":{

        },
        "advices":{
            "AuthLevelConditionAdvice":[
                "3"
            ]
        }
    }
]
```

Advanced Identity Cloud returns decisions not only for the specified resource, but also for matching resource names in the tree whose root is the specified resource.

In the JSON list of decisions returned for each resource, Advanced Identity Cloud includes these fields:

* `resource`

  A resource name whose root is the resource specified in the request.

  The decisions returned aren't guaranteed to be in the same order as the resources were requested.

* `actions`

  A map of action name keys to Boolean values that indicate whether the action is allowed (`true`) or denied (`false`) for the specified resource.

  In the example, for matching resources with a query string only HTTP OPTIONS is allowed according to the policies configured.

* `attributes`

  A map of attribute names to their values if any response attributes are returned according to applicable policies.

  In the example, the policy that applies to `http://www.example.com:80/*` causes a static attribute to be returned.

* `advices`

  A map of advice names to their values if any advice is returned according to applicable policies.

  The `advices` field can provide hints regarding what Advanced Identity Cloud needs to take the authorization decision.

  In the following example, the policy that applies to resources with a query string requests that the subject authenticates at an authentication level of at least 3.

  Notice that with the `advices` field present, no `advices` appear in the JSON response.

  ```json
  {
      "advices": {
          "AuthLevelConditionAdvice": [ "3" ]
      }
  }
  ```

You can use the query string parameters `_prettyPrint=true` to make the output easier to read, and `_fields=field-name[,field-name...]` to limit the fields returned in the output.

---

---
title: Resource types over REST
description: You can manage resource types over REST at the resourcetypes endpoint.
component: pingoneaic-api
page_id: pingoneaic-api:am-authorization:rest-api-authz-resource-types
canonical_url: https://developer.pingidentity.com/pingoneaic-api/am-authorization/rest-api-authz-resource-types.html
keywords: ["Authorization", "Policy", "Resource", "REST API", "Configuration"]
section_ids:
  access-the-endpoints: Access the endpoints
  rest-api-authz-resource-types-query: Query resource types
  rest-api-authz-resource-types-read: Read a resource type
  rest-api-authz-resource-types-create: Create a resource type
  rest-api-authz-resource-types-update: Update a resource type
  rest-api-authz-resource-types-delete: Delete a resource type
---

# Resource types over REST

You can manage resource types over REST at the `resourcetypes` endpoint.

Advanced Identity Cloud stores resource types as JSON objects. A resource type can include the following fields. The fields have JSON values—​strings, numbers, objects, sets, arrays, `true`, `false`, and `null`.

| Resource type field   | Description                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `_id`, `uuid`(1)      | A unique, system-generated UUID string.Use this string to identify a specific resource type. Do not change the generated UUID.                                                                                                                                                                                                              |
| `_rev`(1)             | A system-generated revision string.                                                                                                                                                                                                                                                                                                         |
| `name`                | A human-readable name string for the resource type.Don't use any of the following characters in policy, policy set, or resource type names:- Double quotes (`"`)

- Plus sign (`+`)

- Comma (`,`)

- Less than (`<`)

- Equals (`=`)

- Greater than (`>`)

- Backslash (`\`)

- Forward slash (`/`)

- Semicolon (`;`)

- Null (`\u0000`) |
| `description`         | An optional text string to help identify the resource type.                                                                                                                                                                                                                                                                                 |
| `patterns`            | An array of resource pattern strings specifying URLs or resource names to protect.Learn more in [Resource type patterns](https://docs.pingidentity.com/pingoneaic/latest/am-authorization/resource-types-ui.html#policy-patterns-wildcards).                                                                                                |
| `actions`             | An object where each field is an action name.The value for each action name field is a boolean indicating whether to allow the action by default in policies that derive from this resource type.                                                                                                                                           |
| `createdBy`(1)        | A string indicating who created the resource type.                                                                                                                                                                                                                                                                                          |
| `creationDate`(1)     | An integer containing the creation time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                              |
| `lastModifiedBy`(1)   | A string indicating who last changed the resource type.                                                                                                                                                                                                                                                                                     |
| `lastModifiedDate`(1) | An integer containing the last modified time in milliseconds since January 1, 1970.                                                                                                                                                                                                                                                         |

(1) Don't change the value of this field.

## Access the endpoints

The REST calls to manage resource types rely on an account with the appropriate privileges:

1. Create a resource type administrator.

   In the Advanced Identity Cloud admin console, select Identities > Manage > *Realm Name* Realm - Users > + New *Realm Name* Realm - User and fill the required fields.

   Record the username and password.

2. Create a group that grants the privileges to the resource type administrator.

   Under Native Consoles > Access Management, select Realms > *Realm Name* > Identities > Groups > + Add Group to create a group with the following settings:

   * Group ID

     `am-resource-type-admins`

   * Members

     The resource type administrator whose username you recorded

   * Privileges

     Policy Admin\
     Resource Type Modify Access\
     Resource Type Read Access

3. Before making REST calls to manage resource types, authenticate as the resource type administrator:

   ```bash
   $ curl \
   --request POST \
   --header 'Content-Type: application/json' \
   --header 'X-OpenAM-Username: <resource-type-admin-username>' \
   --header 'X-OpenAM-Password: <resource-type-admin-password>' \
   --header 'Accept-API-Version: resource=2.0, protocol=1.0' \
   'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/authenticate'
   {
     "tokenId": "<resource-type-admin-tokenId>",
     "successUrl": "/enduser/?realm=/alpha",
     "realm": "/alpha"
   }
   ```

   Learn more in [Session tokens after authentication](../am-authentication/rest-using-ssotokens.html).

   Use the `<resource-type-admin-tokenId>` as the value of the `<session-cookie-name>` header to access the REST endpoints.

## Query resource types

To list all the resource types defined for a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/resourcetypes` endpoint with `_queryFilter=true` as the query string parameter.

```bash
$ curl \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes?_queryFilter=true'
[{
  "result": [{
    "_id": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
    "uuid": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
    "name": "Light",
    "description": "",
    "patterns": ["light://*/*"],
    "actions": {
      "switch_off": false,
      "switch_on": false
    },
    "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "creationDate": 1669038769034,
    "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
    "lastModifiedDate": 1669038769034
  }, {
    "_id": "76656a38-5f8e-401b-83aa-4ccb74ce88d2",
    "uuid": "76656a38-5f8e-401b-83aa-4ccb74ce88d2",
    "name": "URL..."
  }, {
    "_id": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "uuid": "d60b7a71-1dc6-44a5-8e48-e4b9d92dee8b",
    "name": "OAuth2 Scope..."
  }],
  "resultCount": 3,
  "pagedResultsCookie": null,
  "totalPagedResultsPolicy": "NONE",
  "totalPagedResults": -1,
  "remainingPagedResults": 0
}
```

Adapt the [query string parameters](../crest/query.html) to refine the results.

| Field         | Supported `_queryFilter` operators               |
| ------------- | ------------------------------------------------ |
| `uuid`        | Equals (`eq`) Contains (`co`) Starts with (`sw`) |
| `name`        |                                                  |
| `description` |                                                  |
| `patterns`    |                                                  |
| `actions`     |                                                  |

## Read a resource type

To read a resource type in a realm, send an HTTP GET request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource.

```bash
$ curl \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/fcaee7dc-f99c-43b1-b10d-592e1c4bd394'
{
  "_id": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
  "_rev": "1669045336245",
  "uuid": "fcaee7dc-f99c-43b1-b10d-592e1c4bd394",
  "name": "Light",
  "description": "",
  "patterns": ["light://*/*"],
  "actions": {
    "switch_off": false,
    "switch_on": false
  },
  "createdBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "creationDate": 1669038769034,
  "lastModifiedBy": "id=a980a458-2654-4d4f-a12a-d4bfa39534f7,ou=user,ou=am-config",
  "lastModifiedDate": 1669038769034
}
```

## Create a resource type

To create a resource type in a realm, send an HTTP POST request to the `/json/realms/root/realms/Realm Name/resourcetypes` endpoint with `_action=create` as the query string parameter and a JSON representation of the resource type as the POST data.

Advanced Identity Cloud generates the UUID for the resource.

```bash
$ curl \
--request POST \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "My Resource Type",
  "actions": {
    "LEFT": true,
    "RIGHT": true,
    "UP": true,
    "DOWN": true
  },
  "patterns": ["https://device/location/*"]
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/?_action=create'
{
  "_id": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "uuid": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "name": "My Resource Type",
  "description": null,
  "patterns": ["https://device/location/*"],
  "actions": {
    "RIGHT": true,
    "DOWN": true,
    "UP": true,
    "LEFT": true
  },
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669045619375,
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": 1669045619375
}
```

## Update a resource type

To update a resource type in a realm, send an HTTP PUT request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource. Include a JSON representation of the resource type as the PUT body, making sure the `"uuid"` and `"_id"` fields match the original resource.

```bash
$ curl \
--request PUT \
--header "Content-Type: application/json" \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
--data '{
  "name": "My Resource Type",
  "actions": {
    "LEFT": true,
    "RIGHT": true,
    "UP": false,
    "DOWN": false
  },
  "patterns": ["https://device/location/*"]
}' \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/c7e09ca1-a0db-4434-9327-ca685ae99899'
{
  "_id": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "uuid": "c7e09ca1-a0db-4434-9327-ca685ae99899",
  "name": "My Resource Type",
  "description": null,
  "patterns": ["https://device/location/*"],
  "actions": {
    "RIGHT": true,
    "DOWN": false,
    "UP": false,
    "LEFT": true
  },
  "createdBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "creationDate": 1669045619375,
  "lastModifiedBy": "id=1dff18dc-ac57-4388-8127-dff309f80002,ou=user,o=alpha,ou=services,ou=am-config",
  "lastModifiedDate": 1669045765822
}
```

## Delete a resource type

To delete a resource type from a realm, send an HTTP DELETE request to the `/json/realms/root/realms/Realm Name/resourcetypes/uuid` endpoint, where *uuid* is the value of the `"uuid"` field for the resource.

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/c7e09ca1-a0db-4434-9327-ca685ae99899'
{"_id":"c7e09ca1-a0db-4434-9327-ca685ae99899","_rev":"0"}
```

You can't delete a resource type if a policy set or policy depends on it. If you attempt to delete a resource type that is in use, Advanced Identity Cloud returns an HTTP 409 Conflict status code and a message like the one in the following example:

```bash
$ curl \
--request DELETE \
--header "<session-cookie-name>: <resource-type-admin-tokenId>" \
--header "Accept-API-Version: resource=1.0" \
'https://<tenant-env-fqdn>/am/json/realms/root/realms/alpha/resourcetypes/76656a38-5f8e-401b-83aa-4ccb74ce88d2'
{
  "code": 409,
  "reason": "Conflict",
  "message": "Unable to remove resource type 76656a38-5f8e-401b-83aa-4ccb74ce88d2 because it is referenced in the policy model."
}
```

Remove the dependency on the resource type from all policy sets and policies before you delete it.