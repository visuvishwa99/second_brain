## Spark State Management

---
### Stateless Transformation
- No need to store the state of results.
- Full load actually fails due to memory issues we implement full with following **Append Mode**.
- **Implementation of aggregation without using statestore** : Instead of taking results from "state store" we take those results from already exist target query and rewrite the merge statement.
- Select(), filter(), map(), flatMap(), explode(), etc.
- It does not support **Complete output mode** because they do not maintain state.

---
### Statefull Transformation
- Spark is maintaining/storing the results. Pass the results across the micro batches.
- Supports **Complete** and **Update** modes.
- Statefull aggregations include windowing and watermarking.