---
tags:
  - level3
---

# Streaming Patterns

## Statefull (S).md

- Statefull  Transformation  -> spark is maintaining/storing  the results . pass the results across the micro batches.
- ![image.png](../assets/image_1740418453707_0.png)
- [[OM:complete]]
- [[OM:update]] ^66426678-bb23-4917-8c31-cc691886f82b
  collapsed:: true
	- statefull aggregations
		- ![image.png](../assets/image_1715630652570_0.png)
-


---

## Stateless (S).md

filters:: {"sparkstreaming" true}

- Stateless Transformation -> No need to store the state of results . so there are stateless
- Full load actually fails due to memory issues we implement full with following 
  [[OM:append]]
- **Implementation of aggregation without using statestore** : Instead of taking results from "state store" we take those results from already exist target query and rewrite the merge statement .
	- We are removing rockdb config.
	-
	- ```python
	  def aggregate_upsert(self, invoices_df, batch_id):
	  rewards_df = self.getAggregates(invoices_df)
	  rewards_df .create0rReplaceTempview("customer_rewards_df_temp_view")
	  merge_statement = "*'*MERGE INTO customer_rewards t
	      USING customer_rewards_df.
	      _temp_view s
	      ON s. CustomerCardNo == t.CustomerCardNo
	      WHEN MATCHED THEN
	      UPDATE SET t. TotalAmount = s. TotalAmount + t. TotalAmount,
	      t. TotalPoints = s. Totalpoints + t. TotalPoints
	  WHEN NOT MATCHED THEN
	  INSERT *
	  invoices_df._jdf.sparkSession() .sql (merge_statement)
	  
	  def saveResults(self, results_df):
	  print(f"\nStarting Silver Stream...
	  , end="')
	  return (results_df.writestream
	            .queryName ("gold-update")
	            •option("checkpointLocation", f"{self.base_data_dir}/chekpoint/customer_rewards*)
	            •outputMode("update")
	            • foreachBatch(self.aggregate_upsert)
	            • start()
	  Tewaras
	  ```
- Filtering out invalid records, removing duplicates, handling null values
- select(), filter(), map(), flatMap(), explode(), etc.
- It does not support Complete output mode because they do not maintain state.
- Few more Examples ->
	- Data Cleansing:** Filtering out invalid records, removing duplicates, handling null values
	- **Data Enrichment:** Joining streaming data with static lookup tables to add additional context.
	- **Simple Aggregations:**  Counting the number of events within each micro-batch.


---

