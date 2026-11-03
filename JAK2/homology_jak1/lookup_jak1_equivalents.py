"""For each JAK2 variant's JAK1-equivalent position: how trustworthy is the mapping, and what
did the rebuilt JAK1 clustering say about that variant?

Two separate questions, deliberately kept apart:
  - mapping confidence, from local alignment identity in a window around the site;
  - the JAK1 variant's features and cluster label, which are only meaningful if the mapping is.
"""
import pathlib

import pandas as pd
from Bio import Align
from Bio.Align import substitution_matrices

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent.parent                      # repository root, from JAK2/homology_jak1/
# inputs live in external_data/ and JAK1/clustering/ in the repository; fall back if run standalone
EXT = ROOT / "external_data" if (ROOT / "external_data").is_dir() else HERE
CL = ROOT / "JAK1" / "clustering"
if not CL.is_dir():
    CL = next((p for p in (ROOT / "clustering", HERE / "clustering") if p.is_dir()), CL)
VARIANTS = ["V1110E", "G571R", "V578I", "L805I", "V617F"]

# G571R does not have a stable JAK1 position: this alignment puts it at 612, the repository's
# earlier one and two of five gap-penalty settings put it at 610. Both are carried so the table
# shows that the choice changes the rebuilt cluster label.
ALT_MAPPINGS = [("G571R", 610)]

# JAK1 domain boundaries (UniProt P23458 annotation)
DOMAINS = [(33, 420, "FERM"), (439, 544, "SH2-like"), (583, 855, "JH2 pseudokinase"),
           (875, 1153, "JH1 kinase")]

seqs, name = {}, None
for line in (EXT / "jak_sequences.fasta").read_text().splitlines():
    if line.startswith(">"):
        name = line[1:].strip(); seqs[name] = ""
    elif name:
        seqs[name] += line.strip()
J2, J1 = seqs["JAK2"], seqs["JAK1"]

al = Align.PairwiseAligner(scoring="blastp")
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -11, -1
aln = al.align(J2, J1)[0]
a2, a1 = str(aln[0]), str(aln[1])

col, i2 = {}, 0                               # JAK2 position -> alignment column
for k, c in enumerate(a2):
    if c != "-":
        i2 += 1
        col[i2] = k
pairs, i2, j1 = {}, 0, 0
for c2, c1 in zip(a2, a1):
    if c2 != "-":
        i2 += 1
    if c1 != "-":
        j1 += 1
    if c2 != "-":
        pairs[i2] = j1 if c1 != "-" else None


def local_identity(k, half):
    """Fraction of identical columns in a window, and gaps in it - the mapping's support."""
    lo, hi = max(0, k - half), min(len(a2), k + half + 1)
    w2, w1 = a2[lo:hi], a1[lo:hi]
    idn = sum(1 for x, y in zip(w2, w1) if x == y and x != "-")
    gp = sum(1 for x, y in zip(w2, w1) if x == "-" or y == "-")
    return idn / len(w2), gp


def domain(p):
    for lo, hi, d in DOMAINS:
        if lo <= p <= hi:
            return d
    return "linker / terminus"


# the feature files, all in EV1 order and keyed on variant_id
feat = {}
for f, c in [("jak1_esm1b.csv", "esm1b"), ("jak1_alphamissense.csv", "alphamissense"),
             ("jak1_polyphen2_humvar.csv", "polyphen2_humvar_prob"), ("jak1_sift.csv", "sift"),
             ("jak1_cadd.csv", "cadd_phred"), ("jak1_clinpred.csv", "clinpred"),
             ("jak1_blosum62.csv", "blosum62"),
             ("jak1_ddg_foldx_precomputed.csv", "foldx_ddg")]:
    feat[c] = pd.read_csv(CL / f).set_index("variant_id")[c]
