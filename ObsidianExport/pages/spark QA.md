exclude-from-graph-view:: true

- Why spark
  title:: spark QA
	- **Iterative Algorithm** 
	  **In Memory Processing** 
	  **Near real-time data processing
	  Rich and Simple API:**
- **DAG Scheduler**  and spark Job
	- Spark application using PySpark APIs, you create a series of transformations on data (e.g., map, filter, join).
	- Each transformation generates a new RDD  AND These RDDs are linked together, forming a directed acyclic graph (DAG)
	- Once you trigger an action on the final RDD (e.g., collect, count), PySpark submits the entire RDD lineage to the DAG scheduler.**
	- DAG Optimization**   ⇒ **Caching**  , **Partition Coalescing**  ,**Broadcast Variable**
	- stages =⇒ The DAG scheduler divides the optimized RDD lineage into stages
	- tasks =⇒  For each stage, the DAG scheduler generates a set of tasks that need to be executed on the Spark workers
	- DAG scheduler tracks the completion of all tasks across all stages  
	  TO Driver .
	- Note: In case of worker failures or task errors, the DAG scheduler can re-schedule tasks on different workers, leveraging RDD lineage for efficient recovery  .
- Stages
	- Spark creates a new stage whenever the data needs to be shuffled
	- Operations like groupByKey, reduceByKey, join, and explicit partition manipulations (repartition, coalesce) are strong indicators of shuffle boundaries.
- Transformations
	- transformations are lazy operations that define a new RDD, DataFrame, or Dataset based on an existing one, but do not perform any actual computation until an action is called  Transformations. Data execution doesn't take place just a plan is made .
	- **Narrow transformation** : Each partition of the child RDD can be computed independently from the other partitions ex:map,filter,union
	- **Wide transformation** : Shuffle requires partitions to be exchanged between the nodes in the cluster and cause of performance issue as well     ex: reducebykey, groupbyKey
	- **reduceByKey  : Both are Wide transformation  Does Mapside combine
	- **groupByKey** : Both are Wide transformation Doesn't do Mapside combine
- Define Action with Examples ?
	- Actions trigger the execution of the lazy transformations that were previously defined on the RDD, Data Frame, or Dataset. execution of takes place only when the action is called but not Transformations
	-
- **coalesce** : Shuffle on existing partitions
- Broad cast join :Allows for efficient joining of a large DataFrame with a smaller DataFrame by broadcasting the smaller DataFrame to all nodes in the cluster.
- **repartition**: repartition creates new partitions and does a full shuffle
- preferred locations: preferred locations allows Spark to understand the optimal locations for each partition's data and schedule tasks accordingly, enabling data locality optimization and minimizing unnecessary data movement across the cluster
- Spark 3.0 Advantages :
	- Adaptive Query execution also called AQE
	- Language Version Upgrades
	- New UI for Structure Streaming
	- Datasource to Read Binary Files
	- Support Recursive folders
	- Support Multi char delimiter (||)
	- New Spark build-in functions
	- Switch to Proleptic Gregorian calendar
	- DataFrame Tail
	- Added repartition to SQL queries
	- Better ANSI SQL compatible
- spark session with example : 
  collapsed:: true
	- spark   =
		- SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
		  
		  data = [
		- ("John", 30, "New York"),
		- ("Alice", 25, "San Francisco"),
		- ("Bob", 35, "Chicago")
		- ]
		- columns = ["Name", "Age", "City"]
- create a Dataframe : createDataFrame(rdd)
- Dataframe : Dataset<row>
- DF to RDD :
  collapsed:: true
	- rdd = df.rdd
	  logseq.order-list-type:: number
	- rddtest=df.rdd.take(1)[0] // row object
	  logseq.order-list-type:: number
- Empty RDD
	- spark.sparkContext.emptyRDD().toDF()
	- spark.createDataFrame(emptyRDD,schema) /// EMPTY DF
	- spark.createDataFrame([], schema)/// EMPTY DF
- data types in dataframe .
  collapsed:: true
	- from pyspark.sql.types import (StructField, StringType, StructType, IntegerType)
