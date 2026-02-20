TARGET DECK: SecondBrain::03_Streaming



START

Cloze

Azure Event Hubs exposes a Kafka-compatible endpoint on port {9093}.
<!--ID: 1771611852939-->
END



START

Cloze

When configuring a Kafka client to connect to Azure Event Hubs via SASL, the username must be set to `{$ConnectionString}` and the password is the {connection string value}.
<!--ID: 1771611852940-->
END



START

Cloze

Unlike Kafka, Azure Event Hubs does **not** support {log compaction}, which is critical for CDC (Change Data Capture) table reconstruction.
<!--ID: 1771611852943-->
END



START

Cloze

In Azure Event Hubs (Standard Tier), the number of partitions is {fixed/immutable} at creation, whereas in Kafka, you can {add partitions} to an existing topic.
<!--ID: 1771611852944-->
END



START

Cloze

Azure Event Hubs throughput is throttled by {Throughput Units (TUs)}, where 1 TU equals {1 MB/s} ingress and {2 MB/s} egress.
<!--ID: 1771611852946-->
END