#!/usr/bin/env python3
"""Merge the JAK3 ddG JSONL into data/ddg/ddg_JAK3_all.json. Safe to run at any point."""
import json, os
W, REPO = "/Users/chervov/ddg_jak3", "/Users/chervov/ProteinModelling1"
f = os.path.join(W, "results_JAK3.jsonl")
seen, recs = set(), []
for line in open(f):
    try: r = json.loads(line)
    except Exception: continue
    k = (r["pos"], r["alt"])
    if k not in seen: seen.add(k); recs.append(r)
recs.sort(key=lambda r: (r["pos"], r["alt"]))
json.dump(recs, open(os.path.join(REPO, "data", "ddg", "ddg_JAK3_all.json"), "w"))
print(f"{len(recs):,} variants, {len({r['pos'] for r in recs})} positions")
