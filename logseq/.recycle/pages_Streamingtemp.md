- [[spark streaming]]
- [[Streaming Aggregates and State Store]] ^663d6cc9-ae7f-4bb0-ba84-3ff0223b0e6f
  collapsed:: true
	- Syntax  => outputMode("complete")
	  ```python
	  def saveResults(self, results_df):
	  print(f"\nStarting Silver Stream...", end=**)
	  return (results_df.writestream
	        queryName ("gold-update")
	        option ("checkpointLocation", f"(self.base_data_dir)/chekpoint/customer _rewards")
	        outputMode("complete")
	        toTable(" customer_ rewards")
	  print ("Done")
	  ```
	  ![image.png](../assets/image_1715303229659_0.png)
- [[Incremental Aggregates and Update Mode]]
  collapsed:: true
	- syntax => Need to use   .outputMode ("update").foreachBatch(self.upsert) ^663dcba4-f021-40bf-a1a0-0e9a9d6156a4
	  #+BEGIN_NOTE
	  upsert = merge + insert 
	  #+END_NOTE
		- ```python
		  def upsert(self, rewards_df, batch_id):
		  rewards_df.createorReplacetempview("customer_ rewards_df.
		  _temp_view")
		  
		  merge_statement = "''MERGE INTO customer_rewards t
		  USING customer_rewards_df
		  _temp_view s
		  ON s. CustomerCardNo == t. CustomerCardNo
		  WHEN MATCHED THEN
		  UPDATE SET t. TotalAmount = s. TotalAmount, t. TotalPoints = s. TotalPoints
		  WHEN NOT MATCHED THEN
		  INSERT *
		  rewards_af.jaf.sparkSession () - sql (merge_ statement)|
		  
		  
		  def saveResults(self, results_df):
		  print(f" (nstarting Silver Stream...", end="')
		  return (results_df writestream
		          .queryName ("gold-update")
		          .option ("checkpointLocation", f"(self.base_data_dir}/chekpoint/customer_rewards*)
		          .outputMode ("update")
		          .foreachBatch(self.upsert)
		          .start()
		  print ("Done")
		  ```
- [[sparkstreaming QA]]
  id:: 663d8712-a5e6-4cfa-b6f0-336db1aab077
  collapsed:: true
	- logseq.order-list-type:: number
	  id:: 663d7c96-d778-4a77-80ce-b2873f34c100
	  deck:: [[sparkstreaming QA]] 
	  syntax of outputmode complete/ Streaming Aggregates and State Store :->{{outputMode("complete")}}
	- logseq.order-list-type:: number
	  id:: 663dcba4-b33b-434f-83e3-f2e4be0eebf9
	  deck:: [[sparkstreaming QA]] 
	  syntax of outputmode update / Incremental Aggregates and Update Mode :->{{outputMode("update").foreachBatch(upsert)}}
	- logseq.order-list-type:: number
-
