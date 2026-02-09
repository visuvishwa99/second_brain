---
created_at: 2026-02-09
tags: 
  - warehousing
---

# Databricks Shallow Clones

A **Shallow Clone** in Databricks (Delta Lake) creates a copy of a table that shares the same underlying data files as the original table but maintains its own separate transaction log (metadata).

## Use Case: Instant Test Environments
Copying large production tables (e.g., 1TB+) to a development environment is slow and expensive. Shallow clones solve this by copying only the metadata.

## Benefits
1.  **Speed**: Clones Petabyte-scale tables in seconds.
2.  **Cost**: Zero additional storage cost initially (pointers to existing data). Storage costs only incur when changes (deltas) are made to the clone.
3.  **Safety**: Modifications to the clone (DELETE, MERGE, UPDATE) write new files for the clone only, leaving the original table untouched.

## Syntax
```sql
CREATE TABLE dev.sales_test
SHALLOW CLONE prod.sales_gold;
```

## Comparisons
| Feature | Deep Clone | Shallow Clone |
| :--- | :--- | :--- |
| **Data Copy** | Copies all data files | Copies only metadata (pointers) |
| **Speed** | Slow (depends on data size) | Instant |
| **Independence** | Completely independent | Dependent on source files (unless source retention helps) |
| **Use Case** | Archival, Migration, DR | Testing, Debugging, Blue/Green Deploy |

> **Note**: If the source table vacuums/deletes old files that the shallow clone relies on, the clone may break. Ensure proper retention policies.
