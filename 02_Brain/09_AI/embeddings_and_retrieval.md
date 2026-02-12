---
tags:
  - "#ai"
created_at: "2026-02-11 19:55"
source: "AI Engineering - Week 3"
status: growing
---
# Embeddings & Retrieval

This note covers the foundations of modern AI applications: how text is represented as vectors (embeddings) and how those vectors are used for semantic search, caching, and Retrieval-Augmented Generation (RAG).

---

## System Architecture

```mermaid
flowchart TD
    User["User Query"] --> Cache{"Semantic Cache"}
    Cache -- Match found --> Resp["Cached Response"]
    Cache -- No match --> Embed["Embedding Model\n(all-MiniLM-L6-v2)"]

    subgraph Storage ["Vector Storage & Search"]
        direction LR
        FAISS["FAISS Index"]
        Chroma["ChromaDB"]
        Cosine["Cosine Similarity"]
    end

    Embed --> Storage
    Storage --> Context["Retrieved Context"]

    subgraph RAG ["Capstone RAG Pipeline"]
        LLM["LLM\n(Qwen 2.5 Coder)"]
        Prompt["Augmented Prompt"]
    end

    User -.-> Prompt
    Context --> Prompt
    Prompt --> LLM
    LLM --> Resp

    subgraph Tech_Stack ["Technology Stack"]
        Stack1["Sentence Transformers\n(like Encoding in DE)"]
        Stack2["FAISS & ChromaDB\n(like Snowflake in DE)"]
        Stack3["Qwen 2.5 Coder\n(like Transformation in DE)"]
    end

    Stack1 -.-> Embed
    Stack2 -.-> Storage
    Stack3 -.-> LLM

    class User,Resp user
    class Cache,FAISS,Chroma storage
    class Embed,Cosine,Context,LLM process
    class Prompt logic

    style Tech_Stack fill:#fff,stroke:#2d3436,stroke-width:1px,color:#2d3436

    classDef logic fill:#2d3436,stroke:#dfe6e9,stroke-width:2px,color:#fff
    classDef storage fill:#0984e3,stroke:#74b9ff,stroke-width:2px,color:#fff
    classDef process fill:#6c5ce7,stroke:#a29bfe,stroke-width:2px,color:#fff
    classDef user fill:#00b894,stroke:#55efc4,stroke-width:2px,color:#fff
```

---

## Architecture Breakdown

### 1. Semantic Caching (The Fast Path)

Before performing a full search, we check if a similar question has been asked recently.

- **Semantic Cache**: Uses vector similarity to reuse previous answers even if the query isn't an exact match.
- **DE Equivalent**: Like a **Materialized View** or a **TTL-based Cache** (Redis) that stores pre-calculated results for expensive join queries.

### 2. Vectorization & Embedding

We transform raw text into numerical representation.

- **Embedding Model**: Encodes semantic meaning into a high-dimensional vector.
- **DE Equivalent**: Like **Data Encoding** or **Hashing** specifically designed for similarity rather than exact matching.

### 3. Vector Search (The Retrieval)

We search our databases for the most relevant pieces of information.

- **FAISS/ChromaDB**: Efficient high-dimensional indexing for similarity search.
- **DE Equivalent**: Like a **Database Index** optimized for `JOIN` operations across massive tables, but using distance metrics instead of primary keys.

### 4. RAG Pipeline (The Generation)

We combine user intent with retrieved data to produce a grounded answer.

- **Augmented Prompt**: Merges the User Query + Retrieved Documents.
- **DE Equivalent**: Like a **Data Enrichment (Lookup)** step in an ETL pipeline where a source record is joined with master data before final loading.

---

## Key Components

### 1. Vector Foundations

- **Cosine Similarity**: Measuring the semantic distance between two blocks of text.
- **Embeddings**: Transforming text into high-dimensional numerical arrays.
- **Vector Core**: Core logic for vector representation.

### 2. Vector Databases

- **FAISS**: High-performance similarity search using Facebook AI Similarity Search.
- **ChromaDB**: Implementing local vector storage using ChromaDB.

### 3. Semantic Caching

- **Semantic Cache**: Intercepts queries to reduce costs and latency by reusing similar previous answers.
