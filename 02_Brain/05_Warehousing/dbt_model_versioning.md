---
created_at: 2026-02-12 07:42
tags:
  - warehousing
status: sapling
---

# dbt Model Logic Versioning

**Problem**: Tracking the "version" of the logic that produced a specific dataset, especially for append-only snapshots. A change in an upstream intermediate model changes the meaning of the data, even if the final model's SQL hasn't changed.

## Approaches to Logic Versioning

### 1. Manual `var()` in `dbt_project.yml`
*   **Mechanism**: Define a variable like `model_version: 1` in the config. Increment it manually when logic changes.
*   **Pros**: Native to dbt, simple.
*   **Cons**: Error-prone (easy to forget), doesn't automatically track upstream changes.

### 2. `dbt_artifacts` Checksum
*   **Mechanism**: The `dbt_artifacts` package stores a SHA hash of each model's SQL execution.
*   **Pros**: Automatic, auditable.
*   **Cons**: Only tracks the *individual* model's file hash. If `int_payments` changes, `fct_orders` (which selects from it) effectively has new logic, but its own SHA hasn't changed.

### 3. Compile-Time Macro & Graph Nodes (Recommended)
*   **Mechanism**: Use a custom macro that traverses the `graph.nodes` at compile time. It combines the checksum of the current model *plus* the checksums of all upstream dependencies into a single "provenance hash".
*   **Pros**: Truly captures the entire lineage state. If *any* upstream logic changes, the final hash changes.
*   **Cons**: Produces a cryptographic hash (e.g., `a1b2c3d4`), not a semantic version number (v1.0), making it harder for humans to read at a glance.

### 4. Native `dbt model version`
*   **Mechanism**: dbt's newer native versioning feature in YAML.
*   **Pros**: First-party support.
*   **Cons**: Still relies on manual definition or static config; shares limitations with approach #1 regarding automatic upstream propagation.

## Conclusion
For robust data engineering pipelines where traceability is key (e.g., reproducing historical numbers), **Approach #3 (Graph Traversal Hash)** is the most technically accurate method, often stored as a metadata column (e.g., `_etl_logic_hash`) in the final table.
