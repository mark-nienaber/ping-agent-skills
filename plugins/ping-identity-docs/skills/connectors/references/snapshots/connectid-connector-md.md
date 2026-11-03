---
title: ConnectID Connector
description: Configure the ConnectID connector in PingOne DaVinci to request identity verification through the ConnectID identity exchange as a FAPI-compliant relying party
component: connectors
page_id: connectors::connectid_connector
canonical_url: https://docs.pingidentity.com/connectors/connectid_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-09-08T00:00:00Z
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  configuring-the-connectid-connector: Configuring the ConnectID connector
  connector-configuration: Connector configuration
  using-the-connector-in-a-flow: Using the connector in a flow
  verifying-a-customers-identity-as-a-relying-party: Verifying a customer's identity as a relying party
  capabilities: Capabilities
  initializeAuthorizationRequest: Verify as a Relying Party
---

# ConnectID Connector

The ConnectID connector lets you request verification of a customer's identity through [ConnectID](https://www.auspayplus.com.au/solutions/connectid) in your PingOne DaVinci flow.

ConnectID is an identity exchange accredited by the Australian Government that lets customers prove who they are using an organization they already trust, such as their bank. Customers verify themselves with a trusted institution, and their data is shared with your business through a secure API. ConnectID doesn't see or store personal information. The connector is a FAPI compliant OpenID Connect (OIDC) *(tooltip: \<div class="paragraph">
\<p>An authentication protocol built on top of OAuth that authenticates users and enables clients (relying parties) of all types to request and receive information about authenticated sessions and users. OIDC is extensible, allowing clients to use optional features such as encryption of identity data, discovery of OpenID Providers (OAuth authorization servers), and session management.\</p>
\</div>)* connector that lets you participate as a relying party in the ConnectID ecosystem.

## Setup

### Resources

You can find more information and setup help in the following:

* ConnectID documentation:

  * [ConnectID identity exchange](https://www.auspayplus.com.au/solutions/connectid)

* PingOne DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using PingOne DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A PingOne account.

* A ConnectID account with administrator access.

* The client ID, KID, and CA certificate issued to you by ConnectID.

* A PingOne signing key ID and PingOne outbound mTLS key ID.

### Configuring the ConnectID connector

Add the connector in PingOne DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

| Setting                  | Description                                                                                                                                                                                                                                   |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Redirect URL             | The PingOne DaVinci callback URL for this connector. This value is provided automatically as a read-only field and allows ConnectID to continue the flow. Copy it into your ConnectID configuration.                                          |
| Client ID                | The client ID provided to you by ConnectID.                                                                                                                                                                                                   |
| PingOne Signing Key ID   | The UUID of the PingOne signing key used to sign requests.                                                                                                                                                                                    |
| PingOne mTLS Key ID      | The UUID of the PingOne outbound mTLS key used for mutual TLS connections.                                                                                                                                                                    |
| ConnectID CA Certificate | The ConnectID certificate authority certificate.                                                                                                                                                                                              |
| ConnectID KID            | The key ID provided to you by ConnectID.                                                                                                                                                                                                      |
| Scope                    | The scopes to send to ConnectID to customize the verification process. The default is openid.                                                                                                                                                 |
| Application Redirect URL | Optional. Your application's redirect URL, such as `https://app.yourorganization.com/`. Enter this URL if you embed the PingOne DaVinci widget in your application so that PingOne DaVinci can redirect the browser back to your application. |

## Using the connector in a flow

### Verifying a customer's identity as a relying party

The **Verify as a Relying Party** capability requests verification of a customer's identity through the ConnectID service and returns the verified claims to your flow.

At a high level:

1. The **Verify as a Relying Party** capability sends an authorization request to ConnectID with the well-known configuration endpoint and claims object you specify in the node. The claims object is a JSON value that can include PingOne DaVinci parameters, which are replaced at runtime.

2. The customer verifies their identity with a trusted institution, such as their bank, and consents to share the requested data.

3. ConnectID redirects back to PingOne DaVinci and the capability outputs the verified claims, including the token response, that you can evaluate in your flow.

Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Verify as a Relying Party

This capability allows you to participate as a Relying Party in the ConnectID ecosystem for verification purposes.

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - Well-Known Configuration Endpoint textField required
>
>   ConnectID Well-Known Configuration Endpoint
>
> - Claims Object (JSON) textArea
>
>   This property needs to be a properly formatted JSON value. It can contain DaVinci parameters, which will be replaced at runtime. If you are using DaVinci parameters that are of type 'string', you will need to put string quotes around it.
>
>   Default:
>
>   ```none
>   {
>    "id_token": {
>    "verified_claims": {
>    "verification": {
>    "trust_framework": "au_connectid"
>    },
>    "claims": {
>    "over18": {
>    "essential": true
>    }
>    }
>    },
>    "txn": {
>    "essential": true
>    },
>    "name": {
>    "essential": true
>    },
>    "given_name": {
>    "essential": true
>    },
>    "middle_name": {
>    "essential": true
>    },
>    "family_name": {
>    "essential": true
>    },
>    "email": {
>    "essential": true
>    },
>    "birthdate": {
>    "essential": true
>    },
>    "phone_number": {
>    "essential": true
>    },
>    "address": {
>    "essential": true
>    }
>    }
>   }
>   ```
>
> * output object
>
>   * statusCode integer
>
>   * rawResponse object
>
>   * tokenResponse object
>
>     * id_token object
>
>     * access_token string
>
>     * token_type string
>
>     * expires_in number