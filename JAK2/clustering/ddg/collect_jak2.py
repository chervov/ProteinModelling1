#!/usr/bin/env python3
"""Snapshot the JAK2 dual-state ddG results into the repository and push.

Run repeatedly. Safe at any point: results are an append-only JSONL written with fsync after
every position, and positions are processed in a shuffled order, so a partial set is an unbiased
random sample rather than a biased prefix.
"""
import json, os, subprocess, time, collections

W = "/Users/chervov/ddg_jak2"
REPO = "/Users/chervov/ProteinModelling1"
OUT = os.path.join(REPO, "data", "ddg")
GENES = ("JAK2P1", "JAK2P2")
PAIR = {"JAK2P1": "pair1 (untemplated, JAK2_20261015_161033)",
        "JAK2P2": "pair2 (templated: ma-l9b1f closed / AF2 open)"}


def load(gene):
    f = os.path.join(W, f"results_{gene}.jsonl")
    if not os.path.exists(f):
        return []
    seen, recs = set(), []
    for line in open(f):
        try:
            r = json.loads(line)
        except Exception:
            continue                      # a torn final line while the worker is mid-write
        k = (r["pos"], r["alt"])
        if k not in seen:
            seen.add(k); recs.append(r)
    return recs


def main():
    os.makedirs(OUT, exist_ok=True)
    summary, changed = [], False
    for g in GENES:
        recs = load(g)
        if not recs:
            summary.append(f"{g}: nothing yet"); continue
        recs.sort(key=lambda r: (r["pos"], r["alt"]))
        p = os.path.join(OUT, f"ddg_{g}_all.json")
        new = json.dumps(recs)
        old = open(p).read() if os.path.exists(p) else ""
        if new != old:
            open(p, "w").write(new); changed = True
        npos = len({r["pos"] for r in recs})
        d = [r["delta"] for r in recs]
        summary.append(f"{g}: {len(recs):,}/21,508 variants ({100*len(recs)/21508:.1f}%), "
                       f"{npos}/1132 positions, mean|delta| {sum(map(abs,d))/len(d):.3f}")
    st = {"updated": time.strftime("%Y-%m-%d %H:%M:%S"), "lines": summary,
          "pairs": PAIR}
    open(os.path.join(OUT, "jak2_ddg_progress.json"), "w").write(json.dumps(st, indent=1))
    print("\n".join(summary), flush=True)
    if changed:
        subprocess.run(["git", "add", "data/ddg"], cwd=REPO, check=False)
        subprocess.run(["git", "commit", "-q", "-m",
                        "JAK2 dual-state ddG: incremental results\n\n" + "\n".join(summary)
                        + "\n\nCo-Authored-By: Claude Opus 5 <noreply@anthropic.com>"],
                       cwd=REPO, check=False)
        r = subprocess.run(["git", "push", "-q", "origin", "main"], cwd=REPO,
                           capture_output=True, text=True)
        print("pushed" if r.returncode == 0 else f"push failed: {r.stderr[:200]}", flush=True)


if __name__ == "__main__":
    main()