dd = pd.read_csv(CL / "jak1_ddg_rosetta_dualstate.csv").set_index("variant_id")
reb = pd.read_csv(CL / "jak1_clustering_rebuilt.csv").set_index("variant_id")

def build(v, p_override=None, kind="primary"):
    """One row: the mapping, its alignment support, and the JAK1 variant's labels and features."""
    wt, pos, alt = v[0], int(v[1:-1]), v[-1]
    p = p_override if p_override is not None else pairs.get(pos)
    id11, g11 = local_identity(col[pos], 5)
    id41, g41 = local_identity(col[pos], 20)
    j1aa = J1[p - 1] if p else None
    eq = f"{j1aa}{p}{alt}" if p else None
    r = {
        "JAK2": v, "mapping": kind, "JAK1_pos": p, "JAK1_wt": j1aa, "JAK1_equivalent": eq,
        "wt_conserved": j1aa == wt, "is_self_sub": j1aa == alt,
        "domain(JAK1)": domain(p) if p else None,
        "local_id_11": round(id11, 2), "gaps_11": g11,
        "local_id_41": round(id41, 2), "gaps_41": g41,
    }
    # a self-substitution has no scores anywhere, by construction - leave the columns empty
    if eq and j1aa != alt and eq in reb.index:
        r["EV1_cluster"] = int(reb.loc[eq, "cluster"])
        r["rebuilt_cluster"] = int(reb.loc[eq, "my_cluster"])
        for c, s in feat.items():
            r[c] = s.get(eq)
        r["ddg_closed"] = dd.loc[eq, "ddg_closed"] if eq in dd.index else None
        r["ddg_open"] = dd.loc[eq, "ddg_open"] if eq in dd.index else None
        r["within_15"] = dd.loc[eq, "within_15"] if eq in dd.index else None
    return r


rows = [build(v) for v in VARIANTS]
rows += [build(v, p, "alternative") for v, p in ALT_MAPPINGS]

T = pd.DataFrame(rows)
pd.set_option("display.width", 250, "display.max_columns", 50)
print("=== mapping and its support ===")
print(T[["JAK2", "mapping", "JAK1_pos", "JAK1_wt", "JAK1_equivalent", "wt_conserved", "is_self_sub",
         "domain(JAK1)", "local_id_11", "gaps_11", "local_id_41", "gaps_41"]].to_string(index=False))

print("\n=== what the JAK1 clustering says about the equivalent variant ===")
print("   EV1_cluster = the paper's label; rebuilt_cluster = the rebuild in JAK1/clustering/")
print("   cluster 1 = gnomAD-common pole, cluster 2 = reported-GOF pole")
cols = ["JAK2", "mapping", "JAK1_equivalent", "EV1_cluster", "rebuilt_cluster", "alphamissense", "esm1b",
        "polyphen2_humvar_prob", "sift", "cadd_phred", "clinpred", "blosum62", "foldx_ddg",
        "ddg_closed", "ddg_open", "within_15"]
print(T.reindex(columns=cols).to_string(index=False))

# context: how do these sit against the whole JAK1 distribution?
print("\n=== percentile of each equivalent within all 21,926 JAK1 substitutions ===")
am = feat["alphamissense"].dropna()
es = feat["esm1b"].dropna()
for _, r in T.iterrows():
    e = r.JAK1_equivalent
    if e in am.index and pd.notna(am.get(e)):
        print(f"  {r.JAK2} -> {e:8s} AlphaMissense {am[e]:.4f} = {(am < am[e]).mean():5.1%} pct    "
              f"ESM-1b {es[e]:8.3f} = {(es < es[e]).mean():5.1%} pct")
    else:
        print(f"  {r.JAK2} -> {e}: no scores (self-substitution)" if r.is_self_sub
              else f"  {r.JAK2} -> {e}: not scored")

T.to_csv(HERE / "jak2_to_jak1_with_clustering.csv", index=False)
print("\nwrote jak2_to_jak1_with_clustering.csv")
