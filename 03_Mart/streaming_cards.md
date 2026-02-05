#flashcards/streaming

# Streaming Flashcards

What are the three Kafka acks settings?::acks=0 (Fire and Forget), acks=1 (Leader only), acks=all (All ISR replicas - highest durability).

What is a Watermark in Spark Streaming?::A threshold (Max Event Time - Watermark Duration) that defines how late data can arrive before being dropped. Prevents unbounded state growth.

What is the difference between Stateless and Stateful transformations?
?
Stateless has no memory of previous batches (filter, map). Stateful depends on previous data (groupBy, dropDuplicates) and requires a State Store.

What are the three Spark Streaming Output Modes?::Append (new rows only), Update (changed rows only), Complete (entire result table rewritten).

What is the difference between DStream and Structured Streaming?::DStream is RDD-based (legacy). Structured Streaming is DataFrame-based and uses Catalyst Optimizer + Tungsten.

What is the default Trigger interval in Spark Streaming?::0 (Runs micro-batches as soon as the previous one finishes).

List 3 common Output Sinks in Spark Streaming.::File (Parquet/JSON), Kafka, Console, Memory, Foreach.
