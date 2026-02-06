TARGET DECK: SecondBrain::08_Architecture

START
Cloze
Delta Lake provides {ACID} transactions (Atomicity, Consistency, Isolation, Durability) on top of data lake storage like S3.
<!--ID: 1770353415889-->
END

START
Cloze
The {transaction log} in Delta Lake is stored in the `_delta_log` directory as a sequence of {JSON} files.
<!--ID: 1770353415891-->
END

START
Cloze
Delta Lake {Time Travel} allows querying older versions of data using `VERSION AS OF` or `TIMESTAMP AS OF`.
<!--ID: 1770353415893-->
END

START
Cloze
{OPTIMIZE} command compacts small files (bin-packing), and `ZORDER BY` colocates related information to skip data during reads.
<!--ID: 1770353415894-->
END

START
Cloze
{VACUUM} removes old data files that are no longer referenced by the transaction log, freeing up storage but limiting {time travel} history.
<!--ID: 1770353415896-->
END

START
Cloze
Delta Lake supports {Schema Enforcement} (rejects writes with wrong schema) and Schema Evolution (allows adapting to new columns).
<!--ID: 1770353415898-->
END
