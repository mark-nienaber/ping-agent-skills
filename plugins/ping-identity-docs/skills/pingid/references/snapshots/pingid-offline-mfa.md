---
title: PingID Offline MFA
description: PingID runs as a cloud service on the PingOne platform. To allow users to authenticate even if the PingID service is unreachable, PingID includes offline multi-factor authentication (MFA).
component: pingid
page_id: pingid:pingid_offline_mfa:pid_offline_mfa
canonical_url: http://docs.pingidentity.com/pingid/pingid_offline_mfa/pid_offline_mfa.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 10, 2024
section_ids:
  pingid-offline-mfa-when-authenticating-through-pingfederate-single-sign-on-sso: PingID offline MFA when authenticating through PingFederate single sign-on (SSO)
  pingid-offline-mfa-when-accessing-through-radius-password-credential-validator-pcv: PingID offline MFA when accessing through RADIUS password credential validator (PCV)
  pingid-offline-mfa-when-accessing-through-windows-login: PingID offline MFA when accessing through Windows login
  pingid-offline-mfa-when-accessing-through-windows-login-passwordless: PingID offline MFA when accessing through Windows login (passwordless)
  pingid-offline-mfa-when-accessing-through-mac-login: PingID offline MFA when accessing through Mac login
  offline-mfa-when-using-the-pingid-integration-with-ssh: Offline MFA when using the PingID integration with SSH
---

# PingID Offline MFA

PingID runs as a cloud service on the PingOne platform. To allow users to authenticate even if the PingID service is unreachable, PingID includes offline multi-factor authentication (MFA).

Offline MFA must be configured, so make sure to carry out the steps outlined here before you actually encounter such a situation.

You can configure PingID offline MFA for the following use cases:

* Access through PingFederate single sign-on (SSO)

* Access through RADIUS password credential validator (PCV)

* Access through Windows login

* Access through Windows login (passwordless)

* Access through Mac login

* Access through the PingID integration with SSH

Below is an outline of the steps required to configure offline MFA for each of these cases. Links are provided to the detailed information for each case.

|   |                                                                                                                                                                                                                                                                                                                                    |
| - | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * PingID policy rules that have been defined are not enforced when authenticating in offline mode.

* Device requirements are taken into account when authenticating in offline mode.

* Changes to the device list that occur during offline mode are updated in the user directory only when the user next authenticates online. |

## PingID offline MFA when authenticating through PingFederate single sign-on (SSO)

Offline MFA requires the following:

* A user directory to store user device information from PingID. For more information, see [User directory for PingID offline MFA](pid_user_directory_for_offline_mfa.html).

* Unlimited Strength Java Cryptography Extension (JCE), which is required for supporting the 256-bit key size for cryptographic algorithms. Without it, the feature will return an exception related to the missing library, and will not function.

When the PingID service is unreachable, after first-factor authentication, the user receives a QR code on an offline authentication screen.

To enable offline authentication, carry out the optional offline MFA step described in [Installing the PingID Integration Kit for PingFederate](../pingid_integrations/installing_the_pid_i_for_pf.html), and configure offline MFA for the PingID Adapter as described in [Configuring offline MFA (PingID Adapter)](../pingid_integrations/pid_adapter_configuring_offline_mfa.html).

When configuring the PingID Adapter for offline MFA, the key option to configure is **AUTHENTICATION DURING ERRORS**, which can be set to one of:

* Bypass User

* Block User

* Passive Offline Authentication

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In addition to the standard options listed above, if you encounter a situation where PingID is down but the Passive Offline Authentication option is not prompting users to authenticate offline, you can select the **Enforce Offline Authentication** option for a limited time until the issue is resolved. This will force all your users to authenticate offline until you switch back to one of the standard options. |

## PingID offline MFA when accessing through RADIUS password credential validator (PCV)

When the PingID service is unreachable, after first-factor authentication, the user receives a 12-digit security key in the VPN client.

For detailed instructions on configuring offline MFA with PingID RADIUS PCV, see [Configuring offline MFA (RADIUS PCV)](../pingid_integrations/pid_configuring_offline_mfa_radius_pcv.html).

