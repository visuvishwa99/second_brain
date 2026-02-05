TARGET DECK: SecondBrain::06_Ingestion

START
Cloze
{AWS Glue} is a fully managed cloud-optimized {ETL} service on AWS.
<!--ID: 1770332399706-->
END

START
Cloze
A {Glue Crawler} scans data in S3, creates schema, and populates the {Glue Data Catalog}.
<!--ID: 1770332399708-->
END

START
Cloze
The Glue Data Catalog stores only {table definitions}; original data stays in {S3}.
<!--ID: 1770332399710-->
END

START
Cloze
A {DynamicFrame} in AWS Glue is similar to a {DataFrame} but with additional ETL capabilities.
<!--ID: 1770332399712-->
END

START
Cloze
{ResolveChoice} transformation is used to handle {ambiguous columns} with multiple data types.
<!--ID: 1770332399714-->
END

START
Cloze
{Pushdown Predicates} optimize memory by filtering data closer to the {source} using partition columns.
<!--ID: 1770332399716-->
END

START
Cloze
For parallel reads in Glue, use {hashfield} and {hashpartitions} in connection options.
<!--ID: 1770332399718-->
END

START
Cloze
Glue worker types are measured in {DPU} (Data Processing Unit). G.1X = {1 DPU} with 4 vCPUs and 16 GB memory.
<!--ID: 1770332399719-->
END

START
Cloze
When reading more than 50000 files, use {groupFiles} and {groupSize} options to control parallelism and prevent driver OOM.
<!--ID: 1770332399722-->
END

START
Cloze
{Job Bookmarks} in AWS Glue persist state information to enable {incremental processing} instead of full loads.
<!--ID: 1770332399724-->
END

START
Cloze
The {FLEX} execution class in Glue is for non-time-critical jobs and offers {cost savings} by using spare capacity.
<!--ID: 1770332399726-->
END

START
Cloze
To reset a job bookmark use aws glue {reset-job-bookmark} with job-name and run-id parameters.
<!--ID: 1770332399728-->
END
