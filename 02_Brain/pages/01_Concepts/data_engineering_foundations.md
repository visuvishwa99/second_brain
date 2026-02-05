---
tags:
  - concepts
---

# Data Engineering Foundations

- ## Data Engineering Workflow
    - **Data Ingestion**: Collecting from various sources.
    - **Data Processing**: Transforming raw data to usable form.
    - **Data Storage**: Maintaining persistent data repositories.
    - **Data Serving**: Making data available to consumers.

- ## Foundation Principles
    - Data as a Product vs. Data as a Service.
    - End-to-end data lifecycle management.
    - Balance of performance, cost, and reliability.

- ## Success Metrics
    - Processing time improvements.
    - Data freshness guarantees.
    - Query performance benchmarks.
    - Cost efficiency measurements.

- ## Batch vs Stream Processing
    - | Aspect | Batch | Stream |
      |---|---|---|
      | **Latency** | High (minutes-hours) | Low (ms-seconds) |
      | **Throughput** | Higher | Lower |
      | **Complexity** | Simpler | Higher (State, Ordering) |
      | **Use Case** | ETL, Reports | Real-time dashboards, Fraud |

- ## Processing Semantics
    - **At-least-once**: Message may be reprocessed (duplicates possible).
    - **At-most-once**: Message may be lost.
    - **Exactly-once**: Guaranteed single delivery (hardest to achieve).

- ## Data Modeling Approaches
    - **Star Schema**: Denormalized, fast queries.
    - **Snowflake Schema**: Normalized dimensions.
    - **Data Vault**: Scalable, audit-friendly.
    - **Kimball vs Inmon**: Bottom-up (marts first) vs Top-down (EDW first).

- ## Data Quality Dimensions
    - Completeness, Accuracy, Consistency, Timeliness, Validity.

- ### Related
    - [[batch_processing]]
    - [[streaming]]
    - [[data_merging_strategies]]
