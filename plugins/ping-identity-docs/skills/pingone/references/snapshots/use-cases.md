---
title: Before you begin configuring Microsoft Entra hybrid join with PingOne as the federated IdP
description: Complete the prerequisites before you can configure Microsoft Entra hybrid join to allow users to access Active Directory and Entra ID resources.
component: pingone
page_id: pingone:use_cases:p1_microsoft_entra_hybrid_join_prerequisites
canonical_url: https://docs.pingidentity.com/pingone/use_cases/p1_microsoft_entra_hybrid_join_prerequisites.html
llms_txt: https://docs.pingidentity.com/pingone/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: October 17, 2025
section_ids:
  p1-download-entra-connect-sync: Downloading Entra Connect Sync
  steps: Steps
  p1-install-entra-connect-sync: Installing Entra Connect Sync
  steps-2: Steps
  result: Result:
  next-steps: Next steps
---

# Before you begin configuring Microsoft Entra hybrid join with PingOne as the federated IdP

Before you can set up PingOne as the federated identity provider (IdP) for Microsoft Entra ID and enable hybrid join, you must complete the prerequisites in this topic.

|   |                                                                                                                                                                                                                                                                                                                                                                               |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | * Don't use a production environment or configuration in PingOne, Active Directory (AD), or Entra ID for the initial setup.

* Test the configuration in a pre-production environment before implementing in a production environment.

* Roll out the solution in stages to a limited set of users initially and gradually increase the set of users if no issues are found. |

You must have the following:

* A PingOne organization. Learn more in [Starting a PingOne trial](../getting_started_with_pingone/p1_start_a_p1_trial.html).

* A pre-production PingOne environment, such as development or test, with the PingOne SSO service added.

* An AD domain with the following:

  * Your user identities and device records stored in the domain.

  * The service account username and password.

