---
title: Data loading and access
description: When transitioning to Ping Government Identity Cloud, you'll need to load your existing data from your legacy systems into your Ping Government Identity Cloud deployment.
component: pgic
page_id: pgic::pgic_data_loading
canonical_url: http://docs.pingidentity.com/pgic/pgic_data_loading.html
---

# Data loading and access

When transitioning to Ping Government Identity Cloud, you'll need to load your existing data from your legacy systems into your Ping Government Identity Cloud deployment.

For security reasons, Ping Identity will not, and should not, have access to your data. However, our Professional Services team will work closely with you to ensure the transition is as painless as possible. We'll discuss the methods we'll use during the system planning and requirements gathering phase.

These methods include:

* Importing an LDIF file remotely through an LDAP browser

* Using PingDataSync or PingIDM

If you intend to use NGINX or PingAccess, request sizes can't be larger than 1 MB.