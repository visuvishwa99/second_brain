- ULAD (Mongo , Denormalized single document)==> Raw table ==> Raw+  (name: **loanevalutionrequest**,s3,parquet file ,  Document )  ==> BYOL job/aws statemachine/
  spark on EMR 
  --> 18 tables (s3/enhanced staging)  ==> EDP job/aws statemachine/ spark
  on EMR --> 1) Glue 2) R&D Team [[Snowflake]]
