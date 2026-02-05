---
tags:
  - concepts
---

# Data Merging Strategies

## 1. Upserts (Update + Insert)
**Definition**: The operation of checking if a record exists. If it does, **update** it; if it doesn't, **insert** it. Essential for maintaining the "Current State" of a dataset.

### Execution
- **When is it used?** When ingesting Dimension tables (SCD Type 1) or current-state snapshots where duplicates are not allowed.
- **When is it NOT used?**
	- **Fact Tables**: Usually Append-Only (e.g., website clicks).
	- **Audit Logs**: You want to see the history of changes, experienced as separate rows (SCD Type 2).

### Examples
**1. SQL (Merge)**
```sql
MERGE INTO target t USING source s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET t.amount = s.amount
WHEN NOT MATCHED THEN INSERT (id, amount) VALUES (s.id, s.amount);
```

**2. Spark (Delta Lake)**
```python
deltaTable.alias("t").merge(
 sourceDF.alias("s"),
 "t.id = s.id"
).whenMatchedUpdate(
 set = { "amount": "s.amount" }
).whenNotMatchedInsert(
 values = { "id": "s.id", "amount": "s.amount" }
).execute()
```

## 2. Handling Deletes (Hard vs Soft)
**Definition**: Managing records that have been removed from the source system.

### A. Soft Deletes
The record remains in the database but is flagged as inactive.
- **Identification**: Source system has an `is_active = false` or `deleted_at IS NOT NULL` column.
- **Handling**: Ingest normally. Filter out `WHERE is_active = true` downstream.

### B. Hard Deletes
The record is physically removed from the source table.
- **Identification**:
	- **Standard Ingestion**: IMPOSSIBLE to detect with simple `SELECT *`. The row is just gone.
	- **Diff/Full Load**: Compare Source IDs vs Target IDs. (Expensive).
	- **CDC**: The transaction log explicitly contains a `DELETE` operation type.
- **Handling**:
	- **SQL**: `DELETE FROM target WHERE id IN (SELECT id FROM deleted_records_stream)`
	- **Spark (Delta)**:
```python
deltaTable.alias("t").merge(
 cdc_stream.alias("s"), "t.id = s.id"
).whenMatchedDelete(
 condition = "s.op_type = 'DELETE'"
).execute()
```

### Related
- [[ingestion]]
- [[scd]]
- [[change_data_capture]]
