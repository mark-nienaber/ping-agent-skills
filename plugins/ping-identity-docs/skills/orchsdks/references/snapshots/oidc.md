---
title: Android OIDC login tutorials
description: Provides a list of OIDC login tutorials for Android with PingOne, Advanced Identity Cloud, PingAM, and PingFederate.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/android/index
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/android/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "Android", "PingOne", "Advanced Identity Cloud", "PingAM", "PingFederate"]
---

# Android OIDC login tutorials

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: circle-check, set=far]PingFederate [icon: android, set=fab]Android

Follow these tutorials to integrate OpenID Connect sign-on to the following servers in your Android apps:

![](../../../_images/logos/PingOne.png)

#### [PingOne](pingone/index.html)

Implement OIDC sign-on to PingOne in Android apps

![](../../../_images/logos/PingOneAICStacked.png)

#### [PingOne Advanced Identity Cloud](aic/index.html)

Implement OIDC sign-on to PingOne Advanced Identity Cloud in Android apps

![](../../../_images/logos/PingAM.png)

#### [PingAM](pingam/index.html)

Implement OIDC sign-on to PingAM in Android apps

![](../../../_images/logos/PingFederate.png)

#### [PingFederate](pingfed/index.html)

Implement OIDC sign-on to PingFederate in Android apps

---

---
title: Apple iOS OIDC login tutorials
description: Provides a list of OIDC login tutorials for iOS with PingOne, Advanced Identity Cloud, PingAM, and PingFederate.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/ios/index
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/ios/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "iOS", "PingOne", "Advanced Identity Cloud", "PingAM", "PingFederate"]
---

# Apple iOS OIDC login tutorials

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: circle-check, set=far]PingFederate [icon: apple, set=fab]iOS

Follow these tutorials to integrate OpenID Connect sign-on to the following servers in your iOS apps:

![](../../../_images/logos/PingOne.png)

#### [PingOne](pingone/index.html)

Implement OIDC sign-on to PingOne in iOS apps

![](../../../_images/logos/PingOneAICStacked.png)

#### [PingOne Advanced Identity Cloud](aic/index.html)

Implement OIDC sign-on to PingOne Advanced Identity Cloud in iOS apps

![](../../../_images/logos/PingAM.png)

#### [PingAM](pingam/index.html)

Implement OIDC sign-on to PingAM in iOS apps

![](../../../_images/logos/PingFederate.png)

#### [PingFederate](pingfed/index.html)

Implement OIDC sign-on to PingFederate in iOS apps

---

---
title: Authenticating devices with the Device Authorization Grant
description: PingOne PingOne Advanced Identity Cloud PingAM Android iOS React Native
component: orchsdks
page_id: orchsdks:oidc:use-cases/device-authorization-grant/index
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/use-cases/device-authorization-grant/index.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 15 May 2026 00:00:00 +0000
keywords: ["OAuth 2.0", "OpenID Connect", "Device Authorization Grant", "RFC 8628", "SDK", "Android", "iOS", "React Native"]
section_ids:
  get_started: Get Started
---

# Authenticating devices with the Device Authorization Grant

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: android, set=fab]Android [icon: apple, set=fab]iOS [icon: react, set=fab]React Native

The Orchestration SDK implements the [OAuth 2.0 Device Authorization Grant (RFC 8628)](https://datatracker.ietf.org/doc/html/rfc8628) that lets you authenticate users on devices that have limited input capabilities or no embedded browser, such as smart TVs, IoT devices, or lobby kiosks.

The flow involves two devices:

* **The requesting device**

  The constrained device running your app. It starts the flow, displays the code, and polls the server until it receives tokens.

* **The approving device**

  A browser-capable device, such as the user's phone or computer, where the user navigates to the authorization server and authenticates.

The app on the requesting device obtains a short-lived code from the authorization server, displays it to the user, and polls in the background while the user completes authentication on the separate, browser-capable approving device.

Figure 1. Summary of the device authorization grant flow

The overall authentication flow is as follows:

1. The requesting app calls `OidcDeviceClient.deviceAuthorization()`, causing the Orchestration SDK to send a `POST` request to the device authorization endpoint.

2. The server returns a `device_code`, a short human-readable `user_code`, a `verification_uri`, an optional `verification_uri_complete` parameter, and a polling `interval`.

   The requesting app now displays the `user_code` and `verification_uri` to the user, so they can complete authentication on a separate, more capable device.

   Options for displaying the values include:

   * Plain text, so the user can visit the URL and type the code manually.

   * A QR Code the user can scan that has the URI, and the user code as a query parameter. When the user scans it on the approving device, the browser opens the authorization server's UI with the code pre-filled, so the user does not need to type it.

3. The requesting app begins polling the server's token endpoint, including the `device_code`, to check if the authentication has been completed.

4. The server returns `authorization_pending`, indicating the user has not yet authenticated. The requesting app waits for the `interval` duration and polls again.

5. On the approving device, the user navigates to the `verification_uri` and enters the `user_code`.

6. The authorization server starts an authentication journey or DaVinci flow.

7. The user completes authentication on the approving device, stepping through the journey or flow.

8. On successful authentication, the server updates the status for the relevant `device_code`.

9. The requesting app is still polling the token endpoint with the `device_code`.

10. This time, the server returns an `access_token`, `id_token`, and optional `refresh_token`. Authentication is complete.

## Get Started

[icon: android, set=fab, size=3x]

#### [Android](android.html)

Configure an Android app to authenticate using the Device Authorization Grant.

[icon: apple, set=fab, size=3x]

#### [iOS](ios.html)

Configure an iOS app to authenticate using the Device Authorization Grant.

[icon: react, set=fab, size=3x]

#### [React Native](react-native.html)

Configure a React Native app to authenticate using the Device Authorization Grant.

---

---
title: Before you begin
description: Set up the custom login UI sample app by downloading dependencies and configuring DNS aliases before starting the tutorial
component: orchsdks
page_id: orchsdks:oidc:use-cases/custom-login-ui/00-before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/use-cases/custom-login-ui/00-before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 20 Feb 2025 10:30:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "SDK"]
section_ids:
  step_1_downloading_the_samples: Step 1. Downloading the samples
  step_2_installing_the_dependencies: Step 2. Installing the dependencies
  step_3_hosting_the_sample_apps: Step 3. Hosting the sample apps
  obtaining_your_local_ip_address: Obtaining your local IP address
  creating_a_dns_alias_for_the_javascript_client_application: Creating a DNS alias for the JavaScript client application
---

# Before you begin

## Step 1. Downloading the samples

To download or clone a copy of the SDK Sample Apps repo, complete these steps:

1. In a web browser, navigate to <https://github.com/ForgeRock/sdk-sample-apps>.

2. Download the source code using one of the following methods:

   * Download a ZIP file

     1. Click Code, and then click Download ZIP.

        ![download samples zip](../../../_images/download-samples-zip.png)Figure 1. Downloading a zip file of the sample apps repo.

     2. Extract the contents of the downloaded ZIP file to a suitable location.

   * Use a Git-compatible tool to clone the repo locally

     1. Click Code, and then copy the HTTPS URL.

        ![download samples git clone](../../../_images/download-samples-git-clone.png)Figure 2. Downloading the sample apps repo using Git clone.

     2. Use the URL to clone the repository to a suitable location.

        For example, from the command-line you could run:

        ```shell
        git clone https://github.com/ForgeRock/sdk-sample-apps.git
        ```

After completing these steps, you will have a local folder named `sdk-sample-apps`. Inside, you'll find separate folders for the Android, iOS, JavaScript, and React Native sample app projects.

## Step 2. Installing the dependencies

In the following procedure, you install the required modules and dependencies, including the Orchestration SDK for JavaScript.

1. In a terminal window, navigate to the `sdk-sample-apps/javascript` folder.

2. To install the required packages, enter the following:

   ```shell
   npm install
   ```

   The `npm` tool downloads the required packages, and places them inside a `node_modules` folder.

## Step 3. Hosting the sample apps

In a production scenario your custom login UI app would have its own fully-qualified domain name that your Android, iOS, and JavaScript clients could all connect to.

For simplicity, in this tutorial you will serve your custom login UI app from the local IP address of your host computer.

Using the local IP of your host computer means Android and iOS apps running on a simulator can resolve the address, and also JavaScript apps running locally.

### Obtaining your local IP address

Complete the following steps to obtain your local IP address:

* Windows

* macOS

1. In a command prompt, enter `ipconfig /all`

   Windows displays information about the network adapters in your computer.

   > **Collapse: Show example output**
   >
   > ```
   > Windows IP Configuration
   >    Host Name . . . . . . . . . . . . : Windows
   >    Primary Dns Suffix  . . . . . . . :
   >    Node Type . . . . . . . . . . . . : Hybrid
   >    IP Routing Enabled. . . . . . . . : No
   >    WINS Proxy Enabled. . . . . . . . : No
   >
   > Ethernet adapter Ethernet:
   >    Media State . . . . . . . . . . . : Media disconnected
   >    Description . . . . . . . . . . . : E3100G 2.5 Gigabit Ethernet Controller
   >    Physical Address. . . . . . . . . : 74-34-E2-2b-30-44
   >    DHCP Enabled. . . . . . . . . . . : Yes
   >    Autoconfiguration Enabled . . . . : Yes
   >
   > Wireless LAN adapter Local Area Connection* 1:
   >    Media State . . . . . . . . . . . : Media disconnected
   >    Description . . . . . . . . . . . : Microsoft Wi-Fi Direct Virtual Adapter
   >    Physical Address. . . . . . . . . : 67-6C-EB-B3-46-82
   >    DHCP Enabled. . . . . . . . . . . : Yes
   >    Autoconfiguration Enabled . . . . : Yes
   >
   > Wireless LAN adapter Wi-Fi:
   >    Description . . . . . . . . . . . : Wireless Network Adapter (210NGW)
   >    Physical Address. . . . . . . . . : 87-6C-DF-C9-17-90
   >    DHCP Enabled. . . . . . . . . . . : Yes
   >    Autoconfiguration Enabled . . . . : Yes
   >    IPv6 Address. . . . . . . . . . . : 2406:3d08:2f61:1400::2d47
   >    Lease Obtained. . . . . . . . . . : January 27, 2025 11:09:26 AM
   >    Lease Expires . . . . . . . . . . : January 28, 2025 6:09:26 AM
   >    IPv6 Address. . . . . . . . . . . : 2406:3d08:2f61:1400::2d47
   >    Temporary IPv6 Address. . . . . . : 2604:2b08:2f93:2600:b479:b5b4:25ff:acc8
   >    Link-local IPv6 Address . . . . . : fe54::d9e5:16ff:d9d4:e22%10
   >    IPv4 Address. . . . . . . . . . . : 192.168.0.35
   >    Subnet Mask . . . . . . . . . . . : 255.255.255.0
   >    Lease Obtained. . . . . . . . . . : January 27, 2025 11:09:24 AM
   >    Lease Expires . . . . . . . . . . : January 29, 2025 11:09:26 AM
   >    Default Gateway . . . . . . . . . : fe80::bb8:c0ee:fea5:8c58%10
   >                                        192.168.0.1
   >    DHCP Server . . . . . . . . . . . : 192.168.0.1
   >    DHCPv6 IAID . . . . . . . . . . . : 893252287
   >    DHCPv6 Client DUID. . . . . . . . : 00-01-00-01-1b-87-59-2D-74-86-C4-3C-30-88
   >    DNS Servers . . . . . . . . . . . : 2025:4e8:0:230b::11
   >                                        2025:4e8:0:230c::11
   >                                        8.8.8.8
   >    NetBIOS over Tcpip. . . . . . . . : Enabled
   > ```

2. Ignoring adapters where the **Media State** property is listed as `Media Disconnected`, locate the ethernet or wireless adapter that connects to your router.

3. Make a note of the **IPv4 Address** field.

   |   |                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The address will often start with `192.168.`, `10.0.`, or `172.16.`, which are the first digits of the commonly used reserved private IPv4 addresses. |

   In this case, the local IPv4 IP address is `192.168.0.35`.

   You will use this address to access your custom UI app for this tutorial.

1) In a terminal window, enter `ifconfig`

   macOS displays information about the network interfaces in your computer.

   > **Collapse: Show example output**
   >
   > ```
   > lo0: flags=8049<UP,LOOPBACK,RUNNING,MULTICAST> mtu 16384
   > 	options=1203<RXCSUM,TXCSUM,TXSTATUS,SW_TIMESTAMP>
   > 	inet 127.0.0.1 netmask 0xff000000
   > 	inet6 ::1 prefixlen 128
   > 	inet6 fe80::1%lo0 prefixlen 64 scopeid 0x1
   > 	nd6 options=201<PERFORMNUD,DAD>
   > gif0: flags=8010<POINTOPOINT,MULTICAST> mtu 1280
   > stf0: flags=0<> mtu 1280
   > anpi0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=400<CHANNEL_IO>
   > 	ether 22:d0:cb:e5:fd:09
   > 	media: none
   > 	status: inactive
   > en3: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=404<VLAN_MTU,CHANNEL_IO>
   > 	ether f8:e4:3b:ad:67:c5
   > 	inet6 fe80::ca4:9a6c:f835:80c9%en8 prefixlen 64 secured scopeid 0x7
   > 	inet6 fd84:bb80:dd60:23b3:855:171f:3651:b7de prefixlen 64 autoconf secured
   > 	inet 192.168.0.35 netmask 0xffffff00 broadcast 192.168.0.255
   > 	nd6 options=201<PERFORMNUD,DAD>
   > 	media: autoselect (1000baseT <full-duplex>)
   > 	status: active
   > en1: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
   > 	options=460<TSO4,TSO6,CHANNEL_IO>
   > 	ether 36:e5:80:6e:d1:40
   > 	media: autoselect <full-duplex>
   > 	status: inactive
   > en2: flags=8963<UP,BROADCAST,SMART,RUNNING,PROMISC,SIMPLEX,MULTICAST> mtu 1500
   > 	options=460<TSO4,TSO6,CHANNEL_IO>
   > 	ether 36:e5:80:6e:d1:44
   > 	media: autoselect <full-duplex>
   > 	status: inactive
   > bridge0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=63<RXCSUM,TXCSUM,TSO4,TSO6>
   > 	ether 36:e5:80:6e:d1:40
   > 	Configuration:
   > 		id 0:0:0:0:0:0 priority 0 hellotime 0 fwddelay 0
   > 		maxage 0 holdcnt 0 proto stp maxaddr 100 timeout 1200
   > 		root id 0:0:0:0:0:0 priority 0 ifcost 0 port 0
   > 		ipfilter disabled flags 0x0
   > 	member: en1 flags=3<LEARNING,DISCOVER>
   > 	        ifmaxaddr 0 port 11 priority 0 path cost 0
   > 	member: en2 flags=3<LEARNING,DISCOVER>
   > 	        ifmaxaddr 0 port 12 priority 0 path cost 0
   > 	member: en3 flags=3<LEARNING,DISCOVER>
   > 	        ifmaxaddr 0 port 13 priority 0 path cost 0
   > 	media: <unknown type>
   > 	status: inactive
   > ap1: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
   > 	ether d6:0f:2c:90:e9:b6
   > 	nd6 options=201<PERFORMNUD,DAD>
   > 	media: autoselect (none)
   > 	status: inactive
   > en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
   > 	options=6460<TSO4,TSO6,CHANNEL_IO,PARTIAL_CSUM,ZEROINVERT_CSUM>
   > 	ether c6:2a:06:29:ee:28
   > 	nd6 options=201<PERFORMNUD,DAD>
   > 	media: autoselect
   > 	status: inactive
   > utun0: flags=8051<UP,POINTOPOINT,RUNNING,MULTICAST> mtu 1500
   > 	inet6 fe80::a19f:5de6:a4ca:fd90%utun0 prefixlen 64 scopeid 0x13
   > 	nd6 options=201<PERFORMNUD,DAD>
   > ```

