deck:: [[pyspark_syntax]]

- What are the different ways to create a DataFrame in PySpark?
  id:: 680b0655-1df6-4c55-a19d-2eb87633ee89
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfc3
		- from files => 
		      ```python
		      spark.read.csv("/text/json/parquet/format")
		    	spark.read.option("key1", "value1").format("file_format").load("path") -> myfav
		  ```
		- from rdd => 
		      ```python
		      createDataFrame(rdd)
		      ```
		- from data lists => 
		      ```python
		      createDataFrame(dataList)
		      ```
		- from Row objects => 
		      ```python
		      createDataFrame(rowData,columns)
		      ```
		- with schema => 
		      ```python
		      createDataFrame(dataList,schema)
		      ```
- How do you check if a specific column exists in a DataFrame schema?
  id:: 680b07a6-18ef-40e4-971e-32e9f50aea0d
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfc4
		- Use:
		      ```python
		      df.schema.contains(StructField("firstname", StringType, true))
		      ```
		      to check for the existence of a column with specific name and data type or 
		      ```python
		      "id" in df.columns
		      ```
- What is the syntax for defining a nested schema with array and map types?
  id:: 680b07a6-ac8a-4d5b-8732-9ba7f31b2ef4
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfc5
		- ```python
		      StructType([
		          StructField('name', StructType([nested fields])), 
		          StructField('hobbies', ArrayType(StringType()), True), 
		          StructField('properties', MapType(StringType(), StringType()), True)
		      ])
		      ```
- How do you update column names when creating a DataFrame?
  id:: 680b07a6-3446-400f-92aa-16ad0fbde06d
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfc6
		- Use:
		      ```python
		      updatedcolumns = ["name", "languagesAtSchool", "currentState"]
		      df = spark.createDataFrame(data).toDF(*updatedcolumns)
		      ```
- How do you configure a streaming data source in PySpark?
  id:: 680b07a6-b4c5-4fb3-ba67-747ea0a8ead5
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfc7
		- Use:
		      ```python
		      spark.readStream.format("source").option("key", "value").load()
		      ```
		      For example with Kafka:
		      ```python
		      spark.readStream.format("kafka") \
		        .option("kafka.bootstrap.servers", "host:port") \
		        .option("subscribe", "topic") \
		        .option("startingOffsets", "earliest") \
		        .load()
		      ```
- What are the different methods to display DataFrame data?
  id:: 680b07a6-8cab-4534-a8a9-b728dad9ab58
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfc8
		- For all rows:
		      ```python
		      df.show(truncate=False)
		      ```
		      For specific number of rows:
		      ```python
		      df.show(2, truncate=False)
		      ```
		      For vertical display with truncation:
		      ```python
		      df.show(n=3, truncate=25, vertical=True)
		  | Parameter       | Meaning                                                            |
		  | --------------- | ------------------------------------------------------------------ |
		  | `n=3`           | Show only **3 rows** from the DataFrame.                           |
		  | `truncate=25`   | **Truncate column values** longer than 25 characters (adds "..."). |
		  | `vertical=True` | Display each **row vertically**, i.e., one field per line per row. |
		  
		  ```
- How do you create an empty DataFrame with a defined schema?
  id:: 680b07a6-5369-4566-b08a-99ec721c3cab
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfc9
		- ```python
		      spark.createDataFrame([], schema)
		      ```
		      or
		      ```python
		   emptyRDD = spark.sparkContext.emptyRDD()
		      spark.createDataFrame(emptyRDD, schema)
		      ```
- What is the syntax for casting a column to a different data type?
  id:: 680b07a6-45f9-4c94-bbd1-01b8167d3caf
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfca
		- ```python
		      df.select(df.fname, df.id.cast("int")).printSchema()
		      ```
- How do you filter data in a PySpark DataFrame?
  id:: 680b07a6-bdd6-4f9b-92b1-28159b657d14
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfcb
		- Use `df.filter()` with conditions like:
		      ```python
		      df.filter(df.id.between(100,300))
		      ```
		      ```python
		      df.filter(df.fname.contains("Cruise"))
		      ```
		      ```python
		      df.filter(df.fname.startswith("T"))
		      ```
- How do you create a struct column with multiple fields and conditional values?
  id:: 680b07a6-b5c4-4c34-9327-ebcaf35158c5
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfcc
		- ```python
		      df2.withColumn("OtherInfo", 
		          struct(
		              col("id").alias("identifier"),
		              col("gender").alias("gender"),
		              col("salary").alias("salary"),
		              when(col("salary").cast(IntegerType()) < 2000, "Low")
		              .when(col("salary").cast(IntegerType()) < 4000, "Medium")
		              .otherwise("High").alias("Salary_Grade")
		          )
		      ).drop("id", "gender", "salary")
		      ```
