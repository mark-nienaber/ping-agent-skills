---
title: Cookie Connector
description: The Cookie connector lets you set and retrieve session cookies in your PingOne DaVinci flow.
component: connectors
page_id: connectors::cookie_connector
canonical_url: https://docs.pingidentity.com/connectors/cookie_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 16, 2024
section_ids:
  setup: Setup
  resources: Resources
  configuring-the-cookie-connector: Configuring the Cookie connector
  connector-configuration: Connector configuration
  hmac-signing-key: HMAC Signing Key
  using-the-connector-in-a-flow: Using the connector in a flow
  creating-a-session-cookie: Creating a session cookie
  retrieving-a-session-cookie: Retrieving a session cookie
  capabilities: Capabilities
  setCookie: Set Session Cookie
  checkSessionCookie: Check Session Cookie
  setCookieWithoutUser: Set Session Cookie (Non User)
  checkSessionCookieWithoutUser: Check Session Cookie (Non User)
---

# Cookie Connector

The Cookie connector lets you set and retrieve session cookies in your PingOne DaVinci flow.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Configuring the Cookie connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### HMAC Signing Key

The Base64-encoded, 256-bit key that the connector uses to sign the session cookies. This prevents unauthorized agents from gaining access by guessing a session ID.

To use this, enable the **Sign Cookies with HMAC Key** option in the **Set a Session Cookie** capabilities.

## Using the connector in a flow

### Creating a session cookie

The connector has two capabilities that allow you to set session cookies:

* **Set a Session Cookie**

* **Set a Session Cookie (Non-User)**

These two capabilities are identical, except the **Non-User** variant doesn't require a user to already have been identified in the flow.

No special configuration is needed. Add the capability and populate its properties according to the help text.

You can include custom claims in the session cookie. In the **Session Cookie Custom Claims** section, click **[icon: plus, set=fa]Field**, select a claim from the list, and enter a value. To delete a custom claim from the list, click **Edit**.

### Retrieving a session cookie

The connector has two capabilities that allow you to read existing session cookies:

* **Check a Session Cookie**

* **Check a Session Cookie (Non-User)**

No special configuration is needed. Add the capability and populate its properties according to the help text.

## Capabilities

### Set Session Cookie

Sets an opaque session cookie so that the user is not asked to authenticate again during the flow.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - - cookieName textField
>   - useSecureCookie toggleSwitch
>   - useHttpOnlyCookie toggleSwitch
>   - cookieExpiresInSeconds textField
>   - cookieDomain textField
>   - Cookie Path textField
>
>   The path where the cookie will be accessible
>
> - * cookieSameSite dropDown
>   * signCookie toggleSwitch
>   * setCookieClientSide toggleSwitch
>   * claimsNameValuePairsSessionCookie selectNameValueListColumn
>   * useSessionTokenFlag toggleSwitch
>   * sessionToken textField
>
> * default object
>
>   * userInfo object required
>
>     User with which the cookie is to be associated.
>
>   * ip string minLength: 1 maxLength: 50
>
>     Ip address of the user in current session.
>
>   * userAgent string minLength: 1 maxLength: 250
>
>     Information about browser, OS, etc. of user in current session.
>
>   * skOpenId object
>
>     Object containing client id of user.
>
>   * origin string minLength: 0 maxLength: 500
>
>     Origin
>
>   * originCookies string minLength: 0 maxLength: 20000
>
>     OriginCookies

### Check Session Cookie

