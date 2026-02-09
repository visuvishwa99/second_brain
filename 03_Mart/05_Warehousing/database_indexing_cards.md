TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
Adding an index to a database always increases {write} latency.
END

START
Cloze
A {composite} index can often replace multiple single-column indexes if designed correctly.
END

START
Cloze
A {covering} index allows the database to retrieve all requested data directly from the index structure, bypassing the table heap.
END

START
Cloze
{Partial} indexes are useful for queries that frequently filter on a specific constant value (e.g., `WHERE status = 'active'`).
END

START
Cloze
In Postgres, the system view {pg_stat_user_indexes} is used to identify unused or rarely used indexes.
END
