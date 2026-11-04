---
title: ID.me Community Verification Connector
description: Configure the ID.me Community Verification connector in PingOne DaVinci to verify user community affiliation with ID.me and return verified user attributes to your flow
component: connectors
page_id: connectors::idme_community_verification_connector
canonical_url: https://docs.pingidentity.com/connectors/idme_community_verification_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-08T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-id-me-community-verification-connector: Configuring the ID.me Community Verification connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  verifying-user-community-affiliation: Verifying user community affiliation
  capabilities: Capabilities
  loginFirstFactor: Redirect to ID.me
---

# ID.me Community Verification Connector

The ID.me Community Verification connector lets you verify a user's community affiliation with [ID.me](https://developers.id.me/) in your PingOne DaVinci flow.

The connector redirects the user to ID.me, where they verify their affiliation with communities such as military, teacher, first responder, nurse, and student, and returns verified user attributes that you can use in your flow.

## Setup

### Resources

You can find more information and setup help in the following:

* ID.me documentation:

  * [ID.me Developer Portal](https://developers.id.me/)

  * [ID.me developer documentation](https://docs.id.me/)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

For help with your ID.me integration, contact ID.me partner support at <partnersupport@id.me>.

### Requirements

To use the connector, you'll need:

* An ID.me developer account.

* An ID.me application with a client ID and client secret.

* The DaVinci Redirect URI added to your ID.me application configuration.

### Configuring the ID.me Community Verification connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                   | Description                                                                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Redirect URI              | The PingOne DaVinci redirect URI for this connector. This value is provided automatically as a read-only field and should be copied into your ID.me application configuration.                  |
| Provider Name             | The display name for this connection shown in the flow.                                                                                                                                         |
| Client ID                 | The client ID from your ID.me application.                                                                                                                                                      |
| Client Secret             | The client secret from your ID.me application.                                                                                                                                                  |
| Authorization Endpoint    | The ID.me endpoint used for authorization. Select **Single Group** to verify against one community verification policy, or **Multiple Groups** to let users verify against more than one group. |
| Scope                     | The community verification policies to request. The openid scope is mandatory. Select one or more additional community scopes, such as military, teacher, first responder, nurse, or student.   |
| Send state with request   | Optional. Sends a unique state value with every request.                                                                                                                                        |
| Application Return To URL | Optional. When using the embedded flow player widget with an identity provider (IdP) or social login connector, provide a callback URL for returning to your application.                       |

## Using the connector in a flow

### Verifying user community affiliation

The **Redirect to ID.me** capability redirects the user to the ID.me Community Verification endpoint, where they prove their community affiliation and consent to share their attributes with your application.

At a high level:

1. The **Redirect to ID.me** capability sends the user to ID.me to authenticate and verify their community affiliation using the scopes you selected in the connector configuration.

2. After verification, ID.me redirects back to PingOne DaVinci and the connector outputs the user attributes, such as the user's ID and access tokens, that you can evaluate in your flow.

|   |                                                                                                                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Users who have already verified their community affiliation with ID.me through a partner in the ID.me network are not prompted to verify again unless their credentials expire. These users still have to accept the permissions to share the user attributes your application requests. To enforce community verification for your application, contact ID.me at <partnersupport@id.me>. |

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Redirect to ID.me

Redirect to the ID.me Community Verification Endpoint

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - Display Name button
>   - showPoweredBy toggleSwitch
>   - skipButtonPress toggleSwitch
>
> * output object
>
>   * sub string
>
>   * aud string
>
>   * jti string
>
>   * iss string
>
>   * iat number
>
>   * exp number
>
>   * auth_time string
>
>   * tokens object
>
>     * access_token string
>
>     * refresh_token string
>
>     * id_token string
>
>     * token_type string
>
>     * expires_at number
>
>   * connectionId string
>
>   * connectorId string