* An Entra account with:

  * A tenant with a verified custom domain configured as a federated domain, where Entra ID redirects users to a federated IdP for authentication.

    Learn more about domains in [Managing custom domain names](https://learn.microsoft.com/en-us/entra/identity/users/domains-manage) in the Entra documentation.

  * Either the Entra Hybrid Identity Administrator or Global Administrator role assigned.

  * Entra Connect Sync installed on a domain-joined Windows Server 2016 or later following the steps in these sections:

    1. [Download Entra Connect Sync](#p1-download-entra-connect-sync).

    2. [Install Entra Connect Sync](#p1-install-entra-connect-sync).

  |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
  |   | You must use Entra Connect Sync in this configuration and can't use Entra Connect Cloud Sync. Learn more in [What is Microsoft Entra Connect?](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/whatis-azure-ad-connect#) and [Comparison between Microsoft Entra Connect Sync and Cloud Sync](https://learn.microsoft.com/en-us/entra/identity/hybrid/cloud-sync/what-is-cloud-sync#comparison-between-microsoft-entra-connect-and-cloud-sync) in the Entra documentation. |

## Downloading Entra Connect Sync

Download Entra Connect Sync to sync AD users and devices joined to the domain to a verified custom domain in Entra ID.

### Steps

1. Review the [Entra Connect prerequisites and hardware requirements](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/how-to-connect-install-prerequisites) in the Entra documentation.

2. On a Windows-based computer, download Entra Connect Sync:

   1. In the Entra admin center, enter `Entra Connect` in the search bar.

   2. Go to **Microsoft Entra Connect > Connect Sync**.

   3. Click **Download the latest Entra Connect Sync Version**.

      ![A screen capture of the page from which to download Connect Sync in the Microsoft Entra admin center.](_images/p1-entra-hybrid-join-download-connect-sync.png)

## Installing Entra Connect Sync

After downloading Entra Connect Sync, install it with the following configuration to ensure Entra hybrid join can sync successfully with AD.

### Steps

1. On the Windows-based computer on which Entra Connect Sync is downloaded, run the installation program.

2. In the **Microsoft Entra Connect Sync** installation tool, select the checkbox to consent to the terms and click **Continue**.

3. In the **Express Settings** step, click **Customize**.

4. In the **Required Components** steps, leave all the checkboxes cleared and click **Install**.

5. In the **User Sign-In** step, select **Do not configure** for the sign-on method and click **Next**.

   ![A screen capture of the Entra Connect Sync installation program - User sign-in step.](_images/p1-entra-hybrid-join-connect-sync-user-signin.png)

6. In the **Connect to Microsoft Entra ID** step, sign on to your Entra ID account.

7. In the **Connect Directories** step, ensure the AD domain displayed for **Forest** is the AD domain you want to use for hybrid join and click **Add Directory**.

   ![A screen capture of the Entra Connect Sync installation program - Connect your directories step.](_images/p1-entra-hybrid-join-connect-sync-directory.png)

   #### Result:

   The **AD forest account** window opens.

   1. Select **Create new AD account**.

   2. Enter the applicable Enterprise admin AD account sign-on credentials.

   3. Click **OK**.

   4. In the **Connect your directories** step, click **Next**.

8. []()In the **Microsoft Entra sign-in** step, verify **User Principal Name** is set to `userPrincipalName` as the on-premise attribute to use as the Entra ID username and click **Next**.

   ![A screen capture of the Entra Connect Sync installation program - Microsoft Entra sign-in configuration step.](_images/p1-entra-hybrid-join-connect-sync-upn.png)

9. In the **Domain/OU Filtering** step:

   1. Click **Sync selected domains and OUs**.

   2. Select the checkboxes for any organizational units (OUs) where cloud users to be synced to Entra ID are located.

      |   |                                                                                                                                                                                                                                                                                                                                      |
      | - | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
      |   | Although you can select multiple OUs in this step, we recommend only selecting the OU where your users are located. When users can successfully authenticate with PingOne, you can configure Entra Connect Sync to sync devices in [Configuring Entra Connect Sync](p1_microsoft_hybrid_join_tasks.html#p1-configure-entra-connect). |

      ![A screen capture of the Entra Connect Sync installation program - Domain and OU filtering step.](_images/p1-entra-hybrid-join-connect-sync-ou-filtering.png)

   3. Click **Next**.

10. In the **Identifying users** step, leave the default settings and click **Next**.

    The default **Let Azure manage the source anchor** setting means Entra ID will identify users with the `sourceAnchor` attribute of `mS-DS-ConsistencyGuid`.

    ![A screen capture of the Entra Connect Sync installation program - Identifying users step.](_images/p1-entra-hybrid-join-connect-sync-identifying-users.png)

    Learn more about `sourceAnchor` in [Entra Connect: Design concepts](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/plan-connect-design-concepts) in the Entra documentation.

11. In the **Filtering** step:

    1. Choose either:

       * **Synchronize all users and devices**: Syncs all users and devices to Entra ID.

       * **Synchronize selected**: Allows you to enter a name or distinguished name (DN) of a group to sync to Entra ID.

    2. Click **Next**.

12. In the **Optional Features** step, leave all the checkboxes cleared and click **Next**.

    ![A screen capture of the Entra Connect Sync installation program - Optional features step.](_images/p1-entra-hybrid-join-connect-sync-optional-features.png)

13. In the **Configure** step, select the **Start the synchronization process when configuration completes** checkbox and click **Install**.

14. When the installation completes, click **Exit**.

15. In the Entra admin center, go to the **All users** page and verify the expected users appear. It could take a few minutes for the users to sync.

16. Use ADSI Edit to connect to your AD domain and ensure each user object in the OU for cloud users is populated with the `mS-DS-ConsistencyGuid` value after the initial sync.

    If any AD user object is missing the `mS-DS-ConsistencyGuid` value:

    1. Re-run the Entra Connect Sync installation program.

    2. In the **Tasks** step, click **Customize synchronization options** and click through the steps without changing any settings.

       ![A screen capture of the Entra Connect Sync installation program - Additional tasks step.](_images/p1-entra-hybrid-join-connect-sync-tasks.png)

    3. In the **Configure** step, select the **Start the synchronization process when configuration completes** checkbox and click **Configure**.

       ![A screen capture of the Entra Connect Sync installation program - Ready to configure step.](_images/p1-entra-hybrid-join-connect-sync-ready.png)

### Next steps

Complete the setup in [Configuring PingOne as the federated IdP](p1_microsoft_hybrid_join_tasks.html).
