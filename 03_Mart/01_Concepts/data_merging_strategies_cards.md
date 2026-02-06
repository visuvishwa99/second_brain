TARGET DECK: SecondBrain::01_Concepts

START
Cloze
{Upsert} (Update + Insert) checks if a record exists: if yes {update}, if no {insert}.
<!--ID: 1770353416037-->
END

START
Cloze
Upserts are commonly used for {Dimension} tables (SCD Type 1) but not for {Fact} tables which are usually append-only.
<!--ID: 1770353416038-->
END

START
Cloze
A {Soft Delete} flags a record as inactive (e.g., `is_active = false`) rather than removing it physically.
<!--ID: 1770353416040-->
END

START
Cloze
{Hard Deletes} physically remove rows. Standard `SELECT` ingestion cannot detect them; you need {CDC} or a full-load diff.
<!--ID: 1770353416042-->
END

START
Cloze
In SQL, you can handle hard deletes using: `DELETE FROM target WHERE id IN (SELECT id FROM {deleted_records_stream})`.
<!--ID: 1770353416044-->
END
