"""AlphaMissense for every SNV-reachable substitution in each JAK gene, on identical footing.

Pulls the ALPHAMISSENSE feature out of the Atlas AVI_SCORE_MODEL_FEATURES for every CDS
SNV, translates strand-aware, and reports the benign/ambiguous/pathogenic split per gene
with no selection by what has been observed in patients.

Also tests two things I asserted earlier:
  A. is AlphaMissense constant across codon changes giving the same substitution?
  B. are SNV-reachable substitutions chemically more conservative than unreachable ones?

Usage: python jak_alphamissense.py JAK1 JAK2 JAK3 TYK2
"""
import pathlib
import sys
import time

import numpy as np
import pandas as pd
import requests
from alphagenome.atlas import atlas
from alphagenome.data import genome
from Bio.Align import substitution_matrices

ENS = "https://rest.ensembl.org"
OUT = pathlib.Path("ag")
BLOSUM = substitution_matrices.load("BLOSUM62")
COMP = {"A": "T", "C": "G", "G": "C", "T": "A"}
AAS = "ACDEFGHIKLMNPQRSTVWY"

CODONS = {}
_b = "TCAG"
_aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
for _i, _x in enumerate(_b):
    for _j, _y in enumerate(_b):
        for _k, _z in enumerate(_b):
            CODONS[_x + _y + _z] = _aa[_i * 16 + _j * 4 + _k]


def ensembl(path, tries=5):
    for a in range(1, tries + 1):
        try:
            r = requests.get(f"{ENS}{path}", headers={"Content-Type": "application/json"},
                             timeout=180)
            r.raise_for_status()
            return r.json()
        except Exception:                            # noqa: BLE001
            if a == tries:
                raise
            time.sleep(4 * a)


client = atlas.create(pathlib.Path("alphagenome_token.txt").read_text("utf-8").strip())
rows_all, summary = [], []

for gene in sys.argv[1:]:
    g = ensembl(f"/lookup/symbol/homo_sapiens/{gene}?expand=1")
    tid = next(t["id"] for t in g["Transcript"] if t.get("is_canonical") == 1)
    tr = ensembl(f"/lookup/id/{tid}?expand=1")
    strand, chrom = tr["strand"], "chr" + tr["seq_region_name"]
    cds_lo, cds_hi = tr["Translation"]["start"], tr["Translation"]["end"]
    aa_len = tr["Translation"]["length"]
    cds_seq = ensembl(f"/sequence/id/{tid}?type=cds")["seq"].upper()

    # CDS parts of exons, in TRANSCRIPT order
    parts = []
    for ex in sorted(tr["Exon"], key=lambda e: e["start"], reverse=(strand == -1)):
        lo, hi = max(ex["start"], cds_lo), min(ex["end"], cds_hi)
        if lo <= hi:
            parts.append((lo, hi))
    pos2cds, idx = {}, 0
    for lo, hi in parts:
        rng = range(lo, hi + 1) if strand == 1 else range(hi, lo - 1, -1)
        for p in rng:
            pos2cds[p] = idx
            idx += 1
    print(f"\n=== {gene} {tid} strand {strand:+d}, {aa_len} aa, CDS {len(cds_seq)} nt, "
          f"{len(pos2cds)} mapped positions", flush=True)

    t0, recs = time.time(), []
    for lo, hi in parts:
        iv = genome.Interval(chromosome=chrom, start=lo - 1, end=hi)
        ad = client.query_interval(interval=iv,
                                   requested_scorers=["AVI_SCORE_MODEL_FEATURES"],
                                   progress_bar=False)["AVI_SCORE_MODEL_FEATURES"]
        col = list(ad.var["name"]).index("ALPHAMISSENSE")
        for var, am in zip(ad.obs["variant"], ad.X[:, col]):
            p, ref, alt = int(var.position), var.reference_bases, var.alternate_bases
            if p not in pos2cds or len(ref) != 1 or len(alt) != 1:
                continue
            i = pos2cds[p]
            t_ref = ref if strand == 1 else COMP[ref]
            t_alt = alt if strand == 1 else COMP[alt]
            if cds_seq[i] != t_ref:
                recs.append({"consequence": "REF_MISMATCH"})
                continue
            cn, off = divmod(i, 3)
            wt_cod = cds_seq[cn * 3:cn * 3 + 3]
            mt_cod = wt_cod[:off] + t_alt + wt_cod[off + 1:]
            wt, mt = CODONS[wt_cod], CODONS[mt_cod]
            cons = ("synonymous" if wt == mt else "nonsense" if mt == "*"
                    else "stop_lost" if wt == "*" else "missense")
            recs.append({"gene": gene, "aa_pos": cn + 1, "wt_aa": wt, "mut_aa": mt,
                         "consequence": cons, "alphamissense": float(am),
                         "variant": f"{wt}{cn + 1}{mt}" if cons == "missense" else ""})
    df = pd.DataFrame(recs)
    mism = (df.consequence == "REF_MISMATCH").sum()
    print(f"    {len(df):,} CDS SNVs in {time.time() - t0:.1f}s, {mism} ref mismatches")

    mis = df[(df.consequence == "missense") & df.alphamissense.notna()].copy()

    # A. is AlphaMissense constant per amino-acid substitution?
    spread = mis.groupby("variant").alphamissense.agg(["nunique", "min", "max", "size"])
    multi = spread[spread["size"] > 1]
    worst = (multi["max"] - multi["min"]).max() if len(multi) else 0.0
    print(f"    A. {len(multi):,} substitutions reachable by >1 SNV; "
          f"largest within-substitution spread {worst:.6f}")

    sub = mis.groupby(["variant", "aa_pos", "wt_aa", "mut_aa"]).alphamissense.max().reset_index()
    cls = pd.cut(sub.alphamissense, [-0.01, 0.34, 0.564, 1.01],
                 labels=["likely benign", "ambiguous", "likely pathogenic"])
    counts = cls.value_counts()
    n = len(sub)
    print(f"    {n:,} distinct substitutions ({n / (19 * aa_len):.1%} of {19 * aa_len:,})")
    for k in ["likely benign", "ambiguous", "likely pathogenic"]:
        print(f"       {k:20s} {counts[k]:5d}  ({counts[k] / n:6.1%})")
    summary.append({"gene": gene, "aa_len": aa_len, "n_reachable": n,
                    "pct_of_possible": n / (19 * aa_len),
                    **{k: counts[k] / n for k in counts.index.tolist()},
                    "mean_alphamissense": sub.alphamissense.mean()})

    # B. are reachable substitutions chemically more conservative?
    reach = set(zip(sub.aa_pos, sub.mut_aa))
    wt_by_pos = dict(zip(sub.aa_pos, sub.wt_aa))
    r_sc, u_sc = [], []
    for pos, wt in wt_by_pos.items():
        for mt in AAS:
            if mt == wt:
                continue
            s = BLOSUM[wt][mt]
            (r_sc if (pos, mt) in reach else u_sc).append(s)
    print(f"    B. BLOSUM62: reachable mean {np.mean(r_sc):+.3f} (n={len(r_sc):,}) vs "
          f"unreachable {np.mean(u_sc):+.3f} (n={len(u_sc):,})  "
          f"[higher = more conservative]")
    sub["gene"] = gene
    rows_all.append(sub)

pd.concat(rows_all).to_csv(OUT / "jak_alphamissense_reachable.csv", index=False)
s = pd.DataFrame(summary)
s.to_csv(OUT / "jak_alphamissense_summary.csv", index=False)
print("\n=== identical-footing comparison ===")
print(s.to_string(index=False, float_format=lambda v: f"{v:.3f}"))
