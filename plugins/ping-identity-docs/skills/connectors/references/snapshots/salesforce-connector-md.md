---
title: Salesforce Connector
description: The Salesforce connector lets you manage users and records in Salesforce from your PingOne DaVinci flows.
component: connectors
page_id: connectors::salesforce_connector
canonical_url: https://docs.pingidentity.com/connectors/salesforce_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirements: Requirements
  setting-up-salesforce: Setting up Salesforce
  using-the-connector-in-a-flow: Using the connector in a flow
  user-management: User management
  record-management: Record management
  document-upload: Document upload
  creating-a-custom-api-call: Creating a custom API call
  capabilities: Capabilities
  createUser: Create User
  readUser: Read User
  updateUser: Update User
  readRecord: Read Record
  updateRecord: Update Record
  searchRecord: Search Record
  uploadDocument: Upload Document
  makeCustomApiCall: Make Custom API Call
---

# Salesforce Connector

The Salesforce connector lets you manage users and records in Salesforce from your PingOne DaVinci flows.

You can use the Salesforce connector to:

* Read, create, and update users.

* Read, update, and search records.

* Upload documents.

* Set up a custom API call to Salesforce.

## Setup

### Resources

Learn more in the following:

* Salesforce:

  * [Quick Start](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm)

  * [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm\&type=5)

  * [User fields](https://help.salesforce.com/s/articleView?id=sf.user_fields.htm)

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirements

To use the connector, you'll need:

* A Salesforce administrator account

* Your Salesforce access and connected app information:

  * Username

  * Salesforce domain name

### Setting up Salesforce

To configure the Salesforce environment to use the Salesforce connector in DaVinci:

1. Sign on to a Salesforce production, developer, or sandbox account.

2. Create a new application to tie to the Salesforce connector:

   1. In the **Platform Tools** section, click **App Manager**.

   2. Click **New Connected App**.

   3. Complete the required fields for app name, API name, and contact email.

      |   |                                                                                                                                                                                                                                                                                                                                                                                          |
      | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | You must enter a valid email. This is required for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">&#xA;\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>&#xA;\</div>)* when performing sensitive operations like looking at the **Client ID** and **Secret**. |

   4. For **Call back URL**, enter `https://oauth.pingone.com/ocs/ppm/rest/v1/oauth/oastempcredresponse/` to approve the application to the administrative user later.

      |   |                                                                                         |
      | - | --------------------------------------------------------------------------------------- |
      |   | This URL is required for the Salesforce administrator to approve the application later. |

3. Create a certificate that will act as a digital signature for the Salesforce connector:

   1. Follow the steps to create a certificate in the [Salesforce DX Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm) or use your own if you already have one.

   2. Select the **Use digital signature** check box and then select your **Public Key** from the previous step.

   3. For **Selected OAuth Scopes**, select **Manage user data via APIs (api)**.

      |   |                                                                                                                          |
      | - | ------------------------------------------------------------------------------------------------------------------------ |
      |   | Ensure that the **Require Secret for Web Server Flow** and **Require Secret for Refresh Token Flow** boxes are selected. |

4. Save the application.

5. Approve the application:

   |   |                                                                                                                                 |
   | - | ------------------------------------------------------------------------------------------------------------------------------- |
   |   | The Salesforce connector requires a Salesforce administrator account. The specified administrator must approve the application. |

   1. Select **App Manager** and find the application that you created.

   2. In the drop-down list, select **View**.

   3. To get the **Consumer Key** and **Secret**, click **Manage Consumer Details**, then **Open**.

   4. Enter the one-time passcode (OTP) *(tooltip: \<div class="paragraph">
      \<p>A passcode valid for only one sign-on or transaction on a computer system or other digital device. Also known as a one-time password, one-time PIN, or dynamic password.\</p>
      \</div>)* value from your email in the **Verification Code** field, then click **Verify**.

   5. Open an incognito or private browser session and go to the PingOne OAuth configuration service.

   6. In the drop-down list, select **Salesforce Production Connector** or **Salesforce Sandbox Connector**.

      |   |                                                                                                         |
      | - | ------------------------------------------------------------------------------------------------------- |
      |   | If you are using a Salesforce developer account, select the **Salesforce Production Connector** option. |

   7. Copy the **Consumer Key** and **Secret** from the Salesforce application details window in the **Client ID** and **Client Secret** fields in the PingOne OAuth configuration service, then click **Connect**.

   8. Sign on and approve the application.

      |   |                                                                                       |
      | - | ------------------------------------------------------------------------------------- |
      |   | Be sure to sign on with the administrator account that uses the Salesforce connector. |

6. In DaVinci, add a Salesforce connector to your flow.

7. Click **Configure** and complete the following fields:

   * Username

     The administrator email used to approve the OAuth application.

   * Consumer Key

     The consumer key that you created for your connected app in Salesforce. This can be found under **Manage Consumer Details** in your Salesforce environment.

   * Private Key

     The consumer key that you created to set up JSON Web Token (JWT) *(tooltip: \<div class="paragraph">
     \<p>An IETF standard container format for a JSON object used for the secure exchange of content, such as identity or entitlement information. You can find the industry standard in \<a href="https\://datatracker.ietf.org/doc/html/rfc7519">RFC 7519\</a>.\</p>
     \</div>)* Bearer authentication in Salesforce.

   * Domain Name

     Your Salesforce domain name, such as `mycompany-dev-ed` Leave off the `.my.salesforce.com` or `.lightning.force.com`. If your Salesforce account does not have a domain name, you must set one up. Learn more in [Custom Domains](https://help.salesforce.com/s/articleView?id=sf.domain_mgmt_add.htm\&type=5) in the Salesforce documentation.

## Using the connector in a flow

### User management

The connector has several capabilities that allow you to manage users:

* **Read User**

* **Create User**

* **Update User**

No special configuration is needed. Add the capability and populate its properties according to the help text.

### Record management

The connector has several capabilities that allow you to manage records:

* **Read Record**

* **Search Record**

* **Update Record**

No special configuration is needed. Add the capability and populate its properties according to the help text.

|   |                                                                                                                                                                                                                                              |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Learn how to build a query for the **Search Record** capability in [Salesforce Object Query Language](https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql.htm) in the Salesforce documentation. |

### Document upload

![A screen capture of the complete document upload flow.](_images/connector-images/dvc-salesforce-document-upload-flow.png)

This flow allows the user to upload a document, such as an image or PDF, to Salesforce.

1. Download the [Salesforce - Document upload](https://marketplace.pingone.com/item/salesforce-document-upload) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. (Optional) Customize the file upload form.

   ![A screen capture of the document upload form.](_images/connector-images/dvc-salesforce-upload-document-form.png)

   1. Select the **Upload Form** node.

   2. In the **HTML Template** field, customize the page displayed to users when signing on.

      |   |                                                                                                                                                                                                                                                                                                       |
      | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
      |   | * Click **Switch View** to display the HTML formatted with syntax highlighting.

      * Click the **Maximize** ([icon: expand, set=fas]) icon to give yourself more room to work.

      * To access a variety of useful tools, right-click the field when you're in syntax highlighting mode (dark background). |

   3. Click **Apply**.

3. Customize the file upload destination and keywords:

   1. Select the **Upload Document** node.

   2. (Optional) In the **Name** and **Description** fields, customize the values.

   3. In the **Folder** list, select the destination Salesforce folder. If the folder you want isn't listed, select **Use Custom Folder ID** and enter the ID, such as `00l8a000002XKVQAA4`, in the **Custom Folder ID** field.

   4. (Optional) In the **Keywords** field, enter the searchable tags to associate with the documents in Salesforce. Enter a keyword and press Enter to add it.

      ![A screen recording of the user adding terms in the Keywords field.](_images/connector-images/dvc-salesforce-keywords-field-terms.gif)

   5. (Optional) Add additional field information in the **Document Fields** section by adding Salesforce fields and assigning values.

   6. Click **Apply**.

4. Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

### Creating a custom API call

If you want to do something that isn't supported by one of the provided capabilities, you can use the **Make a Custom API Call** capability to define your own action.

This capability uses the credentials from your connector to make an API call with the HTTP method, headers, query parameters, and body you specify.

## Capabilities

### Create User

Create a new user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Username textField required
>
>   The user's sign-on username, such as "<jsmith@example.com>". Must be in the form of an email address, using all lowercase characters. It must also be unique across all organizations.
>
> - First Name textField
>
>   The user's first name.
>
> - Last Name textField required
>
>   The user's last name.
>
> - Email textField required
>
>   The user's email address.
>
> - Alias textField required
>
>   The user's alias.
>
> - Email Encoding dropDown required
>
>   The email encoding for the user, such as ISO-8859-1 or UTF-8.
>
>   * Unicode (UTF-8) (Default)
>
>   * General US & Western Europe (ISO-8859-1, ISO-LATIN-1)
>
>   * Japanese (Shift-JIS)
>
>   * Japanese (JIS)
>
>   * Japanese (EUC)
>
>   * Korean (ks\_c\_5601-1987)
>
>   * Traditional Chinese (Big5)
>
>   * Simplified Chinese (GB2312)
>
>   * Traditional Chinese Hong Kong (Big5-HKSCS)
>
>   * Japanese (Shift-JIS\_2004)
>
> - Profile dropDown required
>
>   Profiles contain settings and permissions, which control what users can do. Displays up to 100 results. If the profile you want is not listed, select Use Profile ID.
>
>   * Use Profile ID (Default)
>
> - Profile ID textField required
>
>   The ID of the user's profile, such as "00e8a0000024zklAAA".
>
> - Timezone dropDown required
>
>   The user's timezone.
>
>   * (GMT+14:00) Line Islands Time (Pacific/Kiritimati)
>
>   * (GMT+13:00) Apia Standard Time (Pacific/Apia)
>
>   * (GMT+14:00) Apia Daylight Time (Pacific/Apia)
>
>   * (GMT+13:00) Phoenix Islands Time (Pacific/Enderbury)
>
>   * (GMT+13:00) Tokelau Time (Pacific/Fakaofo)
>
>   * (GMT+13:00) Tonga Standard Time (Pacific/Tongatapu)
>
>   * (GMT+12:45) Chatham Standard Time (Pacific/Chatham)
>
>   * (GMT+13:45) Chatham Daylight Time (Pacific/Chatham)
>
>   * (GMT+12:00) New Zealand Standard Time (Antarctica/McMurdo)
>
>   * (GMT+13:00) New Zealand Daylight Time (Antarctica/McMurdo)
>
>   * (GMT+12:00) Anadyr Standard Time (Asia/Anadyr)
>
>   * (GMT+12:00) Petropavlovsk-Kamchatski Standard Time (Asia/Kamchatka)
>
>   * (GMT+12:00) New Zealand Standard Time (Pacific/Auckland)
>
>   * (GMT+13:00) New Zealand Daylight Time (Pacific/Auckland)
>
>   * (GMT+12:00) Fiji Standard Time (Pacific/Fiji)
>
>   * (GMT+13:00) Fiji Summer Time (Pacific/Fiji)
>
>   * (GMT+12:00) Tuvalu Time (Pacific/Funafuti)
>
>   * (GMT+12:00) Marshall Islands Time (Pacific/Kwajalein)
>
>   * (GMT+12:00) Marshall Islands Time (Pacific/Majuro)
>
>   * (GMT+12:00) Nauru Time (Pacific/Nauru)
>
>   * (GMT+12:00) Gilbert Islands Time (Pacific/Tarawa)
>
>   * (GMT+12:00) Wake Island Time (Pacific/Wake)
>
>   * (GMT+12:00) Wallis & Futuna Time (Pacific/Wallis)
>
>   * (GMT+11:00) Casey Time (Antarctica/Casey)
>
>   * (GMT+11:00) Magadan Standard Time (Asia/Magadan)
>
>   * (GMT+11:00) Sakhalin Standard Time (Asia/Sakhalin)
>
>   * (GMT+11:00) Magadan Standard Time (Asia/Srednekolymsk)
>
>   * (GMT+11:00) Bougainville Standard Time (Pacific/Bougainville)
>
>   * (GMT+11:00) Vanuatu Standard Time (Pacific/Efate)
>
>   * (GMT+11:00) Solomon Islands Time (Pacific/Guadalcanal)
>
>   * (GMT+11:00) Kosrae Time (Pacific/Kosrae)
>
>   * (GMT+11:00) Norfolk Island Standard Time (Pacific/Norfolk)
>
>   * (GMT+12:00) Norfolk Island Daylight Time (Pacific/Norfolk)
>
>   * (GMT+11:00) New Caledonia Standard Time (Pacific/Noumea)
>
>   * (GMT+11:00) Ponape Time (Pacific/Ponape)
>
>   * (GMT+10:30) Lord Howe Standard Time (Australia/Lord\_Howe)
>
>   * (GMT+11:00) Lord Howe Daylight Time (Australia/Lord\_Howe)
>
>   * (GMT+10:00) Dumont-d'Urville Time (Antarctica/DumontDUrville)
>
>   * (GMT+10:00) Australian Eastern Standard Time (Antarctica/Macquarie)
>
>   * (GMT+11:00) Australian Eastern Daylight Time (Antarctica/Macquarie)
>
>   * (GMT+10:00) Vladivostok Standard Time (Asia/Ust-Nera)
>
>   * (GMT+10:00) Vladivostok Standard Time (Asia/Vladivostok)
>
>   * (GMT+10:00) Australian Eastern Standard Time (Australia/Brisbane)
>
>   * (GMT+10:00) Australian Eastern Standard Time (Australia/Currie)
>
>   * (GMT+11:00) Australian Eastern Daylight Time (Australia/Currie)
>
>   * (GMT+10:00) Australian Eastern Standard Time (Australia/Hobart)
>
>   * (GMT+11:00) Australian Eastern Daylight Time (Australia/Hobart)
>
>   * (GMT+10:00) Australian Eastern Standard Time (Australia/Lindeman)
>
>   * (GMT+10:00) Australian Eastern Standard Time (Australia/Melbourne)
>
>   * (GMT+11:00) Australian Eastern Daylight Time (Australia/Melbourne)
>
>   * (GMT+10:00) Australian Eastern Standard Time (Australia/Sydney)
>
>   * (GMT+11:00) Australian Eastern Daylight Time (Australia/Sydney)
>
>   * (GMT+10:00) Chamorro Standard Time (Pacific/Guam)
>
>   * (GMT+10:00) Papua New Guinea Time (Pacific/Port\_Moresby)
>
>   * (GMT+10:00) Chamorro Standard Time (Pacific/Saipan)
>
>   * (GMT+10:00) Chuuk Time (Pacific/Truk)
>
>   * (GMT+09:30) Australian Central Standard Time (Australia/Adelaide)
>
>   * (GMT+10:30) Australian Central Daylight Time (Australia/Adelaide)
>
>   * (GMT+09:30) Australian Central Standard Time (Australia/Broken\_Hill)
>
>   * (GMT+10:30) Australian Central Daylight Time (Australia/Broken\_Hill)
>
>   * (GMT+09:30) Australian Central Standard Time (Australia/Darwin)
>
>   * (GMT+09:00) Yakutsk Standard Time (Asia/Chita)
>
>   * (GMT+09:00) East Timor Time (Asia/Dili)
>
>   * (GMT+09:00) Eastern Indonesia Time (Asia/Jayapura)
>
>   * (GMT+09:00) Yakutsk Standard Time (Asia/Khandyga)
>
>   * (GMT+09:00) Korean Standard Time (Asia/Pyongyang)
>
>   * (GMT+09:00) Korean Standard Time (Asia/Seoul)
>
>   * (GMT+09:00) Japan Standard Time (Asia/Tokyo)
>
>   * (GMT+09:00) Yakutsk Standard Time (Asia/Yakutsk)
>
>   * (GMT+09:00) Palau Time (Pacific/Palau)
>
>   * (GMT+08:45) Australian Central Western Standard Time (Australia/Eucla)
>
>   * (GMT+08:00) Brunei Darussalam Time (Asia/Brunei)
>
>   * (GMT+08:00) Ulaanbaatar Standard Time (Asia/Choibalsan)
>
>   * (GMT+08:00) Hong Kong Standard Time (Asia/Hong\_Kong)
>
>   * (GMT+08:00) Irkutsk Standard Time (Asia/Irkutsk)
>
>   * (GMT+08:00) Malaysia Time (Asia/Kuala\_Lumpur)
>
>   * (GMT+08:00) Malaysia Time (Asia/Kuching)
>
>   * (GMT+08:00) China Standard Time (Asia/Macau)
>
>   * (GMT+08:00) Central Indonesia Time (Asia/Makassar)
>
>   * (GMT+08:00) Philippine Standard Time (Asia/Manila)
>
>   * (GMT+08:00) China Standard Time (Asia/Shanghai)
>
>   * (GMT+08:00) Singapore Standard Time (Asia/Singapore)
>
>   * (GMT+08:00) Taipei Standard Time (Asia/Taipei)
>
>   * (GMT+08:00) Ulaanbaatar Standard Time (Asia/Ulaanbaatar)
>
>   * (GMT+08:00) Australian Western Standard Time (Australia/Perth)
>
>   * (GMT+07:00) Davis Time (Antarctica/Davis)
>
>   * (GMT+07:00) Indochina Time (Asia/Bangkok)
>
>   * (GMT+07:00) Moscow Standard Time + 4 (Asia/Barnaul)
>
>   * (GMT+07:00) Indochina Time (Asia/Ho\_Chi\_Minh)
>
>   * (GMT+07:00) Hovd Standard Time (Asia/Hovd)
>
>   * (GMT+07:00) Western Indonesia Time (Asia/Jakarta)
>
>   * (GMT+07:00) Krasnoyarsk Standard Time (Asia/Krasnoyarsk)
>
>   * (GMT+07:00) Krasnoyarsk Standard Time (Asia/Novokuznetsk)
>
>   * (GMT+07:00) Novosibirsk Standard Time (Asia/Novosibirsk)
>
>   * (GMT+07:00) Indochina Time (Asia/Phnom\_Penh)
>
>   * (GMT+07:00) Western Indonesia Time (Asia/Pontianak)
>
>   * (GMT+07:00) Moscow Standard Time + 4 (Asia/Tomsk)
>
>   * (GMT+07:00) Indochina Time (Asia/Vientiane)
>
>   * (GMT+07:00) Christmas Island Time (Indian/Christmas)
>
>   * (GMT+06:30) Myanmar Time (Asia/Rangoon)
>
>   * (GMT+06:30) Cocos Islands Time (Indian/Cocos)
>
>   * (GMT+06:00) Vostok Time (Antarctica/Vostok)
>
>   * (GMT+06:00) East Kazakhstan Time (Asia/Almaty)
>
>   * (GMT+06:00) Kyrgyzstan Time (Asia/Bishkek)
>
>   * (GMT+06:00) Bangladesh Standard Time (Asia/Dhaka)
>
>   * (GMT+06:00) Omsk Standard Time (Asia/Omsk)
>
>   * (GMT+06:00) East Kazakhstan Time (Asia/Qostanay)
>
>   * (GMT+06:00) Bhutan Time (Asia/Thimphu)
>
>   * (GMT+06:00) China Standard Time (Asia/Urumqi)
>
>   * (GMT+06:00) Indian Ocean Time (Indian/Chagos)
>
>   * (GMT+05:45) Nepal Time (Asia/Kathmandu)
>
>   * (GMT+05:30) India Standard Time (Asia/Colombo)
>
>   * (GMT+05:30) India Standard Time (Asia/Kolkata)
>
>   * (GMT+05:00) Mawson Time (Antarctica/Mawson)
>
>   * (GMT+05:00) West Kazakhstan Time (Asia/Aqtau)
>
>   * (GMT+05:00) West Kazakhstan Time (Asia/Aqtobe)
>
>   * (GMT+05:00) Turkmenistan Standard Time (Asia/Ashgabat)
>
>   * (GMT+05:00) West Kazakhstan Time (Asia/Atyrau)
>
>   * (GMT+05:00) Tajikistan Time (Asia/Dushanbe)
>
>   * (GMT+05:00) Pakistan Standard Time (Asia/Karachi)
>
>   * (GMT+05:00) West Kazakhstan Time (Asia/Oral)
>
>   * (GMT+05:00) West Kazakhstan Time (Asia/Qyzylorda)
>
>   * (GMT+05:00) Uzbekistan Standard Time (Asia/Samarkand)
>
>   * (GMT+05:00) Uzbekistan Standard Time (Asia/Tashkent)
>
>   * (GMT+05:00) Yekaterinburg Standard Time (Asia/Yekaterinburg)
>
>   * (GMT+05:00) French Southern & Antarctic Time (Indian/Kerguelen)
>
>   * (GMT+05:00) Maldives Time (Indian/Maldives)
>
>   * (GMT+04:30) Afghanistan Time (Asia/Kabul)
>
>   * (GMT+04:00) Azerbaijan Standard Time (Asia/Baku)
>
>   * (GMT+04:00) Gulf Standard Time (Asia/Dubai)
>
>   * (GMT+04:00) Gulf Standard Time (Asia/Muscat)
>
>   * (GMT+04:00) Georgia Standard Time (Asia/Tbilisi)
>
>   * (GMT+04:00) Armenia Standard Time (Asia/Yerevan)
>
>   * (GMT+04:00) Samara Standard Time (Europe/Astrakhan)
>
>   * (GMT+04:00) Samara Standard Time (Europe/Samara)
>
>   * (GMT+04:00) Moscow Standard Time + 1 (Europe/Saratov)
>
>   * (GMT+04:00) Moscow Standard Time + 1 (Europe/Ulyanovsk)
>
>   * (GMT+04:00) Seychelles Time (Indian/Mahe)
>
>   * (GMT+04:00) Mauritius Standard Time (Indian/Mauritius)
>
>   * (GMT+04:00) Réunion Time (Indian/Reunion)
>
>   * (GMT+03:30) Iran Standard Time (Asia/Tehran)
>
>   * (GMT+04:30) Iran Daylight Time (Asia/Tehran)
>
>   * (GMT+03:00) East Africa Time (Africa/Addis\_Ababa)
>
>   * (GMT+03:00) East Africa Time (Africa/Asmera)
>
>   * (GMT+03:00) East Africa Time (Africa/Dar\_es\_Salaam)
>
>   * (GMT+03:00) East Africa Time (Africa/Djibouti)
>
>   * (GMT+03:00) East Africa Time (Africa/Kampala)
>
>   * (GMT+03:00) East Africa Time (Africa/Mogadishu)
>
>   * (GMT+03:00) East Africa Time (Africa/Nairobi)
>
>   * (GMT+03:00) Syowa Time (Antarctica/Syowa)
>
>   * (GMT+03:00) Arabian Standard Time (Asia/Aden)
>
>   * (GMT+03:00) Arabian Standard Time (Asia/Baghdad)
>
>   * (GMT+03:00) Arabian Standard Time (Asia/Bahrain)
>
>   * (GMT+03:00) Arabian Standard Time (Asia/Kuwait)
>
>   * (GMT+03:00) Arabian Standard Time (Asia/Qatar)
>
>   * (GMT+03:00) Arabian Standard Time (Asia/Riyadh)
>
>   * (GMT+03:00) Eastern European Standard Time (Europe/Istanbul)
>
>   * (GMT+03:00) Moscow Standard Time (Europe/Kirov)
>
>   * (GMT+03:00) Moscow Standard Time (Europe/Minsk)
>
>   * (GMT+03:00) Moscow Standard Time (Europe/Moscow)
>
>   * (GMT+03:00) Moscow Standard Time (Europe/Simferopol)
>
>   * (GMT+03:00) Volgograd Standard Time (Europe/Volgograd)
>
>   * (GMT+03:00) East Africa Time (Indian/Antananarivo)
>
>   * (GMT+03:00) East Africa Time (Indian/Comoro)
>
>   * (GMT+03:00) East Africa Time (Indian/Mayotte)
>
>   * (GMT+02:00) Central Africa Time (Africa/Blantyre)
>
>   * (GMT+02:00) Central Africa Time (Africa/Bujumbura)
>
>   * (GMT+02:00) Eastern European Standard Time (Africa/Cairo)
>
>   * (GMT+02:00) Central Africa Time (Africa/Gaborone)
>
>   * (GMT+02:00) Central Africa Time (Africa/Harare)
>
>   * (GMT+02:00) South Africa Standard Time (Africa/Johannesburg)
>
>   * (GMT+02:00) Central Africa Time (Africa/Juba)
>
>   * (GMT+02:00) Central Africa Time (Africa/Khartoum)
>
>   * (GMT+02:00) Central Africa Time (Africa/Kigali)
>
>   * (GMT+02:00) Central Africa Time (Africa/Lubumbashi)
>
>   * (GMT+02:00) Central Africa Time (Africa/Lusaka)
>
>   * (GMT+02:00) Central Africa Time (Africa/Maputo)
>
>   * (GMT+02:00) South Africa Standard Time (Africa/Maseru)
>
>   * (GMT+02:00) South Africa Standard Time (Africa/Mbabane)
>
>   * (GMT+02:00) Eastern European Standard Time (Africa/Tripoli)
>
>   * (GMT+02:00) Central Africa Time (Africa/Windhoek)
>
>   * (GMT+02:00) Eastern European Standard Time (Asia/Amman)
>
>   * (GMT+03:00) Eastern European Summer Time (Asia/Amman)
>
>   * (GMT+02:00) Eastern European Standard Time (Asia/Beirut)
>
>   * (GMT+03:00) Eastern European Summer Time (Asia/Beirut)
>
>   * (GMT+02:00) Eastern European Standard Time (Asia/Damascus)
>
>   * (GMT+03:00) Eastern European Summer Time (Asia/Damascus)
>
>   * (GMT+02:00) Eastern European Standard Time (Asia/Famagusta)
>
>   * (GMT+03:00) Eastern European Summer Time (Asia/Famagusta)
>
>   * (GMT+02:00) Eastern European Standard Time (Asia/Gaza)
>
>   * (GMT+03:00) Eastern European Summer Time (Asia/Gaza)
>
>   * (GMT+02:00) Eastern European Standard Time (Asia/Hebron)
>
>   * (GMT+03:00) Eastern European Summer Time (Asia/Hebron)
>
>   * (GMT+02:00) Israel Standard Time (Asia/Jerusalem)
>
>   * (GMT+03:00) Israel Daylight Time (Asia/Jerusalem)
>
>   * (GMT+02:00) Eastern European Standard Time (Asia/Nicosia)
>
>   * (GMT+03:00) Eastern European Summer Time (Asia/Nicosia)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Athens)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Athens)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Bucharest)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Bucharest)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Chisinau)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Chisinau)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Helsinki)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Helsinki)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Kaliningrad)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Kiev)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Kiev)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Mariehamn)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Mariehamn)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Riga)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Riga)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Sofia)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Sofia)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Tallinn)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Tallinn)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Uzhgorod)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Uzhgorod)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Vilnius)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Vilnius)
>
>   * (GMT+02:00) Eastern European Standard Time (Europe/Zaporozhye)
>
>   * (GMT+03:00) Eastern European Summer Time (Europe/Zaporozhye)
>
>   * (GMT+01:00) Central European Standard Time (Africa/Algiers)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Bangui)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Brazzaville)
>
>   * (GMT+01:00) Central European Standard Time (Africa/Ceuta)
>
>   * (GMT+02:00) Central European Summer Time (Africa/Ceuta)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Douala)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Kinshasa)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Lagos)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Libreville)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Luanda)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Malabo)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Ndjamena)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Niamey)
>
>   * (GMT+01:00) West Africa Standard Time (Africa/Porto-Novo)
>
>   * (GMT+01:00) Central European Standard Time (Africa/Tunis)
>
>   * (GMT+01:00) Central European Standard Time (Arctic/Longyearbyen)
>
>   * (GMT+02:00) Central European Summer Time (Arctic/Longyearbyen)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Amsterdam)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Amsterdam)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Andorra)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Andorra)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Belgrade)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Belgrade)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Berlin)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Berlin)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Bratislava)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Bratislava)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Brussels)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Brussels)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Budapest)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Budapest)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Busingen)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Busingen)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Copenhagen)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Copenhagen)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Gibraltar)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Gibraltar)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Ljubljana)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Ljubljana)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Luxembourg)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Luxembourg)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Madrid)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Madrid)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Malta)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Malta)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Monaco)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Monaco)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Oslo)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Oslo)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Paris)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Paris)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Podgorica)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Podgorica)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Prague)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Prague)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Rome)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Rome)
>
>   * (GMT+01:00) Central European Standard Time (Europe/San\_Marino)
>
>   * (GMT+02:00) Central European Summer Time (Europe/San\_Marino)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Sarajevo)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Sarajevo)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Skopje)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Skopje)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Stockholm)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Stockholm)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Tirane)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Tirane)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Vaduz)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Vaduz)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Vatican)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Vatican)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Vienna)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Vienna)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Warsaw)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Warsaw)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Zagreb)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Zagreb)
>
>   * (GMT+01:00) Central European Standard Time (Europe/Zurich)
>
>   * (GMT+02:00) Central European Summer Time (Europe/Zurich)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Abidjan)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Accra)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Bamako)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Banjul)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Bissau)
>
>   * (GMT+00:00) Western European Standard Time (Africa/Casablanca)
>
>   * (GMT+01:00) Western European Summer Time (Africa/Casablanca)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Conakry)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Dakar)
>
>   * (GMT+00:00) Western European Standard Time (Africa/El\_Aaiun)
>
>   * (GMT+01:00) Western European Summer Time (Africa/El\_Aaiun)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Freetown)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Lome)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Monrovia)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Nouakchott)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Ouagadougou)
>
>   * (GMT+00:00) Greenwich Mean Time (Africa/Sao\_Tome)
>
>   * (GMT+00:00) Greenwich Mean Time (America/Danmarkshavn)
>
>   * (GMT+00:00) Greenwich Mean Time (Antarctica/Troll)
>
>   * (GMT+02:00) Central European Summer Time (Antarctica/Troll)
>
>   * (GMT+00:00) Western European Standard Time (Atlantic/Canary)
>
>   * (GMT+01:00) Western European Summer Time (Atlantic/Canary)
>
>   * (GMT+00:00) Western European Standard Time (Atlantic/Faeroe)
>
>   * (GMT+01:00) Western European Summer Time (Atlantic/Faeroe)
>
>   * (GMT+00:00) Western European Standard Time (Atlantic/Madeira)
>
>   * (GMT+01:00) Western European Summer Time (Atlantic/Madeira)
>
>   * (GMT+00:00) Greenwich Mean Time (Atlantic/Reykjavik)
>
>   * (GMT+00:00) Greenwich Mean Time (Atlantic/St\_Helena)
>
>   * (GMT+00:00) Greenwich Mean Time (Europe/Dublin)
>
>   * (GMT+01:00) Irish Standard Time (Europe/Dublin)
>
>   * (GMT+00:00) Greenwich Mean Time (Europe/Guernsey)
>
>   * (GMT+01:00) British Summer Time (Europe/Guernsey)
>
>   * (GMT+00:00) Greenwich Mean Time (Europe/Isle\_of\_Man)
>
>   * (GMT+01:00) British Summer Time (Europe/Isle\_of\_Man)
>
>   * (GMT+00:00) Greenwich Mean Time (Europe/Jersey)
>
>   * (GMT+01:00) British Summer Time (Europe/Jersey)
>
>   * (GMT+00:00) Western European Standard Time (Europe/Lisbon)
>
>   * (GMT+01:00) Western European Summer Time (Europe/Lisbon)
>
>   * (GMT+00:00) Greenwich Mean Time (Europe/London)
>
>   * (GMT+01:00) British Summer Time (Europe/London)
>
>   * (GMT+00:00) Greenwich Mean Time GMT)
>
>   * (GMT-01:00) East Greenland Standard Time (America/Scoresbysund)
>
>   * (GMT+00:00) East Greenland Summer Time (America/Scoresbysund)
>
>   * (GMT-01:00) Azores Standard Time (Atlantic/Azores)
>
>   * (GMT+00:00) Azores Summer Time (Atlantic/Azores)
>
>   * (GMT-01:00) Cape Verde Standard Time (Atlantic/Cape\_Verde)
>
>   * (GMT-02:00) Fernando de Noronha Standard Time (America/Noronha)
>
>   * (GMT-02:00) South Georgia Time (Atlantic/South\_Georgia)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Araguaina)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/Buenos\_Aires)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/La\_Rioja)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/Rio\_Gallegos)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/Salta)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/San\_Juan)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/San\_Luis)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/Tucuman)
>
>   * (GMT-03:00) Argentina Standard Time (America/Argentina/Ushuaia)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Bahia)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Belem)
>
>   * (GMT-03:00) Argentina Standard Time (America/Catamarca)
>
>   * (GMT-03:00) French Guiana Time (America/Cayenne)
>
>   * (GMT-03:00) Argentina Standard Time (America/Cordoba)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Fortaleza)
>
>   * (GMT-03:00) West Greenland Standard Time (America/Godthab)
>
>   * (GMT-02:00) West Greenland Summer Time (America/Godthab)
>
>   * (GMT-03:00) Argentina Standard Time (America/Jujuy)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Maceio)
>
>   * (GMT-03:00) Argentina Standard Time (America/Mendoza)
>
>   * (GMT-03:00) St. Pierre & Miquelon Standard Time (America/Miquelon)
>
>   * (GMT-02:00) St. Pierre & Miquelon Daylight Time (America/Miquelon)
>
>   * (GMT-03:00) Uruguay Standard Time (America/Montevideo)
>
>   * (GMT-03:00) Suriname Time (America/Paramaribo)
>
>   * (GMT-03:00) Chile Standard Time (America/Punta\_Arenas)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Recife)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Santarem)
>
>   * (GMT-03:00) Brasilia Standard Time (America/Sao\_Paulo)
>
>   * (GMT-03:00) Chile Standard Time (Antarctica/Palmer)
>
>   * (GMT-03:00) Rothera Time (Antarctica/Rothera)
>
>   * (GMT-03:00) Falkland Islands Standard Time (Atlantic/Stanley)
>
>   * (GMT-03:30) Newfoundland Standard Time (America/St\_Johns)
>
>   * (GMT-02:30) Newfoundland Daylight Time (America/St\_Johns)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Anguilla)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Antigua)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Aruba)
>
>   * (GMT-04:00) Paraguay Standard Time (America/Asuncion)
>
>   * (GMT-03:00) Paraguay Summer Time (America/Asuncion)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Barbados)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Blanc-Sablon)
>
>   * (GMT-04:00) Amazon Standard Time (America/Boa\_Vista)
>
>   * (GMT-04:00) Amazon Standard Time (America/Campo\_Grande)
>
>   * (GMT-04:00) Venezuela Time (America/Caracas)
>
>   * (GMT-04:00) Amazon Standard Time (America/Cuiaba)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Curacao)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Dominica)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Glace\_Bay)
>
>   * (GMT-03:00) Atlantic Daylight Time (America/Glace\_Bay)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Goose\_Bay)
>
>   * (GMT-03:00) Atlantic Daylight Time (America/Goose\_Bay)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Grenada)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Guadeloupe)
>
>   * (GMT-04:00) Guyana Time (America/Guyana)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Halifax)
>
>   * (GMT-03:00) Atlantic Daylight Time (America/Halifax)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Kralendijk)
>
>   * (GMT-04:00) Bolivia Time (America/La\_Paz)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Lower\_Princes)
>
>   * (GMT-04:00) Amazon Standard Time (America/Manaus)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Marigot)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Martinique)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Moncton)
>
>   * (GMT-03:00) Atlantic Daylight Time (America/Moncton)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Montserrat)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Port\_of\_Spain)
>
>   * (GMT-04:00) Amazon Standard Time (America/Porto\_Velho)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Puerto\_Rico)
>
>   * (GMT-04:00) Chile Standard Time (America/Santiago)
>
>   * (GMT-03:00) Chile Summer Time (America/Santiago)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Santo\_Domingo)
>
>   * (GMT-04:00) Atlantic Standard Time (America/St\_Barthelemy)
>
>   * (GMT-04:00) Atlantic Standard Time (America/St\_Kitts)
>
>   * (GMT-04:00) Atlantic Standard Time (America/St\_Lucia)
>
>   * (GMT-04:00) Atlantic Standard Time (America/St\_Thomas)
>
>   * (GMT-04:00) Atlantic Standard Time (America/St\_Vincent)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Thule)
>
>   * (GMT-03:00) Atlantic Daylight Time (America/Thule)
>
>   * (GMT-04:00) Atlantic Standard Time (America/Tortola)
>
>   * (GMT-04:00) Atlantic Standard Time (Atlantic/Bermuda)
>
>   * (GMT-03:00) Atlantic Daylight Time (Atlantic/Bermuda)
>
>   * (GMT-05:00) Colombia Standard Time (America/Bogota)
>
>   * (GMT-05:00) Eastern Standard Time (America/Cancun)
>
>   * (GMT-05:00) Eastern Standard Time (America/Cayman)
>
>   * (GMT-05:00) Eastern Standard Time (America/Coral\_Harbour)
>
>   * (GMT-05:00) Eastern Standard Time (America/Detroit)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Detroit)
>
>   * (GMT-05:00) Acre Standard Time (America/Eirunepe)
>
>   * (GMT-05:00) Eastern Standard Time (America/Grand\_Turk)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Grand\_Turk)
>
>   * (GMT-05:00) Ecuador Time (America/Guayaquil)
>
>   * (GMT-05:00) Cuba Standard Time (America/Havana)
>
>   * (GMT-04:00) Cuba Daylight Time (America/Havana)
>
>   * (GMT-05:00) Eastern Standard Time (America/Indiana/Indianapolis)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Indiana/Indianapolis)
>
>   * (GMT-05:00) Eastern Standard Time (America/Indiana/Marengo)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Indiana/Marengo)
>
>   * (GMT-05:00) Eastern Standard Time (America/Indiana/Petersburg)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Indiana/Petersburg)
>
>   * (GMT-05:00) Eastern Standard Time (America/Indiana/Vevay)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Indiana/Vevay)
>
>   * (GMT-05:00) Eastern Standard Time (America/Indiana/Vincennes)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Indiana/Vincennes)
>
>   * (GMT-05:00) Eastern Standard Time (America/Indiana/Winamac)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Indiana/Winamac)
>
>   * (GMT-05:00) Eastern Standard Time (America/Iqaluit)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Iqaluit)
>
>   * (GMT-05:00) Eastern Standard Time (America/Jamaica)
>
>   * (GMT-05:00) Eastern Standard Time (America/Kentucky/Monticello)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Kentucky/Monticello)
>
>   * (GMT-05:00) Peru Standard Time (America/Lima)
>
>   * (GMT-05:00) Eastern Standard Time (America/Louisville)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Louisville)
>
>   * (GMT-05:00) Eastern Standard Time (America/Montreal)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Montreal)
>
>   * (GMT-05:00) Eastern Standard Time (America/Nassau)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Nassau)
>
>   * (GMT-05:00) Eastern Standard Time (America/New\_York) (Default)
>
>   * (GMT-04:00) Eastern Daylight Time (America/New\_York) (Default)
>
>   * (GMT-05:00) Eastern Standard Time (America/Nipigon)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Nipigon)
>
>   * (GMT-05:00) Eastern Standard Time (America/Panama)
>
>   * (GMT-05:00) Eastern Standard Time (America/Pangnirtung)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Pangnirtung)
>
>   * (GMT-05:00) Eastern Standard Time (America/Port-au-Prince)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Port-au-Prince)
>
>   * (GMT-05:00) Acre Standard Time (America/Rio\_Branco)
>
>   * (GMT-05:00) Eastern Standard Time (America/Thunder\_Bay)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Thunder\_Bay)
>
>   * (GMT-05:00) Eastern Standard Time (America/Toronto)
>
>   * (GMT-04:00) Eastern Daylight Time (America/Toronto)
>
>   * (GMT-06:00) Central Standard Time (America/Bahia\_Banderas)
>
>   * (GMT-05:00) Central Daylight Time (America/Bahia\_Banderas)
>
>   * (GMT-06:00) Central Standard Time (America/Belize)
>
>   * (GMT-06:00) Central Standard Time (America/Chicago)
>
>   * (GMT-05:00) Central Daylight Time (America/Chicago)
>
>   * (GMT-06:00) Central Standard Time (America/Costa\_Rica)
>
>   * (GMT-06:00) Central Standard Time (America/El\_Salvador)
>
>   * (GMT-06:00) Central Standard Time (America/Guatemala)
>
>   * (GMT-06:00) Central Standard Time (America/Indiana/Knox)
>
>   * (GMT-05:00) Central Daylight Time (America/Indiana/Knox)
>
>   * (GMT-06:00) Central Standard Time (America/Indiana/Tell\_City)
>
>   * (GMT-05:00) Central Daylight Time (America/Indiana/Tell\_City)
>
>   * (GMT-06:00) Central Standard Time (America/Managua)
>
>   * (GMT-06:00) Central Standard Time (America/Matamoros)
>
>   * (GMT-05:00) Central Daylight Time (America/Matamoros)
>
>   * (GMT-06:00) Central Standard Time (America/Menominee)
>
>   * (GMT-05:00) Central Daylight Time (America/Menominee)
>
>   * (GMT-06:00) Central Standard Time (America/Merida)
>
>   * (GMT-05:00) Central Daylight Time (America/Merida)
>
>   * (GMT-06:00) Central Standard Time (America/Mexico\_City)
>
>   * (GMT-05:00) Central Daylight Time (America/Mexico\_City)
>
>   * (GMT-06:00) Central Standard Time (America/Monterrey)
>
>   * (GMT-05:00) Central Daylight Time (America/Monterrey)
>
>   * (GMT-06:00) Central Standard Time (America/North\_Dakota/Beulah)
>
>   * (GMT-05:00) Central Daylight Time (America/North\_Dakota/Beulah)
>
>   * (GMT-06:00) Central Standard Time (America/North\_Dakota/Center)
>
>   * (GMT-05:00) Central Daylight Time (America/North\_Dakota/Center)
>
>   * (GMT-06:00) Central Standard Time (America/North\_Dakota/New\_Salem)
>
>   * (GMT-05:00) Central Daylight Time (America/North\_Dakota/New\_Salem)
>
>   * (GMT-06:00) Central Standard Time (America/Rainy\_River)
>
>   * (GMT-05:00) Central Daylight Time (America/Rainy\_River)
>
>   * (GMT-06:00) Central Standard Time (America/Rankin\_Inlet)
>
>   * (GMT-05:00) Central Daylight Time (America/Rankin\_Inlet)
>
>   * (GMT-06:00) Central Standard Time (America/Regina)
>
>   * (GMT-06:00) Central Standard Time (America/Resolute)
>
>   * (GMT-05:00) Central Daylight Time (America/Resolute)
>
>   * (GMT-06:00) Central Standard Time (America/Swift\_Current)
>
>   * (GMT-06:00) Central Standard Time (America/Tegucigalpa)
>
>   * (GMT-06:00) Central Standard Time (America/Winnipeg)
>
>   * (GMT-05:00) Central Daylight Time (America/Winnipeg)
>
>   * (GMT-06:00) Easter Island Standard Time (Pacific/Easter)
>
>   * (GMT-05:00) Easter Island Summer Time (Pacific/Easter)
>
>   * (GMT-06:00) Galapagos Time (Pacific/Galapagos)
>
>   * (GMT-07:00) Mountain Standard Time (America/Boise)
>
>   * (GMT-06:00) Mountain Daylight Time (America/Boise)
>
>   * (GMT-07:00) Mountain Standard Time (America/Cambridge\_Bay)
>
>   * (GMT-06:00) Mountain Daylight Time (America/Cambridge\_Bay)
>
>   * (GMT-07:00) Mexican Pacific Standard Time (America/Chihuahua)
>
>   * (GMT-06:00) Mexican Pacific Daylight Time (America/Chihuahua)
>
>   * (GMT-07:00) Mountain Standard Time (America/Creston)
>
>   * (GMT-07:00) Mountain Standard Time (America/Dawson)
>
>   * (GMT-07:00) Mountain Standard Time (America/Dawson\_Creek)
>
>   * (GMT-07:00) Mountain Standard Time (America/Denver)
>
>   * (GMT-06:00) Mountain Daylight Time (America/Denver)
>
>   * (GMT-07:00) Mountain Standard Time (America/Edmonton)
>
>   * (GMT-06:00) Mountain Daylight Time (America/Edmonton)
>
>   * (GMT-07:00) Mountain Standard Time (America/Fort\_Nelson)
>
>   * (GMT-07:00) Mexican Pacific Standard Time (America/Hermosillo)
>
>   * (GMT-07:00) Mountain Standard Time (America/Inuvik)
>
>   * (GMT-06:00) Mountain Daylight Time (America/Inuvik)
>
>   * (GMT-07:00) Mexican Pacific Standard Time (America/Mazatlan)
>
>   * (GMT-06:00) Mexican Pacific Daylight Time (America/Mazatlan)
>
>   * (GMT-07:00) Mountain Standard Time (America/Ojinaga)
>
>   * (GMT-06:00) Mountain Daylight Time (America/Ojinaga)
>
>   * (GMT-07:00) Mountain Standard Time (America/Phoenix)
>
>   * (GMT-07:00) Mountain Standard Time (America/Whitehorse)
>
>   * (GMT-07:00) Mountain Standard Time (America/Yellowknife)
>
>   * (GMT-06:00) Mountain Daylight Time (America/Yellowknife)
>
>   * (GMT-08:00) Pacific Standard Time (America/Los\_Angeles)
>
>   * (GMT-07:00) Pacific Daylight Time (America/Los\_Angeles)
>
>   * (GMT-08:00) Northwest Mexico Standard Time (America/Santa\_Isabel)
>
>   * (GMT-07:00) Northwest Mexico Daylight Time (America/Santa\_Isabel)
>
>   * (GMT-08:00) Pacific Standard Time (America/Tijuana)
>
>   * (GMT-07:00) Pacific Daylight Time (America/Tijuana)
>
>   * (GMT-08:00) Pacific Standard Time (America/Vancouver)
>
>   * (GMT-07:00) Pacific Daylight Time (America/Vancouver)
>
>   * (GMT-08:00) Pitcairn Time (Pacific/Pitcairn)
>
>   * (GMT-09:00) Alaska Standard Time (America/Anchorage)
>
>   * (GMT-08:00) Alaska Daylight Time (America/Anchorage)
>
>   * (GMT-09:00) Alaska Standard Time (America/Juneau)
>
>   * (GMT-08:00) Alaska Daylight Time (America/Juneau)
>
>   * (GMT-09:00) Alaska Standard Time (America/Metlakatla)
>
>   * (GMT-08:00) Alaska Daylight Time (America/Metlakatla)
>
>   * (GMT-09:00) Alaska Standard Time (America/Nome)
>
>   * (GMT-08:00) Alaska Daylight Time (America/Nome)
>
>   * (GMT-09:00) Alaska Standard Time (America/Sitka)
>
>   * (GMT-08:00) Alaska Daylight Time (America/Sitka)
>
>   * (GMT-09:00) Alaska Standard Time (America/Yakutat)
>
>   * (GMT-08:00) Alaska Daylight Time (America/Yakutat)
>
>   * (GMT-09:00) Gambier Time (Pacific/Gambier)
>
>   * (GMT-09:30) Marquesas Time (Pacific/Marquesas)
>
>   * (GMT-10:00) Hawaii-Aleutian Standard Time (America/Adak)
>
>   * (GMT-09:00) Hawaii-Aleutian Daylight Time (America/Adak)
>
>   * (GMT-10:00) Hawaii-Aleutian Standard Time (Pacific/Honolulu)
>
>   * (GMT-10:00) Hawaii-Aleutian Standard Time (Pacific/Johnston)
>
>   * (GMT-10:00) Cook Islands Standard Time (Pacific/Rarotonga)
>
>   * (GMT-10:00) Tahiti Time (Pacific/Tahiti)
>
>   * (GMT-11:00) Samoa Standard Time (Pacific/Midway)
>
>   * (GMT-11:00) Niue Time (Pacific/Niue)
>
>   * (GMT-11:00) Samoa Standard Time (Pacific/Pago\_Pago)
>
> - Locale dropDown required
>
>   The user's locale.
>
>   * Afrikaans (South Africa)
>
>   * Amharic (Ethiopia)
>
>   * Arabic (United Arab Emirates)
>
>   * Arabic (Bahrain)
>
>   * Arabic (Algeria)
>
>   * Arabic (Egypt)
>
>   * Arabic (Iraq)
>
>   * Arabic (Jordan)
>
>   * Arabic (Kuwait)
>
>   * Arabic (Lebanon)
>
>   * Arabic (Libya)
>
>   * Arabic (Morocco)
>
>   * Arabic (Oman)
>
>   * Arabic (Qatar)
>
>   * Arabic (Saudi Arabia)
>
>   * Arabic (Sudan)
>
>   * Arabic (Syria)
>
>   * Arabic (Tunisia)
>
>   * Arabic (Yemen)
>
>   * Azerbaijani (Azerbaijan)
>
>   * Belarusian (Belarus)
>
>   * Bulgarian (Bulgaria)
>
>   * Bangla (Bangladesh)
>
>   * Bangla (India)
>
>   * Bosnian (Bosnia & Herzegovina)
>
>   * Catalan (Spain)
>
>   * Catalan (Spain,Euro)
>
>   * Czech (Czechia)
>
>   * Welsh (United Kingdom)
>
>   * Danish (Denmark)
>
>   * German (Austria)
>
>   * German (Austria,Euro)
>
>   * German (Belgium)
>
>   * German (Switzerland)
>
>   * German (Germany)
>
>   * German (Germany,Euro)
>
>   * German (Luxembourg)
>
>   * German (Luxembourg,Euro)
>
>   * Dzongkha (Bhutan)
>
>   * Greek (Cyprus)
>
>   * Greek (Greece)
>
>   * English (United Arab Emirates)
>
>   * English (Antigua & Barbuda)
>
>   * English (Australia)
>
>   * English (Barbados)
>
>   * English (Belgium)
>
>   * English (Bermuda)
>
>   * English (Bahamas)
>
>   * English (Botswana)
>
>   * English (Belize)
>
>   * English (Canada)
>
>   * English (Cameroon)
>
>   * English (Cyprus)
>
>   * English (Germany)
>
>   * English (Eritrea)
>
>   * English (Fiji)
>
>   * English (Falkland Islands)
>
>   * English (United Kingdom)
>
>   * English (Ghana)
>
>   * English (Gibraltar)
>
>   * English (Gambia)
>
>   * English (Guyana)
>
>   * English (Hong Kong SAR China)
>
>   * English (Indonesia)
>
>   * English (Ireland)
>
>   * English (Ireland,Euro)
>
>   * English (Israel)
>
>   * English (India)
>
>   * English (Jamaica)
>
>   * English (Kenya)
>
>   * English (Cayman Islands)
>
>   * English (Liberia)
>
>   * English (Madagascar)
>
>   * English (Malta)
>
>   * English (Mauritius)
>
>   * English (Malawi)
>
>   * English (Malaysia)
>
>   * English (Namibia)
>
>   * English (Nigeria)
>
>   * English (Netherlands)
>
>   * English (New Zealand)
>
>   * English (Papua New Guinea)
>
>   * English (Philippines)
>
>   * English (Pakistan)
>
>   * English (Rwanda)
>
>   * English (Solomon Islands)
>
>   * English (Seychelles)
>
>   * English (Singapore)
>
>   * English (St. Helena)
>
>   * English (Sierra Leone)
>
>   * English (Sint Maarten)
>
>   * English (Eswatini)
>
>   * English (Tonga)
>
>   * English (Trinidad & Tobago)
>
>   * English (Tanzania)
>
>   * English (Uganda)
>
>   * English (United States) (Default)
>
>   * English (Vanuatu)
>
>   * English (Samoa)
>
>   * English (South Africa)
>
>   * Spanish (Argentina)
>
>   * Spanish (Bolivia)
>
>   * Spanish (Chile)
>
>   * Spanish (Colombia)
>
>   * Spanish (Costa Rica)
>
>   * Spanish (Cuba)
>
>   * Spanish (Dominican Republic)
>
>   * Spanish (Ecuador)
>
>   * Spanish (Spain)
>
>   * Spanish (Spain,Euro)
>
>   * Spanish (Guatemala)
>
>   * Spanish (Honduras)
>
>   * Spanish (Mexico)
>
>   * Spanish (Nicaragua)
>
>   * Spanish (Panama)
>
>   * Spanish (Peru)
>
>   * Spanish (Puerto Rico)
>
>   * Spanish (Paraguay)
>
>   * Spanish (El Salvador)
>
>   * Spanish (United States)
>
>   * Spanish (Uruguay)
>
>   * Spanish (Venezuela)
>
>   * Estonian (Estonia)
>
>   * Basque (Spain)
>
>   * Persian (Iran)
>
>   * Finnish (Finland)
>
>   * Finnish (Finland,Euro)
>
>   * French (Belgium)
>
>   * French (Canada)
>
>   * French (Switzerland)
>
>   * French (France)
>
>   * French (France,Euro)
>
>   * French (Guinea)
>
>   * French (Haiti)
>
>   * French (Comoros)
>
>   * French (Luxembourg)
>
>   * French (Morocco)
>
>   * French (Monaco)
>
>   * French (Mauritania)
>
>   * French (Wallis & Futuna)
>
>   * Irish (Ireland)
>
>   * Gujarati (India)
>
>   * Hawaiian (United States)
>
>   * Hindi (India)
>
>   * Hmong (United States)
>
>   * Croatian (Croatia)
>
>   * Haitian Creole (Haiti)
>
>   * Haitian Creole (United States)
>
>   * Hungarian (Hungary)
>
>   * Armenian (Armenia)
>
>   * Indonesian (Indonesia)
>
>   * Icelandic (Iceland)
>
>   * Italian (Switzerland)
>
>   * Italian (Italy)
>
>   * Hebrew (Israel)
>
>   * Japanese (Japan)
>
>   * Yiddish (United States)
>
>   * Georgian (Georgia)
>
>   * Kazakh (Kazakhstan)
>
>   * Kalaallisut (Greenland)
>
>   * Khmer (Cambodia)
>
>   * Kannada (India)
>
>   * Korean (North Korea)
>
>   * Korean (South Korea)
>
>   * Kyrgyz (Kyrgyzstan)
>
>   * Luxembourgish (Luxembourg)
>
>   * Lao (Laos)
>
>   * Lithuanian (Lithuania)
>
>   * Luba-Katanga (Congo - Kinshasa)
>
>   * Latvian (Latvia)
>
>   * Te reo (New Zealand)
>
>   * Macedonian (North Macedonia)
>
>   * Malayalam (India)
>
>   * Marathi (India)
>
>   * Malay (Brunei)
>
>   * Malay (Malaysia)
>
>   * Maltese (Malta)
>
>   * Burmese (Myanmar (Burma))
>
>   * Nepali (Nepal)
>
>   * Dutch (Aruba)
>
>   * Dutch (Belgium)
>
>   * Dutch (Netherlands)
>
>   * Dutch (Suriname)
>
>   * Norwegian (Norway)
>
>   * Punjabi (India)
>
>   * Polish (Poland)
>
>   * Pashto (Afghanistan)
>
>   * Portuguese (Angola)
>
>   * Portuguese (Brazil)
>
>   * Portuguese (Cape Verde)
>
>   * Portuguese (Mozambique)
>
>   * Portuguese (Portugal)
>
>   * Portuguese (São Tomé & Príncipe)
>
>   * Romansh (Switzerland)
>
>   * Rundi (Burundi)
>
>   * Romanian (Moldova)
>
>   * Romanian (Romania)
>
>   * Russian (Armenia)
>
>   * Russian (Belarus)
>
>   * Russian (Kyrgyzstan)
>
>   * Russian (Kazakhstan)
>
>   * Russian (Lithuania)
>
>   * Russian (Moldova)
>
>   * Russian (Poland)
>
>   * Russian (Russia)
>
>   * Russian (Ukraine)
>
>   * Serbian (Latin) (Bosnia and Herzegovina)
>
>   * Serbian (Latin) (Serbia)
>
>   * Montenegrin (Montenegro)
>
>   * Montenegrin (Montenegro, USD)
>
>   * Slovak (Slovakia)
>
>   * Slovenian (Slovenia)
>
>   * Samoan (United States)
>
>   * Samoan (Samoa)
>
>   * Somali (Djibouti)
>
>   * Somali (Somalia)
>
>   * Albanian (Albania)
>
>   * Serbian (Cyrillic) (Bosnia and Herzegovina)
>
>   * Serbian (Cyrillic) (Serbia)
>
>   * Serbian (Serbia)
>
>   * Swedish (Sweden)
>
>   * Swahili (Kenya)
>
>   * Tamil (India)
>
>   * Tamil (Sri Lanka)
>
>   * Telugu (India)
>
>   * Tajik (Tajikistan)
>
>   * Thai (Thailand)
>
>   * Tigrinya (Ethiopia)
>
>   * Tagalog (Philippines)
>
>   * Turkish (Turkey)
>
>   * Ukrainian (Ukraine)
>
>   * Urdu (Pakistan)
>
>   * Uzbek (LATN,UZ)
>
>   * Vietnamese (Vietnam)
>
>   * Xhosa (South Africa)
>
>   * Yoruba (Benin)
>
>   * Chinese (China)
>
>   * 中文（中国，拼音顺序）
>
>   * 中文（中国，笔画顺序）
>
>   * Chinese (Hong Kong SAR China)
>
>   * 中文 (中國香港特別行政區，筆劃順序)
>
>   * Chinese (Macao SAR China)
>
>   * Chinese (Malaysia)
>
>   * Chinese (Singapore)
>
>   * Chinese (Taiwan)
>
>   * 中文 (台灣，筆劃順序)
>
>   * Zulu (South Africa)
>
> - Language dropDown required
>
>   The user's language, such as French or Chinese (Traditional).
>
>   * Chinese (Simplified)
>
>   * Chinese (Traditional)
>
>   * Danish
>
>   * Dutch
>
>   * English (Default)
>
>   * Finnish
>
>   * French
>
>   * German
>
>   * Italian
>
>   * Japanese
>
>   * Korean
>
>   * Norwegian
>
>   * Portuguese (Brazil)
>
>   * Russian
>
>   * Spanish
>
>   * Spanish (Mexico)
>
>   * Swedish
>
>   * Thai
>
> - User Fields variableInputList
>
>   Add user fields and their values.
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * username string required
>
>       Username
>
>     * firstName string
>
>       First Name
>
>     * lastName string required
>
>       Last Name
>
>     * email string required
>
>       Email
>
>     * alias string required
>
>       Alias
>
>     * emailEncodingKey string required
>
>       Email Encoding
>
>     * profile string required
>
>       Profile
>
>     * profileId string
>
>       Profile ID
>
>     * timeZoneSidKey string required
>
>       Timezone
>
>     * localeSidKey string required
>
>       Locale
>
>     * languageLocaleKey string required
>
>       Language
>
>     * userFieldsCreate array
>
>       User Fields
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * success boolean
>
>     * errors array
>
>   * statusCode number
>
>   * headers object
>
>   * id string

