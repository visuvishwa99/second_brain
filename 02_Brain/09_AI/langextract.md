---
created_at: 2026-02-10 11:30
tags:
  - ai
---

# Google LangExtract

LangExtract is an open‑source Python library from Google for extracting structured data from unstructured text with LLMs like Gemini and others.

## What LangExtract is

- A general‑purpose NLP **library** that turns free‑form text (PDFs, clinical notes, legal docs, emails, novels, etc.) into structured records.
- It focuses on information extraction, entity recognition, relationship extraction, and content structuring using large language models.

## Key Features

- **Precise source grounding**: Every extracted field is linked back to its exact character span in the original text for traceability and auditing.
- **Schema‑controlled output**: You define the output schema via instructions and few‑shot examples, and the library enforces consistent, structured outputs.
- **Designed for long documents**: Uses smart chunking, parallel processing, and multiple extraction passes to handle large texts efficiently.
- **Interactive visualization**: Can generate an HTML viewer that shows extracted entities in context for manual review and QA.
- **Flexible model backends**: Supports Gemini models, OpenAI models (e.g., gpt‑4o), and local/open‑source models via Ollama.

## Basic Usage (Conceptual)

Typical workflow in Python looks like:

1.  Input: `text_or_documents` (raw text, file paths, or URLs).
2.  Prompt: Describe what entities/fields to extract.
3.  Examples: Provide few‑shot examples illustrating the desired JSON structure.
4.  Model: Specify `model_id` (e.g., `gemini-2.5-flash`).

```python
import langextract as lx 

result = lx.extract(
    text_or_documents="some long input text or URL",
    prompt_description="Describe what entities/fields to extract",
    examples=examples,  # few-shot examples
    model_id="gemini-2.5-flash", 
)
```

## Use Cases

- **Healthcare**: Structuring clinical notes into diagnoses, meds, lab values with provenance.
- **Legal/Compliance**: Extracting clauses, parties, dates, obligations with auditable source links.
- **Business Intelligence**: Pulling entities and metrics from reports for downstream analytics.
