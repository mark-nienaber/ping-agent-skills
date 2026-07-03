---
title: Resetting a Password by Email
description: This operation sets a confirmation token for the user associated with the specified email address. By default, a confirmation email is sent to that address. The confirmation email contains a link to reset their password. A new confirmation token is set for the user each time this operation is called.
component: p14e-directory-api
page_id: p14e-directory-api::reset-password-by-email
canonical_url: https://developer.pingidentity.com/p14e-directory-api/reset-password-by-email.html
revdate: November 3, 2025
section_ids:
  request-parameters: Request parameters
  request-example: Request example
---

# Resetting a Password by Email

This operation sets a confirmation token for the user associated with the specified email address. By default, a confirmation email is sent to that address. The confirmation email contains a link to reset their password. A new confirmation token is set for the user each time this operation is called.

The endpoint to reset a password by email is:

`https://directory-api.pingone.com/api/directory/users/password-lost`

## Request parameters

| Parameter | Data Type | Description                                                                                                                                                                    |
| --------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| email     | string    | The email address of the user.                                                                                                                                                 |
| link      | string    | (Optional) The URL used to reset user passwords. If specified, this is included in the confirmation email. If not specified, the standard PingOne password reset form is used. |
| skipSend  | string    | (Optional) This can be set to `"enabled"` (do not send an email) or `"disabled"` (send an email).                                                                              |

## Request example

This example sends an email with a link to a password-reset page:

```json
{
   "email" : "jborder@anywhere.com",
   "link" : "https://anywhere.com/passwordReset"
   "skipSend" : "disabled"
}
```

If successful, the link is returned in the response, similar to the following:

```json
HTTP/1.1 200 OK
{
  "link": "https://login.pingone.com/idp/directory/a/61197468-2e9b-11e7-93ae-92361f008429/forgotpassword/confirm/611976e8-2e9b-11e7-93ae-92361f002671/611977f6-2e9b-11e7-93ae-92361f008429/"
}
```
