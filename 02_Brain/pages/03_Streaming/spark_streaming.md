---
tags:
  - streaming
---

# Spark Structured Streaming

- ## Core Concepts
    - Structured Streaming treats a live data stream as a table that is being continuously appended.
    - **Micro-Batch Processing**: Processes data in small batches (latency: 100ms-seconds).
    - **Unbounded Table**: Conceptually, new data is just "appended" to the table.
    - **Fault Tolerance**: Uses **Checkpointing** and Write-Ahead Logs (WAL) to ensure exactly-once semantics.

- ## State Management
    - ### Stateless Transformations
        - **Definition**: No result depends on previous batches.
        - **Examples**: `select`, `filter`, `withColumn`, `join` (with static DF).
        - **Pros**: Highly scalable, low latency, no state store management.
        - **Cons**: No cross-time context.
    - ### Stateful Transformations
        - **Definition**: Results depend on previous data (e.g., "Count events in last hour").
        - **Requirement**: Requires a **State Store** (HDFS or RocksDB).
        - **Examples**: `groupBy().count()`, `dropDuplicates()`, `stream-stream join`.
          ```python
          # Enable RocksDB for large state
          spark.conf.set("spark.sql.streaming.stateStore.providerClass",
          "org.apache.spark.sql.execution.streaming.state.RocksDBStateStoreProvider")
          ```

- ## Windowing & Time
    - **Windowing** buckets data by time.
    - ### Tumbling Window (Non-Overlapping)
        - Distinct time chunks (e.g., 00:00-00:15, 00:15-00:30).
        - ```python
          counts = df.groupBy(window(col("timestamp"), "15 minutes")).count()
          ```
    - ### Sliding Window (Overlapping)
        - Windows slide by a frequency (e.g., 15 min window, sliding every 5 mins).
        - ```python
          # (Column, Window Size, Slide Duration)
          counts = df.groupBy(window(col("timestamp"), "15 minutes", "5 minutes")).count()
          ```
    - ### Watermarking (Handling Late Data)
        - Defines a threshold for **dropping** late data and **clearing** old state.
        - Rule: `Max Event Time - Watermark`.
        - Without watermark, state grows indefinitely -> OOM.
        - ```python
          counts = df \
              .withWatermark("timestamp", "10 minutes") \
              .groupBy(window("timestamp", "10 minutes")).count()
          ```

- ## Output Modes
    - Differentiates how data is written to the sink.
    - | Mode | Description | Support | Use Case |
      |---|---|---|---|
      | **Append** | Only **new** rows are written. | Stateless, Watermarked Aggs. | Log ingestion, IoT raw data. |
      | **Update** | Only **changed** rows are written. | Aggregations. | Dashboard updates (only limit to rows that changed). |
      | **Complete**| **Entire** result table is rewritten. | Aggregations (Small output). | Small leaderboards, top-N. |

- ## Design Patterns
    - ### The `foreachBatch` Pattern (Upserts)
        - Standard sinks (Parquet/JSON) are append-only. To perform **Upserts** (Merge) or write to multiple destinations, use `foreachBatch`.
        - **Scenario**: Update a Delta table with streaming aggregates (Stateless Aggregation via Sink).
        - Instead of maintaining state in Spark (State Store), we carry the batch and `MERGE` it into the target table.
        - ```python
          def upsertToDelta(microBatchDF, batchId):
              microBatchDF.createOrReplaceTempView("updates")
              
              # Merge Logic
              microBatchDF._jdf.sparkSession().sql("""
                  MERGE INTO target_table t
                  USING updates s
                  ON t.id = s.id
                  WHEN MATCHED THEN UPDATE SET t.amount = t.amount + s.amount
                  WHEN NOT MATCHED THEN INSERT *
              """)

          # Streaming Query
          stream = raw_df.writeStream \
              .foreachBatch(upsertToDelta) \
              .outputMode("update") \
              .start()
          ```
    - ### Streaming Join (Enrichment)
        - **Stream-Static Join**: Stateless. Join stream with a cached static dimension table.
        - **Stream-Stream Join**: Stateful. Both sides are buffered. Watermark required on BOTH sides to clean state.

- ## Advanced & Modern Features (Spark 3.4+)
    - ### Arbitrary Stateful Processing (Python)
        - Before 3.4, complex stateful logic (like sessionization with custom rules) required Java/Scala (`mapGroupsWithState`).
        - Now, **`applyInPandasWithState`** brings this power to Python.
        - **Use Case**: Custom session logic (e.g., "End session if user visits 'logout.html' OR after 30 mins").
        - **Mechanism**: Maintain user-defined state per key using Pandas UDFs.
    - ### Session Windows (Dynamic)
        - Unlike fixed Tumbling/Sliding windows, **Session Windows** close after a period of inactivity (gap).
        - **Example**: "Group user clicks into a session; close session if no clicks for 30 mins."
        - ```python
          # Session window with 30 minute gap duration
          events.groupBy(session_window(col("timestamp"), "30 minutes")).count()
          ```
    - ### Protobuf Support
        - Native support for Protocol Buffers (common in gRPC/Streaming).
        - ```python
          # Read direct from binary column
          df.select(from_protobuf("binary_col", "Person", descFilePath).alias("person"))
          ```
    - ### Async Checkpointing (Project Lightspeed)
        - Improves performance by not blocking processing while the checkpoint is being written to effectively allow "Fire and Forget" for state snapshots.
    - ### Related
        - **Databricks Auto Loader**: Proprietary optimized source (`cloudFiles`) for file ingestion.
        - **Delta Live Tables (DLT)**: Declarative framework building pipelines on top of Spark Streaming.
