#flashcards/warehousing

# Warehousing Flashcards

What is SCD Type 2?::Row versioning. A new row is inserted for every change, and old rows are marked as expired.

What is SCD Type 1?::Overwrite. The old value is replaced by the new value. No history is preserved.

What are Late Arriving Dimensions (LAD)?
?
When Fact data arrives before Dimension data. Solution: Insert placeholder row, then backfill when real data arrives.
