---
title: Archive
description: This archive contains the release notes for Web Agent versions that have reached End of Maintenance (EOM).
component: web-agents
version: release-notes
page_id: web-agents::archive
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/archive.html
---

# Archive

This archive contains the release notes for Web Agent versions that have reached End of Maintenance (EOM).

You can find information about release and lifecycle dates in the [Ping Identity End of Life (EOL) Software Tracker](https://support.pingidentity.com/s/article/Ping-Identity-EOL-Tracker#pamagents).

---

---
title: Changes
description: The changes that impact existing functionality in versions of Web Agent that have reached End of Maintenance (EOM).
component: web-agents
version: release-notes
page_id: web-agents::archive-changes
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/archive-changes.html
---

# Changes

The changes that impact existing functionality in versions of Web Agent that have reached End of Maintenance (EOM).

* [Changes in Web Agent 2023.x](changes-2023.html)

* [Changes in Web Agent 5.10.x](changes-510.html)

---

---
title: Changes in Web Agent 2023.x
description: There are no incompatible changes in the Web Agent 2023.11 release, or the Web Agent 2023.11.1 or 2023.11.2 maintenance releases.
component: web-agents
version: release-notes
page_id: web-agents::changes-2023
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/changes-2023.html
section_ids:
  web_agent_2023_11_x: Web Agent 2023.11.x
  web_agent_2023_11_3: Web Agent 2023.11.3
  iaic-am-compatibility-2023: Advanced Identity Cloud and AM compatibility
  web_agent_2023_9: Web Agent 2023.9
  changed-in-2023.6: Web Agent 2023.6
  management_of_agent_credentials: Management of agent credentials
  changed-in-2023.3: Web Agent 2023.3
  nginx_binaries_renamed: NGINX binaries renamed
  openssl_support: OpenSSL support
---

# Changes in Web Agent 2023.x

## Web Agent 2023.11.x

There are no incompatible changes in the Web Agent 2023.11 release, or the Web Agent 2023.11.1 or 2023.11.2 maintenance releases.

### Web Agent 2023.11.3

#### Advanced Identity Cloud and AM compatibility

This version of Web Agent includes changes required for compatibility with future releases of Advanced Identity Cloud and AM.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To maintain compatibility with upcoming Advanced Identity Cloud and AM releases, you must upgrade to one of the following Web Agent versions:- 2025.9

- 2024.11.2

- 2023.11.3 |

## Web Agent 2023.9

There are no incompatible changes in this release.

## Web Agent 2023.6

### Management of agent credentials

An encryption key in `agent.conf` is used to decrypt credentials for the following properties:

* `Agent Profile Password`

* `Private Key Password`

* `Proxy Server Password`

When decryption failed in previous releases, sometimes the agent attempted to use the encrypted form of the password. From this release, the agent does not attempt to use the encrypted form of the password.

## Web Agent 2023.3

### NGINX binaries renamed

NGINX binaries have been renamed as follows:

* Old name format: `web-agent-version-NGINX_rn_Centosn_64bit.zip`

* New name format: `web-agent-version-NGINX_rn_Rheln_64bit.zip`

### OpenSSL support

The following versions of OpenSSL are no longer supported:

| Operating systems                                                    | OpenSSL versions                                  |
| -------------------------------------------------------------------- | ------------------------------------------------- |
| * CentOS

* Red Hat Enterprise Linux

* Oracle Linux

* Ubuntu Linux | - OpenSSL 1.0.x

- OpenSSL 1.1.0                  |
| * Microsoft Windows Server                                           | - OpenSSL 1.0.x

- OpenSSL 1.1.0                  |
| * IBM AIX                                                            | - OpenSSL 0.9.8

- OpenSSL 1.0.x

- OpenSSL 1.1.0 |

---

---
title: Changes in Web Agent 2024.x
description: There are no incompatible changes in the Web Agent 2024.11 release or the Web Agent 2024.11.1 maintenance release.
component: web-agents
version: release-notes
page_id: web-agents::changes-2024
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/changes-2024.html
section_ids:
  web_agent_2024_11_x: Web Agent 2024.11.x
  web_agent_2024_11_2: Web Agent 2024.11.2
  iaic-am-compatibility-2024: Advanced Identity Cloud and AM compatibility
  web_agent_2024_9: Web Agent 2024.9
  web_agent_2024_6: Web Agent 2024.6
  web_agent_2024_3: Web Agent 2024.3
  support_for_sslv3: Support for SSLv3
  nginx_binaries_renamed: NGINX binaries renamed
  aes_256_gcm_encryption: AES-256-GCM encryption
---

# Changes in Web Agent 2024.x

## Web Agent 2024.11.x

There are no incompatible changes in the Web Agent 2024.11 release or the Web Agent 2024.11.1 maintenance release.

### Web Agent 2024.11.2

#### Advanced Identity Cloud and AM compatibility

This version of Web Agent includes changes required for compatibility with future releases of Advanced Identity Cloud and AM.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To maintain compatibility with upcoming Advanced Identity Cloud and AM releases, you must upgrade to one of the following Web Agent versions:- 2025.9

- 2024.11.2

- 2023.11.3 |

## Web Agent 2024.9

There are no incompatible changes in this release.

## Web Agent 2024.6

There are no incompatible changes in this release.

## Web Agent 2024.3

### Support for SSLv3

Support for SSLv3 was removed for OpenSSL.

### NGINX binaries renamed

The operating system name in the downloadable NGINX binaries has been replaced with `Linux`. A single build is now suitable for all NGINX versions and operating systems.

* Example formats for previous release:

  `web-agent-2023.11-NGINX_r30_Rhel7_64bit.zip`\
  `web-agent-2023.11-NGINX_r30_Rhel8_64bit.zip`\
  `web-agent-2023.11-NGINX_r30_Rhel9_64bit.zip`\
  `web-agent-2023.11-NGINX_r30_Ubuntu20_64bit.zip`\
  `web-agent-2023.11-NGINX_r30_Ubuntu22_64bit.zip`

* Example format for this release:

  `web-agent-2024.3-NGINX_r30_Linux_64bit.zip`

### AES-256-GCM encryption

Because of the changes in [Hardened security of agent secrets](whats-new.html#hardened-security-20243), drop-in software update to this release isn't possible. Upgrade to this release from an earlier release is a major upgrade. Learn more in *Upgrade*.

---

---
title: Changes in Web Agent 2025.x
description: There are no incompatible changes in this release.
component: web-agents
version: release-notes
page_id: web-agents::changes-2025
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/changes-2025.html
section_ids:
  web_agent_2025_11: Web Agent 2025.11
  web_agent_2025_9: Web Agent 2025.9
  iaic-am-compatibility: Advanced Identity Cloud and AM compatibility
  web_agent_2025_6: Web Agent 2025.6
  public-client-cert-file-change: Public client certificate file name property
  support_for_sslv3: Support for SSLv3
  des_password_replay: DES Password Replay
  web_agent_2025_3_x: Web Agent 2025.3.x
  web_agent_2025_3: Web Agent 2025.3
  content_security_policy_header_frame_ancestors: Content Security Policy header - frame-ancestors
  agent_authentication_to_advanced_identity_cloud_and_am: Agent authentication to Advanced Identity Cloud and AM
  am_6_5: AM 6.5
  glibc_support: Glibc support
---

# Changes in Web Agent 2025.x

## Web Agent 2025.11

There are no incompatible changes in this release.

## Web Agent 2025.9

### Advanced Identity Cloud and AM compatibility

This version of Web Agent includes changes required for compatibility with future releases of Advanced Identity Cloud and AM.

|   |                                                                                                                                                                                 |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | To maintain compatibility with upcoming Advanced Identity Cloud and AM releases, you must upgrade to one of the following Web Agent versions:- 2025.9

- 2024.11.2

- 2023.11.3 |

## Web Agent 2025.6

### Public client certificate file name property

We've made changes to the use of the [Public Client Certificate File Name](https://docs.pingidentity.com/web-agents/2025.11/properties-reference/com.forgerock.agents.config.cert.file.html) property for agents using Schannel.

This property should now be used only for the name of the file that contains the client certificate chain.

Use the new [Public Client Certificate Friendly Name](https://docs.pingidentity.com/web-agents/2025.11/properties-reference/com.forgerock.agents.config.win.clientcert.friendly.name.html) property to set the friendly name used to look up the client certificate in the Windows certificate store.

### Support for SSLv3

Support for SSLv3 was removed for Windows Secure Channel API (Schannel).

### DES Password Replay

Support for setting up password replay for IIS agents using DES was removed because it's not FIPS 140-3 compliant.

Use the JWT password replay mechanism instead as documented in [Configure basic authentication and password replay support](https://docs.pingidentity.com/web-agents/2025.11/installation-guide/install-iis.html#iis-enable-basic-auth).

## Web Agent 2025.3.x

There are no incompatible changes in the Web Agent 2025.3.1 maintenance release.

### Web Agent 2025.3

#### Content Security Policy header - `frame-ancestors`

By default, the Content Security Policy (CSP) `frame-ancestors` directive is set to `self`, which only allows the site hosting the agent to embed pages in iframes. If you use iframes with another source, you'll need to set the new properties appropriately.

Learn more in [Content Security Policy - `frame-ancestors`](whats-new.html#csp-frame-ancestors).

#### Agent authentication to Advanced Identity Cloud and AM

The default fallback mode setting (`0`) for [AM\_AGENT\_AUTH\_MODE](https://docs.pingidentity.com/web-agents/2025.11/installation-guide/installer-env-vars.html#am-agent-auth-mode) and [Agent Authentication Mode](https://docs.pingidentity.com/web-agents/2025.11/properties-reference/com.forgerock.agents.config.agent.auth.mode.html) has been removed. The default setting is now `1` meaning the agent always authenticates using the `Agent` journey.

If the `Agent` journey doesn't exist, you should create it. Learn more in [Authenticate agents to the identity provider](https://docs.pingidentity.com/web-agents/2025.11/installation-guide/pre-installation.html#authenticate_agents_to_the_identity_provider).

#### AM 6.5

AM 6.5 has reached End of Life (EOL) and is no longer supported.

#### Glibc support

Glibc 2.17 is no longer supported. Glibc 2.28 is the minimum version supported on Linux.

---

---
title: Changes in Web Agent 2026.x
description: The Web Agent downloads for Apache, IBM HTTP and NGINX Plus now include the architecture in the file name.
component: web-agents
version: release-notes
page_id: web-agents::changes-2026
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/changes-2026.html
section_ids:
  web_agent_2026_6: Web Agent 2026.6
  downloads: Web Agent downloads
  ibm_aix: IBM AIX
---

# Changes in Web Agent 2026.x

## Web Agent 2026.6

### Web Agent downloads

The Web Agent downloads for Apache, IBM HTTP and NGINX Plus now include the architecture in the file name.

The following table shows the new naming conventions:

| Server     | Platform | Old name                   | New AMD64 name              | ARM64 name               |
| ---------- | -------- | -------------------------- | --------------------------- | ------------------------ |
| Apache     | Linux    | `Apache_v24_Linux_64bit`   | `Apache_v24_Linux_x86_64`   | `Apache_v24_Linux_arm64` |
|            | Windows  | `Apache_v24_WINNT_64bit`   | `Apache_v24_WINNT_x86_64`   | N/A                      |
| IBM HTTP   | Linux    | `IBMHTTP_v855_Linux_64bit` | `IBMHTTP_v855_Linux_x86_64` | N/A                      |
|            |          | `IBMHTTP_v9_Linux_64bit`   | `IBMHTTP_v9_Linux_x86_64`   | N/A                      |
| NGINX Plus | Linux    | `NGINX_r35_Linux_64bit`    | `NGINX_r35_Linux_x86_64`    | `NGINX_r35_Linux_arm64`  |
|            |          | N/A                        | `NGINX_r36_Linux_x86_64`    | `NGINX_r36_Linux_arm64`  |
|            |          | N/A                        | `NGINX_r37_Linux_x86_64`    | `NGINX_r37_Linux_arm64`  |

### IBM AIX

Support for the IBM AIX operating system has been removed in this release.

---

---
title: Changes in Web Agent 5.10.x
description: IIS agents use Windows libraries and ECMAScript-compatible regular expressions. Adapt the regular expression settings for IIS agents to account for this change.
component: web-agents
version: release-notes
page_id: web-agents::changes-510
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/changes-510.html
section_ids:
  changed-in-510: Web Agent 5.10
  regular_expression_pattern_matching_is_platform_dependent: Regular expression pattern matching is platform-dependent
  fragment_redirect: Fragment redirect
---

# Changes in Web Agent 5.10.x

## Web Agent 5.10

### Regular expression pattern matching is platform-dependent

IIS agents use Windows libraries and [ECMAScript-compatible](https://en.cppreference.com/w/cpp/regex/ecmascript) regular expressions. Adapt the regular expression settings for IIS agents to account for this change.

### Fragment redirect

From Web Agent 5.8.1, when `Enable Fragment Redirect` is `true`, the agent redirects the user back to the original resource using an absolute URL. In previous Web Agent 5 versions, the agent redirects the user using a relative URI.

Proxy rules that rely on fragment redirect to a relative URI, now result in a redirect to a full URL. For example a redirect to `/a/b#c` results in the final URL `prot://host:port/a/b#c`.

Ordered rules that rely on matching a plain URL followed by fully qualified alternatives can result in the fully qualified alternatives matching first.

---

---
title: Deprecated
description: Deprecated is defined in Release levels and interface stability:
component: web-agents
version: release-notes
page_id: web-agents::archive-deprecated
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/archive-deprecated.html
---

# Deprecated

Deprecated is defined in [Release levels and interface stability](stability.html):

| Deprecated in | Description                           | Replaced by                                          | Removed in      |
| ------------- | ------------------------------------- | ---------------------------------------------------- | --------------- |
| 2023.11       | -                                     | -                                                    | -               |
| 2023.9        | `Agent Logout URL Regular Expression` | `Logout URL List` `Enable Regex for Logout URL List` | Not yet removed |
| 2023.6        | -                                     | -                                                    | -               |
| 2023.3        | -                                     | -                                                    | -               |
| 5.10          | Monitoring endpoint                   | Prometheus endpoint                                  | Not yet removed |

---

---
title: Deprecated
description: Deprecated is defined in Release levels and interface stability:
component: web-agents
version: release-notes
page_id: web-agents::deprecated
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/deprecated.html
page_aliases: ["deprecated-functionality.adoc"]
---

# Deprecated

Deprecated is defined in [Release levels and interface stability](stability.html):

| Deprecated in | Description                                                                                                                                                                                                                                                                                                                      | Replaced by                                                                                                                                                                              | Removed in      |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| 2026.6        | -                                                                                                                                                                                                                                                                                                                                | -                                                                                                                                                                                        | -               |
| 2025.11       | -                                                                                                                                                                                                                                                                                                                                | -                                                                                                                                                                                        | -               |
| 2025.9        | -                                                                                                                                                                                                                                                                                                                                | -                                                                                                                                                                                        | -               |
| 2025.6        | Use of the [Public Client Certificate File Name](https://docs.pingidentity.com/web-agents/2025.11/properties-reference/com.forgerock.agents.config.cert.file.html) property for the certificate friendly name.                                                                                                                   | [Public Client Certificate Friendly Name](https://docs.pingidentity.com/web-agents/2025.11/properties-reference/com.forgerock.agents.config.win.clientcert.friendly.name.html) property. | -               |
| 2025.3        | -                                                                                                                                                                                                                                                                                                                                | -                                                                                                                                                                                        | -               |
| 2024.11       | Fallback mode setting (`0`) for [AM\_AGENT\_AUTH\_MODE](https://docs.pingidentity.com/web-agents/2024.11/installation-guide/installer-env-vars.html#am-agent-auth-mode) and [Agent Authentication Mode](https://docs.pingidentity.com/web-agents/2024.11/properties-reference/com.forgerock.agents.config.agent.auth.mode.html). | Default will change to always authenticate using the `Agent` journey.                                                                                                                    | 2025.3          |
|               | `user` field in audit logs.                                                                                                                                                                                                                                                                                                      | `userId` field in audit logs.                                                                                                                                                            | Not yet removed |
| 2024.9        | -                                                                                                                                                                                                                                                                                                                                | -                                                                                                                                                                                        | -               |
| 2024.6        | -                                                                                                                                                                                                                                                                                                                                | -                                                                                                                                                                                        | -               |
| 2024.3        | Support for AM 6.5                                                                                                                                                                                                                                                                                                               | Later versions of AM                                                                                                                                                                     | 2025.3          |
|               | From AM 7.5, values set in the AM admin UI for `Replay Password Key` are ignored.                                                                                                                                                                                                                                                | From AM 7.5, the value of the DES key is inherited from the secret mapped to the AM secret label `am.authentication.replaypassword.key`.                                                 | Not yet removed |

---

---
title: Fixes
description: The fixed issues in versions of Web Agent that have reached End of Maintenance (EOM).
component: web-agents
version: release-notes
page_id: web-agents::archive-fixes
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/archive-fixes.html
---

# Fixes

The fixed issues in versions of Web Agent that have reached End of Maintenance (EOM).

* [Fixes in Web Agent 2023.x](fixes-2023.html)

* [Fixes in Web Agent 5.10.x](fixes-510.html)

---

---
title: Fixes
description: The following pages list important fixes in maintained Web Agent versions.
component: web-agents
version: release-notes
page_id: web-agents::fixes
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/fixes.html
---

# Fixes

The following pages list important fixes in maintained Web Agent versions.

|   |                                                                                                                                                                                                                                                                                                                                                     |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Fixes are cumulative by release date. An issue fixed in a maintenance release, such as Web Agent 2024.11.2, isn't included in a major release, such as Web Agent 2025.3, if the major release was issued before the minor release.You can find the fixes for previous versions that have reached End of Maintenance in the [Archive](archive.html). |

* [Fixes in Web Agent 2026.x](fixes-2026.html)

* [Fixes in Web Agent 2025.x](fixes-2025.html)

* [Fixes in Web Agent 2024.x](fixes-2024.html)

---

---
title: Fixes in Web Agent 2023.x
description: This page lists the cumulative fixes in Web Agent 2023.x releases:
component: web-agents
version: release-notes
page_id: web-agents::fixes-2023
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/fixes-2023.html
section_ids:
  web_agent_2023_11_x: Web Agent 2023.11.x
  web_agent_2023_11_3: Web Agent 2023.11.3
  web_agent_2023_11_2: Web Agent 2023.11.2
  web_agent_2023_11_1: Web Agent 2023.11.1
  web_agent_2023_11: Web Agent 2023.11
  web_agent_2023_9: Web Agent 2023.9
  fix-in-2023.6: Web Agent 2023.6
  fix-in-2023.3: Web Agent 2023.3
---

# Fixes in Web Agent 2023.x

This page lists the cumulative fixes in Web Agent 2023.x releases:

## Web Agent 2023.11.x

### Web Agent 2023.11.3

|               |                                                            |
| ------------- | ---------------------------------------------------------- |
| AMAGENTS-7165 | WPA: agent configuration fetch isn't properly synchronized |
| AMAGENTS-7246 | PDP directory scan isn't working on the AIX platform       |

### Web Agent 2023.11.2

|               |                                                              |
| ------------- | ------------------------------------------------------------ |
| AMAGENTS-6527 | WPA SSL\_shutdown shutdown while in init errors in agent log |
| AMAGENTS-6215 | "Not Enforced Client IP List" abnormal                       |

### Web Agent 2023.11.1

|               |                                                                                     |
| ------------- | ----------------------------------------------------------------------------------- |
| AMAGENTS-6628 | Fragment replay is broken with custom login mode 2                                  |
| AMAGENTS-6494 | Agents local policy eval fails. Agent name and policy application name are switched |

### Web Agent 2023.11

|               |                                                                      |
| ------------- | -------------------------------------------------------------------- |
| AMAGENTS-6175 | Memory leak in credentials\_secure\_free                             |
| AMAGENTS-6133 | Improper use of Bcrypt hash handle in JWT password replay module in  |
| AMAGENTS-6132 | JWT password replay module in IIS should use json parser             |
| AMAGENTS-6073 | Idle timeout should not update on NEU with SSO Only, neu fetch and   |
| AMAGENTS-6057 | Incorrect padding mode used in `jwtpasswdreplay.h`                   |
| AMAGENTS-5594 | Web agent will return 403 errors if OpenSSL libraries aren't loaded. |

## Web Agent 2023.9

|               |                                                                                     |
| ------------- | ----------------------------------------------------------------------------------- |
| AMAGENTS-5995 | Don't extend user session for not enforced url with fetch attributes enabled        |
| AMAGENTS-5833 | WPA 403 error on /agent/cdsso-oauth2 with invalid jwt.aud.whitelist parameter value |
| AMAGENTS-5495 | Web agent validator reports access to OpenSSL v.1.1.x instead of v3.x               |

## Web Agent 2023.6

|               |                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------- |
| AMAGENTS-5678 | Custom Login mode 1 doesn't correctly process composite advice.                                   |
| AMAGENTS-5462 | WPA crash when config.redirect.param is not set                                                   |
| AMAGENTS-5444 | WPA for IIS fails with 0x80090305 error                                                           |
| AMAGENTS-5147 | Web agent incorrectly escapes UTF-8 when creating JSON for audit                                  |
| AMAGENTS-5127 | Internal Server Error (500) when POST is performed without POST data preservation                 |
| AMAGENTS-4478 | Write the Identity used in SSO to the audit logs                                                  |
| AMAGENTS-3683 | Misleading message in "unsuccessful" Agent login when it is actually successful                   |
| AMAGENTS-3315 | WPA: Runtime properties are ignored if they appear before c.s.i.agents.config.repository.location |

## Web Agent 2023.3

|               |                                             |
| ------------- | ------------------------------------------- |
| AMAGENTS-5341 | Installer crashes when checking permissions |

---

---
title: Fixes in Web Agent 2024.x
description: This page lists the cumulative fixes in Web Agent 2024.x releases:
component: web-agents
version: release-notes
page_id: web-agents::fixes-2024
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/fixes-2024.html
section_ids:
  web_agent_2024_11_x: Web Agent 2024.11.x
  web_agent_2024_11_2: Web Agent 2024.11.2
  web_agent_2024_11_1: Web Agent 2024.11.1
  web_agent_2024_11: Web Agent 2024.11
  web_agent_2024_9: Web Agent 2024.9
  web_agent_2024_6: Web Agent 2024.6
  web_agent_2024_3: Web Agent 2024.3
---

# Fixes in Web Agent 2024.x

This page lists the cumulative fixes in Web Agent 2024.x releases:

## Web Agent 2024.11.x

### Web Agent 2024.11.2

|               |                                                      |
| ------------- | ---------------------------------------------------- |
| AMAGENTS-7168 | IIS/ISAPI Schannel Certificate verification fails    |
| AMAGENTS-7246 | PDP directory scan isn't working on the AIX platform |

### Web Agent 2024.11.1

|               |                                                            |
| ------------- | ---------------------------------------------------------- |
| AMAGENTS-7165 | WPA: agent configuration fetch isn't properly synchronized |
| AMAGENTS-7219 | Local policy evaluation mode not working                   |

### Web Agent 2024.11

|               |                                                                                    |
| ------------- | ---------------------------------------------------------------------------------- |
| AMAGENTS-5958 | Invalid error AMConfigurationException generated in the AM log                     |
| AMAGENTS-6729 | Looping after Authentication in session quota mode with -25 / 403 errors           |
| AMAGENTS-6885 | Closing SSL session logs are at ERROR level and should be at DEBUG                 |
| AMAGENTS-6906 | WPA validator validate\_session\_profile test always uses auth module (regression) |
| AMAGENTS-6916 | userId does not get populated by web agent audit                                   |
| AMAGENTS-6929 | NGINX crash in agent\_config\_cleanup                                              |

## Web Agent 2024.9

|               |                                                              |
| ------------- | ------------------------------------------------------------ |
| AMAGENTS-6628 | Fragment replay is broken with custom login mode 2           |
| AMAGENTS-6527 | WPA SSL\_shutdown shutdown while in init errors in agent log |
| AMAGENTS-6215 | "Not Enforced Client IP List" abnormal                       |

## Web Agent 2024.6

|               |                                                                                     |
| ------------- | ----------------------------------------------------------------------------------- |
| AMAGENTS-6557 | Segmentation fault in agentadmin --V before install complete or in custom directory |
| AMAGENTS-6494 | Agents local policy eval fails. Agent name and policy application name are switched |
| AMAGENTS-6428 | Incorrect message formats in task.c                                                 |
| AMAGENTS-6289 | AM\_SYSTEM\_LOG\_FILES only works for debug.log                                     |
| AMAGENTS-3663 | Nginx Agent print absolute build path into debug logs                               |
| AMAGENTS-3166 | The path attribute in agent's audit log is not the full path                        |

## Web Agent 2024.3

|               |                                                                                                                   |
| ------------- | ----------------------------------------------------------------------------------------------------------------- |
| AMAGENTS-6397 | If the agent instance isn't provided for key rotation, agentadmin doesn't print an error                          |
| AMAGENTS-6302 | NGINX agent PDP fails with HTTP/3 connections                                                                     |
| AMAGENTS-6172 | WPA for IIS does not work when running in 32bit mode on 64bit Windows OS                                          |
| AMAGENTS-6046 | convert\_request\_after\_authn\_post writes to /tmp instead of configured PDP directory                           |
| AMAGENTS-5985 | Interactive installation using existing agent configuration files duplicate properties which are commented out    |
| AMAGENTS-5983 | Interactive installer refer to the legacy agent configuration file - OpenSSOAgentBootstrap.properties             |
| AMAGENTS-4590 | login-fragment-relay page should have charset specified.                                                          |
| AMAGENTS-3992 | com.forgerock.agents.config.hostmap doesn't use the IP address                                                    |
| AMAGENTS-3506 | If there are permissions issues with password file with installation on IIS then the log messages are not helpful |

---

---
title: Fixes in Web Agent 2025.x
description: This page lists the cumulative fixes in Web Agent 2025.x releases:
component: web-agents
version: release-notes
page_id: web-agents::fixes-2025
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/fixes-2025.html
section_ids:
  web_agent_2025_11: Web Agent 2025.11
  web_agent_2025_9: Web Agent 2025.9
  web_agent_2025_6: Web Agent 2025.6
  web_agent_2025_3_x: Web Agent 2025.3.x
  web_agent_2025_3_1: Web Agent 2025.3.1
  web_agent_2025_3: Web Agent 2025.3
---

# Fixes in Web Agent 2025.x

This page lists the cumulative fixes in Web Agent 2025.x releases:

## Web Agent 2025.11

|               |                                                                                             |
| ------------- | ------------------------------------------------------------------------------------------- |
| AMAGENTS-7542 | 2025.9 mod\_headers support causes login self submit form failures                          |
| AMAGENTS-4672 | Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly |

## Web Agent 2025.9

|               |                                                                 |
| ------------- | --------------------------------------------------------------- |
| AMAGENTS-7433 | Apache agent custom responses don't work with mod\_headers      |
| AMAGENTS-7390 | Web Agent needs to handle PingAM in serverinfo/version response |

## Web Agent 2025.6

|               |                                                      |
| ------------- | ---------------------------------------------------- |
| AMAGENTS-7168 | IIS/ISAPI Schannel Certificate verification fails    |
| AMAGENTS-7246 | PDP directory scan isn't working on the AIX platform |

## Web Agent 2025.3.x

### Web Agent 2025.3.1

|               |                                          |
| ------------- | ---------------------------------------- |
| AMAGENTS-7219 | Local policy evaluation mode not working |

### Web Agent 2025.3

|               |                                                                                                       |
| ------------- | ----------------------------------------------------------------------------------------------------- |
| AMAGENTS-3301 | Log OpenSSL errors when unable to load CA certificates                                                |
| AMAGENTS-6279 | X-frame option is not coming in response header for Application url when fragment redirect is enabled |
| AMAGENTS-6749 | Agent local configuration files lost formatting                                                       |
| AMAGENTS-6905 | Apache agent should fail to start if multiple AmAgentID directives are detected                       |
| AMAGENTS-6973 | Agent incorrectly %-encodes URLs to make them safe in responses                                       |
| AMAGENTS-7165 | WPA: agent configuration fetch isn't properly synchronized                                            |

---

---
title: Fixes in Web Agent 2026.x
description: This page lists the cumulative fixes in Web Agent 2026.x releases:
component: web-agents
version: release-notes
page_id: web-agents::fixes-2026
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/fixes-2026.html
section_ids:
  web_agent_2026_6: Web Agent 2026.6
---

# Fixes in Web Agent 2026.x

This page lists the cumulative fixes in Web Agent 2026.x releases:

## Web Agent 2026.6

|               |                                                                             |
| ------------- | --------------------------------------------------------------------------- |
| AMAGENTS-7704 | IIS crash in dev\_await\_mutex\_win when dll unloaded due to shutdown       |
| AMAGENTS-7695 | Web Agent crash when policy response attributes contains null array element |
| AMAGENTS-7680 | IIS Web Agent crash in am\_notification\_loop during shutdown               |
| AMAGENTS-7674 | IIS Web Agent running in 32 bit application pool crash                      |
| AMAGENTS-7658 | Agent Profile ID Allow List search is incorrect                             |

---

---
title: Fixes in Web Agent 5.10.x
description: This page lists the cumulative fixes in Web Agent 5.10.x releases:
component: web-agents
version: release-notes
page_id: web-agents::fixes-510
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/fixes-510.html
section_ids:
  web_agent_5_10_4: Web Agent 5.10.4
  web_agent_5_10_3: Web Agent 5.10.3
  web_agent_5_10_2: Web Agent 5.10.2
  web_agent_5_10_1: Web Agent 5.10.1
  web_agent_5_10: Web Agent 5.10
---

# Fixes in Web Agent 5.10.x

This page lists the cumulative fixes in Web Agent 5.10.x releases:

## Web Agent 5.10.4

No issues were fixed in this release.

## Web Agent 5.10.3

|               |                                                                              |
| ------------- | ---------------------------------------------------------------------------- |
| AMAGENTS-5995 | Don't extend user session for not enforced url with fetch attributes enabled |

## Web Agent 5.10.2

No issues were fixed in this release.

## Web Agent 5.10.1

|               |                                                                                         |
| ------------- | --------------------------------------------------------------------------------------- |
| AMAGENTS-5341 | crashes in installer when checking permissions                                          |
| AMAGENTS-5219 | Nginx agent can crash when configured with not-enforced-url regex option                |
| AMAGENTS-5116 | Interactive installer loops infinitely when an invalid host is supplied for the am url. |

## Web Agent 5.10

|               |                                                                                  |
| ------------- | -------------------------------------------------------------------------------- |
| AMAGENTS-5068 | performance issue in AMAGENTS-4716 fix                                           |
| AMAGENTS-4897 | config.fallback.mode doesn't work for not-enforced url configuration             |
| AMAGENTS-4795 | POST Data Sticky Load Balancing Cookie Name configuration option isn't working   |
| AMAGENTS-4788 | WPA doesn't delete session tracking cookie when running in accept.sso.token mode |
| AMAGENTS-4737 | WPA does not support TLS handshake Server Name Indication extension              |
| AMAGENTS-4716 | Agent does not handle SSO tracking cookie enclosed in double quotes              |
| AMAGENTS-4687 | Web Agent 5.9.0 crash if configuration fetch fails.                              |
| AMAGENTS-4545 | nginx agent can crash if graceful restart (reload) is used with load testing.    |
| AMAGENTS-4539 | IIS Web Agent doesn't log reason why PDP file deletion fails.                    |

---

---
title: Getting support
description: Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. Find a general overview of these services at https://www.pingidentity.com.
component: web-agents
version: release-notes
page_id: web-agents::support
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/support.html
---

# Getting support

Ping Identity provides support services, professional services, training, and partner services to assist you in setting up and maintaining your deployments. Find a general overview of these services at <https://www.pingidentity.com>.

Ping Identity has staff members around the globe who support our international customers and partners. For details on Ping Identity's support offering, visit <https://www.pingidentity.com/support>.

Ping Identity publishes comprehensive documentation online:

* The Ping Identity [Knowledge Base](https://support.pingidentity.com/s/knowledge-base) offers a large and increasing number of up-to-date, practical articles that help you deploy and manage Ping Advanced Identity Software software.

  While many articles are visible to everyone, Ping Identity customers have access to much more, including advanced information for customers using Ping Advanced Identity Software software in a mission-critical capacity.

* Ping Identity product documentation, such as this document, aims to be technically accurate and complete with respect to the software documented. It is visible to everyone and covers all product features and examples of how to use them.

---

---
title: Incompatible changes
description: Incompatible changes impact existing functionality and may affect your migration from a previous release. Before you upgrade, review these lists and make the appropriate changes to your scripts and plugins.
component: web-agents
version: release-notes
page_id: web-agents::changes
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/changes.html
---

# Incompatible changes

Incompatible changes impact existing functionality and may affect your migration from a previous release. Before you upgrade, review these lists and make the appropriate changes to your scripts and plugins.

|   |                                                                                                                       |
| - | --------------------------------------------------------------------------------------------------------------------- |
|   | You can find information about previous versions that have reached End of Maintenance in the [Archive](archive.html). |

* [Changes in Web Agent 2026.x](changes-2026.html)

* [Changes in Web Agent 2025.x](changes-2025.html)

* [Changes in Web Agent 2024.x](changes-2024.html)

---

---
title: Known issues
description: "AMAGENTS-6628: Fragment replay is broken with custom login mode 2"
component: web-agents
version: release-notes
page_id: web-agents::archive-known-issues
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/archive-known-issues.html
section_ids:
  web_agent_2023_11: Web Agent 2023.11
  web_agent_2023_9: Web Agent 2023.9
  web_agent_2023_6: Web Agent 2023.6
  web_agent_2023_3: Web Agent 2023.3
  web_agent_5_10: Web Agent 5.10
---

# Known issues

## Web Agent 2023.11

| Issue                                                                                                                                             | Comment                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| AMAGENTS-6628: Fragment replay is broken with custom login mode 2                                                                                 | Fixed in 2024.9, 2023.11.1 |
| AMAGENTS-6527: WPA SSL\_shutdown shutdown while in init errors in agent log                                                                       | Fixed in 2024.9, 2023.11.2 |
| AMAGENTS-6494: Agents local policy eval fails. Agent name and policy application name are switched                                                | Fixed in 2024.6, 2023.11.1 |
| AMAGENTS-6172: WPA for IIS doesn't work when running in 32bit mode on 64bit Windows OS                                                            | Fixed in 2024.3            |
| AMAGENTS-6046: convert\_request\_after\_authn\_post writes to /tmp instead of configured PDP directory                                            | Fixed in 2024.3            |
| AMAGENTS-5985: Interactive installation using existing agent configuration files duplicate properties which are commented out                     | Fixed in 2024.3            |
| AMAGENTS-5983 Interactive installer refer to the legacy agent configuration file - OpenSSOAgentBootstrap.properties                               | Fixed in 2024.3            |
| AMAGENTS-5958: Invalid error AMConfigurationException generated in the AM log                                                                     | Fixed in 2024.11           |
| AMAGENTS-5777: IIS web agent zip file includes 32bit DLL                                                                                          | Won't fix                  |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice.                                                                    | Unresolved                 |
| AMAGENTS-5032: WPA: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names. | Unresolved                 |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                        | Fixed in 2025.11           |
| AMAGENTS-4590: login-fragment-relay page should have charset specified.                                                                           | Fixed in 2024.3            |
| AMAGENTS-3992: WPA: com.forgerock.agents.config.hostmap does not seem to use the IP address                                                       | Fixed in 2024.3            |
| AMAGENTS-3663: Nginx Agent print absolute build path into debug logs                                                                              | Fixed in 2024.6            |
| AMAGENTS-3506: If there are permissions issues with password file with installation on IIS then the log messages are not helpful                  | Fixed in 2024.3            |
| AMAGENTS-2813: Agents Logout perform logout multiple times                                                                                        | Unresolved                 |
| AMAGENTS-2755: Currently when setting up the agent it is necessary to have a client certificate file when using Schannel                          | Unresolved                 |

## Web Agent 2023.9

| Issue                                                                                                                                             | Comment                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| AMAGENTS-6494: Agents local policy eval fails. Agent name and policy application name are switched                                                | Fixed in 2024.6, 2023.11.1 |
| AMAGENTS-6175: Memory leak in credentials\_secure\_free                                                                                           | Fixed in 2023.11           |
| AMAGENTS-6073: Idle timeout should not update on NEU with SSO Only, neu fetch and                                                                 | Fixed in 2023.11           |
| AMAGENTS-6046: convert\_request\_after\_authn\_post writes to /tmp instead of configured PDP directory                                            | Fixed in 2024.3            |
| AMAGENTS-5985: Interactive installation using existing agent configuration files duplicate properties which are commented out                     | Fixed in 2024.3            |
| AMAGENTS-5958: Invalid error AMConfigurationException generated in the AM log                                                                     | Fixed in 2024.11           |
| AMAGENTS-5777: IIS web agent zip file includes 32bit DLL                                                                                          | Unresolved                 |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice.                                                                    | Unresolved                 |
| AMAGENTS-5594: Web agent will return 403 errors if OpenSSL libraries aren't loaded.                                                               | Fixed in 2023.11           |
| AMAGENTS-5032: WPA: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names. | Unresolved                 |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                        | Fixed in 2025.11           |
| AMAGENTS-4590: login-fragment-relay page should have charset specified.                                                                           | Fixed in 2024.3            |
| AMAGENTS-3992: WPA: com.forgerock.agents.config.hostmap does not seem to use the IP address                                                       | Fixed in 2024.3            |
| AMAGENTS-3663: Nginx Agent print absolute build path into debug logs                                                                              | Fixed in 2024.6            |
| AMAGENTS-3506: If there are permissions issues with password file with installation on IIS then the log messages are not helpful                  | Fixed in 2024.3            |
| AMAGENTS-2813: Agents Logout perform logout multiple times                                                                                        | Unresolved                 |
| AMAGENTS-2755: Currently when setting up the agent it is necessary to have a client certificate file when using Schannel                          | Unresolved                 |

## Web Agent 2023.6

| Issue                                                                                                                                             | Comment                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| AMAGENTS-6494: Agents local policy eval fails. Agent name and policy application name are switched                                                | Fixed in 2024.6, 2023.11.1 |
| AMAGENTS-6175: Memory leak in credentials\_secure\_free                                                                                           | Fixed in 2023.11           |
| AMAGENTS-6046: convert\_request\_after\_authn\_post writes to /tmp instead of configured PDP directory                                            | Fixed in 2024.3            |
| AMAGENTS-5995: Don't extend user session for not enforced url with fetch attributes enabled                                                       | Fixed in 2023.9            |
| AMAGENTS-5985: Interactive installation using existing agent configuration files duplicate properties which are commented out                     | Fixed in 2024.3            |
| AMAGENTS-5833: WPA 403 error on /agent/cdsso-oauth2 with invalid jwt.aud.whitelist parameter value                                                | Fixed in 2023.9            |
| AMAGENTS-5777: IIS web agent zip file includes 32bit DLL                                                                                          | Unresolved                 |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice.                                                                    | Unresolved                 |
| AMAGENTS-5594: Web agent will return 403 errors if OpenSSL libraries aren't loaded.                                                               | Fixed in 2023.11           |
| AMAGENTS-5495: Web agent validator reports access to OpenSSL v.1.1.x instead of v3.x                                                              | Fixed in 2023.9            |
| AMAGENTS-5032: WPA: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names. | Unresolved                 |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                        | Fixed in 2025.11           |
| AMAGENTS-4590: login-fragment-relay page should have charset specified.                                                                           | Fixed in 2024.3            |
| AMAGENTS-3992: WPA: com.forgerock.agents.config.hostmap does not seem to use the IP address                                                       | Fixed in 2024.3            |
| AMAGENTS-3663: Nginx Agent print absolute build path into debug logs                                                                              | Fixed in 2024.6            |
| AMAGENTS-3506: If there are permissions issues with password file with installation on IIS then the log messages are not helpful                  | Fixed in 2024.3            |
| AMAGENTS-2813: Agents Logout perform logout multiple times                                                                                        | Unresolved                 |
| AMAGENTS-2755: Currently when setting up the agent it is necessary to have a client certificate file when using Schannel                          | Unresolved                 |
| AMAGENTS-2724: WPA: Custom login does not work, if agent is installed in different location than root                                             | Duplicates AMAGENTS-5981   |

## Web Agent 2023.3

| Issue                                                                                                                                             | Comment          |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-6175: Memory leak in credentials\_secure\_free                                                                                           | Fixed in 2023.11 |
| AMAGENTS-6046: convert\_request\_after\_authn\_post writes to /tmp instead of configured PDP directory                                            | Fixed in 2024.3  |
| AMAGENTS-5995: Don't extend user session for not enforced url with fetch attributes enabled                                                       | Fixed in 2023.9  |
| AMAGENTS-5985: Interactive installation using existing agent configuration files duplicate properties which are commented out                     | Fixed in 2024.3  |
| AMAGENTS-5833: WPA 403 error on /agent/cdsso-oauth2 with invalid jwt.aud.whitelist parameter value                                                | Fixed in 2023.9  |
| AMAGENTS-5777: IIS web agent zip file includes 32bit DLL                                                                                          | Unresolved       |
| AMAGENTS-5495: Web agent validator reports access to OpenSSL v.1.1.x instead of v3.x                                                              | Fixed in 2023.9  |
| AMAGENTS-5594: Web agent will return 403 errors if OpenSSL libraries aren't loaded.                                                               | Fixed in 2023.11 |
| AMAGENTS-5032: WPA: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names. | Unresolved       |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                        | Fixed in 2025.11 |

## Web Agent 5.10

| Issue                                                                                                                                             | Comment                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| AMAGENTS-5995: Don't extend user session for not enforced url with fetch attributes enabled                                                       | Fixed in 5.10.3          |
| AMAGENTS-5833: WPA 403 error on /agent/cdsso-oauth2 with invalid jwt.aud.whitelist parameter value                                                | Fixed in 2023.9          |
| AMAGENTS-5777: IIS web agent zip file includes 32bit DLL                                                                                          | Unresolved               |
| AMAGENTS-5495: Web agent validator reports access to OpenSSL v.1.1.x instead of v3.x                                                              | Fixed in 2023.9          |
| AMAGENTS-5594: Web agent will return 403 errors if OpenSSL libraries aren't loaded.                                                               | Fixed in 2023.11         |
| AMAGENTS-5032: WPA: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names. | Unresolved               |
| AMAGENTS-4984: Setting samesite cookie to lax will cause the agent auth flow to fail if we are using different sites                              | Duplicates AMAGENTS-5189 |
| AMAGENTS-4672: Web Agent does not handle specific case for Not-Enforced URL and one level wildcard properly                                       | Unresolved               |

---

---
title: Known issues
description: "AMAGENTS-7624: The agentadmin installer on Windows writes configuration file comments with double line endings"
component: web-agents
version: release-notes
page_id: web-agents::known-issues
canonical_url: https://docs.pingidentity.com/web-agents/release-notes/known-issues.html
section_ids:
  web_agent_2026_6: Web Agent 2026.6
  web_agent_2025_11: Web Agent 2025.11
  web_agent_2025_9: Web Agent 2025.9
  web_agent_2025_6: Web Agent 2025.6
  web_agent_2025_3: Web Agent 2025.3
  web_agent_2024_11: Web Agent 2024.11
  web_agent_2024_9: Web Agent 2024.9
  web_agent_2024_6: Web Agent 2024.6
  web_agent_2024_3: Web Agent 2024.3
---

# Known issues

## Web Agent 2026.6

| Issue                                                                                                                                      | Comment    |
| ------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| AMAGENTS-7624: The agentadmin installer on Windows writes configuration file comments with double line endings                             | Unresolved |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                              | Unresolved |
| AMAGENTS-5032: Native agents for windows don't correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved |

## Web Agent 2025.11

| Issue                                                                                                                                       | Comment    |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                               | Unresolved |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved |

## Web Agent 2025.9

| Issue                                                                                                                                       | Comment          |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                               | Unresolved       |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved       |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                  | Fixed in 2025.11 |

## Web Agent 2025.6

| Issue                                                                                                                                       | Comment          |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                               | Unresolved       |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved       |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                  | Fixed in 2025.11 |

## Web Agent 2025.3

| Issue                                                                                                                                       | Comment                      |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| AMAGENTS-7219: Local policy evaluation mode not working                                                                                     | Fixed in 2025.3.1, 2024.11.1 |
| AMAGENTS-6363: Shared user profile attributes                                                                                               | Won't fix                    |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                               | Unresolved                   |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved                   |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                  | Fixed in 2025.11             |

## Web Agent 2024.11

| Issue                                                                                                                                       | Comment                      |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| AMAGENTS-7219: Local policy evaluation mode not working                                                                                     | Fixed in 2025.3.1, 2024.11.1 |
| AMAGENTS-6905: Apache agent should fail to start if multiple AmAgentID directives are detected                                              | Fixed in 2025.3              |
| AMAGENTS-6904: validate\_credential\_files issue with config filename that have no path component                                           | Won't fix                    |
| AMAGENTS-6749: Agent local configuration files lost formatting                                                                              | Fixed in 2025.3              |
| AMAGENTS-6363: Shared user profile attributes                                                                                               | Unresolved                   |
| AMAGENTS-6306: Infinite apache error log caused by pipe error                                                                               | Won't fix                    |
| AMAGENTS-6279: X-frame option is not coming in response header for Application url when fragment redirect is enabled                        | Fixed in 2025.3              |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                               | Unresolved                   |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved                   |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                  | Fixed in 2025.11             |

## Web Agent 2024.9

| Issue                                                                                                                                       | Comment          |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| AMAGENTS-6749: Agent local configuration files lost formatting                                                                              | Fixed in 2025.3  |
| AMAGENTS-6729: Looping after Authentication in session quota mode with -25 / 403 errors                                                     | Fixed in 2024.11 |
| AMAGENTS-6363: Shared user profile attributes                                                                                               | Unresolved       |
| AMAGENTS-6306: Infinite apache error log caused by pipe error                                                                               | Unresolved       |
| AMAGENTS-6279: X-frame option is not coming in response header for Application url when fragment redirect is enabled                        | Fixed in 2025.3  |
| AMAGENTS-5958: Invalid error AMConfigurationException generated in the AM log                                                               | Fixed in 2024.11 |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                               | Unresolved       |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved       |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                  | Fixed in 2025.11 |

## Web Agent 2024.6

| Issue                                                                                                                                       | Comment                    |
| ------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| AMAGENTS-6628: Fragment replay is broken with custom login mode 2                                                                           | Fixed in 2024.9, 2023.11.1 |
| AMAGENTS-6527: WPA SSL\_shutdown shutdown while in init errors in agent log                                                                 | Fixed in 2024.9, 2023.11.2 |
| AMAGENTS-6363: Shared user profile attributes                                                                                               | Unresolved                 |
| AMAGENTS-6306: Infinite apache error log caused by pipe error                                                                               | Unresolved                 |
| AMAGENTS-6279: X-frame option is not coming in response header for Application url when fragment redirect is enabled                        | Fixed in 2025.3            |
| AMAGENTS-6215: "Not Enforced Client IP List" abnormal                                                                                       | Fixed in 2024.9, 2023.11.2 |
| AMAGENTS-5958: Invalid error AMConfigurationException generated in the AM log                                                               | Fixed in 2024.11           |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice                                                               | Unresolved                 |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names | Unresolved                 |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                  | Fixed in 2025.11           |

## Web Agent 2024.3

| Issue                                                                                                                                        | Comment                    |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| AMAGENTS-6628: Fragment replay is broken with custom login mode 2                                                                            | Fixed in 2024.9, 2023.11.1 |
| AMAGENTS-6527: WPA SSL\_shutdown shutdown while in init errors in agent log                                                                  | Fixed in 2024.9, 2023.11.2 |
| AMAGENTS-6494: Agents local policy eval fails. Agent name and policy application name are switched                                           | Fixed in 2024.6, 2023.11.1 |
| AMAGENTS-6363:websites sharing a cache sometimes don't get the expected headers set because of cache sharing issues in the agent             | Unresolved                 |
| AMAGENTS-6306: infinite apache error log caused by pipe error                                                                                | Unresolved                 |
| AMAGENTS-6289: AM\_SYSTEM\_LOG\_FILES only works for debug.log                                                                               | Fixed in 2024.6            |
| AMAGENTS-5958: Invalid error AMConfigurationException generated in the AM log                                                                | Fixed in 2024.11           |
| AMAGENTS-5718: Custom Login mode 2 doesn't correctly process composite advice.                                                               | Unresolved                 |
| AMAGENTS-5032: Native agents for windows do not correctly use unicode for the file system, resulting in configured files with garbled names. | Unresolved                 |
| AMAGENTS-4672: Web Agent doesn't handle specific case for Not-Enforced URL and one level wildcard properly                                   | Fixed in 2025.11           |
| AMAGENTS-3663: Nginx Agent print absolute build path into debug logs                                                                         | Fixed in 2024.6            |
| AMAGENTS-2813: Agents Logout perform logout multiple times                                                                                   | Not a defect               |
| AMAGENTS-2755: Currently when setting up the agent it's necessary to have a client certificate file when using Schannel                      | Won't fix                  |