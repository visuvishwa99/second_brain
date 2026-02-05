#flashcards/streaming

# Streaming Flashcards

What are the three Kafka acks settings?::acks=0 (Fire and Forget), acks=1 (Leader only), acks=all (All ISR replicas).

What is a Watermark in Spark Streaming?::A threshold that defines how late data can arrive before being dropped.

What is the difference between Stateless and Stateful transformations?
?
Stateless has no memory of previous batches (filter, map). Stateful depends on previous data (groupBy, dropDuplicates) and requires a State Store.

What are the three Spark Streaming Output Modes?::Append (new rows only), Update (changed rows only), Complete (entire result table rewritten).
