---
title: Ongoing network maintenance
description: After Ping Government Identity Cloud is implemented, it's important that ongoing maintenance occurs to help keep your systems secure and compliant.
component: pgic
page_id: pgic:maintenance:pgic_mainentance
canonical_url: http://docs.pingidentity.com/pgic/maintenance/pgic_mainentance.html
---

# Ongoing network maintenance

After Ping Government Identity Cloud is implemented, it's important that ongoing maintenance occurs to help keep your systems secure and compliant.

* **Maintenance**: Platform and infrastructure maintenance windows occur on the first and third Tuesday from 6 PM to 12 AM Eastern Standard Time (EST). These maintenance processes are typically non-intrusive, however, you might experience some disruption during these times.

* **Patches**: Patches are small code releases that fix specific bugs or close known vulnerabilities and are often urgently released.

  Although you can choose when to add patches to your production environment, you must apply the patches within 30 days to remain FedRAMP compliant.

  Patches are delivered through GitLab and ready to be consumed in your pipeline. It's your responsibility to test the patch against your specific configuration to ensure configuration changes aren't needed.

  Be aware that if any customized configurations have been made, this might break when a patch is consumed. Apply the patch to your Dev and Test environments first to ensure that your configuration works with the patch.

* **Vulnerabilities**: Vulnerabilities are weaknesses or gaps that attackers can exploit to compromise security, steal data, or disrupt operations.

  When vulnerabilities are identified, patches will be provided and applied within 30 days. Test and Prod clusters running in the boundary must be on the most recent version available.

  As part of FedRAMP ConMon requirements for vulnerability scanning, routine container and cluster updating should be scheduled on a monthly basis by your team. New build pipelines must be run against the latest versions, which are built on a daily basis.

* **Upgrades**: To comply with FedRAMP regulations, Ping Government Identity Cloud customers must upgrade within 30 days of notification of a new version being available.

* **Hotfix updates and rollbacks**: If hotfix updates or rollbacks are needed, contact our Support team, which is contracted as FedDevOps. Depending on the severity of the issue, the Support team will handle the request immediately or create a ticket to schedule the fix or rollback needed.
