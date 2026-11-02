"""Are the ClinPred differences against the repo confined to multi-SNV substitutions?

I claimed the 332 disagreements come from aggregation choice over the 759 substitutions
reachable by more than one nucleotide change. If so, every disagreement should fall inside
that set and none outside it. Test rather than assert.
"""
import json
import pathlib
import time

import pandas as pd
import requests

HERE = pathlib.Path(__file__).parent
MV = "https://myvariant.info/v1/query"
FIELDS = "dbnsfp.aa,dbnsfp.clinpred"


def scroll(q):
    out, sid = [], None
    while True:
        for a in (1, 2, 3):
            try:
                p = ({"scroll_id": sid, "fields": FIELDS} if sid
                     else {"q": q, "fields": FIELDS, "fetch_all": "true"})
                r = requests.get(MV, params=p, timeout=300)
                r.raise_for_status()
                j = r.json()
                break
            except Exception:                               # noqa: BLE001
                if a == 3:
                    raise
                time.sleep(5 * a)
        hits = j.get("hits", [])
        if not hits:
            break
        out.extend(hits)
        sid = j.get("_scroll_id")
        if not sid:
            break
    return out


def first(v):
    while isinstance(v, list):
        v = v[0] if v else None
    return v


rows = []
for h in scroll("dbnsfp.genename:JAK1"):
    d = h.get("dbnsfp") or {}
    aa = d.get("aa") or {}
    ref, alt, pos = first(aa.get("ref")), first(aa.get("alt")), first(aa.get("pos"))
    cp = first((d.get("clinpred") or {}).get("score"))
    try:
        pos = int(pos)
    except (TypeError, ValueError):
        continue
    if ref and alt and ref != alt and cp is not None and 1 <= pos <= 1154:
        rows.append({"variant_id": f"{ref}{pos}{alt}", "clinpred": float(cp)})
raw = pd.DataFrame(rows)

g = raw.groupby("variant_id").clinpred
n_snv, spread = g.size(), g.max() - g.min()
multi = set(n_snv[n_snv > 1].index)
print(f"{len(raw):,} genomic variants -> {len(n_snv):,} substitutions")
print(f"reachable by >1 SNV: {len(multi):,}; of those, differing values: "
      f"{(spread[list(multi)] > 1e-6).sum():,}")

feat = pd.DataFrame(json.load(open("sources/orianne/jak1_features.json", encoding="utf-8")))
feat["variant_id"] = feat.wt + feat.pos.astype(str) + feat.alt
repo = feat.set_index("variant_id").clinpred.dropna()

for how, series in (("max", g.max()), ("min", g.min()), ("mean", g.mean()),
                    ("first", raw.groupby("variant_id").clinpred.first())):
    m = pd.concat([series.rename("mine"), repo.rename("repo")], axis=1,
                  join="inner").dropna()
    d = (m.mine - m.repo).abs()
    diff = d > 1e-6
    inside = sum(1 for v in m.index[diff] if v in multi)
    print(f"\naggregating by {how:6s}: {diff.sum():4,} disagreements of {len(m):,}"
          f"   max diff {d.max():.6f}")
    print(f"   inside the multi-SNV set: {inside:,} / {diff.sum():,}"
          f"   outside: {diff.sum() - inside:,}")