- How do you select columns using different methods in PySpark?
  id:: 680b07a6-bdc1-4e08-8dbc-ab46e481072c
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfcd
		- Using column object notation:
		      ```python
		      df.select(df.column_name)
		      ```
		      Using col function:
		      ```python
		      df.select(col("column_name"))
		      ```
		      Using expr and selectExpr function:
		      ```python
		      df.select(expr("column_expression"))
		         result_df = df.select(
		  		"name",
		  		expr("age + 1 AS age_next_year"),
		  		expr("salary * 1.1 AS increased_salary"),
		  		expr("CASE WHEN age > 35 THEN 'Senior' ELSE 'Junior' END AS category")
		  	)
		  or 
		   df.selectExpr(
		      "name",
		      "age + 1 AS age_next_year",
		      "salary * 1.1 AS increased_salary",
		      "CASE WHEN age > 35 THEN 'Senior' ELSE 'Junior' END AS category"
		  )
		  
		  Note : 
		  
		  | Feature                  | `expr`                                                       | `selectExpr`                                                                 |
		  | ------------------------ | ------------------------------------------------------------ | ---------------------------------------------------------------------------- |
		  | **Purpose**              | Converts a SQL expression string into a **Column object**    | Allows **selecting columns and applying expressions directly using strings** |
		  | **Usage**                | Used **inside `select()`, `withColumn()`, `filter()`**, etc. | Used **like `select()`**, but takes **SQL expressions as strings**           |
		  | **Return type**          | `Column`                                                     | `DataFrame`                                                                  |
		  | **Example**              | `python df.select(expr("age + 1 AS age_next_year"))`         | `python df.selectExpr("age + 1 AS age_next_year")`                           |
		  | **Multiple expressions** | Must wrap each expression with `expr()`                      | Can pass multiple strings directly                                           |
		  
		  
		  ```
			- `
- How do you convert a PySpark DataFrame to a Pandas DataFrame?
  id:: 680b07a6-5b93-4eed-a77d-68c5b2ca4ab4
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfce
		- ```python
		      pysparkDF.toPandas()
		      ```
- What is the purpose of the toDF() method and its variations?
  id:: 680b07a6-6001-4608-a9c6-098f63fee25e
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfcf
		- `toDF()` converts an RDD to a DataFrame with default column names
		      ```python
		      rdd.toDF()
		      ```
		      `toDF(*cols)` allows specifying column names during conversion
		      ```python
		      rdd.toDF(*["col1", "col2", "col3"])
		      ```
- How do you work with Row objects in PySpark?
  id:: 680b07a6-e2d6-47c5-b1f7-fee5d54b865c
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd0
		- Create a list of Row objects:
		      ```python
		     - data = [Row(name="James", prop=Row(hair="black", eye="blue"))]
		      # Then create a DataFrame
		     ```
			- ```
			  spark.createDataFrame(data)
			   data = [
			  Row(id=1, text="Hello-World"),
			  Row(id=2, text="Spark-SQL")
			  ]
			  df = spark.createDataFrame(data)
			  display(df)
			  id	text
			  1	Hello-World
			  2	Spark-SQL
			    ```
- How do you concatenate columns using expr() function?
  id:: 680b07a6-c60d-4903-8e04-122576394eba
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd1
		- ```python
		      df.select(expr("fname ||','|| lname").alias("fullName")).show()
		      ```
- What are the different string pattern matching methods for filtering DataFrames?
  id:: 680b081e-adc7-432f-8374-d0f9da5e9248
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd2
		- endswith():
		      ```python
		      df.filter(df.fname.endswith("Cruise"))
		      ```
		      like():
		      ```python
		      df.filter(df.fname.like("%om"))
		      ```
		      rlike() for regex patterns:
		      ```python
		      df.filter(df2.name.rlike("(?i)^*rose$"))
		      ```
		      contains():
		      ```python
		      df.filter(df.state.contains("H"))
		      ```
- How do you check for NULL values in DataFrame columns?
  id:: 680b081e-7d49-47dc-ba77-9d17c2544fdc
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd3
		- Use isNull():
		      ```python
		      df.filter(df.lname.isNull()).show()
		      ```
		      or isNotNull():
		      ```python
		      df.filter(df.lname.isNotNull()).show()
		      ```
- What are the different methods to perform substring operations?
  id:: 680b081e-33b5-4700-bf04-bc77c1834d3a
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd4
		- ```python
		      df.select(df.fname.substr(1,2).alias("substr")).show()
		      ```
		      to extract part of a string
- How do you implement conditional logic in PySpark DataFrame columns?
  id:: 680b081e-7528-40cf-91c9-c80444e90243
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd5
		- Use when() and otherwise():
		      ```python
		      df.select(
		          df.fname, 
		          df.lname, 
		          when(df.gender=="M", "Male")
		          .when(df.gender=="F", "Female")
		          .when(df.gender==None, "")
		          .otherwise(df.gender).alias("new_gender")
		      ).show()
		      ```
- How do you filter DataFrame rows based on whether a value is in a list?
  id:: 680b081e-c7bb-40c2-b19e-b91df1d1b026
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd6
		- Use isin():
		      ```python
		      df.select(df.fname, df.lname, df.id).filter(df.id.isin(list)).show()
		      ```
		      or isin()== False:
		      ```python
		      df.filter(df.state.isin(list)==False).show()
		  ```
- What are the different methods to sort DataFrame data?
  id:: 680b081e-d158-4f7a-bcc8-8f070f30f643
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd7
		- sort():
		      ```python
		      df.sort("department", "state").show(truncate=False)
		      ```
		      orderBy():
		      ```python
		      df.orderBy("department", "state").show(truncate=False)
		      ```
		      With explicit sort order:
		      ```python
		      df.sort(df.department.asc(), df.state.asc()).show(truncate=False)
		      ```
- How do you perform groupBy operations with multiple aggregations?
  id:: 680b081e-adf2-4bf0-a989-e091d12fbbf3
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd8
		- ```python
		      df.groupBy("department").agg(
		          sum("salary").alias("sum_salary"),
		          avg("salary").alias("avg_salary"),
		          sum("bonus").alias("sum_bonus"),
		          max("bonus").alias("max_bonus")
		      ).show(truncate=False)
		      ```
- How do you access nested fields in struct columns?
  id:: 680b081e-d584-4f6d-a36c-fba8c4768481
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfd9
		- Use dot notation:
		      ```python
		    from pyspark.sql.functions import col
		  
		  # Equivalent to the above example
		  df.select(
		  	col("user_id"),
		  	col("user_profile.first_name"),
		  	col("user_profile.address.city"))
		  	
		  	# Explode an array of structs
		  	from pyspark.sql.functions import col, explode
		  	df.select("user_id", explode("addresses").alias("address")) \
		  	  .select("user_id", "address.city", "address.zip")
		  	
		  
		  	#sql 					
		  	from pyspark.sql.functions import expr
		  
		  		df.select(
		  			"user_id",
		  			expr("user_profile.first_name as first_name"),
		  			expr("user_profile.address.city as city")
		  		)
		  		
		  	#Creating a Schema for Complex Types . Nested 
		  						address_schema = StructType([
		  		StructField("street", StringType(), True),
		  		StructField("city", StringType(), True),
		  		StructField("zip", StringType(), True)
		  	])
		  ```
- What methods are available for combining DataFrames?
  id:: 680b081e-0587-40c6-a82d-275806f8d952
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfda
		- union():
		      ```python
		      unionDF = df.union(df2)
		      ```
		      Union with distinct values:
		      ```python
		      disDF = df.union(df2).distinct()
		      ```
		      unionByName():
		      ```python
		      merged_df = df1.unionByName(df2)
		      ```
		      unionByName with missing columns:
		      ```python
		      merged_df = df1.unionByName(df2, allowMissingColumns=True)
		      ```
- How do you create user-defined functions (UDFs) in PySpark?
  id:: 680b081e-9079-426a-a7a2-d0b8a1c28a58
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfdb
		- Define a function, create UDF . Temporary UDF
			- UDF using annotation 
			  ```python
			  @udf(returnType=StringType())
			  def upperCase(str):
			  if str is None:
			  	return None
			  return str.upper()
			  
			  # Apply to DataFrame
			  df = spark.createDataFrame([("john",), ("jane",), (None,)], ["name"])
			  result = df.withColumn("upper_name", upperCase(col("name")))
			  ```
			- single use / session
			     ```python
			  # Define Python function
			  def upperCase(value):
			  	if value is None:
			  		return None
			  	return value.upper()
			  
			  # create a 
			  upperCaseUDF = udf(upperCase, StringType())
			  
			  # Apply directly in DataFrame operations
			  df.withColumn("Curated Name", upperCaseUDF(col("Name")))
			     ```
				- Register it and use in mult - spark session :
				  ```python
				  from pyspark.sql import SparkSession
				  from pyspark.sql.functions import col
				  # Import the functions from your file
				  from my_udfs import upper_case, register_all_udfs
				  
				  # Create a new SparkSession
				  spark = SparkSession.builder.appName("MultiSessionApp").getOrCreate()
				  
				  # Register the UDFs to make them available for Spark SQL
				  register_all_udfs(spark)
				  
				  df = spark.createDataFrame([("john",), ("jane",), (None,)], ["name"])
				  
				  # Use the UDF with DataFrame API
				  df.withColumn("upper_name", upper_case(col("name"))).show()
				  
				  # Use the UDF with Spark SQL
				  df.createOrReplaceTempView("people")
				  spark.sql("SELECT name, upper_case_sql(name) as upper_name FROM people").show()
				  ```
- How do you register UDFs for use in Spark SQL?
  id:: 680b081e-50b2-4609-8fbf-0429f9319131
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfdc
		- ```python
		      spark.udf.register("convertUDF", convertCase, StringType())
		      ```
		      Then use:
		      ```python
		      spark.sql("select Seqno, convertUDF(Name) as Name from NAME_TABLE").show(truncate=False)
		      ```
- How do you implement joins between DataFrames?
  id:: 680b081e-3542-431a-9999-ddd7be5e70de
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfdd
		- ```python
		      empDF.join(deptDF, empDF.emp_dept_id == deptDF.dept_id, "inner").show(truncate=False)
		      ```
		      where the join type can be inner, outer, left, right, etc.
- How do you handle duplicate rows in a DataFrame?
  id:: 680b081e-c23d-4ac6-8fac-cae305d62cc9
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfde
		- Use distinct() for all columns:
		      ```python
		      df.distinct()
		      ```
		      or dropDuplicates() for specific columns:
		      ```python
		      df.dropDuplicates(["department", "salary"])
		      ```
- How do you add missing columns from one DataFrame to another?
  id:: 680b081e-369c-4c4d-b6d0-6c3b1402b88f
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfdf
		- Using lit():
		      ```python
		      for column in [column for column in df2.columns if column not in df1.columns]:
		          df1 = df1.withColumn(column, lit(None))
		      ```
- How do you filter DataFrames based on array column values?
  id:: 680b081e-8aff-4e4f-859e-ef5be626d2fe
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe0
		- Using array_contains:
		      ```python
		  from pyspark.sql.functions import array_contains
		  df.filter(array_contains(df.languages, "Java")).show(truncate=False)
		   
		   or 
		  
		  from pyspark.sql.functions import explode
		  
		  # Explode array then filter
		  df_exploded = df.select("*", explode(df["tags"]).alias("tag"))
		  df_filtered = df_exploded.filter(df_exploded["tag"] == "python").dropDuplicates()
		  ```
- How do you create a UDF using annotation in PySpark?
  id:: 680b081e-b67a-415b-8465-3f820073369f
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe1
		- Use the @udf decorator with return type:
		      ```python
		  @udf(returnType=StringType())
		  def upperCase(str):
		    return str.upper()
		  
		  # Register with SparkSession
		  spark.udf.register("upperCaseSQL", upperCase)
		  ```
- What is the difference between sample() and takeSample() in Spark RDDs?
  id:: 680b081e-be50-4aa1-a8cd-899e06e45ebf
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe2
		- sample(withReplacement, fraction, seed) returns an RDD with a fraction of elements:
		      ```python
		      # withReplacement=False prevents duplicates
		      # withReplacement=True allows duplicates
		      rdd.sample(False, 0.1)
		      ```
		      
		      takeSample(withReplacement, n, seed) is an action that returns a fixed number of elements to the driver:
		      ```python
		      rdd.takeSample(False, 10)
		   
		   sample() keeps your data distributed for further RDD/DataFrame operations, while takeSample() brings a specific number of elements to the driver program
		      ```
- How do you replace NULL/None values in a DataFrame?
  id:: 680b081e-c7d2-4970-9fdb-b6d6da782b43
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe3
		- For all numeric columns:
		      ```python
		      df.na.fill(value=0).show()
		      ```
		      For specific columns:
		      ```python
		      df.na.fill(value=0, subset=["population"]).show()
		      ```
		      With different values per type:
		      ```python
		      df.na.fill("unknown", ["city"]).na.fill("", ["type"]).show()
		      ```
			- Concept	Python / PySpark	SQL / DataFrame Context
			  None	Python’s way of saying "no value" or "missing"	Used in Python code to indicate nulls
			  NULL	SQL’s way of saying "missing value"	Appears in DataFrames and SQL queries
			- None is Python → becomes NULL in DataFrame.
			  Always use Spark-safe functions (isNull(), fillna(), coalesce()) for NULL.
			  Never use == None in filter() — use .isNull() instead.
- What is the difference between map() and flatMap() in Spark RDDs?
  id:: 680b081e-52f1-4f60-bcd0-da993464186b
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe4
		- map(lambda x: transformation) applies a function to each element and preserves the structure:
		      ```python
		   # Create an RDD with strings
		  rdd = sc.parallelize(["hello spark", "big data"])
		  # Using map to split each string
		  map_result = rdd.map(lambda x: x.split())
		  print("map result:", map_result.collect())
		  map result: [['hello', 'spark'], ['big', 'data']]
		      ```
		      
		      flatMap(lambda x: x.split(" ")) applies a function that returns an iterator and flattens the results:
		      ```python
		  # Using flatMap to split each string
		  flatmap_result = rdd.flatMap(lambda x: x.split())
		  print("flatMap result:", flatmap_result.collect())
		  flatMap result: ['hello', 'spark', 'big', 'data']
		  ```
		- The key difference is that map() maintains a one-to-one relationship between input and output elements, while flatMap() allows one-to-many relationships and flattens the results into a single-level collection.
		- | Operation   | Output per record                      | Final structure                        |
		  | ----------- | -------------------------------------- | -------------------------------------- |
		  | `map()`     | Returns **one item/list** per element  | Result is a **list of lists** (nested) |
		  | `flatMap()` | Tokenizing text . Returns **multiple items** per element | Result is a **flattened list** (1D)    |
- How do you access specific columns when using RDD map operations?
  id:: 680b081e-9e70-4926-8f7d-4c57d1679d66
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe5
		- By position:
		      ```python
		      df.rdd.map(lambda x: (x[0]+","+x[1], x[2], x[3]*2))
		      ```
		      By column name:
		      ```python
		      df.rdd.map(lambda x: (x.firstname+","+x.lastname, x.gender, x.salary*2))
		      ```
- How do you convert string columns to arrays in PySpark?
  id:: 680b081e-8c59-4fcd-abe6-726b643c17c3
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe6
		- Using split function:
		      ```python
		      from pyspark.sql.functions import split
		      df.select(split(df.name, ",").alias("nameAsArray")).show()
		   
		   or
		   
		   # Convert string column to array using split()
		   df_with_array = df.withColumn("categories_array", split(col("categories"), ","))
		      ```
- How do you create an array column by combining multiple columns?
  id:: 680b081e-f33e-4875-b792-5d0b40e64bba
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe7
		- Using array function:
		      ```python
		      from pyspark.sql.functions import array
		      df.select(df.name, array(df.currentState, df.previousState).alias("States")).show()
		   or 
		   
		   df = df.withColumn("status_array", expr("array(status, 'active', 'pending')"))
		  
		  Note : Triple quotes """ """ are only required if your expression spans multiple lines:
		    df = df.withColumn(
		      "status_array",
		      expr("""
		          array(
		              status,
		              'active',
		              'pending'
		          )
		      """)
		  )
		  
		  ```
- How do you check if an array column contains a specific value?
  id:: 680b081e-0c18-4adb-930a-9501cc943e7a
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe8
		- Using array_contains:
		      ```python
		      from pyspark.sql.functions import array_contains
		      df.select(df.name, array_contains(df.languagesAtSchool, "Java").alias("array_contains")).show()
		      ```
- How do you iterate through all rows in a DataFrame?
  id:: 680b081e-6ed0-46db-9252-1ab8f223fa4b
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfe9
		- Using foreach action:
		      ```python
		      df.foreach(lambda x: print("Data ==>" + x["firstname"] + "," + x["lastname"] + "," + x["gender"] + "," + str(x["salary"]*2)))
		      ```
		      Or collect and loop:
		      ```python
		      dataCollect = df.collect()
		      for row in dataCollect:
		          print(row["firstname"] + "," + row["lastname"])
		      ```
- What is the usage of explode() function and when is it used?
  id:: 680b081e-0253-414b-8257-96d035f3143f
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfea
		- explode() creates a new row for each element in an array column:
		      ```python
		      df.select(df.name, explode(df.languagesAtSchool)).show()
		      ```
- How do you pivot data in a DataFrame?
  id:: 680b081e-fabb-4142-a16c-7b73b32d13d7
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfeb
		- Using pivot method:
		      ```python
		      df.groupBy("Product").pivot("Country").sum("Amount")
		  Input DataFrame
		  Product	Country	Amount
		  Greek Bowl	USA	100
		  Greek Bowl	Canada	80
		  Falafel Wrap	USA	90
		  Greek Bowl	USA	50
		  
		  output
		  +-------------+------+-------+
		  | Product     |Canada|    USA|
		  +-------------+------+-------+
		  | Greek Bowl  |    80|    150|
		  | Falafel Wrap|  null|     90|
		  +-------------+------+-------+
		  
		  ```
- How do you unpivot data in PySpark?
  id:: 680b081e-13fe-4c1f-b22c-2fa5ebc00c0c
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfec
	  card-last-interval:: -1
	  card-repeats:: 0
	  card-ease-factor:: 2.5
	  card-last-reviewed:: nil
	  card-next-schedule:: nil
	  card-last-score:: nil
		- Using stack function with expr:
		      ```python
		      unpivotExpr = "stack(3, 'Canada', Canada, 'China', China, 'Mexico', Mexico) as (Country, Total)"
		      unPivotDF = pivotDF.select("Product", expr(unpivotExpr)).where("Total is not null")
		   
		   or 
		   
		   # Without using expr:
		  unPivotDF = pivotDF.select(
		  	"Product",
		  	stack(
		  		3,
		  		lit("Canada"), col("Canada"),
		  		lit("China"), col("China"),
		  		lit("Mexico"), col("Mexico")
		  	).alias("Country", "Total")
		  ).where(col("Total").isNotNull())
		      ```
- How do you partition DataFrame output when writing to storage?
  id:: 680b081e-cf1f-4d47-a8ef-c4cb00ffc114
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfed
		- Using partitionBy:
		      ```python
		      df.write.option("header", True) \
		        .partitionBy("state", "city") \
		        .mode("overwrite") \
		        .csv("/tmp/zipcodes-state")
		      ```
- How do you optimize the number of files in partitioned output?
  id:: 680b081e-72a5-4b83-ad82-f6df4464cf96
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfee
		- Using maxRecordsPerFile option:
		      ```python
		  df.write.option("header", True) \
		        .option("maxRecordsPerFile", 2) \
		        .partitionBy("state") \
		        .mode("overwrite") \
		        .csv("/tmp/zipcodes-state")
		  
		  EXAMPLE:
		  /tmp/zipcodes-state/
		  ├── state=California/
		  │   ├── part-00000-xxx.csv  (contains 2 records)
		  │   ├── part-00001-xxx.csv  (contains 2 records)
		  │   └── part-00002-xxx.csv  (contains remaining California records)
		  ├── state=New York/
		  │   ├── part-00000-xxx.csv  (contains 2 records)
		  │   └── part-00001-xxx.csv  (contains remaining New York records)
		  └── state=Texas/
		  	└── part-00000-xxx.csv  (contains all Texas records if ≤ 2)
		    
		  If California has 5 records → 3 files: 2 + 2 + 1
		  If New York has 3 records → 2 files: 2 + 1
		  If Texas has only 2 or fewer records → 1 file
		  ```
- How do you efficiently convert a DataFrame to Pandas with Arrow?
  id:: 680b081e-641a-410b-97da-32376b1fa83a
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfef
		- Enable Arrow optimization:
		      ```python
		      spark.conf.set("spark.sql.execution.arrow.enabled", "true")
		      ```
		      Then convert:
		      ```python
		      pandasDF = df.toPandas()
		      ```
- What is the purpose of the flatten() function?
  id:: 680b081e-2de3-44e7-b4d2-c0402639263d
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff0
		- flatten() converts an array of arrays into a single array without creating new rows:
		      ```python
		      # Create sample data with nested arrays
		  	data = [
		  		("Alice", [["Math", "Physics"], ["English", "Literature"]]),
		  		("Bob", [["History", "Geography"], ["Art"]]),
		  		("Carol", [["Computer Science"], ["Chemistry", "Biology", "Physics"]]),
		  		("David", [[]]),  # Empty inner array
		  		("Eve", None)     # Null array
		  	]
		  
		  	# Create the DataFrame
		  	df = spark.createDataFrame(data, schema)
		  
		  	# Show the original DataFrame
		  	print("Original DataFrame:")
		  	df.show(truncate=False)
		  
		  	# Apply the flatten function
		  	flattened_df = df.select(df.name, flatten(df.subjects).alias("flattened_subjects"))
		      
		      +------+----------------------------------------+
		  | name | flattened_subjects                    |
		  +------+----------------------------------------+
		  | Alice| [Math, Physics, English, Literature]  |
		  | Bob  | [History, Geography, Art]             |
		  | Carol| [Computer Science, Chemistry, Biology, Physics] |
		  | David| []                                     |
		  | Eve  | null                                   |
		  +------+----------------------------------------+
		  
		  ****
		      
		  | Feature    | `flatMap()` (RDD)                             | `flatten()` (DataFrame function)              |
		  | ---------- | --------------------------------------------- | --------------------------------------------- |
		  | Applies To | RDDs                                          | DataFrame columns (arrays)                    |
		  | Input Type | RDD of elements                               | Column of arrays (possibly nested)            |
		  | Output     | **Flattens to rows**                          | **Flattens to a single array** (not rows)     |
		  | Goal       | Convert multiple outputs per row into 1D rows | Merge nested arrays into one array (same row) |
		  | Similar To | explode + map                                 | array flatten in Python or SQL                |
		  
		  ```
- What are the key aggregate functions in PySpark and their syntax?
  id:: 680b085e-85db-4381-b83b-da76e5533b52
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff1
		- first("column"):
			- ```python
			  +-------+-------+
			  |   name| salary|
			  +-------+-------+
			  |   John|  85000|
			  |  Sarah|  92000|
			  | Michael| 78000|
			  |   Emma| 105000|
			  |  David|  67000|
			  |   John|  85000|
			  +-------+-------+
			  
			  
			  df.select(first("salary"))
			  ```
			      last("column"):
			      ```python
			      df.select(last("salary"))
			      ```
			      min("column"):
			      ```python
			      df.select(min("salary"))
			      ```
			      max("column"):
			      ```python
			      df.select(max("salary"))
			      ```
			      avg/mean:
			      ```python
			      df.select(avg("salary"))
			      ```
			      collect_list:
			      ```python
			      df.select(collect_list("salary"))
			    collect_list: [[85000, 92000, 78000, 105000, 67000, 85000]] #keeps all occurrences
			  ```
			      collect_set:
			      ```python
			      df.select(collect_set("salary"))
			    collect_set:  [[85000, 92000, 78000, 105000, 67000]] # collect_set → removes duplicates
			  ```
			      count:
			      ```python
			      df.select(count("salary"))
			      ```
			      countDistinct:
			      ```python
			      df.select(countDistinct("department", "salary"))
			      ```
			      sum:
			      ```python
			      df.select(sum("salary"))
			      ```
			      sumDistinct:
			      ```python
			      df.select(sumDistinct("salary"))
			      ```
- How do you format dates in PySpark?
  id:: 680b085e-bb6e-48ba-921f-894004fff328
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff2
		- Using date_format:
		      ```python
		      df.select(col("input"), date_format(col("input"), "MM-dd-yyyy").alias("date_format")).show()
		      ```
- How do you convert string columns to date type?
  id:: 680b085e-6a2f-4ffc-a9ff-90101ee4e2d2
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff3
		- Using to_date:
		      ```python
		      df.select(col("input"), to_date(col("input"), "yyyy-MM-dd").alias("to_date")).show()
		      ```
- How do you calculate the difference between dates?
  id:: 680b085e-7402-4827-b091-4ae6471e4a9d
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff4
		- Using datediff:
		      ```python
		      df.select(col("input"), datediff(current_date(), col("input")).alias("datediff")).show()
		      ```
- How do you calculate months between two dates?
  id:: 680b085e-3feb-41fe-8f5d-e8e9c066fe0f
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff5
		- Using months_between:
		      ```python
		      df.select(col("input"), months_between(current_date(), col("input")).alias("months_between")).show()
		   
		   or 
		   
		   # Extract year and month components, then calculate difference
		  df = df.withColumn("months_diff", 
		  				  ((year(col("end_date")) - year(col("start_date"))) * 12) + 
		  				  (month(col("end_date")) - month(col("start_date"))))
		    
		  	# Using SQL expression for month calculation
		  	df = df.withColumn("months_diff", 
		                expr("(year(end_date) - year(start_date)) * 12 + (month(end_date) - month(start_date))"))
		      ```
- How do you truncate dates to specific units?
  id:: 680b085e-3641-4994-a88c-b2bde4cd536d
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff6
		- Using trunc:
		      ```python
		      df.select(
		          col("input"), 
		          trunc(col("input"), "Month").alias("Month_Trunc"), 
		          trunc(col("input"), "Year").alias("Year_Trunc")
		      ).show()
		   
		  
		  +-------------------+-------------------+-------------------+-------------------+
		  |timestamp_col      |day_trunc          |month_trunc        |year_trunc         |
		  +-------------------+-------------------+-------------------+-------------------+
		  |2023-09-15 08:30:45|2023-09-15 00:00:00|2023-09-01 00:00:00|2023-01-01 00:00:00|
		  |2023-09-15 14:20:30|2023-09-15 00:00:00|2023-09-01 00:00:00|2023-01-01 00:00:00|
		  |2023-10-22 10:15:00|2023-10-22 00:00:00|2023-10-01 00:00:00|2023-01-01 00:00:00|
		  |2023-12-31 23:59:59|2023-12-31 00:00:00|2023-12-01 00:00:00|2023-01-01 00:00:00
		  
		  """
		  Note: 
		    SELECT
		    timestamp_col,
		    DATE_TRUNC('day', timestamp_col) AS day_trunc,
		    DATE_TRUNC('month', timestamp_col) AS month_trunc,
		    DATE_TRUNC('year', timestamp_col) AS year_trunc
		  FROM your_table_name; /*post-gres & redshift*/
		  """
		  ```
- How do you add or subtract time from dates?
  id:: 680b085e-fd0d-46e0-8bc8-e079a61dcf44
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff7
		- Using add_months, date_add, date_sub:
		      ```python
		      df.select(
		          col("input"),
		          add_months(col("input"), 3).alias("add_months"),
		          add_months(col("input"), -3).alias("sub_months"),
		          date_add(col("input"), 4).alias("date_add"),
		          date_sub(col("input"), 4).alias("date_sub")
		      ).show()
		      ```
- How do you extract parts of a date?
  id:: 680b085e-f420-406a-907e-3a3d7aa18501
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff8
		- Using year, month, next_day, weekofyear:
		      ```python
		      df.select(
		          col("input"),
		          year(col("input")).alias("year"),
		          month(col("input")).alias("month"),
		          next_day(col("input"), "Sunday").alias("next_day"),
		          weekofyear(col("input")).alias("weekofyear")
		      ).show()
		      ```
- How do you extract day information from dates?
  id:: 680b085e-8d09-4af4-867f-e73538630773
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dff9
		- Using dayofweek, dayofmonth, dayofyear:
		      ```python
		      df.select(
		          col("input"),
		          dayofweek(col("input")).alias("dayofweek"),
		          dayofmonth(col("input")).alias("dayofmonth"),
		          dayofyear(col("input")).alias("dayofyear")
		      ).show()
		      ```
- How do you work with timestamps in PySpark?
  id:: 680b085e-373c-41f8-8fc5-f5e63fe857e1
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dffa
		- Get current timestamp:
		      ```python
		      df2.select(current_timestamp().alias("current_timestamp"))
		      ```
		      Convert string to timestamp:
		      ```python
		      to_timestamp(col("input"), "MM-dd-yyyy HH mm ss SSS").alias("to_timestamp")
		      ```
- How do you setup window functions in PySpark?
  id:: 680b085e-672e-4595-94c4-8918ee258477
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dffb
		- Import Window:
		      ```python
		      from pyspark.sql.window import Window
		      ```
		      Define spec:
		      ```python
		      windowSpec = Window.partitionBy("department").orderBy("salary")
		      ```
		      Apply window function:
		      ```python
		      df.withColumn("row_number", row_number().over(windowSpec)).show(truncate=False)
		      ```
- What window ranking functions are available in PySpark?
  id:: 680b085e-6ed2-4e6a-894f-fbdf9bdd7725
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dffc
		- row_number(): assigns unique sequential integers
		      ```python
		      row_number().over(windowSpec)
		      ```
		      rank(): assigns the same number to ties with gaps
		      ```python
		      rank().over(windowSpec)
		      ```
		      dense_rank(): assigns the same number to ties without gaps
		      ```python
		      dense_rank().over(windowSpec)
		      ```
- How do you convert JSON strings to structured data?
  id:: 680b085e-0dbf-4f39-a3de-bc6b9445153d
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dffd
		- Using from_json:
		      ```python
		  from pyspark.sql.functions import from_json
		  df2 = df.withColumn("value", from_json(df.value, MapType(StringType(), StringType())))
		  df2.printSchema()
		  
		  from pyspark.sql import SparkSession
		  from pyspark.sql.functions import from_json, col
		  from pyspark.sql.types import StructType, StructField, StringType, IntegerType
		  
		  # Initialize SparkSession
		  spark = SparkSession.builder.appName("JSONExample").getOrCreate()
		  
		  # Sample JSON data
		  data = [
		      ('{"name": "John", "age": 30, "address": {"city": "NY", "zip": "10001"}}',),
		      ('{"name": "Sarah", "age": 25, "address": {"city": "LA", "zip": "90001"}}',)
		  ]
		  
		  df = spark.createDataFrame(data, ["json_str"])
		  
		  # Define schema for nested JSON
		  schema = StructType([
		      StructField("name", StringType(), True),
		      StructField("age", IntegerType(), True),
		      StructField("address", StructType([
		          StructField("city", StringType(), True),
		          StructField("zip", StringType(), True)
		      ]), True)
		  ])
		  
		  # Parse JSON strings into structured column
		  df_struct = df.withColumn("parsed", from_json(col("json_str"), schema))
		  
		  # Show schema and parsed data
		  df_struct.printSchema()
		  df_struct.show(truncate=False)
		  
		  # Access nested fields using dot notation
		  df_struct.select(
		      col("parsed.name"),
		      col("parsed.age"),
		      col("parsed.address.city"),
		      col("parsed.address.zip")
		  ).show()
		  
		  -----
		  
		  root
		   |-- json_str: string (nullable = true)
		   |-- parsed: struct (nullable = true)
		   |    |-- name: string (nullable = true)
		   |    |-- age: integer (nullable = true)
		   |    |-- address: struct (nullable = true)
		   |    |    |-- city: string (nullable = true)
		   |    |    |-- zip: string (nullable = true)
		  
		  +-------------------------------------------------------------+-------------------------------+
		  |json_str                                                     |parsed                         |
		  +-------------------------------------------------------------+-------------------------------+
		  |{"name": "John", "age": 30, "address": {"city": "NY", "zip":"10001"}} |{John, 30, {NY, 10001}}      |
		  |{"name": "Sarah", "age": 25, "address": {"city": "LA", "zip":"90001"}}|{Sarah, 25, {LA, 90001}}     |
		  +-------------------------------------------------------------+-------------------------------+
		  
		  +-----+---+----+-----+
		  | name|age|city|  zip|
		  +-----+---+----+-----+
		  | John| 30|  NY|10001|
		  |Sarah| 25|  LA|90001|
		  +-----+---+----+-----+
		  
		  ```
- How do you convert structured data to JSON strings?
  id:: 680b085e-646e-40b4-b36e-ed58332c27ef
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dffe
		- Using to_json:
		      ```python
		      from pyspark.sql.functions import to_json, col
		      df2.withColumn("value", to_json(col("value"))).show(truncate=False)
		      ```
- How do you extract fields from JSON strings?
  id:: 680b085e-a58f-4709-8101-4619c980b757
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504dfff
		- Using json_tuple:
		      ```python
		      df.select(
		          col("id"),
		          json_tuple(col("value"), "Zipcode", "ZipCodeType", "City")
		      ).toDF("id", "Zipcode", "ZipCodeType", "City")
		    
		    Limitations: it handles simple json with no nesting .It can only extract top-level fields. 
		    It cannot handle nested JSON structures.
		  
		    data = [
		      (1, '{"zipcode": "90210", "type": "STANDARD", "city": "Beverly Hills"}'),
		      (2, '{"zipcode": "10001", "type": "STANDARD", "city": "New York"}'),
		      (3, '{"zipcode": "60601", "type": "UNIQUE", "city": "Chicago"}')
		  ]
		  
		  columns = ["id", "value"]
		  
		  df = spark.createDataFrame(data, columns)
		  from pyspark.sql.functions import col, json_tuple
		  
		  # Use json_tuple to extract multiple top-level fields
		  df_extracted = df.select(
		      col("id"),
		      json_tuple(col("value"), "zipcode", "type", "city")
		  ).toDF("id", "zipcode", "type", "city")
		  
		  df_extracted.show()
		  
		  ---+-------+--------+-------------+
		  | id|zipcode|    type|         city|
		  +---+-------+--------+-------------+
		  |  1|  90210|STANDARD|Beverly Hills|
		  |  2|  10001|STANDARD|     New York|
		  |  3|  60601|  UNIQUE|      Chicago|
		  +---+-------+--------+-------------+
		  
		  ```
		      Or get_json_object:
		      ```python
		      df.select(
		          col("id"),
		          get_json_object(col("value"), "$.ZipCodeType").alias("ZipCodeType")
		      )
		    
		    --------------------------------------------------------------------------------------------------
		    from pyspark.sql.functions import col, get_json_object, lit
		  
		  # Assuming 'value' is the column containing the JSON string
		  df = spark.createDataFrame([
		      ('{"id": 1, "data": {"zipcode": "90210", "type": "STANDARD", "location": {"city": "Beverly Hills", "state": "CA"}}}',),
		      ('{"id": 2, "data": {"zipcode": "10001", "type": "STANDARD", "location": {"city": "New York", "state": "NY"}}}',)], ['value'])
		  
		  # Extract a nested field using its JSONPath
		  df_city = df.select(
		      get_json_object(col("value"), "$.data.location.city").alias("City"),
		      get_json_object(col("value"), "$.data.zipcode").alias("Zipcode")
		  )
		  
		  df_city.show(truncate=False):
		  ```
- How do you read multiple CSV files with PySpark?
  id:: 680b085e-8af1-4239-aa3c-65d703eaacac
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e000
		- Using comma-separated paths:
		      ```python
		      df = spark.read.csv("path1,path2,path3")
		      ```
- What options are available when reading CSV files?
  id:: 680b085e-5264-4623-a5f2-f3db3a43ad51
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e001
		- ```python
		      spark.read.options(inferSchema='True', delimiter=',').csv("path")
		    
		      spark.read.csv(path, 
		                 header=True,        # First line is header
		                 inferSchema=True,   # Automatically detect column types
		                 sep=',',            # Column delimiter (default ,)
		                 quote='"',          # Quote character for strings
		                 escape='\\',        # Escape character
		                 comment=None,       # Ignore lines starting with this char
		                 nullValue='',       # String to treat as null
		                 mode='PERMISSIVE',  # Handling of malformed rows (PERMISSIVE / DROPMALFORMED / FAILFAST)
		                 encoding='UTF-8',   # File encoding
		                 multiLine=False     # Support multi-line values in a single column
		                )
		  
		  ```
		      ```python
		      spark.read.option("inferSchema", True).option("delimiter", ",").csv("path")
		      ```
		      ```python
		      spark.read.options(header='True', inferSchema='True', delimiter=',').csv("path")
		      ```
- What are the available modes when writing DataFrames to storage?
  id:: 680b088b-2753-40bf-ae33-78348f4d8341
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e002
		- "overwrite" - replaces existing data
		      ```python
		      df.write.mode("overwrite").csv("path")
		      ```
		      "append" - adds data to existing file
		      ```python
		      df.write.mode("append").csv("path")
		      ```
		      "ignore" - does nothing if file exists
		      ```python
		      df.write.mode("ignore").csv("path")
		      ```
		      "error" - default option that returns an error if file exists
		      ```python
		      df.write.mode("error").csv("path")
		      ```
- How do you convert string columns to arrays and vice versa?
  id:: 680b088b-4b3e-48b0-b1bb-b57d1735654e
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e003
		- String to array:
		      ```python
		      df.select(split(col("name"), ",").alias("NameArray")).drop("name")
		      ```
		      Array to string:
		      ```python
		      df.withColumn("languagesAtSchool", concat_ws(",", col("languagesAtSchool")))
		      ```
		- example:
			- ```apl
			  """
			  
			  ### Initial Data
			  
			  Imagine you have a DataFrame with a column `languages` containing a string of programming languages, separated by commas.
			  
			  
			  from pyspark.sql import SparkSession
			  
			  spark = SparkSession.builder.appName("Example").getOrCreate()
			  
			  data = [
			      (1, "Python,Java,C++"),
			      (2, "JavaScript,HTML"),
			      (3, "SQL")
			  ]
			  
			  columns = ["id", "languages"]
			  df = spark.createDataFrame(data, columns)
			  
			  print("Original DataFrame:")
			  df.show()
			  
			  
			  This will produce the following output:
			  
			  
			  +---+----------------+
			  | id|       languages|
			  +---+----------------+
			  |  1| Python,Java,C++|
			  |  2|JavaScript,HTML|
			  |  3|             SQL|
			  +---+----------------+
			  
			  
			  -----
			  
			  ### String to Array
			  
			  To convert the `languages` string column into an array, you use the `split` function.
			  
			  
			  from pyspark.sql.functions import split
			  
			  df_array = df.withColumn("languages_array", split("languages", ","))
			  
			  print("DataFrame with Array Column:")
			  df_array.show()
			  df_array.printSchema()
			  
			  
			  The output will show a new column `languages_array` with the values stored as a list (array), and the schema will confirm the new data type.
			  
			  
			  +---+----------------+--------------------+
			  | id|       languages|     languages_array|
			  +---+----------------+--------------------+
			  |  1| Python,Java,C++|[Python, Java, C++]|
			  |  2|JavaScript,HTML| [JavaScript, HTML]|
			  |  3|             SQL|               [SQL]|
			  +---+----------------+--------------------+
			  
			  root
			   |-- id: long (nullable = true)
			   |-- languages: string (nullable = true)
			   |-- languages_array: array (nullable = true)
			   |    |-- element: string (nullable = true)
			  
			  
			  -----
			  
			  ### Array to String
			  
			  Now, let's take the `languages_array` and convert it back to a delimited string using `concat_ws`.
			  
			  
			  from pyspark.sql.functions import concat_ws, col
			  
			  df_string = df_array.withColumn("languages_string", concat_ws(" | ", col("languages_array")))
			  
			  print("DataFrame with new String Column:")
			  df_string.show(truncate=False)
			  df_string.printSchema()
			  
			  
			  The output will show a new string column, where the elements of the array are joined by the new delimiter `" | "`.
			  
			  
			  +---+----------------+--------------------+----------------------+
			  |id |languages       |languages_array     |languages_string      |
			  +---+----------------+--------------------+----------------------+
			  |1  |Python,Java,C++ |[Python, Java, C++] |Python | Java | C++ |
			  |2  |JavaScript,HTML |[JavaScript, HTML]  |JavaScript | HTML |
			  |3  |SQL             |[SQL]               |SQL                   |
			  +---+----------------+--------------------+----------------------+
			  
			  root
			   |-- id: long (nullable = true)
			   |-- languages: string (nullable = true)
			   |-- languages_array: array (nullable = true)
			   |    |-- element: string (nullable = true)
			   |-- languages_string: string (nullable = true)
			  
			  
			  """
			  ```
- How can you use the expr() function for filtering?
  id:: 680b088b-51ae-48ba-ac5d-eb17bf15f641
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e004
		- ```python
		      df.filter(expr("col1 == col2")).show()
		      ```
		      This allows SQL-like expressions within DataFrame operations.
- What is the syntax for lit() ?
  id:: 680b088b-5ed9-43d3-a230-d98cd18f6a73
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e005
		- lit() handles simple values:
		      ```python
		      df.withColumn("status", lit("Active"))
		      ```
- How do you work with timestamps in DataFrame operations?
  id:: 680b088b-1cd3-4d36-b04e-bd70b5d178d6
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e006
		- Convert string to timestamp:
		      ```python
		      df.withColumn("timestamp", to_timestamp("input_timestamp")).show(truncate=False)
		      ```
		      Get current date/time:
		      ```python
		      df.select(
		          current_date().alias("current_date"),
		          date_format(current_timestamp(), "yyyy MM dd").alias("yyyy MM dd")
		      ).show()
		      ```
- How do you implement conditional logic with the expr() function?
  id:: 680b088b-6c48-41ae-b9c0-f8124334761f
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e007
		- ```python
		      df3 = df.withColumn("new_gender", expr("""
		          CASE 
		              WHEN gender = 'M' THEN 'Male' 
		              WHEN gender = 'F' THEN 'Female' 
		              WHEN gender IS NULL THEN '' 
		              ELSE gender 
		          END
		      """))
		      ```
- How do you integrate SQL expressions with DataFrame operations?
  id:: 680b088b-ff70-4b2b-a28c-74ae3963705a
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e008
		- Create temporary view:
		      ```python
		      df.createOrReplaceTempView("PERSON")
		      ```
		      Execute SQL query:
		      ```python
		      spark.sql("select SPLIT(name, ',') as NameArray from PERSON").show()
		      ```
- How do you extract substrings from DataFrame columns?
  id:: 680b088b-2ce7-44b5-8f53-2f1ac2d5e5b6
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e009
		- Using substring:
		      ```python
		      df.withColumn('year', substring('date', 1, 4)) \
		        .withColumn('month', substring('date', 5, 2)) \
		        .withColumn('day', substring('date', 7, 2))
		      ```
- How do you replace characters in string columns?
  id:: 680b088b-29a4-4db5-bd49-d690ed9fed08
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e00a
		- Using translate:
		      ```python
		   #The translate() function performs "character-by-character" substitution according to a mapping:
		      df.withColumn('address', translate('address', '123', 'ABC')).show(truncate=False)
		   
		  data = [("abcdefg",), ("1234567",)]
		  df = spark.createDataFrame(data, ["value"])
		   
		   result = df.select(
		  	col("value"),
		  	overlay(col("value"), "XXX", 3, 2).alias("overlayed"),
		  	translate(col("value"), "abcd123", "ABCD@#$").alias("translated")
		  )
		  
		  +-------+---------+----------+
		  |  value| overlayed|translated|
		  +-------+---------+----------+
		  |abcdefg|abXXXefg |ABCDefg   |
		  |1234567|12XXX567 |@#$4567   |
		  +-------+---------+----------+
		      ```
- How do you apply regular expressions to DataFrame columns?
  id:: 680b088b-4570-4ea4-9fbb-328977786e48
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e00b
		- Using :
		      ```python
		  df.withColumn("new_column", expr("regexp_replace(col1, col2, col3)").alias("replaced_value")).show()
		  regexp_extract: Extracts a specific pattern from a string
		  regexp_replace: Replaces matches of a pattern with a replacement string
		  rlike / regexp: Filters rows based on a regex pattern
		  regexp_extract_all: Extracts all occurrences of a pattern (available in newer Spark versions)
		  ```
- How do you create map-type columns from existing columns?
  id:: 680b088b-f19f-4f87-bc49-7e66de124418
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e00c
		- Using create_map:
		      ```python
		      df.withColumn("propertiesMap", create_map(
		          lit("salary"), col("salary"),
		          lit("location"), col("location")
		      )).drop("salary", "location")
		   
		  Original DataFrame:
		  +-------+------+-------------+
		  |   name|salary|     location|
		  +-------+------+-------------+
		  |   John| 85000|     New York|
		  |  Sarah| 92000|San Francisco|
		  |Michael| 78000|      Chicago|
		  |   Emma|105000|      Seattle|
		  |  David| 67000|       Austin|
		  +-------+------+-------------+
		  
		  After converting to map:
		  +-------+--------------------------------------------+
		  |name   |propertiesMap                               |
		  +-------+--------------------------------------------+
		  |John   |{salary -> 85000, location -> New York}     |
		  |Sarah  |{salary -> 92000, location -> San Francisco}|
		  |Michael|{salary -> 78000, location -> Chicago}      |
		  |Emma   |{salary -> 105000, location -> Seattle}     |
		  |David  |{salary -> 67000, location -> Austin}  
		  
		  Note: Explicit schema helps Spark avoid schema inference overhead.
		  from pyspark.sql.types import StructType, StructField, StringType, MapType
		  #Keep all values as StringType (simplest)
		  schema = StructType([
		      StructField("name", StringType(), True),
		      StructField("propertiesMap", MapType(StringType(), StringType()), True)
		  ])
		  
		  
		  If you already have a DataFrame and want to combine a few columns into a map:
		  → Use create_map().
		  
		  If you’re reading from an external source that naturally has map-like data:
		  → Use MapType in schema.
		  ```
- How do you access keys and values in map-type columns?
  id:: 680b088b-0298-47df-9775-79e4f0ef1982
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e00d
		- Get keys:
		      ```python
		      df.select(df.id,explode(map_keys(df.properties))).distinct()
		   
		  ```
		      Get values:
		      ```python
		      df.select(df.id, explode(map_values(df.properties)).alias("property_value"))
		  ```
- How do you overlay one string on another at a specific position?
  id:: 680b088b-69ea-46c2-9b3f-91058dc14674
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e00e
		- Using overlay function:
		      ```python
		      overlay() =>  function replaces a substring at a specified position with another string:   overlay(source, replacement, position[, length])
		   translate() ==> Replaces individual characters throughout the string
		  df.select(overlay("original", "replacement", 3, 4).alias("overlayed"))
		  
		  data = [("abcdefg",), ("1234567",)]
		  df = spark.createDataFrame(data, ["value"])
		   
		   result = df.select(
		  	col("value"),
		  	overlay(col("value"), "XXX", 3, 2).alias("overlayed"),
		  	translate(col("value"), "abcd123", "ABCD@#$").alias("translated")
		  )
		  
		  +-------+---------+----------+
		  |  value| overlayed|translated|
		  +-------+---------+----------+
		  |abcdefg|abXXXefg |ABCDefg   |
		  |1234567|12XXX567 |@#$4567   |
		  +-------+---------+----------+
		  For "abcdefg":
		  
		  Overlay: Replaces 2 characters starting at position 3 → "abXXXefg" (replaces "cd" with "XXX")
		  Translate: Maps a→A, b→B, c→C, d→D → "ABCDefg" (other characters unchanged)
		  
		  
		  For "1234567":
		  
		  Overlay: Replaces 2 characters starting at position 3 → "12XXX567" (replaces "34" with "XXX")
		  Translate: Maps 1→@, 2→#, 3→$ → "@#$4567" (other characters unchanged)
		      ```
- How do you write data to CSV files with PySpark?
  id:: 680b088b-93ff-464f-b22f-b7ee750e5c70
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e00f
		- ```python
		      df2.write.format("csv").mode('overwrite').save("/tmp/spark_output/zipcodes")
		      ```
- How do you explode nested array structures?
  id:: 680b088b-d2cc-4ffc-aa17-9c02bf47eee0
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e010
		- Use explode to handle arrays of arrays:
		      ```python
		      df.select(explode("nested_column").alias("inner_array"))
		      ```
- expr vs selectExpr in Spark (syntax examples)
  id:: 68104c77-b73c-4219-a978-02713c316ff0
	- #card
	  id:: 681176f4-7e12-42c1-b44b-1e3dd504e011
		- expr creates a Column object:
		      ```python
		      df.select("name", expr("age + 1 as age_plus_one"))
		      df.withColumn("salary_increased", expr("salary * 1.1"))
		      df.filter(expr("age > 30"))
		      ```
		      
		      selectExpr is a complete DataFrame operation that directly returns a new DataFrame:
		      ```python
		      df.selectExpr("name", "age + 1 as age_plus_one")
		      df.selectExpr("salary * 1.1 as salary_increased")
		      df.selectExpr("CASE WHEN age > 40 THEN 'Senior' ELSE 'Junior' END as level")
		      ```
- load a array to dict ()
	- #card
	  id:: 6813b643-b9b4-4a4a-b2f0-f8a3cf26c08b
		- using counter 
		      ```python
		      from collections import Counter
		   count = Counter(nums)
		      ```