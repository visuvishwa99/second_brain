TARGET DECK: SecondBrain::03_Streaming

START
Cloze
Spark Structured Streaming uses {Micro-Batch} processing (latency ~100ms) treating the stream as an unbounded table.
<!--ID: 1770353415999-->
END

START
Cloze
{Watermarking} defines a threshold for dropping late data and clearing old state to prevent OOM. Rule: `Max Event Time - Watermark`.
<!--ID: 1770353416001-->
END

START
Cloze
{Stateless} transformations (select, filter) have no dependency on previous batches, while {Stateful} transformations (aggregations) require a State Store.
<!--ID: 1770353416002-->
END

START
Cloze
{Tumbling Windows} do not overlap (distinct time chunks), while {Sliding Windows} overlap.
<!--ID: 1770353416004-->
END

START
Cloze
Output Mode: {Append} writes only new rows (stateless), {Update} writes only changed rows, {Complete} rewrites the entire table.
<!--ID: 1770353416006-->
END

START
Cloze
The {foreachBatch} pattern is used to perform arbitrary logic like Upserts (Merge) to Delta tables or writing to multiple sinks.
<!--ID: 1770353416008-->
END

START
Cloze
Spark 3.4+ `applyInPandasWithState` allows arbitrary {stateful processing} in Python using Pandas UDFs.
<!--ID: 1770353416010-->
END
