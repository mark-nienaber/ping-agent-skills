---
title: About alternate authorization identities
description: Alternate authorization identities allow for the proper evaluation of access control rules for users whose entries aren't present within an entry-balanced dataset.
component: pingdirectory
version: 11.1
page_id: pingdirectory:pingdirectoryproxy_server_administration_guide:pd_proxy_about_alt_authn_ids
canonical_url: https://docs.pingidentity.com/pingdirectory/11.1/pingdirectoryproxy_server_administration_guide/pd_proxy_about_alt_authn_ids.html
llms_txt: https://docs.pingidentity.com/pingdirectory/llms.txt
docs_for_agents: https://developer.pingidentity.com/build-with-ai/docs-for-agents.md
revdate: September 13, 2023
section_ids:
  processing-steps: Processing steps
---

# About alternate authorization identities

Alternate authorization identities allow for the proper evaluation of access control rules for users whose entries aren't present within an entry-balanced dataset.

Whenever the PingDirectoryProxy server forwards a request to the backend set containing the user's entry, it forwards the request with an authorization identity that reflects the user's actual identity because the user is known to servers in that set. However, when forwarding a request to a backend set that doesn't contain the user's entry, the PingDirectoryProxy server uses an alternate authorization identity that reflects the generic user with the same set of rights as the actual user issuing the request.

Alternate authorization identities allow for the proper evaluation of access control rules for users whose entries are not present within an entry-balanced dataset.

There are only a few different generic classes of users from an access control perspective. These can be placed in a portion of the directory information tree (DIT) that isn't below the entry-balancing base distinguished name (DN) and is replicated to all servers in the topology.

Whenever a user authenticates to the PingDirectoryProxy server, the server can keep track of which backend set holds that user's entry and determine whether an alternate authorization identity is required. The server can determine which of these generic accounts best describes the rights that the user should have.

For the following example, assume that you have three classes of users: full administrators, password administrators, and normal users. Assume that you create the following entries in the topology and assign them the appropriate access rights:

* `uid=normal user,dc=example,dc=com`

* `uid=server-admin,dc=example,dc=com`

* `uid=password-admin,dc=example,dc=com`

![An illustrated workflow of an alternate authorization identity solving an access control issue in an entry-balancing deployment. The processing steps section below describes the workflow in detail. The client with uid=5000 is represented by a person at a desktop. The flow moves down from the client sending a bind request to the proxy server 01 which is represented by a box with the global index box sitting beside it. The the flow moves from the Proxy Server 01 in two directions: it sends a search request represented by an orange line to the entry balancing set 02 represented by a box with an orange outline and it sends a bind request represented by a green line to entry balancing set 01 represented by a box with a green outline. The entry balancing set 01 contains the base distinguished name, normal users, full administrators, and password administrator users, entries in the uid=0-10000 range, access control instructions, and an entry balancing point. The flow within is described in the processing steps. The entry balancing set 02 contains the base distinguished name, normal users, full administrators, and password administrator users, entries for uid=10001-20000, access control instructions, and an entry balancing point. The flow within is described in the processing steps.](_images/aqs1564012014720.png)Alternate Authorization Identity Solves Access Control Issues in Entry-Balancing Deployments

## Processing steps

1. The client with `uid=5000` binds to the PingDirectoryProxy server, which sends a `BIND` request to entry-balancing set-01.

2. The client sends a `SEARCH` request for `uid=15000`.

3. The PingDirectoryProxy server determines that `uid=15000` lives on entry-balancing set-02.

4. The PingDirectoryProxy server then determines that the client `uid=5000` doesn't have an entry on entry-balancing set-02.

5. The PingDirectoryProxy server uses an alternate authorization identity that reflects the generic user, `uid=normal user`, which has the same set of rights as the client `uid=5000` issuing the request.

6. The access control is accepted and the `SEARCH` request returns a response for `uid=5000`.

7. When an alternate authorization identity is invoked, `authzID='dn:uid=normal user,dc=example,dc=com` records in the server log, which indicates the use of the alternate authorization identity.

   For example, if the `user.15000` is in a different backend set from `user.5000`, the log shows the following response.

   ```
   % bin/ldapsearch -D "uid=user.5000,ou=people,dc=example,dc=com" -w pasword \
     -b uid=user15000,ou=people,dc=example,dc=com "(objectclass=)"

   [18/Aug/2013:11:54:35 -0500] SEARCH REQUEST conn=153 op=1 msgID=2
   via="app='Directory-Proxy address='127.0.0.1'
   authzID='dn:uid=normal user,dc=example,dcom' sessionID='conn=2'
   requestID='op=1'" base="uid=user.150000,ou=people,dc=example,dc=com"scope=2
   filter="(objectclass=)" attrs="ALL"

   [18/Aug/2013:11:54:35 -0500] SEARCH REQUEST conn=153 op=1 msgID=2 resultCode=0 etime=2.038
   entriesReturned=1 authzDN="uid=normal-user,dc=example,dc=com"
   ```
