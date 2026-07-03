---
title: Penetration and load testing
description: Ping Identity has strict policies regarding penetration testing and load testing of your Ping Government Identity Cloud infrastructure and applications.
component: pgic
page_id: pgic:penentration_load_testing:pgic_pentration_load_testing
canonical_url: http://docs.pingidentity.com/pgic/penentration_load_testing/pgic_pentration_load_testing.html
section_ids:
  load-testing-requests: Load testing requests
---

# Penetration and load testing

Ping Identity has strict policies regarding penetration testing and load testing of your Ping Government Identity Cloud infrastructure and applications.

The policy exists for the following reasons:

* **Preserves platform stability for all customers**: Unscheduled testing can cause severe problems, as it can initially be indistinguishable from a real problem or a DoS attack. Unscheduled tests can also set off alarms, cause service shutdowns, add services and IPs to deny lists, and can disproportionately occupy our Support team and delay our response to other customers with urgent issues.

* **Regulates testing**: The policy regulates how testing is approached so that it's realistic and manageable. For example, a load testing plan would not be approved if it created and deleted large numbers of identities and entitlements for each test, as this isn't a realistic pattern of behavior.

* **Avoids unnecessary testing**: At Ping Identity, we directly test the infrastructure and applications on your behalf, using code scans, penetration tests, and automated load tests. This process ensures that testing is consistent and that results can be compared over time.

Penetration testing is done by a third party, who follows industry best practices. Our engineers analyze the results and eliminate false positives, and can then share the results with you.

Regarding load testing, you can:

* Indirectly test Ping Identity infrastructure and applications as part of a wider test of your own infrastructure and applications. Load testing isn't permitted in your Development, Test, and Production environments. However, you can perform load testing in your Staging environment or Production environment prior to live customer activity.

* Perform load testing up to the licence volume limits listed in your sales agreement.

You can't:

* Directly test Ping Identity-hosted infrastructure and applications. This specifically applies to DoS or DDoS attacks. Ping Identity already does this on your behalf.

* Authorize a third party to perform load testing without Ping Identity's prior written consent.

* To obtain this consent, we ask that you provide us with your load-testing plan at least 2 weeks prior to the proposed test date.

## Load testing requests

When requesting a load test, we ask that you provide us with your:

* **Load-testing plan**: Describe the strategy you intend to follow when testing your own infrastructure and applications.

  Indicate the number of identities you intend to create, and the throughput levels you intend to simulate. This number should align with the number of identities and throughput level you agreed upon with Ping Identity when you purchased the service. It shouldn't exceed the following thresholds:

  Agreed number of identities +25% Agreed throughput +50%

  This plan should also avoid unrealistic patterns, such as the setup and tear down of many identities for each load test, and instantaneous user actions, such as changing the password and simultaneously attempting to use the new password.

* **Origin of testing documentation**: Specify whether the testing will originate from an external source over the internet or from an internal source within your organization. If it's originating from an external source, you must also supply IP addresses.

* **Contact name**: Provide the name of a member of your testing team and their contact information in case we have questions or need to stop the testing for any reason.

After submitting your load-testing plan, a ticket will be created for our Product Architecture team to review. If the Product Architecture team approves the plan, we'll submit it to our Change Access Board (CAB) team for review and approval. We'll keep you informed of progress through the ticket.

In the unlikely event that a vulnerability is discovered in the Ping Identity infrastructure or applications, we also need you to attest, in writing, that you won't test the vulnerability further than the point of discovery and that you will immediately report the issue to us.
