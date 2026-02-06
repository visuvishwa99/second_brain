TARGET DECK: SecondBrain::06_Ingestion

START
Cloze
{AWS Glue} is a fully managed cloud-optimized {ETL} service on AWS.
<!--ID: 1770353415920-->
END

START
Cloze
A {Glue Crawler} scans data in S3, creates schema, and populates the {Glue Data Catalog}.
<!--ID: 1770353415922-->
END

START
Cloze
The Glue Data Catalog stores only {table definitions}; original data stays in {S3}.
<!--ID: 1770353415924-->
END

START
Cloze
A {DynamicFrame} in AWS Glue is similar to a {DataFrame} but with additional ETL capabilities.
<!--ID: 1770353415926-->
END

START
Cloze
{ResolveChoice} transformation is used to handle {ambiguous columns} with multiple data types.
<!--ID: 1770353415927-->
END

START
Cloze
{Pushdown Predicates} optimize memory by filtering data closer to the {source} using partition columns.
<!--ID: 1770353415929-->
END

START
Cloze
For parallel reads in Glue, use {hashfield} and {hashpartitions} in connection options.
<!--ID: 1770353415931-->
END

START
Cloze
Glue worker types are measured in {DPU} (Data Processing Unit). G.1X = {1 DPU} with 4 vCPUs and 16 GB memory.
<!--ID: 1770353415932-->
END

START
Cloze
When reading more than 50000 files, use {groupFiles} and {groupSize} options to control parallelism and prevent driver OOM.
<!--ID: 1770353415934-->
END

START
Cloze
{Job Bookmarks} in AWS Glue persist state information to enable {incremental processing} instead of full loads.
<!--ID: 1770353415937-->
END

START
Cloze
The {FLEX} execution class in Glue is for non-time-critical jobs and offers {cost savings} by using spare capacity.
<!--ID: 1770353415939-->
END

START
Cloze
To reset a job bookmark use aws glue {reset-job-bookmark} with job-name and run-id parameters.
<!--ID: 1770353415943-->
END
