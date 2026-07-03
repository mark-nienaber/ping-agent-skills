---
title: Glossary
description: A report that identifies potential anomalous assignments.
component: identity-governance
version: 7.1.2
page_id: identity-governance::glossary
canonical_url: https://docs.pingidentity.com/identity-governance/7.1.2/glossary.html
---

# Glossary

* anomaly report

  A report that identifies potential anomalous assignments.

* as-is predictions

  A process where confidence scores are assigned to the entitlements that users have.

* auto-certify

  An action that an entitlement owner can do to approve a justification. Auto-certify indicates that anyone who has the justification is automatically approved for the entitlement.

* auto-request

  An action that an entitlement owner can do to approve a justification. Auto-request indicates that anyone who matches these justification attributes but may not already have access should automatically get provisioned for this entitlement.

* confidence score

  A score from a scale from 0 to 100% that indicates the strength of correlation between an assigned entitlement and a user's data profile.

* data audit

  A pre-analytics process that audits the seven data files to ensure data validity with the client.

* data ingestion

  A pre-analytics process that pushes the seven .csv files into the Cassandra database. This allows the entire training process to be performed from the database.

* data sparsity

  A reference to data that has null values. Identity Governance requires dense, high quality data with very few null values in the user attributes to get accurate analysis scores.

* data validation

  A pre-analytics process that tests the data to ensure that the content is correct and complete prior to the training process.

* driving factor

  An association rule that is a key factor in a high entitlement confidence score. Any rule that exceeds a confidence threshold level (e.g., 75%) is considered a driving factor.

* entitlement

  An entitlement is a specialized type of `assignment`. A user or device with an entitlement gets access rights to specified resources.

* insight report

  A report that provides metrics on the rules and predictions generated in the analytics run.

* recommendation

  A process run after the as-is predictions that assigns confidence scores to all entitlements and recommends entitlements that users do not currently have. If the confidence score meets a threshold, set by the `conf_thresh` property in the configuration file, the entitlement will be recommended to the user in the UI console.

* resource

  An external system, database, directory server, or other source of identity data to be managed and audited by an identity management system.

* REST

  Representational State Transfer. A software architecture style for exposing resources, using the technologies and protocols of the World Wide Web. REST describes how distributed data objects, or resources, can be defined and addressed.

* stemming

  A process that occurs after training that removes similar association rules that exist in a parent-child relationship. If the child meets three criteria, then it will be removed by the system. The criteria are: 1) the child must match the parent; 2) the child (e.g., \[San Jose, Finance]) is a superset of the parent rule. (e.g., \[Finance]); 3) the child and parent's confidence scores are within a +/- range of each other. The range is set in the configuration file.

* training

  A multi-step process that generates the association rules with confidence scores for each entitlement. First, Identity Governance models the frequent itemsets that appear in the user attributes for each user. Next, Identity Governance merges the user attributes with the entitlements that were assigned to the user. It then applies association rules to model the sets of user attributes that result in an entitlement access and calculates confidence scores, based on their frequency of appearances in the dataset.
