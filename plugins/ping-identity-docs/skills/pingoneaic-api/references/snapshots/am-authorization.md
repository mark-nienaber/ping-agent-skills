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
