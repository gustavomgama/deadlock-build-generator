# rag project conventions

Standalone repo: local RAG oracle over Deadlock data plus a build generator.

- Windows: PowerShell only, no bash syntax.
- Everything the tools need lives in this folder: `corpus/` (markdown), `data/` (item and hero JSON), `codec/`.
- Rebuild the index with `python rag.py build`; it is never committed.
- The build pipeline must fail closed: never print a build code that has not round-tripped and validated.
