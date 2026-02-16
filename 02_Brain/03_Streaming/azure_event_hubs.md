---
created_at: 2026-02-12 11:45
tags:
  - streaming
status: sapling
---

# Azure Event Hubs vs. Kafka: The Data Engineer's Guide

A comparative analysis focusing on the trade-offs between self-managed Apache Kafka and Azure Event Hubs (Kafka API), specifically for interview scenarios.

## Core Value Proposition
**"Why use Event Hubs if we have Kafka?"**
*   **Operational Overhead**: Managing Kafka involves Zookeeper/KRaft, partition rebalancing, OS patching, and disk management. Event Hubs is a PaaS (Platform as a Service) that abstracts this away.
*   **Protocol Compatibility**: Event Hubs provides a Kafka endpoint (port 9093), allowing existing Kafka producers/consumers (Spark, simple clients) to connect without code changes.
*   **IAM Integration**: Native integration with Azure Active Directory (Entra ID) simplifies security vs. managing support ACLs or Kerberos in Kafka.

## Key Challenges & Differences

| Feature | Apache Kafka (Self-Hosted) | Azure Event Hubs |
| :--- | :--- | :--- |
| **Consumer Groups** | Unlimited | **Limited** (20 in Standard Tier). Requires upgrading to Premium for more. |
| **Log Compaction** | Supported (Keep latest value per key). | **Not Supported**. Critical for CDC/Table reconstruction patterns. |
| **Partitions** | Can scale up (add partitions) anytime. | **Fixed at creation** (mostly). Changing requires recreating the hub or using premium features. |
| **Throttling** | Limited by hardware (CPU/Disk/Net). | Throttled by **Throughput Units (TUs)**. 1 TU = 1MB/s In, 2MB/s Out. Can auto-inflate. |
| **Retention** | Configurable (Time or Size driven). | Tier-dependent (e.g., 7 days max on Standard, up to 90 days on Premium). |

## Integration "Gotchas" (Interview Gold)
1.  **Authentication**: Kafka clients use SASL/PLAIN or SASL/SSL. Mapping Azure's "Connection String" to Kafka's JAAS config is tricky.
    *   *Username*: `$ConnectionString`
    *   *Password*: The actual connection string.
2.  **Timestamps**: Spark Structured Streaming watermarking logic may behave effectively differently due to how Event Hubs handles "Enqueue Time" vs Kafka's "Append Time"/"Create Time".
3.  **Partition Count**: Under-provisioning partitions at creation is a common mistake. Since they can't be easily resized in Standard tier, you may end up with a bottlenecked partition key strategy that requires a full migration to fix.