- spark.read method:
  collapsed:: true
	- spark.read.format("avro").load("person.avro")
	  spark.read.format("avro").load("person.avro")    
	  spark.read.jdbc(url, table, properties)  
	  spark.readStream
		- .format("kafka")
		- .option("kafka.bootstrap.servers", "192.168.1.100:9092")
		- .option("subscribe", "json_topic")
		- .option("startingOffsets", "earliest") // From starting
		- .load()
- read multiple files: df = spark.read.csv("path1,path2,path3")
- multi line for JSON :
	- multiline_df = spark.read.option("multiline", "true") \
	                         .json("resources/multiline-zipcode.json")
- print a df :
  collapsed:: true
	- df.show(truncate=False)
	- df.take(1)
	- df.show(n=3,truncate=25,vertical=True)
	- df.collect()
- To Pandas :
  collapsed:: true
	- pysparkDF.toPandas()
- Define  StructType :
  collapsed:: true
	- Represents the entire schema of a DataFrame.
	- It's a collection of StructField objects defining the names, data types, and
	  nullability of each column.
- StructField: Represents a single column in a DataFrame.
- 3 main attributes of  StructField
  collapsed:: true
	- name (str):
	  logseq.order-list-type:: number
	  The name of the column.
	- dataType (DataType):
	  logseq.order-list-type:: number
	  The data type of the column (e.g., StringType, IntegerType,ArrayType,Maptype).
	- nullable (bool,optional): Whether the column can contain null values (defaults to True).
	  logseq.order-list-type:: number
