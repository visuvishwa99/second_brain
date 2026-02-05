---
tags:
  - warehousing
---

# Amazon Redshift

## Overview
*   **Type**: Massively Parallel Processing (MPP) cloud data warehouse.
*   **Provider**: AWS.
*   **Use Case**: Large-scale analytics, BI workloads.

## Supported Storage Types
*   **Data Warehouse**: Star & Snowflake Schema.
*   **Data Mart**: Department-specific subsets.
*   **Lakehouse**: Data Warehouse + Data Lake (via Redshift Spectrum).

## Client Tools
*   MySQL Workbench
*   3rd Party BI Tools (Tableau, MicroStrategy)
*   Amazon QuickSight

## Redshift Serverless
*   No cluster management required.
*   Auto-scaling compute.
*   Pay-per-query pricing.

## Core Functionality
*   ELT-focused (Transformation inside the warehouse).
*   Integration with S3 (COPY, UNLOAD).
*   Concurrency Scaling for burst workloads.

### Related
- [[snowflake]]
- [[bigquery]]
- [[athena]]