Determine if a session cookie exists in the flow. If it exists, continue with the flow, or ask the user to provide additional authentication information.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - cookieName textField
>   - enforceClientIP toggleSwitch
>   - enforceFlowIdMatch toggleSwitch
>   - Resolve to User toggleSwitch
>
>   Attempt to resolve cookie to a user, which will then be available in {{global.userInfo}} parameter
>
> * default object
>
>   * userAgent string minLength: 1 maxLength: 250
>
>     Information about browser, OS, etc. of user in current session.
>
>   * ip string minLength: 1 maxLength: 50
>
>     Ip address of the user in current session.
>
>   * cookies object
>
>     List of cookies associated with the user.
>
>   * skOpenId object
>
>     Object containing client id of user.
>
>   * origin string minLength: 0 maxLength: 500
>
>     Origin
>
>   * originCookies string minLength: 0 maxLength: 20000
>
>     OriginCookies
>
> - output object
>
>   * claims object
>
>     * userId string
>
>     * connectionId string
>
>     * companyId string
>
>     * ip string
>
>     * userAgent number
>
>     * flowId string
>
>     * client\_id string
>
>     * signCookie boolean
>
>     * createdDate number
>
>     * cookieExpiresInSeconds number
>
>     * loa number
>
> Output Example
>
> ```json
> {
>   "userId": "mzDcrsYnonx8S9JTyblHD0bHeE9quaZJ",
>   "connectionId": "HVxcjWW8sBFrduEe6vdryxUSInua51tK",
>   "companyId": "mzDcrsYnonx8S9JTyblHD0bHeE9quaZJ",
>   "ip": "192.168.0.4",
>   "userAgent": "",
>   "flowId": "mzDcrsYnonx8S9JTyblHD0bHeE9quaZJ",
>   "client_id": "mzDcrsYnonx8S9JTyblHD0bHeE9quaZJ",
>   "signCookie": true,
>   "createdDate": 1606535447,
>   "cookieExpiresInSeconds": 1000,
>   "loa": 1
> }
> ```

### Set Session Cookie (Non User)

Set an opaque session cookie with a set of custom claims.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> - - cookieName textField
>   - useSecureCookie toggleSwitch
>   - useHttpOnlyCookie toggleSwitch
>   - cookieExpiresInSeconds textField
>   - cookieDomain textField
>   - Cookie Path textField
>
>   The path where the cookie will be accessible
>
> - * cookieSameSite dropDown
>   * signCookie toggleSwitch
>   * setCookieClientSide toggleSwitch
>   * claimsNameValuePairsSessionCookie selectNameValueListColumn
>   * useSessionTokenFlag toggleSwitch
>   * sessionToken textField
>
> * default object
>
>   * ip string minLength: 1 maxLength: 50
>
>     Ip address of the user in current session.
>
>   * userAgent string minLength: 1 maxLength: 250
>
>     Information about browser, OS, etc. of user in current session.
>
>   * skOpenId object
>
>     Object containing client id of user.
>
>   * origin string minLength: 0 maxLength: 500
>
>     Origin
>
>   * originCookies string minLength: 0 maxLength: 20000
>
>     OriginCookies

### Check Session Cookie (Non User)

Check if a specific session cookie exists and retrieve the custom claims for decision-making purposes.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - - cookieName textField
>   - enforceClientIP toggleSwitch
>   - enforceFlowIdMatch toggleSwitch
>
> * default object
>
>   * userAgent string minLength: 1 maxLength: 250
>
>     Information about browser, OS, etc. of user in current session.
>
>   * ip string minLength: 1 maxLength: 50
>
>     Ip address of the user in current session.
>
>   * cookies object
>
>     List of cookies associated with the user.
>
>   * skOpenId object
>
>     Object containing client id of user.
>
>   * origin string minLength: 0 maxLength: 500
>
>     Origin
>
>   * originCookies string minLength: 0 maxLength: 20000
>
>     OriginCookies
>
> - output object
>
>   * claims object
>
>     * ip string
>
>     * userAgent number
>
>     * flowId string
>
>     * client\_id string
>
>     * signCookie boolean
>
>     * createdDate number
>
>     * cookieExpiresInSeconds number
>
>     * loa number
>
> Output Example
>
> ```json
> {
>   "ip": "192.168.0.4",
>   "userAgent": "",
>   "flowId": "mzDcrsYnonx8S9JTyblHD0bHeE9quaZJ",
>   "client_id": "mzDcrsYnonx8S9JTyblHD0bHeE9quaZJ",
>   "signCookie": true,
>   "createdDate": 1606535447,
>   "cookieExpiresInSeconds": 1000,
>   "loa": 1
> }
> ```