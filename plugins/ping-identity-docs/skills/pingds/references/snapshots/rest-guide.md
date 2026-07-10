---
title: Actions
description: Use PingDS HDAP actions to authenticate, change passwords, check password quality, reset passwords, and rename resources.
component: pingds
version: 8.1
page_id: pingds:rest-guide:action-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/action-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["Authentication", "REST API"]
section_ids:
  rest-action-auth: Authenticate
  rest-action-modify-password: Change your password
  rest-action-password-quality-check: Check password quality
  rest-action-reset-password: Reset a password
  read-pwp-state: Read password policy state
  rest-action-account-usability: Account usability action
  action-schema: Get JSON schema
  action-rename: Rename a resource
---

# Actions

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

## Authenticate

You can use `_action=authenticate` to get a bearer token valid for multiple HDAP requests.

For details, refer to [Bearer auth](rest-operations.html#authenticate-rest-bearer).

## Change your password

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | This action *requires HTTPS* to avoid sending the password over an insecure connection. |

Use HTTPS POST with `_action=modifyPassword` in the query string and a JSON object with the old and new passwords in the following fields:

* `oldPassword`

  The value of this field is the current password as a UTF-8 string.

* `newPassword`

  The value of this field is the new password as a UTF-8 string.

On success, the HTTP status code is 200 OK, and the response body is an empty JSON resource:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=bjensen:hifalutin \
 --header 'Content-Type: application/json' \
 --data '{"oldPassword": "hifalutin", "newPassword": "chngthspwd"}' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=modifyPassword'
```

> **Collapse: Show output**
>
> ```
> {}
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=modifyPassword&dryRun=true',
        method: 'POST',
        credentials: 'dc=com/dc=example/ou=People/uid=bjensen:hifalutin',
        body: { "oldPassword": "hifalutin", "newPassword": "chngthspwd" }
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: dry-run change password', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [action-change-password.js](../_attachments/hdap/js/action-change-password.js), [utils.js](../_attachments/hdap/js/utils.js)

Remove the `dry-run` parameter to perform the operation.

```python
#!/usr/bin/env python3

import requests
import utils

body = { 'oldPassword': 'hifalutin', 'newPassword': 'chngthspwd' }
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_action': 'modifyPassword', 'dryRun': True }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-change-password.py](../_attachments/hdap/py/action-change-password.py)

Remove the `dryRun` parameter to perform the operation.

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = { '_action': 'modifyPassword', 'dryRun': true }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
body = { "oldPassword" => "hifalutin", "newPassword" => "chngthspwd" }
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=bjensen'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-change-password.rb](../_attachments/hdap/rb/action-change-password.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Check password quality

Use the `passwordQualityAdvice` and `dryRun` query string parameters to get details when a password update fails, to test passwords, and to test password policies:

* The `passwordQualityAdvice` parameter relies on the LDAP password quality advice control, OID `1.3.6.1.4.1.36733.2.1.5.5`. Users modifying their password must have access to request the control.

  |   |                                                                                                                     |
  | - | ------------------------------------------------------------------------------------------------------------------- |
  |   | The password quality advice control and the `passwordQualityAdvice` parameter have interface stability: *Evolving*. |

* The `dryRun` parameter relies on the LDAP no-op control, OID `1.3.6.1.4.1.4203.1.10.2`.

The following example shows a password update failure. The status code is HTTP 400 Bad Request and the response JSON describes what passed and what failed:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=bjensen:hifalutin \
 --header 'Content-Type: application/json' \
 --data '{"oldPassword": "hifalutin", "newPassword": "t00shrt"}' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=modifyPassword&passwordQualityAdvice=true&dryRun=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "code" : 400,
>   "reason" : "Bad Request",
>   "message" : "Constraint Violation: The provided new password failed the validation checks defined in the server: The provided password is shorter than the minimum required length of 8 characters",
>   "detail" : {
>     "passwordQualityAdvice" : {
>       "attributeType" : "userPassword",
>       "failingCriteria" : [ {
>         "parameters" : {
>           "max-password-length" : 0,
>           "min-password-length" : 8
>         },
>         "type" : "length-based"
>       } ],
>       "passingCriteria" : [ {
>         "parameters" : {
>           "case-sensitive-validation" : false,
>           "check-substrings" : true,
>           "min-substring-length" : 5,
>           "test-reversed-password" : false
>         },
>         "type" : "dictionary"
>       } ]
>     }
>   }
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=modifyPassword&passwordQualityAdvice=true&dryRun=true',
        method: 'POST',
        credentials: 'dc=com/dc=example/ou=People/uid=bjensen:hifalutin',
        body: { "oldPassword": "hifalutin", "newPassword": "t00shrt" }
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: dry-run check password quality', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [action-check-password-quality.js](../_attachments/hdap/js/action-check-password-quality.js), [utils.js](../_attachments/hdap/js/utils.js)

Remove the `dryRun` parameter to perform the operation.

```python
#!/usr/bin/env python3

import requests
import utils

body = { 'oldPassword': 'hifalutin', 'newPassword': 't00shrt' }
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_action': 'modifyPassword', 'passwordQualityAdvice': True, 'dryRun': True }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-check-password-quality.py](../_attachments/hdap/py/action-check-password-quality.py)

Remove the `dryRun` parameter to perform the operation. Remove the `dry-run` parameter to perform the operation.

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = { '_action': 'modifyPassword', 'passwordQualityAdvice': true, 'dryRun': true }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
body = { "oldPassword" => "hifalutin", "newPassword" => "t00shrt" }
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=bjensen'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-check-password-quality.rb](../_attachments/hdap/rb/action-check-password-quality.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

`"max-password-length" : 0` means DS does not enforce an upper bound.

You can use `passwordQualityAdvice` without the `dryRun` parameter. On failure, you get diagnostic information as shown in the preceding example. On success, the HTTP status code is 200 OK and the response body is an empty JSON resource.

## Reset a password

When one user changes another user's password, DS considers it a password reset. Password policies can require users to change their passwords again after a password reset.

|   |                                                                                         |
| - | --------------------------------------------------------------------------------------- |
|   | This action *requires HTTPS* to avoid sending the password over an insecure connection. |

The example demonstrates a password administrator changing a user's password. The password administrator must have the `password-reset` privilege; otherwise, the reset fails due to insufficient access:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request PATCH \
 --cacert ca-cert.pem \
 --user uid=admin:password \
 --header 'Content-Type: application/json' \
 --data '[{
  "operation": "add",
  "field": "ds-privilege-name",
  "value": "password-reset"
 }]' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_prettyPrint=true'
```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_fields=_id,ds-privilege-name',
        method: 'PATCH',
        credentials: 'uid=admin:password',
        body: [{
            "operation": "add",
            "field": "ds-privilege-name",
            "value": "password-reset"
        }]
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: assign the password-reset privilege', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [action-password-reset.js](../_attachments/hdap/js/action-password-reset.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

jwt = utils.authenticate('uid=admin', 'password')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
patch = [{
    'operation': 'add',
    'field': 'ds-privilege-name',
    'value': 'password-reset'
}]
response = requests.patch(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=kvaughan',
    headers=headers,
    json=patch,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-password-reset.py](../_attachments/hdap/py/action-password-reset.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('uid=admin', 'password')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = { '_fields': '_id,ds-privilege-name' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
body = [{
    "operation" => "add",
    "field" => "ds-privilege-name",
    "value" => "password-reset"
}]
response = hdap.patch do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=kvaughan'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-password-reset.rb](../_attachments/hdap/rb/action-password-reset.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

Use HTTPS POST with `_action=resetPassword` in the query string and an empty JSON document (`{}`) as the POST data.

On success, the HTTP status code is 200 OK. The response body is a JSON resource with a `generatedPassword` containing the new password:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header "Content-Type: application/json" \
 --data '{}' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=resetPassword'
```

> **Collapse: Show output**
>
> ```
> {"generatedPassword":"<new-password>"}
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=resetPassword&dryRun=true',
        method: 'POST',
        body: {}
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: dry-run reset password', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [action-reset-password.js](../_attachments/hdap/js/action-reset-password.js), [utils.js](../_attachments/hdap/js/utils.js)

Remove the `dryRun` parameter to perform the operation.

```python
#!/usr/bin/env python3

import requests
import utils

body = {}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_action': 'resetPassword', 'dryRun': True }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-reset-password.py](../_attachments/hdap/py/action-reset-password.py)

Remove the `dryRun` parameter to perform the operation.

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = { '_action': 'resetPassword', 'dryRun': true }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=bjensen'
    h.body = JSON.generate('{}')
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-reset-password.rb](../_attachments/hdap/rb/action-reset-password.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

Remove the `dryRun` parameter to perform the operation.

The password administrator must communicate the generated password to the user.

Use this in combination with a password policy [to force the user to change their password again after a reset](../security-guide/pwp-samples.html#example-require-password-change-on-add-or-reset).

## Read password policy state

Although it's an operational field rather than an HDAP action, you can use an account's `ds-pwp-state-json` field to read password policy state.

DS servers have a password policy state virtual attribute enabled by default. It provides information similar to the `manage-account get-all` command.

Accounts with access to read the operational attribute `ds-pwp-state-json` get information from the following fields. Many of the fields only appear when the situation requires:

| Field                                          | Description                                                                           |
| ---------------------------------------------- | ------------------------------------------------------------------------------------- |
| `account-expiration-time`                      | Expiration time                                                                       |
| `account-is-disabled`                          | Boolean                                                                               |
| `account-is-expired`                           | Boolean                                                                               |
| `account-is-idle-locked`                       | Boolean                                                                               |
| `account-is-reset-locked`                      | Boolean, `true` if the password was not changed soon enough after reset               |
| `account-is-usable`                            | Boolean                                                                               |
| `authentication-failure-times`                 | Authentication failure times                                                          |
| `current-authentication-failure-count`         | Number of recorded authentication failures                                            |
| `expire-passwords-without-warning`             | Boolean                                                                               |
| `failure-lockout-count`                        | Maximum number of authentication failures allowed before lockout                      |
| `failure-lockout-expiration-interval`          | Duration in seconds of account lockout after too many authentication failures         |
| `force-change-on-add`                          | Boolean, `true` when the password must change immediately after DS adds the account   |
| `force-change-on-reset`                        | Boolean, `true` when the password must change after another user resets it            |
| `grace-login-use-times`                        | Grace login times                                                                     |
| `idle-lockout-interval-seconds`                | Maximum seconds an account can remain idle (no recent authentications) before lockout |
| `idle-lockout-time`                            | Time account locks for being idle (no recent authentications)                         |
| `idle-lockout`                                 | Seconds until the account locks for being idle                                        |
| `is-within-minimum-password-age`               | Boolean, whether the password is too new to change                                    |
| `last-login-time`                              | Time of the last successful authentication                                            |
| `max-password-reset-age-seconds`               | Maximum seconds to change the password after reset                                    |
| `maximum-grace-login-count`                    | Number of grace logins allowed after expiration to set a new password                 |
| `maximum-password-age-seconds`                 | Maximum seconds the password can remain the same                                      |
| `maximum-password-history-count`               | Maximum number of records allowed in the account's list of old password               |
| `maximum-password-history-duration-seconds`    | Maximum number of seconds DS retains old passwords                                    |
| `minimum-password-age-expiration-time`         | Time the password is old enough to change                                             |
| `minimum-password-age-seconds`                 | Minimum seconds between password changes                                              |
| `must-change-password`                         | Boolean, `true` when the password must change as the next action on the account       |
| `password-change-time`                         | Time the password changed                                                             |
| `password-expiration-time`                     | Time the password expires                                                             |
| `password-expiration-warning-interval-seconds` | Seconds before bind responses include expiry notifications                            |
| `password-expiration-warning-issued`           | Boolean, `true` if DS has returned a notification about expiry                        |
| `password-expiration-warning-time`             | Time DS first returned a notification about expiry                                    |
| `password-expiration-warning`                  | Seconds ago DS first returned a notification about expiry                             |
| `password-expiration`                          | Seconds until the password expires                                                    |
| `password-is-expired`                          | Boolean                                                                               |
| `password-policy-dn`                           | The password policy governing the current account                                     |
| `recent-login-history`                         | Array, times of the last successful authentications                                   |
| `remaining-authentication-failure-count`       | Number, difference between the maximum and current authentication failures            |
| `remaining-grace-login-count`                  | Number, difference between the maximum and used grace login count                     |
| `require-secure-authentication`                | Boolean, `true` when authentication must prevent exposing the credentials             |
| `require-secure-password-changes`              | Boolean, `true` when password changes must prevent exposing the credentials           |
| `reset-lockout-time`                           | Time the account locks after reset unless the password changes                        |
| `seconds-remaining-in-failure-lockout`         | Number of seconds before the locked account unlocks                                   |
| `seconds-remaining-in-minimum-password-age`    | Seconds until the password is old enough to change                                    |
| `seconds-since-account-expiration`             | Seconds since the account expired                                                     |
| `seconds-since-idle-lockout`                   | Seconds since the account locked for being idle (no recent authentications)           |
| `seconds-since-last-login`                     | Seconds since the last successful authentication                                      |
| `seconds-since-password-change`                | Seconds since the password changed                                                    |
| `seconds-since-password-expiration-warning`    | Seconds since DS sent the first bind response with an expiry notification             |
| `seconds-since-password-expiration`            | Seconds since the password expired                                                    |
| `seconds-until-account-expiration`             | Seconds until the account expires                                                     |
| `seconds-until-idle-lockout`                   | Seconds until the account locks for being idle (no recent authentications)            |
| `seconds-until-password-expiration-warning`    | Seconds until DS starts sending bind responses with expiry notifications              |
| `seconds-until-password-expiration`            | Seconds until the password expires                                                    |
| `seconds-until-reset-lockout`                  | Seconds until the account locks after reset unless the password changes               |
| `used-grace-login-count`                       | Number of recorded grace logins                                                       |

To read the field:

1. Make sure the reader has access:

   ```console
   $ ldapmodify \
    --hostname localhost \
    --port 1636 \
    --useSsl \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --bindDN uid=admin \
    --bindPassword password << EOF
   dn: dc=example,dc=com
   changetype: modify
   add: aci
   aci: (targetattr="ds-pwp-state-json")(version 3.0;
     acl "Read pwp state"; allow (read,search,compare)
     userdn="ldap:///uid=kvaughan,ou=people,dc=example,dc=com";)
   EOF
   ```

2. Read the attribute on an account:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --cacert ca-cert.pem \
    --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=ds-pwp-state-json&_prettyPrint=true'
   ```

   > **Collapse: Show output**
   >
   > ```
   > {
   >   "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
   >   "_rev" : "<revision>",
   >   "ds-pwp-state-json" : {
   >     "require-secure-authentication" : true,
   >     "password-policy-dn" : "cn=Default Password Policy,cn=Password Policies,cn=config",
   >     "force-change-on-reset" : false,
   >     "account-is-expired" : false,
   >     "password-change-time" : "<timestamp>",
   >     "account-is-idle-locked" : false,
   >     "seconds-since-password-change" : 9,
   >     "account-is-disabled" : false,
   >     "account-is-reset-locked" : false,
   >     "must-change-password" : false,
   >     "password-is-expired" : false,
   >     "is-within-minimum-password-age" : false,
   >     "account-is-usable" : true,
   >     "require-secure-password-changes" : true,
   >     "force-change-on-add" : false
   >   }
   > }
   > ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       const options = getOptions({
           path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=ds-pwp-state-json'
       })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: read password policy state', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [read-pwp-state.js](../_attachments/hdap/js/read-pwp-state.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   params = { '_fields': 'ds-pwp-state-json' }
   jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   response = requests.get(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
       headers=headers,
       params=params,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [utils.py](../_attachments/hdap/py/utils.py), [read-pwp-state.py](../_attachments/hdap/py/read-pwp-state.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'

   utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   fields = { '_fields': 'ds-pwp-state-json' }
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [read-pwp-state.rb](../_attachments/hdap/rb/read-pwp-state.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Account usability action

Use the `accountUsability` action to get details about a user's ability to authenticate.

* The action depends on the LDAP [Account usability control](../ldap-reference/controls.html#account-usability-control), which has OID `1.3.6.1.4.1.42.2.27.9.5.8`.

* The password administrator must have access to use the LDAP control.

Try the `accountUsability` action:

1. Grant the password administrator permission to use the control.

   The following example sets a global access control instruction (ACI) *(tooltip: \<div class="paragraph">
   \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
   \</div>)* for Kirsten Vaughan:

   ```console
   $ dsconfig \
    set-access-control-handler-prop \
    --hostname localhost \
    --port 4444 \
    --bindDN uid=admin \
    --bindPassword password \
    --add global-aci:"(targetcontrol=\"AccountUsability\")(version 3.0; acl \"Account usability access\"; allow(read) userdn=\"ldap:///uid=kvaughan,ou=People,dc=example,dc=com\";)" \
    --trustStorePath /path/to/opendj/config/keystore \
    --trustStoreType PKCS12 \
    --trustStorePassword:file /path/to/opendj/config/keystore.pin \
    --no-prompt
   ```

2. Use a password policy that produces results for account usability:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --request POST \
    --user uid=admin:password \
    --cacert ca-cert.pem \
    --header 'Content-Type: application/json' \
    --data '{
     "_id": "dc=com/dc=example/cn=Lockout%20with%20max%20age%20and%20grace%20logins",
     "objectClass": ["top", "subentry", "ds-pwp-password-policy"],
     "cn": ["Lockout with max age and grace logins"],
     "ds-pwp-default-password-storage-scheme": ["PBKDF2-HMAC-SHA256"],
     "ds-pwp-grace-login-count": 3,
     "ds-pwp-lockout-duration": "5 m",
     "ds-pwp-lockout-failure-count": 3,
     "ds-pwp-lockout-failure-expiration-interval": "10 m",
     "ds-pwp-max-password-age": "30 d",
     "ds-pwp-password-attribute": "userPassword",
     "subtreeSpecification": { "base": "ou=people", "filter": "/uid eq \"bjensen\"" }
    }' \
    'https://localhost:8443/hdap/dc=com/dc=example?_action=create'
   ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       const options = getOptions({
           path: '/hdap/dc=com/dc=example?_action=create',
           credentials: 'uid=admin:password',
           method: 'POST',
           body: {
               "_id": "dc=com/dc=example/cn=Lockout%20with%20max%20age%20and%20grace%20logins",
               "objectClass": ["top", "subentry", "ds-pwp-password-policy"],
               "cn": ["Lockout with max age and grace logins"],
               "ds-pwp-default-password-storage-scheme": ["PBKDF2-HMAC-SHA256"],
               "ds-pwp-grace-login-count": 3,
               "ds-pwp-lockout-duration": "5 m",
               "ds-pwp-lockout-failure-count": 3,
               "ds-pwp-lockout-failure-expiration-interval": "10 m",
               "ds-pwp-max-password-age": "30 d",
               "ds-pwp-password-attribute": "userPassword",
               "subtreeSpecification": { "base": "ou=people", "filter": "/uid eq \"bjensen\"" }
           }
       })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: add password policy', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [action-add-password-policy.js](../_attachments/hdap/js/action-add-password-policy.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   body = {
       '_id': 'dc=com/dc=example/cn=Lockout%20with%20max%20age%20and%20grace%20logins',
       'objectClass': ['top', 'subentry', 'ds-pwp-password-policy'],
       'cn': ['Lockout with max age and grace logins'],
       'ds-pwp-default-password-storage-scheme': ['PBKDF2-HMAC-SHA256'],
       'ds-pwp-grace-login-count': 3,
       'ds-pwp-lockout-duration': '5 m',
       'ds-pwp-lockout-failure-count': 3,
       'ds-pwp-lockout-failure-expiration-interval': '10 m',
       'ds-pwp-max-password-age': '30 d',
       'ds-pwp-password-attribute': 'userPassword',
       'subtreeSpecification': { "base": "ou=people", "filter": "/uid eq \"bjensen\"" }
   }
   jwt = utils.authenticate('uid=admin', 'password')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   response = requests.post(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example',
       headers=headers,
       json=body,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [utils.py](../_attachments/hdap/py/utils.py), [action-add-password-policy.py](../_attachments/hdap/py/action-add-password-policy.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'
   require 'json'

   utils = Utils.new('uid=admin', 'password')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   body = {
       "_id" => "dc=com/dc=example/cn=Lockout%20with%20max%20age%20and%20grace%20logins",
       "objectClass" => ["top", "subentry", "ds-pwp-password-policy"],
       "cn" => ["Lockout with max age and grace logins"],
       "ds-pwp-default-password-storage-scheme" => ["PBKDF2-HMAC-SHA256"],
       "ds-pwp-grace-login-count" => 3,
       "ds-pwp-lockout-duration" => "5 m",
       "ds-pwp-lockout-failure-count" => 3,
       "ds-pwp-lockout-failure-expiration-interval" => "10 m",
       "ds-pwp-max-password-age" => "30 d",
       "ds-pwp-password-attribute" => "userPassword",
       "subtreeSpecification" => { "base": "ou=people", "filter": "/uid eq \"bjensen\"" }
   }
   response = hdap.post do |h|
       h.path = 'dc=com/dc=example'
       h.body = JSON.generate(body)
   end

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-add-password-policy.rb](../_attachments/hdap/rb/action-add-password-policy.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

3. Produce some account usability information on a user account:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --user dc=com/dc=example/ou=People/uid=bjensen:wrong-password \
    --cacert ca-cert.pem \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=_id'
   $ curl \
    --user dc=com/dc=example/ou=People/uid=bjensen:wrong-password \
    --cacert ca-cert.pem \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=_id'
   $ curl \
    --user dc=com/dc=example/ou=People/uid=bjensen:wrong-password \
    --cacert ca-cert.pem \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=_id'
   ```

   ```javascript
   const { doRequest, getOptions } = require('./utils')

   const options = getOptions({
       path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=_id',
       credentials: 'dc=com/dc=example/ou=People/uid=bjensen:wrong-password'
   })

   doRequest('HDAP: Basic auth with wrong password', options)
       .then(response => { console.log(response) })
       .catch(error => { console.error(error) })
       .finally(() => {
           doRequest('HDAP: Basic auth with wrong password', options)
               .then(response => { console.log(response) })
               .catch(error => { console.error(error) })
               .finally(() => {
                   doRequest('HDAP: Basic auth with wrong password', options)
                       .then(response => { console.log(response) })
                       .catch(error => { console.error(error) })
               })
       })
   ```

   Source files for this sample: [action-lock-bjensen.js](../_attachments/hdap/js/action-lock-bjensen.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   from requests.auth import HTTPBasicAuth
   import utils

   for i in range(3):
       response = requests.get(
           f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
           auth=HTTPBasicAuth('dc=com/dc=example/ou=People/uid=bjensen', 'wrong-password'),
           verify=utils.ca_pem)
       print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-lock-bjensen.py](../_attachments/hdap/py/action-lock-bjensen.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'
   require 'json'

   utils = Utils.new('', '')
   options = { ca_file: utils.ca_pem }
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, :basic, 'dc=com/dc=example/ou=People/uid=bjensen', 'wrong-password'
   end
   3.times do
       response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')
       puts "Status code: #{response.status}\nJSON: #{response.body}"
   end
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-lock-bjensen.rb](../_attachments/hdap/rb/action-lock-bjensen.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

4. Use the action to get account usability information:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --request POST \
    --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    --header 'Content-Type: application/json' \
    --cacert ca-cert.pem \
    --data '{}' \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=accountUsability'
   ```

   > **Collapse: Show output**
   >
   > ```
   > {"status":"locked","unlockIn":299}
   > ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       const options = getOptions({
           path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=accountUsability&dryRun=true',
           method: 'POST',
           body: {}
       })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: dry-run check account usability', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [action-account-usability.js](../_attachments/hdap/js/action-account-usability.js), [utils.js](../_attachments/hdap/js/utils.js)

   Remove the `dryRun` parameter to perform the operation.

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   body = {}
   jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   params = { '_action': 'accountUsability' }
   response = requests.post(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
       headers=headers,
       json=body,
       params=params,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-account-usability.py](../_attachments/hdap/py/action-account-usability.py)

   Remove the `dryRun` parameter to perform the operation.

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'
   require 'json'

   utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   query = { '_action': 'accountUsability' }
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   response = hdap.post do |h|
       h.path = 'dc=com/dc=example/ou=People/uid=bjensen'
       h.body = JSON.generate('{}')
   end

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-account-usability.rb](../_attachments/hdap/rb/action-account-usability.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

   Remove the `dryRun` parameter to perform the operation.

The JSON response can contain the following fields. The `status` property is always present. The other fields are present if they apply:

```none
{
  "status": "string",              // One of "disabled", "locked", "passwordExpired",
                                   // "mustChangePassword", or "valid"
  "unlockIn": number,              // Seconds until locked account is unlocked
  "graceLoginsRemaining": number,  // Number of remaining authentications allowed with
                                   // an expired password
  "passwordExpiresIn": number,     // Seconds until password expires
}
```

## Get JSON schema

Use the `schema` action to get the [JSON schema](https://json-schema.org/) for a resource.

Perform an HTTP POST with `_action=schema` in the query string and an empty JSON document (`{}`) as the POST data:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --cacert ca-cert.pem \
 --data '{}' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=schema&_prettyPrint=true'
```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=schema',
        method: 'POST',
        body: JSON.stringify({})
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: get schema', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [action-get-schema.js](../_attachments/hdap/js/action-get-schema.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

body = {}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_action': 'schema' }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-get-schema.py](../_attachments/hdap/py/action-get-schema.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = { '_action': 'schema' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=bjensen'
    h.body = JSON.generate('{}')
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-get-schema.rb](../_attachments/hdap/rb/action-get-schema.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

> **Collapse: Show output**
>
> ```json
> {
>   "type" : "object",
>   "properties" : {
>     "objectClass" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       },
>       "const" : [ "top", "person", "cos", "oauth2TokenObject", "organizationalPerson", "inetOrgPerson", "posixAccount" ]
>     },
>     "sn" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "cn" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "telephoneNumber" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "seeAlso" : {
>       "supertype" : "distinguishedName",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "format" : "json-pointer"
>       }
>     },
>     "userPassword" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "description" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "classOfService" : {
>       "type" : "string"
>     },
>     "diskQuota" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "mailQuota" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "oauth2Token" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "object"
>       }
>     },
>     "telexNumber" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "teletexTerminalIdentifier" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "ou" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "internationaliSDNNumber" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "registeredAddress" : {
>       "supertype" : "postalAddress",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "array",
>         "items" : {
>           "type" : "string"
>         }
>       }
>     },
>     "title" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "facsimileTelephoneNumber" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "x121Address" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "postOfficeBox" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "street" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "physicalDeliveryOfficeName" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "destinationIndicator" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "postalAddress" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "array",
>         "items" : {
>           "type" : "string"
>         }
>       }
>     },
>     "st" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "preferredDeliveryMethod" : {
>       "type" : "string"
>     },
>     "postalCode" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "l" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "preferredLanguage" : {
>       "description" : "preferred written or spoken language for a person",
>       "type" : "string"
>     },
>     "departmentNumber" : {
>       "description" : "identifies a department within an organization",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "o" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "carLicense" : {
>       "description" : "vehicle license or registration plate",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "secretary" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "format" : "json-pointer"
>       }
>     },
>     "employeeType" : {
>       "description" : "type of employment for a person",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "homePhone" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "pager" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "employeeNumber" : {
>       "description" : "numerically identifies an employee within an organization",
>       "type" : "string"
>     },
>     "mobile" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "userPKCS12" : {
>       "description" : "PKCS #12 PFX PDU for exchange of personal identity information",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "contentEncoding" : "base64"
>       }
>     },
>     "userCertificate" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "contentEncoding" : "base64"
>       }
>     },
>     "businessCategory" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "userSMIMECertificate" : {
>       "description" : "PKCS#7 SignedData used to support S/MIME",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "contentEncoding" : "base64"
>       }
>     },
>     "mail" : {
>       "description" : "The email address, including internationalized addresses (changed from the standard which only allowed ascii)",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "roomNumber" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "audio" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "contentEncoding" : "base64"
>       }
>     },
>     "initials" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "manager" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "format" : "json-pointer"
>       }
>     },
>     "photo" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "contentEncoding" : "base64"
>       }
>     },
>     "givenName" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "homePostalAddress" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "array",
>         "items" : {
>           "type" : "string"
>         }
>       }
>     },
>     "displayName" : {
>       "description" : "preferred name of a person to be used when displaying entries",
>       "type" : "string"
>     },
>     "labeledURI" : {
>       "description" : "Uniform Resource Identifier with optional label",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "jpegPhoto" : {
>       "description" : "a JPEG image",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "contentEncoding" : "base64"
>       }
>     },
>     "x500UniqueIdentifier" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "uid" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "homeDirectory" : {
>       "description" : "The absolute path to the home directory",
>       "type" : "string"
>     },
>     "gidNumber" : {
>       "description" : "An integer uniquely identifying a group in an administrative domain",
>       "type" : "integer"
>     },
>     "uidNumber" : {
>       "description" : "An integer uniquely identifying a user in an administrative domain",
>       "type" : "integer"
>     },
>     "loginShell" : {
>       "description" : "The path to the login shell",
>       "type" : "string"
>     },
>     "authPassword" : {
>       "description" : "password authentication information",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "gecos" : {
>       "description" : "The GECOS field; the common name",
>       "type" : "string"
>     }
>   },
>   "requiredProperties" : [ "cn", "gidNumber", "homeDirectory", "objectClass", "sn", "uid", "uidNumber" ],
>   "additionalProperties" : false
> }
> ```

If you haven't yet created a resource, you get the JSON schema for the resource to create from the parent resource by specifying the LDAP object classes for the new resource. Use the `schema` action and a comma-separated list of object classes as the value of an `objectClasses` parameter:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --cacert ca-cert.pem \
 --data '{}' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People?_action=schema&objectClasses=person,posixAccount&_prettyPrint=true'
```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People?_action=schema&objectClasses=person,posixAccount',
        method: 'POST',
        body: JSON.stringify({})
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: get schema for new resource', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [action-get-new-schema.js](../_attachments/hdap/js/action-get-new-schema.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

body = {}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_action': 'schema', 'objectClasses': 'person,posixAccount' }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-get-new-schema.py](../_attachments/hdap/py/action-get-new-schema.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = { '_action': 'schema', 'objectClasses': 'person,posixAccount' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People'
    h.body = JSON.generate('{}')
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-get-new-schema.rb](../_attachments/hdap/rb/action-get-new-schema.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

> **Collapse: Show output**
>
> ```json
> {
>   "type" : "object",
>   "properties" : {
>     "objectClass" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       },
>       "const" : [ "top", "person", "posixAccount" ]
>     },
>     "sn" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "cn" : {
>       "supertype" : "name",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "telephoneNumber" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "seeAlso" : {
>       "supertype" : "distinguishedName",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string",
>         "format" : "json-pointer"
>       }
>     },
>     "userPassword" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "description" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "homeDirectory" : {
>       "description" : "The absolute path to the home directory",
>       "type" : "string"
>     },
>     "gidNumber" : {
>       "description" : "An integer uniquely identifying a group in an administrative domain",
>       "type" : "integer"
>     },
>     "uidNumber" : {
>       "description" : "An integer uniquely identifying a user in an administrative domain",
>       "type" : "integer"
>     },
>     "uid" : {
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "loginShell" : {
>       "description" : "The path to the login shell",
>       "type" : "string"
>     },
>     "authPassword" : {
>       "description" : "password authentication information",
>       "type" : "array",
>       "uniqueItems" : true,
>       "items" : {
>         "type" : "string"
>       }
>     },
>     "gecos" : {
>       "description" : "The GECOS field; the common name",
>       "type" : "string"
>     }
>   },
>   "requiredProperties" : [ "cn", "gidNumber", "homeDirectory", "objectClass", "sn", "uid", "uidNumber" ],
>   "additionalProperties" : false
> }
> ```

You can also read the schema for an individual field or object class directly as described in [the reference for HDAP schema](rest-operations.html#hdap-schema).

## Rename a resource

Use the `rename` action to change a resource's `_id`. This effectively moves the resource.

Perform an HTTP POST with `_action=rename` in the query string and the `newId` in the POST data:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --cacert ca-cert.pem \
 --data '{"newId": "dc=com/dc=example/ou=People/uid=sjensen"}' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=scarter?_action=rename&_fields=uid'
```

> **Collapse: Show output**
>
> ```
> {"uid":["scarter","sjensen"],"_id":"dc=com/dc=example/ou=People/uid=sjensen","_rev":"<revision>"}
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=scarter?_action=rename&_fields=uid',
        method: 'POST',
        body: { "newId": "dc=com/dc=example/ou=People/uid=sjensen" }
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: rename a resource', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [action-rename.js](../_attachments/hdap/js/action-rename.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

body = { 'newId': 'dc=com/dc=example/ou=People/uid=sjensen' }
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_action': 'rename', '_fields': 'uid' }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=scarter',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [action-rename.py](../_attachments/hdap/py/action-rename.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = { '_action': 'rename', '_fields': 'uid' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
body = { "newId" => "dc=com/dc=example/ou=People/uid=sjensen" }
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=scarter'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [action-rename.rb](../_attachments/hdap/rb/action-rename.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

To remove the existing RDN value, `uid=scarter` in this example, use the `deleteOldRdn=true` parameter. A relative distinguished name (RDN) *(tooltip: \<div class="paragraph">
\<p>The initial portion of a DN distinguishing the entry from all others at the same level.\</p>
\</div>)* refers to the part of an entry's DN that differentiates it from all other DNs at the same level in the directory tree. For HDAP, the last path element of the `_id` holds the field value DS deletes when `deleteOldRdn=true`. In `dc=com/dc=example/ou=People/uid=sjensen`, it's `uid=sjensen`. In `dc=com/dc=example/ou=People`, it's `ou=People`.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | When you rename a resource with child resources, DS renames all the child resources, too.For example, if you rename `dc=com/dc=example/ou=People` to `dc=com/dc=example/ou=Subscribers`, `dc=com/dc=example/ou=People/uid=sjensen` becomes `dc=com/dc=example/ou=Subscribers/uid=sjensen`.DS directory servers support this operation only for moving resources in the same backend, under the same path. Depending on the number of resources moved, this can be a resource-intensive operation. |

---

---
title: Binary resources
description: Add and read binary resources such as profile photos in PingDS directory entries over the HDAP API.
component: pingds
version: 8.1
page_id: pingds:rest-guide:binary-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/binary-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  binary-rest-update: Add a binary resource
  binary-rest-read: Read a binary resource
---

# Binary resources

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

## Add a binary resource

1. Get the base64-encoded string representation of the binary resource to upload.

   For example, save the JPEG photo, [picture.jpg](../_attachments/images/picture.jpg), to the current directory and convert it to a base64-encoded string:

   ```console
   $ base64 encode --rawDataFile picture.jpg
   ```

   > **Collapse: Show output**
   >
   > ```
   > /9j/4AAQSkZJRgABAQEAYABgAAD/4QAWRXhpZgAASUkqAAgAAAAAAAAAAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAr/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AL+AAf/Z
   > ```

2. Upload the string representation of the binary resource.

   The following example updates Babs Jensen's resource to add or replace the profile photo:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --request PUT \
    --cacert ca-cert.pem \
    --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    --header 'Content-Type: application/json' \
    --data '{"photo": "/9j/4AAQSkZJRgABAQEAYABgAAD/4QAWRXhpZgAASUkqAAgAAAAAAAAAAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAr/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AL+AAf/Z"}' \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen'
   ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       const photo = { "photo": "/9j/4AAQSkZJRgABAQEAYABgAAD/4QAWRXhpZgAASUkqAAgAAAAAAAAAAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAr/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AL+AAf/Z" }
       const resource = '/hdap/dc=com/dc=example/ou=People/uid=bjensen'
       const options = getOptions({ method: 'PUT', path: resource, body: photo })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: add photo', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [binary-add.js](../_attachments/hdap/js/binary-add.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   photo = { 'photo': '/9j/4AAQSkZJRgABAQEAYABgAAD/4QAWRXhpZgAASUkqAAgAAAAAAAAAAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAr/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AL+AAf/Z' }
   jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   response = requests.put(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
       headers=headers,
       json=photo,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [binary-add.py](../_attachments/hdap/py/binary-add.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'
   require 'json'

   utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   photo = { "photo" => "/9j/4AAQSkZJRgABAQEAYABgAAD/4QAWRXhpZgAASUkqAAgAAAAAAAAAAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAr/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AL+AAf/Z" }
   response = hdap.put do |h|
       h.path = 'dc=com/dc=example/ou=People/uid=bjensen'
       h.body = JSON.generate(photo)
   end

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [binary-add.rb](../_attachments/hdap/rb/binary-add.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Read a binary resource

1. Read the binary resource as a base64-encoded JSON string.

   The following example reads Babs Jensen's profile photo:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --cacert ca-cert.pem \
    --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=photo&_prettyPrint=true'
   ```

   > **Collapse: Show output**
   >
   > ```
   > {
   >   "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
   >   "_rev" : "<revision>",
   >   "photo" : [ "/9j/4AAQSkZJRgABAQEAYABgAAD/4QAWRXhpZgAASUkqAAgAAAAAAAAAAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/2wBDAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQH/wAARCAABAAEDASIAAhEBAxEB/8QAFQABAQAAAAAAAAAAAAAAAAAAAAr/xAAUEAEAAAAAAAAAAAAAAAAAAAAA/8QAFAEBAAAAAAAAAAAAAAAAAAAAAP/EABQRAQAAAAAAAAAAAAAAAAAAAAD/2gAMAwEAAhEDEQA/AL+AAf/Z" ]
   > }
   > ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       const resource = '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=photo'
       const options = getOptions({ path: resource })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: read photo', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [binary-read.js](../_attachments/hdap/js/binary-read.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   params = { '_fields': 'photo' }
   jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   response = requests.get(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
       headers=headers,
       params=params,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [binary-read.py](../_attachments/hdap/py/binary-read.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'

   utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   fields = { "_fields": "photo" }
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [binary-read.rb](../_attachments/hdap/rb/binary-read.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

---

---
title: Create
description: Create directory resources in PingDS over HTTP using HDAP with HTTP PUT or POST operations.
component: pingds
version: 8.1
page_id: pingds:rest-guide:create-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/create-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  rest-create: Create (HTTP PUT)
  rest-action-create: Create (HTTP POST)
---

# Create

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

Before creating a resource, you can [get its JSON schema](action-rest.html#action-schema) if you know its LDAP object classes.

## Create (HTTP PUT)

Use HTTP PUT with the headers `Content-Type: application/json` and `If-None-Match: *`. The payload is the JSON resource:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request PUT \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --header 'If-None-Match: *' \
 --data '{
  "_id" : "dc=com/dc=example/ou=People/uid=newuser",
  "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
  "cn" : [ "New User" ],
  "givenName" : [ "New" ],
  "mail" : [ "newuser@example.com" ],
  "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
  "sn" : [ "User" ],
  "telephoneNumber" : [ "+1 408 555 1212" ],
  "uid" : [ "newuser" ]
 }' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=newuser',
        method: 'PUT',
        body: {
            "_id": "dc=com/dc=example/ou=People/uid=newuser",
            "objectClass": ["person", "inetOrgPerson", "organizationalPerson", "top"],
            "cn": ["New User"],
            "givenName": ["New"],
            "mail": ["newuser@example.com"],
            "manager": ["dc=com/dc=example/ou=People/uid=bjensen"],
            "sn": ["User"],
            "telephoneNumber": ["+1 408 555 1212"],
            "uid": ["newuser"]
        }
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    options.headers['If-None-Match'] = '*'
    const response = await doRequest('HDAP: create with PUT', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [create.js](../_attachments/hdap/js/create.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

body = {
    '_id': 'dc=com/dc=example/ou=People/uid=newuser',
    'objectClass': ['person', 'inetOrgPerson', 'organizationalPerson', 'top'],
    'cn': ['New User'],
    'givenName': ['New'],
    'mail': ['newuser@example.com'],
    'manager': ['dc=com/dc=example/ou=People/uid=bjensen'],
    'sn': ['User'],
    'telephoneNumber': ['+1 408 555 1212'],
    'uid': ['newuser']
}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = {
    'Authorization': f'Bearer {jwt}',
    'Content-Type': 'application/json',
    'If-None-Match': '*'
}
response = requests.put(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=newuser',
    headers=headers,
    json=body,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [create.py](../_attachments/hdap/py/create.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
body = {
    '_id' => "dc=com/dc=example/ou=People/uid=newuser",
    'objectClass' => ["person", "inetOrgPerson", "organizationalPerson", "top"],
    'cn' => ["New User"],
    'givenName' => ["New"],
    'mail' => ["newuser@example.com"],
    'manager' => ["dc=com/dc=example/ou=People/uid=bjensen"],
    'sn' => ["User"],
    'telephoneNumber' => ["+1 408 555 1212"],
    'uid' => ["newuser"]
}
response = hdap.put do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=newuser'
    h.body = JSON.generate(body)
    h.headers['If-None-Match'] = '*'
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [create.rb](../_attachments/hdap/rb/create.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Create (HTTP POST)

Use HTTP POST with the header `Content-Type: application/json` and, optionally, the parameter `_action=create`. The payload is the JSON resource:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --cacert ca-cert.pem \
 --user uid=admin:password \
 --header 'Content-Type: application/json' \
 --data '{
  "_id" : "dc=com/dc=example/ou=People/uid=newuser",
  "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
  "cn" : [ "New User" ],
  "givenName" : [ "New" ],
  "mail" : [ "newuser@example.com" ],
  "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
  "sn" : [ "User" ],
  "telephoneNumber" : [ "+1 408 555 1212" ],
  "uid" : [ "newuser" ]
 }' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People?_action=create&_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People?_action=create',
        method: 'POST',
        body: {
            "_id": "dc=com/dc=example/ou=People/uid=newuser",
            "objectClass": ["person", "inetOrgPerson", "organizationalPerson", "top"],
            "cn": ["New User"],
            "givenName": ["New"],
            "mail": ["newuser@example.com"],
            "manager": ["dc=com/dc=example/ou=People/uid=bjensen"],
            "sn": ["User"],
            "telephoneNumber": ["+1 408 555 1212"],
            "uid": ["newuser"]
        }
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: create with POST', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [create-post.js](../_attachments/hdap/js/create-post.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

body = {
    '_id': 'dc=com/dc=example/ou=People/uid=newuser',
    'objectClass': ['person', 'inetOrgPerson', 'organizationalPerson', 'top'],
    'cn': ['New User'],
    'givenName': ['New'],
    'mail': ['newuser@example.com'],
    'manager': ['dc=com/dc=example/ou=People/uid=bjensen'],
    'sn': ['User'],
    'telephoneNumber': ['+1 408 555 1212'],
    'uid': ['newuser']
}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.post(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    headers=headers,
    json=body,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [create-post.py](../_attachments/hdap/py/create-post.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
body = {
    '_id' => "dc=com/dc=example/ou=People/uid=newuser",
    'objectClass' => ["person", "inetOrgPerson", "organizationalPerson", "top"],
    'cn' => ["New User"],
    'givenName' => ["New"],
    'mail' => ["newuser@example.com"],
    'manager' => ["dc=com/dc=example/ou=People/uid=bjensen"],
    'sn' => ["User"],
    'telephoneNumber' => ["+1 408 555 1212"],
    'uid' => ["newuser"]
}
response = hdap.post do |h|
    h.path = 'dc=com/dc=example/ou=People'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [create-post.rb](../_attachments/hdap/rb/create-post.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

---

---
title: Delete
description: Delete individual resources, specific revisions, or entire subtrees in PingDS over HTTP using the HDAP API.
component: pingds
version: 8.1
page_id: pingds:rest-guide:delete-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/delete-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  delete_a_resource: Delete a resource
  delete_a_specific_revision: Delete a specific revision
  delete_a_subtree: Delete a subtree
---

# Delete

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

## Delete a resource

Use HTTP DELETE on the resource URL. HDAP returns the resource you deleted:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request DELETE \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=newuser',
        method: 'DELETE'
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: delete newuser', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [delete.js](../_attachments/hdap/js/delete.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.delete(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=newuser',
    headers=headers,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [delete.py](../_attachments/hdap/py/delete.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.delete('dc=com/dc=example/ou=People/uid=newuser')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [delete.rb](../_attachments/hdap/rb/delete.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Delete a specific revision

To delete a resource only if the resource matches a particular version, use an `If-Match: <revision>` header:

* Curl

* JavaScript

* Python

* Ruby

```console
$ export JWT=$(echo $(curl \
 --request POST \
 --cacert ca-cert.pem \
 --header 'Content-Type: application/json' \
 --data '{ "password": "bribery" }' \
 --silent \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_action=authenticate') | jq -r .access_token)
$ export REVISION=$(cut -d \" -f 8 <(curl \
 --get \
 --cacert ca-cert.pem \
 --header "Authorization: Bearer $JWT" \
 --header 'Content-Type: application/json' \
 --data '_fields=_rev' \
 --silent \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser'))
$ curl \
 --request DELETE \
 --cacert ca-cert.pem \
 --header "Authorization: Bearer $JWT" \
 --header "If-Match: $REVISION" \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=newuser?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=newuser",
>   "objectClass" : [ "person", "inetOrgPerson", "organizationalPerson", "top" ],
>   "cn" : [ "New User" ],
>   "givenName" : [ "New" ],
>   "mail" : [ "newuser@example.com" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=bjensen" ],
>   "sn" : [ "User" ],
>   "telephoneNumber" : [ "+1 408 555 1212" ],
>   "uid" : [ "newuser" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=newuser'
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    let response = await doRequest('HDAP: read newuser _rev', options)
    console.log(response)
    options.headers['If-Match'] = JSON.parse(response.data)._rev
    options.method = 'DELETE'
    response = await doRequest('HDAP: delete specific revision', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [delete-rev.js](../_attachments/hdap/js/delete-rev.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
rev = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=newuser',
    headers=headers,
    verify=utils.ca_pem).json()['_rev']

headers['If-Match'] = rev
response = requests.delete(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=newuser',
    headers=headers,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [delete-rev.py](../_attachments/hdap/py/delete-rev.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
resource = 'dc=com/dc=example/ou=People/uid=newuser'
rev = JSON.parse(hdap.get(resource).body, symbolize_names: true)[:_rev]

response = hdap.delete do |h|
    h.path = resource
    h.headers['If-Match'] = rev
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [delete-rev.rb](../_attachments/hdap/rb/delete-rev.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Delete a subtree

|   |                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Only users granted access to perform a subtree delete can remove a resource with children.

* This can be a resource-intensive operation.

  The resources required to remove a branch depend on the number of LDAP entries to delete. |

To delete a resource and all of its children, follow these high-level steps:

* When configuring the gateway, make sure `"useSubtreeDelete": "true"` (default).

* Grant the user access to the subtree delete control:

  ```console
  $ dsconfig \
   set-access-control-handler-prop \
   --hostname localhost \
   --port 4444 \
   --bindDN uid=admin \
   --bindPassword password \
   --add global-aci:"(targetcontrol=\"SubtreeDelete\")(version 3.0; acl \"Allow Subtree Delete\"; allow(read) userdn=\"ldap:///uid=kvaughan,ou=People,dc=example,dc=com\";)" \
   --trustStorePath /path/to/opendj/config/keystore \
   --trustStoreType PKCS12 \
   --trustStorePassword:file /path/to/opendj/config/keystore.pin \
   --no-prompt
  ```

* Delete the base resource as a user with access to perform a subtree delete.

  Include the `subtreeDelete=true` query string parameter in the delete request.

---

---
title: HDAP and password policies
description: Use the PingDS HDAP API to create and assign a replicated subentry password policy with examples in multiple languages.
component: pingds
version: 8.1
page_id: pingds:rest-guide:rest-pwp
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/rest-pwp.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API", "Setup &amp; Configuration"]
---

# HDAP and password policies

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

This example demonstrates how to add a subentry password policy with HDAP. Subentry password policies are replicated.

This example uses Kirsten Vaughan as a password administrator. Kirsten is a member of the `Directory Administrators` group.

1. Before trying this example, make sure the password administrator has the necessary access:

   1. Grant the `subentry-write` privilege to edit password policies:

      * Curl

      * JavaScript

      * Python

      * Ruby

      ```console
      $ curl \
       --request PATCH \
       --cacert ca-cert.pem \
       --user uid=admin:password \
       --header 'Content-Type: application/json' \
       --data '[{
        "operation": "add",
        "field": "ds-privilege-name",
        "value": "subentry-write"
       }]' \
       'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_fields=_id,ds-privilege-name'
      ```

      ```javascript
      (async () => {
          const { authenticate, doRequest, getOptions } = require('./utils')
          const options = getOptions({
              path: '/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_fields=_id,ds-privilege-name',
              method: 'PATCH',
              credentials: 'uid=admin:password',
              body: [{
                  "operation": "add",
                  "field": "ds-privilege-name",
                  "value": "subentry-write"
              }]
          })
          const jwt = await authenticate(options)
          options.headers['Authorization'] = 'Bearer ' + jwt
          const response = await doRequest('HDAP: assign the subentry-write privilege', options)
          console.log(response)
      })().catch(error => { console.error(error) })
      ```

      Source files for this sample: [pwp-subentry-write.js](../_attachments/hdap/js/pwp-subentry-write.js), [utils.js](../_attachments/hdap/js/utils.js)

      ```python
      #!/usr/bin/env python3

      import requests
      import utils

      patch = [{
          'operation': 'add',
          'field': 'ds-privilege-name',
          'value': 'subentry-write'
      }]
      jwt = utils.authenticate('uid=admin', 'password')
      headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
      response = requests.patch(
          f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=kvaughan',
          headers=headers,
          json=patch,
          verify=utils.ca_pem)
      print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
      ```

      Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [pwp-subentry-write.py](../_attachments/hdap/py/pwp-subentry-write.py)

      ```ruby
      require_relative 'utils.rb'
      require 'faraday'
      require 'json'

      utils = Utils.new('uid=admin', 'password')
      options = { ca_file: utils.ca_pem }
      jwt = utils.authenticate
      query = { '_fields': '_id,ds-privilege-name' }
      hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
          f.headers['Content-Type'] = 'application/json'
          f.request :authorization, 'Bearer', jwt
      end
      body = [{
          "operation" => "add",
          "field" => "ds-privilege-name",
          "value" => "subentry-write"
      }]
      response = hdap.patch do |h|
          h.path = 'dc=com/dc=example/ou=People/uid=kvaughan'
          h.body = JSON.generate(body)
      end

      puts "Status code: #{response.status}\nJSON: #{response.body}"
      ```

      Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [pwp-subentry-write.rb](../_attachments/hdap/rb/pwp-subentry-write.rb)

      HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

   2. Grant access to manage password policies.

      * Curl

      * JavaScript

      * Python

      * Ruby

      ```console
      $ curl \
       --request PATCH \
       --cacert ca-cert.pem \
       --user uid=admin:password \
       --header 'Content-Type: application/json' \
       --url 'https://localhost:8443/hdap/dc=com/dc=example?_fields=_id,aci' \
       --data @- << JSON
      [{
        "operation": "add",
        "field": "aci",
        "value": "(targetattr = \"pwdPolicySubentry||ds-pwp-password-policy-dn||ds-pwp-password-validator||subtreeSpecification\")(version 3.0;acl \"Allow Administrators to manage user password policies\";allow (all) (groupdn = \"ldap:///cn=Directory Administrators,ou=Groups,dc=example,dc=com\");)"
      }]
      JSON
      ```

      ```javascript
      (async () => {
          const { authenticate, doRequest, getOptions } = require('./utils')
          const options = getOptions({
              path: '/hdap/dc=com/dc=example?_fields=_id,aci',
              method: 'PATCH',
              credentials: 'uid=admin:password',
              body: [{
                  "operation": "add",
                  "field": "aci",
                  "value": "(targetattr = \"pwdPolicySubentry||ds-pwp-password-policy-dn||ds-pwp-password-validator||subtreeSpecification\")(version 3.0;acl \"Allow Administrators to manage user password policies\";allow (all) (groupdn = \"ldap:///cn=Directory Administrators,ou=Groups,dc=example,dc=com\");)"
              }]
          })
          const jwt = await authenticate(options)
          options.headers['Authorization'] = 'Bearer ' + jwt
          const response = await doRequest('HDAP: grant access to manage password policies', options)
          console.log(response)
      })().catch(error => { console.error(error) })
      ```

      Source files for this sample: [pwp-admin-access.js](../_attachments/hdap/js/pwp-admin-access.js), [utils.js](../_attachments/hdap/js/utils.js)

      ```python
      #!/usr/bin/env python3

      import requests
      import utils

      patch = [{
          'operation': 'add',
          'field': 'aci',
          'value': '(targetattr = "pwdPolicySubentry||ds-pwp-password-policy-dn||ds-pwp-password-validator||subtreeSpecification")(version 3.0;acl "Allow Administrators to manage user password policies";allow (all) (groupdn = "ldap:///cn=Directory Administrators,ou=Groups,dc=example,dc=com");)'
      }]
      jwt = utils.authenticate('uid=admin', 'password')
      headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
      params = {'_fields': '_id,aci' }
      response = requests.patch(
          f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example',
          headers=headers,
          json=patch,
          params=params,
          verify=utils.ca_pem)
      print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
      ```

      Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [pwp-admin-access.py](../_attachments/hdap/py/pwp-admin-access.py)

      ```ruby
      require_relative 'utils.rb'
      require 'faraday'
      require 'json'

      utils = Utils.new('uid=admin', 'password')
      options = { ca_file: utils.ca_pem }
      jwt = utils.authenticate
      query = { '_fields': '_id,aci' }
      hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
          f.headers['Content-Type'] = 'application/json'
          f.request :authorization, 'Bearer', jwt
      end
      body = [{
          "operation" => "add",
          "field" => "aci",
          "value" => "(targetattr = \"pwdPolicySubentry||ds-pwp-password-policy-dn||ds-pwp-password-validator||subtreeSpecification\")(version 3.0;acl \"Allow Administrators to manage user password policies\";allow (all) (groupdn = \"ldap:///cn=Directory Administrators,ou=Groups,dc=example,dc=com\");)"
      }]
      response = hdap.patch do |h|
          h.path = 'dc=com/dc=example'
          h.body = JSON.generate(body)
      end

      puts "Status code: #{response.status}\nJSON: #{response.body}"
      ```

      Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [pwp-admin-access.rb](../_attachments/hdap/rb/pwp-admin-access.rb)

      HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

2. Create and assign a subentry password policy as the password administrator:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --request POST \
    --cacert ca-cert.pem \
    --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    --header 'Content-Type: application/json' \
    --url 'https://localhost:8443/hdap/dc=com/dc=example?_action=create&_fields=*,subtreeSpecification&_prettyPrint=true' \
    --data @- << JSON
   {
     "_id" : "dc=com/dc=example/cn=Replicated%20password%20policy",
     "objectClass" : [ "top", "subentry", "ds-pwp-password-policy", "ds-pwp-validator", "ds-pwp-length-based-validator" ],
     "cn" : [ "Replicated password policy" ],
     "ds-pwp-default-password-storage-scheme" : [ "PBKDF2-HMAC-SHA512" ],
     "ds-pwp-length-based-min-password-length" : 8,
     "ds-pwp-password-attribute" : "userPassword",
     "subtreeSpecification": { "base": "ou=People", "filter": "/objectClass eq \"person\"" }
    }
   JSON
   ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       const options = getOptions({
           path: '/hdap/dc=com/dc=example?_action=create&_fields=*,subtreeSpecification',
           method: 'POST',
           body: {
               "_id": "dc=com/dc=example/cn=Replicated%20password%20policy",
               "objectClass": ["top", "subentry", "ds-pwp-password-policy", "ds-pwp-validator", "ds-pwp-length-based-validator"],
               "cn": ["Replicated password policy"],
               "ds-pwp-default-password-storage-scheme": ["PBKDF2-HMAC-SHA512"],
               "ds-pwp-length-based-min-password-length": 8,
               "ds-pwp-password-attribute": "userPassword",
               "subtreeSpecification": { "base": "ou=People", "filter": "/objectClass eq \"person\"" }
           }
       })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: create password policy', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [pwp-add-policy.js](../_attachments/hdap/js/pwp-add-policy.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   body = {
       '_id': 'dc=com/dc=example/cn=Replicated%20password%20policy',
       'objectClass': ['top', 'subentry', 'ds-pwp-password-policy', 'ds-pwp-validator', 'ds-pwp-length-based-validator'],
       'cn': ['Replicated password policy'],
       'ds-pwp-default-password-storage-scheme': ['PBKDF2-HMAC-SHA512'],
       'ds-pwp-length-based-min-password-length': 8,
       'ds-pwp-password-attribute': 'userPassword',
       'subtreeSpecification': { "base": "ou=people", "filter": "/objectClass eq \"person\"" }
   }
   jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   params = { '_fields': '*,subtreeSpecification' }
   response = requests.post(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example',
       headers=headers,
       json=body,
       params=params,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [pwp-add-policy.py](../_attachments/hdap/py/pwp-add-policy.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'
   require 'json'

   utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   query = { '_fields': '*,subtreeSpecification' }
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   body = {
       "_id": "dc=com/dc=example/cn=Replicated%20password%20policy",
       "objectClass": ["top", "subentry", "ds-pwp-password-policy", "ds-pwp-validator", "ds-pwp-length-based-validator"],
       "cn": ["Replicated password policy"],
       "ds-pwp-default-password-storage-scheme": ["PBKDF2-HMAC-SHA512"],
       "ds-pwp-length-based-min-password-length": 8,
       "ds-pwp-password-attribute": "userPassword",
       "subtreeSpecification": { "base": "ou=People", "filter": "/objectClass eq \"person\"" }
   }
   response = hdap.post do |h|
       h.path = 'dc=com/dc=example'
       h.body = JSON.generate(body)
   end

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [pwp-add-policy.rb](../_attachments/hdap/rb/pwp-add-policy.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

3. Verify the password administrator can view which password policy applies:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --cacert ca-cert.pem \
    --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_fields=_id,pwdPolicySubentry&_prettyPrint=true'
   ```

   > **Collapse: Show output**
   >
   > ```
   > {
   >   "_id" : "dc=com/dc=example/ou=People/uid=kvaughan",
   >   "_rev" : "<revision>",
   >   "pwdPolicySubentry" : "dc=com/dc=example/cn=Replicated%20password%20policy"
   > }
   > ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       // Kirsten Vaughan is the password administrator in this example.
       const options = getOptions({
           path: '/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_fields=_id,pwdPolicySubentry'
       })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: read pwp as admin', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [pwp-read-pol-as-admin.js](../_attachments/hdap/js/pwp-read-pol-as-admin.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   params = { '_fields': '_id,pwdPolicySubentry' }
   # Kirsten Vaughan is the password administrator in this example.
   jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   response = requests.get(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
       headers=headers,
       params=params,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [pwp-read-pol-as-admin.py](../_attachments/hdap/py/pwp-read-pol-as-admin.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'

   # Kirsten Vaughan is the password administrator in this example.
   utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   fields = { "_fields": "_id,pwdPolicySubentry" }
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [pwp-read-pol-as-admin.rb](../_attachments/hdap/rb/pwp-read-pol-as-admin.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

4. Verify the field is not visible to regular users:

   * Curl

   * JavaScript

   * Python

   * Ruby

   ```console
   $ curl \
    --cacert ca-cert.pem \
    --user dc=com/dc=example/ou=People/uid=bjensen:hifalutin \
    'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=_id,pwdPolicySubentry&_prettyPrint=true'
   ```

   > **Collapse: Show output**
   >
   > ```
   > {
   >   "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
   >   "_rev" : "<revision>"
   > }
   > ```

   ```javascript
   (async () => {
       const { authenticate, doRequest, getOptions } = require('./utils')
       const options = getOptions({
           path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=_id,pwdPolicySubentry',
           credentials: 'dc=com/dc=example/ou=People/uid=bjensen:hifalutin'
       })
       const jwt = await authenticate(options)
       options.headers['Authorization'] = 'Bearer ' + jwt
       const response = await doRequest('HDAP: read pwp as user', options)
       console.log(response)
   })().catch(error => { console.error(error) })
   ```

   Source files for this sample: [pwp-read-pol-as-user.js](../_attachments/hdap/js/pwp-read-pol-as-user.js), [utils.js](../_attachments/hdap/js/utils.js)

   ```python
   #!/usr/bin/env python3

   import requests
   import utils

   params = { '_fields': '_id,pwdPolicySubentry' }
   jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
   headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
   response = requests.get(
       f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
       headers=headers,
       params=params,
       verify=utils.ca_pem)
   print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
   ```

   Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [pwp-read-pol-as-user.py](../_attachments/hdap/py/pwp-read-pol-as-user.py)

   ```ruby
   require_relative 'utils.rb'
   require 'faraday'

   utils = Utils.new('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
   options = { ca_file: utils.ca_pem }
   jwt = utils.authenticate
   fields = { "_fields": "_id,pwdPolicySubentry" }
   hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
       f.headers['Content-Type'] = 'application/json'
       f.request :authorization, 'Bearer', jwt
   end
   response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

   puts "Status code: #{response.status}\nJSON: #{response.body}"
   ```

   Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [pwp-read-pol-as-user.rb](../_attachments/hdap/rb/pwp-read-pol-as-user.rb)

   HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

When listing subentry password policies, use the `subentries=true` parameter:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --get \
 --cacert ca-cert.pem \
 --user uid=admin:password \
 --data "_queryFilter=/objectClass+eq+'ds-pwp-password-policy'" \
 --data '_fields=*,subtreeSpecification' \
 --data 'subentries=true' \
 --data '_prettyPrint=true' \
 'https://localhost:8443/hdap/dc=com/dc=example'
```

> **Collapse: Show output**
>
> ```
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/cn=Replicated%20password%20policy",
>     "_rev" : "<revision>",
>     "objectClass" : [ "top", "subentry", "ds-pwp-password-policy", "ds-pwp-validator", "ds-pwp-length-based-validator" ],
>     "cn" : [ "Replicated password policy" ],
>     "ds-pwp-default-password-storage-scheme" : [ "PBKDF2-HMAC-SHA512" ],
>     "ds-pwp-length-based-min-password-length" : 8,
>     "ds-pwp-password-attribute" : "userPassword",
>     "subtreeSpecification" : {
>       "filter" : "/objectClass eq \"person\"",
>       "base" : "ou=People"
>     }
>   } ],
>   "resultCount" : 1,
>   "pagedResultsCookie" : null,
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const filter = "/objectClass+eq+'ds-pwp-password-policy'"
    const parameters = 'subentries=true&_fields=*,subtreeSpecification'
    const options = getOptions({
        path: `/hdap/dc=com/dc=example?_queryFilter=${filter}&${parameters}`,
        credentials: 'uid=admin:password'
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: query subentry password policies', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [pwp-query.js](../_attachments/hdap/js/pwp-query.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

params = {
    '_fields': '*,subtreeSpecification',
    '_queryFilter': '/objectClass eq "ds-pwp-password-policy"',
    'subentries': True
}
jwt = utils.authenticate('uid=admin', 'password')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example',
    headers=headers,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [pwp-query.py](../_attachments/hdap/py/pwp-query.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('uid=admin', 'password')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = {
    "_fields": "*,subtreeSpecification",
    "_queryFilter": "/objectClass eq 'ds-pwp-password-policy'",
    "subentries": true
}
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [pwp-query.rb](../_attachments/hdap/rb/pwp-query.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

For details about policy settings, refer to [DS subentry password policies](../security-guide/pwp-about.html#pwp-replicated).

---

---
title: HDAP API reference
description: "Reference for the PingDS HDAP API: resources, operations, authentication, query parameters, and HTTP status codes."
component: pingds
version: 8.1
page_id: pingds:rest-guide:rest-operations
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/rest-operations.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  authenticate-rest: Authentication
  authenticate-rest-anon: Anonymous
  authenticate-rest-basic: Basic auth
  authenticate-rest-bearer: Bearer auth
  resources: Resources
  fields: Fields
  values: Values
  hdap-schema: Schema
  operations: Operations
  create: Create
  read: Read
  update: Update
  delete: Delete
  patch: Patch
  patch-add: Add
  patch-remove: Remove
  patch-replace: Replace
  patch-increment: Increment
  action: Action
  query: Query
  headers: Headers
  accept_api_version: Accept-API-Version
  x_forgerock_transactionid: X-ForgeRock-TransactionId
  query-parameters: Query parameters
  filter-expressions: Filter expressions
  http-status-codes: HTTP status codes
---

# HDAP API reference

HDAP APIs offer HTTP access to directory data as [JSON](https://json.org) resources. DS software maps JSON resources to LDAP entries.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

## Authentication

### Anonymous

When you perform an operation without authenticating, HDAP responds like LDAP:

* If DS access control lets anonymous users perform the operation, the operation returns the expected result.

  The `ds-evaluation` profile lets anonymous users read and search many attributes.

* If anonymous users can't perform the operation, HDAP returns HTTP 401 Unauthorized.

  HTTP status code 401 means the user must authenticate.

- Curl

- JavaScript

- Python

- Ruby

```console
$ curl \
 --cacert ca-cert.pem \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen'
```

```javascript
const { doRequest, getOptions } = require('./utils')

const options = getOptions({
    path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers: { 'Content-Type': 'application/json' }
})

doRequest('HDAP: anonymous read', options)
    .then(response => { console.log(response) })
    .catch(error => { console.error(error) })
```

Source files for this sample: [anonymous-read.js](../_attachments/hdap/js/anonymous-read.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [anonymous-read.py](../_attachments/hdap/py/anonymous-read.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('', '')
options = { ca_file: utils.ca_pem }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
end
response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [anonymous-read.rb](../_attachments/hdap/rb/anonymous-read.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

### Basic auth

HDAP supports [HTTP Basic authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication#basic_authentication_scheme) with the `_id` of resource as the HTTP username. The `_id` matches the suffix of the path to the resource.

When you set up DS with the `ds-evaluation` profile, Babs Jensen's `_id` is `dc=com/dc=example/ou=People/uid=bjensen`.

Use HTTPS to avoid sending the password over an insecure connection.

* Curl

* JavaScript

* Python

* Ruby

HTTP Basic authentication

```console
$ curl \
 --user dc=com/dc=example/ou=People/uid=bjensen:hifalutin \
 --cacert ca-cert.pem \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=cn'
```

> **Collapse: Show output**
>
> ```
> {"_id":"dc=com/dc=example/ou=People/uid=bjensen","_rev":"<revision>","cn":["Barbara Jensen","Babs Jensen"]}
> ```

HTTP Basic with credentials in the URL

```console
$ curl \
 --cacert ca-cert.pem \
 'https://dc=com%2Fdc=example%2Fou=People%2Fuid=bjensen:hifalutin@localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=cn'
```

> **Collapse: Show output**
>
> ```
> {"_id":"dc=com/dc=example/ou=People/uid=bjensen","_rev":"<revision>","cn":["Barbara Jensen","Babs Jensen"]}
> ```

```javascript
const { doRequest, getOptions } = require('./utils')

const options = getOptions({
    path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=cn',
    credentials: 'dc=com/dc=example/ou=People/uid=bjensen:hifalutin'
})

doRequest('HDAP: Basic auth', options)
    .then(response => { console.log(response) })
    .catch(error => { console.error(error) })
```

Source files for this sample: [basic-auth.js](../_attachments/hdap/js/basic-auth.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
from requests.auth import HTTPBasicAuth
import utils

response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    auth=HTTPBasicAuth('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin'),
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [basic-auth.py](../_attachments/hdap/py/basic-auth.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('', '')
options = { ca_file: utils.ca_pem }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: { '_fields': 'cn' }, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, :basic, 'dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin'
end
response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [basic-auth.rb](../_attachments/hdap/rb/basic-auth.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

### Bearer auth

HDAP supports HTTP Bearer authorization using an access token. The access token is a JSON Web Token (JWT) DS returns for a successful authentication action.

|   |                                                                                                                                                                                                                                                                                                                                                                                      |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Using a JWT bearer token for authorization means DS only has to authenticate the user once during the lifetime of the token.Use this when performing multiple operations as a user with a strong password storage scheme. The computational cost to validate the password is high, but you only pay the cost once. The cost to validate a JWT token is low for each later operation. |

Use HTTPS POST to the path for the account to authenticate with `_action=authenticate` in the query string and a JSON object `{ "password": "<password>" }` as the request payload.

On success, the HTTP status code is 200 OK, and the response body is a JSON resource with an `access_token`. Use the bearer token to authorize later HTTP requests.

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request POST \
 --header 'Content-Type: application/json' \
 --data '{ "password": "hifalutin" }' \
 --cacert ca-cert.pem \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_action=authenticate'
```

> **Collapse: Show output**
>
> ```
> {"access_token":"<jwt>","expires_in":"299","token_type":"Bearer"}
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const resource = '/hdap/dc=com/dc=example/ou=People/uid=bjensen'
    const options = getOptions({ path: resource })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: JWT auth', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [basic-auth.js](../_attachments/hdap/js/bearer-auth.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [basic-auth.py](../_attachments/hdap/py/bearer-auth.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: { '_fields': 'cn' }, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [basic-auth.rb](../_attachments/hdap/rb/bearer-auth.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

Learn about alternative authentication options:

* [Configure HTTP authorization](../config-guide/http-access.html#setup-http-authorization)

* [Identity mappers](../ldap-guide/client-auth.html#client-auth-identity-mappers)

## Resources

HDAP resources are JSON objects whose top-level elements are fields with string identifiers; for example:

```json
{
  "_id" : "dc=com/dc=example/ou=People/uid=user.0",
  "_rev" : "0d3ce3bf-4107-3b34-9e5a-fa71deb8b504",
  "objectClass" : [ "top", "person", "organizationalPerson", "inetOrgPerson" ],
  "cn" : [ "Aaccf Amar" ],
  "description" : [ "This is the description for Aaccf Amar." ],
  "employeeNumber" : "0",
  "givenName" : [ "Aaccf" ],
  "homePhone" : [ "+1 720 204 9090" ],
  "initials" : [ "AAA" ],
  "l" : [ "Harrisonburg" ],
  "mail" : [ "user.0@example.com" ],
  "mobile" : [ "+1 412 030 0042" ],
  "pager" : [ "+1 439 180 6470" ],
  "postalAddress" : [ "Aaccf Amar$31206 Spring Street$Harrisonburg, IL  04284" ],
  "postalCode" : [ "04284" ],
  "sn" : [ "Amar" ],
  "st" : [ "IL" ],
  "street" : [ "31206 Spring Street" ],
  "telephoneNumber" : [ "+1 485 381 2060" ],
  "uid" : [ "user.0" ]
}
```

HDAP resources have the following special fields:

* `_id`

  Unique identifier.

  The resource `_id` matches the trailing components of its path. For example, the resource at `/hdap/dc=com/dc=example/ou=People/uid=bjensen` has `"_id":"dc=com/dc=example/ou=People/uid=bjensen"`.

  The path elements of an `_id` are URL path-encoded RDN strings. When you create a resource:

  * Percent-encode each path element.

  * If the path element includes characters to escape in LDAP, `" # + , ; < = > \`, escape those characters in the LDAP RDN string before percent-encoding the result for HDAP.

  | CN value      | LDAP RDN           | HDAP path element     |
  | ------------- | ------------------ | --------------------- |
  | `Babs Jensen` | `cn=Babs Jensen`   | `cn=Babs%20Jensen`    |
  | `Babs/Jensen` | `cn=Babs/Jensen`   | `cn=Babs%2FJensen`    |
  | `Babs\Jensen` | `cn=Babs\\Jensen`  | `cn=Babs%5C%5CJensen` |
  | `Babs,Jensen` | `cn=Babs\2CJensen` | `cn=Babs%5C2Jensen`   |

* `_rev`

  The resource revision.

  HDAP versions individual resources with revision numbers corresponding to the LDAP `ETag` operational attribute. HDAP uses the `If-Match: <revision>` header to determine whether to apply changes to a resource.

The other JSON fields have the same names as the LDAP attributes they represent.

### Fields

Multivalued LDAP attributes correspond to arrays in JSON. Unlike arrays in JavaScript, these arrays have set semantics. No duplicates are allowed and the element order is arbitrary.

By default, HDAP behaves like a normal LDAP client application, returning JSON fields for all non-empty LDAP user attributes.

* To return JSON fields for operational LDAP attributes, request them specifically with the `_fields` parameter.

  Use `+`, which encodes to `%2B`, to return fields for all operational attributes.

* To return empty fields, set the advanced HDAP endpoint configuration property `return-null-for-missing-properties:true`.

  With the feature enabled, HDAP returns empty single-valued fields as `null` and empty multivalued fields as `[]`, except for password fields, which HDAP returns as an array even if they are constrained to being single-valued.

  access control instruction (ACI) *(tooltip: \<div class="paragraph">
  \<p>An instruction or rule that can be used to grant or deny access to users to perform operations on a server.\</p>
  \</div>)* `deny` rules can cause misleading results, where an "empty" attribute exists, but you can't read it. Check the applicable ACIs when HDAP doesn't return an expected field.

* To return field names as specified with the `_fields` query parameter or as stored in the LDAP entry, set the HDAP endpoint configuration property `normalize-attribute-names:false`.

  By default, HDAP returns resources with normalized field names.

### Values

HDAP derives its resource field values from LDAP attribute values based on the attribute syntax.

| LDAP attribute type   | LDAP example                                                                                                           | JSON field type                                                                                                  | JSON example                                                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| ACI                   | `(targetattr="userPassword")(version 3.0; acl "Read own password";allow (read,search,compare) userdn="ldap:///self";)` | ACI string[1](#hdap-values-footnote-strings)                                                                     | `(targetattr=\"userPassword\")(version 3.0; acl \"Read own password\";allow (read,search,compare) userdn=\"ldap:///self\";)` |
| Binary                | A binary photo or a certificate                                                                                        | Base64-encoded string                                                                                            | A base64-encoded photo or certificate                                                                                        |
| Boolean               | `true`                                                                                                                 | Boolean                                                                                                          | `true`                                                                                                                       |
| DN                    | `uid=bjensen,ou=People,dc=example,dc=com`                                                                              | `_id` string                                                                                                     | `dc=com/dc=example/ou=People/uid=bjensen`                                                                                    |
| JSON                  | `{"array":[{"x":1,"y":2},{"x":3,"y":4}]}`                                                                              | JSON                                                                                                             | `{"array":[{"x":1,"y":2},{"x":3,"y":4}]}`                                                                                    |
| Number                | `42`                                                                                                                   | Number                                                                                                           | `42`                                                                                                                         |
| Password              | A password hash                                                                                                        | Password string                                                                                                  | The same password hash                                                                                                       |
| Postal address        | `1234 Main St.$Anytown, CA 12345$USA`                                                                                  | Array of strings[1](#hdap-values-footnote-strings)                                                               | `["1234 Main St.","Anytown, CA 12345","USA"]`                                                                                |
| String                | `Hello world!`                                                                                                         | String[1](#hdap-values-footnote-strings)                                                                         | `Hello world!`                                                                                                               |
| Subtree specification | `{ base "ou=people", specificationFilter "(uid=bjensen)" }`                                                            | Subtree specification object[1](#hdap-values-footnote-strings),[2](#hdap-values-footnote-subtree-specifications) | `{ "base": "ou=people", "filter": "uid eq \"bjensen\"" }`                                                                    |
| Telephone number      | `+1 408 555 1212`                                                                                                      | Telephone number string                                                                                          | `+1 408 555 1212`                                                                                                            |
| Time                  | `20230622065924Z`                                                                                                      | ISO 8601 string                                                                                                  | `2023-06-22T06:59:24Z`                                                                                                       |
| UUID                  | `597ae2f6-16a6-1027-98f4-d28b5365dc14`                                                                                 | UUID string                                                                                                      | `597ae2f6-16a6-1027-98f4-d28b5365dc14`                                                                                       |

1 JSON strings are enclosed in double quotes, so double quotes are escaped with a backslash `\"`.

2 DS supports more subtree specification features than demonstrated in this simple example. For complex subtree specifications, add an example from LDIF, read the resource, and review the resulting JSON.

### Schema

HDAP provides two ways to read [JSON schema](https://json-schema.org/) for resources:

* Read the schema for an existing resource or a resource to create with [the `schema` action](action-rest.html#action-schema).

* Read the schema for an individual field or object class directly.

  The fields map to LDAP attribute types. A resource's `objectClass` values map to LDAP object classes.

  | To read the schema for | Use                                                                                                                                              |
  | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
  | An individual field.   | HTTP GET on `schemas/attributeTypes/type`:```http
  GET /hdap/schemas/attributeTypes/cn HTTP/1.1
  Host: example.com
  Accept: application/json
  ```    |
  | An object class.       | HTTP GET on `schemas/objectClasses/class`:```http
  GET /hdap/schemas/objectClasses/person HTTP/1.1
  Host: example.com
  Accept: application/json
  ``` |

## Operations

HDAP APIs support the following operations:

| HDAP operation    | Description                             | HTTP method |
| ----------------- | --------------------------------------- | ----------- |
| [Create](#create) | Add a new resource                      | PUT or POST |
| [Read](#read)     | Retrieve a single resource              | GET         |
| [Update](#update) | Replace content in an existing resource | PUT         |
| [Delete](#delete) | Remove an existing resource             | DELETE      |
| [Patch](#patch)   | Modify an existing resource             | PATCH       |
| [Action](#action) | Perform a predefined action             | POST        |
| [Query](#query)   | List resources                          | GET         |

### Create

Use either HTTP POST or HTTP PUT.

Use HTTP POST with the query string parameter `_action=create` and the JSON resource as a payload. Accept a JSON response. HDAP builds the `_id` using the parent resource path and the field in the resource corresponding to the LDAP RDN:

```http
POST /hdap/dc=com/dc=example/ou=People?_action=create HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
{ JSON resource }
```

Use HTTP PUT with the `_id` in the resource and the URL path. Use the `If-None-Match: *` header. Accept a JSON response:

```http
PUT /hdap/dc=com/dc=example/ou=People/uid=newuser HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-None-Match: *
{ JSON resource }
```

The response indicates the resource location in the `Location` header.

* If you include the `If-None-Match` header, you must use `If-None-Match: *`.

  The request creates the object if it does not exist. It fails if the object does exist.

  If you include any value other `If-None-Match: *`, HDAP returns an HTTP 400 Bad Request error. For example, creating an object with `If-None-Match: revision` returns a bad request error.

* If you do not include `If-None-Match: *`, the request creates the object if it does not exist and *updates* the object if it does exist.

Supported [parameters](#query-parameters):

* `_action=create`

* `dryRun=true`

* `_fields`

* `manageDsaIT=true`

* `passwordQualityAdvice=true`

* `_prettyPrint=true`

* `relax=true`

Learn more in [Create](create-rest.html).

### Read

Read a resource with HTTP GET and accept a JSON response:

```http
GET /hdap/dc=com/dc=example/ou=People/uid=newuser HTTP/1.1
Host: example.com
Accept: application/json
```

Supported [parameters](#query-parameters):

* `_fields`

* `manageDsaIT=true`

* `_prettyPrint=true`

Learn more in [Read](read-rest.html).

### Update

Update a resource with HTTP PUT and the JSON resource as the payload. Accept a JSON response.

* Unlike other Common REST applications, HDAP does not require the full JSON resource.

  HDAP replaces the fields in the resource with the fields in the payload, operating like a patch [Replace](#patch-replace). Other fields retain their existing values.

* Use the `If-Match: _rev` header to update the resource only if the revision matches.

  Use `If-Match: *` to apply the update irrespective of the revision.

```http
PUT /hdap/dc=com/dc=example/ou=People/uid=newuser HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-Match: _rev
{ JSON resource }
```

Supported [parameters](#query-parameters):

* `dryRun=true`

* `_fields`

* `manageDsaIT=true`

* `passwordQualityAdvice=true`

* `_prettyPrint=true`

* `relax=true`

Learn more in [Update](update-rest.html).

### Delete

Use HTTP DELETE and accept a JSON response:

```http
DELETE /hdap/dc=com/dc=example/ou=People/uid=newuser HTTP/1.1
Host: example.com
Accept: application/json
```

Supported [parameters](#query-parameters):

* `dryRun=true`

* `_fields`

* `manageDsaIT=true`

* `_prettyPrint=true`

* `subtreeDelete=true`

Learn more in [Delete](delete-rest.html).

### Patch

Use HTTP PATCH request with a JSON array of patch objects appropriate to the operation. Each patch object in the payload can have these fields:

* `operation`

  HDAP supports these patch operations:

  * [`add`](#patch-add)

  * [`remove`](#patch-remove)

  * [`replace`](#patch-replace)

  * [`increment`](#patch-increment)

HDAP does not support the common REST `copy`, `move`, or `transform` operations.

* `field`

  A JSON pointer to the target field

* `value`

  The value for the patch

The patch request has the following format:

```http
PATCH /hdap/dc=com/dc=example/ou=People/uid=newuser HTTP/1.1
Host: example.com
Accept: application/json
Content-Length: ...
Content-Type: application/json
If-Match: _rev
[ JSON array of patch operations ]
```

Patch operations apply to these types of target fields:

* **Single-valued**, such as an object, string, boolean, or number.

* **Set semantics array**, where the elements are not ordered and duplicates are not allowed.

  If you reference array values by index, HDAP returns an error.

Supported [parameters](#query-parameters):

* `dryRun=true`

* `_fields`

* `manageDsaIT=true`

* `passwordQualityAdvice=true`

* `_prettyPrint=true`

* `relax=true`

Learn more in [Patch](patch-rest.html).

#### Add

Patch `add` ensures the target field contains the value provided, creating parent fields as necessary.

* If the target field is single-valued and a value already exists, HDAP replaces the value with the value you provide.

  *HDAP does not return an error when adding a value to a single-valued field with an existing value.*

* If the target field is multivalued (an array), HDAP merges the array of values you provide with the existing values.

  For arrays, HDAP adds new values and ignores duplicates.

Add a telephone number

```javascript
[{
  "operation" : "add",
  "field" : "/telephoneNumber",
  "value" : "+1 408 555 1212"
}]
```

#### Remove

Patch `remove` ensures the target field does not contain the value provided.

* If you do not provide a value and the target field exists, HDAP removes the entire field.

* If you provide a value and the target field is single-valued, the value must match the existing value to remove; otherwise, HDAP does not change the field.

* If the target field is multivalued, HDAP removes the values in the array you provide from the existing set of values.

Remove all telephone numbers

```javascript
[{
  "operation" : "remove",
  "field" : "/telephoneNumber"
}]
```

Remove a specific telephone number

```javascript
[{
  "operation" : "remove",
  "field" : "/telephoneNumber",
  "value" : "+1 408 555 1212"
}]
```

#### Replace

Patch `replace` removes existing values on the target field and replaces them with the values you provide. It is equivalent to a `remove` of the field followed by an `add`.

Reset the telephone number

```javascript
[{
  "operation" : "replace",
  "field" : "/telephoneNumber",
  "value" : "+1 408 555 1212"
}]
```

#### Increment

Patch `increment` changes the value(s) in the target field by the amount you specify.

* Use a positive number to increment or a negative number to decrement the value(s).

* The target field must hold a number or a set of numbers.

* The value you provide must be a single number.

Lower the temperature

```javascript
[{
  "operation" : "increment",
  "field" : "/temperature",
  "value" : -2
}]
```

### Action

Use HTTP POST with the `_action` parameter to request a predefined action.

* `_action=accountUsability`: Determine whether the user can authenticate to the directory.

* `_action=create`: Create a resource with HTTP POST.

* `_action=modifyPassword`: Change your password.

* `_action=rename`: Rename a resource, changing its `_id`.

* `_action=resetPassword`: Change another user's password.

* `_action=schema`: Get the JSON schema for an object.

Supported [parameters](#query-parameters):

* `_action`

* `deleteOldRdn=true` (rename operation)

* `dryRun=true` (create, password, and rename operations)

* `_fields`

* `manageDsaIT=true` (rename operation)

* `objectClasses` (schema operation)

* `passwordQualityAdvice=true` (password operations)

* `_prettyPrint=true`

* `relax=true` (rename operation)

The request and response depend on the action. Learn more in [Actions](action-rest.html).

### Query

Use HTTP GET with the `_queryFilter` parameter to list resources at or under a target resource and matching a query filter. Accept a JSON response.

```http
GET /hdap/dc=com/dc=example/ou=People?_queryFilter=... HTTP/1.1
Host: example.com
Accept: application/json
```

HDAP returns the result as a JSON object including a `results` array. Other response fields depend on the parameters.

Supported [parameters](#query-parameters):

* `_countOnly=true`

* `_fields`

* `_pagedResultsCookie`

* `_pageSize`

* `_prettyPrint=true`

* `_queryFilter`

* `scope`

* `_sortKeys`

* `subentries=true`

* `_totalPagedResultsPolicy`

Learn more in [Query](query-rest.html).

## Headers

In addition to the headers described for HDAP [Operations](#operations), HDAP APIs support these Common REST headers.

### Accept-API-Version

The `Accept-API-Version` header specifies protocol and resource versions:

```
Accept-API-Version: protocol=version,resource=version
```

* `protocol`

  The version reflects changes in the Common REST protocol, such as common method parameters and headers specified by the protocol itself, or the input or response conventions it prescribes.

  For example, protocol version 2.2 introduced the `_countOnly` parameter.

* `resource`

  The version reflects changes in the resource implementation, including JSON representation of resources, input parameters required, and incompatible behavior changes.

  For example, the version changes when `errorMessage` changes to `message` in a JSON response.

The `Content-API-Version` response header specifies the protocol and resource versions for the operation. The default HDAP settings are equivalent to:

```
Accept-API-Version: protocol=2.1,resource=1.0
```

### X-ForgeRock-TransactionId

The optional `X-ForgeRock-TransactionId` header helps to track related requests through the Ping Identity Platform.

```
X-ForgeRock-TransactionId: transactionID
```

The transactionID consists of a unique identifier for the transaction optionally followed by a sequence number for the individual request.

You configure platform products to trust transaction IDs and let them propagate for audit purposes. For DS, learn more in [Log LDAP access to files](../logging-guide/ldap-access.html) or [Log HTTP access to files](../logging-guide/http-access.html).

## Query parameters

HDAP supports the following query string parameters.

|   |                                                                                       |
| - | ------------------------------------------------------------------------------------- |
|   | Some parameter values are not safe for URLs.URL-encode parameter values as necessary. |

* `_action=<action>`

  Perform an extended action as part of an HTTP POST.

  The \<action> is one of:

  * `accountUsability`

  * `create`

  * `modifyPassword`

  * `rename`

  * `resetPassword`

  * `schema`

* `_countOnly=true`

  Return a count of query results without returning the resources.

  This parameter requires protocol version 2.2 or later in the `Accept-API-Version` request header:

  ```
  Accept-API-Version: protocol=2.2,resource=1.0
  ```

* `deleteOldRdn=true`

  Delete the old RDN value when renaming a resource.

* `dryRun=true`

  Discover how a server reacts to an operation without performing the operation.

  This parameter relies on the LDAP no-op control, OID `1.3.6.1.4.1.4203.1.10.2`.

* `_fields=<field>[,<field>…​]`

  Return only the specified fields in the body of the response.

  The \<field> values are JSON pointers. In `{"parent":{"child":"value"}}`, `parent/child` refers to `"child": "value"`.

  When the request omits the `_field` parameter, HDAP returns fields for all LDAP user attributes.

  HDAP returns fields for operational attributes only when specifically requested. Use `+`, which encodes to `%2B`, to return fields for all operational attributes.

* `manageDsaIT=true`

  Manage [referrals](../config-guide/referrals.html).

  This parameter relies on the LDAP manage DSAIT request control, OID `2.16.840.1.113730.3.4.2`.

* `objectClasses=<objectClass>[,<objectClass>…​]`

  Return JSON schema for a resource to create based on the LDAP object classes and the parent resource.

* `_pagedResultsCookie=<cookie>`

  The \<cookie> is an opaque string HDAP uses when paging to keep track of the position in the query results:

  1. Set the `_pageSize` in the request to a non-zero number.

     HDAP returns the cookie with the first request.

  2. Supply the cookie in later requests until HDAP returns a `null` cookie when it reaches the final page.

* `_pageSize=<number>`

  Return query results in pages of this size.

  After the initial request, use `_pagedResultsCookie` or `_pageResultsOffset` to page through the results.

* `passwordQualityAdvice=true`

  Get additional information for a failed password update.

  The `passwordQualityAdvice` parameter relies on the DS LDAP password quality advice control, OID `1.3.6.1.4.1.36733.2.1.5.5`.

* `_prettyPrint=true`

  Format the body of the response.

* `_queryFilter=filter-expression`

  Query resources matching the [filter expression](#filter-expressions).

  You must URL-escape the filter-expression.

* `relax=true`

  Relax data and service rules temporarily for the requested update.

  This parameter relies on the LDAP relax rules control, OID `1.3.6.1.4.1.4203.666.5.12`.

* `scope=<scope>`

  Scope of the query; one of:

  * `base`: Query only the target resource.

  * `one` (default): Query direct child resources of the target resource.

  * `sub`: Query the target resource and all child resources recursively.

  * `subordinates`: Query all child resources recursively but do not include the target resource.

* `_sortKeys=(|-)[.var]##<field>##[,(|-)<field>…​]`

  Sort the query results based on the specified field(s).

  * Use `+` for ascending order (default, encoded as `%2B`).

  * Use `-` for descending order.

* `subentries=true`

  Return resources corresponding to LDAP subentries. Subentries aren't returned by default.

  This parameter relies on the LDAP subentries request control, OID `1.3.6.1.4.1.4203.1.10.1`.

* `subtreeDelete=true`

  Delete an entire subtree of resources.

  This parameter relies on the LDAP subtree delete control, OID `1.2.840.113556.1.4.805`.

* `_totalPagedResultsPolicy=<policy>`

  When a `_pageSize` is non-zero, HDAP can calculate `totalPagedResults`. It returns the `totalPagedResults` in the response depending on the \<policy>:

  * `"totalPagedResults": -1` by default, when `_pageSize` is not set, or when `_totalPagedResultsPolicy=NONE`.

  * An estimated count when `_totalPagedResultsPolicy=ESTIMATE`.

  * The exact count when `_totalPagedResultsPolicy=EXACT`, if possible.

### Filter expressions

Query filters request entries matching the filter expression. You must URL-escape the filter expression.

The string representation of the filter expression is:

```none
Expr           = OrExpr
OrExpr         = AndExpr ( 'or' AndExpr ) *
AndExpr        = NotExpr ( 'and' NotExpr ) *
NotExpr        = '!' PrimaryExpr | PrimaryExpr
PrimaryExpr    = '(' Expr ')' | ComparisonExpr | PresenceExpr | LiteralExpr
ComparisonExpr = Pointer OpName JsonValue
PresenceExpr   = Pointer 'pr'
LiteralExpr    = 'true' | 'false'
Pointer        = JSON pointer
OpName         = 'eq' |  # equal to
                 'co' |  # contains
                 'sw' |  # starts with
                 'lt' |  # less than
                 'le' |  # less than or equal to
                 'gt' |  # greater than
                 'ge' |  # greater than or equal to
                 STRING  # extended operator
JsonValue      = NUMBER | BOOLEAN | '"' UTF8STRING '"'
STRING         = ASCII string not containing white-space
UTF8STRING     = UTF-8 string possibly containing white-space
```

JsonValue components of filter expressions follow [RFC 7159: The JavaScript Object Notation (JSON) Data Interchange Format](https://www.rfc-editor.org/rfc/rfc7159.html). In particular, as described in section 7 of the RFC, the escape character in strings is the backslash character. For example, to match the identifier `test\`, use `_id eq 'test\\'`. In the JSON resource, the `\` is escaped the same way: `"_id":"test\\"`.

When using a query filter in a URL, the filter expression is part of a query string parameter and requires URL encoding. Learn more in [RFC 3986: Uniform Resource Identifier (URI): Generic Syntax](https://www.rfc-editor.org/rfc/rfc3986.html). For example, spaces, double quotes, parentheses, and exclamation characters need URL encoding. The following rules apply to URL query components:

```none
query       = *( pchar / "/" / "?" )
pchar       = unreserved / pct-encoded / sub-delims / ":" / "@"
unreserved  = ALPHA / DIGIT / "-" / "." / "_" / "~"
pct-encoded = "%" HEXDIG HEXDIG
sub-delims  = "!" / "$" / "&" / "'" / "(" / ")"
                  / "*" / "+" / "," / ";" / "="
```

`ALPHA`, `DIGIT`, and `HEXDIG` are core rules of [RFC 5234: Augmented BNF for Syntax Specifications](https://www.rfc-editor.org/rfc/rfc5234.html):

```none
ALPHA       =  %x41-5A / %x61-7A   ; A-Z / a-z
DIGIT       =  %x30-39             ; 0-9
HEXDIG      =  DIGIT / "A" / "B" / "C" / "D" / "E" / "F"
```

A backslash escape character in a JsonValue component is percent-encoded in the URL query string parameter as `%5C`. To encode the query filter expression `uid eq 'test\\'`, use `uid+eq'test%5C%5C'+`, for example.

A simple filter expression can represent a comparison, presence, or a literal value.

For comparison expressions use json-pointer comparator json-value, where the comparator is one of the following:

`eq` (equals)\
`co` (contains)\
`sw` (starts with)\
`lt` (less than)\
`le` (less than or equal to)\
`gt` (greater than)\
`ge` (greater than or equal to)

For presence, use json-pointer pr to match resources where:

* The JSON pointer is present.

* The value it points to is not `null`.

Literal values include `true` (match anything) and `false` (match nothing).

Complex expressions employ `and`, `or`, and `!` (not), with parentheses, `(expression)`, to group expressions.

## HTTP status codes

When working with HDAP APIs, client applications should expect at least these HTTP status codes:

* 200 OK

  The request succeeded and HDAP returned a resource, depending on the request.

* 201 Created

  The request succeeded and the HDAP created the resource.

* 204 No Content

  The action request succeeded and there was no content to return.

* 304 Not Modified

  The read request included an `If-None-Match` header and the value of the header matched the revision value of the resource.

* 400 Bad Request

  The request was malformed.

* 401 Unauthorized

  The request requires user authentication.

* 403 Forbidden

  Access was forbidden during an operation on a resource.

* 404 Not Found

  The specified resource could not be found, perhaps because it does not exist.

* 405 Method Not Allowed

  The HTTP method is not allowed for the requested resource.

* 406 Not Acceptable

  The request contains unacceptable parameters, such as an unsupported resource or protocol version.

* 409 Conflict

  The request would have resulted in a conflict with the current state of the resource.

* 410 Gone

  The requested resource is no longer available and will not become available again. This can happen when resources expire, for example.

* 412 Precondition Failed

  The resource's current version does not match the version provided.

* 413 Content Too Large

  The search results exceeded the size limit.

* 415 Unsupported Media Type

  The request is in a format not supported by the requested resource for the requested method.

* 428 Precondition Required

  The resource requires a version and no version was supplied in the request.

* 500 Internal Server Error

  HDAP encountered an unexpected condition preventing it from fulfilling the request.

* 501 Not Implemented

  The resource does not support the functionality required to fulfill the request.

* 503 Service Unavailable

  The requested resource was temporarily unavailable.

---

---
title: Patch
description: Update specific fields of a PingDS directory resource over HTTP using HDAP patch operations.
component: pingds
version: 8.1
page_id: pingds:rest-guide:patch-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/patch-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  add_a_member_to_a_group: Add a member to a group
  remove_a_member_from_a_group: Remove a member from a group
  add_multiple_values: Add multiple values
  patch_a_specific_revision: Patch a specific revision
---

# Patch

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

The [patch operation](rest-operations.html#patch) updates one or more fields of a resource. Use it when you must make fine-grained changes to a resource; for example:

* Add a member to a static group.

* Remove a member from a static group.

* Add or remove a single mail address or telephone number.

If you intend only to *replace* fields' values, update the resource instead with HTTP PUT and a partial resource including just the fields to replace.

## Add a member to a group

The following example adds Babs to a static group:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request PATCH \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --data '[{
  "operation": "add",
  "field": "uniqueMember",
  "value": "dc=com/dc=example/ou=People/uid=bjensen"
  }]' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=Groups/cn=Directory%20Administrators?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=Groups/cn=Directory%20Administrators",
>   "objectClass" : [ "groupofuniquenames", "top" ],
>   "cn" : [ "Directory Administrators" ],
>   "ou" : [ "Groups" ],
>   "uniqueMember" : [ "dc=com/dc=example/ou=People/uid=kvaughan", "dc=com/dc=example/ou=People/uid=rdaugherty", "dc=com/dc=example/ou=People/uid=hmiller", "dc=com/dc=example/ou=People/uid=bjensen" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=Groups/cn=Directory%20Administrators',
        method: 'PATCH',
        body: [{
            "operation": "add",
            "field": "uniqueMember",
            "value": "dc=com/dc=example/ou=People/uid=bjensen"
        }]
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: add group member', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [patch-group-add.js](../_attachments/hdap/js/patch-group-add.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

patch = [{
    'operation': 'add',
    'field': 'uniqueMember',
    'value': 'dc=com/dc=example/ou=People/uid=bjensen'
}]
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.patch(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=Groups/cn=Directory%20Administrators',
    headers=headers,
    json=patch,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [patch-group-add.py](../_attachments/hdap/py/patch-group-add.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
patch = [{
    "operation" => "add",
    "field" => "uniqueMember",
    "value" => "dc=com/dc=example/ou=People/uid=bjensen"
}]
response = hdap.patch do |h|
    h.path = 'dc=com/dc=example/ou=Groups/cn=Directory%20Administrators'
    h.body = JSON.generate(patch)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [patch-group-add.rb](../_attachments/hdap/rb/patch-group-add.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Remove a member from a group

The following example removes Babs from the group:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request PATCH \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --data '[{
  "operation": "remove",
  "field": "uniqueMember",
  "value": "dc=com/dc=example/ou=People/uid=bjensen"
  }]' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=Groups/cn=Directory%20Administrators?_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=Groups/cn=Directory%20Administrators",
>   "objectClass" : [ "groupofuniquenames", "top" ],
>   "cn" : [ "Directory Administrators" ],
>   "ou" : [ "Groups" ],
>   "uniqueMember" : [ "dc=com/dc=example/ou=People/uid=kvaughan", "dc=com/dc=example/ou=People/uid=rdaugherty", "dc=com/dc=example/ou=People/uid=hmiller" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=Groups/cn=Directory%20Administrators',
        method: 'PATCH',
        body: [{
            "operation": "remove",
            "field": "uniqueMember",
            "value": "dc=com/dc=example/ou=People/uid=bjensen"
        }]
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: remove group member', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [patch-group-remove.js](../_attachments/hdap/js/patch-group-remove.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

patch = [{
    'operation': 'remove',
    'field': 'uniqueMember',
    'value': 'dc=com/dc=example/ou=People/uid=bjensen'
}]
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.patch(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=Groups/cn=Directory%20Administrators',
    headers=headers,
    json=patch,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [patch-group-remove.py](../_attachments/hdap/py/patch-group-remove.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
patch = [{
    "operation" => "remove",
    "field" => "uniqueMember",
    "value" => "dc=com/dc=example/ou=People/uid=bjensen"
}]
response = hdap.patch do |h|
    h.path = 'dc=com/dc=example/ou=Groups/cn=Directory%20Administrators'
    h.body = JSON.generate(patch)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [patch-group-remove.rb](../_attachments/hdap/rb/patch-group-remove.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Add multiple values

To change multiple fields, include multiple operation objects in the patch payload:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request PATCH \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --data '[{
  "operation": "add",
  "field": "telephoneNumber",
  "value": "+1 408 555 9999"
 }, {
  "operation": "add",
  "field": "mail",
  "value": "barbara.jensen@example.com"
 }]' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=mail,telephoneNumber&_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
>   "telephoneNumber" : [ "+1 408 555 1862", "+1 408 555 9999" ],
>   "mail" : [ "bjensen@example.com", "barbara.jensen@example.com" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=mail,telephoneNumber',
        method: 'PATCH',
        body: [{
            "operation": "add",
            "field": "telephoneNumber",
            "value": "+1 408 555 9999"
        }, {
            "operation": "add",
            "field": "mail",
            "value": "barbara.jensen@example.com"
        }]
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: patch multiple fields', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [patch-multiple.js](../_attachments/hdap/js/patch-multiple.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

patch = [{
    'operation': 'add',
    'field': 'telephoneNumber',
    'value': '+1 408 555 9999'
}, {
    'operation': 'add',
    'field': 'mail',
    'value': 'barbara.jensen@example.com'
}]
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_fields': 'mail,telephoneNumber' }
response = requests.patch(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    json=patch,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [patch-multiple.py](../_attachments/hdap/py/patch-multiple.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
fields = { '_fields': 'mail,telephoneNumber' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
patch = [{
    "operation" => "add",
    "field" => "telephoneNumber",
    "value" => "+1 408 555 9999"
}, {
    "operation" => "add",
    "field" => "mail",
    "value" => "barbara.jensen@example.com"
}]
response = hdap.patch do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=bjensen'
    h.body = JSON.generate(patch)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [patch-multiple.rb](../_attachments/hdap/rb/patch-multiple.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

For a multivalued attribute, the `value` field takes an array. whereas the `value` field takes a single value for a single-valued field. For single-valued fields, an `add` operation has the same effect as a `replace` operation.

## Patch a specific revision

Use an `If-Match: <revision>` header to patch only a specific revision of a resource:

* Curl

* JavaScript

* Python

* Ruby

```console
$ export JWT=$(echo $(curl \
 --request POST \
 --cacert ca-cert.pem \
 --header 'Content-Type: application/json' \
 --data '{ "password": "bribery" }' \
 --silent \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_action=authenticate') | jq -r .access_token)
$ export REVISION=$(cut -d \" -f 8 <(curl \
 --get \
 --cacert ca-cert.pem \
 --header "Authorization: Bearer $JWT" \
 --header 'Content-Type: application/json' \
 --data '_fields=_rev' \
 --silent \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen'))
$ curl \
 --request PATCH \
 --cacert ca-cert.pem \
 --header "Authorization: Bearer $JWT" \
 --header 'Content-Type: application/json' \
 --header "If-Match: $REVISION" \
 --data '[{
  "operation": "remove",
  "field": "telephoneNumber",
  "value": "+1 408 555 9999"
 }, {
  "operation": "remove",
  "field": "mail",
  "value": "barbara.jensen@example.com"
 }]' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=mail,telephoneNumber&_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
>   "telephoneNumber" : [ "+1 408 555 1862" ],
>   "mail" : [ "bjensen@example.com" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen',
        body: [{
            "operation": "add",
            "field": "telephoneNumber",
            "value": "+1 408 555 9999"
        }, {
            "operation": "add",
            "field": "mail",
            "value": "barbara.jensen@example.com"
        }]
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    let response = await doRequest('HDAP: read bjensen _rev', options)
    console.log(response)
    options.headers['If-Match'] = JSON.parse(response.data)._rev
    options.method = 'PATCH'
    response = await doRequest('HDAP: patch specific revision', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [patch-rev.js](../_attachments/hdap/js/patch-rev.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
rev = requests.get(f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    verify=utils.ca_pem).json()['_rev']

headers['If-Match'] = rev
patch = [{
    'operation': 'add',
    'field': 'telephoneNumber',
    'value': '+1 408 555 9999'
}, {
    'operation': 'add',
    'field': 'mail',
    'value': 'barbara.jensen@example.com'
}]
params = { '_fields': 'mail,telephoneNumber' }
response = requests.patch(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    json=patch,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [patch-rev.py](../_attachments/hdap/py/patch-rev.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
fields = { '_fields': 'mail,telephoneNumber' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
patch = [{
    "operation" => "add",
    "field" => "telephoneNumber",
    "value" => "+1 408 555 9999"
}, {
    "operation" => "add",
    "field" => "mail",
    "value" => "barbara.jensen@example.com"
}]
resource = 'dc=com/dc=example/ou=People/uid=bjensen'
rev = JSON.parse(hdap.get(resource).body, symbolize_names: true)[:_rev]

response = hdap.patch do |h|
    h.path = resource
    h.body = JSON.generate(patch)
    h.headers['If-Match'] = rev
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [patch-rev.rb](../_attachments/hdap/rb/patch-rev.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

The resource revision changes when the patch is successful.

---

---
title: Query
description: Search PingDS directory resources over HTTP using HDAP query filters, paged results, sorting, and graph queries.
component: pingds
version: 8.1
page_id: pingds:rest-guide:query-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/query-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  example_query_filters: Example query filters
  build_query_filters: Build query filters
  query-rest-graph: Graph-like queries
  query-rest-complex: Queries and JSON attributes
  query-rest-count: Count child resources
  query-rest-paged-results: Paged results
  query-rest-sort: Server-side sort
---

# Query

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

To search, use HTTP GET with at least a `_queryFilter=<filter-expression>` parameter and other applicable parameters as necessary, such as `scope`. For reference details, refer to:

* [Query](rest-operations.html#query)

* [Query parameters](rest-operations.html#query-parameters)

* [Filter expressions](rest-operations.html#filter-expressions)

## Example query filters

The following table shows LDAP search filters and corresponding `_queryFilter` expressions:

| LDAP search filter(1)         | HDAP `_queryFilter`(1)              |
| ----------------------------- | ----------------------------------- |
| `(&)`                         | `true`                              |
| `(uid=*)`                     | `uid pr`                            |
| `(uid=bjensen)`               | `uid eq 'bjensen'`                  |
| `(uid=*jensen*)`              | `uid co 'jensen'`                   |
| `(uid=jensen*)`               | `uid sw 'jensen'`                   |
| `(&(uid=*jensen*)(cn=babs*))` | `uid co 'jensen' and cn sw 'babs')` |
| `(\|(uid=*jensen*)(cn=sam*))` | `(uid co 'jensen' or cn sw 'sam')`  |
| `(!(uid=*jensen*))`           | `!(uid co 'jensen')`                |
| `(uid<=jensen)`               | `uid le 'jensen'`                   |
| `(uid>=jensen)`               | `uid ge 'jensen'`                   |

(1) Quote LDAP search filters and encode HDAP `_queryFilter` parameters as necessary in your applications.

For details on which index to configure for a specific filter, refer to [Necessary indexes](../config-guide/idx-what.html#necessary-indexes).

## Build query filters

For query operations, the \<filter-expression> has the following building blocks. You must URL-encode the filter expressions. This page shows them without URL-encoding to make them easier to read.

In filter expressions, the simplest \<json-pointer> is a JSON field name. A \<json-pointer> can also reference nested elements. For details, read RFC 6901, [JavaScript Object Notation (JSON) Pointer](https://www.rfc-editor.org/rfc/rfc6901.html).

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The `co` (contains) and `sw` (starts with) query filter expressions match part of a value.HDAP does not support `co` and `sw` to match values for:- Binary fields, such as photos or digital certificates (binary attributes in LDAP)

- `_id` and JSON fields whose values are the `_id`s of other resources, such as `manager` (DN attributes in LDAP)

- Time fields, such as a last login time (generalized time attributes in LDAP) |

* Comparison expressions

  Build filters using the following comparison expressions:

  * `<json-pointer> eq <json-value>`

    Matches when the pointer equals the value.

    > **Collapse: Show example**
    >
    > * Curl
    >
    > * JavaScript
    >
    > * Python
    >
    > * Ruby
    >
    > ```console
    > $ curl \
    >  --get \
    >  --cacert ca-cert.pem \
    >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    >  --data "_queryFilter=mail+eq+'bjensen@example.com'" \
    >  --data '_fields=cn' \
    >  --data '_prettyPrint=true' \
    >  --data 'scope=sub' \
    >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
    > ```
    >
    > Output
    >
    > ```
    > {
    >   "result" : [ {
    >     "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Barbara Jensen", "Babs Jensen" ]
    >   } ],
    >   "resultCount" : 1,
    >   "pagedResultsCookie" : null,
    >   "totalPagedResultsPolicy" : "NONE",
    >   "totalPagedResults" : -1,
    >   "remainingPagedResults" : -1
    > }
    > ```
    >
    > ```javascript
    > (async () => {
    >     const { authenticate, doRequest, getOptions } = require('./utils')
    >     const options = getOptions({
    >         path: "/hdap/dc=com/dc=example/ou=People?_queryFilter=mail+eq+'bjensen@example.com'&_fields=cn&scope=sub"
    >     })
    >     const jwt = await authenticate(options)
    >     options.headers['Authorization'] = 'Bearer ' + jwt
    >     const response = await doRequest('HDAP: query eq', options)
    >     console.log(response)
    > })().catch(error => { console.error(error) })
    > ```
    >
    > Source files for this sample: [query-eq.js](../_attachments/hdap/js/query-eq.js), [utils.js](../_attachments/hdap/js/utils.js)
    >
    > ```python
    > #!/usr/bin/env python3
    >
    > import requests
    > import utils
    >
    > params = {
    >     '_fields': 'cn',
    >     '_queryFilter': 'mail eq "bjensen@example.com"',
    >     'scope': 'sub'
    > }
    > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
    > response = requests.get(
    >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    >     headers=headers,
    >     params=params,
    >     verify=utils.ca_pem)
    > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
    > ```
    >
    > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-eq.py](../_attachments/hdap/py/query-eq.py)
    >
    > ```ruby
    > require_relative 'utils.rb'
    > require 'faraday'
    >
    > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > options = { ca_file: utils.ca_pem }
    > jwt = utils.authenticate
    > query = {
    >     "_fields": "cn",
    >     "_queryFilter": "mail eq 'bjensen@example.com'",
    >     "scope": "sub"
    > }
    > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    >     f.headers['Content-Type'] = 'application/json'
    >     f.request :authorization, 'Bearer', jwt
    > end
    > response = hdap.get('dc=com/dc=example/ou=People')
    >
    > puts "Status code: #{response.status}\nJSON: #{response.body}"
    > ```
    >
    > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-eq.rb](../_attachments/hdap/rb/query-eq.rb)
    >
    > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

  * `<json-pointer> co <json-value>`

    Matches when the pointer contains the value.

    > **Collapse: Show example**
    >
    > * Curl
    >
    > * JavaScript
    >
    > * Python
    >
    > * Ruby
    >
    > ```console
    > $ curl \
    >  --get \
    >  --cacert ca-cert.pem \
    >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    >  --data "_queryFilter=mail+co+'jensen'" \
    >  --data '_fields=cn' \
    >  --data '_prettyPrint=true' \
    >  --data 'scope=sub' \
    >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
    > ```
    >
    > Output
    >
    > ```
    > {
    >   "result" : [ {
    >     "_id" : "dc=com/dc=example/ou=People/uid=ajensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Allison Jensen" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Barbara Jensen", "Babs Jensen" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=gjensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Gern Jensen" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=jjensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Jody Jensen" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=kjensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Kurt Jensen" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=rjensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Richard Jensen" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=tjensen",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Ted Jensen" ]
    >   } ],
    >   "resultCount" : 7,
    >   "pagedResultsCookie" : null,
    >   "totalPagedResultsPolicy" : "NONE",
    >   "totalPagedResults" : -1,
    >   "remainingPagedResults" : -1
    > }
    > ```
    >
    > ```javascript
    > (async () => {
    >     const { authenticate, doRequest, getOptions } = require('./utils')
    >     const options = getOptions({
    >         path: "/hdap/dc=com/dc=example/ou=People?_queryFilter=mail+co+'jensen'&_fields=cn&scope=sub"
    >     })
    >     const jwt = await authenticate(options)
    >     options.headers['Authorization'] = 'Bearer ' + jwt
    >     const response = await doRequest('HDAP: query co', options)
    >     console.log(response)
    > })().catch(error => { console.error(error) })
    > ```
    >
    > Source files for this sample: [query-co.js](../_attachments/hdap/js/query-co.js), [utils.js](../_attachments/hdap/js/utils.js)
    >
    > ```python
    > #!/usr/bin/env python3
    >
    > import requests
    > import utils
    >
    > params = {
    >     '_fields': 'cn',
    >     '_queryFilter': 'mail co "jensen"',
    >     'scope': 'sub'
    > }
    > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
    > response = requests.get(
    >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    >     headers=headers,
    >     params=params,
    >     verify=utils.ca_pem)
    > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
    > ```
    >
    > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-co.py](../_attachments/hdap/py/query-co.py)
    >
    > ```ruby
    > require_relative 'utils.rb'
    > require 'faraday'
    >
    > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > options = { ca_file: utils.ca_pem }
    > jwt = utils.authenticate
    > query = {
    >     "_fields": "cn",
    >     "_queryFilter": "mail co 'jensen'",
    >     "scope": "sub"
    > }
    > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    >     f.headers['Content-Type'] = 'application/json'
    >     f.request :authorization, 'Bearer', jwt
    > end
    > response = hdap.get('dc=com/dc=example/ou=People')
    >
    > puts "Status code: #{response.status}\nJSON: #{response.body}"
    > ```
    >
    > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-co.rb](../_attachments/hdap/rb/query-co.rb)
    >
    > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

  * `<json-pointer> sw <json-value>`

    Matches when the pointer starts with the value.

    > **Collapse: Show example**
    >
    > * Curl
    >
    > * JavaScript
    >
    > * Python
    >
    > * Ruby
    >
    > ```console
    > $ curl \
    >  --get \
    >  --cacert ca-cert.pem \
    >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    >  --data "_queryFilter=mail+sw+'ab'" \
    >  --data '_fields=cn' \
    >  --data '_prettyPrint=true' \
    >  --data 'scope=sub' \
    >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
    > ```
    >
    > Output
    >
    > ```
    > {
    >   "result" : [ {
    >     "_id" : "dc=com/dc=example/ou=People/uid=abarnes",
    >      "_rev" : "<revision>",
    >     "cn" : [ "Anne-Louise Barnes" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=abergin",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Andy Bergin" ]
    >   } ],
    >   "resultCount" : 2,
    >   "pagedResultsCookie" : null,
    >   "totalPagedResultsPolicy" : "NONE",
    >   "totalPagedResults" : -1,
    >   "remainingPagedResults" : -1
    > }
    > ```
    >
    > ```javascript
    > (async () => {
    >     const { authenticate, doRequest, getOptions } = require('./utils')
    >     const options = getOptions({
    >         path: "/hdap/dc=com/dc=example/ou=People?_queryFilter=mail+sw+'ab'&_fields=cn&scope=sub"
    >     })
    >     const jwt = await authenticate(options)
    >     options.headers['Authorization'] = 'Bearer ' + jwt
    >     const response = await doRequest('HDAP: query sw', options)
    >     console.log(response)
    > })().catch(error => { console.error(error) })
    > ```
    >
    > Source files for this sample: [query-sw.js](../_attachments/hdap/js/query-sw.js), [utils.js](../_attachments/hdap/js/utils.js)
    >
    > ```python
    > #!/usr/bin/env python3
    >
    > import requests
    > import utils
    >
    > params = {
    >     '_fields': 'cn',
    >     '_queryFilter': 'mail sw "ab"',
    >     'scope': 'sub'
    > }
    > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
    > response = requests.get(
    >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    >     headers=headers,
    >     params=params,
    >     verify=utils.ca_pem)
    > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
    > ```
    >
    > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-sw.py](../_attachments/hdap/py/query-sw.py)
    >
    > ```ruby
    > require_relative 'utils.rb'
    > require 'faraday'
    >
    > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > options = { ca_file: utils.ca_pem }
    > jwt = utils.authenticate
    > query = {
    >     "_fields": "cn",
    >     "_queryFilter": "mail sw 'ab'",
    >     "scope": "sub"
    > }
    > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    >     f.headers['Content-Type'] = 'application/json'
    >     f.request :authorization, 'Bearer', jwt
    > end
    > response = hdap.get('dc=com/dc=example/ou=People')
    >
    > puts "Status code: #{response.status}\nJSON: #{response.body}"
    > ```
    >
    > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-eq.rb](../_attachments/hdap/rb/query-sw.rb)
    >
    > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

  * `<json-pointer> lt <json-value>`

    Matches when the pointer is less than the value.

    > **Collapse: Show example**
    >
    > * Curl
    >
    > * JavaScript
    >
    > * Python
    >
    > * Ruby
    >
    > ```console
    > $ curl \
    >  --get \
    >  --cacert ca-cert.pem \
    >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    >  --data "_queryFilter=mail+lt+'ac'" \
    >  --data '_fields=cn' \
    >  --data '_prettyPrint=true' \
    >  --data 'scope=sub' \
    >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
    > ```
    >
    > Output
    >
    > ```
    > {
    >   "result" : [ {
    >     "_id" : "dc=com/dc=example/ou=People/uid=abarnes",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Anne-Louise Barnes" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=abergin",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Andy Bergin" ]
    >   } ],
    >   "resultCount" : 2,
    >   "pagedResultsCookie" : null,
    >   "totalPagedResultsPolicy" : "NONE",
    >   "totalPagedResults" : -1,
    >   "remainingPagedResults" : -1
    > }
    > ```
    >
    > ```javascript
    > (async () => {
    >     const { authenticate, doRequest, getOptions } = require('./utils')
    >     const options = getOptions({
    >         path: "/hdap/dc=com/dc=example/ou=People?_queryFilter=mail+lt+'ac'&_fields=cn&scope=sub"
    >     })
    >     const jwt = await authenticate(options)
    >     options.headers['Authorization'] = 'Bearer ' + jwt
    >     const response = await doRequest('HDAP: query lt', options)
    >     console.log(response)
    > })().catch(error => { console.error(error) })
    > ```
    >
    > Source files for this sample: [query-lt.js](../_attachments/hdap/js/query-lt.js), [utils.js](../_attachments/hdap/js/utils.js)
    >
    > ```python
    > #!/usr/bin/env python3
    >
    > import requests
    > import utils
    >
    > params = {
    >     '_fields': 'cn',
    >     '_queryFilter': 'mail lt "ac"',
    >     'scope': 'sub'
    > }
    > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
    > response = requests.get(
    >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    >     headers=headers,
    >     params=params,
    >     verify=utils.ca_pem)
    > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
    > ```
    >
    > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-lt.py](../_attachments/hdap/py/query-lt.py)
    >
    > ```ruby
    > require_relative 'utils.rb'
    > require 'faraday'
    >
    > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > options = { ca_file: utils.ca_pem }
    > jwt = utils.authenticate
    > query = {
    >     "_fields": "cn",
    >     "_queryFilter": "mail lt 'ac'",
    >     "scope": "sub"
    > }
    > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    >     f.headers['Content-Type'] = 'application/json'
    >     f.request :authorization, 'Bearer', jwt
    > end
    > response = hdap.get('dc=com/dc=example/ou=People')
    >
    > puts "Status code: #{response.status}\nJSON: #{response.body}"
    > ```
    >
    > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-lt.rb](../_attachments/hdap/rb/query-lt.rb)
    >
    > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

  * `<json-pointer> le <json-value>`

    Matches when the pointer is less than or equal to the value.

    > **Collapse: Show example**
    >
    > * Curl
    >
    > * JavaScript
    >
    > * Python
    >
    > * Ruby
    >
    > ```console
    > $ curl \
    >  --get \
    >  --cacert ca-cert.pem \
    >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    >  --data "_queryFilter=mail+le+'ad'" \
    >  --data '_fields=cn' \
    >  --data '_prettyPrint=true' \
    >  --data 'scope=sub' \
    >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
    > ```
    >
    > Output
    >
    > ```
    > {
    >   "result" : [ {
    >     "_id" : "dc=com/dc=example/ou=People/uid=abarnes",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Anne-Louise Barnes" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=abergin",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Andy Bergin" ]
    >   }, {
    >     "_id" : "dc=com/dc=example/ou=People/uid=achassin",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Ashley Chassin" ]
    >   } ],
    >   "resultCount" : 3,
    >   "pagedResultsCookie" : null,
    >   "totalPagedResultsPolicy" : "NONE",
    >   "totalPagedResults" : -1,
    >   "remainingPagedResults" : -1
    > }
    > ```
    >
    > ```javascript
    > (async () => {
    >     const { authenticate, doRequest, getOptions } = require('./utils')
    >     const options = getOptions({
    >         path: "/hdap/dc=com/dc=example/ou=People?_queryFilter=mail+le+'ad'&_fields=cn&scope=sub"
    >     })
    >     const jwt = await authenticate(options)
    >     options.headers['Authorization'] = 'Bearer ' + jwt
    >     const response = await doRequest('HDAP: query le', options)
    >     console.log(response)
    > })().catch(error => { console.error(error) })
    > ```
    >
    > Source files for this sample: [query-le.js](../_attachments/hdap/js/query-le.js), [utils.js](../_attachments/hdap/js/utils.js)
    >
    > ```python
    > #!/usr/bin/env python3
    >
    > import requests
    > import utils
    >
    > params = {
    >     '_fields': 'cn',
    >     '_queryFilter': 'mail le "ad"',
    >     'scope': 'sub'
    > }
    > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
    > response = requests.get(
    >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    >     headers=headers,
    >     params=params,
    >     verify=utils.ca_pem)
    > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
    > ```
    >
    > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-le.py](../_attachments/hdap/py/query-le.py)
    >
    > ```ruby
    > require_relative 'utils.rb'
    > require 'faraday'
    >
    > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > options = { ca_file: utils.ca_pem }
    > jwt = utils.authenticate
    > query = {
    >     "_fields": "cn",
    >     "_queryFilter": "mail le 'ad'",
    >     "scope": "sub"
    > }
    > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    >     f.headers['Content-Type'] = 'application/json'
    >     f.request :authorization, 'Bearer', jwt
    > end
    > response = hdap.get('dc=com/dc=example/ou=People')
    >
    > puts "Status code: #{response.status}\nJSON: #{response.body}"
    > ```
    >
    > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-le.rb](../_attachments/hdap/rb/query-le.rb)
    >
    > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

  * `<json-pointer> gt <json-value>`

    Matches when the pointer is greater than the value.

    > **Collapse: Show example**
    >
    > * Curl
    >
    > * JavaScript
    >
    > * Python
    >
    > * Ruby
    >
    > ```console
    > $ curl \
    >  --get \
    >  --cacert ca-cert.pem \
    >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    >  --data "_queryFilter=mail+gt+'wa'" \
    >  --data '_fields=cn' \
    >  --data '_prettyPrint=true' \
    >  --data 'scope=sub' \
    >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
    > ```
    >
    > Output
    >
    > ```
    > {
    >   "result" : [ {
    >     "_id" : "dc=com/dc=example/ou=People/uid=wlutz",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Wendy Lutz" ]
    >   } ],
    >   "resultCount" : 1,
    >   "pagedResultsCookie" : null,
    >   "totalPagedResultsPolicy" : "NONE",
    >   "totalPagedResults" : -1,
    >   "remainingPagedResults" : -1
    > }
    > ```
    >
    > ```javascript
    > (async () => {
    >     const { authenticate, doRequest, getOptions } = require('./utils')
    >     const options = getOptions({
    >         path: "/hdap/dc=com/dc=example/ou=People?_queryFilter=mail+gt+'wa'&_fields=cn&scope=sub"
    >     })
    >     const jwt = await authenticate(options)
    >     options.headers['Authorization'] = 'Bearer ' + jwt
    >     const response = await doRequest('HDAP: query gt', options)
    >     console.log(response)
    > })().catch(error => { console.error(error) })
    > ```
    >
    > Source files for this sample: [query-gt.js](../_attachments/hdap/js/query-gt.js), [utils.js](../_attachments/hdap/js/utils.js)
    >
    > ```python
    > #!/usr/bin/env python3
    >
    > import requests
    > import utils
    >
    > params = {
    >     '_fields': 'cn',
    >     '_queryFilter': 'mail gt "wa"',
    >     'scope': 'sub'
    > }
    > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
    > response = requests.get(
    >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    >     headers=headers,
    >     params=params,
    >     verify=utils.ca_pem)
    > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
    > ```
    >
    > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-gt.py](../_attachments/hdap/py/query-gt.py)
    >
    > ```ruby
    > require_relative 'utils.rb'
    > require 'faraday'
    >
    > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > options = { ca_file: utils.ca_pem }
    > jwt = utils.authenticate
    > query = {
    >     "_fields": "cn",
    >     "_queryFilter": "mail gt 'wa'",
    >     "scope": "sub"
    > }
    > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    >     f.headers['Content-Type'] = 'application/json'
    >     f.request :authorization, 'Bearer', jwt
    > end
    > response = hdap.get('dc=com/dc=example/ou=People')
    >
    > puts "Status code: #{response.status}\nJSON: #{response.body}"
    > ```
    >
    > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-gt.rb](../_attachments/hdap/rb/query-gt.rb)
    >
    > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

  * `<json-pointer> ge <json-value>`

    Matches when the pointer is greater than or equal to the value.

    > **Collapse: Show example**
    >
    > * Curl
    >
    > * JavaScript
    >
    > * Python
    >
    > * Ruby
    >
    > ```console
    > $ curl \
    >  --get \
    >  --cacert ca-cert.pem \
    >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
    >  --data "_queryFilter=mail+ge+'va'" \
    >  --data '_fields=cn' \
    >  --data '_prettyPrint=true' \
    >  --data 'scope=sub' \
    >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
    > ```
    >
    > Output
    >
    > ```
    > {
    >   "result" : [ {
    >     "_id" : "dc=com/dc=example/ou=People/uid=wlutz",
    >     "_rev" : "<revision>",
    >     "cn" : [ "Wendy Lutz" ]
    >   } ],
    >   "resultCount" : 1,
    >   "pagedResultsCookie" : null,
    >   "totalPagedResultsPolicy" : "NONE",
    >   "totalPagedResults" : -1,
    >   "remainingPagedResults" : -1
    > }
    > ```
    >
    > ```javascript
    > (async () => {
    >     const { authenticate, doRequest, getOptions } = require('./utils')
    >     const options = getOptions({
    >         path: "/hdap/dc=com/dc=example/ou=People?_queryFilter=mail+ge+'va'&_fields=cn&scope=sub"
    >     })
    >     const jwt = await authenticate(options)
    >     options.headers['Authorization'] = 'Bearer ' + jwt
    >     const response = await doRequest('HDAP: query ge', options)
    >     console.log(response)
    > })().catch(error => { console.error(error) })
    > ```
    >
    > Source files for this sample: [query-ge.js](../_attachments/hdap/js/query-ge.js), [utils.js](../_attachments/hdap/js/utils.js)
    >
    > ```python
    > #!/usr/bin/env python3
    >
    > import requests
    > import utils
    >
    > params = {
    >     '_fields': 'cn',
    >     '_queryFilter': 'mail ge "va"',
    >     'scope': 'sub'
    > }
    > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
    > response = requests.get(
    >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    >     headers=headers,
    >     params=params,
    >     verify=utils.ca_pem)
    > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
    > ```
    >
    > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-ge.py](../_attachments/hdap/py/query-ge.py)
    >
    > ```ruby
    > require_relative 'utils.rb'
    > require 'faraday'
    >
    > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
    > options = { ca_file: utils.ca_pem }
    > jwt = utils.authenticate
    > query = {
    >     "_fields": "cn",
    >     "_queryFilter": "mail ge 'va'",
    >     "scope": "sub"
    > }
    > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    >     f.headers['Content-Type'] = 'application/json'
    >     f.request :authorization, 'Bearer', jwt
    > end
    > response = hdap.get('dc=com/dc=example/ou=People')
    >
    > puts "Status code: #{response.status}\nJSON: #{response.body}"
    > ```
    >
    > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-ge.rb](../_attachments/hdap/rb/query-ge.rb)
    >
    > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

* Presence expression

  `<json-pointer> pr` matches a resource where the pointer is present.

  > **Collapse: Show example**
  >
  > * Curl
  >
  > * JavaScript
  >
  > * Python
  >
  > * Ruby
  >
  > ```console
  > $ curl \
  >  --get \
  >  --cacert ca-cert.pem \
  >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
  >  --data "_queryFilter=cn+pr" \
  >  --data '_fields=cn' \
  >  --data '_prettyPrint=true' \
  >  --data 'scope=sub' \
  >  'https://localhost:8443/hdap/dc=com/dc=example/ou=Groups'
  > ```
  >
  > Output
  >
  > ```
  > {
  >   "result" : [ {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=Accounting%20Managers",
  >     "_rev" : "<revision>",
  >     "cn" : [ "Accounting Managers" ]
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=Groups/cn=Directory%20Administrators",
  >     "_rev" : "<revision>",
  >     "cn" : [ "Directory Administrators" ]
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=HR%20Managers",
  >     "_rev" : "<revision>",
  >     "cn" : [ "HR Managers" ]
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=PD%20Managers",
  >     "_rev" : "<revision>",
  >     "cn" : [ "PD Managers" ]
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=QA%20Managers",
  >     "_rev" : "<revision>",
  >     "cn" : [ "QA Managers" ]
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=Groups/ou=Self%20Service/cn=Carpoolers",
  >     "_rev" : "<revision>",
  >     "cn" : [ "Carpoolers" ]
  >   } ],
  >   "resultCount" : 6,
  >   "pagedResultsCookie" : null,
  >   "totalPagedResultsPolicy" : "NONE",
  >   "totalPagedResults" : -1,
  >   "remainingPagedResults" : -1
  > }
  > ```
  >
  > ```javascript
  > (async () => {
  >     const { authenticate, doRequest, getOptions } = require('./utils')
  >     const options = getOptions({
  >         path: '/hdap/dc=com/dc=example/ou=Groups?_queryFilter=cn+pr&_fields=cn&scope=sub'
  >     })
  >     const jwt = await authenticate(options)
  >     options.headers['Authorization'] = 'Bearer ' + jwt
  >     const response = await doRequest('HDAP: query pr', options)
  >     console.log(response)
  > })().catch(error => { console.error(error) })
  > ```
  >
  > Source files for this sample: [query-pr.js](../_attachments/hdap/js/query-pr.js), [utils.js](../_attachments/hdap/js/utils.js)
  >
  > ```python
  > #!/usr/bin/env python3
  >
  > import requests
  > import utils
  >
  > params = {
  >     '_fields': 'cn',
  >     '_queryFilter': 'cn pr',
  >     'scope': 'sub'
  > }
  > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
  > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
  > response = requests.get(
  >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=Groups',
  >     headers=headers,
  >     params=params,
  >     verify=utils.ca_pem)
  > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
  > ```
  >
  > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-pr.py](../_attachments/hdap/py/query-pr.py)
  >
  > ```ruby
  > require_relative 'utils.rb'
  > require 'faraday'
  >
  > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
  > options = { ca_file: utils.ca_pem }
  > jwt = utils.authenticate
  > query = {
  >     "_fields": "cn",
  >     "_queryFilter": "cn pr",
  >     "scope": "sub"
  > }
  > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
  >     f.headers['Content-Type'] = 'application/json'
  >     f.request :authorization, 'Bearer', jwt
  > end
  > response = hdap.get('dc=com/dc=example/ou=Groups')
  >
  > puts "Status code: #{response.status}\nJSON: #{response.body}"
  > ```
  >
  > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-pr.rb](../_attachments/hdap/rb/query-pr.rb)
  >
  > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

* Literal expressions

  `true` matches any resource in scope.

  `false` matches no resources.

  > **Collapse: Show example**
  >
  > * Curl
  >
  > * JavaScript
  >
  > * Python
  >
  > * Ruby
  >
  > ```console
  > $ curl \
  >  --get \
  >  --cacert ca-cert.pem \
  >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
  >  --data "_queryFilter=true" \
  >  --data '_fields=_id' \
  >  --data '_prettyPrint=true' \
  >  'https://localhost:8443/hdap/dc=com/dc=example/ou=Groups'
  > ```
  >
  > Output
  >
  > ```
  > {
  >   "result" : [ {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=Accounting%20Managers",
  >     "_rev" : "<revision>"
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=Groups/cn=Directory%20Administrators",
  >     "_rev" : "<revision>"
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=HR%20Managers",
  >     "_rev" : "<revision>"
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=PD%20Managers",
  >     "_rev" : "<revision>"
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=groups/cn=QA%20Managers",
  >     "_rev" : "<revision>"
  >   }, {
  >     "_id" : "dc=com/dc=example/ou=Groups/ou=Self%20Service",
  >     "_rev" : "<revision>"
  >   } ],
  >   "resultCount" : 6,
  >   "pagedResultsCookie" : null,
  >   "totalPagedResultsPolicy" : "NONE",
  >   "totalPagedResults" : -1,
  >   "remainingPagedResults" : -1
  > }
  > ```
  >
  > ```javascript
  > (async () => {
  >     const { authenticate, doRequest, getOptions } = require('./utils')
  >     const options = getOptions({
  >         path: '/hdap/dc=com/dc=example/ou=Groups?_queryFilter=true&_fields=cn&scope=sub'
  >     })
  >     const jwt = await authenticate(options)
  >     options.headers['Authorization'] = 'Bearer ' + jwt
  >     const response = await doRequest('HDAP: query true', options)
  >     console.log(response)
  > })().catch(error => { console.error(error) })
  > ```
  >
  > Source files for this sample: [query-true.js](../_attachments/hdap/js/query-true.js), [utils.js](../_attachments/hdap/js/utils.js)
  >
  > ```python
  > #!/usr/bin/env python3
  >
  > import requests
  > import utils
  >
  > params = {
  >     '_fields': 'cn',
  >     '_queryFilter': True,
  >     'scope': 'sub'
  > }
  > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
  > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
  > response = requests.get(
  >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=Groups',
  >     headers=headers,
  >     params=params,
  >     verify=utils.ca_pem)
  > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
  > ```
  >
  > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-true.py](../_attachments/hdap/py/query-true.py)
  >
  > ```ruby
  > require_relative 'utils.rb'
  > require 'faraday'
  >
  > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
  > options = { ca_file: utils.ca_pem }
  > jwt = utils.authenticate
  > query = {
  >     "_fields": "cn",
  >     "_queryFilter": true,
  >     "scope": "sub"
  > }
  > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
  >     f.headers['Content-Type'] = 'application/json'
  >     f.request :authorization, 'Bearer', jwt
  > end
  > response = hdap.get('dc=com/dc=example/ou=Groups')
  >
  > puts "Status code: #{response.status}\nJSON: #{response.body}"
  > ```
  >
  > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-true.rb](../_attachments/hdap/rb/query-true.rb)
  >
  > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

* Complex expressions

  Combine expressions using boolean operators `and`, `or`, and `!` (not), and by using parentheses `(<filter-expression>)` with group expressions.

  > **Collapse: Show example**
  >
  > * Curl
  >
  > * JavaScript
  >
  > * Python
  >
  > * Ruby
  >
  > ```console
  > $ curl \
  >  --get \
  >  --cacert ca-cert.pem \
  >  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
  >  --data "_queryFilter=mail+co+'jensen'+and+givenName+sw+'Al'" \
  >  --data '_fields=cn' \
  >  --data '_prettyPrint=true' \
  >  --data 'scope=sub' \
  >  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
  > ```
  >
  > Output
  >
  > ```
  > {
  >   "result" : [ {
  >     "_id" : "dc=com/dc=example/ou=People/uid=ajensen",
  >     "_rev" : "<revision>",
  >     "cn" : [ "Allison Jensen" ]
  >   } ],
  >   "resultCount" : 1,
  >   "pagedResultsCookie" : null,
  >   "totalPagedResultsPolicy" : "NONE",
  >   "totalPagedResults" : -1,
  >   "remainingPagedResults" : -1
  > }
  > ```
  >
  > ```javascript
  > (async () => {
  >     const { authenticate, doRequest, getOptions } = require('./utils')
  >     const filter = encodeURIComponent("mail co 'jensen' and givenName sw 'Al'")
  >     const options = getOptions({
  >         path: `/hdap/dc=com/dc=example/ou=People?_queryFilter=${filter}&_fields=cn&scope=sub`
  >     })
  >     const jwt = await authenticate(options)
  >     options.headers['Authorization'] = 'Bearer ' + jwt
  >     const response = await doRequest('HDAP: complex query', options)
  >     console.log(response)
  > })().catch(error => { console.error(error) })
  > ```
  >
  > Source files for this sample: [query-complex.js](../_attachments/hdap/js/query-complex.js), [utils.js](../_attachments/hdap/js/utils.js)
  >
  > ```python
  > #!/usr/bin/env python3
  >
  > import requests
  > import utils
  >
  > params = {
  >     '_fields': 'cn',
  >     '_queryFilter': 'mail co "jensen" and givenName sw "Al"',
  >     'scope': 'sub'
  > }
  > jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
  > headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
  > response = requests.get(
  >     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
  >     headers=headers,
  >     params=params,
  >     verify=utils.ca_pem)
  > print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
  > ```
  >
  > Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-complex.py](../_attachments/hdap/py/query-complex.py)
  >
  > ```ruby
  > require_relative 'utils.rb'
  > require 'faraday'
  >
  > utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
  > options = { ca_file: utils.ca_pem }
  > jwt = utils.authenticate
  > query = {
  >     "_fields": "cn",
  >     "_queryFilter": "mail co 'jensen' and givenName sw 'Al'",
  >     "scope": "sub"
  > }
  > hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
  >     f.headers['Content-Type'] = 'application/json'
  >     f.request :authorization, 'Bearer', jwt
  > end
  > response = hdap.get('dc=com/dc=example/ou=People')
  >
  > puts "Status code: #{response.status}\nJSON: #{response.body}"
  > ```
  >
  > Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-complex.rb](../_attachments/hdap/rb/query-complex.rb)
  >
  > HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Graph-like queries

[Collective attributes](../config-guide/collective-attrs.html) provide a mechanism to inherit LDAP attributes from other entries. HDAP relies on this mechanism for graph-like queries.

The `ds-evaluation` setup profile uses collective attributes to inherit LDAP attribute values for street address from location and quota settings from class of service.

> **Collapse: Show example**
>
> * Curl
>
> * JavaScript
>
> * Python
>
> * Ruby
>
> ```console
> $ curl \
>  --get \
>  --cacert ca-cert.pem \
>  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
>  --data "_queryFilter=(mail+co+'jensen'+and+l+eq+'San+Francisco'+and+classOfService+eq+'bronze')" \
>  --data '_fields=diskQuota,mailQuota,street' \
>  --data '_prettyPrint=true' \
>  --data 'scope=sub' \
>  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
> ```
>
> Output
>
> ```
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
>     "_rev" : "<revision>",
>     "street" : [ "201 Mission Street Suite 2900" ],
>     "mailQuota" : [ "1 GB" ],
>     "diskQuota" : [ "10 GB" ]
>   } ],
>   "resultCount" : 1,
>   "pagedResultsCookie" : null,
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```
>
> ```javascript
> (async () => {
>     const { authenticate, doRequest, getOptions } = require('./utils')
>     const filter = "mail+co+'jensen'+and+l+eq+'San+Francisco'+and+classOfService+eq+'bronze'"
>     const options = getOptions({
>         path: `/hdap/dc=com/dc=example/ou=People?_queryFilter=${filter}&_fields=diskQuota,mailQuota,street&scope=sub`
>     })
>     const jwt = await authenticate(options)
>     options.headers['Authorization'] = 'Bearer ' + jwt
>     const response = await doRequest('HDAP: graph query', options)
>     console.log(response)
> })().catch(error => { console.error(error) })
> ```
>
> Source files for this sample: [query-graph.js](../_attachments/hdap/js/query-graph.js), [utils.js](../_attachments/hdap/js/utils.js)
>
> ```python
> #!/usr/bin/env python3
>
> import requests
> import utils
>
> params = {
>     '_fields': 'diskQuota,mailQuota,street',
>     '_queryFilter': 'mail co "jensen" and l eq "San Francisco" and classOfService eq "bronze"',
>     'scope': 'sub'
> }
> jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
> headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
> response = requests.get(
>     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
>     headers=headers,
>     params=params,
>     verify=utils.ca_pem)
> print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
> ```
>
> Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-graph.py](../_attachments/hdap/py/query-graph.py)
>
> ```ruby
> require_relative 'utils.rb'
> require 'faraday'
>
> utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
> options = { ca_file: utils.ca_pem }
> jwt = utils.authenticate
> query = {
>     "_fields": "diskQuota,mailQuota,street",
>     "_queryFilter": "mail co 'jensen' and l eq 'San Francisco' and classOfService eq 'bronze'",
>     "scope": "sub"
> }
> hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
>     f.headers['Content-Type'] = 'application/json'
>     f.request :authorization, 'Bearer', jwt
> end
> response = hdap.get('dc=com/dc=example/ou=People')
>
> puts "Status code: #{response.status}\nJSON: #{response.body}"
> ```
>
> Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-graph.rb](../_attachments/hdap/rb/query-graph.rb)
>
> HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

Configure collective attributes as necessary for your graph-like queries.

## Queries and JSON attributes

The default JSON query index works for JSON attributes that hold arbitrary JSON objects. This includes JSON with nested objects, such as `{"array":[{"x":1,"y":2},{"x":3,"y":4}]}`. As a result, HDAP filter expressions can target JSON fields in indexed JSON attribute objects.

HDAP query filter expressions support the [grouping operators](https://www.rfc-editor.org/rfc/rfc7644.html#section-3.4.2.2) described in RFC 7644, section *3.4.2.2. Filtering*, Table 5: *Grouping Operators*. In other words, HDAP query filter expressions can use *complex attribute filter grouping*, with brackets (`[]`) to group expressions in the filter.

Complex attribute filter grouping lets filter expressions target array objects. This search finds an entry with a `json` attribute containing an `array` of objects:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --get \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --data-urlencode "_queryFilter=(json/array[x eq 1] and json/array[y eq 4])" \
 --data '_fields=json' \
 --data '_prettyPrint=true' \
 --data 'scope=sub' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
```

> **Collapse: Show output**
>
> ```
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/ou=People/uid=abarnes",
>     "_rev" : "<revision>",
>     "json" : [ {
>       "array" : [ {
>         "x" : 1,
>         "y" : 2
>       }, {
>         "x" : 3,
>         "y" : 4
>       } ]
>     } ]
>   } ],
>   "resultCount" : 1,
>   "pagedResultsCookie" : null,
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const filter = encodeURIComponent('(json/array[x eq 1] and json/array[y eq 4])')
    const options = getOptions({
        path: `/hdap/dc=com/dc=example/ou=People?_queryFilter=${filter}&_fields=json&scope=sub`
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: JSON query', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [query-json.js](../_attachments/hdap/js/query-json.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

params = {
    '_fields': 'json',
    '_queryFilter': '(json/array[x eq 1] and json/array[y eq 4])',
    'scope': 'sub'
}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    headers=headers,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-json.py](../_attachments/hdap/py/query-json.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = {
    "_fields": "json",
    "_queryFilter": "(json/array[x eq 1] and json/array[y eq 4])",
    "scope": "sub"
}
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example/ou=People')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-json.rb](../_attachments/hdap/rb/query-json.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

* The filter `json/array[x eq 1] and json/array[y eq 4]` matches because it matches both objects in the array.

* The filter `json/array[x eq 1 and y eq 2]` matches because it matches the first object of the array.

* The filter `json/array[x eq 1 and y eq 4]` fails to match, because the array has no object `{"x":1,"y":4}`.

## Count child resources

Use the `_countOnly=true` query string parameter to get the number of child resources directly beneath a resource. You must also set `_queryFilter=true` and leave `scope=one` (default):

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --get \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --cacert ca-cert.pem \
 --header 'Accept-API-Version: protocol=2.2,resource=1.0' \
 --data '_countOnly=true' \
 --data '_queryFilter=true' \
 --data '_prettyPrint=true' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
```

> **Collapse: Show output**
>
> ```
> {
>   "result" : [ ],
>   "resultCount" : 100153,
>   "pagedResultsCookie" : null,
>   "totalPagedResultsPolicy" : "ESTIMATE",
>   "totalPagedResults" : 100153,
>   "remainingPagedResults" : -1
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People?_queryFilter=true&_countOnly=true',
    })
    const jwt = await authenticate(options)
    options.headers['Accept-API-Version'] = 'protocol=2.2,resource=1.0'
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: query for count', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [query-count.js](../_attachments/hdap/js/query-count.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

params = {
    '_countOnly': True,
    '_queryFilter': True
}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {jwt}',
    'Accept-API-Version': 'protocol=2.2,resource=1.0'
}
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    headers=headers,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-count.py](../_attachments/hdap/py/query-count.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = {
    "_countOnly": true,
    "_queryFilter": true
}
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.headers['Accept-API-Version'] = 'protocol=2.2,resource=1.0'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example/ou=People')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-count.rb](../_attachments/hdap/rb/query-count.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

Notice the search returns an empty `result` array. This feature relies on the [`numSubordinates` virtual attribute](../config-guide/virtual-attrs.html#default-virtual-attributes).

## Paged results

Get results one page at a time with these [query string parameters](rest-operations.html#query-parameters):

* `_pageSize=<number>`

* `_pagedResultsCookie=<cookie>`

> **Collapse: Show request for first page of five results**
>
> * Curl
>
> * JavaScript
>
> * Python
>
> * Ruby
>
> ```console
> $ curl \
>  --get \
>  --cacert ca-cert.pem \
>  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
>  --data "_queryFilter=objectClass+eq+'posixAccount'" \
>  --data '_pageSize=5' \
>  --data '_fields=_id' \
>  --data '_prettyPrint=true' \
>  --data 'scope=sub' \
>  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
> ```
>
> Output
>
> ```
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/ou=People/uid=abarnes",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=abergin",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=achassin",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=ahall",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=ahel",
>     "_rev" : "<revision>"
>   } ],
>   "resultCount" : 5,
>   "pagedResultsCookie" : "AAAAAAAAABE=",
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```
>
> ```javascript
> (async () => {
>     const { authenticate, doRequest, getOptions } = require('./utils')
>     const filter = "objectClass+eq+'posixAccount'"
>     const options = getOptions({
>         path: `/hdap/dc=com/dc=example/ou=People?_queryFilter=${filter}&_pageSize=5&_fields=_id&scope=sub`
>     })
>     const jwt = await authenticate(options)
>     options.headers['Authorization'] = 'Bearer ' + jwt
>     const response = await doRequest('HDAP: query first five paged results', options)
>     console.log(response)
> })().catch(error => { console.error(error) })
> ```
>
> Source files for this sample: [query-paged-first-five.js](../_attachments/hdap/js/query-paged-first-five.js), [utils.js](../_attachments/hdap/js/utils.js)
>
> ```python
> #!/usr/bin/env python3
>
> import requests
> import utils
>
> params = {
>     '_fields': '_id',
>     '_queryFilter': 'objectClass eq "posixAccount"',
>     '_pageSize': 5,
>     'scope': 'sub'
> }
> jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
> headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
> response = requests.get(
>     f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
>     headers=headers,
>     params=params,
>     verify=utils.ca_pem)
> print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
> ```
>
> Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-paged-first-five.py](../_attachments/hdap/py/query-paged-first-five.py)
>
> ```ruby
> require_relative 'utils.rb'
> require 'faraday'
>
> utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
> options = { ca_file: utils.ca_pem }
> jwt = utils.authenticate
> query = {
>     "_fields": "_id",
>     "_queryFilter": "objectClass eq 'posixAccount'",
>     "_pageSize": 5,
>     "scope": "sub"
> }
> hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
>     f.headers['Content-Type'] = 'application/json'
>     f.request :authorization, 'Bearer', jwt
> end
> response = hdap.get('dc=com/dc=example/ou=People')
>
> puts "Status code: #{response.status}\nJSON: #{response.body}"
> ```
>
> Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-paged-first-five.rb](../_attachments/hdap/rb/query-paged-first-five.rb)
>
> HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

> **Collapse: Show request for next page of five results**
>
> * Curl
>
> * JavaScript
>
> * Python
>
> * Ruby
>
> ```console
> $ export COOKIE=$(cut -d \" -f 4 <(grep pagedResultsCookie \
>  <(curl \
>  --get \
>  --cacert ca-cert.pem \
>  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
>  --data "_queryFilter=objectClass+eq+'posixAccount'" \
>  --data '_pageSize=5' \
>  --data '_fields=_id' \
>  --data '_prettyPrint=true' \
>  --data 'scope=sub' \
>  'https://localhost:8443/hdap/dc=com/dc=example/ou=People')))
> $ curl \
>  --get \
>  --cacert ca-cert.pem \
>  --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
>  --data "_queryFilter=objectClass+eq+'posixAccount'" \
>  --data '_pageSize=5' \
>  --data "_pagedResultsCookie=$COOKIE" \
>  --data '_fields=_id' \
>  --data '_prettyPrint=true' \
>  --data 'scope=sub' \
>  'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
> ```
>
> Output
>
> ```
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/ou=People/uid=ahunter",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=ajensen",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=aknutson",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=alangdon",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=alutz",
>     "_rev" : "<revision>"
>   } ],
>   "resultCount" : 5,
>   "pagedResultsCookie" : "AAAAAAAAABE=",
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```
>
> ```javascript
> (async () => {
>     const { authenticate, doRequest, getOptions } = require('./utils')
>     const filter = "objectClass+eq+'posixAccount'"
>     const options = getOptions({
>         path: `/hdap/dc=com/dc=example/ou=People?_queryFilter=${filter}&_pageSize=5&_fields=_id&scope=sub`
>     })
>     const jwt = await authenticate(options)
>     options.headers['Authorization'] = 'Bearer ' + jwt
>     let response = await doRequest('HDAP: query first five paged results', options)
>     console.log(response)
>     const cookie = JSON.parse(response.data).pagedResultsCookie
>     options.path += `&_pagedResultsCookie=${cookie}`
>     response = await doRequest('HDAP: query next five paged results', options)
>     console.log(response)
> })().catch(error => { console.error(error) })
> ```
>
> Source files for this sample: [query-paged-next-five.js](../_attachments/hdap/js/query-paged-next-five.js), [utils.js](../_attachments/hdap/js/utils.js)
>
> ```python
> #!/usr/bin/env python3
>
> import requests
> import utils
>
> resource = f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People'
> params = {
>     '_fields': '_id',
>     '_queryFilter': 'objectClass eq "posixAccount"',
>     '_pageSize': 5,
>     'scope': 'sub'
> }
> jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
> headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
> response = requests.get(
>     resource,
>     headers=headers,
>     params=params,
>     verify=utils.ca_pem)
>
> cookie = response.json()['pagedResultsCookie']
> params['_pagedResultsCookie'] = cookie
>
> response = requests.get(
>     resource,
>     headers=headers,
>     params=params,
>     verify=utils.ca_pem)
> print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
> ```
>
> Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-paged-next-five.py](../_attachments/hdap/py/query-paged-next-five.py)
>
> ```ruby
> require_relative 'utils.rb'
> require 'faraday'
>
> utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
> options = { ca_file: utils.ca_pem }
> jwt = utils.authenticate
> query = {
>     "_fields": "_id",
>     "_queryFilter": "objectClass eq 'posixAccount'",
>     "_pageSize": 5,
>     "scope": "sub"
> }
> resource = 'dc=com/dc=example/ou=People'
> hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
>     f.headers['Content-Type'] = 'application/json'
>     f.request :authorization, 'Bearer', jwt
> end
> cookie = JSON.parse(hdap.get(resource).body, symbolize_names: true)[:pagedResultsCookie]
>
> query['_pagedResultsCookie'] = cookie
> hdap.params = query
> response = hdap.get(resource)
>
> puts "Status code: #{response.status}\nJSON: #{response.body}"
> ```
>
> Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-paged-next-five.rb](../_attachments/hdap/rb/query-paged-next-five.rb)
>
> HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

Notice the following features of the responses:

* `"totalPagedResultsPolicy" : "NONE"` means HDAP did not calculate the counts.

* `"remainingPagedResults" : -1` means HDAP did not count the remaining results.

  HDAP never counts `remainingPagedResults` because it would require a potentially costly calculation to determine the current position in the total result set.

* `"totalPagedResults" : -1` means HDAP did not count the total results.

When the query has the following characteristics, the response contains an estimated `totalPagedResults` count:

* The request specifies the policy using the parameter `_totalPagedResultsPolicy=ESTIMATE`.

* The `_pageSize` parameter is an integer greater than zero.

* The LDAP search for the query is indexed.

- Curl

- JavaScript

- Python

- Ruby

```console
$ curl \
 --get \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --data "_queryFilter=mail+co+'jensen'" \
 --data '_pageSize=2' \
 --data '_totalPagedResultsPolicy=ESTIMATE' \
 --data '_fields=_id' \
 --data '_prettyPrint=true' \
 --data 'scope=sub' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
```

> **Collapse: Show output**
>
> ```
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/ou=People/uid=ajensen",
>     "_rev" : "<revision>"
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
>     "_rev" : "<revision>"
>   } ],
>   "resultCount" : 2,
>   "pagedResultsCookie" : "AAAAAAAAAEI=",
>   "totalPagedResultsPolicy" : "ESTIMATE",
>   "totalPagedResults" : 7,
>   "remainingPagedResults" : -1
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const filter = "mail+co+'jensen'"
    const pageParams = '_pageSize=2&_totalPagedResultsPolicy=ESTIMATE'
    const options = getOptions({
        path: `/hdap/dc=com/dc=example/ou=People?_queryFilter=${filter}&${pageParams}&_fields=_id&scope=sub`
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: paged query', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [query-paged.js](../_attachments/hdap/js/query-paged.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

params = {
    '_fields': '_id',
    '_queryFilter': 'mail co "jensen"',
    '_pageSize': 2,
    '_totalPagedResultsPolicy': 'ESTIMATE',
    'scope': 'sub'
}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    headers=headers,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-paged.py](../_attachments/hdap/py/query-paged.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = {
    "_fields": "_id",
    "_queryFilter": "mail co 'jensen'",
    "_pageSize": 2,
    "_totalPagedResultsPolicy": "ESTIMATE",
    "scope": "sub"
}
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example/ou=People')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-paged.rb](../_attachments/hdap/rb/query-paged.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

The estimated number of results can be useful, for example, when the LDAP search uses a big index or a VLV index and the total number of results is large.

## Server-side sort

Use the [`_sortKeys` parameter](rest-operations.html#query-parameters) to have HDAP sort the query results based on one or more fields in the resources.

The following example sorts results in reverse order by given name (`-givenName`):

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --get \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --data "_queryFilter=sn+co+'barnes'" \
 --data '_sortKeys=-givenName' \
 --data '_fields=cn' \
 --data '_prettyPrint=true' \
 --data 'scope=sub' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People'
```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const filter = "sn+co+'barnes'"
    const options = getOptions({
        path: `/hdap/dc=com/dc=example/ou=People?_queryFilter=${filter}&_sortKeys=-givenName&_fields=cn&scope=sub`
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: query with server-side sort', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [query-sss.js](../_attachments/hdap/js/query-sss.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

params = {
    '_fields': 'cn',
    '_queryFilter': 'sn co "barnes"',
    '_sortKeys': '-givenName',
    'scope': 'sub'
}
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People',
    headers=headers,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [query-sss.py](../_attachments/hdap/py/query-sss.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
query = {
    "_fields": "cn",
    "_queryFilter": "sn co 'barnes'",
    "_sortKeys": "-givenName",
    "scope": "sub"
}
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: query, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example/ou=People')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [query-sss.rb](../_attachments/hdap/rb/query-sss.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

> **Collapse: Show results**
>
> ```json
> {
>   "result" : [ {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.94561",
>     "_rev" : "<revision>",
>     "cn" : [ "Atsushi Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.81142",
>     "_rev" : "<revision>",
>     "cn" : [ "Atsuo Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.67723",
>     "_rev" : "<revision>",
>     "cn" : [ "Atmane Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.54304",
>     "_rev" : "<revision>",
>     "cn" : [ "Atlante Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.40885",
>     "_rev" : "<revision>",
>     "cn" : [ "Atlanta Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.27466",
>     "_rev" : "<revision>",
>     "cn" : [ "Atl-Sales Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.14047",
>     "_rev" : "<revision>",
>     "cn" : [ "Atl Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=user.628",
>     "_rev" : "<revision>",
>     "cn" : [ "Atique Barnes" ]
>   }, {
>     "_id" : "dc=com/dc=example/ou=People/uid=abarnes",
>     "_rev" : "<revision>",
>     "cn" : [ "Anne-Louise Barnes" ]
>   } ],
>   "resultCount" : 9,
>   "pagedResultsCookie" : null,
>   "totalPagedResultsPolicy" : "NONE",
>   "totalPagedResults" : -1,
>   "remainingPagedResults" : -1
> }
> ```

* To specify multiple sort keys, use a comma-separated list of fields.

* The sort key fields you specify must exist in the result entries.

  You do not need to include the sort field(s) in the results.

* [VLV for paged server-side sort](../config-guide/idx-config.html#vlv-for-paged-sss) shows an HDAP query using a browsing index.

HDAP stores the entire result set before sorting the results. If you expect a large result set for your search, use [paged results](#query-rest-paged-results) to limit the performance cost and get results quickly.

---

---
title: Read
description: Read PingDS directory resources and request specific fields over HTTP using the HDAP API.
component: pingds
version: 8.1
page_id: pingds:rest-guide:read-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/read-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  read-rest-resource: Read a resource
  read-rest-fields: Read specific fields
---

# Read

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

## Read a resource

Read with HTTP GET:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --get \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --data '_prettyPrint=true' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
>   "_rev" : "<revision>",
>   "objectClass" : [ "person", "cos", "oauth2TokenObject", "inetOrgPerson", "organizationalPerson", "posixAccount", "top" ],
>   "classOfService" : "bronze",
>   "cn" : [ "Barbara Jensen", "Babs Jensen" ],
>   "departmentNumber" : [ "3001" ],
>   "description" : [ "Original description" ],
>   "diskQuota" : [ "10 GB" ],
>   "facsimileTelephoneNumber" : [ "+1 408 555 1992" ],
>   "gidNumber" : 1000,
>   "givenName" : [ "Barbara" ],
>   "homeDirectory" : "/home/bjensen",
>   "l" : [ "San Francisco" ],
>   "mail" : [ "bjensen@example.com" ],
>   "mailQuota" : [ "1 GB" ],
>   "manager" : [ "dc=com/dc=example/ou=People/uid=trigden" ],
>   "oauth2Token" : [ {
>     "access_token" : "123",
>     "expires_in" : 59,
>     "token_type" : "Bearer",
>     "refresh_token" : "456"
>   } ],
>   "ou" : [ "Product Development", "People" ],
>   "preferredLanguage" : "en, ko;q=0.8",
>   "roomNumber" : [ "0209" ],
>   "sn" : [ "Jensen" ],
>   "street" : [ "201 Mission Street Suite 2900" ],
>   "telephoneNumber" : [ "+1 408 555 1862" ],
>   "uid" : [ "bjensen" ],
>   "uidNumber" : 1076,
>   "userPassword" : [ "<hashed-password>" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen'
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: read with GET', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [read.js](../_attachments/hdap/js/read.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [read.py](../_attachments/hdap/py/read.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [read.rb](../_attachments/hdap/rb/read.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Read specific fields

HDAP can return only specified fields in the resource. Use the [`_fields` parameter](rest-operations.html#query-parameters):

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --get \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --data '_fields=cn,mail' \
 --data '_prettyPrint=true' \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=bjensen'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=bjensen",
>   "_rev" : "<revision>",
>   "mail" : [ "bjensen@example.com" ],
>   "cn" : [ "Barbara Jensen", "Babs Jensen" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=bjensen?_fields=cn,mail'
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: read specific fields', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [read-fields.js](../_attachments/hdap/js/read-fields.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

params = { '_fields': 'cn,mail' }
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
response = requests.get(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=bjensen',
    headers=headers,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [read-fields.py](../_attachments/hdap/py/read-fields.py)

```ruby
require_relative 'utils.rb'
require 'faraday'

utils = Utils.new('dc=com/dc=example/ou=People/uid=bjensen', 'hifalutin')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
fields = { '_fields': 'cn,mail' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
response = hdap.get('dc=com/dc=example/ou=People/uid=bjensen')

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [read-fields.rb](../_attachments/hdap/rb/read-fields.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

---

---
title: Update
description: Update and replace fields in PingDS directory resources over HTTP using the HDAP PUT operation.
component: pingds
version: 8.1
page_id: pingds:rest-guide:update-rest
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/update-rest.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
section_ids:
  update_a_resource: Update a resource
  update_a_specific_revision: Update a specific revision
  rename_a_resource: Rename a resource
---

# Update

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Examples in this documentation depend on features activated in [the `ds-evaluation` setup profile](../install-guide/setup-ds.html#about-ds-evaluation).The code samples demonstrate how to contact the server over HTTPS using the deployment CA certificate. Before trying the samples, generate the CA certificate in PEM format from the server deployment ID and password:```console
$ dskeymgr \
 export-ca-cert \
 --deploymentId $DEPLOYMENT_ID \
 --deploymentIdPassword password \
 --outputFile ca-cert.pem
``` |

## Update a resource

Use HTTP PUT to replace any and all writable fields in a resource.

The effect is the same as a [patch replace operation](rest-operations.html#patch-replace).

The following example updates Sam Carter's telephone number regardless of the revision:

* Curl

* JavaScript

* Python

* Ruby

```console
$ curl \
 --request PUT \
 --cacert ca-cert.pem \
 --user dc=com/dc=example/ou=People/uid=kvaughan:bribery \
 --header 'Content-Type: application/json' \
 --data '{"telephoneNumber": "+1 408 555 1212"}' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=scarter?_fields=telephoneNumber&_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=scarter",
>   "telephoneNumber" : [ "+1 408 555 1212" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=scarter?_fields=telephoneNumber',
        method: 'PUT',
        body: { "telephoneNumber": "+1 408 555 1212" }
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    const response = await doRequest('HDAP: update telephone number', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [update.js](../_attachments/hdap/js/update.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

body = { 'telephoneNumber': '+1 408 555 1212' }
jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
params = { '_fields': 'telephoneNumber' }
response = requests.put(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=scarter',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [update.py](../_attachments/hdap/py/update.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
fields = { '_fields': 'telephoneNumber' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
body = { "telephoneNumber" => "+1 408 555 1212" }
response = hdap.put do |h|
    h.path = 'dc=com/dc=example/ou=People/uid=scarter'
    h.body = JSON.generate(body)
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [update.rb](../_attachments/hdap/rb/update.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Update a specific revision

To update a resource only if the resource matches a particular version, use an `If-Match: <revision>` header:

* Curl

* JavaScript

* Python

* Ruby

```console
$ export JWT=$(echo $(curl \
 --request POST \
 --cacert ca-cert.pem \
 --header 'Content-Type: application/json' \
 --data '{ "password": "bribery" }' \
 --silent \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=kvaughan?_action=authenticate') | jq -r .access_token)
$ export REVISION=$(cut -d \" -f 8 <(curl \
 --get \
 --cacert ca-cert.pem \
 --header "Authorization: Bearer $JWT" \
 --header 'Content-Type: application/json' \
 --data '_fields=_rev' \
 --silent \
'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=scarter'))
$ curl \
 --request PUT \
 --cacert ca-cert.pem \
 --header "Authorization: Bearer $JWT" \
 --header 'Content-Type: application/json' \
 --header "If-Match: $REVISION" \
 --data '{"telephoneNumber": "+1 408 555 1213"}' \
 'https://localhost:8443/hdap/dc=com/dc=example/ou=People/uid=scarter?_fields=telephoneNumber&_prettyPrint=true'
```

> **Collapse: Show output**
>
> ```
> {
>   "_id" : "dc=com/dc=example/ou=People/uid=scarter",
>   "telephoneNumber" : [ "+1 408 555 1213" ]
> }
> ```

```javascript
(async () => {
    const { authenticate, doRequest, getOptions } = require('./utils')
    const options = getOptions({
        path: '/hdap/dc=com/dc=example/ou=People/uid=scarter?_fields=telephoneNumber',
        body: { "telephoneNumber": "+1 408 555 1213" }
    })
    const jwt = await authenticate(options)
    options.headers['Authorization'] = 'Bearer ' + jwt
    let response = await doRequest('HDAP: read scarter _rev', options)
    console.log(response)
    options.headers['If-Match'] = JSON.parse(response.data)._rev
    options.method = 'PUT'
    response = await doRequest('HDAP: update specific revision', options)
    console.log(response)
})().catch(error => { console.error(error) })
```

Source files for this sample: [update-rev.js](../_attachments/hdap/js/update-rev.js), [utils.js](../_attachments/hdap/js/utils.js)

```python
#!/usr/bin/env python3

import requests
import utils

jwt = utils.authenticate('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
headers = { 'Content-Type': 'application/json', 'Authorization': f'Bearer {jwt}' }
rev = requests.get(f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=scarter',
    headers=headers,
    verify=utils.ca_pem).json()['_rev']

headers['If-Match'] = rev
body = { 'telephoneNumber': '+1 408 555 1213' }
params = { '_fields': 'telephoneNumber' }
response = requests.put(
    f'https://{utils.host}:{utils.port}/hdap/dc=com/dc=example/ou=People/uid=scarter',
    headers=headers,
    json=body,
    params=params,
    verify=utils.ca_pem)
print('Status code: %d\nJSON: %s' % (response.status_code, response.json()))
```

Source files for this sample: [utils.py](../_attachments/hdap/py/utils.py), [update-rev.py](../_attachments/hdap/py/update-rev.py)

```ruby
require_relative 'utils.rb'
require 'faraday'
require 'json'

utils = Utils.new('dc=com/dc=example/ou=People/uid=kvaughan', 'bribery')
options = { ca_file: utils.ca_pem }
jwt = utils.authenticate
fields = { '_fields': 'telephoneNumber' }
hdap = Faraday.new(url: "https://#{utils.host}:#{utils.port}/hdap/", params: fields, ssl: options) do |f|
    f.headers['Content-Type'] = 'application/json'
    f.request :authorization, 'Bearer', jwt
end
resource = 'dc=com/dc=example/ou=People/uid=scarter'
rev = JSON.parse(hdap.get(resource).body, symbolize_names: true)[:_rev]

body = { "telephoneNumber" => "+1 408 555 1213" }
response = hdap.put do |h|
    h.path = resource
    h.body = JSON.generate(body)
    h.headers['If-Match'] = rev
end

puts "Status code: #{response.status}\nJSON: #{response.body}"
```

Source files for this sample: [utils.rb](../_attachments/hdap/rb/utils.rb), [update-rev.rb](../_attachments/hdap/rb/update-rev.rb)

HDAP Ruby examples require Ruby 3.2 and the `faraday` and `json` gems.

## Rename a resource

Refer to the [rename action](action-rest.html#action-rename).

---

---
title: Use HDAP
description: Overview of the PingDS HDAP APIs for REST-based HTTP access to directory data, with links to each operation.
component: pingds
version: 8.1
page_id: pingds:rest-guide:preface
canonical_url: https://docs.pingidentity.com/pingds/8.1/rest-guide/preface.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2025-10-22T14:42:39Z
keywords: ["REST API"]
page_aliases: ["index.adoc"]
---

# Use HDAP

These pages show you how to use the DS HTTP directory access protocol (HDAP) *(tooltip: \<div class="paragraph">
\<p>The DS feature providing REST APIs and HTTP access to directory data.\</p>
\</div>)* APIs for REST-based HTTP access to directory services. HDAP transforms HTTP operations into LDAP operations and maps JSON resources to LDAP entries.

The interface stability for HDAP is *Evolving*.

[icon: plus, set=fas, size=3x]

#### [Create](create-rest.html)

Create resources over HTTP.

[icon: book, set=fas, size=3x]

#### [Read](read-rest.html)

Read resources over HTTP.

[icon: edit, set=fas, size=3x]

#### [Update](update-rest.html)

Update resources over HTTP.

[icon: times, set=fas, size=3x]

#### [Delete](delete-rest.html)

Delete resources over HTTP.

[icon: search, set=fas, size=3x]

#### [Search](query-rest.html)

Query DS over HTTP.

[icon: user-secret, set=fas, size=3x]

#### [Passwords/Accounts](action-rest.html)

Manage passwords and accounts.