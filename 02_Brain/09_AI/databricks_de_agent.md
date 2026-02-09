---
created_at: 2026-02-09
tags: 
  - ai
---

# Databricks Data Engineering Agent

The **Data Engineering Agent** is a specialized capability within Databricks Assistant (Agent Mode) designed to autonomously plan, build, and fix data pipelines. It specifically targets **Lakeflow Pipelines** and Spark Declarative Pipelines (SDP).

## Core Concept
Unlike a standard chat assistant that answers questions, the DE Agent is an **autonomous partner** that can:
1.  **Plan**: Break down complex requests into multi-step plans.
2.  **Execute**: Run code, edit multiple files, and search tables.
3.  **Iterate**: Analyze errors or output and self-correct.

## capabilities
-   **Data Discovery**: Search workspace tables to find relevant datasets.
-   **Multi-File Editing**: Create or modify multiple pipeline files primarily for Medallion Architecture.
-   **Pipeline Execution**: Trigger dry-runs or full updates and inspect results.
-   **Diagnosis**: Trace data lineage and explain/fix pipeline failures.

## Workflow
1.  User provides a high-level prompt (e.g., "Build a fraud detection pipeline using `transactions` table").
2.  Agent proposes a plan.
3.  User approves the plan.
4.  Agent executes tools (edits code, runs pipeline).
5.  Agent iterates based on feedback or errors.

## Requirements
-   Partner-powered AI features enabled.
-   Databricks Assistant Agent Mode enabled.

## Reference
- [Databricks Documentation: Use the Data Engineering Agent](https://docs.databricks.com/aws/en/ldp/de-agent)
