---
created_at: 2026-02-09
tags: 
  - warehousing
---

# Database Indexing Strategy

Indexing is a trade-off, not a free performance boost. While indexes speed up reads, they introduce "write amplification" because every `INSERT` or `UPDATE` must also update the index structures.

## The Hidden Cost of Indexes
- **Write Latency**: Every `INSERT` updates `N+1` data structures (Heap + N Indexes).
- **Storage Bloat**: Indexes consume significant disk and memory.
- **Planner Confusion**: Too many indexes can confuse the query optimizer.

> **Rule of Thumb**: Verify if an index justifies its write cost.

## Optimization Framework
The goal is to have the minimum number of indexes that cover the maximum number of query patterns.

1.  **Audit Regularly**: Use `pg_stat_user_indexes` (in Postgres) to find unused indexes.
2.  **Delete Unused Indexes**: If an index has zero scans in 30 days, it is dead weight.
3.  **Prefer Composite Indexes**: A single composite index on `(A, B)` can often replace separate indexes on `A` and `B` (depending on query patterns).
4.  **Use Covering Indexes**: Indexes that include all columns required by a query (via `INCLUDE` clause or composite keys) allow **Index Only Scans**, bypassing the heap entirely.
5.  **Partial Indexes**: Index only a subset of rows (e.g., `WHERE status = 'active'`) to save space and improve performance for specific queries.

## Example Scenario
**Problem**: A table with 34 indexes had fast reads but P99 insert latency of 1.2s.
**Solution**:
- Analyzed usage via `pg_stat_user_indexes`.
- Removed 28 unused/redundant indexes.
- Created 3 composite indexes covering 94% of queries.
**Result**:
- Write latency dropped 73%.
- Storage reduced by 40%.
- Read performance remained identical.

## Code Example (Postgres)
```sql
-- Check for unused indexes
SELECT
    schemaname,
    relname,
    indexrelname,
    idx_scan,
    idx_tup_read,
    idx_tup_fetch
FROM pg_stat_user_indexes
ORDER BY idx_scan ASC;
```
