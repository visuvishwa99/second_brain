
> **Q:** Why does Functional Data Engineering advocate against unrestricted mutability in Delta/Iceberg tables?
>
> **A:** Unrestricted mutability breaks **idempotency** and **reproducibility**. If a pipeline run silently updates rows differently based on execution time or order, the pipeline is no longer a pure function (f(input) != output), making debugging impossible and downstream aggregates unreliable.
---

> **Q:** What is the core principle of Functional Data Engineering regarding pipeline logic?
>
> **A:** Pipelines should be treated as **Pure Functions** ($f(input) = output$), meaning they efficiently handle immutability and side effects so that re-running the same data always yields the same result (idempotency), regardless of the underlying storage mutability.
---
