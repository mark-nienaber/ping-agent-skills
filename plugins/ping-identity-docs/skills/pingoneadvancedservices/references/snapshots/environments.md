---
title: Data storage considerations
description: Data is measured in entries. An entry could be a user account, the grants associated with that user, or any data associated with that user. The total number of entries is also known as the total number of objects.
component: pingoneadvancedservices
page_id: pingoneadvancedservices:environments:p1as_data_storage
canonical_url: https://docs.pingidentity.com/pingoneadvancedservices/environments/p1as_data_storage.html
revdate: July 23, 2024
---

# Data storage considerations

Data is measured in entries. An entry could be a user account, the grants associated with that user, or any data associated with that user. The total number of entries is also known as the total number of objects.

The amount of data that can be loaded to an environment depends on the size of each entry, the amount of memory required to store it, and the amount of storage available. As the schema for an entry is customized for each customer, there is no single calculation that can be made to determine how much memory and storage a customer will require.

In these examples, we illustrate how data storage is calculated using two different entry sizes.

* If the average size of each entry is 1 KB, and 1 GB can store 1 million KB:

  1 KB per entry \* 1 million entries = 1 GB of storage needed.

* If the average size of each entry is larger, the number of entries that can be stored in each GB will be smaller. For example, if the average size of each entry is 10 KB, you can only store about 100,000 entries:

  10 KB per entry \* 100,000 entries = 1 GB of storage needed.

![This image illustrates the storage capacity when the average size of each entry is 1 KB and when the average size of each entry is 10 KB.](_images/msk1678908440884.png)

Remember that Development and Testing environments are provisioned with 8 GB of RAM and 40 GB of disk space and are not intended for load testing. You can load a portion of your data into those environments to quality-check your applications and perform user acceptance testing, and then move all of your data to the Staging environment for performance and load testing.
