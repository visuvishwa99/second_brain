---
tags:
 
---

deck:: [[kafka]]

- What is Apache Kafka? :-> {{ A distributed streaming platform that allows publishing and subscribing to streams of records, storing streams of records, and processing streams of records }} ^680bcf9a-f412-47e0-8e9e-119d1bdb4b1f
- Key and value in Kafka are serialized as what? :-> {{ ByteArray }} ^680bcf9a-7b33-4204-a44c-f9b2ee34366f
- Important parts of a Kafka packet :-> {{ key, value, timestamp }} ^680bcf9a-092b-4f02-8caf-234710a03fa2
- What is an offset in Kafka? :-> {{ In partitions, messages are assigned a unique ID number }} ^680bcf9a-8179-4a6a-ba78-74e96ac134d4
- What is Zookeeper's role in Kafka? :-> {{ It is a high performance and open source complete coordination service used for distributed applications adapted by Kafka. It lets Kafka manage sources properly }} ^680bcf9a-cb5e-4b58-add1-b868aa30b921
- What is a replica in the Kafka environment? :-> {{ The replica is a list of essential nodes needed for logging for any particular partition. It can play the role of a follower or leader }} ^680bcf9a-ef1d-48ee-ba25-5602fe692c2e
- What is a consumer group in Kafka? :-> {{ When more than one consumer consumes a bunch of subscribed topics jointly, it forms a consumer group }} ^680bcf9a-1b10-4176-a88d-e4c2863263c7
- Why are replications important in Kafka? :-> {{ Duplication assures that issued messages are not lost }} ^680bcf9a-9dd7-4651-9018-0ffcebecc027
- What are the three key broker configuration files in Kafka? :-> {{ broker.id, log.dirs, zookeeper.connect }} ^680bcf9a-0584-48d1-a150-8bc59190f92c
- What is the maximum message size the Kafka server can receive by default? :-> {{ 1,000,000 bytes (1 MB) }} ^680bcf9a-d1ae-4816-91f6-d3e38b07b2a7
- What are the components of Confluent Platform 3.x? :-> {{ Kafka Connect, Kafka Streams, SchemaRegistry, RESTProxy, ControlCenter }} ^680bcf9a-acd2-40ca-9f85-6eaf7ed94e06
- What is Kafka MirrorMaker used for? :-> {{ Provides Geo-replication support for clusters, replicating messages across multiple cloud regions or datacenters }} ^680bcf9a-6205-4e04-8792-34330a33542b
- What is a partition in Kafka? :-> {{ A single piece of Kafka topic that allows excellent parallelism when reading from topics }} ^680bcf9a-bc1d-4874-801b-acd839f3cbaa
- What does ISR stand for in Kafka? :-> {{ In-Sync Replicas, which are a set of message replicas that are synced to be leaders }} ^680bcf9a-3b96-4813-93f1-0462240929ee
- How can you start a Kafka Server? :-> {{ First start Zookeeper with bin/zookeeper-server-start.sh config/zookeeper.properties, then start Kafka with bin/kafka-server-start.sh config/server.properties }} ^680bcf9a-51df-4ad2-a3eb-c8f6532c96b7
- What is SerDes in Kafka? :-> {{ Serializer and Deserializer that materializes the data whenever necessary for any Kafka stream }} ^680bcf9a-289a-4d99-bda9-8557b7780cd2
- What is multi-tenancy in Kafka? :-> {{ Ability to share a single Kafka cluster across multiple isolated tenants or applications with logical separation and access control }} ^680bcf9a-44a0-4fa6-a19c-93dc898f0a83
- What are the three available ack settings in Kafka? :-> {{ acks=0 (Fire and Forget), acks=1 (Leader Acknowledgement), acks=all (Full Acknowledgement) }} ^680bcf9a-b81e-4531-8714-4ac0be013d38
- When does acks=0 setting get used? :-> {{ When highest throughput is needed but data loss is acceptable, as producer doesn't wait for any acknowledgment }} ^680bcf9a-c993-4387-a7cf-f911c4077490
- When does acks=1 setting get used? :-> {{ When balance between throughput and durability is needed, as producer waits only for leader acknowledgment }} ^680bcf9a-fbca-48ce-a4ab-88ef2818f27a
- When does acks=all setting get used? :-> {{ When data durability is critical, as producer waits for all in-sync replicas to acknowledge the message }} ^680bcf9a-348f-4fb4-8e9f-08f6ca5b7623
- What is the main difference between RabbitMQ and Kafka? :-> {{ RabbitMQ follows a "smart broker, dumb consumer" model while Kafka follows a "dumb broker, smart consumer" model }} ^680bcf9a-6586-49af-8dc1-c85ab500acf9
- What is KRaft mode in Kafka? :-> {{ Kafka Raft mode allows Kafka to run without ZooKeeper, introduced in version 2.8.0 and fully supported in 3.5.0 }} ^680bcf9a-350c-4f89-b5b9-fc573a24f0d4
- How is partitioning key used in Kafka? :-> {{ It indicates the destination partition of the message, using a hashing function to map the key to a specific partition number }} ^680bcf9a-010a-4e01-9d4e-41d769297b61
- What causes QueueFullException in Kafka? :-> {{ Occurs when the producer attempts to send messages at a pace not handleable by the broker }} ^680bcf9a-6633-41d3-81bd-ebf706902ef4
- What is Kafka's protocol for communication? :-> {{ Kafka leverages the TCP protocol for communication between brokers and clients }} ^680bcf9a-b496-4de4-98fc-ee056e0ea652
- How can a remote consumer's throughput be improved in Kafka? :-> {{ By tuning the socket buffer size to amortize the long network latency }} ^680bcf9a-4703-4fac-baee-80926b7d01f2
- What indicates if a replica stays out of ISR for a long time? :-> {{ It indicates the follower cannot fetch data as fast as data is accumulated at the leader }} ^680bcf9a-7837-48ee-9759-d9e75606f75a
- What happens if the preferred replica is not in the ISR? :-> {{ The controller will fail to move leadership to the preferred replica }} ^680bcf9a-4b21-49ec-b705-7602633c0f67
- What is Synchronous Producer (SyncProducer) in Kafka? :-> {{ A producer whose send() method blocks until it receives acknowledgment from Kafka brokers based on the acks configuration }} ^680bcf9a-f9ec-492b-9843-3caff3cb2762
- What is Asynchronous Producer (AsyncProducer) in Kafka? :-> {{ A producer whose send() method returns a Future and does not block, adding messages to a buffer to be sent in batches }} ^680bcf9a-e7b5-4ae5-9ae7-7a33e38e40e1
- How is a compacted topic configured in Kafka? :-> {{ Using bin/kafka-topics.sh with --config cleanup.policy=compact parameter }} ^680bcf9a-cd08-4d3e-b990-f9dd4ca0b8da
- For which use cases is Kafka NOT a good fit? :-> {{ Low throughput requirements, strict ordering requirements across partitions, short-lived data streams, simple point-to-point communication }} ^680bcf9a-63cd-41ac-b2c1-5f19decd36e2
- How do you rebalance a Kafka cluster? :-> {{ By identifying imbalance, generating a reassignment plan with kafka-reassign-partitions tool, reviewing and modifying the plan, executing reassignment, and verifying progress }} ^680bcf9a-b26b-41cc-903a-7357d5c7ac8c


### Related
- [[Streaming]]
- [[Ingestion]]
