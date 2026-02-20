---
tags:
  - ai
---

# AI/ML System Design & Interview Strategy

## Portfolio and CV Optimization
When presenting projects, especially for senior roles, focus on concrete metrics and architectural clarity:
- **Direct Links**: Provide clickable repository or application links.
- **Architecture Sketch**: Include a diagram showing data flow (Data → Retrieval/Inference → Serving).
- **Performance Metrics**: Mention p95 latency, cost per request, and evaluation metrics (e.g., hit@10).
- **Tooling**: Highlight cloud infrastructure, CI/CD, and MLOps principles.
- **Retrospectives**: Include "Postmortem" notes on what broke and the subsequent fix.

**Example CV Bullet Point:**
> "Built Hybrid Search for X: p95 latency ~700ms, cost $0.004/request, hit@10 of 0.83. Stack: FastAPI, Postgres, OpenSearch, LangGraph. Ops: Docker, CI, alerts. Reduced latency by 42% via caching and batching."

## AI/ML System Design Framework
A structured approach to design interviews:
1. **Goals & SLOs**: Define p95 latency, quality, and cost constraints.
2. **Data Flow**: Ingest → Store → Retrieve → Infer → Feedback.
3. **Trade-offs**: Latency vs. Quality, Freshness vs. Cost.
4. **Reliability**: Implement caching, fallbacks, and observability.

### Design Prompts for Practice
- **Scalable RAG**: Design RAG for 1M PDFs with <1.5s latency (Focus: Caching and reranker placement).
- **Model Routing**: Deploy assistant with routing (Small vs. Big models), cost guardrails, and fail-open paths.
- **Resilience**: Handle data drift with eval gates, rollbacks, and shadow tests.

### Interview Evaluation Checklist
- Clarifying ambiguity and choosing constraints.
- Identifying latency bottlenecks (I/O, tokenization, reranking, tool calls).
- Measuring cost and quality per request.
- Operational readiness (retries, alerts, etc.).
