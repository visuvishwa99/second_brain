
> **Q:** Why does Functional Data Engineering advocate against unrestricted mutability in Delta/Iceberg tables?
>
> **A:** Unrestricted mutability breaks **idempotency** and **reproducibility**. If a pipeline run silently updates rows differently based on execution time or order, the pipeline is no longer a pure function (f(input) != output), making debugging impossible and downstream aggregates unreliable.
---

> **Q:** What is the core principle of Functional Data Engineering regarding pipeline logic?
>
> **A:** Pipelines should be treated as **Pure Functions** ($f(input) = output$), meaning they efficiently handle immutability and side effects so that re-running the same data always yields the same result (idempotency), regardless of the underlying storage mutability.
---

> **Q:** What is the key architectural difference between LangChain and LangGraph?
>
> **A:** LangChain is optimized for **DAGs (Directed Acyclic Graphs)** or linear chains, while LangGraph is optimized for **Cyclic Graphs** (loops), which are essential for agentic behaviors like retries and iterative planning.
---

> **Q:** What role does LangSmith play in the LangChain ecosystem?
>
> **A:** LangSmith is the **observability platform** for LLM applications. It provides tracing, debugging, and monitoring of metrics like latency and token usage (think "Datadog for LLMs").
---

> **Q:** How does Snowflake Cortex Code (CoCo) prevent hallucinations about non-existent tables?
>
> **A:** Unlike generic AI tools, CoCo is **Context Aware**—it checks the actual database metadata (schema, RBAC privileges) before generating code, ensuring it only suggests valid objects.
---

> **Q:** What is the "Hybrid Strategy" for Databricks and Snowflake in 2026?
>
> **A:** Using Databricks as the **Data Factory** (for heavy engineering, ML, structureless data) and Snowflake as the **Data Storefront** (for high-concurrency BI and serving governed data via Iceberg/replication).
---
