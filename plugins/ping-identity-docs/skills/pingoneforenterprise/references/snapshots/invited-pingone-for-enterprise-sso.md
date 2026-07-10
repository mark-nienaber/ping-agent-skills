---
title: Getting started with Invited PingOne for Enterprise SSO
description: Follow this workflow to set up Invited PingOne single sign-on (SSO).
component: pingoneforenterprise
page_id: pingoneforenterprise:invited_pingone_for_enterprise_sso:p14e_getting_started_invited_sso
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/invited_pingone_for_enterprise_sso/p14e_getting_started_invited_sso.html
revdate: April 10, 2024
section_ids:
  steps: Steps
  next-steps: Next steps
---

# Getting started with Invited PingOne for Enterprise SSO

Follow this workflow to set up Invited PingOne single sign-on (SSO).

## Steps

1. Familiarize yourself with how PingOne for Enterprise works.

   See [PingOne for Enterprise](../pingone_for_enterprise/p14e_overview.html) and [Federated SSO with PingOne for Enterprise](../pingone_for_enterprise/p14e_federated_sso.html) for information.

2. Connect to an identity repository.

   You can configure an identity bridge to connect to an external identity repository or use the PingOne for Enterprise Directory as your identity repository. See [Connecting to an identity repository](../pingone_for_enterprise/p14e_connecting_idp.html) for information.

3. Assign administrators.

   See [Assign administrative roles](../pingone_for_enterprise/p14e_assign_administrative_roles.html) for information.

4. Add user groups.

   See [Managing users by group](../pingone_for_enterprise/p14e_managing_users_by_group.html) for information.

5. **Optional:** Manage your PingOne for Enterprise Directory users.

   If you're using PingOne for Enterprise Directory as your identity repository, see [Managing PingOne for Enterprise Directory users](../pingone_for_enterprise/p14e_managing_p1d_users.html) for information and instructions.

6. Manage certificates for your account.

   See [Certificate management](../pingone_for_enterprise/p14e_managing_certificates.html) for information.

## Next steps

If you encounter problems as you configure PingOne for Enterprise, visit the [Ping support portal](https://support.pingidentity.com/s/) to look for answers, or [sign on to your account](https://www.pingidentity.com/en/account/sign-on.html) to file a support case.

---

---
title: Invited PingOne for Enterprise SSO
description: Invited SSO allows PingOne SSO for SaaS Apps customers to delegate SSO configurations to their partners.
component: pingoneforenterprise
page_id: pingoneforenterprise:invited_pingone_for_enterprise_sso:p14e_invited_sso
canonical_url: https://docs.pingidentity.com/pingoneforenterprise/invited_pingone_for_enterprise_sso/p14e_invited_sso.html
revdate: April 15, 2024
---

# Invited PingOne for Enterprise SSO

Invited SSO allows PingOne SSO for SaaS Apps customers to delegate SSO configurations to their partners.

Partners can manage both IdP and SP sides of the connection themselves. Invited SSO also allows partners to connect to non-SAML IdPs using PingOne for Enterprise as a bridge.

|   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|   | Invited SSO is a legacy function that has been improved on by PingOne SSO for SaaS Apps Managed Accounts.Managed Accounts lets you directly manage and monitor partner accounts, and also allows you to delegate management by assigning appropriate administrative roles. This gives your partners the ability to manage their own accounts, but also allows you to access a partner account for onboarding or troubleshooting.To learn more, see [Manage partner accounts](../pingone_sso_for_saas_apps/p14saas_manage_partner_accounts.html). |