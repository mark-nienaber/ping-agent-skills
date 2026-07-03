---
title: Daon Connector
description: The Daon connector lets you use Daon IdentityX for multi-factor authentication (MFA) in your PingOne DaVinci flow.
component: connectors
page_id: connectors::daon_connector
canonical_url: https://docs.pingidentity.com/connectors/daon_connector.html
llms_txt: https://docs.pingidentity.com/connectors/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: August 19, 2024
section_ids:
  setup: Setup
  resources: Resources
  requirement: Requirement
  configuring-the-daon-connector: Configuring the Daon connector
  connector-configuration: Connector configuration
  api-base-url: API Base URL
  admin-username: Admin Username
  admin-password: Admin Password
  using-the-connector-in-a-flow: Using the connector in a flow
  authenticating-users-with-results-via-webhook: Authenticating users with results via webhook
  authenticating-users-with-results-via-polling: Authenticating users with results via polling
  capabilities: Capabilities
  getUserByUsername: Get User by Username
  createAuthRequest: Create Authentication Request
  getAuthRequest: Get Authentication Request
  webhook: Webhook Handler
---

# Daon Connector

The Daon connector lets you use Daon IdentityX for multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* in your PingOne DaVinci flow.

The connector triggers authentication on a user's mobile device using an app that was built with the Daon mobile SDK. DaVinci can get the result of the authentication process by polling Daon or by listening for a webhook response.

## Setup

### Resources

Learn more in the following:

