---
created_at: "2026-02-05 09:40"
status: seed
processed: true
Explain: false
tags: streaming
examples: 1
Realtime: false
diagram: false
card_creation: true
card_type: "basic"
card_diagram: false
---

# Spark Streaming Concepts

A DStream is a continuous sequence of RDDs. 
However, Structured Streaming is better because it uses the Catalyst Optimizer and Tungsten Engine.

The default Trigger interval is 0 (processing as fast as possible).
We can set a Fixed Interval Trigger like `ProcessingTime("10 seconds")`.

Output sinks include:
- File (Parquet, JSON)
- Kafka
- Foreach (Arbitrary logic)
- Console (Debugging)
- Memory (Debugging)
