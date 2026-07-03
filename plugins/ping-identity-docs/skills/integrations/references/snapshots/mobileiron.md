---
title: Configuration examples
description: The following examples use the adapter's issuance criteria to put restrictions on authorizing users to access protected resources.
component: mobileiron
page_id: mobileiron:setup:pf_mobileiron_ik_configuration_examples
canonical_url: https://docs.pingidentity.com/integrations/mobileiron/setup/pf_mobileiron_ik_configuration_examples.html
revdate: November 5, 2025
section_ids:
  restrict-users-based-on-device-ownership: Restrict users based on device ownership
  restrict-users-based-on-device-operating-system: Restrict users based on device operating system
---

# Configuration examples

The following examples use the adapter's issuance criteria to put restrictions on authorizing users to access protected resources.

You can find more information about adapter contract mapping in [Defining the IdP adapter contract](https://docs.pingidentity.com/pingfederate/latest/administrators_reference_guide/help_authnadapterinstancetasklet_plugincontractstate.html) in the PingFederate documentation.

## Restrict users based on device ownership

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Open the MobileIron adapter you configured.

2. Click **Adapter Contract Mapping**, then click **Configure Adapter Contract** to access the adapter's attribute mapping summary page. Go to the **Issuance Criteria** section.

3. In the **Source** list, select `adapter`.

4. In the **Attribute Name** list, select `Ownership`.

5. In the **Condition** list, select `not equal to`.

6. The MobileIron Device API returns one of three values for ownership:

   * `COMPANY` for Corporate-owned devices

   * `EMPLOYEE` for Employee-owned devices

   * `UNKNOWN`

   Select the device ownership type that complies with your business practices.

7. Click **Add**, click **Done** twice, then click **Save**.

## Restrict users based on device operating system

1. In the PingFederate admin console, go to **Authentication > Integration > IdP Adapters**. Open the MobileIron adapter you configured.

2. Click **Adapter Contract Mapping**, then click **Configure Adapter Contract** to access the adapter's attribute mapping summary page. Go to the **Issuance Criteria** section.

3. In the **Source** list, select `adapter`.

4. In the **Attribute Name** list, select `os`.

5. In the **Condition** list, select `not equal to`.

6. The MobileIron Device API returns different values for device operating systems.

   * `IOS`

   * `ANDROID`

   Select the device operating system type that complies with your business practices.

7. Click **Add**, click **Done** twice, then click **Save**.
