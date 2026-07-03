---
title: Changelog
description: The following is the change history for the PingAM Integration Kit.
component: pingam
page_id: pingam:release_notes:pf_pingam_ik_changelog
canonical_url: https://docs.pingidentity.com/integrations/pingam/release_notes/pf_pingam_ik_changelog.html
revdate: May 21, 2026
section_ids:
  pingam-integration-kit-1-4-may-2026: PingAM Integration Kit 1.4 - May 2026
  pingam-integration-kit-1-3-1-november-2025: PingAM Integration Kit 1.3.1 - November 2025
  pingam-integration-kit-1-3-october-2025: PingAM Integration Kit 1.3 - October 2025
  pingam-integration-kit-1-2-february-2025: PingAM Integration Kit 1.2 - February 2025
  pingam-integration-kit-1-1-november-2024: PingAM Integration Kit 1.1 – November 2024
  pingam-integration-kit-1-0-august-2024: PingAM Integration Kit 1.0 – August 2024
---

# Changelog

The following is the change history for the PingAM Integration Kit.

## PingAM Integration Kit 1.4 - May 2026

* Added the ability to indicate that an attribute in the Journey Response Mappings is multi-valued.\
  Learn more in step 5d of [Configuring an adapter instance](../setup/pf_pingam_ik_configuring_an_adapter_instance.html).

* Added the **Always Authenticate User** option to authenticate the user with a PingAM Journey.

## PingAM Integration Kit 1.3.1 - November 2025

* Fixed an issue that caused PingFederate to not send a username value to PingAM when using backchannel authentication.

  A new tracked HTTP request parameter called `username` is now available. Entering `login_hint` as the **Source Parameter** in step 4d of [Configuring an adapter instance](../setup/pf_pingam_ik_configuring_an_adapter_instance.html) prompts PingFederate to send the username value to PingAM as a string.

## PingAM Integration Kit 1.3 - October 2025

* Username validation only occurs once now. If validation fails, the adapter encounters an error.

* The `redirect_uri` no longer includes any additional parameters. Learn more in [Known issues and limitations](pf_pingam_ik_known_issues_and_limitations.html).

## PingAM Integration Kit 1.2 - February 2025

* Added the ability to use backchannel communication with PingAM to pass data from PingFederate to PingAM securely.

  To send PingFederate parameters to PingAM, you must create an OAuth client in PingAM and update the PingAM IdP Adapter configuration with the associated **Client ID** and **Client Secret**.

  Learn more in step 6 of [Preparing to use a PingAM journey](../setup/pf_pingam_ik_using_pingam_journey.html) and refer to the **Client ID** and **Client Secret** table entries in [PingAM IdP Adapter settings reference](../setup/pf_pingam_ik_pingam_idp_adapter_settings_reference.html).

* Added the ability to configure whether the PingAM session should be deleted after a user signs off from the protected application.

  Learn more in the **Logout Mode** table entry in the [PingAM IdP Adapter settings reference](../setup/pf_pingam_ik_pingam_idp_adapter_settings_reference.html).

## PingAM Integration Kit 1.1 – November 2024

* Added the ability to track PingFederate and PingAM transactions using a unique request ID that's set by the adapter. This enhances the application log debugging experience. You can find configuration instructions in [Tracking transactions between PingFederate and PingAM](../troubleshooting/pf_pingam_ik_tracking_transactions.html).

* Added the ability to perform username validation. To do so, configure the [Username Path](../setup/pf_pingam_ik_pingam_idp_adapter_settings_reference.html) between the username that the adapter receives from the authentication policy and a value in the PingAM session info payload.

* Fixed an issue that caused an infinite loop between PingFederate and PingAM if the PingAM and adapter cookie name values didn't match. The adapter now fails if it doesn't receive the expected cookie name from PingAM.

## PingAM Integration Kit 1.0 – August 2024

* Initial release
