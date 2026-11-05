# Case study: generating Deadlock builds you can actually import

## Problem

Deadlock builds are shared as opaque codes: base64 over a zstd-compressed protobuf. An
LLM can happily invent an item name, a tier, or an ID, and the result looks like a build
until you paste it into the game. The interesting engineering question is not "can a model
write a build", it is "how do you make an unreliable generator produce only artifacts that
are legal and verifiable".

## Approach

Four layers, each able to fail on its own:

1. **Retrieval** (`rag.py`) — 563 curated markdown documents chunked into 3,101 records,
   ranked with BM25 + cosine + MMR over a JSON index. A scope gate and a token-coverage
   check let it abstain instead of answering from model memory.
2. **Planning** (`buildgen.py`) — a 14-section template plus retrieved evidence plus the
   exact list of shopable items for that tier and slot. The model picks names, never IDs.
3. **Resolution** — every name is mapped to a real game ID; anything unmatched aborts the
   run. Unknown IDs cannot reach the encoder.
4. **Verification** (`validate_build.py` + codec) — encode, decode the result, compare the
   hero, then run structural checks (category set, tier/slot legality, duplicates, ability
   currency rules). Only a code that survives all of it is printed.

## Tradeoffs taken deliberately

- **JSON index over a vector database.** 3,101 chunks load in seconds and are debuggable
  with a text editor. At a hundred times this size I would revisit it.
- **Hashed embedding fallback.** Semantic quality drops when Ollama is absent, but the
  system never hard-fails because a model server is not running.
- **Whole-document output, not streaming.** The user gets a build only after validation,
  so a half-generated build can never be copied by mistake.

## Results

- Retrieval: **recall@5 0.972** (69/71), **abstention 1.000** (12/12) over 83 labelled
  questions, reproducible from a clean clone in CI.
- Generation: **1.000 average** over 12 hero/role cases, each producing a code that
  decodes and validates, plus a negative case that must be rejected.
- Runtime: 49–76 s per build against a hosted chat model; index build ~10 s.

## What I would do next

- Patch-freshness pipeline so the corpus tracks new versions automatically.
- Per-item win-rate priors feeding the candidate list (the analytics fetcher already
  exists, it is just not wired into the prompt).
- Cross-encoder rerank for the two categories that still miss: mechanics and multi-hop.
