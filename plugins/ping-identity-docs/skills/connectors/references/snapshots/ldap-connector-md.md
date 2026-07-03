---
title: LDAP Connector
description: The Lightweight Directory Access Protocol (LDAP) connector for PingOne DaVinci lets you gain access to entries in an LDAP directory to be used in your PingOne DaVinci flow.
component: connectors
page_id: connectors::ldap_connector
canonical_url: https://docs.pingidentity.com/connectors/ldap_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-the-ldap-connector: Setting up the LDAP connector
  setting-up-the-connector-configuration: Setting up the connector configuration
  connector-settings: Connector settings
  environment-id: Environment ID
  client-id: Client ID
  client-secret: Client secret
  region: Region
  using-the-connector-in-a-flow: Using the connector in a flow
  managing-entries-in-an-ldap-directory-store: Managing entries in an LDAP directory store
  managing-passwords-in-an-ldap-directory-store: Managing passwords in an LDAP directory store
  managing-attributes-in-an-ldap-directory-store: Managing attributes in an LDAP directory store
  pass-base64-encoded-ldap-controls: Pass base64-encoded LDAP controls
  example-active-directory-server-policy-hints-control: "Example: Active directory server policy hints control"
  troubleshooting-ldap-controls-errors: Troubleshooting LDAP controls errors
  capabilities: Capabilities
  search: LDAP Search
  add: LDAP Add
  delete: LDAP Delete
---

# LDAP Connector

The Lightweight Directory Access Protocol (LDAP) *(tooltip: \<div class="paragraph">
\<p>An open, cross platform protocol used for interacting with directory services.\</p>
\</div>)* connector for PingOne DaVinci lets you gain access to entries in an LDAP directory to be used in your PingOne DaVinci flow.

You can use the LDAP connector to:

* Create a new entry in your LDAP store.

* Reset a user's password, including generating a new password.

* Update a user or group's profile.

* Delete an entry from your LDAP store.

* Search for and view a user's group membership.

## Setup

### Resources

Learn more in the following documentation:

* PingOne Gateway documentation:

  * [Introduction to Gateways](https://docs.pingidentity.com/pingone/integrations/p1_gateways.html)

  * Documentation for your LDAP directory, such as [PingDirectory](https://docs.pingidentity.com/pingdirectory/10.3/pd_ds_landing_page.html):

  * [Introduction to PingDirectory Server](https://docs.pingidentity.com/pingdirectory/10.3/pd_ds_intro_pindirectory_server.html)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* An LDAP directory store, such as PingDirectory:

  * Learn more in [Supported directories](https://docs.pingidentity.com/pingone/integrations/p1_ldap_gateways.html).

* Your LDAP directory store credentials

* A PingOne LDAP Gateway installation

* A worker application for userless administration:

  * Learn more in the [Worker application](https://docs.pingidentity.com/pingdirectory/latest/pingdatasync_server_administration_guide/pd_sync_create_p1_worker_app.html) documentation.

### Setting up the LDAP connector

Review the prerequisites in [Before you begin](https://docs.pingidentity.com/pingone/integrations/p1_gateway_prereqs.html), and then follow the gateway set up instructions in [Overview](https://docs.pingidentity.com/pingone/integrations/p1_gateways_overview.html).

### Setting up the connector configuration

In DaVinci, add an LDAP connector. Learn more in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html).

#### Connector settings

##### Environment ID

Your PingOne Environment ID. In PingOne, go to **Environment > Properties**.

##### Client ID

The **Client ID** for your PingOne Worker application. In PingOne, go to **Applications > Your application > Configuration**.

##### Client secret

The **Client secret** for your PingOne Worker application. In PingOne, go to **Applications > Your application > Configuration**.

##### Region

Your PingOne environment region. In PingOne, go to **Environment > Properties**.

## Using the connector in a flow

### Managing entries in an LDAP directory store

The connector has several capabilities that allow you to manage entries in your LDAP directory store:

* **Create entry**

* **Modify DN**

* **Search entries**

* **Delete entry**

![A screen capture of the Create LDAP entry capability being employed in a flow. The flow includes variable initialization, the sending of an entry-creation request, and a success or error HTML message based on the results of this request.](_images/connector-images/dvc-ldap-create-ldap-entry-capability.png)

This flow allows the user to create a new entry in any LDAP directory.

1. Customize the entry-creation parameters:

   1. Select the **Create LDAP entry** node.

   2. In the **DN** field, customize the distinguished name of the new entry.

   3. In the **Attributes** section, click the **Add** button. In the **Variable Name** field, enter `objectClass`, and in the **Value** field, enter the name of the new entry's objectClass according to the directory schema.

      |   |                                                                                                                                                                                                                                                                                                                                                                                                                    |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | The objectClass attribute value differs depending on the directory. For example, a new PingDirectory entry is an instance of the `inetOrgPerson` objectClass, while a new Active Directory (AD) *(tooltip: \<div class="paragraph">&#xA;\<p>A directory service for Windows domain networks, included in most Windows Server operation systems.\</p>&#xA;\</div>)* entry is an instance of the `user` objectClass. |

   4. In the **Attributes** section, click the **Add** button and populate the **Variable Name** and **Value** fields with information on the entry's username.

      |   |                                                                                                                                                                                                                              |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | The **Variable Name** differs depending on the directory. For example, a new PingDirectory entry's username requires a variable name of `uid`, while a new AD entry's username requires a variable name of `sAMAccountName`. |

   5. (Optional) In the **Attributes** section, add other attributes as permitted by the new entry's objectClass.

   6. In the **Perform Operation As** list, select the user account performing the entry creation.

   7. Click **Apply**.

### Managing passwords in an LDAP directory store

The connector has several capabilities that allow you to manage different entries' passwords in your LDAP directory store:

* **Generate password**

* **Reset password**

* **Check password**

No special flow configuration is needed. Add the capability that you want and populate its properties according to the help text.

### Managing attributes in an LDAP directory store

The connector has several capabilities that allow you to manage different entries' attributes in your LDAP directory store:

* **Modify attributes**

* **Replace attributes**

No special flow configuration is needed. Add the capability that you want and populate its properties according to the help text.

### Pass base64-encoded LDAP controls

The LDAP connector supports many well-known controls natively. For any control that doesn't have native value-json support, you can also provide the control value using the value-base64 field.

1. In your **LDAP** node, in the **Controls** field, enter a JSON array.

   ```json
   [
     {
       "oid": "<control-OID>",
       "criticality": false,
       "value-base64": "<base64-encoded DER payload>"
     }
   ]
   ```

   Each array element defines one control:

   | Element        | Description                                                                                                         |
   | -------------- | ------------------------------------------------------------------------------------------------------------------- |
   | `oid`          | The dotted-decimal object identifier (OID) for the control.                                                         |
   | `criticality`  | Indicates whether the directory server must understand the control before it can continue processing the operation. |
   | `value-base64` | The control value, encoded as Base64 from raw DER/ASN.1 bytes.                                                      |

2. Build the value-base64 value.

   The **value-base64** field requires a Base64-encoded DER payload. For the correct ASN.1 structure, learn more in [PingDirectory LDAP Controls](https://developer.pingidentity.com/pingdirectory/directory/controls.html) in the API documentation if you're running PingDirectory. Otherwise, reference your directory vendor's documentation. You can find this in the directory type in your [User Type](https://docs.pingidentity.com/pingone/integrations/p1_add_a_user_type.html) configuration.

   DER encodes data as tag-length-value (TLV) elements. Common tags include `0x02` (INTEGER), `0x04` (OCTET STRING), `0x01` (BOOLEAN), and 0x30 (SEQUENCE). For nested structures, build the inner TLV elements first, concatenate them, and wrap them in the required outer element.

3. Base64-encode your DER bytes using one of these commands:

   * Bash

     ```bash
     printf '\x30\x03\x02\x01\x01' | base64
     ```

   * PowerShell

     ```powershell
     [Convert]::ToBase64String([byte[]](0x30,0x03,0x02,0x01,0x01))
     ```

     Both commands return:

     ```text
     MAMCAQE=
     ```

4. Paste the following JSON into the **Controls** field.

   ```json
   [
     {
       "oid": "1.2.840.113556.1.4.2239",
       "criticality": false,
       "value-base64": "MAMCAQE="
     }
   ]
   ```

#### Example: Active directory server policy hints control

The following example shows how to use the active directory server policy hints control, `1.2.840.113556.1.4.2239`, to apply normal password policy checks, including password history enforcement, during a password reset.

1. Find the ASN.1 syntax for the control in your directory vendor's documentation.

   The documented format for this control requires a sequence with a single integer field named `Flags`:

   ```asn1
   PolicyHintsRequestValue ::= SEQUENCE {
   Flags     INTEGER
   }
   ```

2. Use a `Flags` value of 1 to enforce the password history check.

   * **Tag**: `0x02` (INTEGER)

   * **Length**: `0x01`

   * **Value**: `0x01`

   * **Result**: `02 01 01`

3. Wrap the encoded integer bytes inside the outer sequence element:

   * **Tag**: `0x30` (SEQUENCE)

   * **Length**: `0x03` (The total number of bytes in the inner element)

   * **Value**: `02 01 01`

   * **Result**: `30 03 02 01 01`

4. Base64-encode the final DER bytes , `30 03 02 01 01`, using one of these commands:

   * Bash

     ```bash
     printf '\x30\x03\x02\x01\x01' | base64
     ```

   * PowerShell

     ```powershell
     [Convert]::ToBase64String([byte[]](0x30,0x03,0x02,0x01,0x01))
     ```

     Both commands return: `MAMCAQE=`

5. Paste the following JSON into the **Controls** field:

   ```json
   [
     {
       "oid": "1.2.840.113556.1.4.2239",
       "criticality": false,
       "value-base64": "MAMCAQE="
     }
   ]
   ```

#### Troubleshooting LDAP controls errors

* Unavailable critical extension errors

  The `unavailableCriticalExtension` result code indicates that your request included a control with `criticality` set to `true`, but the directory server could not process it. This usually happens if:

  * The server doesn't support the control.

  * The control isn't valid for the requested operation type.

  * The request doesn't meet the required conditions for the control.

  * The control is only supported for specific parts of the Directory Information Tree (DIT). For example, some controls only work on user entries and will fail on server-provided entries like the root DSE, schema subentry, or configuration entries.

    Check your LDAP directory server to ensure it supports the control, and validate you're using the right control.

* `INVALID_VALUE` validation errors

  An `INVALID_VALUE` error means the control was malformed or contained invalid attributes.

  ```json
  {
  "id":"6e5abbdd-1079-40fe-8a72-06c246e37bd4",
  "code":"INVALID_REQUEST",
  "message":"The request could not be completed. The request was malformed or invalid.",
  "details":[
  {
  "code":"INVALID_VALUE",
  "target":"controls",
  "message":"Invalid value for attribute."
  }
  ]
  }
  ```

  If you're passing a value to the value-base64 field, check your DER byte sequence and make sure it's properly encoded as a valid Base64 string.

## Capabilities

### LDAP Search

Execute ldap/ad searches

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - baseDN textField
>   - ldapScope dropDown
>   - ldapFilter textField
>   - ldapAttributes textFieldArrayView
>
> * output object

### LDAP Add

Add entry to your LDAP Directory

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - - DN textField
>   - New User Entry Fields selectNameValueListColumn
>
>   Use this section to add additional fields to the response
>
> * output object

### LDAP Delete

Delete entry from your LDAP Directory

> **Collapse: Show details**
>
> * Properties
>
> * Output Schema
>
> - DN textField
>
> * output object