### Read User

Get information about a user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   The unique ID of the user, such as "0058a00000LYDB8AAP".
>
> - Fields textFieldArrayView
>
>   Specifies which field values to get for the user. Leave this blank to get all fields.
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * userId string required
>
>       User ID
>
>     * userFieldsRead array
>
>       Fields
>
> - output object
>
>   * rawResponse object
>
>     * attributes object
>
>       * type string
>
>       * url string
>
>     * Id string
>
>     * Username string
>
>     * LastName string
>
>     * FirstName string
>
>     * Name string
>
>     * CompanyName string
>
>     * Division string
>
>     * Department string
>
>     * Title string
>
>     * Street string
>
>     * City string
>
>     * State string
>
>     * PostalCode string
>
>     * Country string
>
>     * Latitude number
>
>     * Longitude number
>
>     * GeocodeAccuracy string
>
>     * Address object
>
>       * city string
>
>       * country string
>
>       * geocodeAccuracy string
>
>       * latitude number
>
>       * longitude number
>
>       * postalCode string
>
>       * state string
>
>       * street string
>
>     * Email string
>
>     * EmailPreferencesAutoBcc boolean
>
>     * EmailPreferencesAutoBccStayInTouch boolean
>
>     * EmailPreferencesStayInTouchReminder boolean
>
>     * SenderEmail string
>
>     * SenderName string
>
>     * Signature string
>
>     * StayInTouchSubject string
>
>     * StayInTouchSignature string
>
>     * StayInTouchNote string
>
>     * Phone string
>
>     * Fax string
>
>     * MobilePhone string
>
>     * Alias string
>
>     * CommunityNickname string
>
>     * BadgeText string
>
>     * IsActive boolean
>
>     * TimeZoneSidKey string
>
>     * UserRoleId string
>
>     * LocaleSidKey string
>
>     * ReceivesInfoEmails boolean
>
>     * ReceivesAdminInfoEmails boolean
>
>     * EmailEncodingKey string
>
>     * ProfileId string
>
>     * UserType string
>
>     * LanguageLocaleKey string
>
>     * EmployeeNumber string
>
>     * DelegatedApproverId string
>
>     * ManagerId string
>
>     * LastLoginDate string
>
>     * LastPasswordChangeDate string
>
>     * CreatedDate string
>
>     * CreatedById string
>
>     * LastModifiedDate string
>
>     * LastModifiedById string
>
>     * SystemModstamp string
>
>     * NumberOfFailedLogins integer
>
>     * OfflineTrialExpirationDate string
>
>     * OfflinePdaTrialExpirationDate string
>
>     * UserPermissionsMarketingUser boolean
>
>     * UserPermissionsOfflineUser boolean
>
>     * UserPermissionsCallCenterAutoLogin boolean
>
>     * UserPermissionsSFContentUser boolean
>
>     * UserPermissionsKnowledgeUser boolean
>
>     * UserPermissionsInteractionUser boolean
>
>     * UserPermissionsSupportUser boolean
>
>     * UserPermissionsJigsawProspectingUser boolean
>
>     * UserPermissionsSiteforceContributorUser boolean
>
>     * UserPermissionsSiteforcePublisherUser boolean
>
>     * UserPermissionsWorkDotComUserFeature boolean
>
>     * ForecastEnabled boolean
>
>     * UserPreferencesActivityRemindersPopup boolean
>
>     * UserPreferencesEventRemindersCheckboxDefault boolean
>
>     * UserPreferencesTaskRemindersCheckboxDefault boolean
>
>     * UserPreferencesReminderSoundOff boolean
>
>     * UserPreferencesDisableAllFeedsEmail boolean
>
>     * UserPreferencesDisableFollowersEmail boolean
>
>     * UserPreferencesDisableProfilePostEmail boolean
>
>     * UserPreferencesDisableChangeCommentEmail boolean
>
>     * UserPreferencesDisableLaterCommentEmail boolean
>
>     * UserPreferencesDisProfPostCommentEmail boolean
>
>     * UserPreferencesContentNoEmail boolean
>
>     * UserPreferencesContentEmailAsAndWhen boolean
>
>     * UserPreferencesApexPagesDeveloperMode boolean
>
>     * UserPreferencesReceiveNoNotificationsAsApprover boolean
>
>     * UserPreferencesReceiveNotificationsAsDelegatedApprover boolean
>
>     * UserPreferencesHideCSNGetChatterMobileTask boolean
>
>     * UserPreferencesDisableMentionsPostEmail boolean
>
>     * UserPreferencesDisMentionsCommentEmail boolean
>
>     * UserPreferencesHideCSNDesktopTask boolean
>
>     * UserPreferencesHideChatterOnboardingSplash boolean
>
>     * UserPreferencesHideSecondChatterOnboardingSplash boolean
>
>     * UserPreferencesDisCommentAfterLikeEmail boolean
>
>     * UserPreferencesDisableLikeEmail boolean
>
>     * UserPreferencesSortFeedByComment boolean
>
>     * UserPreferencesDisableMessageEmail boolean
>
>     * UserPreferencesHideLegacyRetirementModal boolean
>
>     * UserPreferencesJigsawListUser boolean
>
>     * UserPreferencesDisableBookmarkEmail boolean
>
>     * UserPreferencesDisableSharePostEmail boolean
>
>     * UserPreferencesEnableAutoSubForFeeds boolean
>
>     * UserPreferencesDisableFileShareNotificationsForApi boolean
>
>     * UserPreferencesShowTitleToExternalUsers boolean
>
>     * UserPreferencesShowManagerToExternalUsers boolean
>
>     * UserPreferencesShowEmailToExternalUsers boolean
>
>     * UserPreferencesShowWorkPhoneToExternalUsers boolean
>
>     * UserPreferencesShowMobilePhoneToExternalUsers boolean
>
>     * UserPreferencesShowFaxToExternalUsers boolean
>
>     * UserPreferencesShowStreetAddressToExternalUsers boolean
>
>     * UserPreferencesShowCityToExternalUsers boolean
>
>     * UserPreferencesShowStateToExternalUsers boolean
>
>     * UserPreferencesShowPostalCodeToExternalUsers boolean
>
>     * UserPreferencesShowCountryToExternalUsers boolean
>
>     * UserPreferencesShowProfilePicToGuestUsers boolean
>
>     * UserPreferencesShowTitleToGuestUsers boolean
>
>     * UserPreferencesShowCityToGuestUsers boolean
>
>     * UserPreferencesShowStateToGuestUsers boolean
>
>     * UserPreferencesShowPostalCodeToGuestUsers boolean
>
>     * UserPreferencesShowCountryToGuestUsers boolean
>
>     * UserPreferencesShowForecastingChangeSignals boolean
>
>     * UserPreferencesHideS1BrowserUI boolean
>
>     * UserPreferencesDisableEndorsementEmail boolean
>
>     * UserPreferencesPathAssistantCollapsed boolean
>
>     * UserPreferencesCacheDiagnostics boolean
>
>     * UserPreferencesShowEmailToGuestUsers boolean
>
>     * UserPreferencesShowManagerToGuestUsers boolean
>
>     * UserPreferencesShowWorkPhoneToGuestUsers boolean
>
>     * UserPreferencesShowMobilePhoneToGuestUsers boolean
>
>     * UserPreferencesShowFaxToGuestUsers boolean
>
>     * UserPreferencesShowStreetAddressToGuestUsers boolean
>
>     * UserPreferencesLightningExperiencePreferred boolean
>
>     * UserPreferencesPreviewLightning boolean
>
>     * UserPreferencesHideEndUserOnboardingAssistantModal boolean
>
>     * UserPreferencesHideLightningMigrationModal boolean
>
>     * UserPreferencesHideSfxWelcomeMat boolean
>
>     * UserPreferencesHideBiggerPhotoCallout boolean
>
>     * UserPreferencesGlobalNavBarWTShown boolean
>
>     * UserPreferencesGlobalNavGridMenuWTShown boolean
>
>     * UserPreferencesCreateLEXAppsWTShown boolean
>
>     * UserPreferencesFavoritesWTShown boolean
>
>     * UserPreferencesRecordHomeSectionCollapseWTShown boolean
>
>     * UserPreferencesRecordHomeReservedWTShown boolean
>
>     * UserPreferencesFavoritesShowTopFavorites boolean
>
>     * UserPreferencesExcludeMailAppAttachments boolean
>
>     * UserPreferencesSuppressTaskSFXReminders boolean
>
>     * UserPreferencesSuppressEventSFXReminders boolean
>
>     * UserPreferencesPreviewCustomTheme boolean
>
>     * UserPreferencesHasCelebrationBadge boolean
>
>     * UserPreferencesUserDebugModePref boolean
>
>     * UserPreferencesSRHOverrideActivities boolean
>
>     * UserPreferencesNewLightningReportRunPageEnabled boolean
>
>     * UserPreferencesReverseOpenActivitiesView boolean
>
>     * UserPreferencesShowTerritoryTimeZoneShifts boolean
>
>     * UserPreferencesHasSentWarningEmail boolean
>
>     * UserPreferencesNativeEmailClient boolean
>
>     * ContactId string
>
>     * AccountId string
>
>     * CallCenterId string
>
>     * Extension string
>
>     * FederationIdentifier string
>
>     * AboutMe string
>
>     * FullPhotoUrl string
>
>     * SmallPhotoUrl string
>
>     * IsExtIndicatorVisible boolean
>
>     * OutOfOfficeMessage string
>
>     * MediumPhotoUrl string
>
>     * DigestFrequency string
>
>     * DefaultGroupNotificationFrequency string
>
>     * JigsawImportLimitOverride integer
>
>     * LastViewedDate string
>
>     * LastReferencedDate string
>
>     * BannerPhotoUrl string
>
>     * SmallBannerPhotoUrl string
>
>     * MediumBannerPhotoUrl string
>
>     * IsProfilePhotoActive boolean
>
>     * IndividualId string
>
>   * statusCode number
>
>   * headers object

