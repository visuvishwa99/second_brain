TARGET DECK: SecondBrain::02_Compute

START
Cloze
Spark Stage boundaries are determined by {Shuffle} operations (e.g., repartition, groupByKey).
<!--ID: 1770353416024-->
END

START
Cloze
{Narrow} transformations (map, filter) do not require data movement across partitions, while {Wide} transformations (reduceByKey) require a shuffle.
<!--ID: 1770353416026-->
END

START
Cloze
`reduceByKey` performs a {Map-side combine} (efficient) while `groupByKey` does not (expensive, risk of OOM).
<!--ID: 1770353416028-->
END

START
Cloze
{coalesce} reduces partitions without shuffling, while {repartition} performs a full shuffle to increase/decrease partitions.
<!--ID: 1770353416030-->
END

START
Cloze
A {Broadcast Join} optimizes joining a large DF with a small DF by sending the small DF to all nodes, avoiding a shuffle.
<!--ID: 1770353416032-->
END

START
Cloze
{Actions} (e.g., collect, count) trigger the execution of the DAG, while {Transformations} (e.g., map, filter) are lazy.
<!--ID: 1770353416033-->
END

START
Cloze
Spark 3.4+ introduced {Spark Connect}, a decoupled client-server architecture allowing lightweight local clients.
<!--ID: 1770353416035-->
END
