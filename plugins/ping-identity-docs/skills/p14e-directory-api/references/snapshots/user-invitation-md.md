---
title: User Invitation
description: To invite a new user to your directory, you can supply an email address to the /useractions/invite endpoint. This returns the activation link that the user will use to complete the registration. The activation link is valid for 24 hours.
component: p14e-directory-api
page_id: p14e-directory-api::user-invitation
canonical_url: https://developer.pingidentity.com/p14e-directory-api/user-invitation.html
revdate: October 30, 2025
section_ids:
  available-attributes: Available attributes
---

# User Invitation

To invite a new user to your directory, you can supply an email address to the `/useractions/invite` endpoint. This returns the activation link that the user will use to complete the registration. The activation link is valid for 24 hours.

If the email invitation is sent to an existing user, this is a resend operation. The new activation link returned invalidates the previous activation link.

Here we invite Joe Border (jborder\@pingdevelopers.com) to our directory instance:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
-d '{ "email" : "jborder@pingdevelopers.com" }' \
-X POST https://directory-api.pingone.com/api/directory/useractions/invite
```

The response is the invite activation URL contained in the email sent to the user:

```json
{
  "value":"https://login.pingone.com/idp/directory/a/1234-aaaa-bbbb-5678/registration/confirm/xxyy-jj88-
abcd-12345678/abcd-9876-aaaa-87654321/"
}
```

Joe will need to click the activation button or link in the email to go to the registration page.

The `email` attribute is required, and this will generate an email invitation using the default PingOne for Enterprise email invitation template. In addition, there are other, optional attributes that you can specify to customize the email invitation for your organization. Here's an example:

```shell
curl -v --user 1234-aaaa-bbbb-5678:eXJzbmVha3kh \
-H "Content-Type: application/json" \
-H "Accept: application/json" \
--data "@custom_email.json" \
-X POST https://directory-api.pingone.com/api/directory/useractions/invite
```

The content of custom\_email.json looks like this:

```json
{
  "email": "jborder@pingdevelopers.com",
  "alternateEmail": "jborder+home@pingdevelopers.com",
  "fromName": "Custom Corp.",
  "bodyText": "Custom email body",
  "titleText": "Welcome to PingOne's customized invitation emails!",
  "supportText": "Need support? Call ...",
  "subject": "Activate your Custom Corp directory membership",
  "activationButtonText": "This is a button!",
  "link": "https://custom.com/register",
  "footerText": "All your footers are belong to us.",
  "footerLogoImage": "https://custom.com/images/customCorpFooter.png",
  "headerImage": "http://custom.com/images/customCorpHeader.png",
  "skipSend": "disabled",
  "redirectLink": "https://mysite.custom.com"
 }
```

## Available attributes

All of these attributes are optional. Any attributes that you don't specify use the default PingOne for Enterprise values.

| Attribute            | Description                                                                                                                                                                                                 |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| alternateEmail       | If specified, the invitation email is sent to this address instead of the primary email address.                                                                                                            |
| fromName             | The name of the email sender.                                                                                                                                                                               |
| bodyText             | The body of the email.                                                                                                                                                                                      |
| titleText            | The title of the email (displayed above the body).                                                                                                                                                          |
| supportText          | Contact information for further support.                                                                                                                                                                    |
| subject              | The email subject.                                                                                                                                                                                          |
| activationButtonText | The label used for the activation button.                                                                                                                                                                   |
| link                 | The URL used for the activation button. This URL is also displayed below the button.                                                                                                                        |
| footerText           | Text displayed in the footer of the email.                                                                                                                                                                  |
| footerLogoImage      | The URL for an image to be displayed in the email footer. Maximum size: 40 pixels wide x 70 pixels high.                                                                                                    |
| headerImage          | The URL for an image to be displayed in the email header. Maximum size: 606 pixels wide x 273 pixels high.                                                                                                  |
| skipSend             | If set to 'enabled', the email invitation isn't sent to the user, though the activation link is still returned in the response. If unspecified or set to any value other than 'enabled', the email is sent. |
| redirectLink         | If specified, the user is redirected to the specified URL when they've completed their invitation process. By default, users are redirected to the PingOne for Enterprise dock.                             |