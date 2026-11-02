"""ClinPred (and the other dbNSFP-only features) for JAK1, in EV1 order.

One MyVariant query returns ClinPred, SIFT and REVEL together, so all three are written
here rather than making three identical queries. PolyPhen-2 HVAR is pulled too, purely as a
cross-check against the 100%-coverage run already in this directory.

These three cannot exceed ~31%, and for ClinPred and REVEL that is structural rather than
fixable: both are ensembles whose inputs are other predictors' scores and gnomAD allele
frequencies, all keyed on genomic variants. A substitution needing two nucleotide changes has
no genomic SNV, hence no allele frequency and no component scores - nothing to feed the model.
"""
import json
import pathlib
import time

import pandas as pd
import requests

HERE = pathlib.Path(__file__).parent
MV = "https://myvariant.info/v1/query"
FIELDS = ("dbnsfp.aa,dbnsfp.clinpred,dbnsfp.sift,dbnsfp.sift4g,dbnsfp.revel,"
          "dbnsfp.polyphen2,dbnsfp.ensembl")


def scroll(q):
    """Page through a MyVariant query; `fields` must be repeated on every continuation."""
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
            except Exception as exc:                    # noqa: BLE001
                if a == 3:
                    raise
                print(f"   retry {a}: {type(exc).__name__}")
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


hits = scroll("dbnsfp.genename:JAK1")
print(f"records retrieved: {len(hits):,}")

rows = []
for h in hits:
    d = h.get("dbnsfp") or {}
    aa = d.get("aa") or {}
    ref, alt, pos = first(aa.get("ref")), first(aa.get("alt")), first(aa.get("pos"))
    try:
        pos = int(pos)
    except (TypeError, ValueError):
        continue
    if not (ref and alt and ref != alt and 1 <= pos <= 1154):
        continue
    rows.append({
        "variant_id": f"{ref}{pos}{alt}",
        "clinpred": first((d.get("clinpred") or {}).get("score")),
        "sift": first((d.get("sift") or {}).get("score")),
        "sift4g": first((d.get("sift4g") or {}).get("score")),
        "revel": first((d.get("revel") or {}).get("score")),
        "polyphen2_hvar": first(((d.get("polyphen2") or {}).get("hvar") or {}).get("score")),
    })
raw = pd.DataFrame(rows)
print(f"rows mapped to a protein substitution: {len(raw):,}; "
      f"distinct substitutions: {raw.variant_id.nunique():,}")

# is each predictor constant across the genomic variants giving the same substitution?
print("\nwithin-substitution spread (should be 0 for a protein-level score):")
for c in ("clinpred", "sift", "sift4g", "revel", "polyphen2_hvar"):
    g = raw.dropna(subset=[c]).groupby("variant_id")[c]
    spread = (g.max() - g.min())
    multi = (g.size() > 1).sum()
    print(f"   {c:16s} n={g.size().sum():6,}  substitutions={len(spread):6,}  "
          f"reachable>1 SNV={multi:4d}  max spread={spread.max():.6f}")

agg = raw.groupby("variant_id").max(numeric_only=True)

# ---- align to EV1 order ------------------------------------------------------
base = pd.read_csv(HERE / "jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
real = (base.wt != base.alt).sum()
written = []
for col, fname in (("clinpred", "jak1_clinpred.csv"),
                   ("sift", "jak1_sift.csv"),
                   ("revel", "jak1_revel.csv")):
    out = base.copy()
    out[col] = out.variant_id.map(agg[col])
    if col == "sift":
        out["sift4g"] = out.variant_id.map(agg["sift4g"])
    out.to_csv(HERE / fname, index=False)
    n = out[col].notna().sum()
    written.append((fname, n))
    print(f"\nwrote {fname}: {len(out):,} rows in EV1 order; "
          f"{n:,} of {real:,} substitutions ({n / real:.1%})")
    print(f"   range {out[col].min():.4g} .. {out[col].max():.4g}")

# ---- validate against what the repo already had -----------------------------
feat = pd.DataFrame(json.load(open("sources/orianne/jak1_features.json", encoding="utf-8")))
feat["variant_id"] = feat.wt + feat.pos.astype(str) + feat.alt
print("\nvalidation against data/orianne/jak1_features.json:")
for col in ("clinpred", "sift", "revel"):
    m = agg[[col]].join(feat.set_index("variant_id")[[col]], how="inner",
                        lsuffix="_mine", rsuffix="_repo").dropna()
    if not len(m):
        continue
    d = (m[f"{col}_mine"] - m[f"{col}_repo"]).abs()
    print(f"   {col:10s} n={len(m):6,}  identical={(d < 1e-6).sum():6,}  "
          f"max diff={d.max():.6f}")

# PolyPhen-2 cross-check against our own 100% run
pp = pd.read_csv(HERE / "jak1_polyphen2_humvar.csv").set_index("variant_id")
m = agg[["polyphen2_hvar"]].join(pp[["polyphen2_humvar_prob"]], how="inner").dropna()
d = (m.polyphen2_hvar - m.polyphen2_humvar_prob).abs()
print(f"   polyphen2  n={len(m):6,}  within 0.001={(d < 0.001).sum():6,}  "
       f"median diff={d.median():.4f}  (structural-snapshot difference, expected)")
