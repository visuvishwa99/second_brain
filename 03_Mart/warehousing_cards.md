TARGET DECK: warehousing

# Warehousing Flashcards

START
Basic
What is SCD Type 2 ?
Back: Row versioning. A new row is inserted for every change, and old rows are marked as expired using `is_current = false` and `end_date`.
Tags: warehousing scd
END

START
Basic
What is SCD Type 1 ?
Back: Overwrite. The old value is replaced by the new value. No history is preserved.
Tags: warehousing scd
END

START
Basic
What are Late Arriving Dimensions (LAD) ?
Back: When Fact data arrives before Dimension data. Solution: Insert placeholder row, then backfill when real data arrives.
Tags: warehousing scd
END
