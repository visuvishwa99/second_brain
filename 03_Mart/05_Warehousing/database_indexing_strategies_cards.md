TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
Every extra index on a table causes {write amplification} because every INSERT must update N+1 data structures.
END

START
Cloze
Too many indexes can cause the {query planner} to get confused with too many choices.
END

START
Cloze
To identify unused indexes in PostgreSQL, you should analyze the {pg_stat_user_indexes} view.
END

START
Cloze
{Composite} indexes are generally preferred over multiple single-column indexes because they can satisfy queries filtering on multiple columns more efficiently.
END

START
Cloze
A {covering} index contains all the columns required by a query, thereby eliminating the need for heap lookups.
END

START
Cloze
{Partial} indexes are useful for queries that frequently filter on a constant value (e.g., `WHERE status = 'active'`).
END