- Create DataFrame with schema : StructType([StructField("f1", StringType(), **True**)
- Adding a new col in df with default value :
  collapsed:: true
	- from pyspark.sql.functions import col,struct,lit
	- new_df = df.withColumn("state", lit("X"))
	- [Row(Name='John', Age=30, City='New York', state='X')]
- Adding a new col in df with exsisting value :
  collapsed:: true
	- new_df = df.withColumn("state", col("Age")*2)
- Filter : new_df.filter(col("DoubleAge")60).show()
- groupby : 
  collapsed:: true
	- new_df.groupBy(col("DoubleAge")).sum("DoubleAge").show()
	- df.groupBy("department").count()
- sort : df.sort(df.department.asc(),df.state.asc()).show(true))
- [pyspark.sql.streaming module](https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html#module-pyspark.sql.streaming)  consists of:
  collapsed:: true
	- [StreamingQuery](https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html#pyspark.sql.streaming.StreamingQuery)
	- [StreamingQueryManager](https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html#pyspark.sql.streaming.StreamingQueryManager)
	- [DataStreamReader](https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html#pyspark.sql.streaming.DataStreamReader)
	- [DataStreamWriter](https://spark.apache.org/docs/2.4.0/api/python/pyspark.sql.html#pyspark.sql.streaming.DataStreamWriter)
- Add a new row :
  collapsed:: true
	- from pyspark.sql import Row
	- Create a new row class
	  new_row = Row(col1=value1, col2=value2, ...)
	- Create a new DataFrame with the new row
	  new_df = spark.createDataFrame([new_row])
	- Union the new DataFrame with the existing DataFrame
	  updated_df = df.union(new_df)
- When and otherwise :
  collapsed:: true
	- df = df.withColumn("desc", when(col("Age") > 20, "old").otherwise("young"))
	- df = df.withColumn("desc", when(df.Age > 20, "old").otherwise("young"))
	- df.show()
- StructType.existsRecursively and its implementation :
  collapsed:: true
	- nested_schema = StructType([
	    StructField("name", StringType(), True),
	    StructField("contact", StructType([
	        StructField("email", StringType(), True),
	        StructField("phone", StringType(), True)
	    ]))
	  ])
	- print(nested_schema.existsRecursively("name"))  # True
	  print(nested_schema.existsRecursively("email"))  # True
	  print(nested_schema.existsRecursively("address"))  # False
- How to pass sql query in spark :
  collapsed:: true
	- import pyspark.sql.functions as F
	- expr_x = F.expr("""
		- avg(Age) over (partition by Age)  """)
			- df=df.withColumn('x',expr_x)
			- df.show()
- contains : df=df.filter((df.Name.contains("John"))
- startswith : df.filter(df.fname.startswith("T")).show()
- endswith : df.filter(df.fname.endswith("Cruise")).show()
- Handle nulls: 
  collapsed:: true
	- Using isNull() and isNotNull() functions:
		- df.filter(df.column.isNull()) - Filters rows where the specified column is NULL
		- df.filter(df.column.isNotNull()) - Filters rows where the specified column is not NULL
- How do you "like" in df : df2.filter(df2.name.like("%rose%")).show() ^6644550d-d004-4b0e-adf2-88d66f3288ba
- rlike : df2.filter(df2.name.rlike("(?i)^*rose$")).show()
- Filter vs select :
- select is for choosing which columns to keep  and filter is Keep all columns but filter rows based on a condition
  collapsed:: true
	- Both if you selecting all the columns :
	  collapsed:: true
		- df.select(df.fname,df.lname,df.id) \
		- .filter(df.id.isin(list)) \
		- .show()
- withColumn  vs select : 
  collapsed:: true
	- If you're adding a new column or modifying an existing one, use withColumn.
	- If you're just selecting specific columns (potentially with some transformation), use select.
- select vs selectExpr() : 
  collapsed:: true
	- select(): Used to select one or more columns from a DataFrame.
	  selectExpr(): Allows for more complex column selection using SQL expressions in run-time
		- df.select(col("col1"), col("col2"))
		  df.selectExpr("col1", "col2 * 2 as new_col")
- array_contains : 
  collapsed:: true
	- from pyspark.sql.functions import array_contains
		- df.filter(array_contains(df.languages,"Java")) \
		- .show(truncate=False)
- drop duplicates by selecting multiple columns : df.dropDuplicates(["department","salary"])
- join : empDF.join(deptDF,empDF.emp_dept_id=deptDF.dept_id,"inner").show(truncate=False)
- cache() : 
  collapsed:: true
	- MEMORY_ONLY for **RDD**
	- MEMORY_AND_DISK for **Dataset**
- Persist():
  collapsed:: true
	- from pyspark.storagelevel import StorageLevel
		- df.persist(StorageLevel.MEMORY_ONLY)
		- df.persist(StorageLevel.MEMORY_AND_DISK)
		- df.persist(StorageLevel.DISK_ONLY)
		- df.persist(StorageLevel.MEMORY_ONLY_SER)
			- df.persist(StorageLevel.MEMORY_AND_DISK_SER)
- **Choosing the Right Storage Level:**: 
  collapsed:: true
	- **For performance-critical operations:** Consider MEMORY_ONLY or MEMORY_AND_DISK if  your data fits in memory.
	- **For large datasets or limited memory:** Use MEMORY_AND_DISK_SER or DISK_ONLY for
	      efficient storage and fault tolerance.
	- **For archiving data:** DISK_ONLY is
	      suitable for long-term storage with low access frequency.
- unionAll syntax: df1.unionAll(df2)
- unionByName/allowMissingColumns :
  collapsed:: true
	- schema1 = ["id", "name", "age"]
	- schema2 = ["id", "name", "age", "city"]
	- df1 = spark.createDataFrame(data1, schema1)
	- f2 = spark.createDataFrame(data2, schema2) ^664456dd-4ad0-4b64-b0cc-63f58f5d95a8
	- merged_df = df1.unionByName(df2, allowMissingColumns=True).show()
- UDF :
  collapsed:: true
	- from pyspark.sql.functions import udf
	  my_udf = udf(my_udf, StringType())
	  spark.udf.register("<UDI-name in spark>", my_udf)
- UDF using annotation
  collapsed:: true
	- @udf(returnType=StringType())
	- def upperCase(str):
	- return str.upper()
	- df.withColumn("Cureated Name",
	- upperCase(col("Name"))) \
	- .show(truncate=False)
- map(f, preservesPartitioning=True): ^66445721-301d-4c13-a092-d72e3e68dc3e
  collapsed:: true
	- If the original RDD is partitioned (e.g., using partitionBy), the resulting RDD will maintain the same partitioning scheme
	- ex: used in reduceByKey or join, as it can avoid unnecessary data shuffling across partitions.
	- by default ,
	- map(f, preservesPartitioning=False) applies the function f to each element of the RDD, and the resulting RDD is not guaranteed to maintain the same partitioning scheme as the original RDD.
- flatMap():
  collapsed:: true
	- flatMap( [Iterator] ) // syntax
	- Ex: words = rdd.flatMap(lambda x: x)
- pandas:df.toPandas()
- Replace Replace 0 for null on only population column :
  collapsed:: true
	- df.na.fill(value=0,subset=["population"]).show()
	- df.na.fill(value=0).show()
- Row to column:
  collapsed:: true
	- df.groupBy("Product").pivot("Country").sum("Amount")
	  from pyspark.sql.functions import expr
	- unpivotExpr = "stack(3, 'Canada', Canada, 'China', China,
	- 'Mexico', Mexico) as (Country,Total)"
	- unPivotDF = pivotDF.select("Product",
	- expr(unpivotExpr)) \
	- .where("Total is not null")
	- unPivotDF.show(truncate=False)
- Multiple agg functions
  collapsed:: true
	- df.groupBy("department") \
	- .agg(sum("salary").alias("sum_salary"), \
	- avg("salary").alias("avg_salary"), \
	- sum("bonus").alias("sum_bonus"), \
	- max("bonus").alias("max_bonus") \
	- ) \
- partitionBy():
  collapsed:: true
	- df.write.option("header",True) \
	- .partitionBy("state","city") \
	- .mode("overwrite") \
	- .csv("/tmp/zipcodes-state")
- controlling Data skew:
  collapsed:: true
	- f.write.option("header",True) \
	- .option("maxRecordsPerFile", 2) \
	- .partitionBy("state") \
	- .mode("overwrite") \
	- .csv("/tmp/zipcodes-state")
- explode:
  collapsed:: true
	- If you want to include null values in the exploded output, you can use the explode_outer or posexplode_outer functions instead of explode
- flatten vs explode:
  collapsed:: true
	- "flatten" refers to the process of denormalizing nested data structures, while "explode" is a specific operation in Apache Spark that transforms array or map columns into multiple rows.
- approx distinct count:
  collapsed:: true
	- approx_count_distinct()
	- str(df.select(approx_count_distinct("salary")).collect()[0][0]))
- collect_list  vs collect_set:
  collapsed:: true
	- collect_list: Aggregates values into a list preserving duplicates.
	  collect_set: Aggregates values into a set removing duplicates.
	- df.select(collect_list("salary")).show(truncate=False)
	  df.select(collect_set("salary")).show(truncate=False)
- concat_ws:
  collapsed:: true
	- from pyspark.sql.functions import col, concat_ws
	- df2 = df.withColumn("languagesAtSchool",
	- concat_ws(",",col("languagesAtSchool")))
- max,min,first,last:
  collapsed:: true
	- from pyspark.sql.window import Window
	- from pyspark.sql.functions import row_number
	- windowSpec =Window.partitionBy("department").orderBy("salary")
	- df.withColumn("row_number",row_number().over(windowSpec)).show(truncate=False)
- date_format:
  collapsed:: true
	- df.select(col("input"),
	- date_format(col("input"), "MM-ddyyyy").
	- alias("date_format")).show()
- to_json:
  collapsed:: true
	- from pyspark.sql.functions import to_json,col
	- df2.withColumn("value",to_json(col("value"))) \
	- .show(truncate=False)
- json_tuple:
  collapsed:: true
	- from pyspark.sql.functions import json_tuple
	- df.select(col("id"),json_tuple(col("value"),"Zipcode
	- ","ZipCodeType","City")) \
	- .toDF("id","Zipcode","ZipCodeType","City") \
	- .show(truncate=False)
- df.write:
	- df2.write.format("csv").mode('overwrite').save("/tmp/
	  collapsed:: true
		- spark_output/zipcodes")
		  collapsed:: true
			- Diff Modes
			- overwrite – mode is used to overwrite the existing file.
			- append – To add the data to the existing file.
			- ignore – Ignores write operation when the file already exists.
			- error – This is a default option when the file already exists, it returns an error.
-
