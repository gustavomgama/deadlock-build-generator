# Deadlock RAG Oracle — Specification

## Scope
Answers any question about the game Deadlock (Valve) using retrieved, cited, patch-versioned source data as evidence, with reasoning over that evidence. No other domain.

## Data sources (trust levels)
- deadlock.wiki (community wiki): medium-high. Prose/tables on heroes, abilities, items, mechanics, patch history. Verify numeric claims against API.
- api.deadlock-api.com: high for structured game data and match statistics. Endpoints discovered via /docs.
- Conflict rule: prefer structured API data for numeric values; record discrepancy; never silently merge.

## Record metadata
Every record carries: patch version, date, entity type, related hero/item, source URL, trust level. Structured API data = one entity per record. Wiki prose = chunked by section.

## Domain boundary / no invention
Only ingested Deadlock data and tool output. No model memory as source. Decline non-Deadlock questions. Unsupported in-domain questions -> supported portion + stated limit + logged gap. Interpretation derives conclusions; never adds premises.

## Abstention policy
Abstain (return no chunks / decline) when retrieval confidence is low, scope check fails, or token coverage < 0.5, or a numeric token from the question is absent from retrieved content.

## Baseline RAG pipeline
- Chunking suited to data type (section-based wiki, one-entity API).
- Hybrid retrieval (lexical BM25 + vector cosine) with MMR reranking.
- Current-patch resolution filters superseded values.
- Answers cite chunks. Abstention on low confidence.

## Reasoning layer
Structured answer format: sourced facts (cited), computed results (tool output), inferences, conclusion, assumptions, confidence. Scope gate declines non-Deadlock questions.

## Interface
CLI: build, sync, query (top-k, min-score, --json, --rewrite, filters, --current-only), health. Query output cites source, patch version, trust level.

## Observability
Optional query logging via RAG_LOG_QUERIES=1 to .rag_query_log.jsonl.

## Evaluation
Harness: rag/eval.py + rag/eval/questions.jsonl. Metrics: retrieval recall, answer correctness, citation validity, abstention accuracy, reasoning quality, invention rate. Per category. Held-out split never used for tuning.

## Storage/model stack
Python 3.13 stdlib + `zstandard`. Ollama nomic-embed-text (GPU) if available, else hashed fallback. JSON vector store + pickle sidecar. No cloud/paid services.
PY