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
