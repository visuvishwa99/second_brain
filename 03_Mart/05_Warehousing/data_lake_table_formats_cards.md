TARGET DECK: SecondBrain::05_Warehousing

START
Cloze
{Delta Lake} uses an Optimistic Concurrency Control mechanism and stores transaction logs in the `_delta_log` folder.
END

START
Cloze
{Apache Iceberg} supports **Hidden Partitioning**, allowing users to query by timestamp without knowing the physical directory structure.
END

START
Cloze
In Apache Hudi, {Copy-on-Write (COW)} table type rewrites the entire file on update, favoring **read** performance over write speed.
END

START
Cloze
In Apache Hudi, {Merge-on-Read (MOR)} stores updates in row-based **delta logs** and merges them with base files at query time.
END

START
Cloze
Hudi's {Bloom Index} is the default indexing strategy, using bloom filters to identify files that might contain a specific record key.
END

START
Cloze
Hudi {Incremental Queries} allow you to pull only the data that has changed since a specific commit time, enabling efficient streaming pipelines.
END
