---
title: About account linking
description: Account linking provides a means for a user to log on to disparate sites with just one authentication when the user has established accounts and credentials at each site.
component: pingfederate
version: 13.1
page_id: pingfederate:introduction_to_pingfederate:pf_about_account_link
canonical_url: https://docs.pingidentity.com/pingfederate/13.1/introduction_to_pingfederate/pf_about_account_link.html
llms_txt: https://docs.pingidentity.com/pingfederate/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: July 5, 2022
section_ids:
  processing-steps: Processing steps
---

# About account linking

Account linking provides a means for a user to log on to disparate sites with just one authentication when the user has established accounts and credentials at each site.

All protocols support this method of interconnecting accounts across domains.

Account linking involves a persistent name identifier associated with accounts at each participating site. The assertion conveys the name identifier, which can be an opaque pseudonym. Once established locally, the service provider (SP) can use the account link to look up the user and provide access without re-authentication.

![Diagram illustrating the 4 steps involved in account linking.](_images/bkp1564003101403.jpg)Account linking

## Processing steps

1. David Smith logs on to Site A as *davidsmith*. He then decides to access his account on Site B through Site A.

2. Optionally, the federation server looks up additional attributes from the datastore.

3. The Site A federation server sends a persistent name identifier to Site B, along with any other attributes.

   |   |                                                                                                                         |
   | - | ----------------------------------------------------------------------------------------------------------------------- |
   |   | When using a pseudonym and sending other attributes, be careful not to send attributes that could identify the subject. |

4. The federation server on Site B uses the information to associate the pseudonym with the existing account of *dsmith* and optionally might ask David to provide consent to the linking.

   Once the link has been established, Site B stores the information so that David only has to log on to Site A to access Site B.
