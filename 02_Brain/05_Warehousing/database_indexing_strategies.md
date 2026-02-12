---
created_at: 2026-02-08 00:21
tags:
  - warehousing
---

# Database Indexing Strategies: Beyond the Basics

Your database has 50 indexes.
And it's SLOWER than having 5.

Here's what most engineers get wrong about indexing:

We treat indexes like free performance boosts.
But every index you add is a hidden contract:

- Every INSERT now updates N+1 data structures
- Every UPDATE potentially rewrites multiple B-trees
- The query planner gets confused with too many choices
- Your working set no longer fits in memory

I learned this the hard way at scale.

We had a table with 34 indexes.
Reads were fast. Writes were dying.
P99 latency on inserts hit 1.2 seconds.

The fix? We dropped 28 indexes.

But here's the part nobody talks about:

We replaced them with 3 composite indexes that covered 94% of our query patterns.

The trick was analyzing `pg_stat_user_indexes`.
Most of our indexes had ZERO scans in 30 days.
They were dead weight burning I/O on every write.

## Framework for Index Optimization

1. **Audit index usage monthly**: Use `pg_stat_user_indexes` (PostgreSQL) or equivalent.
2. **Justify write amplification**: Every index must earn its keep.
3. **Composite > Single**: Composite indexes are almost always better than single-column indexes.
4. **Covering Indexes**: Aim to eliminate heap lookups entirely.
5. **Partial Indexes**: Use for queries that filter on a constant (e.g., `WHERE status = 'active'`).

## Results After Cleanup

- Write latency dropped 73%
- Storage shrank by 40%
- Read performance stayed identical

The best performance optimization isn't adding something new.
It's removing what shouldn't be there.
