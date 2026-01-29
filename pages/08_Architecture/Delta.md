- Delta
  Tables are a storage format and table abstraction layer that sits on top of
  your existing data lake storage (like S3 on AWS).
- **Key Features:**
  collapsed:: true
	- **ACID Transactions: ** ((Atomicity,
	  collapsed:: true
	  Consistency, Isolation, Durability))
		- **Atomicity**
		  Delta Lake guarantees that all operations in a transaction either fully complete or fully fail1.
		- For example, when appending data to a table, if a failure occurs mid-operation, the table remains unaltered, ensuring data integrity2.
		- **Consistency**
		  Delta Lake maintains consistency through Schema enforcement. New data must match the existing table schema1.
		  Column constraints: Users can specify requirements for data added to a table1.
		  Strong schema checking: Prevents writing data that doesn't conform to the table schema2.
		- **Isolation**
		  Delta Lake uses serializable isolation, the highest level possible. Transactions are applied sequentially and persisted in monotonically increasing transaction files. This allows users to see consistent views of data even during real-time writes.
		- **Durability**
		  Committed changes in Delta Lake are permanent3. Writes to cloud object storage use transactional commits, creating metadata files that ensure durability
	-
	- **Delta Lake Internal Architecture**
		- create a delta table
			- create table (col1 , col2 ) using delta
			- deltatable.createOrreplace(spark)
			- df.write.format(delta).saveastable(table_name)
		- Time travel (JSON, Parquet, and CRC files)
			- ![image.png](../assets/image_1738861871698_0.png)
				- JSON Files
				  (log associated to file)
				-
				- The JSON
				  files in the **_delta_log directory** serve as the transaction log for the Delta
				  table. They record all the operations (inserts, updates, deletes) performed on
				  the table in an ordered and atomic manner. Each JSON file represents a single
				  commit or transaction on the table, e.g., 000000.json, 000001.json, etc.
					- The JSON files allow Delta Lake to Maintain an audit trail of all changes made to the table Enable time travel operations to view the table at a previous version
					- Recover from failures by replaying the transaction log
				-
				- Parquet Files (actuall data is stored) While the
				  JSON files store the transaction log, the actual data of the Delta table is
				  stored in Parquet files. Parquet is a columnar storage format that is highly
				  efficient for analytical workloads. The Parquet data files contain the rows of the Delta table,
					- e.g.,
					  part-00000-123abc.parquet. Delta Lake manages these files transparently, adding
					  new files for new data and removing files for deleted data based on the
					  operations recorded in the JSON transaction log.
					-
				- CRC Files CRC (Cyclic Redundancy Check)The CRC file
				  contains a checksum of the data stored in the associated Parquet files for that
				  transaction. Delta Lake uses the CRC files to Detect any corruption in the Parquet data files Automatically repair corrupted files by recalculating the data from the transaction log.
			-
			- **DML/CRUD**
			     How DML works ??
				- Delta engine will locate files for suitable records .
				- Load the files into memory and engine scan for all the records among these 3 files each and make update Write back to storage system.
			- **Using a Timestamp:**
				- SELECT*FROMYOUR_DELTA_TABLE_NAME
				  AS OF TIMESTAMP'2024-04-25 10:30:00';
			- **2. Using a Version Number:**
			- Delta Tables
			  assign a unique version number to each write operation. You can use this
			  version number to travel back to a specific version of your data. Here's the
			  syntax (using Scala):
				- ```htmlmixed
				  Scala
				  valdf = spark.read
				    .format("delta")
				    .option("versionAsOf", 1234)  // Replace 1234 with the specific version number.load("/path/to/your/delta/table")
				  ```
			- Note :
				- Time travel is not possible if you drop and recreate the table
				- Data older than the retention period will be automatically deleted and unavailable
				  for time travel.
				- Vacuum operations (process of removing unused data) in Delta Lakes can also impact time travel capabilities. Vacuuming removes old data files, potentially limiting your ability to access specific historical versions.
			- Optimizations
				- 1. Z-Order ->  Sorts data inside partitions, improving read performance.
					- CAVA (Optimize Queries on `store_id`) and Users frequently filter sales by store (`store_id`).
				- 2. OPTIMIZE (Compacts Small Files)
					- `OPTIMIZE .. ZORDER BY (column)
				- 3. VACUUM (Removes Old Data for Storage Efficiency)
					- VACUUM fact_subscriptions RETAIN 48 HOURS;
