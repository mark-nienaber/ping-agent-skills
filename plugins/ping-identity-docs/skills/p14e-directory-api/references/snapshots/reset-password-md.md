---
title: Resetting a Password
description: This operation resets a user password based on the supplied user ID. You can specify either the oldPassword or confirmationToken value in the request, but not both. You can use confirmationToken only to reset the password of non-administrative users.
component: p14e-directory-api
page_id: p14e-directory-api::reset-password
canonical_url: https://developer.pingidentity.com/p14e-directory-api/reset-password.html
revdate: November 3, 2025
section_ids:
  request-parameters: Request parameters
  request-example: Request example
---

# Resetting a Password

This operation resets a user password based on the supplied user ID. You can specify either the `oldPassword` or `confirmationToken` value in the request, but not both. You can use `confirmationToken` only to reset the password of non-administrative users.

The endpoint to reset a user's password is:

`https://directory-api.pingone.com/api/directory/users/password-reset`

## Request parameters

| Parameter         | Data Type | Description                                                                                                                                                               |
| ----------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                | string    | the ID of the user                                                                                                                                                        |
| newPassword       | string    | The new password to assign to the user.                                                                                                                                   |
| oldPassword       | string    | (Optional) The user's current password. You can specify this value or confirmationToken, but not both.                                                                    |
| confirmationToken | string    | (Optional) The user's confirmation token. This can't be used when you're resetting an administrator's password. You'll find the confirmation token on the user's account. |

## Request example

This example resets the user's password by supplying the old password:

```json
{
 "id" : "4ec0bb1e-37b0-414e-b27e-b17ec8ee9321",
 "newPassword" : "$ecret@123"
 "oldPassword" : "$ecret@456"
}
```

If successful, `HTTP 200 OK` is returned in the response.