### Update User

Update information for a user.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField required
>
>   The unique ID of the user, such as "0058a00000LYDB8AAP".
>
> - User Fields variableInputList
>
>   Add the user fields that you want to update and provide their values.
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * userId string required
>
>       User ID
>
>     * userFieldsUpdate array required
>
>       User Fields
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Read Record

Get information about a record.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Object Type textField required
>
>   The type of standard or custom object, such as "User", "Lead", or "Document".
>
> - Record ID textField required
>
>   The unique ID of the record, such as "0058a00000LYDB8AAP".
>
> - Fields textFieldArrayView
>
>   Specifies which field values to get for the record. Leave this blank to get all fields.
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * objectType string required
>
>       Object Type
>
>     * recordId string required
>
>       Record ID
>
>     * recordFieldsRead array
>
>       Fields
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Update Record

Update information in a record.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Object Type textField required
>
>   The type of standard or custom object, such as "User", "Lead", or "Document".
>
> - Record ID textField required
>
>   The unique ID of the record, such as "0058a00000LYDB8AAP".
>
> - Record Fields variableInputList
>
>   Add the record fields that you want to update and provide their values.
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * objectType string required
>
>       Object Type
>
>     * recordId string required
>
>       Record ID
>
>     * recordFieldsUpdate array required
>
>       Object Fields
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object

