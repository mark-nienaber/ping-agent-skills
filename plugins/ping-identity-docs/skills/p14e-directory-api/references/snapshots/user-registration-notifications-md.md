---
title: User Registration Notifications
description: You can use the /userregistration/preferences endpoint to customize the notifications sent that are related to user registrations. Conditions where notifications occur include password expirations, forgotten passwords, invitations to register, and account locks.
component: p14e-directory-api
page_id: p14e-directory-api::user-registration-notifications
canonical_url: https://developer.pingidentity.com/p14e-directory-api/user-registration-notifications.html
revdate: November 3, 2025
section_ids:
  preferences: Preferences
  required-fields: Required fields
  additional-fields: Additional fields
---

# User Registration Notifications

## Preferences

You can use the `/userregistration/preferences` endpoint to customize the notifications sent that are related to user registrations. Conditions where notifications occur include password expirations, forgotten passwords, invitations to register, and account locks.

Use the following command to get all of the current notification preferences for an account:

```shell
curl -X GET "https://directory-api.pingone.com/api/directory/userregistration/preferences"`
```

The response will be similar to the following (shown only for invite notification preferences, though preferences for all types will be returned):

```
[
  {
    "notification_name": "invite",
    "preferences": [
      {
        "values": [
         {
           "name": "product",
           "default_value": "PingOne Â®"
         },
         {
           "name": "titleText",
           "default_value": "Welcome to PingOne Â®"
         },
         {
           "name": "headerImage",
            "default_value": "http://someImages.com/email/images/activation.jpg"
         },
         {
           "name": "footerText",
           "default_value": ""
         },
         {
           "name": "activationButtonText",
           "default_value": "Activate PingOne Â®"
         },
         {
           "name": "subject",
           "default_value": "You have been invited to use PingOne Â®"
         },
         {
           "name": "supportText",
           "default_value": ""
         },
         {
           "name": "redirectLink",
           "default_value": "The URL to your PingOne"
         },
         {
           "name": "link",
           "default_value": "https://login.pingone.com/idp/directory/a/${accountId}/
                                registration/confirm/${userId}/${confirmationToken}/"
         },
         {
           "name": "footerLogoImage",
           "default_value": "http://someImages.com/email/images/general/logo.2x.png"
         },
         {
           "name": "bodyText",
           "default_value": " has invited you to PingOne Â®.  You're just a few clicks away from
                              the security and convenience of single sign-on access to applications
                              you need to get your job done.  To get started, click the button below."
         },
         {
           "name": "fromName",
           "default_value": "PingOne"
         }
        ]
      }
    ]
  },
 .
 .
 .
]
```

You can also get the preferences for a single, specified type of notification (shown for forgotten passwords):

```shell
curl -X GET
"https://test-directory-api.pingone.com/api/directory/userregistration/preferences/forgot_password"
```

This returns the preference settings used for forgotten password notifications, similar to the following:

```json
{
  "notification_name": "forgot_password",
  "preferences": [
   {
     "values": [
       {
         "name": "product",
         "default_value": "PingOne Â®"
       },
       {
         "name": "redirectLink",
         "default_value": "The URL to your PingOne"
       },
       {
         "name": "footerLogoImage",
         "default_value": "http://someImages.com/email/images/general/footer-logo.2x.png"
       },
       {
         "name": "fromName",
         "default_value": "PingOne"
       }
     ]
   }
  ]
}
```

You can also set or replace existing or default preference values, or remove preferences (only non-required fields). When notifications are sent, if you haven't assigned a notification preference, the `default_value` setting is used.

A replace operation with a null value is the same as executing a remove operation.

You can set required fields to null (which will then use the default values). However, you can't set a required field to an empty string.

## Required fields

For all email types:

* fromName

* product

* subject

## Additional fields

For all email types:

* bannerText

* titleText

* bodyText

* footerText

* footerLogoImage

For all email types except self\_registered\_welcome:

* activationButtonText

* link

For invite and forgot\_password only:

* redirectLink

For invite only:

* headerImage

* supportText

The following example uses a replace operation:

```shell
curl -X PATCH --header "Content-Type: application/json" -d "{
    \"operations\": [
        {\"op\": \"replace\",
              \"path\": \"/forgot_password/preferences/product\",
              \"value\": \"myProduct\"
         }]
}" "https://test-directory-api.pingone.com/api/directory/userregistration/preferences"
```

The operation returns all notification preferences for the account. In the `forgot_password` notification type, you'll find the changed product name.
