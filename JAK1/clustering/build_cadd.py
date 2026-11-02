"""CADD for JAK1 from MyVariant, in EV1 order.

mutations_clustering.md section 4 records CADD as "attempted and unavailable", because
dbnsfp.cadd.phred is empty - CADD is licence-restricted inside the academic dbNSFP build.
But MyVariant carries CADD as its OWN source at cadd.phred, outside the dbnsfp document,
and that one is populated. This closes the gap without the 81 GB download.
"""
import pathlib
import time

import pandas as pd
import requests

HERE = pathlib.Path(__file__).parent
MV = "https://myvariant.info/v1/query"
FIELDS = "dbnsfp.aa,cadd.phred,cadd.rawscore,cadd.consequence,dbnsfp.genename"


def scroll(q):
    out, total, sid = [], None, None
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
        if total is None:
            total = j.get("total")
            print(f"total hits: {total:,}")
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
    aa = ((h.get("dbnsfp") or {}).get("aa")) or {}
    cadd = h.get("cadd") or {}
    ref, alt, pos = first(aa.get("ref")), first(aa.get("alt")), first(aa.get("pos"))
    phred, raw = first(cadd.get("phred")), first(cadd.get("rawscore"))
    try:
        pos = int(pos)
    except (TypeError, ValueError):
        continue
    if ref and alt and ref != alt and 1 <= pos <= 1154 and phred is not None:
        rows.append({"variant_id": f"{ref}{pos}{alt}",
                     "cadd_phred": float(phred),
                     "cadd_raw": float(raw) if raw is not None else None})
d = pd.DataFrame(rows)
print(f"records with CADD and a protein substitution: {len(d):,}")
print(f"distinct substitutions: {d.variant_id.nunique():,}")

g = d.groupby("variant_id").cadd_phred
multi = (g.size() > 1).sum()
spread = (g.max() - g.min())
print(f"reachable by >1 SNV: {multi:,}; max within-substitution spread "
      f"{spread.max():.4f}  -> CADD is a per-SNV score, not protein-level")

agg = d.groupby("variant_id").max(numeric_only=True)
base = pd.read_csv(HERE / "jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
out = base.copy()
out["cadd_phred"] = out.variant_id.map(agg.cadd_phred)
out["cadd_raw"] = out.variant_id.map(agg.cadd_raw)
out.to_csv(HERE / "jak1_cadd.csv", index=False)
real = (base.wt != base.alt).sum()
n = out.cadd_phred.notna().sum()
print(f"\nwrote jak1_cadd.csv: {len(out):,} rows in EV1 order; "
      f"{n:,} of {real:,} ({n / real:.1%})")
print(f"   PHRED range {out.cadd_phred.min():.1f} .. {out.cadd_phred.max():.1f}, "
      f"median {out.cadd_phred.median():.1f}")

# validate against the CADD column already in the repo's JAK1 table
ext = pd.read_csv("sources/counts/JAK1_predict.csv", low_memory=False)
ext = ext[ext.Variant.str.match(r"^[A-Z]\d+[A-Z]$", na=False)]
ext["repo"] = pd.to_numeric(ext["CADD phred"], errors="coerce")
m = out.merge(ext[["Variant", "repo"]], left_on="variant_id", right_on="Variant").dropna(
    subset=["cadd_phred", "repo"])
diff = (m.cadd_phred - m.repo).abs()
print(f"\nvalidation against the repo's 'CADD phred' column: {len(m):,} shared")
print(f"   identical to 0.05: {(diff < 0.05).sum():,} ({(diff < 0.05).mean():.1%})  "
      f"median |diff| {diff.median():.3f}  max {diff.max():.2f}")
