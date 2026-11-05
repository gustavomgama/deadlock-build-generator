"""Retrieval evaluation for the local RAG oracle.

Usage:
  python eval.py [--index PATH] [--questions PATH] [--top-k N]

Each JSONL line: id, category, question, expected_sources (substrings of
retrieved citations), expected_abstain (bool).
"""
import argparse
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import rag

DEFAULT_Q = pathlib.Path(__file__).resolve().parent / "eval" / "questions.jsonl"


def load_questions(path):
    rows = []
    for line in pathlib.Path(path).read_text(encoding="utf-8-sig").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def run_one(index, question, top_k):
    payload = json.loads(rag.query(index, question, top_k=top_k, as_json=True, generate=False))
    citations = [row.get("citation") or "" for row in payload]
    return payload, citations


def main():
    parser = argparse.ArgumentParser(description="Retrieval recall and abstention evaluation")
    parser.add_argument("--index", default=str(rag.DEFAULT_INDEX))
    parser.add_argument("--questions", default=str(DEFAULT_Q))
    parser.add_argument("--top-k", type=int, default=5)
    parser.add_argument("--min-recall", type=float, default=None)
    parser.add_argument("--min-abstention", type=float, default=None)
    args = parser.parse_args()

    if not pathlib.Path(args.index).exists():
        raise SystemExit(f"no index at {args.index}; run: python rag.py build")

    questions = load_questions(args.questions)
    stats = {}
    hits = misses = 0
    abstain_ok = abstain_total = 0

    for q in questions:
        expected = q.get("expected_sources") or []
        want_abstain = bool(q.get("expected_abstain"))
        payload, citations = run_one(args.index, q["question"], q.get("top_k") or args.top_k)
        abstained = not payload

        if want_abstain:
            abstain_total += 1
            abstain_ok += int(abstained)
            ok = abstained
        else:
            ok = bool(citations) and any(any(e in c for c in citations) for e in expected)
            if ok:
                hits += 1
            else:
                misses += 1

        bucket = stats.setdefault(q["category"], [0, 0])
        bucket[0] += int(ok)
        bucket[1] += 1

    print(f"{'category':24} {'passed':>6} {'total':>5} {'rate':>6}")
    for name in sorted(stats):
        passed, total = stats[name]
        print(f"{name:24} {passed:6} {total:5} {passed / total:6.3f}")

    answered = hits + misses
    recall = hits / answered if answered else 0.0
    abst = abstain_ok / abstain_total if abstain_total else 1.0
    print()
    print(f"retrieval recall@{args.top_k}: {recall:.3f} ({hits}/{answered})")
    print(f"abstention accuracy:    {abst:.3f} ({abstain_ok}/{abstain_total})")

    failed = []
    if args.min_recall is not None and recall < args.min_recall:
        failed.append(f"recall {recall:.3f} < {args.min_recall}")
    if args.min_abstention is not None and abst < args.min_abstention:
        failed.append(f"abstention {abst:.3f} < {args.min_abstention}")
    if failed:
        raise SystemExit("threshold not met: " + ", ".join(failed))


if __name__ == "__main__":
    main()
