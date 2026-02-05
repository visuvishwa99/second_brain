---
tags:
  - compute
---

# Spark Concepts & QA

## Why Spark?
* **Iterative Algorithm** support (great for ML).
* **In-Memory Processing**: Faster than disk-based map-reduce.
* **Near real-time** data processing capabilities.
* **Rich and Simple API**: Available in Python, Scala, SQL, Java.

## DAG Scheduler & Spark Job
* **Spark Application**: Uses APIs to create a series of transformations (map, filter, join).
* **RDD Lineage**: Each transformation generates a new RDD linked to its parent, forming a Directed Acyclic Graph (DAG).
* **Execution**: Actions (e.g., `collect`, `count`) trigger the submission of the lineage to the DAG Scheduler.
* **Encapsulation**:
    * **Stages**: Scheduler divides the optimized DAG into stages based on shuffle boundaries.
    * **Tasks**: For each stage, tasks are generated to run on workers.
    * **Recovery**: Scheduler tracks tasks and reschedules failures using RDD lineage.
* **Optimizations**: Caching, Partition Coalescing, Broadcast Variables.

## Core Concepts

### Stages
* Spark creates a new **Stage** whenever data needs to be **shuffled**.
* **Shuffle Indicators**: `groupByKey`, `reduceByKey`, `join`, `repartition`, `coalesce`.

### Transformations (Lazy)
Transformations define a new RDD/DataFrame but execute nothing until an Action is called.
* **Narrow Transformation**: Computed independently per partition (No Shuffle).
    * Examples: `map`, `filter`, `union`.
* **Wide Transformation**: Requires partitions to be exchanged across the cluster (Shuffle).
    * Examples: `reduceByKey`, `groupByKey`.
* **reduceByKey vs groupByKey**:
    * `reduceByKey`: Performs **Map-side combine** (efficient).
    * `groupByKey`: No Map-side combine (expensive, potential OOM).

### Actions (Eager)
Triggers the execution of the physical plan.
* Examples: `count`, `collect`, `show`, `save`.

## Partitioning & Shuffling
* **coalesce**: Reduces number of partitions. **No Shuffle** (minimizes movement). Use for decreasing partitions.
* **repartition**: Increases/Decreases partitions. **Full Shuffle**. Use for increasing partitions or balancing.
* **Broadcast Join**: Optimizes join of Large DF with Small DF by sending the small copy to all nodes (avoids shuffle).
* **Preferred Locations**: Spark schedules tasks where data resides (Data Locality).

## Modern Spark Features (3.4, 3.5, 4.0)
*   **Spark Connect**: Decoupled client-server architecture allowing lightweight local clients (IDEs) to run Spark code against remote clusters.
*   **Python UDTFs**: User Defined Table Functions allow returning multiple rows/tables from a single Python function.
    ```python
    @udtf(returnType="word: string")
    class WordSplitter:
        def eval(self, text: str):
            for word in text.split(" "):
                yield (word,)
    ```
*   **Native XML Support**: `spark.read.xml()` is now built-in (replacing external spark-xml library).
*   **Protobuf Support**: Native handling of Protobuf serialization.
*   **Parameterized SQL**: Prevents SQL injection and simplifies dynamic queries.
    ```python
    spark.sql("SELECT * FROM tables WHERE id > :id", args={"id": 10})
    ```
*   **TimestampNTZ**: First-class support for Timestamps without Timezones.

---

## PySpark Syntax Cookbook

### 1. Creating DataFrames
**From Lists/Dictionaries**:
```python
data = [("John", 30), ("Alice", 25)]
df = spark.createDataFrame(data, ["Name", "Age"])
```

**Complex Nested Schema**:
```python
from pyspark.sql.types import *
schema = StructType([
    StructField('name', StringType(), True),
    StructField('properties', MapType(StringType(), StringType()), True),
    StructField('history', ArrayType(IntegerType()), True)
])
```

### 2. Columns & Expressions
**Select & Expr**:
```python
# Dot notation vs Col vs Expr
df.select(df.name)
df.select(col("name"))
df.selectExpr("name", "age + 1 as new_age")
```

**Conditional Logic (Case When)**:
```python
from pyspark.sql.functions import when
df.withColumn("category", 
    when(col("age") < 18, "Child")
    .when(col("age") < 65, "Adult")
    .otherwise("Senior")
)
```

**Casting**:
```python
df.select(col("id").cast("int"), col("salary").cast("decimal(10,2)"))
```

### 3. Filtering & Null Handling
**String Pattern Matching**:
```python
df.filter(col("name").startswith("T"))
df.filter(col("name").endswith("son"))
df.filter(col("name").contains("John"))
df.filter(col("name").rlike("(?i)^A")) # Regex
```

**Nulls**:
```python
# Filter Nulls
df.filter(col("id").isNull())
df.filter(col("id").isNotNull())

# Fill Nulls
df.na.fill(0) # All numeric columns
df.na.fill("Unknown", subset=["name", "city"])
```

### 4. Complex Types (Arrays & Maps)
**Array Operations**:
```python
from pyspark.sql.functions import size, array_contains, explode, split

# Check existence
df.filter(array_contains(col("languages"), "Java"))

# Split String to Array
df.withColumn("tags_arr", split(col("tags_str"), ","))
```

**Flatten vs Explode**:
| Function | Input | Output | Usage |
|---|---|---|---|
| `explode()` | Array/Map | Multiple Rows | Unnesting valid lists (drops nulls) |
| `explode_outer()` | Array/Map | Multiple Rows | Unnesting (keeps nulls) |
| `flatten()` | Array of Arrays | Single Array | Merging nested lists `[[1,2],[3]]` -> `[1,2,3]` |

### 5. Aggregations & Windowing
**Multi-Agg**:
```python
df.groupBy("dept").agg(
    sum("salary").alias("total"),
    avg("salary").alias("avg"),
    max("bonus").alias("max_bonus")
)
```

**Pivot/Unpivot**:
```python
# Pivot: Rows -> Cols
df.groupBy("product").pivot("country").sum("sales")

# Unpivot: Cols -> Rows (Stack)
df.selectExpr("product", "stack(3, 'USA', sales_usa, 'UK', sales_uk, 'CA', sales_ca) as (country, sales)")
```

**Window Functions**:
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank

w = Window.partitionBy("dept").orderBy(col("salary").desc())
df.withColumn("rank", rank().over(w))
```

### 6. DataFrame vs RDD Operations
**Map vs FlatMap (RDD)**:
*   `map()`: 1 Input -> 1 Output (e.g., lowercase string).
*   `flatMap()`: 1 Input -> N Outputs (e.g., split sentence into words).

**Pandas Conversion (Arrow Optimized)**:
```python
spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", "true")
pandas_df = df.toPandas()
```

### 7. Join Types
```python
df1.join(df2, df1.id == df2.id, "left") # inner, outer, left, right, anti, semi
```
*   **Left Anti**: Rows in df1 that are NOT in df2.
*   **Left Semi**: Rows in df1 that ARE in df2 (but only columns from df1).

### 8. Handling Duplicates
```python
df.distinct() # All columns
df.dropDuplicates(["id", "date"]) # Specific subset
```

### 9. Writing Data (Best Practices)
**Partitioning & Bucketing**:
```python
df.write.partitionBy("date").parquet("/data/sales")
df.write.bucketBy(10, "id").saveAsTable("bucketed_table")
```

**Controlling File Size**:
```python
# Repartition before write to control file count
df.repartition(10).write...
# Max records
df.write.option("maxRecordsPerFile", 10000)...
```