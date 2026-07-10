---
title: Penetration and load testing
description: Information about our penetration and load-testing policies.
component: pingoneadvancedservices
page_id: pingoneadvancedservices::p1as_load_testing
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/p1as_load_testing.html
revdate: September 15, 2025
section_ids:
  _penetration_load_testing: Penetration and load-testing policy
  _load_testing_requests: Load-testing requests
---

# Penetration and load testing

Penetration testing is a simulated attack designed to find and exploit vulnerabilities in a system's defenses that attackers could take advantage of, while load testing determines if the system will perform as intended under normal conditions.

Our policies regarding these tests were created to:

* **Preserve platform stability**: Unplanned testing can interfere with our ability to effectively support all of our customers. Since some tests are initially indistinguishable from denial-of-service (DoS) attacks or other serious issues, they can:

  * Set off alarms

  * Cause service shutdowns

  * Add services and IPs to deny lists

  * Prevent our Support teams from taking the appropriate remedial actions.

    This type of disruption can also disproportionately occupy our Support teams, which will delay our response to other customers.

* **Regulate testing**: When you request a load test, we ask that you provide us with your load testing plan, origin of testing information, and the name and contact information for members of your testing team. That way, we can schedule the tests and help ensure that your testing approach is realistic, manageable, and provides meaningful results.

* **Avoid unnecessary testing**: At Ping Identity, we test all of our infrastructure and applications for you using code scans and automated load tests, which ensures that testing methods are consistent and can be compared over time. A third party performs penetration testing.

## Penetration and load-testing policy

With PingOne Advanced Services, penetration testing is performed by a third party, which is an industry best practice. We can share the results of these tests with you at any time. Our engineers review the test results, eliminate false positives, and perform in-depth analysis regarding the security of your infrastructure and applications.

Regarding load testing, you can:

* Indirectly test Ping Identity infrastructure and applications, as part of a wider test of your own infrastructure and applications, in your staging environment. Load testing is not permitted in your development, test, and production environments.

* Specify the number of identities you intend to create and the throughput levels you intend to simulate, which should not exceed the number of licenses you have.

You cannot:

* Directly test Ping Identity-hosted infrastructure and applications. This specifically applies to DoS or DDoS attacks. Ping Identity already does this testing on your behalf.

* Authorize a third party to perform load testing without Ping Identity's prior written consent. To perform load testing, we must receive your request in writing at least 2 weeks prior to the proposed test date.

## Load-testing requests

When requesting a load test, we ask that you provide us with your:

* **Load-testing plan**: Describe the strategy you intend to follow when testing your own infrastructure and applications.

  Indicate the number of identities you intend to create, and the throughput levels you intend to simulate. This number should align with the number of identities and throughput level you agreed upon with Ping Identity when you purchased the service, and should not exceed the following thresholds:

  * Agreed number of identities +25%

  * Agreed throughput +50%

    This plan should also avoid unrealistic patterns, such as the setup and tear down of many identities for each load test, and instantaneous user actions, such as changing the password and simultaneously attempting to use the new password.

* **Origin of testing documentation**: Specify whether the testing will originate from an external source over the internet or from an internal source within your organization. If it's originating from an external source, you must also supply IP addresses.

* **Contact name**: Provide the name of a member of your testing team and their contact information in case we have questions or need to stop the testing for any reason.

In the unlikely event that a vulnerability is discovered in the Ping infrastructure or applications, we also need you to attest, in writing, that you will not test the vulnerability further than the point of discovery, and that you will immediately report the issue to us.