TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
In dbt incremental models, the {incremental_strategy} configuration determines how rows are added or updated, while {on_schema_change} determines how column changes are handled.
END

START
Cloze
The {merge} incremental strategy matches records based on a `unique_key`; it updates existing records and inserts new ones.
END

START
Cloze
The {append} incremental strategy simply inserts new rows without checking for duplicates, making it the fastest but least "safe" strategy.
END

START
Cloze
The {insert_overwrite} strategy replaces entire partitions of data, making it ideal for idempotent runs on partitioned fact tables.
END

START
Cloze
To automatically add new source columns to a destination table without dropping old ones, set `on_schema_change` to {append_new_columns}.
END

START
Cloze
The {sync_all_columns} option for `on_schema_change` will add new columns AND data-destructively drop columns from the destination that are no longer in the model.
END