2) Looking at interfaces where the **status** property is listed as `active`, locate the ethernet or wireless interface that connects to your router.

   Often the prefix of the interface is `en`.

3) Make a note of the IPv4 address in the **inet** field.

   |   |                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | The address will often start with `192.168.`, `10.0.`, or `172.16.`, which are the first digits of the commonly used reserved private IPv4 addresses. |

   In this case, the local IPv4 IP address is `192.168.0.35`.

   You will use this address to access your custom UI app for this tutorial.

### Creating a DNS alias for the JavaScript client application

You should assign a DNS alias to your localhost address to help differentiate the client application from the custom UI application during this tutorial.

You can choose whatever host name you prefer for your client application. This tutorial uses `sdkapp.example.com`.

Complete the following steps to configure a DNS alias for your local IP address:

* Windows

* macOS

1. As an administrator, in a text editor open the `%SystemRoot%\system32\drivers\etc\hosts` file.

2. Add the following:

   `127.0.0.1 sdkapp.example.com`

3. Close and save the file.

1) As an administrator, in a text editor open the `/etc/hosts` file.

2) Add the following:

   `127.0.0.1 sdkapp.example.com`

3) Close and save the file.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the Android OIDC sign-on module tutorial for Advanced Identity Cloud.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/android/aic/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/android/aic/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "Android", "Advanced Identity Cloud", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: android, set=fab]Android

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-connection-properties.html)

* [Run](03_test-the-app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne Advanced Identity Cloud tenant.

## Prerequisites

* Android Studio

  Download and install [Android Studio](https://developer.android.com/studio), which is available for many popular operating systems.

* An Android emulator or physical device

  To try the quick start application as you develop it, you need an Android device. To add a virtual, emulated Android device to Android Studio, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds), on the **Android Developers** website.

## Server configuration

This tutorial requires you to configure your PingOne Advanced Identity Cloud tenant as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Identities > Manage.
>
> 3. Click [icon: plus, set=fa]New Alpha realm - User.
>
> 4. Enter the following details:
>
>    * **Username** = `demo`
>
>    * **First Name** = `Demo`
>
>    * **Last Name** = `User`
>
>    * **Email Address** = `demo.user@example.com`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Create an authentication journey**
>
> Authentication journeys provide fine-grained authentication by allowing multiple paths and decision points throughout the flow. Authentication journeys are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> You'll need an authentication journey configured on your server to try out the **Journey** module. That journey must only use [nodes, and therefore callbacks, that the Orchestration SDKs supports](../../../../journey/compatibility.html#supported-authentication-journey-callbacks).
>
> |   |                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------- |
> |   | You can use the default **Login** journey that both Advanced Identity Cloud and PingAM include out-of-the-box. |
>
> To create your own authentication journey for use when testing the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Journeys, and click [icon: plus, set=fa]New Journey.
>
> 2. Enter a name, such as `sdkUsernamePasswordJourney` and click Save.
>
>    The authentication journey designer appears.
>
> 3. Drag the following nodes into the designer area:
>
>    * **Page Node**
>
>    * **Platform Username**
>
>    * **Platform Password**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Platform Username** and **Platform Password** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![sdk username password journey idcloud en](../../../../_images/sdk-username-password-journey-idcloud-en.png)Figure 1. Example username and password authentication journey
>
> 6. Click Save.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Native / SPA as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Public SDK Client`.
>
> 7. In Owners, select a user that is responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. In Client ID, enter `sdkPublicClient`
>
> 9. Select **Configure for SDK Sample Apps**.
>
> 10. Click Create Application.
>
>     PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 11. On the Sign On tab:
>
>     1. In Sign-In URLs, ensure the following values appear, or add them if they don't:
>
>        `com.example.demo://oauth2redirect`
>
>        |   |                                                             |
>        | - | ----------------------------------------------------------- |
>        |   | Also add any other domains where you host SDK applications. |
>
>     2. In Grant Types, ensure the following values appear:
>
>        `Authorization Code`
>
>        `Refresh Token`
>
>     3. In Scopes, ensure the following values appear:
>
>        `openid profile email address`
>
> 12. Click Show advanced settings, and on the Authentication tab, confirm the following properties:
>
>     1. In Token Endpoint Authentication Method, select `none`.
>
>     2. In Client Type, select `Public`.
>
>     3. Enable the Implied Consent property.
>
> 13. Click Save.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the example applications and tutorials covered by this documentation.

> **Collapse: Task 4. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingOne Advanced Identity Cloud OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Native Consoles > Access Management.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the Android OIDC sign-on module tutorial for PingAM.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/android/pingam/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/android/pingam/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "Android", "PingAM", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingAM [icon: android, set=fab]Android

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-connection-properties.html)

* [Run](03_test-the-app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingAM server.

## Prerequisites

* Android Studio

  Download and install [Android Studio](https://developer.android.com/studio), which is available for many popular operating systems.

* An Android emulator or physical device

  To try the quick start application as you develop it, you need an Android device. To add a virtual, emulated Android device to Android Studio, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds), on the **Android Developers** website.

## Server configuration

This tutorial requires you to configure your PingAM server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingAM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: address-card, set=fa]Identities, and then click [icon: plus, set=fa]Add Identity.
>
> 3. Enter the following details:
>
>    * **User ID** = `demo`
>
>    * **Password** = `Ch4ng3it!`
>
>    * **Email Address** = `demo.user@example.com`
>
> 4. Click Create.

> **Collapse: Task 2. Create an authentication tree**
>
> Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow. Authentication trees are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> To create a simple tree for use when testing the Orchestration SDKs, follow these steps:
>
> 1. Under Realm Overview, click Authentication Trees, then click Create Tree.
>
> 2. Enter a tree name, for example `sdkUsernamePasswordJourney`, and then click Create.
>
>    The authentication tree designer appears, showing the Start entry point connected to the Failure exit point.
>
> 3. Drag the following nodes from the Components panel on the left side into the designer area:
>
>    * **Page Node**
>
>    * **Username Collector**
>
>    * **Password Collector**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Username Collector** and **Password Collector** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![trees node login example](../../../../_images/trees-node-login-example.png)Figure 1. Example username and password authentication tree
>
> 6. Select the **Page Node**, and in the Properties pane, set the Stage property to `UsernamePassword`.
>
>    |   |                                                                                                            |
>    | - | ---------------------------------------------------------------------------------------------------------- |
>    |   | You can configure the node properties by selecting a node and altering properties in the right-hand panel. |
>
>    One of the samples uses this specific value to determine the custom UI to display.
>
> 7. Click **Save**.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkPublicClient`.
>
> 4. Leave Client secret empty.
>
> 5. In Redirection URIs, enter the following values:
>
>    `com.example.demo://oauth2redirect`
>
>    |   |                                                                        |
>    | - | ---------------------------------------------------------------------- |
>    |   | Also add any other domains where you will be hosting SDK applications. |
>
> 6. In Scopes, enter the following values:
>
>    `openid profile email address`
>
> 7. Click Create.
>
>    PingAM creates the new OAuth 2.0 client, and displays the properties for further configuration.
>
> 8. On the Core tab:
>
>    1. In Client type, select `Public`.
>
>    2. Disable Allow wildcard ports in redirect URIs.
>
>    3. Click Save Changes.
>
> 9. On the Advanced tab:
>
>    1. In Grant Types, enter the following values:
>
>       ```none
>       Authorization Code
>       Refresh Token
>       ```
>
>    2. In Token Endpoint Authentication Method, select `None`.
>
>    3. Enable the Implied consent property.
>
> 10. Click Save Changes.

> **Collapse: Task 4. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingAM OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the Android OIDC sign-on module tutorial for PingFederate.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/android/pingfed/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/android/pingfed/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "Android", "PingFederate", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingFederate [icon: android, set=fab]Android

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-sample-for-pingfed.html)

* [Run](03_running-sample-pingfed.html)

To successfully complete this tutorial refer to the prerequisites and compatibility requirements in this section.

The tutorial also requires a configured PingFederate server.

## Prerequisites

* Android Studio

  Download and install [Android Studio](https://developer.android.com/studio), which is available for many popular operating systems.

* An Android emulator or physical device

  To try the quick start application as you develop it, you need an Android device. To add a virtual, emulated Android device to Android Studio, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds), on the **Android Developers** website.

## Server configuration

This tutorial requires you to configure your PingFederate server as follows:

> **Collapse: Task 1. Register a public OAuth 2.0 client**
>
> OAuth 2.0 client application profiles define how applications connect to PingFederate and obtain OAuth 2.0 tokens.
>
> To allow the Orchestration SDKs to connect to PingFederate and obtain OAuth 2.0 tokens, you must register an OAuth 2.0 client application:
>
> 1. Log in to the PingFederate administration console as an administrator.
>
> 2. Navigate to **Applications** [icon: angle-right, set=fa] **OAuth** [icon: angle-right, set=fa] **Clients**.
>
> 3. Click **Add Client**.
>
>    PingFederate displays the **Clients | Client** page.
>
> 4. In **Client ID** and **Name**, enter a name for the profile, for example `sdkPublicClient`
>
>    Make a note of the **Client ID** value, you will need it when you configure the sample code.
>
> 5. In **Client Authentication**, select `None`.
>
> 6. In **Redirect URIs**, add the following:
>
>    `com.example.demo://oauth2redirect`
>
>    |   |                                                                                                                                                                                                                                                                                   |
>    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Also add any other URLs where you host SDK applications.Failure to add redirect URLs that exactly match your client app's values can cause PingFederate to display an error message such as `Redirect URI mismatch` when attempting to end a session by redirecting from the SDK. |
>
> 7. In **Allowed Grant Types**, select the following values:
>
>    `Authorization Code`
>
>    `Refresh Token`
>
> 8. In the **OpenID Connect** section:
>
>    1. In **Logout Mode**, select **Ping Front-Channel**
>
>    2. In **Front-Channel Logout URIs**, add the following:
>
>       `com.example.demo://oauth2redirect`
>
>       |   |                                                                                                                                                                                                                                                                                                                       |
>       | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Also add any other URLs that redirect users to PingFederate to end their session.Failure to add sign off URLs that exactly match your client app's values can cause PingFederate to display an error message such as `invalid post logout redirect URI` when attempting to end a session by redirecting from the SDK. |
>
>    3. In **Post-Logout Redirect URIs**, add the following:
>
>       `com.example.demo://oauth2redirect`
>
> 9. Click Save.
>
>    |   |                                                                                                                                                                                                                                                                                                  |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    |   | After changing PingFederate configuration using the administration console, you must replicate the changes to each server node in the cluster before they take effect.In the PingFederate administration console, navigate to **System > Server > Cluster Management**, and click **Replicate**. |
>
>    The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the Orchestration SDK PingFederate example applications and tutorials covered by this documentation.

> **Collapse: Task 2. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingFederate, you can configure CORS to allow browsers or apps from trusted domains to access protected resources.
>
> To configure CORS in PingFederate follow these steps:
>
> 1. Log in to the PingFederate administration console as an administrator.
>
> 2. Navigate to **System** [icon: angle-right, set=fa] **OAuth Settings** [icon: angle-right, set=fa] **Authorization Server Settings**.
>
> 3. In the **Cross-Origin Resource Sharing Settings** section, in the **Allowed Origin** field, enter any DNS aliases you use for your SDK apps.
>
>    This documentation assumes the following configuration:
>
>    | Property         | Values                              |
>    | ---------------- | ----------------------------------- |
>    | `Allowed Origin` | `com.example.demo://oauth2redirect` |
>
> 4. Click **Save**.
>
>    |   |                                                                                                                                                                                                                                                                                                  |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    |   | After changing PingFederate configuration using the administration console, you must replicate the changes to each server node in the cluster before they take effect.In the PingFederate administration console, navigate to **System > Server > Cluster Management**, and click **Replicate**. |
>
>    Your PingFederate server is now able to accept connections from origins hosting apps built with the Orchestration SDKs.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the Android OIDC sign-on module tutorial for PingOne.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/android/pingone/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/android/pingone/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "Android", "PingOne", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  p1-server-android: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: android, set=fab]Android

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-sample-for-pingone.html)

* [Run](03_running-sample-pingone.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a [configured PingOne instance](#p1-server-android).

## Prerequisites

* Android Studio

  Download and install [Android Studio](https://developer.android.com/studio), which is available for many popular operating systems.

* An Android emulator or physical device

  To try the quick start application as you develop it, you need an Android device. To add a virtual, emulated Android device to Android Studio, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds), on the **Android Developers** website.

## Server configuration

This tutorial requires you to configure your PingOne server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Directory > Users.
>
> 3. Next to the Users label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add User panel.
>
> 4. Enter the following details:
>
>    * **Given Name** = `Demo`
>
>    * **Family Name** = `User`
>
>    * **Username** = `demo`
>
>    * **Email** = `demo.user@example.com`
>
>    * **Population** = `Default`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Register a public OAuth 2.0 client**
>
> To register a *public* OAuth 2.0 client application in PingOne for use with the Orchestration SDKs for Android and iOS, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Applications > Applications.
>
> 3. Next to the Applications label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add Application panel.
>
> 4. In Application Name, enter a name for the profile, for example `sdkNativeClient`
>
> 5. Select Native as the Application Type, and then click Save.
>
> 6. On the Configuration tab, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Grant Type, select the following values:
>
>       `Authorization Code`
>
>       `Refresh Token`
>
>    2. In Redirect URIs, enter the following values:
>
>       `com.example.demo://oauth2redirect`
>
>    3. In Token Endpoint Authentication Method, select `None`.
>
>    4. In the **Advanced Settings** section, enable **Terminate User Session by ID Token**.
>
>    5. Click Save.
>
> 7. On the Resources tab, next to Allowed Scopes, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Scopes, select the following values:
>
>       `email`
>
>       `phone`
>
>       `profile`
>
>       |   |                                            |
>       | - | ------------------------------------------ |
>       |   | The `openid` scope is selected by default. |
>
>       The result resembles the following:
>
>       ![Adding scopes to an application.](../../../../_images/pingone-oidc-native-scopes-en.png)Figure 1. Adding scopes to an application.
>
> 8. Optionally, on the Policies tab, click the pencil icon ([icon: pencil, set=fa]) to select the authentication policies for the application.
>
>    |   |                                                                                                                                        |
>    | - | -------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Applications that have no authentication policy assignments use the environment's default authentication policy to authenticate users. |
>
>    If you have a DaVinci license, you can select PingOne policies or DaVinci Flow policies, but not both. If you do not have a DaVinci license, the page only displays PingOne policies.
>
>    To use a *PingOne policy*:
>
>    1. Click [icon: plus, set=fa]Add policies and then select the policies that you want to apply to the application.
>
>    2. Click Save.
>
>       PingOne applies the policies in the order in which they appear in the list. PingOne evaluates the first policy in the list first. If the requirements are not met, PingOne moves to the next one.
>
>       For more information, see [Authentication policies for applications](https://docs.pingidentity.com/pingone/applications/p1_auth_policies_for_applications.html).
>
>    To use a *DaVinci Flow policy*:
>
>    1. You must clear all PingOne policies. Click Deselect all PingOne Policies.
>
>    2. In the confirmation message, click Continue.
>
>    3. On the DaVinci Policies tab, select the policies that you want to apply to the application.
>
>    4. Click Save.
>
>       PingOne applies the first policy in the list.
>
> 9. Click Save.
>
> 10. Enable the OAuth 2.0 client application by using the toggle next to its name:
>
>     ![Enable the application using the toggle.](../../../../_images/pingone-apps-enable-native-client-en.png)Figure 2. Enable the application using the toggle.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the Android and iOS PingOne example applications and tutorials covered by this documentation.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the JavaScript OIDC sign-on module tutorial for Advanced Identity Cloud.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/javascript/aic/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/javascript/aic/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "JavaScript", "Advanced Identity Cloud", "prerequisites"]
section_ids:
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: js, set=fab]JavaScript

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configure_connection_properties.html)

