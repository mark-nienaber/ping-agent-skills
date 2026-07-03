---
title: About indexes
description: Understand how PingDS uses indexes to respond quickly to LDAP searches, and how indexes are maintained when directory data changes.
component: pingds
version: 8.1
page_id: pingds:config-guide:idx-about
canonical_url: https://docs.pingidentity.com/pingds/8.1/config-guide/idx-about.html
llms_txt: https://docs.pingidentity.com/pingds/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: 2026-01-02T15:53:44Z
keywords: ["Features", "LDAP", "Setup &amp; Configuration"]
section_ids:
  role_of_an_index: Role of an index
  index_implementation: Index implementation
  how_ds_uses_indexes: How DS uses indexes
  unindexed-searches: Unindexed searches
  index-updates: How DS updates indexes
  changing_an_index_doesnt_reindex_existing_data: Changing an index doesn't reindex existing data
  rebuilding_indexes: Rebuilding indexes
---

# About indexes

A basic, standard directory feature is the ability to respond quickly to searches.

An LDAP search specifies the information that directly affects how long the directory might take to respond:

* The base DN for the search.

  The more specific the base DN, the less information to check during the search. For example, a request with base DN `dc=example,dc=com` potentially involves checking many more entries than a request with base DN `uid=bjensen,ou=people,dc=example,dc=com`.

* The scope of the search.

  A subtree or one-level scope targets many entries, whereas a base search is limited to one entry.

* The search filter to match.

  A search filter asserts that for an entry to match, it has an attribute that corresponds to some value. For example, `(cn=Babs Jensen)` asserts that `cn` must have a value that equals `Babs Jensen`.

  A directory server would waste resources checking all entries for a match. Instead, directory servers maintain indexes to expedite checking for a match.

LDAP directory servers disallow searches that cannot be handled expediently using indexes. Maintaining appropriate indexes is a key aspect of directory administration.

## Role of an index

The role of an index is to answer the question, "Which entries have an attribute with this corresponding value?"

Each index is therefore specific to an attribute.

Each index is also specific to the comparison implied in the search filter. For example, a directory server maintains distinct indexes for exact (equality) matching and for substring matching. The types of indexes are explained in [Index types](idx-types.html). Furthermore, indexes are configured in specific directory backends.

## Index implementation

An index is implemented as a tree of key-value pairs. The key is a form of the value to match, such as `babs jensen`. The value is a list of IDs for entries that match the key. The figure that follows shows an equality (case ignore exact match) index with five keys from a total of four entries. If the data set were large, there could be more than one entry ID per key:

![An index is implemented as a tree of key-value pairs.](../_images/equality-index.png)

## How DS uses indexes

This example illustrates how DS uses an index.

When the search filter is `(cn=Babs Jensen)`, DS retrieves the IDs for entries whose CN matches `Babs Jensen` by looking them up in the equality index of the CN attribute. (For a complex filter, it might optimize the search by changing the order in which it uses the indexes.) A successful result is zero or more entry IDs. These are the candidate result entries.

For each candidate, DS retrieves the entry by ID from a system index called `id2entry`. As its name suggests, this index returns an entry for an entry ID. If there is a match, and the client application has the right to access the data, DS returns the search result. It continues this process until no candidates are left.

## Unindexed searches

If there are no indexes that correspond to a search request, DS must check for a match against every entry in the scope of the search. Evaluating every entry for a match is referred to as an unindexed search *(tooltip: \<div class="paragraph">
\<p>A search operation for which the server has no appropriate index.\</p>
\</div>)*.

An unindexed search is an expensive operation, particularly for large directories. A server refuses unindexed searches unless the user has specific permission to make such requests. The permission to perform an unindexed search is granted with the `unindexed-search` privilege. This privilege is reserved for the directory superuser by default. It should not be granted lightly.

If the number of entries is smaller than the default resource limits, you can still perform what appear to be unindexed searches, meaning searches with filters for which no index appears to exist. That is because the `dn2id` index returns all user data entries without hitting a resource limit that would make the search unindexed.

Use cases that may call for unindexed searches include the following:

* An application must periodically retrieve a very large amount of directory data all at once through an LDAP search.

  For example, an application performs an LDAP search to retrieve everything in the directory once a week as part of a batch job that runs during off-peak hours.

  Make sure the application has no resource limits. Learn more in [Enforce limits](../use-cases/limits.html).

* A directory data administrator occasionally browses directory data through a graphical UI without initially knowing what they are looking for or how to narrow the search.

  Big indexes let you work around this problem. They facilitate searches where large numbers of entries match. For example, big indexes can help when paging through all the employees in a large company, or all the users in the state of California. Learn more in [Big index](idx-types.html#big-indexes) and [Indexes for attributes with few unique values](idx-config.html#use-big-indexes).

  Alternatively, DS directory servers can use an appropriately configured VLV index to sort results for an unindexed search. Learn more in [VLV for paged server-side sort](idx-config.html#vlv-for-paged-sss).

## How DS updates indexes

DS updates indexes when directory data changes. When you import data from LDIF or when an application adds, modifies, or deletes an entry, DS updates each affected index based on its configuration.

DS updates indexes while the server is online. This has a cost, and the cost is the reason to maintain only indexes applications actually use. Updating an unindexed attribute is faster than updating an indexed attribute.

### Changing an index doesn't reindex existing data

You, the administrator, define how DS indexes attributes. You configure which attributes to index and the type of indexes to maintain for each attribute.

You can [change index configurations at any time](idx-config.html).

DS doesn't automatically reindex existing data when you change an index configuration, however. "Automatic" index updates only happen when directory data changes.

### Rebuilding indexes

After changing an index configuration, you can manually [rebuild indexes](idx-config.html#rebuild-index), forcing DS to update indexes for the existing directory data.

Importing data from LDIF, which replaces the data in a backend, also forces DS to index all the data.
