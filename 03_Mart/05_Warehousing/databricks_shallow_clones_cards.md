TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
A {Shallow Clone} in Databricks copies only the table metadata/transaction log, appearing as a full copy without duplicating data files.
END

START
Cloze
Shallow Clones incur {zero (or near-zero)} storage costs initially because they point to existing data files.
END

START
Cloze
The SQL command to create a pointer-based copy of a Delta table is `CREATE TABLE target {SHALLOW CLONE} source;`
END
