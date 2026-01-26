- Athena -> Amazon Athena is a query service that makes it easy to analyze data directly
  collapsed:: true
  S3 using standard SQL
	- Athena is not database or not data warehouse
	- For very small queries (processing less than 10 MB), you'll still be billed for 10 MB
- To run Amazon Athena queries on data stored in Amazon S3, follow these steps:
  collapsed:: true
	- Ensure your data is stored in S3 in a supported format (e.g., CSV, JSON, Parquet, ORC)
	- Create a database in Athena if you haven't already.
	- Open the Athena console in AWS.
	- Query Editor, write your SQL query to analyze the data in your S3-backed table.
	-
- Optimization and Cost
  collapsed:: true
	- Amazon Athena (Query Performance & Cost Efficiency)
	- Partitioning and Bucketing for Faster Queries – Use CREATE TABLE WITH PARTITION to avoid full-table scans and improve query efficiency.
	- Leverage Result Caching – Enable Athena query caching to speed up recurring queries and reduce costs.
	- Optimize Join Performance with Smaller Data Loads – Reduce JOIN complexity by pre-aggregating large datasets in Glue before querying in Athena.
	- Use Compression & Columnar Storage – Athena reads Parquet and ORC much faster than CSV, reducing query execution time and cost.
	- Precompute Aggregations in DBT or Glue – Instead of running expensive aggregations in Athena, use DBT models or Glue ETL jobs to precompute and store summaries in S3.
