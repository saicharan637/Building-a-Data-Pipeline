## Building-a-Data-Pipeline
Utilized Lambda Architecture and created a data pipeline on AWS to make analysis on a Permanent magnet synchronous motor(PMSM) dataset which is taken from Kaggle. The data of a PMSM machine is uploaded into an input source(S3 bucket) batch-wise and a lambda function is used as a trigger to insert the data into a DynamoDB Table. Once the data is uploaded into DynamoDB, the DynamoDB stream is activated to stream the data through Amazon kinesis. The data from Kinesis is now delivered by a delivery stream called Kinesis Data Firehose to an S3 Bucket. Another lambda function is now used as a trigger to deliver the data to S3 through the Firehose, whenever new data is inserted into the DynamoDB Table. The Data from S3 bucket is further crawled using AWS Glue Crawler for it to be available for querying in AWS Athena. The Data crawled from S3 is then stored in Glue Data Catalog and is now accessible for querying by AWS Athena. The data queried in Athena is finally visualized in AWS Quick Sight.

## Architecture:

![img](https://user-images.githubusercontent.com/22254732/119434254-65fff680-bcdd-11eb-93d4-f6ac640378ac.png)
