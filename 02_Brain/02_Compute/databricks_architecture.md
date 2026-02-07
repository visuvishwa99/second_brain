---
created_at: 2026-02-07 16:10
tags:
  -compute
source: 01_Raw/journals/2026-02-07_09-58-56.md
---

# Databricks Architecture Overview

The Databricks platform architecture is structured into four key layers, designed to unify governance, semantics, performance, and consumption. This "one semantic layer, many access points" philosophy ensures consistent data definitions across diverse analytical workloads.

## 1. Foundation Layer: Unity Catalog
At the base lies the **Unity Catalog**, the core semantic layer responsible for centralized governance across the entire platform.
*   **Governance**: Defines who can access what data.
*   **Security**: Implements Row Level Security (RLS) and Column Level Masking.
*   **Sharing**: Facilitates secure data sharing via Delta Sharing.
*   **Management**: Handles permissions for data, AI models (DAB), and APIs.

## 2. Semantic Layer
Built on top of the Unity Catalog, this layer focuses on defining business metrics and logic once, to be reused everywhere.
*   **Reusable KPIs**: Metric definitions stored in Unity Catalog.
*   **Materialized Views**: Pre-computed views that automatically update, ensuring consistency and performance.
*   **Logic Centralization**: Prevents "metric drift" where different teams calculate the same KPI differently.

## 3. Accelerators (Performance & AI)
This layer enhances the speed and capability of the platform.
*   **Lakehouse Performance**: Features like **Lakebase** and **Synced Tables** provide low-latency reads, time travel (PITR), and compute-store separation.
*   **Vector Search**: Optimized for AI/RAG workloads.
*   **Agent Bricks & MCP**: Tools for building governed AI agents and model serving, integrated with Unity Catalog for security.

## 4. Consumption Layer
The top layer provides three primary interfaces for users to interact with data, all governed by the underlying layers.
1.  **AI/BI Dashboards**: Interactive, AI-assisted BI tools that allow users to visualize governed data. Supports external embedding.
2.  **Genie**: A conversational analytics tool that translates natural language into SQL. It uses a "knowledge store" to understand business context and provide trusted answers.
3.  **Databricks Apps**: A bespoke application environment for custom data apps, fully integrated with OAuth/OBO authentication and platform observability.

## Code Example: Defining a Governed Table in Unity Catalog

This SQL example demonstrates creating a table within Unity Catalog, applying a row filter for governance.

```sql
-- Create a catalog and schema if they don't exist
CREATE CATALOG IF NOT EXISTS investments;
CREATE SCHEMA IF NOT EXISTS investments.gold;

-- Create a governed table in Unity Catalog
CREATE TABLE IF NOT EXISTS investments.gold.portfolio_performance (
    portfolio_id STRING,
    customer_id STRING,
    total_value DECIMAL(18, 2),
    performance_pct DECIMAL(5, 2),
    last_updated TIMESTAMP
)
USING DELTA
COMMENT 'Daily performance metrics for customer portfolios';

-- Create a Row Filter function
CREATE OR REPLACE FUNCTION investments.gold.filter_by_region(region_col STRING)
RETURN IF(is_account_group_member('admin'), true, region_col = 'US');

-- Apply Row Level Security (RLS) to the table
ALTER TABLE investments.gold.portfolio_performance
SET ROW FILTER investments.gold.filter_by_region ON (customer_id);

-- Grant access to specific groups
GRANT SELECT ON TABLE investments.gold.portfolio_performance TO `data_analysts`;
```