* [Run](03_test_the_app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne Advanced Identity Cloud tenant.

* Node and NPM

  This sample requires a minimum Node.js version of `18`, and is tested on versions `18` and `20`. To get a supported version of Node.js, refer to the [Node.js download page](https://nodejs.org/en/download/).

  You will also need `npm` to build the code and run the samples.

## Server configuration

This tutorial requires you to configure your PingOne Advanced Identity Cloud tenant as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Identities > Manage.
>
> 3. Click [icon: plus, set=fa]New Alpha realm - User.
>
> 4. Enter the following details:
>
>    * **Username** = `demo`
>
>    * **First Name** = `Demo`
>
>    * **Last Name** = `User`
>
>    * **Email Address** = `demo.user@example.com`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Create an authentication journey**
>
> Authentication journeys provide fine-grained authentication by allowing multiple paths and decision points throughout the flow. Authentication journeys are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> You'll need an authentication journey configured on your server to try out the **Journey** module. That journey must only use [nodes, and therefore callbacks, that the Orchestration SDKs supports](../../../../journey/compatibility.html#supported-authentication-journey-callbacks).
>
> |   |                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------- |
> |   | You can use the default **Login** journey that both Advanced Identity Cloud and PingAM include out-of-the-box. |
>
> To create your own authentication journey for use when testing the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Journeys, and click [icon: plus, set=fa]New Journey.
>
> 2. Enter a name, such as `sdkUsernamePasswordJourney` and click Save.
>
>    The authentication journey designer appears.
>
> 3. Drag the following nodes into the designer area:
>
>    * **Page Node**
>
>    * **Platform Username**
>
>    * **Platform Password**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Platform Username** and **Platform Password** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![sdk username password journey idcloud en](../../../../_images/sdk-username-password-journey-idcloud-en.png)Figure 1. Example username and password authentication journey
>
> 6. Click Save.

> **Collapse: Task 3. Register a confidential OAuth 2.0 client**
>
> Confidential clients are able to securely store credentials and are commonly used for server-to-server communication. For example, the "Todo" API backend provided with the SDK samples uses a confidential client to obtain tokens.
>
> To register a *confidential* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Web as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Confidential SDK Client`.
>
> 7. In Owners, select a user responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. On the Web Settings page:
>
>    1. In Client ID, enter `sdkConfidentialClient`
>
>    2. In Client Secret, enter a strong password and make a note of it for later use.
>
>       For example, `5tr0ngP@S5w0rd!`
>
>       |   |                                                                                                                                               |
>       | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | The client secret is not available to view after this step.If you forget it, you must reset the secret and reconfigure any connected clients. |
>
>    3. Click Create Application.
>
>       PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 9. On the Sign On tab, click Show advanced settings, and on the Access tab:
>
>    1. In Default Scopes, enter `am-introspect-all-tokens`.
>
> 10. Click Save.

> **Collapse: Task 4. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Native / SPA as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Public SDK Client`.
>
> 7. In Owners, select a user that is responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. In Client ID, enter `sdkPublicClient`
>
> 9. Select **Configure for SDK Sample Apps**.
>
> 10. Click Create Application.
>
>     PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 11. On the Sign On tab:
>
>     1. In Sign-In URLs, ensure the following values appear, or add them if they don't:
>
>        `https://localhost:8443/callback.html`
>
>        |   |                                                             |
>        | - | ----------------------------------------------------------- |
>        |   | Also add any other domains where you host SDK applications. |
>
>     2. In Grant Types, ensure the following values appear:
>
>        `Authorization Code`
>
>        `Refresh Token`
>
>     3. In Scopes, ensure the following values appear:
>
>        `openid profile email address`
>
> 12. Click Show advanced settings, and on the Authentication tab, confirm the following properties:
>
>     1. In Token Endpoint Authentication Method, select `none`.
>
>     2. In Client Type, select `Public`.
>
>     3. Enable the Implied Consent property.
>
> 13. Click Save.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the example applications and tutorials covered by this documentation.

> **Collapse: Task 5. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingOne Advanced Identity Cloud OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Native Consoles > Access Management.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

> **Collapse: Task 6. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingOne Advanced Identity Cloud, you can configure CORS to allow browsers from trusted domains to access PingOne Advanced Identity Cloud protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the PingOne Advanced Identity Cloud REST API.
>
> The Orchestration SDK for JavaScript samples and tutorials use `https://localhost:8443` as the host domain, which you should add to your CORS configuration.
>
> If you are using a different domain for hosting SDK applications, ensure you add them to the CORS configuration as accepted origin domains.
>
> To update the CORS configuration in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. At the top right of the screen, click your name, and then select Tenant settings.
>
> 3. On the Global Settings tab, click Cross-Origin Resource Sharing (CORS).
>
> 4. Perform one of the following actions:
>
>    * If listed, click PingSDK.
>
>    * If there isn't an existing CORS configuration listed, click [icon: plus, set=fa]Add a CORS Configuration, select Ping SDK, and then click Next.
>
>      The **Ping SDK** template contains many of the default values used in these tutorials.
>
> 5. In Accepted Origins:
>
>    1. Ensure `https://localhost:8443` is listed.
>
>    2. Add any DNS aliases you use to host your Orchestration SDK for JavaScript applications.
>
> 6. Complete the remaining fields to suit your environment.
>
>    This documentation assumes the following configuration, required for the tutorials and sample applications:
>
>    | Property            | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>    | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    | `Accepted Origins`  | `https://localhost:8443``http://localhost:9443`                                                                                                                                                                                                                                                                                                                                                                                                        |
>    | `Accepted Methods`  | `GET``POST`                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>    | `Accepted Headers`  | `accept-api-version``x-requested-with``content-type``authorization``if-match``x-requested-platform``iPlanetDirectoryPro` \[[1](#_footnotedef_1 "View footnote.")]`ch15fefc5407912` \[[2](#_footnotedef_2 "View footnote.")]***[1](#_footnoteref_1). Cookie name value in PingAM servers.[2](#_footnoteref_2). In PingOne Advanced Identity Cloud tenants, go to **Tenant Settings > Global Settings > Cookie** to find this dynamic cookie name value. |
>    | `Exposed Headers`   | `authorization``content-type`                                                                                                                                                                                                                                                                                                                                                                                                                          |
>    | `Enable Caching`    | `True`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>    | `Max Age`           | `600`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
>    | `Allow Credentials` | `True`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>
>    |   |                                                                       |
>    | - | --------------------------------------------------------------------- |
>    |   | Click Show advanced settings to be able to edit all available fields. |
>
> 7. Click Save CORS Configuration.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the JavaScript OIDC sign-on module tutorial for PingAM.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/javascript/pingam/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/javascript/pingam/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "JavaScript", "PingAM", "prerequisites"]
section_ids:
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingAM [icon: js, set=fab]JavaScript

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configure_connection_properties.html)

* [Run](03_test_the_app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingAM server.

* Node and NPM

  This sample requires a minimum Node.js version of `18`, and is tested on versions `18` and `20`. To get a supported version of Node.js, refer to the [Node.js download page](https://nodejs.org/en/download/).

  You will also need `npm` to build the code and run the samples.

## Server configuration

This tutorial requires you to configure your PingAM server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingAM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: address-card, set=fa]Identities, and then click [icon: plus, set=fa]Add Identity.
>
> 3. Enter the following details:
>
>    * **User ID** = `demo`
>
>    * **Password** = `Ch4ng3it!`
>
>    * **Email Address** = `demo.user@example.com`
>
> 4. Click Create.

> **Collapse: Task 2. Create an authentication tree**
>
> Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow. Authentication trees are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> To create a simple tree for use when testing the Orchestration SDKs, follow these steps:
>
> 1. Under Realm Overview, click Authentication Trees, then click Create Tree.
>
> 2. Enter a tree name, for example `sdkUsernamePasswordJourney`, and then click Create.
>
>    The authentication tree designer appears, showing the Start entry point connected to the Failure exit point.
>
> 3. Drag the following nodes from the Components panel on the left side into the designer area:
>
>    * **Page Node**
>
>    * **Username Collector**
>
>    * **Password Collector**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Username Collector** and **Password Collector** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![trees node login example](../../../../_images/trees-node-login-example.png)Figure 1. Example username and password authentication tree
>
> 6. Select the **Page Node**, and in the Properties pane, set the Stage property to `UsernamePassword`.
>
>    |   |                                                                                                            |
>    | - | ---------------------------------------------------------------------------------------------------------- |
>    |   | You can configure the node properties by selecting a node and altering properties in the right-hand panel. |
>
>    One of the samples uses this specific value to determine the custom UI to display.
>
> 7. Click **Save**.

> **Collapse: Task 3. Register a confidential OAuth 2.0 client**
>
> Confidential clients are able to store credentials securely and are commonly used for server-to-server communication.
>
> To register a *confidential* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkConfidentialClient`.
>
> 4. In Client Secret, enter a strong password and make a note of it for later use.
>
>    For example, `5tr0ngP@S5w0rd!`
>
>    |   |                                                                                                                                               |
>    | - | --------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | The client secret is not available to view after this step.If you forget it, you must reset the secret and reconfigure any connected clients. |
>
> 5. In Default Scopes, enter `am-introspect-all-tokens`.
>
>    PingAM creates the new OAuth 2.0 client and displays the properties for further configuration.
>
> 6. On the Advanced tab:
>
>    1. Enable the Implied consent property.
>
> 7. Click Save Changes.

> **Collapse: Task 4. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkPublicClient`.
>
> 4. Leave Client secret empty.
>
> 5. In Redirection URIs, enter the following values:
>
>    `https://localhost:8443/callback.html`
>
>    |   |                                                                        |
>    | - | ---------------------------------------------------------------------- |
>    |   | Also add any other domains where you will be hosting SDK applications. |
>
> 6. In Scopes, enter the following values:
>
>    `openid profile email address`
>
> 7. Click Create.
>
>    PingAM creates the new OAuth 2.0 client, and displays the properties for further configuration.
>
> 8. On the Core tab:
>
>    1. In Client type, select `Public`.
>
>    2. Disable Allow wildcard ports in redirect URIs.
>
>    3. Click Save Changes.
>
> 9. On the Advanced tab:
>
>    1. In Grant Types, enter the following values:
>
>       ```none
>       Authorization Code
>       Refresh Token
>       ```
>
>    2. In Token Endpoint Authentication Method, select `None`.
>
>    3. Enable the Implied consent property.
>
> 10. Click Save Changes.

> **Collapse: Task 5. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingAM OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

> **Collapse: Task 6. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingAM, you can configure CORS to allow browsers from trusted domains to access PingAM protected resources. For example, you might want a custom web application running on your own domain to get an end-user's profile information using the PingAM REST API.
>
> The Orchestration SDK for JavaScript samples and tutorials all use `https://localhost:8443` as the host domain, which you should add to your CORS configuration.
>
> If you are using a different URL for hosting SDK applications, ensure you add them to the CORS configuration as accepted origin domains.
>
> To enable CORS in PingAM, and create a CORS filter to allow requests from your configured domain names, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to Configure > Global Services > CORS Service > Configuration, and set the Enable the CORS filter property to `true`.
>
>    |   |                                                                                                                      |
>    | - | -------------------------------------------------------------------------------------------------------------------- |
>    |   | If this property is not enabled, CORS headers are not added to responses from PingAM, and CORS is disabled entirely. |
>
> 3. On the Secondary Configurations tab, click Add a Secondary Configuration.
>
> 4. In the Name field, enter `OrchSDK`.
>
> 5. in the Accepted Origins field, enter any DNS aliases you use for your SDK apps.
>
>    This documentation assumes the following configuration:
>
>    | Property           | Values                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
>    | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    | `Accepted Origins` | `https://localhost:8443``http://localhost:9443`                                                                                                                                                                                                                                                                                                                                                                                                        |
>    | `Accepted Methods` | `GET``POST`                                                                                                                                                                                                                                                                                                                                                                                                                                            |
>    | `Accepted Headers` | `accept-api-version``x-requested-with``content-type``authorization``if-match``x-requested-platform``iPlanetDirectoryPro` \[[1](#_footnotedef_1 "View footnote.")]`ch15fefc5407912` \[[2](#_footnotedef_2 "View footnote.")]***[1](#_footnoteref_1). Cookie name value in PingAM servers.[2](#_footnoteref_2). In PingOne Advanced Identity Cloud tenants, go to **Tenant Settings > Global Settings > Cookie** to find this dynamic cookie name value. |
>
> 6. Click Create.
>
>    PingAM displays the configuration of your new CORS filter.
>
> 7. On the CORS filter configuration page:
>
>    1. Ensure Enable the CORS filter is enabled.
>
>    2. Set the Max Age property to `600`
>
>    3. Ensure Allow Credentials is enabled.
>
> 8. Click Save Changes.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the JavaScript OIDC sign-on module tutorial for PingOne.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/javascript/pingone/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/javascript/pingone/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "JavaScript", "PingOne", "prerequisites"]
section_ids:
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: js, set=fab]JavaScript

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configure_connection_properties.html)

* [Run](03_test_the_app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne tenant.

* Node and NPM

  This sample requires a minimum Node.js version of `18`, and is tested on versions `18` and `20`. To get a supported version of Node.js, refer to the [Node.js download page](https://nodejs.org/en/download/).

  You will also need `npm` to build the code and run the samples.

## Server configuration

This tutorial requires you to configure your PingOne tenant as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Directory > Users.
>
> 3. Next to the Users label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add User panel.
>
> 4. Enter the following details:
>
>    * **Given Name** = `Demo`
>
>    * **Family Name** = `User`
>
>    * **Username** = `demo`
>
>    * **Email** = `demo.user@example.com`
>
>    * **Population** = `Default`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Create a revoke resource**
>
> To allow the Orchestration SDKs to revoke access tokens issued by PingOne, you must create a custom resource that is assigned the `revoke` scope in your PingOne tenant.
>
> To create a custom resource and assign the `revoke` scope, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Applications > Resources.
>
> 3. Next to the Resources label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add Custom Resource panel.
>
> 4. In Resource Name, enter a name for the custom resource, for example `SDK Revoke Resource`, and then click Next.
>
> 5. On the Attributes page, click Next.
>
> 6. On the Scopes page, click [icon: plus, set=fa]Add Scope.
>
> 7. In Scope Name, enter `revoke`, and then click Save.
>
> When you have created the custom resource in your PingOne instance, continue with the next step.
>
> For more information on resources in PingOne, refer to [Adding a custom resource](https://docs.pingidentity.com/pingone/applications/p1_adding_custom_resource.html).

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> To register a *public* OAuth 2.0 client application in PingOne for use with the Orchestration SDK for JavaScript, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Applications > Applications.
>
> 3. Next to the Applications label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add Application panel.
>
> 4. In Application Name, enter a name for the profile, for example `sdkPublicClient`
>
> 5. Select OIDC Web App as the Application Type, and then click Save.
>
> 6. On the Configuration tab, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Grant Type, select the following:
>
>       `Authorization Code`
>
>       `Refresh Token`
>
>    2. In Redirect URIs, enter the following:
>
>       `https://localhost:8443/callback.html`
>
>       |   |                                                                                                                                                                                                                                                                              |
>       | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Also add any other URLs where you host SDK applications.Failure to add redirect URLs that exactly match your client app's values can cause PingOne to display an error message such as `Redirect URI mismatch` when attempting to end a session by redirecting from the SDK. |
>
>    3. In Token Endpoint Authentication Method, select `None`.
>
>    4. In Signoff URLs, enter the following:
>
>       `https://localhost:8443`
>
>       |   |                                                                                                                                                                                                                                                                                                             |
>       | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Also add any other URLs that redirect users to PingOne to end their session.Failure to add sign off URLs that exactly match your client app's values can cause PingOne to display an error message such as `invalid post logout redirect URI` when attempting to end a session by redirecting from the SDK. |
>
>    5. In CORS Settings, in the drop-down select Allow specific origins, and in the Allowed Origins field, enter the URL where you will be running the sample app.
>
>       For example, `https://localhost:8443`
>
>    6. In the **Advanced Settings** section, enable **Terminate User Session by ID Token**.
>
>    7. Click Save.
>
> 7. On the Resources tab, next to Allowed Scopes, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Scopes, select the following values:
>
>       `email`
>
>       `phone`
>
>       `profile`
>
>       `SDK Revoke Resource`
>
>       |   |                                            |
>       | - | ------------------------------------------ |
>       |   | The `openid` scope is selected by default. |
>
>       The result resembles the following:
>
>       ![Adding scopes to an application.](../../../../_images/pingone-oidc-scopes-with-revoke-en.png)Figure 1. Adding scopes to an application.
>
> 8. Optionally, on the Policies tab, click the pencil icon ([icon: pencil, set=fa]) to select the authentication policies for the application.
>
>    |   |                                                                                                                                        |
>    | - | -------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Applications that have no authentication policy assignments use the environment's default authentication policy to authenticate users. |
>
>    If you have a DaVinci license, you can select PingOne policies or DaVinci Flow policies, but not both. If you do not have a DaVinci license, the page only displays PingOne policies.
>
>    To use a *PingOne policy*:
>
>    1. Click [icon: plus, set=fa]Add policies and then select the policies that you want to apply to the application.
>
>    2. Click Save.
>
>       PingOne applies the policies in the order in which they appear in the list. PingOne evaluates the first policy in the list first. If the requirements are not met, PingOne moves to the next one.
>
>       For more information, see [Authentication policies for applications](https://docs.pingidentity.com/pingone/applications/p1_auth_policies_for_applications.html).
>
>    To use a *DaVinci Flow policy*:
>
>    1. You must clear all PingOne policies. Click Deselect all PingOne Policies.
>
>    2. In the confirmation message, click Continue.
>
>    3. On the DaVinci Policies tab, select the policies that you want to apply to the application.
>
>    4. Click Save.
>
>       PingOne applies the first policy in the list.
>
> 9. Click Save.
>
> 10. Enable the OAuth 2.0 client application by using the toggle next to its name:
>
>     ![Enable the application using the toggle.](../../../../_images/pingone-apps-enable-client-en.png)Figure 2. Enable the application using the toggle.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the JavaScript example PingOne applications and tutorials covered by this documentation.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the iOS OIDC sign-on module tutorial for Advanced Identity Cloud.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/ios/aic/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/ios/aic/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "iOS", "Advanced Identity Cloud", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: apple, set=fab]iOS

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-connection-properties.html)

* [Run](03_test-the-app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne Advanced Identity Cloud tenant.

## Prerequisites

* Xcode

  You can download the latest version for free from <https://developer.apple.com/xcode/>.

## Server configuration

This tutorial requires you to configure your PingOne Advanced Identity Cloud tenant as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Identities > Manage.
>
> 3. Click [icon: plus, set=fa]New Alpha realm - User.
>
> 4. Enter the following details:
>
>    * **Username** = `demo`
>
>    * **First Name** = `Demo`
>
>    * **Last Name** = `User`
>
>    * **Email Address** = `demo.user@example.com`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Create an authentication journey**
>
> Authentication journeys provide fine-grained authentication by allowing multiple paths and decision points throughout the flow. Authentication journeys are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> You'll need an authentication journey configured on your server to try out the **Journey** module. That journey must only use [nodes, and therefore callbacks, that the Orchestration SDKs supports](../../../../journey/compatibility.html#supported-authentication-journey-callbacks).
>
> |   |                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------- |
> |   | You can use the default **Login** journey that both Advanced Identity Cloud and PingAM include out-of-the-box. |
>
> To create your own authentication journey for use when testing the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Journeys, and click [icon: plus, set=fa]New Journey.
>
> 2. Enter a name, such as `sdkUsernamePasswordJourney` and click Save.
>
>    The authentication journey designer appears.
>
> 3. Drag the following nodes into the designer area:
>
>    * **Page Node**
>
>    * **Platform Username**
>
>    * **Platform Password**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Platform Username** and **Platform Password** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![sdk username password journey idcloud en](../../../../_images/sdk-username-password-journey-idcloud-en.png)Figure 1. Example username and password authentication journey
>
> 6. Click Save.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Native / SPA as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Public SDK Client`.
>
> 7. In Owners, select a user that is responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. In Client ID, enter `sdkPublicClient`
>
> 9. Select **Configure for SDK Sample Apps**.
>
> 10. Click Create Application.
>
>     PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 11. On the Sign On tab:
>
>     1. In Sign-In URLs, ensure the following values appear, or add them if they don't:
>
>        `com.example.demo://oauth2redirect`
>
>        |   |                                                             |
>        | - | ----------------------------------------------------------- |
>        |   | Also add any other domains where you host SDK applications. |
>
>     2. In Grant Types, ensure the following values appear:
>
>        `Authorization Code`
>
>        `Refresh Token`
>
>     3. In Scopes, ensure the following values appear:
>
>        `openid profile email address`
>
> 12. Click Show advanced settings, and on the Authentication tab, confirm the following properties:
>
>     1. In Token Endpoint Authentication Method, select `none`.
>
>     2. In Client Type, select `Public`.
>
>     3. Enable the Implied Consent property.
>
> 13. Click Save.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the example applications and tutorials covered by this documentation.

> **Collapse: Task 4. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingOne Advanced Identity Cloud OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Native Consoles > Access Management.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the iOS OIDC sign-on module tutorial for PingAM.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/ios/pingam/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/ios/pingam/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "iOS", "PingAM", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingAM [icon: apple, set=fab]iOS

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-connection-properties.html)

* [Run](03_test-the-app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingAM server.

## Prerequisites

* Xcode

  You can download the latest version for free from <https://developer.apple.com/xcode/>.

## Server configuration

This tutorial requires you to configure your PingAM server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingAM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: address-card, set=fa]Identities, and then click [icon: plus, set=fa]Add Identity.
>
> 3. Enter the following details:
>
>    * **User ID** = `demo`
>
>    * **Password** = `Ch4ng3it!`
>
>    * **Email Address** = `demo.user@example.com`
>
> 4. Click Create.

> **Collapse: Task 2. Create an authentication journey**
>
> Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow. Authentication trees are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> To create a simple tree for use when testing the Orchestration SDKs, follow these steps:
>
> 1. Under Realm Overview, click Authentication Trees, then click Create Tree.
>
> 2. Enter a tree name, for example `sdkUsernamePasswordJourney`, and then click Create.
>
>    The authentication tree designer appears, showing the Start entry point connected to the Failure exit point.
>
> 3. Drag the following nodes from the Components panel on the left side into the designer area:
>
>    * **Page Node**
>
>    * **Username Collector**
>
>    * **Password Collector**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Username Collector** and **Password Collector** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![trees node login example](../../../../_images/trees-node-login-example.png)Figure 1. Example username and password authentication tree
>
> 6. Select the **Page Node**, and in the Properties pane, set the Stage property to `UsernamePassword`.
>
>    |   |                                                                                                            |
>    | - | ---------------------------------------------------------------------------------------------------------- |
>    |   | You can configure the node properties by selecting a node and altering properties in the right-hand panel. |
>
>    One of the samples uses this specific value to determine the custom UI to display.
>
> 7. Click **Save**.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkPublicClient`.
>
> 4. Leave Client secret empty.
>
> 5. In Redirection URIs, enter the following values:
>
>    `com.example.demo://oauth2redirect`
>
>    |   |                                                                        |
>    | - | ---------------------------------------------------------------------- |
>    |   | Also add any other domains where you will be hosting SDK applications. |
>
> 6. In Scopes, enter the following values:
>
>    `openid profile email address`
>
> 7. Click Create.
>
>    PingAM creates the new OAuth 2.0 client, and displays the properties for further configuration.
>
> 8. On the Core tab:
>
>    1. In Client type, select `Public`.
>
>    2. Disable Allow wildcard ports in redirect URIs.
>
>    3. Click Save Changes.
>
> 9. On the Advanced tab:
>
>    1. In Grant Types, enter the following values:
>
>       ```none
>       Authorization Code
>       Refresh Token
>       ```
>
>    2. In Token Endpoint Authentication Method, select `None`.
>
>    3. Enable the Implied consent property.
>
> 10. Click Save Changes.

> **Collapse: Task 4. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingAM OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the iOS OIDC sign-on module tutorial for PingFederate.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/ios/pingfed/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/ios/pingfed/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "iOS", "PingFederate", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingFederate [icon: apple, set=fab]iOS

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-sample-for-pingfed.html)

* [Run](03_running-sample-pingfed.html)

To successfully complete this tutorial refer to the prerequisites and compatibility requirements in this section.

The tutorial also requires a configured PingFederate server.

## Prerequisites

* Xcode

  You can download the latest version for free from <https://developer.apple.com/xcode/>.

## Server configuration

This tutorial requires you to configure your PingFederate server as follows:

> **Collapse: Task 1. Register a public OAuth 2.0 client**
>
> OAuth 2.0 client application profiles define how applications connect to PingFederate and obtain OAuth 2.0 tokens.
>
> To allow the Orchestration SDKs to connect to PingFederate and obtain OAuth 2.0 tokens, you must register an OAuth 2.0 client application:
>
> 1. Log in to the PingFederate administration console as an administrator.
>
> 2. Navigate to **Applications** [icon: angle-right, set=fa] **OAuth** [icon: angle-right, set=fa] **Clients**.
>
> 3. Click **Add Client**.
>
>    PingFederate displays the **Clients | Client** page.
>
> 4. In **Client ID** and **Name**, enter a name for the profile, for example `sdkPublicClient`
>
>    Make a note of the **Client ID** value, you will need it when you configure the sample code.
>
> 5. In **Client Authentication**, select `None`.
>
> 6. In **Redirect URIs**, add the following:
>
>    `com.example.demo://oauth2redirect`
>
>    |   |                                                                                                                                                                                                                                                                                   |
>    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Also add any other URLs where you host SDK applications.Failure to add redirect URLs that exactly match your client app's values can cause PingFederate to display an error message such as `Redirect URI mismatch` when attempting to end a session by redirecting from the SDK. |
>
> 7. In **Allowed Grant Types**, select the following values:
>
>    `Authorization Code`
>
>    `Refresh Token`
>
> 8. In the **OpenID Connect** section:
>
>    1. In **Logout Mode**, select **Ping Front-Channel**
>
>    2. In **Front-Channel Logout URIs**, add the following:
>
>       `com.example.demo://oauth2redirect`
>
>       |   |                                                                                                                                                                                                                                                                                                                       |
>       | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Also add any other URLs that redirect users to PingFederate to end their session.Failure to add sign off URLs that exactly match your client app's values can cause PingFederate to display an error message such as `invalid post logout redirect URI` when attempting to end a session by redirecting from the SDK. |
>
>    3. In **Post-Logout Redirect URIs**, add the following:
>
>       `com.example.demo://oauth2redirect`
>
> 9. Click Save.
>
>    |   |                                                                                                                                                                                                                                                                                                  |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    |   | After changing PingFederate configuration using the administration console, you must replicate the changes to each server node in the cluster before they take effect.In the PingFederate administration console, navigate to **System > Server > Cluster Management**, and click **Replicate**. |
>
>    The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the Orchestration SDK PingFederate example applications and tutorials covered by this documentation.

> **Collapse: Task 2. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingFederate, you can configure CORS to allow browsers or apps from trusted domains to access protected resources.
>
> To configure CORS in PingFederate follow these steps:
>
> 1. Log in to the PingFederate administration console as an administrator.
>
> 2. Navigate to **System** [icon: angle-right, set=fa] **OAuth Settings** [icon: angle-right, set=fa] **Authorization Server Settings**.
>
> 3. In the **Cross-Origin Resource Sharing Settings** section, in the **Allowed Origin** field, enter any DNS aliases you use for your SDK apps.
>
>    This documentation assumes the following configuration:
>
>    | Property         | Values                              |
>    | ---------------- | ----------------------------------- |
>    | `Allowed Origin` | `com.example.demo://oauth2redirect` |
>
> 4. Click **Save**.
>
>    |   |                                                                                                                                                                                                                                                                                                  |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    |   | After changing PingFederate configuration using the administration console, you must replicate the changes to each server node in the cluster before they take effect.In the PingFederate administration console, navigate to **System > Server > Cluster Management**, and click **Replicate**. |
>
>    Your PingFederate server is now able to accept connections from origins hosting apps built with the Orchestration SDKs.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the iOS OIDC sign-on module tutorial for PingOne.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/ios/pingone/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/ios/pingone/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Thu, 2 Apr 2026 11:33:37 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "iOS", "PingOne", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  p1-server-ios: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: apple, set=fab]iOS

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-sample-for-pingone.html)

* [Run](03_running-sample-pingone.html)

To successfully complete this tutorial refer to the prerequisites and compatibility requirements in this section.

The tutorial also requires a [configured PingOne instance](#p1-server-ios).

## Prerequisites

* Xcode

  You can download the latest version for free from <https://developer.apple.com/xcode/>.

## Server configuration

This tutorial requires you to configure your PingOne server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Directory > Users.
>
> 3. Next to the Users label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add User panel.
>
> 4. Enter the following details:
>
>    * **Given Name** = `Demo`
>
>    * **Family Name** = `User`
>
>    * **Username** = `demo`
>
>    * **Email** = `demo.user@example.com`
>
>    * **Population** = `Default`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Register a public OAuth 2.0 client**
>
> To register a *public* OAuth 2.0 client application in PingOne for use with the Orchestration SDKs for Android and iOS, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Applications > Applications.
>
> 3. Next to the Applications label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add Application panel.
>
> 4. In Application Name, enter a name for the profile, for example `sdkNativeClient`
>
> 5. Select Native as the Application Type, and then click Save.
>
> 6. On the Configuration tab, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Grant Type, select the following values:
>
>       `Authorization Code`
>
>       `Refresh Token`
>
>    2. In Redirect URIs, enter the following values:
>
>       `com.example.demo://oauth2redirect`
>
>    3. In Token Endpoint Authentication Method, select `None`.
>
>    4. In the **Advanced Settings** section, enable **Terminate User Session by ID Token**.
>
>    5. Click Save.
>
> 7. On the Resources tab, next to Allowed Scopes, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Scopes, select the following values:
>
>       `email`
>
>       `phone`
>
>       `profile`
>
>       |   |                                            |
>       | - | ------------------------------------------ |
>       |   | The `openid` scope is selected by default. |
>
>       The result resembles the following:
>
>       ![Adding scopes to an application.](../../../../_images/pingone-oidc-native-scopes-en.png)Figure 1. Adding scopes to an application.
>
> 8. Optionally, on the Policies tab, click the pencil icon ([icon: pencil, set=fa]) to select the authentication policies for the application.
>
>    |   |                                                                                                                                        |
>    | - | -------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Applications that have no authentication policy assignments use the environment's default authentication policy to authenticate users. |
>
>    If you have a DaVinci license, you can select PingOne policies or DaVinci Flow policies, but not both. If you do not have a DaVinci license, the page only displays PingOne policies.
>
>    To use a *PingOne policy*:
>
>    1. Click [icon: plus, set=fa]Add policies and then select the policies that you want to apply to the application.
>
>    2. Click Save.
>
>       PingOne applies the policies in the order in which they appear in the list. PingOne evaluates the first policy in the list first. If the requirements are not met, PingOne moves to the next one.
>
>       For more information, see [Authentication policies for applications](https://docs.pingidentity.com/pingone/applications/p1_auth_policies_for_applications.html).
>
>    To use a *DaVinci Flow policy*:
>
>    1. You must clear all PingOne policies. Click Deselect all PingOne Policies.
>
>    2. In the confirmation message, click Continue.
>
>    3. On the DaVinci Policies tab, select the policies that you want to apply to the application.
>
>    4. Click Save.
>
>       PingOne applies the first policy in the list.
>
> 9. Click Save.
>
> 10. Enable the OAuth 2.0 client application by using the toggle next to its name:
>
>     ![Enable the application using the toggle.](../../../../_images/pingone-apps-enable-native-client-en.png)Figure 2. Enable the application using the toggle.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the Android and iOS PingOne example applications and tutorials covered by this documentation.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the React Native OIDC sign-on module tutorial for Advanced Identity Cloud.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/react-native/aic/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/react-native/aic/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "React Native", "Advanced Identity Cloud", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: react, set=fab]React Native

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-connection-properties.html)

* [Run](03_test-the-app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne Advanced Identity Cloud tenant.

## Prerequisites

* React Native

  This sample app requires React Native 0.80.1 or later.

* iOS

  This sample app requires iOS 17.0 or later.

* Android

  This sample app requires Android 11 (API level 30) or later.

The React Native development environment must be fully configured before you begin. Follow the official [React Native environment setup guide](https://reactnative.dev/docs/set-up-your-environment) and ensure the following tools are installed:

* Node.js and Yarn

  Install [Node.js](https://nodejs.org/) version 20 or later.

  This project uses Yarn. Install Yarn by running:

  ```shell
  corepack enable
  ```

* Xcode (iOS only)

  Download and install [Xcode](https://developer.apple.com/xcode/) from the Mac App Store.

  Xcode 15 or later is recommended.

* Ruby and Bundler (iOS only)

  Ruby 3.3.6 or later is required to manage CocoaPods.

  |   |                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | macOS ships with an older version of Ruby that is not compatible with this project.Install a current version using [rbenv](https://rbenv.org/) or a similar version manager before continuing. |

  Install [Bundler](https://bundler.io/) with:

  ```shell
  gem install bundler
  ```

* CocoaPods (iOS only)

  CocoaPods is installed locally during the tutorial. You do not need to install it globally.

* Android Studio (Android only)

  Download and install [Android Studio](https://developer.android.com/studio).

  An Android emulator or physical device is required to run the app. To add a virtual device, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds) on the Android Developers website.

* Java (Android only)

  Android Studio includes an embedded JDK.

  Java 21 is recommended and is bundled with recent versions of Android Studio.

* `keytool` (Android only)

  `keytool` is part of the Java Development Kit (JDK) and is used to generate the debug signing keystore required for the Android build. It is included with Android Studio's bundled JDK.

## Server configuration

This tutorial requires you to configure your PingOne Advanced Identity Cloud tenant as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Identities > Manage.
>
> 3. Click [icon: plus, set=fa]New Alpha realm - User.
>
> 4. Enter the following details:
>
>    * **Username** = `demo`
>
>    * **First Name** = `Demo`
>
>    * **Last Name** = `User`
>
>    * **Email Address** = `demo.user@example.com`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Create an authentication journey**
>
> Authentication journeys provide fine-grained authentication by allowing multiple paths and decision points throughout the flow. Authentication journeys are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> You'll need an authentication journey configured on your server to try out the **Journey** module. That journey must only use [nodes, and therefore callbacks, that the Orchestration SDKs supports](../../../../journey/compatibility.html#supported-authentication-journey-callbacks).
>
> |   |                                                                                                                |
> | - | -------------------------------------------------------------------------------------------------------------- |
> |   | You can use the default **Login** journey that both Advanced Identity Cloud and PingAM include out-of-the-box. |
>
> To create your own authentication journey for use when testing the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Journeys, and click [icon: plus, set=fa]New Journey.
>
> 2. Enter a name, such as `sdkUsernamePasswordJourney` and click Save.
>
>    The authentication journey designer appears.
>
> 3. Drag the following nodes into the designer area:
>
>    * **Page Node**
>
>    * **Platform Username**
>
>    * **Platform Password**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Platform Username** and **Platform Password** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![sdk username password journey idcloud en](../../../../_images/sdk-username-password-journey-idcloud-en.png)Figure 1. Example username and password authentication journey
>
> 6. Click Save.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Native / SPA as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Public SDK Client`.
>
> 7. In Owners, select a user that is responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. In Client ID, enter `sdkPublicClient`
>
> 9. Select **Configure for SDK Sample Apps**.
>
> 10. Click Create Application.
>
>     PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 11. On the Sign On tab:
>
>     1. In Sign-In URLs, ensure the following values appear, or add them if they don't:
>
>        `org.forgerock.oidc://oauth2redirect`
>
>        |   |                                                             |
>        | - | ----------------------------------------------------------- |
>        |   | Also add any other domains where you host SDK applications. |
>
>     2. In Grant Types, ensure the following values appear:
>
>        `Authorization Code`
>
>        `Refresh Token`
>
>     3. In Scopes, ensure the following values appear:
>
>        `openid profile email address`
>
> 12. Click Show advanced settings, and on the Authentication tab, confirm the following properties:
>
>     1. In Token Endpoint Authentication Method, select `none`.
>
>     2. In Client Type, select `Public`.
>
>     3. Enable the Implied Consent property.
>
> 13. Click Save.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the example applications and tutorials covered by this documentation.

> **Collapse: Task 4. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingOne Advanced Identity Cloud OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Native Consoles > Access Management.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the React Native OIDC sign-on module tutorial for PingAM.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/react-native/pingam/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/react-native/pingam/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "React Native", "PingAM", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingAM [icon: react, set=fab]React Native

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-connection-properties.html)

* [Run](03_test-the-app.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingAM server.

## Prerequisites

* React Native

  This sample app requires React Native 0.80.1 or later.

* iOS

  This sample app requires iOS 17.0 or later.

* Android

  This sample app requires Android 11 (API level 30) or later.

The React Native development environment must be fully configured before you begin. Follow the official [React Native environment setup guide](https://reactnative.dev/docs/set-up-your-environment) and ensure the following tools are installed:

* Node.js and Yarn

  Install [Node.js](https://nodejs.org/) version 20 or later.

  This project uses Yarn. Install Yarn by running:

  ```shell
  corepack enable
  ```

* Xcode (iOS only)

  Download and install [Xcode](https://developer.apple.com/xcode/) from the Mac App Store.

  Xcode 15 or later is recommended.

* Ruby and Bundler (iOS only)

  Ruby 3.3.6 or later is required to manage CocoaPods.

  |   |                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | macOS ships with an older version of Ruby that is not compatible with this project.Install a current version using [rbenv](https://rbenv.org/) or a similar version manager before continuing. |

  Install [Bundler](https://bundler.io/) with:

  ```shell
  gem install bundler
  ```

* CocoaPods (iOS only)

  CocoaPods is installed locally during the tutorial. You do not need to install it globally.

* Android Studio (Android only)

  Download and install [Android Studio](https://developer.android.com/studio).

  An Android emulator or physical device is required to run the app. To add a virtual device, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds) on the Android Developers website.

* Java (Android only)

  Android Studio includes an embedded JDK.

  Java 21 is recommended and is bundled with recent versions of Android Studio.

* `keytool` (Android only)

  `keytool` is part of the Java Development Kit (JDK) and is used to generate the debug signing keystore required for the Android build. It is included with Android Studio's bundled JDK.

## Server configuration

This tutorial requires you to configure your PingAM server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingAM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: address-card, set=fa]Identities, and then click [icon: plus, set=fa]Add Identity.
>
> 3. Enter the following details:
>
>    * **User ID** = `demo`
>
>    * **Password** = `Ch4ng3it!`
>
>    * **Email Address** = `demo.user@example.com`
>
> 4. Click Create.

> **Collapse: Task 2. Create an authentication tree**
>
> Authentication trees provide fine-grained authentication by allowing multiple paths and decision points throughout the authentication flow. Authentication trees are made up of nodes that define actions taken during authentication.
>
> Each node performs a single task, such as collecting a username or making a simple decision. Nodes can have multiple outcomes rather than just success or failure.
>
> To create a simple tree for use when testing the Orchestration SDKs, follow these steps:
>
> 1. Under Realm Overview, click Authentication Trees, then click Create Tree.
>
> 2. Enter a tree name, for example `sdkUsernamePasswordJourney`, and then click Create.
>
>    The authentication tree designer appears, showing the Start entry point connected to the Failure exit point.
>
> 3. Drag the following nodes from the Components panel on the left side into the designer area:
>
>    * **Page Node**
>
>    * **Username Collector**
>
>    * **Password Collector**
>
>    * **Data Store Decision**
>
> 4. Drag and drop the **Username Collector** and **Password Collector** nodes onto the **Page Node**, so that they both appear on the same page when logging in.
>
> 5. Connect the nodes as follows:
>
>    ![trees node login example](../../../../_images/trees-node-login-example.png)Figure 1. Example username and password authentication tree
>
> 6. Select the **Page Node**, and in the Properties pane, set the Stage property to `UsernamePassword`.
>
>    |   |                                                                                                            |
>    | - | ---------------------------------------------------------------------------------------------------------- |
>    |   | You can configure the node properties by selecting a node and altering properties in the right-hand panel. |
>
>    One of the samples uses this specific value to determine the custom UI to display.
>
> 7. Click **Save**.

> **Collapse: Task 3. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkPublicClient`.
>
> 4. Leave Client secret empty.
>
> 5. In Redirection URIs, enter the following values:
>
>    `org.forgerock.oidc://oauth2redirect`
>
>    |   |                                                                        |
>    | - | ---------------------------------------------------------------------- |
>    |   | Also add any other domains where you will be hosting SDK applications. |
>
> 6. In Scopes, enter the following values:
>
>    `openid profile email address`
>
> 7. Click Create.
>
>    PingAM creates the new OAuth 2.0 client, and displays the properties for further configuration.
>
> 8. On the Core tab:
>
>    1. In Client type, select `Public`.
>
>    2. Disable Allow wildcard ports in redirect URIs.
>
>    3. Click Save Changes.
>
> 9. On the Advanced tab:
>
>    1. In Grant Types, enter the following values:
>
>       ```none
>       Authorization Code
>       Refresh Token
>       ```
>
>    2. In Token Endpoint Authentication Method, select `None`.
>
>    3. Enable the Implied consent property.
>
> 10. Click Save Changes.

> **Collapse: Task 4. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingAM OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

---

---
title: Before you begin
description: Outlines the prerequisites and server configuration steps required before starting the React Native OIDC sign-on module tutorial for PingOne.
component: orchsdks
page_id: orchsdks:oidc:try-it-out/react-native/pingone/00_before-you-begin
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/try-it-out/react-native/pingone/00_before-you-begin.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
keywords: ["OAuth 2.0", "OpenID Connect", "Tutorial", "Source Code", "Integration", "SDK", "React Native", "PingOne", "prerequisites"]
section_ids:
  prerequisites: Prerequisites
  server_configuration: Server configuration
---

# Before you begin

[icon: circle-check, set=far]PingOne [icon: react, set=fab]React Native

* **Prepare**

* [Download](01_download-sample-repo.html)

* [Configure](02_configuring-sample-for-pingone.html)

* [Run](03_running-sample-pingone.html)

To successfully complete this tutorial refer to the prerequisites in this section.

The tutorial also requires a configured PingOne instance.

## Prerequisites

* React Native

  This sample app requires React Native 0.80.1 or later.

* iOS

  This sample app requires iOS 17.0 or later.

* Android

  This sample app requires Android 11 (API level 30) or later.

The React Native development environment must be fully configured before you begin. Follow the official [React Native environment setup guide](https://reactnative.dev/docs/set-up-your-environment) and ensure the following tools are installed:

* Node.js and Yarn

  Install [Node.js](https://nodejs.org/) version 20 or later.

  This project uses Yarn. Install Yarn by running:

  ```shell
  corepack enable
  ```

* Xcode (iOS only)

  Download and install [Xcode](https://developer.apple.com/xcode/) from the Mac App Store.

  Xcode 15 or later is recommended.

* Ruby and Bundler (iOS only)

  Ruby 3.3.6 or later is required to manage CocoaPods.

  |   |                                                                                                                                                                                                |
  | - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  |   | macOS ships with an older version of Ruby that is not compatible with this project.Install a current version using [rbenv](https://rbenv.org/) or a similar version manager before continuing. |

  Install [Bundler](https://bundler.io/) with:

  ```shell
  gem install bundler
  ```

* CocoaPods (iOS only)

  CocoaPods is installed locally during the tutorial. You do not need to install it globally.

* Android Studio (Android only)

  Download and install [Android Studio](https://developer.android.com/studio).

  An Android emulator or physical device is required to run the app. To add a virtual device, refer to [Create and manage virtual devices](https://developer.android.com/studio/run/managing-avds) on the Android Developers website.

* Java (Android only)

  Android Studio includes an embedded JDK.

  Java 21 is recommended and is bundled with recent versions of Android Studio.

* `keytool` (Android only)

  `keytool` is part of the Java Development Kit (JDK) and is used to generate the debug signing keystore required for the Android build. It is included with Android Studio's bundled JDK.

## Server configuration

This tutorial requires you to configure your PingOne server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Directory > Users.
>
> 3. Next to the Users label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add User panel.
>
> 4. Enter the following details:
>
>    * **Given Name** = `Demo`
>
>    * **Family Name** = `User`
>
>    * **Username** = `demo`
>
>    * **Email** = `demo.user@example.com`
>
>    * **Population** = `Default`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Register a public OAuth 2.0 client**
>
> To register a *public* OAuth 2.0 client application in PingOne for use with the Orchestration SDKs for Android and iOS, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Applications > Applications.
>
> 3. Next to the Applications label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add Application panel.
>
> 4. In Application Name, enter a name for the profile, for example `sdkNativeClient`
>
> 5. Select Native as the Application Type, and then click Save.
>
> 6. On the Configuration tab, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Grant Type, select the following values:
>
>       `Authorization Code`
>
>       `Refresh Token`
>
>    2. In Redirect URIs, enter the following values:
>
>       `org.forgerock.oidc://oauth2redirect`
>
>    3. In Token Endpoint Authentication Method, select `None`.
>
>    4. In the **Advanced Settings** section, enable **Terminate User Session by ID Token**.
>
>    5. Click Save.
>
> 7. On the Resources tab, next to Allowed Scopes, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Scopes, select the following values:
>
>       `email`
>
>       `phone`
>
>       `profile`
>
>       |   |                                            |
>       | - | ------------------------------------------ |
>       |   | The `openid` scope is selected by default. |
>
>       The result resembles the following:
>
>       ![Adding scopes to an application.](../../../../_images/pingone-oidc-native-scopes-en.png)Figure 1. Adding scopes to an application.
>
> 8. Optionally, on the Policies tab, click the pencil icon ([icon: pencil, set=fa]) to select the authentication policies for the application.
>
>    |   |                                                                                                                                        |
>    | - | -------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Applications that have no authentication policy assignments use the environment's default authentication policy to authenticate users. |
>
>    If you have a DaVinci license, you can select PingOne policies or DaVinci Flow policies, but not both. If you do not have a DaVinci license, the page only displays PingOne policies.
>
>    To use a *PingOne policy*:
>
>    1. Click [icon: plus, set=fa]Add policies and then select the policies that you want to apply to the application.
>
>    2. Click Save.
>
>       PingOne applies the policies in the order in which they appear in the list. PingOne evaluates the first policy in the list first. If the requirements are not met, PingOne moves to the next one.
>
>       For more information, see [Authentication policies for applications](https://docs.pingidentity.com/pingone/applications/p1_auth_policies_for_applications.html).
>
>    To use a *DaVinci Flow policy*:
>
>    1. You must clear all PingOne policies. Click Deselect all PingOne Policies.
>
>    2. In the confirmation message, click Continue.
>
>    3. On the DaVinci Policies tab, select the policies that you want to apply to the application.
>
>    4. Click Save.
>
>       PingOne applies the first policy in the list.
>
> 9. Click Save.
>
> 10. Enable the OAuth 2.0 client application by using the toggle next to its name:
>
>     ![Enable the application using the toggle.](../../../../_images/pingone-apps-enable-native-client-en.png)Figure 2. Enable the application using the toggle.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the Android and iOS PingOne example applications and tutorials covered by this documentation.

---

---
title: Compatibility
description: View supported servers, operating systems, and browsers for the OIDC module across Android, iOS, and JavaScript platforms
component: orchsdks
page_id: orchsdks:oidc:compatibility
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/compatibility.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 20 May 2023 16:11:17 +0100
keywords: ["Compatibility", "Features", "Source Code", "SDK"]
section_ids:
  supported-servers: Supported server versions
  supported-os: Supported operating systems and browsers
  webviews_unsupported_davinci: JavaScript Compatibility with WebViews
---

# Compatibility

## Supported server versions

The **OIDC** module is compatible with the following servers:

* PingOne

  Current version.

* PingOne Advanced Identity Cloud

  Current version.

* PingAM

  Currently supported versions.

  For information on supported PingAM versions, visit the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pam).

* PingFederate

  Currently supported versions.

  For information on supported PingFederate versions, visit the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pf).

* OIDC-spec compliant servers

  The **OIDC** module works with any server that fully implements the relevant OpenID Connect and OAuth 2.0 specifications.

  **Required specifications**

  | Specification                                                                                                                                   | Requirement                                                                                               | Notes                                                                                                                                                                                       |
  | ----------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | [OpenID Connect Discovery 1.0](https://openid.net/specs/openid-connect-discovery-1_0.html) / [RFC 8414](https://www.rfc-editor.org/rfc/rfc8414) | Expose a discovery document at `/.well-known/openid-configuration`, or at a URL the developer configures. | The Orchestration SDKs resolve all endpoint URLs from the discovery document.                                                                                                               |
  | [OIDC Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html) / [RFC 6749](https://www.rfc-editor.org/rfc/rfc6749)                     | Authorization endpoint, token endpoint, and UserInfo endpoint.                                            | The authorization endpoint must support `response_type=code`.The token endpoint must accept public clients that does not use a client secret, and the `client_id` is in the form body only. |
  | [RFC 7636](https://www.rfc-editor.org/rfc/rfc7636) - PKCE                                                                                       | Must accept `code_challenge_method=S256`.                                                                 | PKCE is used by the Orchestration SDKs whenever possible.                                                                                                                                   |
  | [RFC 7009](https://www.rfc-editor.org/rfc/rfc7009) - Token Revocation                                                                           | Token revocation endpoint advertised in the discovery document.                                           | The Orchestration SDKs revoke tokens on sign-out.Local token storage is cleared regardless of the server response.                                                                          |
  | [RP-Initiated Logout 1.0](https://openid.net/specs/openid-connect-rpinitiated-1_0.html)                                                         | End session endpoint advertised in the discovery document.                                                | The Orchestration SDKs require `end_session_endpoint` to be present in the discovery document.                                                                                              |

## Supported operating systems and browsers

Select a platform below to view the supported operating systems and browsers.

* Android

* iOS

* JavaScript / Login Widget

* React Native

The OIDC module for Android supports the following versions of the Android operating system:

**Supported Android versions and original release dates**

| Release    | API Levels | Release date    |
| ---------- | ---------- | --------------- |
| Android 17 | 37         | June, 2026      |
| Android 16 | 36         | August, 2025    |
| Android 15 | 35         | September, 2024 |
| Android 14 | 34         | October, 2023   |
| Android 13 | 33         | March, 2022     |
| Android 12 | 31, 32     | October, 2021   |
| Android 11 | 30         | September, 2020 |

|   |                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | We have updated how we determine which Android versions form our support policy for the OIDC module for Android.The support policy is as follows:- Every public major release of Android within the last 6 years.

  For example, this would mean support for **Android 11** and later versions. |

**Supported browsers on Android**

* Chrome - Two most recent major versions.

The OIDC module for iOS supports the following versions of the iOS operating system:

**Supported iOS versions and original release dates**

| Release | Release date    |
| ------- | --------------- |
| iOS 27  | September, 2026 |
| iOS 26  | September, 2025 |
| iOS 18  | September, 2024 |
| iOS 17  | September, 2023 |

|   |                                                                                                                                                                                                                                                                                  |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | We have updated how we determine which iOS versions form our support policy for the OIDC module for iOS.The support policy is as follows:- Every public major release of iOS within the last 3 years.

  For example, this would mean support for **iOS 17** and later versions. |

**Supported browsers on iOS**

* Safari - Two most recent major versions.

The OIDC module for JavaScript, and the Advanced Identity Cloud/PingAM Login Widget support the [desktop](#js-desktop-browsers) and [mobile](#js-desktop-browsers) browsers listed below.

**Minimum supported Desktop browser versions**

* Chrome 83

* Firefox 77

* Safari 13

* Microsoft Edge 83 (Chromium)

**Supported Mobile browsers**

* iOS (Safari) - Two most recent major versions of the operating system.

* Android (Chrome) - Two most recent major versions of the operating system.

The OIDC module for React Native wraps the native Android and iOS OIDC modules, so supported operating systems and browsers are a superset of the Android and iOS support listed in the tabs above.

Support depends on the platform the app runs on:

**Supported Android versions and original release dates**

| Release    | API Levels | Release date    |
| ---------- | ---------- | --------------- |
| Android 17 | 37         | June, 2026      |
| Android 16 | 36         | August, 2025    |
| Android 15 | 35         | September, 2024 |
| Android 14 | 34         | October, 2023   |
| Android 13 | 33         | March, 2022     |
| Android 12 | 31, 32     | October, 2021   |
| Android 11 | 30         | September, 2020 |

**Supported iOS versions and original release dates**

| Release | Release date    |
| ------- | --------------- |
| iOS 27  | September, 2026 |
| iOS 26  | September, 2025 |
| iOS 18  | September, 2024 |
| iOS 17  | September, 2023 |

### JavaScript Compatibility with WebViews

A WebView allows you to embed a web browser into your native Android or iOS application to display HTML pages, and run JavaScript apps.

For example, the Android system WebView is based on the Google Chrome engine, and the iOS WebView is based on the Safari browser engine.

However, it is important to note that WebViews do not implement the full feature set of their respective browsers. For example, some of the browser-provided APIs that the Orchestration SDK for JavaScript requires are not available in a WebView, such as the WebAuthn APIs.

In addition, there are concerns that a WebView does not provide the same level of security as their full browser counterparts.

As the SDK requires full, spec-compliant, browser-supplied APIs for full functionality we **do not** support usage within a WebView.

We also do not support or test usage with any wrappers around WebViews.

Whilst you might be able to implement simple use-cases using the Orchestration SDK for JavaScript within a WebView, we recommend that you use an alternative such as opening a full browser, or using an in-app instance of a full browser such as [Custom Tabs](https://developer.android.com/develop/ui/views/layout/webapps/overview-of-android-custom-tabs) for Android or [SFSafariViewController](https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller) for iOS.

---

---
title: Configuring Android apps for OIDC sign-on
description: Configure Android apps to use OIDC centralized sign-on with PingOne Advanced Identity Cloud, PingAM, or any OIDC-compliant authorization server
component: orchsdks
page_id: orchsdks:oidc:usage/android-centralized-login
canonical_url: https://developer.pingidentity.com/orchsdks/oidc/usage/android-centralized-login.html
llms_txt: https://developer.pingidentity.com/orchsdks/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: Tue, 17 Oct 2025 11:22:33 +0100
keywords: ["OAuth 2.0", "OpenID Connect", "Setup &amp; Configuration", "Source Code", "Integration", "SDK", "Android"]
section_ids:
  android_oidc_server_config: Before you begin
  android_oidc_redirects: Step 1. Configuring your app to handle redirects
  android_oidc_modules: Step 2. Installing modules
  android_oidc_properties: Step 3. Configuring connection properties
  android_oidc_full_configuration: Full configuration
  android_oidc_common_json_configuration: Common JSON configuration
  configuration_property_reference: Configuration property reference
  android_oidc_start_oauth2: Step 4. Starting the OAuth 2.0 flow
  android_oidc_access_token: Step 5. Obtaining an Access Token
  android_oidc_logout: Step 6. Revoking tokens and signing out
  android_oidc_tabs: Step 7. Customizing browser tabs
---

# Configuring Android apps for OIDC sign-on

[icon: circle-check, set=far]PingOne [icon: circle-check, set=far]PingOne Advanced Identity Cloud [icon: circle-check, set=far]PingAM [icon: circle-check, set=far]OIDC-compliant servers [icon: android, set=fab]Android

You can configure your Android apps to use your authorization server's UI, or your own web application, for sign-on requests.

When a user attempts to sign on to your app it redirects them to the central sign-on UI. After the user authenticates, the authorization server redirects them back to your application or site.

Changes to authentication journeys or flows on your authorization server are available to all your apps that use the OIDC sign-on method, without the need to rebuild or redistribute the app. Likewise, any rebranding applied to your central sign-on UI is reflected immediately in your client apps.

Your app doesn't need to access user credentials directly, just the result of the authentication from the server—usually an access token.

To configure an Android app to perform OIDC sign-on, complete each of the following steps:

* [Before you begin](#android_oidc_server_config)

* [Step 1. Configuring your app to handle redirects](#android_oidc_redirects)

* [Step 2. Installing modules](#android_oidc_modules)

* [Step 3. Configuring connection properties](#android_oidc_properties)

* [Step 4. Starting the OAuth 2.0 flow](#android_oidc_start_oauth2)

* [Step 5. Obtaining an Access Token](#android_oidc_access_token)

* [Step 6. Revoking tokens and signing out](#android_oidc_logout)

* [Step 7. Customizing browser tabs](#android_oidc_tabs)

## Before you begin

You need to prepare your server for OIDC sign-on. Select your server from the options below and complete the tasks before proceeding to configure your application.

* PingOne

* Advanced Identity Cloud

* AM

* PingFederate

This tutorial requires you to configure your PingOne server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Directory > Users.
>
> 3. Next to the Users label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add User panel.
>
> 4. Enter the following details:
>
>    * **Given Name** = `Demo`
>
>    * **Family Name** = `User`
>
>    * **Username** = `demo`
>
>    * **Email** = `demo.user@example.com`
>
>    * **Population** = `Default`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Register a public OAuth 2.0 client**
>
> To register a *public* OAuth 2.0 client application in PingOne for use with the Orchestration SDKs for Android and iOS, follow these steps:
>
> 1. Log in to your PingOne administration console.
>
> 2. In the left panel, navigate to Applications > Applications.
>
> 3. Next to the Applications label, click the plus icon ([icon: plus, set=fa]).
>
>    PingOne displays the Add Application panel.
>
> 4. In Application Name, enter a name for the profile, for example `sdkNativeClient`
>
> 5. Select Native as the Application Type, and then click Save.
>
> 6. On the Configuration tab, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Grant Type, select the following values:
>
>       `Authorization Code`
>
>       `Refresh Token`
>
>    2. In Redirect URIs, enter the following values:
>
>       `com.example.demo://oauth2redirect`
>
>    3. In Token Endpoint Authentication Method, select `None`.
>
>    4. In the **Advanced Settings** section, enable **Terminate User Session by ID Token**.
>
>    5. Click Save.
>
> 7. On the Resources tab, next to Allowed Scopes, click the pencil icon ([icon: pencil, set=fa]).
>
>    1. In Scopes, select the following values:
>
>       `email`
>
>       `phone`
>
>       `profile`
>
>       |   |                                            |
>       | - | ------------------------------------------ |
>       |   | The `openid` scope is selected by default. |
>
>       The result resembles the following:
>
>       ![Adding scopes to an application.](../../_images/pingone-oidc-native-scopes-en.png)Figure 1. Adding scopes to an application.
>
> 8. Optionally, on the Policies tab, click the pencil icon ([icon: pencil, set=fa]) to select the authentication policies for the application.
>
>    |   |                                                                                                                                        |
>    | - | -------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Applications that have no authentication policy assignments use the environment's default authentication policy to authenticate users. |
>
>    If you have a DaVinci license, you can select PingOne policies or DaVinci Flow policies, but not both. If you do not have a DaVinci license, the page only displays PingOne policies.
>
>    To use a *PingOne policy*:
>
>    1. Click [icon: plus, set=fa]Add policies and then select the policies that you want to apply to the application.
>
>    2. Click Save.
>
>       PingOne applies the policies in the order in which they appear in the list. PingOne evaluates the first policy in the list first. If the requirements are not met, PingOne moves to the next one.
>
>       For more information, see [Authentication policies for applications](https://docs.pingidentity.com/pingone/applications/p1_auth_policies_for_applications.html).
>
>    To use a *DaVinci Flow policy*:
>
>    1. You must clear all PingOne policies. Click Deselect all PingOne Policies.
>
>    2. In the confirmation message, click Continue.
>
>    3. On the DaVinci Policies tab, select the policies that you want to apply to the application.
>
>    4. Click Save.
>
>       PingOne applies the first policy in the list.
>
> 9. Click Save.
>
> 10. Enable the OAuth 2.0 client application by using the toggle next to its name:
>
>     ![Enable the application using the toggle.](../../_images/pingone-apps-enable-native-client-en.png)Figure 2. Enable the application using the toggle.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the Android and iOS PingOne example applications and tutorials covered by this documentation.

This tutorial requires you to configure your PingOne Advanced Identity Cloud tenant as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Identities > Manage.
>
> 3. Click [icon: plus, set=fa]New Alpha realm - User.
>
> 4. Enter the following details:
>
>    * **Username** = `demo`
>
>    * **First Name** = `Demo`
>
>    * **Last Name** = `User`
>
>    * **Email Address** = `demo.user@example.com`
>
>    * **Password** = `Ch4ng3it!`
>
> 5. Click Save.

> **Collapse: Task 2. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in PingOne Advanced Identity Cloud, follow these steps:
>
> 1. Log in to your PingOne Advanced Identity Cloud tenant.
>
> 2. In the left panel, click Applications.
>
> 3. Click [icon: plus, set=fa]Custom Application.
>
> 4. Select OIDC - OpenId Connect as the sign-in method, and then click Next.
>
> 5. Select Native / SPA as the application type, and then click Next.
>
> 6. In Name, enter a name for the application, such as `Public SDK Client`.
>
> 7. In Owners, select a user that is responsible for maintaining the application, and then click Next.
>
>    |   |                                                                                    |
>    | - | ---------------------------------------------------------------------------------- |
>    |   | When trying out the SDKs, you could select the `demo` user you created previously. |
>
> 8. In Client ID, enter `sdkPublicClient`
>
> 9. Select **Configure for SDK Sample Apps**.
>
> 10. Click Create Application.
>
>     PingOne Advanced Identity Cloud creates the application and displays the details screen.
>
> 11. On the Sign On tab:
>
>     1. In Sign-In URLs, ensure the following values appear, or add them if they don't:
>
>        `com.example.demo://oauth2redirect`
>
>        `https://demo.example.com/oauth2redirect`
>
>        |   |                                                             |
>        | - | ----------------------------------------------------------- |
>        |   | Also add any other domains where you host SDK applications. |
>
>     2. In Grant Types, ensure the following values appear:
>
>        `Authorization Code`
>
>        `Refresh Token`
>
>     3. In Scopes, ensure the following values appear:
>
>        `openid profile email address`
>
> 12. Click Show advanced settings, and on the Authentication tab, confirm the following properties:
>
>     1. In Token Endpoint Authentication Method, select `none`.
>
>     2. In Client Type, select `Public`.
>
>     3. Enable the Implied Consent property.
>
> 13. Click Save.
>
> The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the example applications and tutorials covered by this documentation.

> **Collapse: Task 3. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingOne Advanced Identity Cloud OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. In your PingOne Advanced Identity Cloud tenant, navigate to Native Consoles > Access Management.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

This tutorial requires you to configure your AM server as follows:

> **Collapse: Task 1. Create a demo user**
>
> The samples and tutorials in this documentation often require that you have an identity set up so that you can test authentication.
>
> To create a demo user in PingAM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: address-card, set=fa]Identities, and then click [icon: plus, set=fa]Add Identity.
>
> 3. Enter the following details:
>
>    * **User ID** = `demo`
>
>    * **Password** = `Ch4ng3it!`
>
>    * **Email Address** = `demo.user@example.com`
>
> 4. Click Create.

> **Collapse: Task 2. Register a public OAuth 2.0 client**
>
> Public clients do not use a client secret to obtain tokens because they are unable to keep them hidden. The Orchestration SDKs commonly use this type of client to obtain tokens, as they cannot guarantee safekeeping of the client credentials in a browser or on a mobile device.
>
> To register a *public* OAuth 2.0 client application for use with the SDKs in AM, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. Navigate to [icon: list-alt, set=fa]Applications > OAuth 2.0 > Clients, and then click [icon: plus, set=fa]Add Client.
>
> 3. In Client ID, enter `sdkPublicClient`.
>
> 4. Leave Client secret empty.
>
> 5. In Redirection URIs, enter the following values:
>
>    `com.example.demo://oauth2redirect`
>
>    https\://demo.example.com/oauth2redirect
>
>    |   |                                                                        |
>    | - | ---------------------------------------------------------------------- |
>    |   | Also add any other domains where you will be hosting SDK applications. |
>
> 6. In Scopes, enter the following values:
>
>    `openid profile email address`
>
> 7. Click Create.
>
>    PingAM creates the new OAuth 2.0 client, and displays the properties for further configuration.
>
> 8. On the Core tab:
>
>    1. In Client type, select `Public`.
>
>    2. Disable Allow wildcard ports in redirect URIs.
>
>    3. Click Save Changes.
>
> 9. On the Advanced tab:
>
>    1. In Grant Types, enter the following values:
>
>       ```none
>       Authorization Code
>       Refresh Token
>       ```
>
>    2. In Token Endpoint Authentication Method, select `None`.
>
>    3. Enable the Implied consent property.
>
> 10. Click Save Changes.

> **Collapse: Task 3. Configure the OAuth 2.0 provider**
>
> The provider specifies the supported OAuth 2.0 configuration options for a realm.
>
> To ensure the PingAM OAuth 2.0 provider service is configured for use with the Orchestration SDKs, follow these steps:
>
> 1. Log in to the PingAM admin UI as an administrator.
>
> 2. In the left panel, click [icon: plug, set=fa]Services.
>
> 3. In the list of services, click OAuth2 Provider.
>
> 4. On the Core tab, ensure Issue Refresh Tokens is enabled.
>
> 5. On the Consent tab, ensure Allow Clients to Skip Consent is enabled.
>
> 6. Click Save Changes.

This tutorial requires you to configure your PingFederate server as follows:

> **Collapse: Task 1. Register a public OAuth 2.0 client**
>
> OAuth 2.0 client application profiles define how applications connect to PingFederate and obtain OAuth 2.0 tokens.
>
> To allow the Orchestration SDKs to connect to PingFederate and obtain OAuth 2.0 tokens, you must register an OAuth 2.0 client application:
>
> 1. Log in to the PingFederate administration console as an administrator.
>
> 2. Navigate to **Applications** [icon: angle-right, set=fa] **OAuth** [icon: angle-right, set=fa] **Clients**.
>
> 3. Click **Add Client**.
>
>    PingFederate displays the **Clients | Client** page.
>
> 4. In **Client ID** and **Name**, enter a name for the profile, for example `sdkPublicClient`
>
>    Make a note of the **Client ID** value, you will need it when you configure the sample code.
>
> 5. In **Client Authentication**, select `None`.
>
> 6. In **Redirect URIs**, add the following:
>
>    `com.example.demo://oauth2redirect`
>
>    https\://demo.example.com/oauth2redirect
>
>    |   |                                                                                                                                                                                                                                                                                   |
>    | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>    |   | Also add any other URLs where you host SDK applications.Failure to add redirect URLs that exactly match your client app's values can cause PingFederate to display an error message such as `Redirect URI mismatch` when attempting to end a session by redirecting from the SDK. |
>
> 7. In **Allowed Grant Types**, select the following values:
>
>    `Authorization Code`
>
>    `Refresh Token`
>
> 8. In the **OpenID Connect** section:
>
>    1. In **Logout Mode**, select **Ping Front-Channel**
>
>    2. In **Front-Channel Logout URIs**, add the following:
>
>       `com.example.demo://oauth2redirect`
>
>       https\://demo.example.com/oauth2redirect
>
>       |   |                                                                                                                                                                                                                                                                                                                       |
>       | - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
>       |   | Also add any other URLs that redirect users to PingFederate to end their session.Failure to add sign off URLs that exactly match your client app's values can cause PingFederate to display an error message such as `invalid post logout redirect URI` when attempting to end a session by redirecting from the SDK. |
>
>    3. In **Post-Logout Redirect URIs**, add the following:
>
>       `com.example.demo://oauth2redirect`
>
>       https\://demo.example.com/oauth2redirect
>
> 9. Click Save.
>
>    |   |                                                                                                                                                                                                                                                                                                  |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    |   | After changing PingFederate configuration using the administration console, you must replicate the changes to each server node in the cluster before they take effect.In the PingFederate administration console, navigate to **System > Server > Cluster Management**, and click **Replicate**. |
>
>    The application is now configured to accept client connections from and issue OAuth 2.0 tokens to the Orchestration SDK PingFederate example applications and tutorials covered by this documentation.

> **Collapse: Task 2. Configure CORS**
>
> [Cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) (CORS) lets user agents make cross-domain server requests. In PingFederate, you can configure CORS to allow browsers or apps from trusted domains to access protected resources.
>
> To configure CORS in PingFederate follow these steps:
>
> 1. Log in to the PingFederate administration console as an administrator.
>
> 2. Navigate to **System** [icon: angle-right, set=fa] **OAuth Settings** [icon: angle-right, set=fa] **Authorization Server Settings**.
>
> 3. In the **Cross-Origin Resource Sharing Settings** section, in the **Allowed Origin** field, enter any DNS aliases you use for your SDK apps.
>
>    This documentation assumes the following configuration:
>
>    | Property         | Values                              |
>    | ---------------- | ----------------------------------- |
>    | `Allowed Origin` | `com.example.demo://oauth2redirect` |
>
> 4. Click **Save**.
>
>    |   |                                                                                                                                                                                                                                                                                                  |
>    | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
>    |   | After changing PingFederate configuration using the administration console, you must replicate the changes to each server node in the cluster before they take effect.In the PingFederate administration console, navigate to **System > Server > Cluster Management**, and click **Replicate**. |
>
>    Your PingFederate server is now able to accept connections from origins hosting apps built with the Orchestration SDKs.

## Step 1. Configuring your app to handle redirects

After completing authentication in the browser, the server redirects the user back to your application, by using the value of the `redirect_uri` parameter.

You need to configure your app to open and accept the data the server sends as part of the redirect.

There are two methods for configuring an Android app to handle redirect URIs. To ensure that only your app is able to obtain authorization tokens during OIDC sign-on we recommend you configure it to use [Android App Links](https://developer.android.com/studio/write/app-link-indexing).

If you don't want to implement Android App Links, you can instead use a custom scheme for your redirect URIs.

* Android App Links / HTTPS

* Custom Scheme

You can configure your Android app to open and handle redirects that match the base domain of your authorization server, and use the HTTPS protocol.

Using this method, your redirect URI will resemble the following:

`https://demo.example.com/oauth2redirect`

To configure App Links in an Android application, perform the following steps:

1. In your application, configure the Orchestration SDK `browser` module to use the HTTPS scheme for capturing redirect URIs, by adding an `<intent-filter>` for `com.pingidentity.browser.CustomTabActivity` to your `AndroidManifest.xml`:

   AndroidManifest.xml

   ```xml
   <activity
       android:name="com.pingidentity.browser.CustomTabActivity"
       android:exported="true"
       android:launchMode="singleTop">
       <intent-filter android:autoVerify="true">
           <action android:name="android.intent.action.VIEW" />

           <category android:name="android.intent.category.DEFAULT" />
           <category android:name="android.intent.category.BROWSABLE" />

           <data android:scheme="https" />
           <data android:host="demo.example.com" />
           <data android:path="/oauth2redirect" />
       </intent-filter>
   </activity>
   ```

   * You must set `android:autoVerify` to `true`. This instructs Android to verify the specified host against the `assetlinks.json` file you update in the next step.

   * Specify the `scheme`, `hosts`, and `path` parameters to use in your redirect URIs. The host value must match the domain where you upload the `assetlinks.json` file.

   To learn more about intents, refer to [Add intent filters](https://developer.android.com/studio/write/app-link-indexing#intent) in the Android Developer documentation.

2. For Android 11 or higher, add the following to the `AndroidManfest.xml` file:

   AndroidManifest.xml

   ```xml
   <queries>
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="https" />
        </intent>
    </queries>
   ```

3. Create or update a Digital Asset Links (`assetlinks.json`) file that associates your app with your domain.

   You must host the file in a `.well-known` folder on the same host that you entered in the intent filter earlier.

   The file will resemble the following:

   https\://demo.example.com/.well-known/assetlinks.json

   ```json
   [
     {
       "relation": [
         "delegate_permission/common.handle_all_urls",
       ],
       "target": {
         "namespace": "android_app",
         "package_name": "com.example.demo",
         "sha256_cert_fingerprints": [
           "c4:15:c8:f1:...:fe:ce:d7:37"
         ]
       }
     }
   ]
   ```

   * To learn more, refer to [Associate your app with your website](https://developer.android.com/studio/write/app-link-indexing#associatesite) in the Android Developer documentation.

4. Upload the completed file to the domain that matches the host value you configured in the earlier step.

   For information on uploading an `assetLinks.json` file to an Advanced PingOne Advanced Identity Cloud instance, refer to [Upload an Android assetlinks.json file](https://docs.pingidentity.com/pingoneaic/latest/end-user/upload-android-assetlinks.html).

You can configure your Android app to open and handle redirects that use a custom scheme, rather than HTTPS.

Using this method, your redirect URI will resemble the following:

`com.example.demo://oauth2redirect`

To configure a custom scheme in an Android application, perform the following steps:

1. Add the custom scheme your app will use to your `gradle.build.kts` file:

   ```gradle
   android {
       defaultConfig {
           manifestPlaceholders["appRedirectUriScheme"] = "com.example.demo"
       }
   }
   ```

   |   |                                                                                       |
   | - | ------------------------------------------------------------------------------------- |
   |   | The custom scheme consists of the string before the colon (`:`) character in the URI. |

2. For Android 11 or higher, add the following to the `AndroidManfest.xml` file:

   ```xml
   <queries>
        <intent>
            <action android:name="android.intent.action.VIEW" />
            <category android:name="android.intent.category.BROWSABLE" />
            <data android:scheme="com.example.demo" />
        </intent>
    </queries>
   ```

## Step 2. Installing modules

For OIDC sign-on, you need these modules:

* `oidc`

* `browser`

To install these modules into your Android app:

1. In the **Project** tree view of your Android Studio project, open the `build.gradle.kts` file.

2. In the `dependencies` section, add the `oidc` and `browser` modules as dependencies:

   ```gradle
   dependencies {
       implementation("com.pingidentity.sdks:oidc:2.2.0")
       implementation("com.pingidentity.sdks:browser:2.2.0")
   }
   ```

## Step 3. Configuring connection properties

Configure the `oidc` module to connect to your OpenID Connect 1.0-compliant authorization server.

There are two methods for configuring the `oidc` module:

* [Full configuration](#android_oidc_full_configuration)

  Use the Kotlin builder DSL to access all available settings, including Android-specific options such as custom HTTP clients and storage configuration.

* [Common JSON configuration](#android_oidc_common_json_configuration)

  Use a shared key-value structure that works identically across Android, iOS, and JavaScript, letting you load a single config file across platforms.

### Full configuration

Configure the `oidc` module

```kotlin
val oidcClient = OidcWebClient {
    logger = Logger.STANDARD
    module(com.pingidentity.oidc.module.Oidc) {
        discoveryEndpoint =
            "https://auth.pingone.ca/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration"
        clientId = "6c7eb89a-66e9-ab12-cd34-eeaf795650b2"
        redirectUri = "https://demo.example.com/oath2redirect"
        scopes = mutableSetOf("openid", "email", "address", "profile", "phone")
        par = true
    }
}
```

### Common JSON configuration

You can provide the same OIDC configuration as a JSON object, which lets you share a single config file across Android, iOS, and JavaScript.

Configure `OidcWebClient` from a JSON object

```kotlin
val oidcClient = OidcWebClient(buildJsonObject {
    put("timeout", 30000) // milliseconds
    put("log", "WARN")
    putJsonObject("oidc") {
        put("clientId", "6c7eb89a-66e9-ab12-cd34-eeaf795650b2")
        put("discoveryEndpoint",
            "https://auth.pingone.ca/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration")
        putJsonArray("scopes") { add("openid"); add("profile"); add("email") }
        put("redirectUri", "com.example.demo://oauth2redirect")
        put("par", true)
    }
}).getOrThrow()
```

Optionally, you can store this JSON in a file alongside your app and load it at runtime so the same file can be shared across platforms.

JSON configuration supports the common properties that work across all platforms.

|   |                                                                                                                                                                                                                                                                        |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The JSON factory and the native `OidcWebClient {}` builder DSL are mutually exclusive, there is no combined form.If you need Android-specific settings such as `httpClient` or storage configuration, use the native builder DSL for the entire configuration instead. |

### Configuration property reference

The following properties are available when configuring the `oidc` module for Android.

The **JSON property** column shows the equivalent key when using JSON configuration.

**OIDC module configuration properties for Android**

| Property               | JSON property               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Required? |
| ---------------------- | --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| `logger`               | `log`                       | The logger the module uses to output messages.Choose from `STANDARD`, `WARN`, or `NONE`, or specify a custom logger to use.Learn more in [Customizing logging on Android](../customization/logging/android-custom-logging.html).In JSON configuration, use the `log` property at the root level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | No        |
| `timeout`              | `timeout`                   | A timeout, in milliseconds, for each request that communicates with the server.For example, for 30 seconds specify `30000`.When using JSON configuration, specify `timeout` at the root level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No        |
| `acrValues`            | `oidc.acrValues`            | An optional space-separated list of Authentication Context Class Reference (`acr`) values, in order of preference.The server can use these values to help determine how the user should be authenticated as part of the OIDC flow\.Before you specify an `acr` value, configure your server to map it to a specific authentication path:- PingOne

  Map `acrValues` to a DaVinci flow policy ID.

  Learn more in [Invoking the flow](https://docs.pingidentity.com/davinci/integrating_flows_into_applications/davinci_launch_flow_redirect.html#invoking-the-flow).

- PingOne Advanced Identity Cloud

  Map `acrValues` to a journey.

  Learn more in [The acr claim](https://docs.pingidentity.com/pingoneaic/latest/am-oidc1/oidc-authentication-requirements.html#acr-claim).

- PingAM

  Map `acrValues` to an authentication tree.

  Learn more in [The acr claim](https://docs.pingidentity.com/pingam/8.1/am-oidc1/oidc-authentication-requirements.html#acr-claim).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No        |
| `clientId`             | `oidc.clientId`             | The client ID of your OAuth 2.0 application.For example, `6c7eb89a-66e9-ab12-cd34-eeaf795650b2`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Yes       |
| `discoveryEndpoint`    | `oidc.discoveryEndpoint`    | The `.well-known` endpoint from your OAuth 2.0 application.> **Collapse: How do I find my PingOne .well-known URL?**
>
> To find the `.well-known` endpoint for an OAuth 2.0 client in PingOne:
>
> 1. Log in to your PingOne administration console.
>
> 2. Go to **Applications > Applications**, and then select your OAuth 2.0 client.
>
>    For example, sdkPublicClient.
>
> 3. On the **Overview** tab, expand the **Connection Details** section, and then copy the **OIDC Discovery Endpoint** value.
>
>    ![Locating the .well-known URL in a PingOne client profile.](../../_images/p1-client-well-known.png)> **Collapse: How do I form my PingFederate .well-known URL?**
>
> To form the `.well-known` endpoint for a PingFederate server:
>
> 1. Log in to your PingFederate administration console.
>
> 2. Navigate to **System** [icon: angle-right, set=fa] **Server** [icon: angle-right, set=fa] **Protocol Settings**.
>
> 3. Make a note of the **Base URL** value.
>
>    For example, `https://pingfed.example.com`
>
>    Do not use the admin console URL.
>
> 4. Append `/.well-known/openid-configuration` after the base URL value to form the `.well-known` endpoint of your server.
>
>    For example, `https://pingfed.example.com/.well-known/openid-configuration`.
>
>    The SDK reads the OAuth 2.0 paths it requires from this endpoint.> **Collapse: How do I find my PingOne Advanced Identity Cloud  URL?**
>
> You can view the `.well-known` endpoint for an OAuth 2.0 client in the PingOne Advanced Identity Cloud admin console:
>
> 1. Log in to your PingOne Advanced Identity Cloud administration console.
>
> 2. Click Applications, and then select the OAuth 2.0 client you created earlier. For example, sdkPublicClient.
>
> 3. On the Sign On tab, in the Client Credentials section, copy the Discovery URI value.
>
>    For example, `https://openam-forgerock-sdks.forgeblocks.com/am/oauth2/alpha/.well-known/openid-configuration`
>
> &#xA;&#xA;If you are using a custom domain, your .well-known is formed as follows:&#xA;&#xA;https\://\<custom-domain-fqdn>/.well-known/openid-configuration&#xA;&#xA;Learn more in Access OIDC configuration discovery endpoint.> **Collapse: How do I find my PingAM  URL?**
>
> To form the `.well-known` URL for an PingAM server, concatenate the following information into a single URL:
>
> 1. The base URL of the PingAM component of your deployment, including the port number and deployment path.
>
>    For example, `https://openam.example.com:8443/openam`
>
> 2. The string `/oauth2`
>
> 3. The hierarchy of the realm that contains the OAuth 2.0 client.
>
>    You must specify the entire hierarchy of the realm, starting at the Top Level Realm. Prefix each realm in the hierarchy with the `realms/` keyword.
>
>    For example, `/realms/root/realms/customers`
>
>    &#xA;&#xA;If you omit the realm hierarchy, the top level ROOT realm is used by default.
>
> 4. The string `/.well-known/openid-configuration`
>
> For example, `https://openam.example.com:8443/openam/oauth2/realms/root/.well-known/openid-configuration`For example, `https://auth.pingone.ca/3072206d-c6ce-ch15-m0nd-f87e972c7cc3/as/.well-known/openid-configuration` | Yes       |
| `loginHint`            | `oidc.loginHint`            | An optional string that lets the server know what identifier the user might use to authenticate with.The server can use this to pre-populate a sign-on form, or to customize the UI to match a particular brand or organization.The Orchestration SDK sends this as the `login_hint` parameter in the authentication request, as per the specification.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | No        |
| `par`                  | `oidc.par`                  | Whether to use Pushed Authorization Requests (PAR) for communicating with the authorization server.Learn more in [Securing OIDC sign-on with Pushed Authorization Requests](../use-cases/par/index.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No        |
| `redirectUri`          | `oidc.redirectUri`          | The redirect URI as configured in the OAuth 2.0 client profile.This value must exactly match one of the values configured in your OAuth 2.0 client.App link / HTTPS redirect URI: `https://demo.example.com/oauth2redirect`Custom scheme redirect URI: `com.example.demo://oauth2redirect`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Yes       |
| `scopes`               | `oidc.scopes`               | The scopes you added to your OAuth 2.0 application.For example, `"openid", "email", "address", "profile", "phone"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Yes       |
| `additionalParameters` | `oidc.additionalParameters` | Add any additional key-value query parameters your environment might require to complete an OAuth 2.0 flow.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | No        |
| `display`              | `oidc.display`              | How the authorization server should display the authentication UI.- `page`

  Full-page redirect (default).

- `popup`

  Pop-up window.

- `touch`

  Optimized for touch-based devices.

- `wap`

  Optimized for WAP/mobile browsers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No        |
| `nonce`                | `oidc.nonce`                | A value to associate with the ID token to prevent replay attacks.If not set, the SDK generates a nonce automatically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | No        |
| `prompt`               | `oidc.prompt`               | Controls whether the authorization server prompts the user for re-authentication or consent.- `none`

  No UI; returns an error if interaction is required.

- `login`

  Force re-authentication.

- `consent`

  Request consent even if previously granted.

- `select_account`

  Prompt to select an account.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | No        |
| `refreshThreshold`     | `oidc.refreshThreshold`     | The number of seconds before token expiry at which the SDK proactively refreshes the token.Defaults to `0`, meaning the SDK refreshes only when the token has expired.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | No        |
| `signOutRedirectUri`   | `oidc.signOutRedirectUri`   | The URI to redirect to after sign-out.Maps to the `post_logout_redirect_uri` parameter in the end-session request.This value must be registered in your OAuth 2.0 client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | No        |
| `uiLocales`            | `oidc.uiLocales`            | Space-separated BCP 47 language tags indicating the preferred display language for the authorization server's UI.For example, `en-US fr`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No        |

Learn more about OAuth 2.0 authentication request parameters in [Authentication Request](https://openid.net/specs/openid-connect-core-1_0.html#AuthRequest), in the *OpenID Connect Core 1.0* specification.

## Step 4. Starting the OAuth 2.0 flow

The `oidc` module provides the `authorize()` method, which launches the web browsers and starts the OAuth 2.0 flow.

Start the OAuth 2.0 flow by using the `authorize()` method

```kotlin
oidcClient.authorize()
  .onSuccess { user ->
    ...
  }.onFailure { throwable ->
    ...
  }
```

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| - | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | You can inject or override OAuth 2.0 parameters, and pass custom key-pair values when starting the OAuth 2.0 flow with the `authorize()` method.Adding parameters when using the `authorize()` method```kotlin
oidcClient.authorize(
    "customParameter" to "my_custom_value"
).onSuccess { user ->
    ...
  }.onFailure { throwable ->
    ...
  }
```If you've already set a value using a dedicated configuration property, such as `acrValues` or `loginHint`, passing the same key to `authorize()` duplicates the parameter in the request rather than overriding it, and may have unexpected consequences. |

## Step 5. Obtaining an Access Token

After successfully starting the OAuth 2.0 flow and authenticating the user, the server redirects control back to your application. Your application receives the OAuth 2.0 `code` and `state` parameters it needs to continue the flow and obtain an access token.

To obtain an access token on behalf of a user, follow these steps:

1. Create an object that represents a user's authentication session by using the `user()` method:

   Create a user object by calling the `user()` method

   ```kotlin
   val user = oidcClient.user()
   ```

2. Retrieve a token on behalf of the user by calling the `token()` method on your `user` object, and handle the result:

   Obtain an access token for a user by calling `user.token()` and handle the result

   ```kotlin
   when (val result = user.token()) {
       is Result.Failure -> {
           when (result.value) {
               is OidcError.ApiError -> TODO()
               is OidcError.AuthenticationRequired -> TODO()
               is OidcError.AuthorizeError -> TODO()
               is OidcError.NetworkError -> TODO()
               is OidcError.Unknown -> TODO()
           }
       }
       is Result.Success -> {
           val accessToken = result.value
       }
   }
   ```

## Step 6. Revoking tokens and signing out

You can call the following methods on your `user` object to revoke OAuth 2.0 tokens, and sign out the user from the server:

* `user.revoke()`

  Revokes the OAuth 2.0 tokens on the server, and deletes them from storage.

* `user.logout()`

  Removes an session tokens the user may have, and contacts the server to end the user's session.

## Step 7. Customizing browser tabs

The **OIDC** module uses Auth Tabs for OIDC sign-on where possible, and falls back to use a custom tab if not.

You can customize aspects of how both of these appear in your app:

* Auth tabs

  Auth Tabs provide enhanced security features for OAuth 2.0 flows and are automatically used when supported by the device and when the redirect URI uses a custom scheme.

  Learn more in [Simplify authentication using Auth Tab](https://developer.chrome.com/docs/android/custom-tabs/guide-auth-tab) in the *Chrome for Developers* documentation.

  To customize the auth tab, add your preferred configuration to `BrowserLauncher.authTabCustomizer` before you call `authorize()`, as follows:

  Customizing auth tabs on Android

  ```kotlin
  BrowserLauncher.authTabCustomizer = {
      setColorScheme(CustomTabsIntent.COLOR_SCHEME_DARK)
      // Add other AuthTabsIntent configurations as needed
  }
  ```

* Custom tabs

  The **OIDC** module falls back to using custom tabs if auth tabs are not supported on the device.

  To customize the auth tab, add your preferred configuration to `BrowserLauncher.customTabsCustomizer` before you call `authorize()`, as follows:

  Customizing custom tabs on Android

  ```kotlin
  BrowserLauncher.customTabsCustomizer = {
      setShowTitle(false)
      setColorScheme(CustomTabsIntent.COLOR_SCHEME_SYSTEM) // Use the system default color scheme
      setToolbarColor(
          ContextCompat.getColor(
              context,
              R.color.colorPrimary
          )
      ) // Set a specific toolbar color
      setUrlBarHidingEnabled(true)
      // Add other CustomTabsIntent configurations as needed
  }
  ```

  Learn more in [Customizing the UI](https://developer.chrome.com/docs/android/custom-tabs/guide-ui-customization) in the *Chrome for Developers* documentation.