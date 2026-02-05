---
tags:
  - warehousing
---

# Slowly Changing Dimensions (SCD)

- **Definition**: Data warehousing techniques used to manage and track changes in dimensional data over time. They ensure reporting accuracy and enable historical analysis.

- ## Core SCD Types
    - ### 1. SCD Type 1: Overwrite (No History)
        - **Logic**: The old value is simply replaced by the new value.
        - **Use Case**: Corrections, or when history is irrelevant (e.g., correcting a spelling mistake in a Name).
        - **Pros**: Simple, saves space.
        - **Cons**: History is lost forever.
        - | Customer ID | Name | Address |
          |---|---|---|
          | 1001 | John | 456 Oak Ave (Old was 123 Main) |
        - **Databricks SQL Implementation**:
          ```sql
          MERGE INTO dim_customer AS target
          USING updates AS source
          ON target.customer_id = source.customer_id
          WHEN MATCHED THEN
           UPDATE SET target.address = source.address;
          ```
    - ### 2. SCD Type 2: Row Versioning (Full History)
        - **Logic**: A new row is inserted for every change. Old rows are marked as expired.
        - **Use Case**: Tracking address changes, role changes, price history.
        - **Columns Needed**: `start_date`, `end_date`, `is_current`.
        - | Customer ID | Address | Start Date | End Date | Is_Current |
          |---|---|---|---|---|
          | 1001 | 123 Main St | 2020-01-01 | 2025-02-15 | false |
          | 1001 | 456 Oak Ave | 2025-02-16 | NULL | true |
        - **Databricks SQL Implementation**:
          ```sql
          MERGE INTO dim_customer AS target
          USING updates AS source
          ON target.customer_id = source.customer_id AND target.is_current = TRUE
          WHEN MATCHED THEN
           UPDATE SET target.is_current = FALSE, target.end_date = current_date()
          WHEN NOT MATCHED THEN
           INSERT (customer_id, name, address, start_date, end_date, is_current)
           VALUES (source.customer_id, source.name, source.address, current_date(), NULL, TRUE);
          ```
    - ### 3. SCD Type 3: Previous Value Column (Limited History)
        - **Logic**: Add a column for the *previous* value. Tracks only the immediate last change.
        - **Use Case**: When you only need "Current" vs "Previous" state (e.g., Re-orgs).
        - | Customer ID | Previous Address | Current Address |
          |---|---|---|
          | 1001 | 123 Main St | 456 Oak Ave |
        - **Databricks SQL Implementation**:
          ```sql
          MERGE INTO dim_customer AS target
          USING updates AS source
          ON target.customer_id = source.customer_id
          WHEN MATCHED THEN
           UPDATE SET
           target.previous_address = target.current_address,
           target.current_address = source.current_address,
           target.change_date = current_date();
          ```

- ## Advanced Patterns
    - ### Late Arriving Dimensions (LAD)
        - **Scenario**: Fact data (Sales) arrives *before* the Dimension data (New Customer).
        - **Problem**: The Foreign Key in Fact table would fail or look up NULL.
        - **Solution**:
            1. **Insert Placeholder**: Create a dummy row in Dimension table (`ID=99, Name='Unknown'`).
            2. **Backfill**: When real Customer data arrives, UPDATE the placeholder row.
        - **Step 1: Insert Placeholder**
          ```sql
          INSERT INTO dim_customer (customer_id, name, address)
          SELECT DISTINCT f.customer_id, 'Unknown', 'Unknown'
          FROM fact_sales f
          WHERE f.customer_id NOT IN (SELECT customer_id FROM dim_customer);
          ```
        - **Step 2: Backfill (Merge Update)**
          ```sql
          MERGE INTO dim_customer AS target
          USING updates AS source
          ON target.customer_id = source.customer_id
          WHEN MATCHED AND target.name = 'Unknown' THEN
           UPDATE SET
           target.name = source.name,
           target.address = source.address;
          ```

- ## SCD in Medallion Architecture
    - | Layer | SCD Type | Purpose | Time Travel Use |
      |---|---|---|---|
      | **Bronze** | None | Raw ingestion (Append only or Overwrite partition). | Debugging, Replay |
      | **Silver** | Type 1 or 2 | Cleaned, modeled data. Business logic applied here. | Debugging, Replay |
      | **Gold** | Type 1 or 3 | Aggregated for BI. Often flattened for performance. | Rarely used |

- ### Related
    - [[dimensional_modeling]]
    - [[databricks]]
    - [[snowflake]]
    - [[data_merging_strategies]]