### Search Record

Query records using SOQL.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - SOQL Query textArea
>
>   Enter a query using Salesforce Object Query Language, such as "SELECT FirstName from User WHERE Id = '0058a00000Ky3eP'".
>
> - Next Records URL textField
>
>   If you expect more than 2000 results, connect multiple Search Record nodes in series. In each node, populate the Next Records URL field with the Next Records URL variable from the previous node.
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * query string
>
>       Query
>
>     * nextRecordsUrl string
>
>       Next Records URl
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object
>
>   * nextRecordsUrl string

### Upload Document

Upload a new document.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Name textField required
>
>   The name of the document.
>
> - File textField required
>
>   Base64-encoded file data.
>
> - Folder dropDown required
>
>   The folder that contains the document. Displays up to 100 results. If the folder you want is not listed, select Use Folder ID.
>
>   * Use Folder ID (Default)
>
> - Folder ID textField required
>
>   The ID of the folder that contains the document, such as "00l8a000002XKVQAA4".
>
> - Description textField
>
>   A text description of the document.
>
> - Keywords textFieldArrayView
>
>   Searchable keywords to associate with the document. Type a keyword and press Enter to add it.
>
> - Document Fields variableInputList
>
>   Add document fields and their values.
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * documentName string required
>
>       Document Name
>
>     * file string required
>
>       File
>
>     * documentFolder string required
>
>       Document Folder
>
>     * documentFolderId string
>
>       Document Folder ID
>
>     * documentDescription string
>
>       Document Description
>
>     * documentKeywords array
>
>       Document Keywords
>
>     * documentFields array
>
>       Document Fields
>
> - output object
>
>   * rawResponse object
>
>     * id string
>
>     * success boolean
>
>     * errors array
>
>   * statusCode number
>
>   * headers object
>
>   * id string

### Make Custom API Call

Define a custom API call to Salesforce.

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Endpoint textField required
>
>   The Salesforce API endpoint, such as "/services/data/v54.0/sobjects/User".
>
> - Method dropDown required
>
>   The HTTP Method.
>
>   * GET
>
>   * POST
>
>   * PUT
>
>   * DELETE
>
>   * PATCH
>
> - Query Parameters keyValueList
>
>   Add query parameters and provide their values.
>
> - Headers keyValueList
>
>   Add HTTP headers and provide their values.
>
> - Body codeEditor
>
>   The raw JSON body, such as "{ "Username": "<jsmith@example.com>", "ProfileId": "00e8a0000024zkjAAA" }".
>
> * default object
>
>   * properties object
>
>     * adminUsername string required
>
>       Username
>
>     * consumerKey string required
>
>       Consumer Key
>
>     * privateKey string required
>
>       Private Key
>
>     * domainName string required
>
>       Domain Name
>
>     * endpoint string required
>
>       Endpoint
>
>     * method string required
>
>       Method
>
>     * queryParameters array
>
>       Query Parameters
>
>     * headers array
>
>       Headers
>
>     * body object
>
>       Body
>
> - output object
>
>   * rawResponse object
>
>   * statusCode number
>
>   * headers object