* DaVinci documentation:

  * [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html)

  * [Using connectors securely](https://docs.pingidentity.com/davinci/connectors/davinci_using_connectors_securely.html)

  * [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html)

### Requirement

To use the connector, you'll need:

* An existing integration between your mobile app and Daon IdentityX

* Your Daon access information, including:

  * Admin credentials

  * The URL for your IdentityX application programming interface (API) *(tooltip: \<div class="paragraph">
    \<p>A specification of interactions available for building software to access an application or service.\</p>
    \</div>)* service

### Configuring the Daon connector

Add the connector in DaVinci as shown in [Adding a connector](https://docs.pingidentity.com/davinci/connectors/davinci_adding_a_connector.html), then configure it as follows.

#### Connector configuration

##### API Base URL

The URL for your Daon IdentityX API. For example, `https://api.identityx-cloud.com/yourcompany/IdentityXServices/rest/v1`

##### Admin Username

The username for your Daon administrator account.

##### Admin Password

The password for your Daon administrator account.

## Using the connector in a flow

### Authenticating users with results via webhook

![A screen capture of the complete authentication flow.](_images/connector-images/dvc-daon-authentication-flow.png)

This flow asks the user to enter their username in an HTML form. The connector gets their Daon user ID and initiates the authentication process on the user's mobile device.

The user sees a "Check your device" message that stays on screen until as long as the flow challenge remains unresolved.

In a secondary branch, the connector listens for a transaction result that Daon sends using a webhook. When DaVinci receives the result, the flow challenge is updated and the waiting message changes to show the result of the authentication process.

1. Download the [Daon - Authentication with results via webhook](https://support.pingidentity.com/s/marketplace-integration/a7iDo0000010xT2IAI/daon-authentication-with-results-via-webhook) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. Configure the **Create Authentication Request** node by adding your Daon authentication policy in the **Policy URL** field.

3. Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

### Authenticating users with results via polling

![A screen capture of the complete authentication flow.](_images/connector-images/dvc-daon-authentication-flow-polling.png)

This flow asks the user to enter their username in an HTML form. The connector gets their Daon user ID and initiates the authentication process on the user's mobile device.

The user sees a "Check your device" message, and the flow begins polling Daon until the authentication result is available. When DaVinci gets the result, the flow updates the waiting message to show the result of the authentication process.

1. Download the [Daon - Authentication with results via webhook](https://support.pingidentity.com/s/marketplace-integration/a7iDo0000010xT2IAI/daon-authentication-with-results-via-webhook) flow template. Learn more in [Using DaVinci flow templates](https://docs.pingidentity.com/davinci/flows/davinci_using_davinci_flow_templates.html).

2. Configure the **Create Authentication Request** node by adding your Daon authentication policy in the **Policy URL** field.

3. Test the flow by clicking **Save**, **Deploy**, and **Try Flow**.

## Capabilities

### Get User by Username

Retrieve a user record with the user's login

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User Login textField
>
>   The userId of the user you want to retrieve. E.g. <user@example.com>
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * username string required
>
>     * password string required
>
>     * userLogin string required
>
> - output object
>
>   * rawResponse object
>
>   * userId string
>
> Output Example
>
> ```json
> {
>   "metadata": {
>     "limit": 1,
>     "page": 1,
>     "totalCount": 1
>   },
>   "paging": {
>     "first": null,
>     "previous": null,
>     "next": null,
>     "last": null
>   },
>   "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users?userId=akennedy%2Batu001%40pingidentity.com&status=ACTIVE&limit=1",
>   "items": [
>     {
>       "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w",
>       "id": "QTAzs3wrZYvmxdu0LQ13r8z75w",
>       "userId": "akennedy+atu001@pingidentity.com",
>       "created": "2022-04-26T14:35:04.399+0000",
>       "updated": "2022-04-26T14:35:04.399+0000",
>       "nextPossibleDirectOtpDtm": "2022-04-26T15:56:28.103+0000",
>       "pinEnrolled": false,
>       "faceEnrolled": false,
>       "voiceEnrolled": false,
>       "keystrokesEnrolled": false,
>       "failedVerificationCount": 0,
>       "accountUnlockedCount": 0,
>       "status": "ACTIVE",
>       "tenant": {
>         "href": "https://api.identityx-cloud.com/IdentityXServices/rest/v1/tenants/r4SWIoHpn0fmXw4pkQhAbw"
>       },
>       "applications": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/applications"
>       },
>       "registrations": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/registrations"
>       },
>       "authenticators": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/authenticators"
>       },
>       "authenticationRequests": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/authenticationRequests"
>       },
>       "sponsorships": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/sponsorships"
>       },
>       "registrationChallenges": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/registrationChallenges"
>       },
>       "enrollments": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/enrollments"
>       },
>       "samples": {
>         "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w/samples"
>       }
>     }
>   ]
> }
> ```

### Create Authentication Request

Create an authentication request on the Identity X server for a user

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - User ID textField
>
>   The ID of the user.
>
> - Authentication Description textField
>
>   A description of the authentication request - if using the IdentityX Authenticator, this will be provided to the user.
>
> - Authentication Type dropDown
>
>   Specifies the protocol type of the authentication request.
>
>   * Fido 1 (Default)
>
>   * Fido Offline
>
>   * IdX
>
>   * REST
>
>   * OTP
>
>   * Fido 2 W3C
>
> - Policy URL textField
>
>   The policy associated with the authentication request.
>
> - Push Notification Type dropDown
>
>   Provides operation instructions to the mobile application how to behave when a push notification is received.
>
>   * Refresh
>
>   * Verify Without Confirmation
>
>   * Verify With Confirmation (Default)
>
> - Secure Transaction Content Type dropDown
>
>   Describes the value of the secureTransactionContent and secureTextTransactionContent property.
>
>   * text/plain (Default)
>
>   * image/png
>
>   * text/plain;image/png
>
> - Secure Text Transaction Content textField
>
>   Text to be displayed securely to a user. The secureTransactionContentType property must be "text/plain" or "text/plain;image/png".
>
> - Secure Image Transaction Content textField
>
>   Image to be displayed securely to a user. The secureTransactionContentType property must be "image/png" or "text/plain;image/png".
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * username string required
>
>     * password string required
>
>     * userId string required
>
>     * description string required
>
>     * type string required
>
>     * pushNotificationType string required
>
>     * secureTextTransactionContent string
>
>     * secureTransactionContent string required
>
>     * secureTransactionContentType string required
>
>     * policyUrl string required
>
> - output object
>
>   * rawResponse object
>
>   * status string
>
>   * id string
>
> Output Example
>
> ```json
> {
>   "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzw8gbh6Z777TpHz3pkXErIw/authenticationRequests/QTAzAFVlolrfXPHCidlov4Yt6Q",
>   "id": "QTAzAFVlolrfXPHCidlov4Yt6Q",
>   "authenticationRequestId": "postman-27b76ffa-6c2f-4359-bdec-0f7a1199c86c",
>   "description": "FIDO - OOB Auth Request",
>   "expiration": "2022-04-25T12:42:31.141+0000",
>   "availableRetries": 5,
>   "totalRetriesAllowed": 5,
>   "oneTimePasswordEnabled": false,
>   "created": "2022-04-25T12:27:31.835+0000",
>   "type": "FI",
>   "fidoChallenge": "TuA-su0iHlpEWcdGR-xxZQ",
>   "secureTextTransactionContent": "secure transaction details from postman",
>   "secureTransactionContentType": "text/plain",
>   "fidoAuthenticationRequest": "[{\"header\":{\"upv\":{\"major\":1,\"minor\":0},\"op\":\"Auth\",\"appID\":\"https://example.com\",\"exts\":[{\"id\":\"com.daon.sdk.ados.decChain\",\"data\":\"[\\\"MIIE6TCCAtOgAwIBAgIRAJEmGK-0XEGFin4brMpnidIwCwYJKoZIhvcNAQELMEcxFTATBgNVBAMMDElkZW50aXR5WCBDQTENMAsGA1UECgwERGFvbjESMBAGA1UECwwJSWRlbnRpdHlYMQswCQYDVQQGEwJJRTAeFw0xNzA2MTUwOTQ3NTFaFw0xOTA2MTUwOTQ3NTFaMFoxDTALBgNVBAoMBERhb24xEjAQBgNVBAsMCUlkZW50aXR5WDELMAkGA1UEBhMCSUUxKDAmBgNVBAMMH0RFX0RBT05fQVVUSEVOVElDQVRJT05fREFUQV9LRUswggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCXrHT7hGCZR4KzlwawZl3yefpUov44BWofCNnuGh3RoaQ63vXX6jsrfoCVJdto5a38Nd7ckQzjhtuoAfLeUT3sbm7uhXCCoC5xJ_B96G6LeTvY6yZ2ZsO3K8dOl8epKOI7e2Xh_3WQg0xa21QmJxnTcMSMj0TMHrXlb66nh-CoTbAcKopm0xbrPfOMLoZ1xGk7iOVxSY_TRjep6tn4Z7t7r-bsJnDjJtctto4gYXk7mDkwdAMfBpoq1Jp0nGbv8TCMySAjOUSs9ptE7pRl5No6iF4QYNDDUUhI9q7MAcpSgEYLaAPzhZdzZnmDfwwOIPCiss0qKV9L3H6wh-NLQ_r7AgMBAAGjgcAwgb0wfgYDVR0jBHcwdYAUZplSSlDw67i7wEa-1wVzqzvdL5ahS6RJMEcxFTATBgNVBAMMDElkZW50aXR5WCBDQTENMAsGA1UECgwERGFvbjESMBAGA1UECwwJSWRlbnRpdHlYMQswCQYDVQQGEwJJRYIQKuhll9ePQGSsywpelEVwazAdBgNVHQ4EFgQUyeJ8CGmnhFk5Cs0c6TEEG2GrL08wDAYDVR0TAQH_BAIwADAOBgNVHQ8BAf8EBAMCBLAwCwYJKoZIhvcNAQELA4ICAQA-cpJUeOAz96VXYHqIS_yRkltsSkLvmgqwuwx2fShZJQ1pawaRf8qWH9takyyBzAPNVMYsxIc4eMF4qRhExtADB5EQBFF-DWVMoLymYOLMDHii9lnuYdsV0B82EsQu5U7SccuDH3ffNOlVJq2NS8jHUFm7GxF36O6BdojT3vXgHmH_dZo3GzGCRDpkKt_gUAO1aj2Ga1YmLcd2ptA6OA1SllW0eWS5yb_KNscCVVQke2gvJkACHrsIel7AxNBgukWlTANCrgH2UOhhhXlOmu3RRoxhUL8Ya5V7qSdiVZzmfMZwRpyX92FbGUIb_lL9nlFs3iGtE9gXE-DVTNs93jn_XIK0Q8D6lcvpVtI4bJQhUJ7u78MeoSPuYx-9SX4ioiNmVVYC6fdAieSG1ggEiIhw0U8l-4u1pItyPIqwt_OijaElOouTWzeBa3AJA7CqasOZoMx6BXJE5dLcILbpYduA0vSc3em6cr-LJgRr7uuvQCJ-3pGX_gipMyailXYd2S985PQXsyKEW5AegBcEgNX3MIvNPUhb2eS-Ab_JIZbQGAUGTT_HwQXFB08pMXJ-UK_FwdphXVGMJy9jmyvwWLlBFXyYGrAiq0pLlkHexCqHcjYbchgf1IDIwp0yQ3KcoA42w555djBN7hFHTa9dfAdTOHRKlICG_PhsMUdhZ_T7oQ==\\\"]\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.ados.dekId\",\"data\":\"1000090661\",\"fail_if_unknown\":false},{\"id\":\"com.daon.authRequest.retriesRemaining\",\"data\":\"5\",\"fail_if_unknown\":false},{\"id\":\"com.daon.authRequest.maxAttempts\",\"data\":\"5\",\"fail_if_unknown\":false},{\"id\":\"com.daon.user.retriesRemaining\",\"data\":\"10\",\"fail_if_unknown\":false},{\"id\":\"com.daon.user.maxAttempts\",\"data\":\"10\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.voice.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.voice.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.passcode.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.passcode.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.otp.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.otp.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.identityx.version\",\"data\":\"5.2.4.0\",\"fail_if_unknown\":false}]},\"challenge\":\"TuA-su0iHlpEWcdGR-xxZQ\",\"policy\":{\"accepted\":[[{\"aaid\":[\"D409#2601\"],\"keyIDs\":[\"RkE4NDhFQ0ItMjI5Ri00MkU2LUEzNkYtNUIzQjAzMTBCRkQw\"]}]]},\"transaction\":[{\"contentType\":\"text/plain\",\"content\":\"c2VjdXJlIHRyYW5zYWN0aW9uIGRldGFpbHMgZnJvbSBwb3N0bWFu\"},{\"tcDisplayPNGCharacteristics\":{\"width\":320,\"height\":240,\"bitDepth\":16,\"colorType\":2,\"compression\":0,\"filter\":0,\"interlace\":0},\"contentType\":\"image/png\",\"content\":\"iVBORw0KGgoAAAANSUhEUgAAAUAAAADwCAYAAABxLb1rAAA0QklEQVR4Xu2dCdgXVfXHrZASTDY3yAdQSQG1FE0UBaEC0cAtFSRks8VE0wxSQFv00VRScwEUQQUVE3eMREwCFXNJUxAEEVMDQ0RLSUta5v985u-83t-ZO8udd37bO-fzPOcpee_c-d2ZO9-Ze-6952zlKYqiFJSt5D8oiqIUBRVARVEKiwqgoiiFRQVQUZTCogKoKEphUQFUFKWwqAAqilJYVAAVRSksKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSwqgIqiFJZUAvjhhx96c-fO9X74wx96X__61719993X23XXXb3ddtvN23vvvb3evXt7w4cP9372s5958-fP99555x1ZhRObN2_27r__fu-0007zDj_8cK9Hjx7--fbbbz__v3_84x97v__9771___vf8tBGQTsfeughb_z48d43vvENr2fPnt7uu-_uffGLX_T2339_75vf_Kb305_-1HvkkUe8f_3rX_LwEI8__rj_OwN78803ZZFE_va3v5XUkabdK1euLCm_bNmykr__73__8_993Lhx_v3s1q2b16lTJ-9LX_qSd_7555eUjaNa90lR8iJWAD_44ANvwoQJ3uc__3lvq622Sm2f-cxnvK997WveK6-8IquMZdOmTb7Ifvaznw3VabPOnTt7t912m_9ANwbOe-6553otW7YMnSPKtt12W--UU06JbWO7du1KjrnhhhtkkUQQEHluRDGOb33rWyXlEfOARYsW-S8tWWdgCFcS1bpPipI3kQL4l7_8xdtjjz1CndnFHn74YVltJPfdd5_XqlWrUB1p7KijjvK_3rJw9913e9ttt12ozrR2zTXXyCobqDUBvPzyy71PfepTofpMGzBggKitlGrdJ0UpB1YB_Oc__-ntueeeoQ6M8dZnyMSwl-ETw8QuXbr4X32ybFoBvPbaa71Pf_rToeOxFi1a-EJ84IEH-v_bvHnzUBns4IMPdn64fvGLX0QKAv_eoUMH78tf_rI__GVo16xZs1C5ehHAm266KVRPYGa7-vfvL6troFr3SVHKhVUAL7roolDHPeSQQ7zf_va3kb4vRPOpp57yfWTBECuNAN57772hc_GQnXjiid6SJUu8LVu2lJTH78RwCtGVx33ve98rKRvHrFmzQsdj1ItQ_fWvf5WH-A8ufj18W_jMKF8PArjPPvuUDO-7du3qTZkyxVuzZo330Ucf-UPTt956y_vNb37jXXLJJbI6n2rdJ0UpJ1YBlF9_Rx99tPef__xHFouFiQIesDhef_11r02bNiXnQjSYiEgC_-SgQYNCD9fChQtl0RAvvvii_8Uij2VSQD7IUfz3v__1br_9dv-lEEWtCGDWNgZU6z4pSrkJCSAObtlZmVUsB_JB_dznPuc98cQTslgkfHUyc2nWweRLEviiZBtdZj_TUmsCOHbsWFk0FbK-St0nRSk3IQHk68jsqAxzyjF7xyTL1ltvXXIuhs-uMPySD_qKFStksQb4m_T79erVy_kLNw21JIAdO3b0v8ZcqdZ9UpRKEBLAVatWhTpqlvVrSbBm0DwHQ1L8RlnAx2XWddVVV8kiDTAElO1DZMpBLQngxRdfLIulolr3SVEqQUgA6dxytnP06NGyWKPp06dPyTlYZJyVM888s6SuE044QRZp4IADDigpi7-zXNSSACb5Y6Oo1n1SlEoQEkCQnR7j33D457Gqn5lH_Ehm_ZdeeqkslhqWZ5h18aVh4_333w8t1zn11FNlsdyoFQFs3bq1LJKKat0nRakUVgF88MEHQw9dYG3btvWGDBniL6N4_vnnM_nOXnrppVC9bKWbPHlyiV122WUNxoNnGss1Ahs6dGhJXV_4whfkKX2WL18eOu_MmTNlsdyoFQFkHWMWqnWfFKVSWAUQmBWVnd9m7AoYPHiw_3bfuHGjrMYKa-lkPXnaNttsI0_ps3jx4lBZ9i6Xi1oRwK9-9auySCqqdZ8UpVJECiDceuutXvv27UMdN8rwHfKWZyIljnnz5oWOzdMY5tqwLeZdunSpLJYbtSKA5l5gF6p1nxSlUsQKILB0YsaMGV6_fv0itzdJY7vc1KlTZVUN2IRo--2393baaadcLGpoZXugH330UVksN-pdAKt1nxSlUiQKoAliyPY2lkawkDUpesrs2bNlFT6IjizLcKvc2IZ0hHMqF3kIINFb5G-ulABW6z4pSqVwEkAJW6rY0vTtb3_burUMAWDmVcICWFn2lltukcVyx-bUx3dZLvhaMs81ffp0WSQR21dYpQSwWvdJUSpFowTQZN26dX4kEPnAzJkzRxb1gwrIWHJnnHGGLJY7CLYU6pNPPlkWy40gYEJgV1xxhSySyLRp00LXtFICWK37pCiVIjcBhNdeey0ULonFrzb69u1bUo5wU5WAobt53p133tk5OEBa5P7Xc845RxZJZMSIESV1YJUSQKjWfVKUSpCrAIKMNjxs2DBZxMcWcquc_rgAYgDK895xxx2yWC4cccQRJecZOHCgLBILQQR22GGH0O-tpABW6z4pSiXIXQAJIGo-LFE7LYg_J4ej3bt3z7Rh3wXWKrL-zDwvXzU2X2VjmTRpUsl52FXx3nvvyWKRXHnllSHxwSopgNW6T4pSCUIC-Oqrr3p___vf5T-ngqAJch8xOwWiIK-EfLjZa9qYIelzzz0n_ykESXzyPq8N246atJFU_vSnP4WEOrBKCiBU6z4pSrkJCSBLNUiC9KMf_ShxQbMJX1CsFZQPytq1a2XRBniQybgmjyE8lcvmfaJUMyxjxwNfWUmQtY7wUPK8hIMn-Gca1q9f75199tl-qPko2CYoF5KzlpK8GnGw55r9u_L3BVZpAazWfVKUcmMVQLOT48hnKMdDyySHGRIfHxVfKvjVWNQqH5CRI0d-UnEELLUgw5o8ll0Cxx9_vHfzzTd7q1ev9oeOxCX8xz_-4c84P_bYY344JXaemEmNmLVMwx_-8IdQnLvgeJb18KASC4_2EgCCoTNr4BiW8gAHkz1xIfGB_bDyHMQjPOmkk_wQ9LwgEFP2VbNMRk7SjBkzJnR8pQUQqnWfFKWcJAqgzRiaRQ3PAsMXmPSgBpBLxCagWczlwVqwYIFzyk9pSQKIeJIvVx6Xxs4666yq7gSRVOs-KUq5yCSASUbIeVc_4oYNG0KzplmMpO0uvPDCC6FAnS6WZiE1CZZcz0HipSCBufxbtQQQqnWfFKUchASQYS1DM2ZvbX6fKGNISJpMjm0MDE0RUBmHLs722msv3x_3zDPPyOpSQYIjdjjIdXtRxtCZYTDBIqKy5EkYGiJqSe3iy9lMNlRrAhhQjfukKHkTEkDJ22-_7Tvl8eMwJGNhLjOA-HRIb8i-YLZr8WWQJwgxmeXwLzILGZwXvyK7EUjyze-ypa9sDPj9brzxRm_ixIned77zHd-_haB8__vf92e0OWdjlswghHfddZcvhqNGjfLrx8-Hr7AehaFa90lR8iBRABVFUZoqKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKAywAZ81jYFnSHCi1gwqgojggA-ruueeesohSR6gAKooDKoBNi0gBnDlzpr-HNDC2wSlKPZJnX1YBbFpECiABUc0bvf_--8siilIX5NmXVQCbFiqASpMnz75M0AqCwAZGhBulflEBVJo82peVKFQAlSaP9mUlChVApcmjfVmJQgVQafJoX1aiKBHAZcuW-SHYsRNPPLGk0-yxxx4Nf4uyF1980ayugZUrV5aU4zwmQe6LcePG-WH1u3Xr5nXq1MkPUX_--eeXlJUQzv7ZZ5_1I1YTobpv375-_o3OnTv79RxyyCHeCSec4Gdza0wu2qQ2ABnQCPl-2GGH-ekEdt99d--ggw7yM8CRNS0plH0SH374oTd37lw_8jLXibwaJHXfbbfdvL333tvr3bu3N3z4cD9K9_z58_30n65U6nrGQTtJCzB-_Hh_2UrPnj39a8k1RbyIOE1-ZSJRR6UkKFdfJm2qWY5EUVngOrOr5Cc_-Yk3aNAg78ADD_TvI9eazIBkJrzzzjudc-uY1EKfrXVKBJDOZnYUV6Nj2ojLUbFo0SL_4ZV1BXb44YcbNf0_ZFoj9wgPe1z-XJsdfPDBfsJyV-LaQEpLOo08l7R27dp5U6ZMMWpNxwcffOBNmDDBOYMds5Q8TK-88oqssoRqXE8bmzZt8s4991yvZcuWofNEGak6TznllFAby9WX81gGw0sMoZHntBnZ83gRZBHCavbZeqGqAki-CHLkynpMGzBggKjN83MRy3KuxtcmicvTEtWGO-64w--ksv44O_PMM0Xt0ZCjhC8WWYeLPfzww7LaEqpxPSV33313Sd5gV5PpScvVlxsjgORKPvLII0PnSmM77LCD9-STT8oqY6lWn60nqiaAN910U-j4wJo1a9bw__v37y-ri3xgOS4YOjNs6tq1a2zWMpL2pMXWhgceeMD_yjL_HUHnrbnLLrvEdrIZM2bIU4Qg4RAPmDwWo26GpAx7GQ7T3i5duoR-D5ZVAMt5PU0QlagXIf_eoUMHP1sew1-G_Gb_CKzWBfDdd9_1h7nyPIGRb5n2MQyNusZ8GS9cuFBWHUk1-my9USKAjPfJ3oWRBc1sPB0w-FuURfkL5I3Az2EOc3iw-Mxes2aN99FHH_k-wbfeessfll1yySWyuoYHllSc-KSuuOIKP6OazR_E8A5fy-jRo_3y8qbSIdIg28D1MIeL-Mruv_9-_y0fwLkZ4vfp0yd0Xo7loYjjoosuCh1He8myZmsrIJr4pfCRBa6FtAJYyesZMGvWrFAdGGJOjmpbNjl8hI8__rifWQ-BprwUwHL15awCiN9UthEhpw1r164tKUsfIuVq0DbT2rRp448K0lCNPltvVGQWWN4I0xg6bdmyRR4Sy4oVK_yUlQimC48--mjIx5U2QXdUG3ibXnfddbJ4CTi8cSrLY5OSqsuvv6OPPtp5mMlEQdJ1qsb1BCYaWrRoEbouLn2Ca3v77bf7L4Uo8uzLWQQQMZNtbNWqVeIECulX8eHKY8lJnYZq9Nl6o6oCOHbsWFm07PA1JH8HXxNJRLVBfnlEQWfeeeedS47t1auXLNYAEwLyXMzq1RpZryeQWF0emzTrn4U8-7KrADKaYVhrHsOQk6-sNGzevNnr3r176DotXrxYFg1R6T5bj1RNADt27OjPblYDZpbN33LeeefJIiFsbcD_5gIznObx22yzTeQXHV9HZlmGmzxMtUiW68lXp_T78XBFXY_GkGdfdhVAvkzN8hiz1i4glrKO4447ThYLUek-W49UTQAvvvhiWaxi8AY0fwuTCEnY2nDffffJYrGwFkvWEfVVt2rVqlDZN998UxarCbJcT4a5sn1cn3KQZ192FcARI0aE2unqagC5ZAX_YdIHRKX7bD1SNQHM0gnygskV87e0b99eFgkh25CmA0o2btwYug5LliyRxXwY-sjZTiYeapEs1_OAAw4oOSZJSBpDnn3ZVQDl8JfZ9CzgezPrwZKGwZXus_VIVQQQx3neMHv8wgsv-A5nQhYxDGPtEn5Gacccc0zJ72HZQRKyDcywusLQQXamefPmyWIN2Gbi-DeGVczWlZNyXk98S3IpxqmnniqL5UaefdlFANmJI-8fvyULLFyWdfFb4qhGn603qiKAjalLsmDBAm_o0KFOuwdsZlvyYSLbwBKCLMh1Vr_-9a9lkQbYYSF_Z2Bt27b1hgwZ4i8f4uHIyy9Tieu5fPnyUHmiNpeLPPuyiwDa1lfOnj1bFksFs-Jbb711SV0s74mjGn223qiKAKadxo_jjTfe8AYOHFhSb2MsaauRbIO5rcgF2ZlYwhEHs6Lyt9qMZRWDBw_2h0oMW1yp5PVk6CbLs3e5XOTZl10E0DZ5wQsmKzvuuGNJXbyo4qhWn60nqiKAWW9EwKuvvmpdJGoagsB-SyL28ttNs20ti1r4GpBXG7J0Joah-NXkb44yfD08HEykpKHS1_Pee-8NlV-6dKkslht59mUXAbznnntC7XziiSdksdRIf6Jtn7xJNftsvVB3AshSEBzJZn0YW6TYOcGDZK5st2Gb2Yp7YCGvNmTtTDiv2YrUr18_r3nz5qHfbzPONXXqVFlVCdW4nviQZHkWVZeLPPuyiwCyy0K2k-grWSFajFkX-4rjqHafrQfqTgDnzJlTUhdG2CaXSQHbAxj3wEJebcijMyGGLEAm7BU7BZL8dXF-p2pcTxZKy_KIRbnIsy-7CCCiLtvZmKE--3XNuuiTcdRSn61V6k4A2Q4mf5frBABxzsw6sLgHFvJqQzk6Ew5yNskTQ862tYwHh5lXG9W4ni-99FKofDm3WOXZl10E0DbZc_3118tiqeClJ_den3766bJYCbXcZ2uFuhNAfFFmXVlilRFQ1KwDi3tgIa82lLszrVu3zhp1hC89G9W4ngi2FOqTTz5ZFsuNPPuyiwAiWnItZ9LMbRT4DuU1Tnpp1EufrSaRAkiUCrPRPXr0kEVSk9eNINKJ7ARp91Sa8ADIeuIeWMirDZXoTK-99lroa8EWz62a11Nu8mfPadoACK7k2ZddBBA4l0v5KC688MLQNSZydxz11GerRaQAXnDBBSWNJmRVVvK6EYTIkp3A1XlOGHdZB5b0wObVhkp1Jhlle9iwYbJIVa-nFBKMQJ3lIM--LH93kqD94Ac_CLXz6aeflsViYaJKzrQTHTzJT1tvfbYaRArg1VdfXdJoovVmJa8bwReCWQ82ffp0WSyWqIi8SQ9sXm2oVGci9pt5HttOi2peT9YqsrHePIaZ5yhfZWPIsy-7CqBtMXTS8hWJzceaJpJSvfXZahApgLYwRzh1s5DXjQC5FICcFGkh0KdsU2BJD2xebUjbmVibF7eYOA6CJkjf0-TJk2Uxn2pdTzjttNNCxxGJOe-hcJ592VUAgSCz8vwEe00D_YBw-OaxRNFhIimJSvfZeiRSAIn8Kh8iwtOn6diSvG4E2B6aiRMnymIlMKtpi65sWlK78mpD2s7EA8IwBwd-2gXNwBcUawVl-2TU4YBqXU9gryxh0eSx9DOyr6Vh_fr1flYzUixEkWdfziKATGDIvc_8d1KIeUKi2ZIn2b7mbVS6z9YjkQIIcokExrCFFHpcXOKamTZt2jRZhU9eNwJWr14d6kwY2-uIShIMoYhoy_YuhnTktDDLsodWHp_0MOTVhrSdCQE0y9GGSZMm-eGMmOQw99oymcFQi4eT3BKybSNHjvykYkG1rmcA4fXlHleM68SyHtYHEgKe9uLzYujMOkLScvIbg8mepCCfefXlLAII3Dt5fozJIPbWMntP-7huCCa-Q9lXMHyBaSO6VLrP1iOxAkjQSumnibOoRDJ53YiApP2x_GbbQ42NGjXKeecC5NWGtJ1JCqDNaGfS_cEXmNS2alxPE_bHuqb8lJYkgHn15awCyFfzmDFjQudxMdwVMv1nHJXus_VIrAACndv2VWGzqE6T140IYFZMJrpJYziO6YhZHti82pC2M6URwCQj5HwaP2I1rqeE0Fsky5L1pLWkNXGQR1_OKoABJEK3ffEmGX5EW4KoOCrdZ-uRRAEEhh98pvO232-__XynrC11X1SnyetGSPhNcnmAzVgYbEbhyPLA5tWGtJ2JYS1DUPw9chN8nDEkJCIzx7pSyetpg2H2LbfcEhpiRxlCwjCYYBFx4bdMGtuXGyuA8PLLL_tZ4mRfsBnLmbIuD6p0n61HUglgLcNDg08IpzyZzY4__ng_Ego-FAIBpJktqwfefvttPxDqVVdd5Z111ll-qHUeUtrK3l32BRNlZcOGDfJQJ2rleuL3u_HGG_0JmeB38EDzpcqMNteiHEtmKglBJvDpksKUdp144om-MLNwGx8kM8BKeal7AVQURcmKCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSxlFUBWrrNw1LR6X7tVq7Cn1rzOacNaZT2uHqE_PvDAA_4um1_-8pcl7WbNoVI8yiqAzzzzTGhlOwtclfzJukMh63H1BDspDjjggFBfNI0900rxUAFsImQVsqzH1QPscWZnheyDNlMBLCYqgB8zc-ZMf69kYGw3qyeyClnW4-qBSy65JNT_okwFsJioAH5MnpnDqkFWIct6XK3DPtvWrVuXtI3AB0Sx_uMf_-jHVKQvBkZ-FKV4qAB-TL0L4KWXXurH7Atsr732kkWsNFUBxO9ntosw8oTcUhQTFcCPqXcBzEpTFUCZq9gl14lSHFQAP0YFsGkJ4LHHHlvSLsLcK4pEBfBjVACblgASKNVsF_EMFUWiAvgxKoBNSwBlKsozzzxTFlEUNwEk3-yvfvUrP8MWC0s7d-7sh-weNGiQH0F4zZo1JeXzFMDNmzf7GcJI40hi6R49eviJtAlrzn8TRZfQ7GTWSsuyZcv8YzCi8Zq_k9Dwwd-ijLSFSRBh-dlnn_UjORO5uW_fvn7uC65dt27d_AeV8OhkOXvuuefk4akhjaT525566ilZxEpjBfDDDz_05s6d6_vcCMW_7777-veFBD70jd69e3vDhw_3I1bPnz_fT4VZDsikZrafc5vtInq2-XfTbPdx5cqVJWXoKyasMeTfx40b57ebe9mpUyc_nD9JptJA32AnDnlCeIZINcB1o3-QLY6seHfeeWeqvC42ktrA-YmszTNFP-zSpYufhvOggw7y_23JkiUl5W1Qx0MPPeSdfvrp3qGHHuqnb8D4_3x1p6mjmqQSQMTnjDPOaEhBGGX8nbDlhG-HPARw06ZN_sMl8xJEGcJy2223-R00Cdb7yeNdLCpvBCJMTg4efLkUI8lw1j_44IOyykSyClnW40jNOGHCBOdsbsxQ83C7ZDdLQ9pkRzaz3ce4fBqLFi0KCaxpvJCT4KVhy_lrM_r--PHjnYUwqQ3ca3kuaYh71DNLwvnu3buHjpE2cODAyDqqTaIAsl6Kt5JsVJwhQuSbbawAki-hVatWoTrSGBnR-DqJo1wCSI5eWdbV-LIg41pasgpZluO4h2mSJ8UZD0-eVEoAL7_8cn9JjazDtAEDBojaPoH1iUceeWTomDTGOsYnn3xSVhlJVBtIIZr0MWMa1xYdMKHfJF0H09AQl2e_UsQK4Pr16yPfUuRY5VOdIR1vAZnqjwbzaSyPS3sRSHMYdZNatGjhP4AMGfjf5s2bh8pgfE3FiWClBbBZs2YNw6SePXt6Xbt2tWYkC4yv7rRkETJwPY5sdVFfDnypMBRk2MuXA21kWGXLKVyPAnjTTTeFjg2Mexv8__79-8vqfN59912_z8pjA6MN-J4ZQkb1i5YtW3oLFy6UVVuxtWHOnDmhOnl2O3To4AtslKjhagpeyLwE5N9pf_v27b0dd9wx8rllWJxmZFZJYgWQoYpsBBeJyBm8yUzw7bDKftttt20oa8vzmkYAyW4mj-Oi4qfDp7Bly5aS8gzRGfbysMnj8LtFQepGIoRgMi8uW6OCv0VZVOrHQAD5zfhWuC58DdtSNzJcxg80evRoa8chekkaXIUswPU4fL3yN9JGfEm29gGiiU-S7GfB0DFvAdy4cWPJvZFCQ2Y5ef_i7qMUD_oy4hP8Ny-vKVOm-H7vjz76yH-w2U2C64MteDbw9cprh3Dgv167dm1JWZ4v0n3ywpTHtGnTJtVzJNvAi9d0WZBpD9-g6TfHfUV_tbk2rrvuOj9joPlC45mUdeC2iqqDtKe1RKQA2t52fOklbRmiQ_AmkMcGlnTjcOZzg81j2rVr539NJoFfCmeyPGeaN2aes8ArVqzwHzg5KZTEo48-GvIZMqmQBlchC3A9Tn79MSHmMlSHRx55xPnauNLYWWApHqbhnpAv4SQQM1kP7p2kySrCx9k-RFjmk0RUGxgxMbkSB0Nt-RXKvQ98fvwNF1UcTExJ332vXr1ksapiFUBmduSbh5v1xhtvyKJW-AKSQ-LAkgRQ3jQuNBcyLXxtyMTadKAk8hTAxsCXkbxmvHWTcBWyAJfjeLPL38ZMYy1SLgEcO3asLJoIX4cyuT1DTSYi0sAIxzbZsHjxYlm0hKg2zJo1Sxa1cs4554SODYzk8mk4--yzQ8fykVMrWAWQWUj5oxn3uyC3IgUWJ4D8TQonwyZXGCbL8_JVFketCCAwi2j-lvPOO08WCeEiZCYux7FcxCzLkL3WfDoB5RDAjh07-qMMV3APyLpcd6YglrKO4447ThYrwdYGfLNp4StdHo-Zs8lJvPTSS6Hj77rrLlmsalgF8OSTTy75wfg-pM8vCb4WbQ7VOAFkrZhZlskO3n5ZkP5H1uHFUUsCyCyd-VvSdFoXITNxOW7VqlUlZTHWhtYi5RDAiy--WBZLxYgRI0J1ZXEBsD7PrAP_YZwg29qAj9IFJkdkHWlcSiZMjJjHs-6xVrAKoJxMGDJkiCySCmYD5cWLE8A-ffqUlLXNzqWFDm_WhQM6jloSQDqp-VvwqSbhImQmLsfxMjJnOzEmb2qRcghgFtECOfxldjwLrIyQvyluGCzbwOgqblWEjX79-pXUgU-PSR8XpA6ceuqpskjVCAkgU_XyIrNLIQss3pR1RQkgF1U6XQnxlBXZWfgijKPcAkj7CMeEM5x2MazlocSnJO2YY44p-S1clyRchMzE9Tj5ksL4N4Z5Lrtwyk3eAsjkVBZYHSGvF30tC88__3yoLu5fFLINSc-ADRlUguUwrgwePLikjpNOOkkWqRohAWTblrzIv_vd72SxVMyePTtUV5QA2nwF7KSYPHlyiV122WUNhpCYxvKDwIYOHVpSF2us4iiXAC5YsMD_LeYSiiwWtcQkwFXIAlyPs_mHA2vbtq0_WmB5CA-r6-xwnuQtgFn7g21NKM9FFph5lj5ylm9FIdvA15wrso6oNY5x0CfMOnjB1wohAWSJgrxhdOYs2B6WKAFkplOWzdNYuB1H3gKID5QtQPJ3ZLWkbVCuQhaQ5Tj2usrfZzNWDvD252ucdXqVJG8BTLPsxIZt8oKXYlakP42XaxSyDS6TFwGyDpY9uSIFMEsd5SIkgPfcc0_ohr366quyWCpYviLrihLAefPmhcrmaSzejCNPAeR6yWVE0hAHdtkQuZlzmWbbZmZbrGuSRcgg63EM5ePWe0rDd8jDykRKJchbALOIB9ieJ5dlXRLpT4zbd5xHG2QdWcSrrgSQxY3yhmV1_rKwV9YVJYC23R_bb7-9t9NOO-VilRoCsywEJ7dsCxFS2EWxdOnSxBl1VtbL42tNAIEZyBkzZvhDq6jtiNJwok-dOlVWlTu1IoBEMJLX4LHHHpPFUiP35bOvOIo82iDryCJedSWAzCrJG4ZfMAtyNhOLEkCbWKZZAJwXeQmgba8l2_FcJghsX8O1KIAmiCGLuFnKxMLzJJ9nVj9YWmpFAG39mrBgWWFXlFkXvzOKPNog68giXnUlgMxUyhvmunYoYPr06aG6ogSQhcqybCX3DeYlgNxcWY_rZMDNN98cuha1LoASHPasFyOmHes5ZXt4kNnmVS5qRQCXL18eavv1118vi6WCl4zcL04cvijyaIOsI4t41ZUAsk5IrvVi6JYFlnSY9WBRAsh55b5Bl2gojSUvAZThu5gRdcW2i6beBNBk3bp1oeAEGF_L5aJWBBDRks9T3MxtHDafOhNMUeTRBllHFvGqKwEENuCbPzguvlkctqCRUQIIhNYyy-I3qxRE5DDPTcRpV9iHLNubdr-nCeIr66lnAQTiycmvF1dRcqFWBBDoS3lc4wsvvLCkHizOPZVHG2QdWcSr7gSQLy_zBzODumHDBlksFttQGosTQFuoJZzIleCCCy4oOS_hjlwhUo78_fiAXCAsvqwDq3cBBPlCHDZsmCySG7UkgISGN-vCnn76aVksFibX5OoAwk3F-ZbzaIOsI4t41Z0A2hZDu3YgtrHJOrA4AURApL-IKBhx-x3z4uqrry4573bbbSeLJILfS7YXP6gLUdGCm4IAEmPRPFc5t0TVkgDaFkPHLV-xYfMLJ0WmyaMNso4s4lV3AghyGIYfgyUcabj77rtDNyuwOAEEm_8LMXWNv2aSJtmQLQwVDmxX5DIFl4TcBJGUvyGwWhBA1jcmLciOgqAJ0hfGzp5yUUsCCPL3YDfccIMsZoXrTiBi81gCjbB7Ko482iDryCJedSmArEWT0VzY6kT04jhYwiH39JqWJIA86HKxJ0YgRZf1iGwdY_jMCv40e2nZAy0fULb9JAmPhGxa8rdPnDhRFiuBWWLb8N-0pN_hImQmLsfxwDLsYsLIZUEzs71yUz0moyDniRScagsgExgyNQD_zTrKOAhBZktLkebrOY82yDqyiFddCiCwhEFeeG4a69oQwiCyBFFC2C8s99_ahnNJAggsiTFD65vnJow3wwGSLr333nu-b4SFxcw0ssCUsFf8DoawwXHMLqdBLmHB2EJ32GGH-R2BGG6mTZs2TVbh_y7Z0TGEmOVEwdIPgs6yXY4hsgzgKjsMVisCaJbld0-aNMlfPM8kh7lfmQkhhn7Ub8vXMXLkyE8qLgO1JoDAtZLXAWPdJAFG6cP49LjXCCa-Q7kyAsMXmMYtlEcbZB1ZxEv25yx1lItYAaQT8-DKG2AaAiH_DUM0bNP2aQQQCBVue3CyWFoBRHij2mOzqHBdSXtlOYdNJLFRo0bV7E4QKYA2o21J1xBfYFJ7GkstCiBf-mPGjAldDxfDxZI2pWgebZB1ZBGvuhVAyJLGj-EOvqLGpsVk5vmII44I1eFqafNqAOKTVnijBJCvUplkKY3h1OYhqWcBTDLSlWb1I7pQiwIYQEBQGdUljdEmkjilJY82yDqyiFddC2AAw05CgsubYhqRKnDkBzsfGiuAAQy3eXDifIvSCDJAPgJ-gysM5RiS8DVG_DMc0LZzRwlgAHXIpQs2Y5GwGSGkVgWQEQHDePxPNj9tlLH-j6jWWXcUZaGWBRBefvllP0ivbYgrjeVDd9xxh6wikTzaIOvIIl5NQgCBLxvWtf385z_3vvvd7_r-OMJ9k7eDB9g1UqwrPICE6-KhZbaYcyNC-JNYu0jeEgJzurwlyw2-PvY0M8lBpjiuGT5K_DsEBUiayatlSKHI9cbvetZZZzXcD9qHn5h9wQS5cF1DWiQYYeFD5Rli1ECaSV68LMzHx5w1EpOSDicBVBRFaUqoACqKUlhUABVFKSwqgIqiFBYVQEVRCosKoKIohUUFUFGUwqICqChKYVEBVBSlsKgAKopSWFQAK8jMmTP9_ZiBsX1MUZTqoQJYQfLKPKcoSj6oAFYQFUBFqS1UACuICqCi1BYqgBVEBVBRagsVwAqiAqgotYUKYAVRAVSU2iJSAFeuXOmHZg9s2bJlJX8n-vNdd93lZ4476KCDvC5duvjh1EmiRMh0IjcTDTkPqIew-ORSGDRokB9CnuQw--yzj59Ri99w55135pZrgmx3c-fO9aNOE8qdnCK77rqrf07Ck_fu3dsbPny4H_F4_vz53jvvvCOraIDrFlxDov2aAki4fPMa24y0iDaS7g_XjGjNpOkkPDz3h_SK3Cv-bcmSJSXlbVDHQw895J1--uneoYce6ofBx_j_RLROU0cc1P_ss8_6EaWJIN23b1__nnbu3Nnr1q2b_7sJG3_llVemyu0cR9L1ArIKkkaBhF60M7heJ510kp8SIiktgVJ_RAqgzAVg5hMgP0GHDh1K_m4zOtHixYuNWt1BiGx5UW1GfoXx48dnFkJSDU6YMMHPfSvrjjMyvCHEtmxdXDdZ3sWi8o7E3Z9Fixb5LyNZlzTEPSpHC4niu3fvHjpG2sCBAyPrsEHaR3KD8AJp3bp1qL44I8n8gw8-KKtMRdz1ev75532hk-eT1q5dO2_KlClGrUq94yyA5557bqhjxBnJ1S-88EJRezJZstEFRhKjJ598UlYZCw9xmgRGcYZoSCotgNdcc42fhEjWE2VkwCOnrwk5V7hvsmyU8WWcVgTJFSyPd7Vx48Y1JN5KS9T14mWeJjGRaa4JlpTaxUkAyfgmO0P79u39N3OvXr1i00leeuml8hSRvPvuu_4wV9YRGOfBf8YXpi1bG9ayZUtv4cKFsmorJFuK-mLi4WA4xrCXL6aePXv6w0lbXt9qC-CcOXNCx5N-ka91XgpRokbmu0BQSCwl_96sWTP_PpP1L0pcGRaTNCuJKAHkHJ06dfKTrXONu3btGnlvMZJguWC7Xg888EDoPnKN-NLbZZddYoVxxowZ8hRKHZJaAPk6at68ecN_H3744davLHw1xx57bKjD0LHIKJcG_D7yeB4QMmWtXbu2pCxfirfeeqv_8Mhj2rRpk-rLhIxt8lj8T_jQSJFpA9EkeTvZvPALcoxNAPEbkaUOk7mCSRAe_C3KovxO8v4gHObQnexz-LoYcgaQxY2XmG2If9111_nZ60xBwGcp69i0aVNkHbfccktDuSgCAURIucbURepS23XmvPh-R48ebRVeBCwt8npx7c0hOP7H---_3-9PAZwfd0KfPn1C5-ZYXtRKfZNaAE0777zzZPEQl112Weg4vrJsHd0EMZPHtWrVyhebON5__33fDyePZVImCfn1R95S1yEWkz5r1qyR_1xCnrPAUfeHlxQTQnHw4pJfV1yDwOfH30jVGMcTTzwR-kJiFJDEihUr_PSgSddKwstT-gxdEt5HXS8EH_GPg8kaJkLksddee60sqtQZzgJIR0iL_OLBbrzxRlmsAYZQMuE2X468hdOwefNmq-M-biKGLxpZnhnDclAJAZw1a5YsauWcc84JHRsYCd3TwIypPPb111-XxXKDL2x5Pr5a0xB1vfCZpoEX7M4771xybBrBV2obJwFk2OOSdJzZWHxPZh3MtkXBkFOe85RTTpHFYkEsZR3HHXecLNYAy0zMsgy10viyslBuAcRHmRa-wOTxmDk7mgRJ3eXxLI0qJ7hezPOlGY2A7Xrh13VBTgBus802ziMFpbZwEkDWarkiOw0Wle1-xIgRobKuQyWQSxrwH7LExcaqVatC53zzzTdlsVwotwCyvMQF21KmtBNHAUyMmMezVrOc8MVmni-t6NuuV9IwX4I_VNZRrtGCUhmcBJAO4MoLL7wQqofZShty-MtsYBbwzchzRg2DGTYjkGZZnO7loJwCyGwvC7hd6NevX0kd-PRY4O4CX1FmHSyCLyeIvHk-ZqfTIK9X3Esxio0bN5bUgTV2MbhSXVILIENDc4YsLTiQWZJi1mULBMpuCtm5EIwssLBV1sXatihss3z8G0Nycwa0sZRTANlB4YqcrWc5jCuDBw8uqcPFRxyA6PKiZAKM5VIMa1lrN3bs2JAdc8wxJedjwiYN8noxc-8Kw12zDmzevHmymFJHpBZA1r5lRa7pY5ZVYlsfNnv2bFksFVu2bPG_iMy6mJCJgt0F8tyBtW3b1hsyZIi_AwBhbYzPp5wCyNecK7KO_v37yyKJcG3MOhCotCxYsMAbOnRo6AXpakkrC0C2lWUvWZAz32knjJTaJLUAxk1eJCEXA_N1JbFNXvCAZEX6pnjQ4jj__PND57cZS3L46mGYzZDIhXIKoMvkRYCsw_ZiSkIKYJo63njjDX8Lnby2WS3N1kfZ1izXC6QA3n777bKIUkekFsABAwbIIqkZNmxYSV0s2pXcc889oY7NWrOsSH8is4dJMATDpyR_R5ThR0JYmUhJgwqg50-A2Ratm8ZLhv3fe-21l3-NTLNtV4xaLG4i25rleoEKYNMitQCyyDgrMgpKjx49ZBF_Fb7s2ETnyAr7U8262FecBhzjbHNiSGnufIkzHoqpU6fKqkIUXQBZXsTElrx-RNphN87SpUsT_cy2mVgVQCUrqQXwK1_5iiySGjncse3OYKW_7NiEmsoK-znNumiPK4ghi28Je8ULIMlXleSzLLoA2vYqs7TKZaKJSQdZhwqgkpXUAsjm8Kww5DXrsm3wX758eahjX3_99bJYKhAuuXeUmHaNhckV1skRf7BFixah34vosmMgiqILIH-T7XedVCIun1kHpgKoZCW1AGJxgT-jsM3ITpo0SRbzRUuux4ubuY0D36H87Xnv21y3bl1odhuLWuMIRRdAfHtm2Syx9QhSa9aBqQAqWXESQCYqXGEBsqwHf58NfINmOTboZ4H4g_KcRB7OG-LoyS_NuFhxRLMxy9p8oWmR9yfLAy3riBOvKNIKINFzzHJY2j3eJrw0ZD0qgEpWnASQEEuuEPnDrIPoG1HLRwizLs_59NNPy2Kx4GiXM4XsYXbxM7kQhMIKjBnvKC644IKSssS8y4q8P1keaFlHlHjFkVYA33rrrZJyWNrwaAGEWpN1YCqASlacBBDxwleXlj__-c-hsEtHHXWULNaAbTF0muUrJjYfETsIygVx5cxzxW0Fu_rqq0vKbrfddrJIauT9yfJAyzqixCuOtAKIK8Qsh02fPl0WiyUqQrgKoJIVJwHECAGUZuU9X1ysHZTHJ83sEiRTHnPDDTfIYlZYYyajzxBOi6glUXBMmoW0NgiaIP2WkydPlsUasIVzcnmhmMj7k-WBlnVEiVccaQUQ5NIkIomnxRaNPDAVQCUrzgKI0cnjZjvZlC8XP2O25S8SJjBkmHL-OykEOWGtbMmT4r7IAHFliMwERdoFzUD7ZTABTEasNiGCsBRMtp-leYAl8v5keaBlHXHiFYWLAJKNTl6viRMnymIlMEtsi9htWprrJ9ua5XqBCmDTIrUAMuNprq3r2LGjP6RjWxMBD_C9rV-_3o-uK3dhYMROSxvaillieTzGWjz2XjIDyxcmHR_BxHcoOyaGLzAp4gcCaB7Dkh3OT6gkJjnMr10c-QzTCaxgy38ycuTITyqOQC4Fwbg2pGLkmhP_0LRp06bJKnzk_cnyQMs64sQrChcBXL16dejlhvFiJMpL8FKlP9GvGCLLJVTyfJgKoJKV1AJIh6GT2jowXzVyqYtp_M0lVh1v_TFjxoTqcTGGW7Y0lRIpgDZDoDD576bhC0zzIBISPqku02xrJsF2f1yRdcSJVxRSkJLqSNpzzbWx9TFs1KhRuhNEyRUnAQS-wGQniDPWfrkGngwguGacsEYZfsS0kavTCGCSMbHj4kfkIbZ9QdqsqQkgIwVbqoQkYyKLF6MKoJInzgIIfMXI7W3S-CpkDzDD4sbw8ssv-1niZMezGUtSyPPqAsNavk7xFdqG7lHG-j-iEbt82ZowtOZlwlcNcfiYvJEz5lhTE8AA2i6XK9kM14sZFUgFUMmTTAIYwAwqPirezjwITHyQtJqvKlIw5gmb5PmSJA0lXxCIK-LB4mJ-Q1SYfVf43QRCveqqq_zArYTpR4SI-sK-VfYF33vvvd6GDRvkoYoj-PpIasQkB-tFWWfKdcanS3CJuNl7RcmDRgmgoihKPaMCqChKYVEBVBSlsKgAKopSWFQAFUUpLCqAiqIUFhVARVEKiwqgoiiFJVIAWQDMnszA4uL4KYqi1CORAqgoitLUUQFUFKWwqAAqilJYVAAVRSksKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSwqgIqiFBYVQEVRCosKoKIohUUFUFGUwqICqChKYVEBVBSlsKgAKopSWFQAFUUpLCqAiqIUFhVARVEKiwqgoiiFRQVQUZTCogKoKEphUQFUFKWwqAAqilJYVAAVRSksKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSwqgIqiFBYVQEVRCosKoKIohUUFUFGUwqICqChKYVEBVBSlsKgAKopSWFQAFUUpLCqAiqIUFhVARVEKiwqgoiiFRQVQUZTCogKoKEphUQFUFKWw_B9FTUkADrx2aAAAAABJRU5ErkJggg\"}]}]",
>   "status": "PENDING",
>   "policy": {
>     "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/policies/QTAzCPHRfwCBXcI1Rm9-FiDR1g"
>   },
>   "application": {
>     "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/applications/QTAzdui396GxUj_w7N2KHr1edg"
>   },
>   "user": {
>     "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzw8gbh6Z777TpHz3pkXErIw",
>     "userId": "jbeloncik@daon.com"
>   },
>   "tenant": {
>     "href": "https://api.identityx-cloud.com/IdentityXServices/rest/v1/tenants/r4SWIoHpn0fmXw4pkQhAbw"
>   }
> }
> ```

### Get Authentication Request

Retrieve an authentication request

> **Collapse: Show details**
>
> * Properties
>
> * Input Schema
>
> * Output Schema
>
> - Authentication Request Id textField
>
>   The identifier of the authentication request to be retrieved.
>
> * default object
>
>   * properties object
>
>     * apiUrl string required
>
>     * username string required
>
>     * password string required
>
>     * authId string required
>
> - output object
>
>   * rawResponse object
>
>   * complete boolean
>
>   * verificationResult string
>
>   * fidoResponseCode number
>
>   * fidoResponseMessage string
>
>   * status string
>
> Output Example
>
> ```json
> {
>   "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/authenticationRequests/QTAzqDIl7wrj-v_gtombS9f_tw",
>   "id": "QTAzqDIl7wrj-v_gtombS9f_tw",
>   "complete": true,
>   "authenticationRequestId": "8bAHBTRJ06N8vbLncP-Irg",
>   "description": "FIDO - OOB Auth Request",
>   "verificationResult": "Y",
>   "expiration": "2022-04-27T11:37:07.476+0000",
>   "availableRetries": 5,
>   "totalRetriesAllowed": 5,
>   "processed": "2022-04-27T11:24:51.484+0000",
>   "oneTimePasswordEnabled": false,
>   "created": "2022-04-27T11:22:08.033+0000",
>   "type": "FI",
>   "fidoChallenge": "Kcd2xYLyd1hwPwRWdrohcw",
>   "secureTextTransactionContent": "secure transaction details from postman",
>   "secureTransactionContentType": "text/plain",
>   "fidoAuthenticationRequest": "[{\"header\":{\"upv\":{\"major\":1,\"minor\":0},\"op\":\"Auth\",\"appID\":\"https://example.com\",\"exts\":[{\"id\":\"com.daon.sdk.envCheck\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.deviceInfo\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.location\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.authenticatorMetadata\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.healthCheck\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"fido.uaf.safetynet\",\"data\":\"\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.ados.decChain\",\"data\":\"[\\\"MIIE6TCCAtOgAwIBAgIRAJEmGK-0XEGFin4brMpnidIwCwYJKoZIhvcNAQELMEcxFTATBgNVBAMMDElkZW50aXR5WCBDQTENMAsGA1UECgwERGFvbjESMBAGA1UECwwJSWRlbnRpdHlYMQswCQYDVQQGEwJJRTAeFw0xNzA2MTUwOTQ3NTFaFw0xOTA2MTUwOTQ3NTFaMFoxDTALBgNVBAoMBERhb24xEjAQBgNVBAsMCUlkZW50aXR5WDELMAkGA1UEBhMCSUUxKDAmBgNVBAMMH0RFX0RBT05fQVVUSEVOVElDQVRJT05fREFUQV9LRUswggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCXrHT7hGCZR4KzlwawZl3yefpUov44BWofCNnuGh3RoaQ63vXX6jsrfoCVJdto5a38Nd7ckQzjhtuoAfLeUT3sbm7uhXCCoC5xJ_B96G6LeTvY6yZ2ZsO3K8dOl8epKOI7e2Xh_3WQg0xa21QmJxnTcMSMj0TMHrXlb66nh-CoTbAcKopm0xbrPfOMLoZ1xGk7iOVxSY_TRjep6tn4Z7t7r-bsJnDjJtctto4gYXk7mDkwdAMfBpoq1Jp0nGbv8TCMySAjOUSs9ptE7pRl5No6iF4QYNDDUUhI9q7MAcpSgEYLaAPzhZdzZnmDfwwOIPCiss0qKV9L3H6wh-NLQ_r7AgMBAAGjgcAwgb0wfgYDVR0jBHcwdYAUZplSSlDw67i7wEa-1wVzqzvdL5ahS6RJMEcxFTATBgNVBAMMDElkZW50aXR5WCBDQTENMAsGA1UECgwERGFvbjESMBAGA1UECwwJSWRlbnRpdHlYMQswCQYDVQQGEwJJRYIQKuhll9ePQGSsywpelEVwazAdBgNVHQ4EFgQUyeJ8CGmnhFk5Cs0c6TEEG2GrL08wDAYDVR0TAQH_BAIwADAOBgNVHQ8BAf8EBAMCBLAwCwYJKoZIhvcNAQELA4ICAQA-cpJUeOAz96VXYHqIS_yRkltsSkLvmgqwuwx2fShZJQ1pawaRf8qWH9takyyBzAPNVMYsxIc4eMF4qRhExtADB5EQBFF-DWVMoLymYOLMDHii9lnuYdsV0B82EsQu5U7SccuDH3ffNOlVJq2NS8jHUFm7GxF36O6BdojT3vXgHmH_dZo3GzGCRDpkKt_gUAO1aj2Ga1YmLcd2ptA6OA1SllW0eWS5yb_KNscCVVQke2gvJkACHrsIel7AxNBgukWlTANCrgH2UOhhhXlOmu3RRoxhUL8Ya5V7qSdiVZzmfMZwRpyX92FbGUIb_lL9nlFs3iGtE9gXE-DVTNs93jn_XIK0Q8D6lcvpVtI4bJQhUJ7u78MeoSPuYx-9SX4ioiNmVVYC6fdAieSG1ggEiIhw0U8l-4u1pItyPIqwt_OijaElOouTWzeBa3AJA7CqasOZoMx6BXJE5dLcILbpYduA0vSc3em6cr-LJgRr7uuvQCJ-3pGX_gipMyailXYd2S985PQXsyKEW5AegBcEgNX3MIvNPUhb2eS-Ab_JIZbQGAUGTT_HwQXFB08pMXJ-UK_FwdphXVGMJy9jmyvwWLlBFXyYGrAiq0pLlkHexCqHcjYbchgf1IDIwp0yQ3KcoA42w555djBN7hFHTa9dfAdTOHRKlICG_PhsMUdhZ_T7oQ==\\\"]\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.ados.dekId\",\"data\":\"1000090661\",\"fail_if_unknown\":false},{\"id\":\"com.daon.authRequest.retriesRemaining\",\"data\":\"5\",\"fail_if_unknown\":false},{\"id\":\"com.daon.authRequest.maxAttempts\",\"data\":\"5\",\"fail_if_unknown\":false},{\"id\":\"com.daon.user.retriesRemaining\",\"data\":\"10\",\"fail_if_unknown\":false},{\"id\":\"com.daon.user.maxAttempts\",\"data\":\"10\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.voice.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.voice.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.passcode.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.passcode.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.otp.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.otp.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.identityx.version\",\"data\":\"5.2.4.0\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8201.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9201.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8401.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9401.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8201.recognition.timeout\",\"data\":\"7000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9201.recognition.timeout\",\"data\":\"7000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8401.recognition.timeout\",\"data\":\"30000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9401.recognition.timeout\",\"data\":\"30000\",\"fail_if_unknown\":false}]},\"challenge\":\"Kcd2xYLyd1hwPwRWdrohcw\",\"policy\":{\"accepted\":[[{\"aaid\":[\"D409#2204\"],\"keyIDs\":[\"NDRBQjlGQzQtNUYyNC00QTA0LTk0NjMtMURFNEI5MTBEQ0Y1\"]}]]},\"transaction\":[{\"contentType\":\"text/plain\",\"content\":\"c2VjdXJlIHRyYW5zYWN0aW9uIGRldGFpbHMgZnJvbSBwb3N0bWFu\"},{\"tcDisplayPNGCharacteristics\":{\"width\":320,\"height\":240,\"bitDepth\":16,\"colorType\":2,\"compression\":0,\"filter\":0,\"interlace\":0},\"contentType\":\"image/png\",\"content\":\"iVBORw0KGgoAAAANSUhEUgAAAUAAAADwCAYAAABxLb1rAAA0QklEQVR4Xu2dCdgXVfXHrZASTDY3yAdQSQG1FE0UBaEC0cAtFSRks8VE0wxSQFv00VRScwEUQQUVE3eMREwCFXNJUxAEEVMDQ0RLSUta5v985u-83t-ZO8udd37bO-fzPOcpee_c-d2ZO9-Ze-6952zlKYqiFJSt5D8oiqIUBRVARVEKiwqgoiiFRQVQUZTCogKoKEphUQFUFKWwqAAqilJYVAAVRSksKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSwqgIqiFJZUAvjhhx96c-fO9X74wx96X__61719993X23XXXb3ddtvN23vvvb3evXt7w4cP9372s5958-fP99555x1ZhRObN2_27r__fu-0007zDj_8cK9Hjx7--fbbbz__v3_84x97v__9771___vf8tBGQTsfeughb_z48d43vvENr2fPnt7uu-_uffGLX_T2339_75vf_Kb305_-1HvkkUe8f_3rX_LwEI8__rj_OwN78803ZZFE_va3v5XUkabdK1euLCm_bNmykr__73__8_993Lhx_v3s1q2b16lTJ-9LX_qSd_7555eUjaNa90lR8iJWAD_44ANvwoQJ3uc__3lvq622Sm2f-cxnvK997WveK6-8IquMZdOmTb7Ifvaznw3VabPOnTt7t912m_9ANwbOe-6553otW7YMnSPKtt12W--UU06JbWO7du1KjrnhhhtkkUQQEHluRDGOb33rWyXlEfOARYsW-S8tWWdgCFcS1bpPipI3kQL4l7_8xdtjjz1CndnFHn74YVltJPfdd5_XqlWrUB1p7KijjvK_3rJw9913e9ttt12ozrR2zTXXyCobqDUBvPzyy71PfepTofpMGzBggKitlGrdJ0UpB1YB_Oc__-ntueeeoQ6M8dZnyMSwl-ETw8QuXbr4X32ybFoBvPbaa71Pf_rToeOxFi1a-EJ84IEH-v_bvHnzUBns4IMPdn64fvGLX0QKAv_eoUMH78tf_rI__GVo16xZs1C5ehHAm266KVRPYGa7-vfvL6troFr3SVHKhVUAL7roolDHPeSQQ7zf_va3kb4vRPOpp57yfWTBECuNAN57772hc_GQnXjiid6SJUu8LVu2lJTH78RwCtGVx33ve98rKRvHrFmzQsdj1ItQ_fWvf5WH-A8ufj18W_jMKF8PArjPPvuUDO-7du3qTZkyxVuzZo330Ucf-UPTt956y_vNb37jXXLJJbI6n2rdJ0UpJ1YBlF9_Rx99tPef__xHFouFiQIesDhef_11r02bNiXnQjSYiEgC_-SgQYNCD9fChQtl0RAvvvii_8Uij2VSQD7IUfz3v__1br_9dv-lEEWtCGDWNgZU6z4pSrkJCSAObtlZmVUsB_JB_dznPuc98cQTslgkfHUyc2nWweRLEviiZBtdZj_TUmsCOHbsWFk0FbK-St0nRSk3IQHk68jsqAxzyjF7xyTL1ltvXXIuhs-uMPySD_qKFStksQb4m_T79erVy_kLNw21JIAdO3b0v8ZcqdZ9UpRKEBLAVatWhTpqlvVrSbBm0DwHQ1L8RlnAx2XWddVVV8kiDTAElO1DZMpBLQngxRdfLIulolr3SVEqQUgA6dxytnP06NGyWKPp06dPyTlYZJyVM888s6SuE044QRZp4IADDigpi7-zXNSSACb5Y6Oo1n1SlEoQEkCQnR7j33D457Gqn5lH_Ehm_ZdeeqkslhqWZ5h18aVh4_333w8t1zn11FNlsdyoFQFs3bq1LJKKat0nRakUVgF88MEHQw9dYG3btvWGDBniL6N4_vnnM_nOXnrppVC9bKWbPHlyiV122WUNxoNnGss1Ahs6dGhJXV_4whfkKX2WL18eOu_MmTNlsdyoFQFkHWMWqnWfFKVSWAUQmBWVnd9m7AoYPHiw_3bfuHGjrMYKa-lkPXnaNttsI0_ps3jx4lBZ9i6Xi1oRwK9-9auySCqqdZ8UpVJECiDceuutXvv27UMdN8rwHfKWZyIljnnz5oWOzdMY5tqwLeZdunSpLJYbtSKA5l5gF6p1nxSlUsQKILB0YsaMGV6_fv0itzdJY7vc1KlTZVUN2IRo--2393baaadcLGpoZXugH330UVksN-pdAKt1nxSlUiQKoAliyPY2lkawkDUpesrs2bNlFT6IjizLcKvc2IZ0hHMqF3kIINFb5G-ulABW6z4pSqVwEkAJW6rY0vTtb3_burUMAWDmVcICWFn2lltukcVyx-bUx3dZLvhaMs81ffp0WSQR21dYpQSwWvdJUSpFowTQZN26dX4kEPnAzJkzRxb1gwrIWHJnnHGGLJY7CLYU6pNPPlkWy40gYEJgV1xxhSySyLRp00LXtFICWK37pCiVIjcBhNdeey0ULonFrzb69u1bUo5wU5WAobt53p133tk5OEBa5P7Xc845RxZJZMSIESV1YJUSQKjWfVKUSpCrAIKMNjxs2DBZxMcWcquc_rgAYgDK895xxx2yWC4cccQRJecZOHCgLBILQQR22GGH0O-tpABW6z4pSiXIXQAJIGo-LFE7LYg_J4ej3bt3z7Rh3wXWKrL-zDwvXzU2X2VjmTRpUsl52FXx3nvvyWKRXHnllSHxwSopgNW6T4pSCUIC-Oqrr3p___vf5T-ngqAJch8xOwWiIK-EfLjZa9qYIelzzz0n_ykESXzyPq8N246atJFU_vSnP4WEOrBKCiBU6z4pSrkJCSBLNUiC9KMf_ShxQbMJX1CsFZQPytq1a2XRBniQybgmjyE8lcvmfaJUMyxjxwNfWUmQtY7wUPK8hIMn-Gca1q9f75199tl-qPko2CYoF5KzlpK8GnGw55r9u_L3BVZpAazWfVKUcmMVQLOT48hnKMdDyySHGRIfHxVfKvjVWNQqH5CRI0d-UnEELLUgw5o8ll0Cxx9_vHfzzTd7q1ev9oeOxCX8xz_-4c84P_bYY344JXaemEmNmLVMwx_-8IdQnLvgeJb18KASC4_2EgCCoTNr4BiW8gAHkz1xIfGB_bDyHMQjPOmkk_wQ9LwgEFP2VbNMRk7SjBkzJnR8pQUQqnWfFKWcJAqgzRiaRQ3PAsMXmPSgBpBLxCagWczlwVqwYIFzyk9pSQKIeJIvVx6Xxs4666yq7gSRVOs-KUq5yCSASUbIeVc_4oYNG0KzplmMpO0uvPDCC6FAnS6WZiE1CZZcz0HipSCBufxbtQQQqnWfFKUchASQYS1DM2ZvbX6fKGNISJpMjm0MDE0RUBmHLs722msv3x_3zDPPyOpSQYIjdjjIdXtRxtCZYTDBIqKy5EkYGiJqSe3iy9lMNlRrAhhQjfukKHkTEkDJ22-_7Tvl8eMwJGNhLjOA-HRIb8i-YLZr8WWQJwgxmeXwLzILGZwXvyK7EUjyze-ypa9sDPj9brzxRm_ixIned77zHd-_haB8__vf92e0OWdjlswghHfddZcvhqNGjfLrx8-Hr7AehaFa90lR8iBRABVFUZoqKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKAywAZ81jYFnSHCi1gwqgojggA-ruueeesohSR6gAKooDKoBNi0gBnDlzpr-HNDC2wSlKPZJnX1YBbFpECiABUc0bvf_--8siilIX5NmXVQCbFiqASpMnz75M0AqCwAZGhBulflEBVJo82peVKFQAlSaP9mUlChVApcmjfVmJQgVQafJoX1aiKBHAZcuW-SHYsRNPPLGk0-yxxx4Nf4uyF1980ayugZUrV5aU4zwmQe6LcePG-WH1u3Xr5nXq1MkPUX_--eeXlJUQzv7ZZ5_1I1YTobpv375-_o3OnTv79RxyyCHeCSec4Gdza0wu2qQ2ABnQCPl-2GGH-ekEdt99d--ggw7yM8CRNS0plH0SH374oTd37lw_8jLXibwaJHXfbbfdvL333tvr3bu3N3z4cD9K9_z58_30n65U6nrGQTtJCzB-_Hh_2UrPnj39a8k1RbyIOE1-ZSJRR6UkKFdfJm2qWY5EUVngOrOr5Cc_-Yk3aNAg78ADD_TvI9eazIBkJrzzzjudc-uY1EKfrXVKBJDOZnYUV6Nj2ojLUbFo0SL_4ZV1BXb44YcbNf0_ZFoj9wgPe1z-XJsdfPDBfsJyV-LaQEpLOo08l7R27dp5U6ZMMWpNxwcffOBNmDDBOYMds5Q8TK-88oqssoRqXE8bmzZt8s4991yvZcuWofNEGak6TznllFAby9WX81gGw0sMoZHntBnZ83gRZBHCavbZeqGqAki-CHLkynpMGzBggKjN83MRy3KuxtcmicvTEtWGO-64w--ksv44O_PMM0Xt0ZCjhC8WWYeLPfzww7LaEqpxPSV33313Sd5gV5PpScvVlxsjgORKPvLII0PnSmM77LCD9-STT8oqY6lWn60nqiaAN910U-j4wJo1a9bw__v37y-ri3xgOS4YOjNs6tq1a2zWMpL2pMXWhgceeMD_yjL_HUHnrbnLLrvEdrIZM2bIU4Qg4RAPmDwWo26GpAx7GQ7T3i5duoR-D5ZVAMt5PU0QlagXIf_eoUMHP1sew1-G_Gb_CKzWBfDdd9_1h7nyPIGRb5n2MQyNusZ8GS9cuFBWHUk1-my9USKAjPfJ3oWRBc1sPB0w-FuURfkL5I3Az2EOc3iw-Mxes2aN99FHH_k-wbfeessfll1yySWyuoYHllSc-KSuuOIKP6OazR_E8A5fy-jRo_3y8qbSIdIg28D1MIeL-Mruv_9-_y0fwLkZ4vfp0yd0Xo7loYjjoosuCh1He8myZmsrIJr4pfCRBa6FtAJYyesZMGvWrFAdGGJOjmpbNjl8hI8__rifWQ-BprwUwHL15awCiN9UthEhpw1r164tKUsfIuVq0DbT2rRp448K0lCNPltvVGQWWN4I0xg6bdmyRR4Sy4oVK_yUlQimC48--mjIx5U2QXdUG3ibXnfddbJ4CTi8cSrLY5OSqsuvv6OPPtp5mMlEQdJ1qsb1BCYaWrRoEbouLn2Ca3v77bf7L4Uo8uzLWQQQMZNtbNWqVeIECulX8eHKY8lJnYZq9Nl6o6oCOHbsWFm07PA1JH8HXxNJRLVBfnlEQWfeeeedS47t1auXLNYAEwLyXMzq1RpZryeQWF0emzTrn4U8-7KrADKaYVhrHsOQk6-sNGzevNnr3r176DotXrxYFg1R6T5bj1RNADt27OjPblYDZpbN33LeeefJIiFsbcD_5gIznObx22yzTeQXHV9HZlmGmzxMtUiW68lXp_T78XBFXY_GkGdfdhVAvkzN8hiz1i4glrKO4447ThYLUek-W49UTQAvvvhiWaxi8AY0fwuTCEnY2nDffffJYrGwFkvWEfVVt2rVqlDZN998UxarCbJcT4a5sn1cn3KQZ192FcARI0aE2unqagC5ZAX_YdIHRKX7bD1SNQHM0gnygskV87e0b99eFgkh25CmA0o2btwYug5LliyRxXwY-sjZTiYeapEs1_OAAw4oOSZJSBpDnn3ZVQDl8JfZ9CzgezPrwZKGwZXus_VIVQQQx3neMHv8wgsv-A5nQhYxDGPtEn5Gacccc0zJ72HZQRKyDcywusLQQXamefPmyWIN2Gbi-DeGVczWlZNyXk98S3IpxqmnniqL5UaefdlFANmJI-8fvyULLFyWdfFb4qhGn603qiKAjalLsmDBAm_o0KFOuwdsZlvyYSLbwBKCLMh1Vr_-9a9lkQbYYSF_Z2Bt27b1hgwZ4i8f4uHIyy9Tieu5fPnyUHmiNpeLPPuyiwDa1lfOnj1bFksFs-Jbb711SV0s74mjGn223qiKAKadxo_jjTfe8AYOHFhSb2MsaauRbIO5rcgF2ZlYwhEHs6Lyt9qMZRWDBw_2h0oMW1yp5PVk6CbLs3e5XOTZl10E0DZ5wQsmKzvuuGNJXbyo4qhWn60nqiKAWW9EwKuvvmpdJGoagsB-SyL28ttNs20ti1r4GpBXG7J0Joah-NXkb44yfD08HEykpKHS1_Pee-8NlV-6dKkslht59mUXAbznnntC7XziiSdksdRIf6Jtn7xJNftsvVB3AshSEBzJZn0YW6TYOcGDZK5st2Gb2Yp7YCGvNmTtTDiv2YrUr18_r3nz5qHfbzPONXXqVFlVCdW4nviQZHkWVZeLPPuyiwCyy0K2k-grWSFajFkX-4rjqHafrQfqTgDnzJlTUhdG2CaXSQHbAxj3wEJebcijMyGGLEAm7BU7BZL8dXF-p2pcTxZKy_KIRbnIsy-7CCCiLtvZmKE--3XNuuiTcdRSn61V6k4A2Q4mf5frBABxzsw6sLgHFvJqQzk6Ew5yNskTQ862tYwHh5lXG9W4ni-99FKofDm3WOXZl10E0DbZc_3118tiqeClJ_den3766bJYCbXcZ2uFuhNAfFFmXVlilRFQ1KwDi3tgIa82lLszrVu3zhp1hC89G9W4ngi2FOqTTz5ZFsuNPPuyiwAiWnItZ9LMbRT4DuU1Tnpp1EufrSaRAkiUCrPRPXr0kEVSk9eNINKJ7ARp91Sa8ADIeuIeWMirDZXoTK-99lroa8EWz62a11Nu8mfPadoACK7k2ZddBBA4l0v5KC688MLQNSZydxz11GerRaQAXnDBBSWNJmRVVvK6EYTIkp3A1XlOGHdZB5b0wObVhkp1Jhlle9iwYbJIVa-nFBKMQJ3lIM--LH93kqD94Ac_CLXz6aeflsViYaJKzrQTHTzJT1tvfbYaRArg1VdfXdJoovVmJa8bwReCWQ82ffp0WSyWqIi8SQ9sXm2oVGci9pt5HttOi2peT9YqsrHePIaZ5yhfZWPIsy-7CqBtMXTS8hWJzceaJpJSvfXZahApgLYwRzh1s5DXjQC5FICcFGkh0KdsU2BJD2xebUjbmVibF7eYOA6CJkjf0-TJk2Uxn2pdTzjttNNCxxGJOe-hcJ592VUAgSCz8vwEe00D_YBw-OaxRNFhIimJSvfZeiRSAIn8Kh8iwtOn6diSvG4E2B6aiRMnymIlMKtpi65sWlK78mpD2s7EA8IwBwd-2gXNwBcUawVl-2TU4YBqXU9gryxh0eSx9DOyr6Vh_fr1flYzUixEkWdfziKATGDIvc_8d1KIeUKi2ZIn2b7mbVS6z9YjkQIIcokExrCFFHpcXOKamTZt2jRZhU9eNwJWr14d6kwY2-uIShIMoYhoy_YuhnTktDDLsodWHp_0MOTVhrSdCQE0y9GGSZMm-eGMmOQw99oymcFQi4eT3BKybSNHjvykYkG1rmcA4fXlHleM68SyHtYHEgKe9uLzYujMOkLScvIbg8mepCCfefXlLAII3Dt5fozJIPbWMntP-7huCCa-Q9lXMHyBaSO6VLrP1iOxAkjQSumnibOoRDJ53YiApP2x_GbbQ42NGjXKeecC5NWGtJ1JCqDNaGfS_cEXmNS2alxPE_bHuqb8lJYkgHn15awCyFfzmDFjQudxMdwVMv1nHJXus_VIrAACndv2VWGzqE6T140IYFZMJrpJYziO6YhZHti82pC2M6URwCQj5HwaP2I1rqeE0Fsky5L1pLWkNXGQR1_OKoABJEK3ffEmGX5EW4KoOCrdZ-uRRAEEhh98pvO232-__XynrC11X1SnyetGSPhNcnmAzVgYbEbhyPLA5tWGtJ2JYS1DUPw9chN8nDEkJCIzx7pSyetpg2H2LbfcEhpiRxlCwjCYYBFx4bdMGtuXGyuA8PLLL_tZ4mRfsBnLmbIuD6p0n61HUglgLcNDg08IpzyZzY4__ng_Ego-FAIBpJktqwfefvttPxDqVVdd5Z111ll-qHUeUtrK3l32BRNlZcOGDfJQJ2rleuL3u_HGG_0JmeB38EDzpcqMNteiHEtmKglBJvDpksKUdp144om-MLNwGx8kM8BKeal7AVQURcmKCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSxlFUBWrrNw1LR6X7tVq7Cn1rzOacNaZT2uHqE_PvDAA_4um1_-8pcl7WbNoVI8yiqAzzzzTGhlOwtclfzJukMh63H1BDspDjjggFBfNI0900rxUAFsImQVsqzH1QPscWZnheyDNlMBLCYqgB8zc-ZMf69kYGw3qyeyClnW4-qBSy65JNT_okwFsJioAH5MnpnDqkFWIct6XK3DPtvWrVuXtI3AB0Sx_uMf_-jHVKQvBkZ-FKV4qAB-TL0L4KWXXurH7Atsr732kkWsNFUBxO9ntosw8oTcUhQTFcCPqXcBzEpTFUCZq9gl14lSHFQAP0YFsGkJ4LHHHlvSLsLcK4pEBfBjVACblgASKNVsF_EMFUWiAvgxKoBNSwBlKsozzzxTFlEUNwEk3-yvfvUrP8MWC0s7d-7sh-weNGiQH0F4zZo1JeXzFMDNmzf7GcJI40hi6R49eviJtAlrzn8TRZfQ7GTWSsuyZcv8YzCi8Zq_k9Dwwd-ijLSFSRBh-dlnn_UjORO5uW_fvn7uC65dt27d_AeV8OhkOXvuuefk4akhjaT525566ilZxEpjBfDDDz_05s6d6_vcCMW_7777-veFBD70jd69e3vDhw_3I1bPnz_fT4VZDsikZrafc5vtInq2-XfTbPdx5cqVJWXoKyasMeTfx40b57ebe9mpUyc_nD9JptJA32AnDnlCeIZINcB1o3-QLY6seHfeeWeqvC42ktrA-YmszTNFP-zSpYufhvOggw7y_23JkiUl5W1Qx0MPPeSdfvrp3qGHHuqnb8D4_3x1p6mjmqQSQMTnjDPOaEhBGGX8nbDlhG-HPARw06ZN_sMl8xJEGcJy2223-R00Cdb7yeNdLCpvBCJMTg4efLkUI8lw1j_44IOyykSyClnW40jNOGHCBOdsbsxQ83C7ZDdLQ9pkRzaz3ce4fBqLFi0KCaxpvJCT4KVhy_lrM_r--PHjnYUwqQ3ca3kuaYh71DNLwvnu3buHjpE2cODAyDqqTaIAsl6Kt5JsVJwhQuSbbawAki-hVatWoTrSGBnR-DqJo1wCSI5eWdbV-LIg41pasgpZluO4h2mSJ8UZD0-eVEoAL7_8cn9JjazDtAEDBojaPoH1iUceeWTomDTGOsYnn3xSVhlJVBtIIZr0MWMa1xYdMKHfJF0H09AQl2e_UsQK4Pr16yPfUuRY5VOdIR1vAZnqjwbzaSyPS3sRSHMYdZNatGjhP4AMGfjf5s2bh8pgfE3FiWClBbBZs2YNw6SePXt6Xbt2tWYkC4yv7rRkETJwPY5sdVFfDnypMBRk2MuXA21kWGXLKVyPAnjTTTeFjg2Mexv8__79-8vqfN59912_z8pjA6MN-J4ZQkb1i5YtW3oLFy6UVVuxtWHOnDmhOnl2O3To4AtslKjhagpeyLwE5N9pf_v27b0dd9wx8rllWJxmZFZJYgWQoYpsBBeJyBm8yUzw7bDKftttt20oa8vzmkYAyW4mj-Oi4qfDp7Bly5aS8gzRGfbysMnj8LtFQepGIoRgMi8uW6OCv0VZVOrHQAD5zfhWuC58DdtSNzJcxg80evRoa8chekkaXIUswPU4fL3yN9JGfEm29gGiiU-S7GfB0DFvAdy4cWPJvZFCQ2Y5ef_i7qMUD_oy4hP8Ny-vKVOm-H7vjz76yH-w2U2C64MteDbw9cprh3Dgv167dm1JWZ4v0n3ywpTHtGnTJtVzJNvAi9d0WZBpD9-g6TfHfUV_tbk2rrvuOj9joPlC45mUdeC2iqqDtKe1RKQA2t52fOklbRmiQ_AmkMcGlnTjcOZzg81j2rVr539NJoFfCmeyPGeaN2aes8ArVqzwHzg5KZTEo48-GvIZMqmQBlchC3A9Tn79MSHmMlSHRx55xPnauNLYWWApHqbhnpAv4SQQM1kP7p2kySrCx9k-RFjmk0RUGxgxMbkSB0Nt-RXKvQ98fvwNF1UcTExJ332vXr1ksapiFUBmduSbh5v1xhtvyKJW-AKSQ-LAkgRQ3jQuNBcyLXxtyMTadKAk8hTAxsCXkbxmvHWTcBWyAJfjeLPL38ZMYy1SLgEcO3asLJoIX4cyuT1DTSYi0sAIxzbZsHjxYlm0hKg2zJo1Sxa1cs4554SODYzk8mk4--yzQ8fykVMrWAWQWUj5oxn3uyC3IgUWJ4D8TQonwyZXGCbL8_JVFketCCAwi2j-lvPOO08WCeEiZCYux7FcxCzLkL3WfDoB5RDAjh07-qMMV3APyLpcd6YglrKO4447ThYrwdYGfLNp4StdHo-Zs8lJvPTSS6Hj77rrLlmsalgF8OSTTy75wfg-pM8vCb4WbQ7VOAFkrZhZlskO3n5ZkP5H1uHFUUsCyCyd-VvSdFoXITNxOW7VqlUlZTHWhtYi5RDAiy--WBZLxYgRI0J1ZXEBsD7PrAP_YZwg29qAj9IFJkdkHWlcSiZMjJjHs-6xVrAKoJxMGDJkiCySCmYD5cWLE8A-ffqUlLXNzqWFDm_WhQM6jloSQDqp-VvwqSbhImQmLsfxMjJnOzEmb2qRcghgFtECOfxldjwLrIyQvyluGCzbwOgqblWEjX79-pXUgU-PSR8XpA6ceuqpskjVCAkgU_XyIrNLIQss3pR1RQkgF1U6XQnxlBXZWfgijKPcAkj7CMeEM5x2MazlocSnJO2YY44p-S1clyRchMzE9Tj5ksL4N4Z5Lrtwyk3eAsjkVBZYHSGvF30tC88__3yoLu5fFLINSc-ADRlUguUwrgwePLikjpNOOkkWqRohAWTblrzIv_vd72SxVMyePTtUV5QA2nwF7KSYPHlyiV122WUNhpCYxvKDwIYOHVpSF2us4iiXAC5YsMD_LeYSiiwWtcQkwFXIAlyPs_mHA2vbtq0_WmB5CA-r6-xwnuQtgFn7g21NKM9FFph5lj5ylm9FIdvA15wrso6oNY5x0CfMOnjB1wohAWSJgrxhdOYs2B6WKAFkplOWzdNYuB1H3gKID5QtQPJ3ZLWkbVCuQhaQ5Tj2usrfZzNWDvD252ucdXqVJG8BTLPsxIZt8oKXYlakP42XaxSyDS6TFwGyDpY9uSIFMEsd5SIkgPfcc0_ohr366quyWCpYviLrihLAefPmhcrmaSzejCNPAeR6yWVE0hAHdtkQuZlzmWbbZmZbrGuSRcgg63EM5ePWe0rDd8jDykRKJchbALOIB9ieJ5dlXRLpT4zbd5xHG2QdWcSrrgSQxY3yhmV1_rKwV9YVJYC23R_bb7-9t9NOO-VilRoCsywEJ7dsCxFS2EWxdOnSxBl1VtbL42tNAIEZyBkzZvhDq6jtiNJwok-dOlVWlTu1IoBEMJLX4LHHHpPFUiP35bOvOIo82iDryCJedSWAzCrJG4ZfMAtyNhOLEkCbWKZZAJwXeQmgba8l2_FcJghsX8O1KIAmiCGLuFnKxMLzJJ9nVj9YWmpFAG39mrBgWWFXlFkXvzOKPNog68giXnUlgMxUyhvmunYoYPr06aG6ogSQhcqybCX3DeYlgNxcWY_rZMDNN98cuha1LoASHPasFyOmHes5ZXt4kNnmVS5qRQCXL18eavv1118vi6WCl4zcL04cvijyaIOsI4t41ZUAsk5IrvVi6JYFlnSY9WBRAsh55b5Bl2gojSUvAZThu5gRdcW2i6beBNBk3bp1oeAEGF_L5aJWBBDRks9T3MxtHDafOhNMUeTRBllHFvGqKwEENuCbPzguvlkctqCRUQIIhNYyy-I3qxRE5DDPTcRpV9iHLNubdr-nCeIr66lnAQTiycmvF1dRcqFWBBDoS3lc4wsvvLCkHizOPZVHG2QdWcSr7gSQLy_zBzODumHDBlksFttQGosTQFuoJZzIleCCCy4oOS_hjlwhUo78_fiAXCAsvqwDq3cBBPlCHDZsmCySG7UkgISGN-vCnn76aVksFibX5OoAwk3F-ZbzaIOsI4t41Z0A2hZDu3YgtrHJOrA4AURApL-IKBhx-x3z4uqrry4573bbbSeLJILfS7YXP6gLUdGCm4IAEmPRPFc5t0TVkgDaFkPHLV-xYfMLJ0WmyaMNso4s4lV3AghyGIYfgyUcabj77rtDNyuwOAEEm_8LMXWNv2aSJtmQLQwVDmxX5DIFl4TcBJGUvyGwWhBA1jcmLciOgqAJ0hfGzp5yUUsCCPL3YDfccIMsZoXrTiBi81gCjbB7Ko482iDryCJedSmArEWT0VzY6kT04jhYwiH39JqWJIA86HKxJ0YgRZf1iGwdY_jMCv40e2nZAy0fULb9JAmPhGxa8rdPnDhRFiuBWWLb8N-0pN_hImQmLsfxwDLsYsLIZUEzs71yUz0moyDniRScagsgExgyNQD_zTrKOAhBZktLkebrOY82yDqyiFddCiCwhEFeeG4a69oQwiCyBFFC2C8s99_ahnNJAggsiTFD65vnJow3wwGSLr333nu-b4SFxcw0ssCUsFf8DoawwXHMLqdBLmHB2EJ32GGH-R2BGG6mTZs2TVbh_y7Z0TGEmOVEwdIPgs6yXY4hsgzgKjsMVisCaJbld0-aNMlfPM8kh7lfmQkhhn7Ub8vXMXLkyE8qLgO1JoDAtZLXAWPdJAFG6cP49LjXCCa-Q7kyAsMXmMYtlEcbZB1ZxEv25yx1lItYAaQT8-DKG2AaAiH_DUM0bNP2aQQQCBVue3CyWFoBRHij2mOzqHBdSXtlOYdNJLFRo0bV7E4QKYA2o21J1xBfYFJ7GkstCiBf-mPGjAldDxfDxZI2pWgebZB1ZBGvuhVAyJLGj-EOvqLGpsVk5vmII44I1eFqafNqAOKTVnijBJCvUplkKY3h1OYhqWcBTDLSlWb1I7pQiwIYQEBQGdUljdEmkjilJY82yDqyiFddC2AAw05CgsubYhqRKnDkBzsfGiuAAQy3eXDifIvSCDJAPgJ-gysM5RiS8DVG_DMc0LZzRwlgAHXIpQs2Y5GwGSGkVgWQEQHDePxPNj9tlLH-j6jWWXcUZaGWBRBefvllP0ivbYgrjeVDd9xxh6wikTzaIOvIIl5NQgCBLxvWtf385z_3vvvd7_r-OMJ9k7eDB9g1UqwrPICE6-KhZbaYcyNC-JNYu0jeEgJzurwlyw2-PvY0M8lBpjiuGT5K_DsEBUiayatlSKHI9cbvetZZZzXcD9qHn5h9wQS5cF1DWiQYYeFD5Rli1ECaSV68LMzHx5w1EpOSDicBVBRFaUqoACqKUlhUABVFKSwqgIqiFBYVQEVRCosKoKIohUUFUFGUwqICqChKYVEBVBSlsKgAKopSWFQAK8jMmTP9_ZiBsX1MUZTqoQJYQfLKPKcoSj6oAFYQFUBFqS1UACuICqCi1BYqgBVEBVBRagsVwAqiAqgotYUKYAVRAVSU2iJSAFeuXOmHZg9s2bJlJX8n-vNdd93lZ4476KCDvC5duvjh1EmiRMh0IjcTDTkPqIew-ORSGDRokB9CnuQw--yzj59Ri99w55135pZrgmx3c-fO9aNOE8qdnCK77rqrf07Ck_fu3dsbPny4H_F4_vz53jvvvCOraIDrFlxDov2aAki4fPMa24y0iDaS7g_XjGjNpOkkPDz3h_SK3Cv-bcmSJSXlbVDHQw895J1--uneoYce6ofBx_j_RLROU0cc1P_ss8_6EaWJIN23b1__nnbu3Nnr1q2b_7sJG3_llVemyu0cR9L1ArIKkkaBhF60M7heJ510kp8SIiktgVJ_RAqgzAVg5hMgP0GHDh1K_m4zOtHixYuNWt1BiGx5UW1GfoXx48dnFkJSDU6YMMHPfSvrjjMyvCHEtmxdXDdZ3sWi8o7E3Z9Fixb5LyNZlzTEPSpHC4niu3fvHjpG2sCBAyPrsEHaR3KD8AJp3bp1qL44I8n8gw8-KKtMRdz1ev75532hk-eT1q5dO2_KlClGrUq94yyA5557bqhjxBnJ1S-88EJRezJZstEFRhKjJ598UlYZCw9xmgRGcYZoSCotgNdcc42fhEjWE2VkwCOnrwk5V7hvsmyU8WWcVgTJFSyPd7Vx48Y1JN5KS9T14mWeJjGRaa4JlpTaxUkAyfgmO0P79u39N3OvXr1i00leeuml8hSRvPvuu_4wV9YRGOfBf8YXpi1bG9ayZUtv4cKFsmorJFuK-mLi4WA4xrCXL6aePXv6w0lbXt9qC-CcOXNCx5N-ka91XgpRokbmu0BQSCwl_96sWTP_PpP1L0pcGRaTNCuJKAHkHJ06dfKTrXONu3btGnlvMZJguWC7Xg888EDoPnKN-NLbZZddYoVxxowZ8hRKHZJaAPk6at68ecN_H3744davLHw1xx57bKjD0LHIKJcG_D7yeB4QMmWtXbu2pCxfirfeeqv_8Mhj2rRpk-rLhIxt8lj8T_jQSJFpA9EkeTvZvPALcoxNAPEbkaUOk7mCSRAe_C3KovxO8v4gHObQnexz-LoYcgaQxY2XmG2If9111_nZ60xBwGcp69i0aVNkHbfccktDuSgCAURIucbURepS23XmvPh-R48ebRVeBCwt8npx7c0hOP7H---_3-9PAZwfd0KfPn1C5-ZYXtRKfZNaAE0777zzZPEQl112Weg4vrJsHd0EMZPHtWrVyhebON5__33fDyePZVImCfn1R95S1yEWkz5r1qyR_1xCnrPAUfeHlxQTQnHw4pJfV1yDwOfH30jVGMcTTzwR-kJiFJDEihUr_PSgSddKwstT-gxdEt5HXS8EH_GPg8kaJkLksddee60sqtQZzgJIR0iL_OLBbrzxRlmsAYZQMuE2X468hdOwefNmq-M-biKGLxpZnhnDclAJAZw1a5YsauWcc84JHRsYCd3TwIypPPb111-XxXKDL2x5Pr5a0xB1vfCZpoEX7M4771xybBrBV2obJwFk2OOSdJzZWHxPZh3MtkXBkFOe85RTTpHFYkEsZR3HHXecLNYAy0zMsgy10viyslBuAcRHmRa-wOTxmDk7mgRJ3eXxLI0qJ7hezPOlGY2A7Xrh13VBTgBus802ziMFpbZwEkDWarkiOw0Wle1-xIgRobKuQyWQSxrwH7LExcaqVatC53zzzTdlsVwotwCyvMQF21KmtBNHAUyMmMezVrOc8MVmni-t6NuuV9IwX4I_VNZRrtGCUhmcBJAO4MoLL7wQqofZShty-MtsYBbwzchzRg2DGTYjkGZZnO7loJwCyGwvC7hd6NevX0kd-PRY4O4CX1FmHSyCLyeIvHk-ZqfTIK9X3Esxio0bN5bUgTV2MbhSXVILIENDc4YsLTiQWZJi1mULBMpuCtm5EIwssLBV1sXatihss3z8G0Nycwa0sZRTANlB4YqcrWc5jCuDBw8uqcPFRxyA6PKiZAKM5VIMa1lrN3bs2JAdc8wxJedjwiYN8noxc-8Kw12zDmzevHmymFJHpBZA1r5lRa7pY5ZVYlsfNnv2bFksFVu2bPG_iMy6mJCJgt0F8tyBtW3b1hsyZIi_AwBhbYzPp5wCyNecK7KO_v37yyKJcG3MOhCotCxYsMAbOnRo6AXpakkrC0C2lWUvWZAz32knjJTaJLUAxk1eJCEXA_N1JbFNXvCAZEX6pnjQ4jj__PND57cZS3L46mGYzZDIhXIKoMvkRYCsw_ZiSkIKYJo63njjDX8Lnby2WS3N1kfZ1izXC6QA3n777bKIUkekFsABAwbIIqkZNmxYSV0s2pXcc889oY7NWrOsSH8is4dJMATDpyR_R5ThR0JYmUhJgwqg50-A2Ratm8ZLhv3fe-21l3-NTLNtV4xaLG4i25rleoEKYNMitQCyyDgrMgpKjx49ZBF_Fb7s2ETnyAr7U8262FecBhzjbHNiSGnufIkzHoqpU6fKqkIUXQBZXsTElrx-RNphN87SpUsT_cy2mVgVQCUrqQXwK1_5iiySGjncse3OYKW_7NiEmsoK-znNumiPK4ghi28Je8ULIMlXleSzLLoA2vYqs7TKZaKJSQdZhwqgkpXUAsjm8Kww5DXrsm3wX758eahjX3_99bJYKhAuuXeUmHaNhckV1skRf7BFixah34vosmMgiqILIH-T7XedVCIun1kHpgKoZCW1AGJxgT-jsM3ITpo0SRbzRUuux4ubuY0D36H87Xnv21y3bl1odhuLWuMIRRdAfHtm2Syx9QhSa9aBqQAqWXESQCYqXGEBsqwHf58NfINmOTboZ4H4g_KcRB7OG-LoyS_NuFhxRLMxy9p8oWmR9yfLAy3riBOvKNIKINFzzHJY2j3eJrw0ZD0qgEpWnASQEEuuEPnDrIPoG1HLRwizLs_59NNPy2Kx4GiXM4XsYXbxM7kQhMIKjBnvKC644IKSssS8y4q8P1keaFlHlHjFkVYA33rrrZJyWNrwaAGEWpN1YCqASlacBBDxwleXlj__-c-hsEtHHXWULNaAbTF0muUrJjYfETsIygVx5cxzxW0Fu_rqq0vKbrfddrJIauT9yfJAyzqixCuOtAKIK8Qsh02fPl0WiyUqQrgKoJIVJwHECAGUZuU9X1ysHZTHJ83sEiRTHnPDDTfIYlZYYyajzxBOi6glUXBMmoW0NgiaIP2WkydPlsUasIVzcnmhmMj7k-WBlnVEiVccaQUQ5NIkIomnxRaNPDAVQCUrzgKI0cnjZjvZlC8XP2O25S8SJjBkmHL-OykEOWGtbMmT4r7IAHFliMwERdoFzUD7ZTABTEasNiGCsBRMtp-leYAl8v5keaBlHXHiFYWLAJKNTl6viRMnymIlMEtsi9htWprrJ9ua5XqBCmDTIrUAMuNprq3r2LGjP6RjWxMBD_C9rV-_3o-uK3dhYMROSxvaillieTzGWjz2XjIDyxcmHR_BxHcoOyaGLzAp4gcCaB7Dkh3OT6gkJjnMr10c-QzTCaxgy38ycuTITyqOQC4Fwbg2pGLkmhP_0LRp06bJKnzk_cnyQMs64sQrChcBXL16dejlhvFiJMpL8FKlP9GvGCLLJVTyfJgKoJKV1AJIh6GT2jowXzVyqYtp_M0lVh1v_TFjxoTqcTGGW7Y0lRIpgDZDoDD576bhC0zzIBISPqku02xrJsF2f1yRdcSJVxRSkJLqSNpzzbWx9TFs1KhRuhNEyRUnAQS-wGQniDPWfrkGngwguGacsEYZfsS0kavTCGCSMbHj4kfkIbZ9QdqsqQkgIwVbqoQkYyKLF6MKoJInzgIIfMXI7W3S-CpkDzDD4sbw8ssv-1niZMezGUtSyPPqAsNavk7xFdqG7lHG-j-iEbt82ZowtOZlwlcNcfiYvJEz5lhTE8AA2i6XK9kM14sZFUgFUMmTTAIYwAwqPirezjwITHyQtJqvKlIw5gmb5PmSJA0lXxCIK-LB4mJ-Q1SYfVf43QRCveqqq_zArYTpR4SI-sK-VfYF33vvvd6GDRvkoYoj-PpIasQkB-tFWWfKdcanS3CJuNl7RcmDRgmgoihKPaMCqChKYVEBVBSlsKgAKopSWFQAFUUpLCqAiqIUFhVARVEKiwqgoiiFJVIAWQDMnszA4uL4KYqi1CORAqgoitLUUQFUFKWwqAAqilJYVAAVRSksKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSwqgIqiFBYVQEVRCosKoKIohUUFUFGUwqICqChKYVEBVBSlsKgAKopSWFQAFUUpLCqAiqIUFhVARVEKiwqgoiiFRQVQUZTCogKoKEphUQFUFKWwqAAqilJYVAAVRSksKoCKohQWFUBFUQqLCqCiKIVFBVBRlMKiAqgoSmFRAVQUpbCoACqKUlhUABVFKSwqgIqiFBYVQEVRCosKoKIohUUFUFGUwqICqChKYVEBVBSlsKgAKopSWFQAFUUpLCqAiqIUFhVARVEKiwqgoiiFRQVQUZTCogKoKEphUQFUFKWw_B9FTUkADrx2aAAAAABJRU5ErkJggg\"}]}]",
>   "fidoAuthenticationResponse": "[{\"header\":{\"upv\":{\"major\":1,\"minor\":0},\"op\":\"Auth\",\"appID\":\"https://example.com\",\"exts\":[{\"id\":\"com.daon.capture.edek\",\"data\":\"ALnaVOLAKy_woNCp-DLwwrwGGKKZjahZ83gS-nw9S-i_RCWuKKzDebZIVavvTEAS9_s6dobKQkRSIuz8E5SXMKUGYfy8nYPvPZK_5xqHXdjOxFK6ffATgSnlXz-HcmK3sEi6fV3N9LwAyU_Pg9NqoCnIWcAY9Y5kcC0q82YYEQJvhqu6jyGgqAbBPJREiGLFYFyLoO_arXTQPyz-xhNjuGpCcZIZhYi50QEdL3-tV8NdLYAQDRPHnwWYheSATg4Q6rDzzC-QTdj7X6OFldf-Z79H5yQQQmKzH69pL0Uv2pCifo22u4f-xeDlNwABtqJ91HHbRnzkJyb3lGg4brj6Tg==\",\"fail_if_unknown\":false},{\"id\":\"com.daon.capture.iv\",\"data\":\"e3hxRsGyxR_wJfM-F94Mwg==\",\"fail_if_unknown\":false},{\"id\":\"com.daon.capture.schemeId\",\"data\":\"CDEM1\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8201.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8201.recognition.timeout\",\"data\":\"7000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8401.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#8401.recognition.timeout\",\"data\":\"30000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9201.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9201.recognition.timeout\",\"data\":\"7000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9401.ados.mode\",\"data\":\"enrol\",\"fail_if_unknown\":false},{\"id\":\"com.daon.D409#9401.recognition.timeout\",\"data\":\"30000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.authentication.reason\",\"data\":\"Authenticate with Face ID\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.embedded.ui.enabled\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.liveness.active.type\",\"data\":\"blink\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.liveness.enroll\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.registration.reason\",\"data\":\"Register with Face ID\",\"fail_if_unknown\":false},{\"id\":\"com.daon.finger.authentication.reason\",\"data\":\"Authenticate with Touch ID\",\"fail_if_unknown\":false},{\"id\":\"com.daon.finger.embedded.ui.enabled\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.finger.embedded.ui.reason\",\"data\":\"ui-reason\",\"fail_if_unknown\":false},{\"id\":\"com.daon.finger.registration.reason\",\"data\":\"Register with Touch ID\",\"fail_if_unknown\":false},{\"id\":\"com.daon.finger.sdk.locking\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.identityx.version\",\"data\":\"5.2.4.0\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.ados.decChain\",\"data\":\"[\\\"MIIE6TCCAtOgAwIBAgIRAJEmGK-0XEGFin4brMpnidIwCwYJKoZIhvcNAQELMEcxFTATBgNVBAMMDElkZW50aXR5WCBDQTENMAsGA1UECgwERGFvbjESMBAGA1UECwwJSWRlbnRpdHlYMQswCQYDVQQGEwJJRTAeFw0xNzA2MTUwOTQ3NTFaFw0xOTA2MTUwOTQ3NTFaMFoxDTALBgNVBAoMBERhb24xEjAQBgNVBAsMCUlkZW50aXR5WDELMAkGA1UEBhMCSUUxKDAmBgNVBAMMH0RFX0RBT05fQVVUSEVOVElDQVRJT05fREFUQV9LRUswggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQCXrHT7hGCZR4KzlwawZl3yefpUov44BWofCNnuGh3RoaQ63vXX6jsrfoCVJdto5a38Nd7ckQzjhtuoAfLeUT3sbm7uhXCCoC5xJ_B96G6LeTvY6yZ2ZsO3K8dOl8epKOI7e2Xh_3WQg0xa21QmJxnTcMSMj0TMHrXlb66nh-CoTbAcKopm0xbrPfOMLoZ1xGk7iOVxSY_TRjep6tn4Z7t7r-bsJnDjJtctto4gYXk7mDkwdAMfBpoq1Jp0nGbv8TCMySAjOUSs9ptE7pRl5No6iF4QYNDDUUhI9q7MAcpSgEYLaAPzhZdzZnmDfwwOIPCiss0qKV9L3H6wh-NLQ_r7AgMBAAGjgcAwgb0wfgYDVR0jBHcwdYAUZplSSlDw67i7wEa-1wVzqzvdL5ahS6RJMEcxFTATBgNVBAMMDElkZW50aXR5WCBDQTENMAsGA1UECgwERGFvbjESMBAGA1UECwwJSWRlbnRpdHlYMQswCQYDVQQGEwJJRYIQKuhll9ePQGSsywpelEVwazAdBgNVHQ4EFgQUyeJ8CGmnhFk5Cs0c6TEEG2GrL08wDAYDVR0TAQH_BAIwADAOBgNVHQ8BAf8EBAMCBLAwCwYJKoZIhvcNAQELA4ICAQA-cpJUeOAz96VXYHqIS_yRkltsSkLvmgqwuwx2fShZJQ1pawaRf8qWH9takyyBzAPNVMYsxIc4eMF4qRhExtADB5EQBFF-DWVMoLymYOLMDHii9lnuYdsV0B82EsQu5U7SccuDH3ffNOlVJq2NS8jHUFm7GxF36O6BdojT3vXgHmH_dZo3GzGCRDpkKt_gUAO1aj2Ga1YmLcd2ptA6OA1SllW0eWS5yb_KNscCVVQke2gvJkACHrsIel7AxNBgukWlTANCrgH2UOhhhXlOmu3RRoxhUL8Ya5V7qSdiVZzmfMZwRpyX92FbGUIb_lL9nlFs3iGtE9gXE-DVTNs93jn_XIK0Q8D6lcvpVtI4bJQhUJ7u78MeoSPuYx-9SX4ioiNmVVYC6fdAieSG1ggEiIhw0U8l-4u1pItyPIqwt_OijaElOouTWzeBa3AJA7CqasOZoMx6BXJE5dLcILbpYduA0vSc3em6cr-LJgRr7uuvQCJ-3pGX_gipMyailXYd2S985PQXsyKEW5AegBcEgNX3MIvNPUhb2eS-Ab_JIZbQGAUGTT_HwQXFB08pMXJ-UK_FwdphXVGMJy9jmyvwWLlBFXyYGrAiq0pLlkHexCqHcjYbchgf1IDIwp0yQ3KcoA42w555djBN7hFHTa9dfAdTOHRKlICG_PhsMUdhZ_T7oQ==\\\"]\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.ados.dekId\",\"data\":\"1000090661\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.authenticatorMetadata\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.deviceInfo\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.envCheck\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.healthCheck\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.keys.access.biometry\",\"data\":\"false\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.location\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.response.deviceInfo\",\"data\":\"{\\\"deviceId\\\":\\\"85F60EE0-E6B9-46EB-AD5A-A714AEFF3462\\\",\\\"make\\\":\\\"Apple\\\",\\\"osVersion\\\":\\\"15.4.1\\\",\\\"model\\\":\\\"iPhone 12 Mini\\\",\\\"sdkVersion\\\":\\\"4.4.0.24\\\",\\\"appId\\\":\\\"6FE23CA3-9F8D-4BE5-AE59-8B4D5B10F81E\\\",\\\"name\\\":\\\"seaPhone\\\",\\\"notificationToken\\\":\\\"1976b4665f3b9bce4c4342999ec2acb290da4a3896d800a32b1232892863c084\\\"}\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.response.envCheck\",\"data\":\"Passed\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.response.healthCheck\",\"data\":\"true\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.response.location\",\"data\":\"44.667134,-63.567784,1651058684217.362793\",\"fail_if_unknown\":false},{\"id\":\"com.daon.sdk.version\",\"data\":\"4.4.0.24\",\"fail_if_unknown\":false},{\"id\":\"com.daon.status.D409#2204.NDRBQjlGQzQtNUYyNC00QTA0LTk0NjMtMURFNEI5MTBEQ0Y1.reenrolCounter\",\"data\":\"0\",\"fail_if_unknown\":false},{\"id\":\"com.daon.status.D409#2204.NDRBQjlGQzQtNUYyNC00QTA0LTk0NjMtMURFNEI5MTBEQ0Y1.state\",\"data\":\"AVAIL\",\"fail_if_unknown\":false},{\"id\":\"com.daon.status.D409#2204.NDRBQjlGQzQtNUYyNC00QTA0LTk0NjMtMURFNEI5MTBEQ0Y1.unlockCounter\",\"data\":\"0\",\"fail_if_unknown\":false},{\"id\":\"fido.uaf.safetynet\",\"data\":\"null\",\"fail_if_unknown\":false},{\"id\":\"com.daon.authRequest.retriesRemaining\",\"data\":\"5\",\"fail_if_unknown\":false},{\"id\":\"com.daon.authRequest.maxAttempts\",\"data\":\"5\",\"fail_if_unknown\":false},{\"id\":\"com.daon.user.retriesRemaining\",\"data\":\"10\",\"fail_if_unknown\":false},{\"id\":\"com.daon.user.maxAttempts\",\"data\":\"10\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.face.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.voice.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.voice.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.passcode.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.passcode.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.otp.retriesRemaining\",\"data\":\"3\",\"fail_if_unknown\":false},{\"id\":\"com.daon.otp.maxAttempts\",\"data\":\"3\",\"fail_if_unknown\":false}]},\"fcParams\":\"eyJhcHBJRCI6Imh0dHBzOlwvXC9leGFtcGxlLmNvbSIsImNoYW5uZWxCaW5kaW5nIjp7fSwiZmFjZXRJRCI6ImlvczpidW5kbGUtaWQ6Y29tLmRhb24uZmlkby5zYW1wbGUucnAucHVzaCIsImNoYWxsZW5nZSI6IktjZDJ4WUx5ZDFod1B3Uldkcm9oY3cifQ==\",\"assertions\":[{\"assertionScheme\":\"UAFV1TLV\",\"assertion\":\"Aj4pAQQ-4QALLgkARDQwOSMyMjA0Di4FAAQAAgEADy4IAEy_Boox0eJBCi4gAJk_6zJweHGVDWIahD5EZYDetzyd82MEdHvDFqFEtIE3EC4gADK9bO7JZ-V1snweynF3csizuEQayV3mdpcqwW8L_2kkCS4kADQ0QUI5RkM0LTVGMjQtNEEwNC05NDYzLTFERTRCOTEwRENGNQ0uBAAAAAAAEj5DABMuGwBjb20uZGFvbi5zZGsuZXh0ZW5zaW9uc0hhc2gULiAARz18jrN1ZwiM9oxH7ziEhMPRzNh8NtLepJ4-MThdwAEGLkAAEGJ3BBXgGWcPtanbkZ641WHOMfHLFLC7hFJxvqrmc-0-bhVraMqgynDSX-Rt85E1v2_qIxY0ze4AL-QX9kYvbw==\",\"exts\":[{\"id\":\"com.daon.dataStoreType\",\"data\":\"OS\",\"fail_if_unknown\":false},{\"id\":\"com.daon.embedded.ui.reason\",\"data\":\"Verify your face to continue authentication.\",\"fail_if_unknown\":false},{\"id\":\"com.daon.info.time\",\"data\":\"3000\",\"fail_if_unknown\":false},{\"id\":\"com.daon.keyStoreType\",\"data\":\"HardwareOS\",\"fail_if_unknown\":false},{\"id\":\"com.daon.token\",\"data\":\"1651058688715\",\"fail_if_unknown\":false}]}]}]",
>   "fidoResponseCode": 1200,
>   "fidoResponseMsg": "Successfully Validated Authentication",
>   "status": "COMPLETED_SUCCESSFUL",
>   "deviceStatus": "{\"version\":\"1.0\",\"authenticatorInfo\":{\"D409#2204\":{\"registrationInfo\":{\"deviceInfo\":{\"appId\":\"6FE23CA3-9F8D-4BE5-AE59-8B4D5B10F81E\",\"deviceId\":\"85F60EE0-E6B9-46EB-AD5A-A714AEFF3462\",\"make\":\"Apple\",\"model\":\"iPhone 12 Mini\",\"osVersion\":\"15.4.1\",\"sdkVersion\":\"4.4.0.24\",\"name\":\"seaPhone\",\"notificationToken\":\"1976b4665f3b9bce4c4342999ec2acb290da4a3896d800a32b1232892863c084\",\"location\":{\"longitude\":\"-63.567784\",\"latitude\":\"44.667134\",\"captured\":\"2022-04-27T11:24:44.217+00:00\"},\"healthCheckPassed\":true,\"environmentCheckResult\":\"Passed\"},\"attestation\":{\"form\":\"SURROGATE_BASIC\"}},\"authenticationInfo\":{\"deviceInfo\":{\"appId\":\"6FE23CA3-9F8D-4BE5-AE59-8B4D5B10F81E\",\"deviceId\":\"85F60EE0-E6B9-46EB-AD5A-A714AEFF3462\",\"make\":\"Apple\",\"model\":\"iPhone 12 Mini\",\"osVersion\":\"15.4.1\",\"sdkVersion\":\"4.4.0.24\",\"name\":\"seaPhone\",\"notificationToken\":\"1976b4665f3b9bce4c4342999ec2acb290da4a3896d800a32b1232892863c084\",\"location\":{\"longitude\":\"-63.567784\",\"latitude\":\"44.667134\",\"captured\":\"2022-04-27T11:24:44.217+00:00\"},\"healthCheckPassed\":true,\"environmentCheckResult\":\"Passed\"},\"attestation\":{\"form\":\"SURROGATE_BASIC\"}}}}}",
>   "authenticationAttempts": [
>     {
>       "attemptId": "1006700020:1006701019",
>       "created": "2022-04-27T11:24:51.446+0000",
>       "decision": "Y",
>       "state": "COMPLETED_SUCCESSFUL",
>       "attributes": {},
>       "items": [
>         {
>           "created": "2022-04-27T11:24:51.446+0000",
>           "authenticator": {
>             "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/authenticators/QTAzbtS4D4IA2RfWR1tpJiWfdg",
>             "id": "QTAzbtS4D4IA2RfWR1tpJiWfdg"
>           },
>           "type": "Face",
>           "result": "MATCH",
>           "authenticatorCounter": 2,
>           "aaid": "D409#2204"
>         }
>       ]
>     }
>   ],
>   "registration": {
>     "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/registrations/QTAzSJr1BHUwctCsDXZtGvVJ1Q"
>   },
>   "policy": {
>     "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/policies/QTAzCPHRfwCBXcI1Rm9-FiDR1g"
>   },
>   "application": {
>     "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/applications/QTAzdui396GxUj_w7N2KHr1edg"
>   },
>   "user": {
>     "href": "https://api.identityx-cloud.com/pingdavinci/IdentityXServices/rest/v1/users/QTAzs3wrZYvmxdu0LQ13r8z75w"
>   },
>   "tenant": {
>     "href": "https://api.identityx-cloud.com/IdentityXServices/rest/v1/tenants/r4SWIoHpn0fmXw4pkQhAbw"
>   }
> }
> ```

### Webhook Handler

Listen for an authentication response webhook

> **Collapse: Show details**
>
> * Output Schema
>
> - output object
>
>   * restId string
>
>   * transactionIdentifier string
>
>   * transactionStatus string
