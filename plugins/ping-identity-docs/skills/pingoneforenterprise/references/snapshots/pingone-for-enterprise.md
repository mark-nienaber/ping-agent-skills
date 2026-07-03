---
title: AD Connect final setup
description: Complete the setup or manual update of AD Connect, verify the AD Connect installation, and configure additional settings in PingOne for Enterprise.
component: pingoneforenterprise
page_id: pingoneforenterprise:pingone_for_enterprise:p14e_adc_final_setup
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/pingone_for_enterprise/p14e_adc_final_setup.html
revdate: January 9, 2026
section_ids:
  about-this-task: About this task
  steps: Steps
  next-steps: Next steps
---

# AD Connect final setup

Complete the setup or manual update of AD Connect, verify the AD Connect installation, and configure additional settings in PingOne for Enterprise.

## About this task

## Steps

1. On the PingOne for Enterprise admin portal page for AD Connect, click **Verify Installation**.

   |   |                                                                                                                                                                                                       |
   | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   |   | If you're using AD Connect in a clustered, high availability configuration, you will verify the installation in the PingOne for Enterprise admin portal only for the initial AD Connect installation. |

2. **Optional:** Choose whether to enable Integrated Windows Authentication (IWA).

   When enabled, IWA is applied when the user is on your organization's network. When the user comes from outside your network, NTLM is used. A user is prompted for their credentials only once per browser session.

   1. If you enable IWA, the **Intranet IP Ranges** entry box is displayed. Your entries here apply IWA to all users whose IP addresses are specified or contained within a block of IP addresses. The addresses need to be IPv4 addresses in dot-decimal format (123.123.123.123), or an IPv4 address block in CIDR format (123.123.123.0/24).

3. In **AD Connect Configuration**, the following settings are available:

   * **Authentication Account Lookup Method**

     Assigns the Active Directory attribute to use when looking up the account information for the user during delegated authentication. This can be:

     * **Mail**. The email address assigned to the user.

     * **sAMAccountName**. The legacy Windows logon name for the user.

     * **Filter**. An LDAP filter to use when looking up the account information for the user.

       Include `{0}` in your filter where you want the user's input to be substituted. For example, if you want to look up users by `sAMAccountName`, you would enter `sAMAccountName={0}`.

     * **userPrincipalName**. We recommend you use `userPrincipalName` if you select the **Enable Global Catalog** option.

   * **Subject Attribute**

     Choose the value to use for `SAML_SUBJECT`. The possible values are `sAMAccountName` or `userPrincipalName`.

     |   |                                                                                                                                                                                                             |
     | - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
     |   | If your user population comes from multiple domains, choose `userPrincipalName` as the subject attribute to avoid the potential of different users in different domains signing in using the same username. |

   * **Enable Delegated Windows Authentication**

     Select to enable a URL automatically created by PingOne for Enterprise that is unique to your account. We use this URL to verify the credentials used for sign-on requests received when a Salesforce user attempts to sign on using either the Salesforce UI or API.

     To ensure security, PingOne for Enterprise also generates a random key that is associated with this URL. If the existing key is compromised, click **Renew** to generate a new random key for the URL.

   * **Enable Password Change**

     Select to enable users to change their corporate passwords through AD Connect. When enabled, a Change My Password option is displayed on the AD Connect sign on screen. Users selecting this option are prompted for their existing password and the new password to use. Their password is then changed in Active Directory.

   * **Enable Group Hierarchy**

     Select to enable support for group hierarchies in Active Directory. When enabled, Active Directory groups that are nested will inherit the SSO permissions of their parent group or groups. When disabled (the default), an Active Directory group uses only the SSO permissions that are assigned to it, with no inheritance.

   * **Enable Global Catalog**

     Select to use the Active Directory Global Catalog for user lookup. When enabled, we recommend you use `userPrincipalName` as the **Authentication Account Lookup Method**.

4. Assign the Active Directory-to-PingOne for Enterprise attribute mapping.

   This assignment maps Active Directory attributes to the default PingOne for Enterprise attributes. This attribute mapping is not used by applications that you add to PingOne for Enterprise. You will configure those attribute mappings for each application.

   1. For any of the attribute mappings, you can choose to configure an advanced mapping. Learn more in [Creating advanced attribute mappings](p14e_creating_advaced_attribute_mappings.html).

5. Click **Finish**.

   When you return to the **Setup > Identity Repository**, a summary of the settings for your identity bridge is displayed.

## Next steps

If you're using AD Connect in a clustered, high availability configuration, repeat these steps on each AD Connect host.
