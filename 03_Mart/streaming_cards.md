TARGET DECK: streaming

# Streaming Flashcards

START
Basic
What are the three Kafka acks settings?
Back: acks=0 (Fire and Forget), acks=1 (Leader only), acks=all (All ISR replicas - highest durability).
Tags: streaming kafka
END

START
Basic
What is a Watermark in Spark Streaming?
Back: A threshold (Max Event Time - Watermark Duration) that defines how late data can arrive before being dropped. Prevents unbounded state growth.
Tags: streaming spark
END

START
Basic
What is the difference between Stateless and Stateful transformations?
Back: Stateless has no memory of previous batches (filter, map). Stateful depends on previous data (groupBy, dropDuplicates) and requires a State Store.
Tags: streaming spark
END

START
Basic
What are the three Spark Streaming Output Modes?
Back: Append (new rows only), Update (changed rows only), Complete (entire result table rewritten).
Tags: streaming spark
END
