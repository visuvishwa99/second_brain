TARGET DECK: SecondBrain::03_Streaming

START
Cloze
Kafka partitions allow {parallelism}; a topic's data is split across partitions.
<!--ID: 1770353416012-->
END

START
Cloze
Kafka {Offsets} are unique sequential ID numbers assigned to messages within a partition.
<!--ID: 1770353416014-->
END

START
Cloze
{ISR} (In-Sync Replicas) are replicas that are fully caught up with the leader.
<!--ID: 1770353416016-->
END

START
Cloze
Producer `acks={all}` ensures the highest durability by waiting for the leader and all ISRs to acknowledge.
<!--ID: 1770353416018-->
END

START
Cloze
Producer `acks={0}` (Fire & Forget) provides the lowest latency but highest risk of data loss.
<!--ID: 1770353416019-->
END

START
Cloze
A {Consumer Group} allows multiple consumers to read from a topic to scale processing; each partition is assigned to {ONE} consumer in the group.
<!--ID: 1770353416021-->
END

START
Cloze
{KRaft} (Kafka Raft) removes the dependency on {ZooKeeper} for metadata management (since 2.8+).
<!--ID: 1770353416023-->
END