|   |                                                                    |
| - | ------------------------------------------------------------------ |
|   | PingID offline MFA does not support RADIUS VPNs with no challenge. |

When configuring offline MFA for the PingID RADIUS PCV, the key option to configure is **Authentication During Errors**, which can be set to one of:

* Bypass User

* Block User

* Passive Offline Authentication

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In addition to the standard options listed above, if you encounter a situation where PingID is down but the Passive Offline Authentication option is not prompting users to authenticate offline, you can select the **Enforce Offline Authentication** option for a limited time until the issue is resolved. This will force all your users to authenticate offline until you switch back to one of the standard options. |

## PingID offline MFA when accessing through Windows login

When the PingID service is unreachable, after first-factor authentication, the user is prompted to authenticate using a security key or the PingID mobile app in offline MFA mode (manual authentication).

For detailed information about configuring offline MFA for Windows login, see [Installing the PingID integration for Windows login](../pingid_integrations/pid_install_integration_windows_login.html).

The behavior for offline situations is determined by the value provided for the `offlineAuthType` parameter when carrying out command-line installation of the integration with Windows login. You can set `offlineAuthType` to:

* 0 - do not allow MFA for offline authentication

* 1 - allow offline MFA using PingID mobile app only

* 2 - allow offline MFA using a FIDO2 security key only

* 3 - allow offline MFA using either PingID mobile app or a FIDO2 security key

## PingID offline MFA when accessing through Windows login (passwordless)

When the PingID service is unreachable, after authentication is initiated, the user is prompted to authenticate using a security key or the PingID mobile app in offline MFA mode (manual authentication).

For details, see the description of the **Offline Mode** option in [Creating an authentication policy (Windows passwordless)](../pingid_integrations/pid_creating_authentication_policy_windows_passwordless.html).

## PingID offline MFA when accessing through Mac login

When the PingID service is unreachable, after first-factor authentication, the user is prompted to authenticate using a security key or the PingID mobile app in offline MFA mode (manual authentication).

For detailed information about configuring offline MFA for Mac login, see [Installing the PingID integration for Mac login](../pingid_integrations/pid_installing_integration_for_mac_login.html).

The behavior for offline situations is determined by the value provided for the `offlineAuthType` parameter when carrying out command-line installation of the integration with Mac login. You can set `offlineAuthType` to:

* 0 - allow offline MFA with the PingID mobile app

* 1 - if the user does not have a paired PingID mobile app with their account, bypass MFA during login

* 2 - do not allow offline MFA

## Offline MFA when using the PingID integration with SSH

When the PingID service is unreachable, after first-factor authentication, the user receives a 12-digit security key in the terminal window.

For detailed information, see [Enabling offline MFA in SSH integration](../pingid_integrations/pid_enabling_offline_mfa_in_ssh_integration.html).

The behavior for offline situations is determined by the value provided for the `fail_mode setting` in the configuration file, which can set to:

* `restrictive`

* `passive_offline_authentication`

* `permissive`

|   |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| - | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | In addition to the standard options listed above, if you encounter a situation where PingID is down but the `passive_offline_authentication` option is not prompting users to authenticate offline, you can select the `enforce_offline_authentication` option for a limited time until the issue is resolved. This will force all your users to authenticate offline until you switch back to one of the standard options. |

---

---
title: User directory for PingID offline MFA
description: PingID offline multi-factor authentication (MFA) supports storage of user authentication device details according to different user directory deployments.
component: pingid
page_id: pingid:pingid_offline_mfa:pid_user_directory_for_offline_mfa
canonical_url: http://docs.pingidentity.com/pingid/pingid_offline_mfa/pid_user_directory_for_offline_mfa.html
llms_txt: http://docs.pingidentity.com/pingid/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: April 4, 2023
section_ids:
  user-directory: User directory
  priority-of-parameter-settings-during-the-flow-of-pingid-offline-mfa: Priority of parameter settings during the flow of PingID offline MFA
---

# User directory for PingID offline MFA

