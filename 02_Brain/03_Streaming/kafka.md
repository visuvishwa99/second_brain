---
tags:
  - streaming
---

# Apache Kafka

- ## Kafka Components (Confluent Platform)
    - **Kafka Connect**: Framework for building connectors to stream data between Kafka and external systems (DBs, S3).
    - **Kafka Streams**: Library for building real-time stream processing applications.
    - **Schema Registry**: Central repository for Avro/Protobuf schemas, ensuring data compatibility.
    - **REST Proxy**: Interface for interacting with Kafka via HTTP.
    - **Control Center**: Web-based monitoring and management.
    - **MirrorMaker (MM2)**: Geo-replication for DR (Active/Passive).

- ## Core Architecture
    - **Partitions**: A single piece of a topic. Allows parallelism. 
        - Formula: `partition = murmur2(key) % number_of_partitions`
        - Key partitioning ensures ordering per key.
    - **Offsets**: Unique ID number assigned to messages within a partition.
    - **ISR (In-Sync Replicas)**: Replicas that are fully caught up with the leader.
        - If a replica lags too long, it is dropped from ISR.
        - `replica.lag.time.max.ms` controls tolerance.
    - **Zookeeper vs KRaft**:
        - **ZooKeeper**: External coordination service (Legacy).
        - **KRaft**: Internal Raft consensus (Modern, Zookeeper-less since 2.8+).

- ## Producers
    - **Modes**:
        - **SyncProducer**: Blocks until ack. Strong durability, lower throughput.
        - **AsyncProducer**: Sends in batches (background). High throughput, risk of data loss.
    - **Acks Configuration**:
        - `acks=0` (Fire & Forget): No wait. Lowest latency, High risk.
        - `acks=1` (Leader): Wait for Leader. Balanced.
        - `acks=all`: Wait for ISR. Highest durability.
    - **Code Example (Python)**:
      ```python
      producer = KafkaProducer(
          bootstrap_servers=['broker1:9092'],
          acks='all',
          retries=3
      )
      producer.send('topic', key=b'key', value=b'msg')
      ```

- ## Consumers
    - **Consumer Group**: Multiple consumers reading from a topic to scale processing. Each partition is assigned to ONE consumer in the group.
    - **Offset Management**: Consumers track their own progress (Smart Consumer / Dumb Broker model).
    - **Remote Consumer Tuning**:
        - If high latency (files across DCs): Increase `socket.receive.buffer.bytes`.

- ## Kafka vs RabbitMQ
    - **Messaging Model**:
        - **Kafka**: Pull-based, Distributed Log, Replayable.
        - **RabbitMQ**: Push-based, Traditional Queue, Ephemeral.
    - **Throughput**: Kafka >> RabbitMQ.
    - **Ordering**: Kafka guarantees order *per partition*. RabbitMQ has stronger queue guarantees.
    - **Scale**: Kafka is horizontal. RabbitMQ is vertical (mostly).

- ## Operations & Tuning
    - **Rebalancing**: Redistributing partitions.
        - Tool: `kafka-reassign-partitions`.
    - **Performance Tuning**:
        - **Partitions**: Increase for throughput. `Throughput / Single Partition Speed`.
        - **Batch Size**: Increase `batch.size` and `linger.ms` (e.g., 20ms) for better compression/throughput.
        - **Compression**: Snappy/LZ4/Zstd.
    - **Multi-Tenancy**:
        - Isolation via Namespaces (Topic prefixes).
        - Quotas on Produce/Consume rates.
        - ACLs for security.

- ## When NOT to use Kafka
    - Low throughput (Simple queue is better).
    - Strict global ordering (across all partitions).
    - Small payloads only (overhead > value).
    - Short-lived transient data (no need for persistence).
