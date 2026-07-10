---
title: System requirements
description: This version of the Ping Identity Custom Claims Provider for SharePoint requires the following:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker::pf_sharepoint_peoplepicker_ik_system_requirements
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/pf_sharepoint_peoplepicker_ik_system_requirements.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
---

# System requirements

This version of the Ping Identity Custom Claims Provider for SharePoint requires the following:

* Microsoft SharePoint Server 2016, 2019, or Subscription Edition configured with PingFederate as the Trusted Identity Token Issuer.

* Connectivity to one or more backing LDAP user stores. Testing has been performed on Microsoft Active Directory 2016 and Microsoft Active Directory on Windows Server 2022.

|   |                                                                                                                                                                                                                                                                                           |
| - | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   | Microsoft has announced the end of extended support for [SharePoint Server 2016](https://learn.microsoft.com/en-us/lifecycle/products/sharepoint-server-2016) and [SharePoint Server 2019](https://learn.microsoft.com/en-us/lifecycle/products/sharepoint-server-2019) on July 14, 2026. |

---

---
title: Uninstall the solution
description: In Central Administration disable the Trusted Identity provider from the web application.
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:troubleshooting:pf_sharepoint_peoplepicker_ik_uninstall_the_solution
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/troubleshooting/pf_sharepoint_peoplepicker_ik_uninstall_the_solution.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 11, 2026
section_ids:
  steps: Steps
---

# Uninstall the solution

## Steps

1. In Central Administration disable the Trusted Identity provider from the web application.

   This step must be completed for each web application that is using that Trusted Identity provider (also known as the Partner STS or Trusted Identity Token Issuer).

![qsz1563995703178](_images/qsz1563995703178.jpg)

1. In **Central Administration > System Settings > Farm Features** deactivate the Ping Identity People Picker Claims Provider farm feature.

   ![qzl1563995704583](_images/qzl1563995704583.jpg)

2. In **Central Administration > Site Settings > Site Features** deactivate the Ping Identity People Picker Claims Administration site feature.

   ![sok1563995705092](_images/sok1563995705092.jpg)

3. In **Central Administration > System Settings > Farm Solutions** retract the pingidentity.sharepoint.ppclaimsprovider.wsp solution.

   ![awz1563995705587](_images/awz1563995705587.jpg)

4. In **Central Administration > System Settings > Farm Solutions** retract the pingidentity.sharepoint.ppclaimsprovider.wsp solution.

   |   |                                                                                                    |
   | - | -------------------------------------------------------------------------------------------------- |
   |   | During retraction, schedule 10 minutes to prevent timer issues that sometimes occur in SharePoint. |

   ![afs1563995706306](_images/afs1563995706306.jpg)

5. Open SharePoint Management Shell as an Administrator.

6. Make a backup copy of your configuration settings for your existing Trusted Identity Token Issuer. For example: use this command tor produce a file called partnersts.txt that contains your list of token issuers and their settings:

   ```
   Get-SPTrustedIdentityTokenIssuer >partnersts.txt
   ```

7. Use this command to delete your current Trusted Identity Token Issuer:

   ```
   Remove-SPTrustedIdentityTokenIssuer –Identity "<PartnerSTS>"
   ```

   Replace `<PartnerSTS>` with the Name of your Trusted Identity Token Issuer.

8. User PowerShell to recreate your SP Trusted Identity Token Issuer (without setting the default claims provider). You can refer to the partnersts.txt to review what settings you used previously.

9. In Central Administration reconfigure the web application to use the newly created SPTrustedIdentityTokenIssuer.

10. (Optional) For a complete cleanup, you may also wish to remove the People Picker configuration settings that were stored for each web application that you configured to use the People Picker. This can be done by running the following commands via the SharePoint Management Shell for each web application:

    * Identify the web application by replacing `<web app URL>` with the SharePoint Web Application's URL:

      ```shell
      $webApp = Get-SPWebApplication <web app URL>
      ```

    * To view the settings associated for the web application:

      ```shell
      $webApp.Properties["PingClaimsProviderConfig"]
      ```

    * To remove the settings associated for the web application:

      ```shell
      $webApp.Properties.Remove("PingClaimsProviderConfig")
      $webApp.Update()
      ```

---

---
title: Upgrade from a previous version
description: Use Update-SPSolution in a Sharepoint Management Shell to upgrade to a newer version:
component: sharepoint-peoplepicker
page_id: sharepoint-peoplepicker:setup:pf_sharepoint_peoplepicker_ik_upgrade_from_a_previous_version
canonical_url: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/setup/pf_sharepoint_peoplepicker_ik_upgrade_from_a_previous_version.html
llms_txt: https://docs.pingidentity.com/integrations/sharepoint-peoplepicker/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: June 20, 2024
---

# Upgrade from a previous version

Use Update-SPSolution in a Sharepoint Management Shell to upgrade to a newer version:

```
Update-SPSolution -Identity pingidentity.sharepoint.ppclaimsprovider.wsp
     -LiteralPath "C:\path_to_solution\PingIdentity.SharePoint.PPClaimsProvider.wsp"
     –GacDeployment
```

|   |                                                                                            |
| - | ------------------------------------------------------------------------------------------ |
|   | The remaining steps of the Installation and Setup section are not required when upgrading. |