PingID offline multi-factor authentication (MFA) *(tooltip: \<div class="paragraph">
\<p>An electronic authentication method where a user is granted access only after presenting two or more verification factors for authentication.\</p>
\</div>)* supports storage of user authentication device details according to different user directory deployments.

## User directory

PingID offline MFA can access device information stored in the directory's user object, or in a directory object separate from the user object, either in the same directory as the user object, or in a different directory.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | The PingID offline MFA feature is designed to work with directories from several vendors, including Active Directory, Oracle Directory, and Ping Directory.Directory setup scripts are provided for Active Directory as part of the PingID Integration Kit 2.0 and later. You must configure other directories manually.For more information on directory configuration, see [Installing the PingID Integration Kit for PingFederate](../pingid_integrations/installing_the_pid_i_for_pf.html). |

Scripts provided in the PingID Integration Kit 2.0 or later add the following attributes to the directory:

* `pf-pingid-state`

  The `pf-pingid-state` attribute holds the authentication state of the user during offline MFA.Administrators can use this attribute to bypass or block individual users.It is an optional attribute. When it is used, it must be coupled with the `user` object class on the main user directory. The optional values, `block` or `bypass`, stored in this attribute are managed by the administrator. For more information, see [Configuring offline MFA (PingID Adapter)](../pingid_integrations/pid_adapter_configuring_offline_mfa.html) or [Configuring offline MFA (RADIUS PCV)](../pingid_integrations/pid_configuring_offline_mfa_radius_pcv.html).PingFederate only requires read access to the `pf-pingid-state` attribute.The value of the `pf-pingid-state` attribute is always stored in the user's object. You can assign a different name to the attribute using the setup script, within the limits permitted by the user directory.When PingID is offline, the identity provider checks the configuration.

  * If the user's `pf-pingid-state` configuration is empty, the authentication flow continues.

  * If `pf-pingid-state` is set to `bypass`, the user bypasses MFA.

  * If `pf-pingid-state` is set to `block`, the user is blocked from logging in.

* `pf-pingid-local-fallback`

  The `pf-pingid-local-fallback` attribute holds the user's authentication devices list information.It is a mandatory attribute.The administrator must decide between:

  * Adding the attribute to the `user` objectClass on the main user directory.

  * Adding the attribute to a separate custom `pf-pingid-device` objectClass.

If you add `pf-pingid-local-fallback` to `pf-pingid-device`, you must decide which directory should hold the `pf-pingid-device` objects. These objects can be stored in the same directory as the users in a different location in the directory tree, or in an entirely separate directory. PingFederate configuration will vary according to the design you choose.

Multiple Adapter/PCV Instances: When running a single PingFederate server with multiple PingID tenants, the `pf-pingid-local-fallback` attribute cannot be linked to the user objectClass. It is mandatory to set up a separate custom `pf-pingid-device` objectClass. The location of the `pf-pingid-device` objects must be different for each Adapter/PCV instance.

If multiple Adapter/PCV instances use the same PingID tenant, there is no restriction on the `pf-pingid-local-fallback` attribute location.

For more information, see [Installing the PingID Integration Kit for PingFederate](../pingid_integrations/installing_the_pid_i_for_pf.html).PingFederate will have read and write access to the `pf-pingid-local-fallback` attribute, because values stored in this attribute are managed by PingFederate.

## Priority of parameter settings during the flow of PingID offline MFA

1. If the `Authentication During Errors` parameter is set to `Bypass` or `Block`, the user's `state` attribute is ignored during offline authentication. All users will either bypass PingID offline MFA or be blocked from authenticating, according to the `Authentication During Errors` setting.

2. If the `Authentication During Errors` parameter is set to `Passive` or `Enforce`, PingFederate checks the user's `state` attribute.

   * The user's `state` attribute is empty

     If the user has a paired mobile device, the flow proceeds to offline MFA.If the user does not have a paired mobile device, the flow proceeds according to the setting in the `Users Without a Paired Device` parameter.

     * The user's `state` attribute is set to `Bypass`

       The user will bypass PingID offline MFA.

     * The user's `state` attribute is set to `Block`

       The user is blocked from authenticating.