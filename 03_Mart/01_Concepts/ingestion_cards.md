TARGET DECK: SecondBrain::01_Concepts



START

Cloze

{Incremental Ingestion} moves only new or modified data to reduce latency and cost, compared to a {Full Load}.
<!--ID: 1770353416046-->

END



START

Cloze

{High Watermark} strategy uses a column like `updated_at` to identify new records: `SELECT * FROM source WHERE updated_at > {last_high_watermark}`.
<!--ID: 1770353416047-->

END



START

Cloze

A major limitation of High Watermark strategy is that it cannot track {Hard Deletes} (rows physically removed).
<!--ID: 1770353416049-->

END



START

Cloze

{Change Data Capture (CDC)} reads database transaction logs to capture INSERT, UPDATE, and {DELETE} events.
<!--ID: 1770353416051-->

END



START

Cloze

CDC is ideal for databases requiring {exact synchronization} including deletes, but has higher setup complexity.
<!--ID: 1770353416052-->

END