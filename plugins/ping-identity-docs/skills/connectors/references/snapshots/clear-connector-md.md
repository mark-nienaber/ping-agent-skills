---
title: CLEAR Connector
description: The CLEAR connector lets you verify users using CLEAR's hosted identity verification UI in your PingOne DaVinci flow.
component: connectors
page_id: connectors::clear_connector
canonical_url: https://docs.pingidentity.com/connectors/clear_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 14, 2025
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-clear-connector: Configuring the CLEAR connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  verifying-a-users-identity-with-clear: Verifying a user's identity with CLEAR
  reverifying-a-returning-user-with-clear: Reverifying a returning user with CLEAR
  capabilities: Capabilities
  initializeAuthorizationRequest: Redirect to CLEAR
---

# CLEAR Connector

The CLEAR connector lets you verify users using [CLEAR's](https://www.clearme.com/) hosted identity verification UI in your PingOne DaVinci flow.

The connector redirects users to CLEAR for identity verification and receives the verification results, including verified identity traits and document data, that you can use in your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A CLEAR account with API access

* A CLEAR API Key

* A CLEAR Verification Project ID

### Configuring the CLEAR connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                             | Description                                                                                                                                      |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **DaVinci Redirect URL**            | The DaVinci redirect URL for this connector. This value is provided automatically as a read-only field.                                          |
| **Application Return To URL**       | The URL where the user is redirected after completing the CLEAR verification flow. If not provided, CLEAR uses a default completion page.        |
| **API Key**                         | Your CLEAR API Key used to authenticate requests to the CLEAR API.                                                                               |
| **Initial Verification Project ID** | The CLEAR project ID used for initial identity verification of new users.                                                                        |
| **Re-verification Project ID**      | The CLEAR project ID used for reverification of returning users. If not provided, the Initial Verification Project ID is used.                   |
| **Secure Endpoint Selection**       | The CLEAR API endpoint to use. Select either `verified.clearme.com` or `secure.verified.clearme.com`, based on your CLEAR account configuration. |

## Using the connector in a flow

### Verifying a user's identity with CLEAR

![A screen capture of the CLEAR verification flow.](_images/connector-images/tap-clear-verification-flow.png)

This example flow redirects the user to the CLEAR hosted verification UI and displays the verification session results.

At a high level:

1. The **Redirect to CLEAR** node redirects the user to the CLEAR verification UI for initial identity verification.

2. After the user completes verification, the flow receives the session results and displays them using a **Custom HTML Message** node.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

### Reverifying a returning user with CLEAR

![A screen capture of the CLEAR reverification flow.](_images/connector-images/tap-clear-reverification-flow.png)

This example flow checks whether a user has an existing CLEAR identity and routes them to either initial verification or reverification accordingly.

At a high level:

1. The flow authenticates the user and reads the user profile from PingOne to check for an existing CLEAR user ID.

2. If no CLEAR user ID exists, the flow redirects to CLEAR for **initial verification**, then stores the returned CLEAR user ID on the PingOne user object for future reverification sessions.

3. If a CLEAR user ID already exists, the flow redirects to CLEAR for **reverification** using the stored user ID, which streamlines the verification process for returning users.

4. The flow displays the verification or reverification results.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Redirect to CLEAR

Redirect user to CLEAR

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Redirect URL textField required
>
>   The target URL for the post-verification redirect.
>
> - User ID textField
>
>   CLEAR user ID for re-verification. When provided, triggers a re-verification flow against an existing CLEAR identity instead of a full initial verification.
>
> - Custom Fields keyValueList
>
>   Custom key-value pairs passed to CLEAR (e.g., your internal customer or employee ID for identity matching).
>
> - First Name textField
>
>   User's first name for CLEAR identity matching.
>
> - Last Name textField
>
>   User's last name for CLEAR identity matching.
>
> - Date of Birth textField
>
>   User's date of birth for CLEAR identity matching.
>
> - Phone textField
>
>   User's phone number for CLEAR identity matching.
>
> - Email textField
>
>   User's email address for CLEAR identity matching.
>
> - Address Line 1 textField
>
>   User's street address line 1 for CLEAR identity matching.
>
> - Address Line 2 textField
>
>   User's street address line 2 for CLEAR identity matching.
>
> - City textField
>
>   User's city for CLEAR identity matching.
>
> - State textField
>
>   User's state for CLEAR identity matching.
>
> - Postal Code textField
>
>   User's postal code for CLEAR identity matching.
>
> - Country textField
>
>   User's country for CLEAR identity matching.
>
> * output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * id string
>
>   * object\_name string
>
>   * authenticated boolean
>
>   * authentication\_methods array
>
>   * activated\_authentication\_methods array
>
>   * checks array
>
>   * completed\_at number
>
>   * created\_at number
>
>   * email string
>
>   * expires\_at number
>
>   * fields\_to\_collect array
>
>   * ip array
>
>   * phone string
>
>   * redirect\_url string
>
>   * status string
>
>   * token string
>
>   * updated\_at number
>
>   * user\_agent array
>
>   * user\_created boolean
>
>   * user\_id string
>
>   * traits object
>
>     * address object
>
>       * line1 string
>
>       * line2 string
>
>       * city string
>
>       * state string
>
>       * postal\_code string
>
>       * country string
>
>     * dob object
>
>       * day number
>
>       * month number
>
>       * year number
>
>     * email string
>
>     * first\_name string
>
>     * last\_name string
>
>     * middle\_name string
>
>     * second\_family\_name string
>
>     * full\_last\_name string
>
>     * phone string
>
>     * ssn4 string
>
>     * ssn9 string
>
>     * identification\_number string
>
>     * identification\_type string
>
>     * document object
>
>       * nationality string
>
>       * document\_type string
>
>       * issuing\_country string
>
>       * document\_number string
>
>       * date\_of\_expiry object
>
>         * day number
>
>         * month number
>
>         * year number
>
>       * gender string
>
>       * date\_of\_birth object
>
>         * day number
>
>         * month number
>
>         * year number
>
>       * first\_name string
>
>       * last\_name string
>
>       * middle\_name string
>
>     * document\_front string
>
>     * document\_back string
>
>     * face\_scan\_preview string
>
>   * project\_id string
>
>   * custom\_fields object
>
>   * user\_profile\_information object
>
>     * name object
>
>       * first\_name string
>
>       * last\_name string
>
>       * middle\_name string
>
>     * dob string
>
>     * phone string
>
>     * address object
>
>       * line1 string
>
>       * line2 string
>
>       * city string
>
>       * state string
>
>       * postal\_code string
>
>       * country string
>
>     * email string
>
>   * user\_profile\_match\_status string
>
>   * idv\_status string
>
>   * sessions array