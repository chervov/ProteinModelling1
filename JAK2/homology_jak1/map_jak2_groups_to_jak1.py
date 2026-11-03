"""Map two groups of JAK2 variants onto JAK1, with per-site mapping confidence.

Group 1: gain-of-function variants previously reported.
Group 2: variants identified in the study.

Same method as align_jak2_to_jak1.py, extended in three ways that matter at this scale:
  - every variant's wild-type residue is checked against O60674 before anything else;
  - each site's mapping is recomputed at five gap-penalty settings and reported as unanimous
    or not, so an unstable mapping cannot pass as a result;
  - nonsense variants (X) are carried but never given a cluster label or a substitution score,
    because no missense predictor applies to them.

Group 1 being independently known gain-of-function makes it a test of the JAK1 clustering:
if the clustering carries transferable signal, Group 1's JAK1 equivalents should sit in
Cluster 2 (the GOF-anchored pole) more often than chance. Chance here is high - Cluster 2 holds
65% of all JAK1 substitutions - so the test is run against that base rate, not against 50%.
"""
import pathlib

import pandas as pd
from Bio import Align
from Bio.Align import substitution_matrices
from scipy.stats import binomtest, fisher_exact, mannwhitneyu

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent.parent
EXT = ROOT / "external_data" if (ROOT / "external_data").is_dir() else HERE
CL = ROOT / "JAK1" / "clustering"
if not CL.is_dir():
    CL = next((p for p in (ROOT / "clustering", HERE / "clustering") if p.is_dir()), CL)

GROUP1 = ["T108A", "Y317H", "H345L", "H608N", "L611S", "V617I", "V617F", "V625F",
          "E846D", "R867Q", "T875N", "S755R", "R938Q", "R1063H"]
GROUP2 = ["P37A", "F240V", "H380Y", "R426X", "C427R", "G571R", "V578I", "L805I",
          "I1065T", "V1110E"]
GAP_SETTINGS = [(-11, -1), (-10, -0.5), (-12, -2), (-8, -2), (-14, -1)]

DOMAINS = [(33, 420, "FERM"), (439, 544, "SH2-like"), (583, 855, "JH2 pseudokinase"),
           (875, 1153, "JH1 kinase")]

seqs, name = {}, None
for line in (EXT / "jak_sequences.fasta").read_text().splitlines():
    if line.startswith(">"):
        name = line[1:].strip(); seqs[name] = ""
    elif name:
        seqs[name] += line.strip()
J2, J1 = seqs["JAK2"], seqs["JAK1"]


def align(op, ex):
    al = Align.PairwiseAligner(scoring="blastp")
    al.substitution_matrix = substitution_matrices.load("BLOSUM62")
    al.open_gap_score, al.extend_gap_score = op, ex
    a = al.align(J2, J1)[0]
    a2, a1 = str(a[0]), str(a[1])
    pairs, col, i2, j1 = {}, {}, 0, 0
    for k, (c2, c1) in enumerate(zip(a2, a1)):
        if c2 != "-":
            i2 += 1
            col[i2] = k
        if c1 != "-":
            j1 += 1
        if c2 != "-":
            pairs[i2] = j1 if c1 != "-" else None
    return pairs, col, a2, a1


maps = {g: align(*g) for g in GAP_SETTINGS}
pairs, col, a2, a1 = maps[(-11, -1)]            # the reference setting


def local_identity(k, half):
    lo, hi = max(0, k - half), min(len(a2), k + half + 1)
    w2, w1 = a2[lo:hi], a1[lo:hi]
    return (sum(1 for x, y in zip(w2, w1) if x == y and x != "-") / len(w2),
            sum(1 for x, y in zip(w2, w1) if x == "-" or y == "-"))


def domain(p):
    return next((d for lo, hi, d in DOMAINS if p and lo <= p <= hi), "linker / terminus")


feat = {}
for f, c in [("jak1_esm1b.csv", "esm1b"), ("jak1_alphamissense.csv", "alphamissense"),
             ("jak1_polyphen2_humvar.csv", "polyphen2_humvar_prob"), ("jak1_sift.csv", "sift"),
             ("jak1_cadd.csv", "cadd_phred"), ("jak1_clinpred.csv", "clinpred"),
             ("jak1_blosum62.csv", "blosum62"),
             ("jak1_ddg_foldx_precomputed.csv", "foldx_ddg")]:
    feat[c] = pd.read_csv(CL / f).set_index("variant_id")[c]
reb = pd.read_csv(CL / "jak1_clustering_rebuilt.csv").set_index("variant_id")

rows = []
for grp, lst in (("1 reported GOF", GROUP1), ("2 this study", GROUP2)):
    for v in lst:
        wt, pos, alt = v[0], int(v[1:-1]), v[-1]
        r = {"group": grp, "JAK2": v, "JAK2_pos": pos, "is_nonsense": alt == "X"}
        # ---- 1. does the stated wild type match O60674? ----
        r["JAK2_wt_ok"] = (1 <= pos <= len(J2)) and J2[pos - 1] == wt
        r["JAK2_actual_wt"] = J2[pos - 1] if 1 <= pos <= len(J2) else None
        if not r["JAK2_wt_ok"]:
            rows.append(r)
            continue
        # ---- 2. mapping, and whether it survives the gap settings ----
        ps = [maps[g][0].get(pos) for g in GAP_SETTINGS]
        p = pairs.get(pos)
        r["JAK1_pos"] = p
        r["unanimous"] = len(set(ps)) == 1
        r["positions_seen"] = "/".join(str(x) for x in sorted({x for x in ps if x}))
        id11, g11 = local_identity(col[pos], 5)
        r["local_id_11"], r["gaps_11"] = round(id11, 2), g11
        r["domain(JAK1)"] = domain(p)
        j1aa = J1[p - 1] if p else None
        r["JAK1_wt"] = j1aa
        r["wt_conserved"] = (j1aa == wt) if j1aa else None
        r["is_self_sub"] = (j1aa == alt) if j1aa else None
        # ---- 3. the JAK1 equivalent, only where one is meaningful ----
        if j1aa and alt != "X" and j1aa != alt:
            eq = f"{j1aa}{p}{alt}"
            r["JAK1_equivalent"] = eq
            if eq in reb.index:
                r["EV1_cluster"] = int(reb.loc[eq, "cluster"])
                r["new_cluster"] = int(reb.loc[eq, "my_cluster"])
                for c, s in feat.items():
                    r[c] = s.get(eq)
        elif j1aa and alt == "X":
            r["JAK1_equivalent"] = f"{j1aa}{p}X"
        elif j1aa:
            r["JAK1_equivalent"] = f"{j1aa}{p}{alt}"
        rows.append(r)

T = pd.DataFrame(rows)
pd.set_option("display.width", 260, "display.max_columns", 60)

print("=== 1. wild-type check against JAK2 O60674 ===")
bad = T[~T.JAK2_wt_ok]
if len(bad):
    print(bad[["group", "JAK2", "JAK2_pos", "JAK2_actual_wt"]].to_string(index=False))
    print(f"  -> {len(bad)} variant(s) do NOT match the canonical sequence")
else:
    print(f"  all {len(T)} match")

print("\n=== 2. mapping and its support ===")
print(T[["group", "JAK2", "JAK1_pos", "JAK1_wt", "JAK1_equivalent", "wt_conserved",
         "is_self_sub", "is_nonsense", "domain(JAK1)", "local_id_11", "gaps_11",
         "unanimous", "positions_seen"]].to_string(index=False))

print("\n=== 3. where the JAK1 equivalent lands ===")
print(T[["group", "JAK2", "JAK1_equivalent", "EV1_cluster", "new_cluster", "alphamissense",
         "esm1b", "polyphen2_humvar_prob", "blosum62", "foldx_ddg"]].to_string(index=False))

# ---- 4. is Group 1 enriched in Cluster 2 above the 65% base rate? ----
print("\n=== 4. does the JAK1 clustering recognise the known GOF variants? ===")
base = (reb.my_cluster == 2).mean()
ev_base = (reb.cluster == 2).mean()
print(f"base rate of Cluster 2: rebuilt {base:.1%}, EV1 {ev_base:.1%}")
for lbl, cc, b in (("EV1", "EV1_cluster", ev_base), ("new", "new_cluster", base)):
    print(f"\n  {lbl} clustering:")
    for grp in ("1 reported GOF", "2 this study"):
        s = T[(T.group == grp) & T[cc].notna()][cc]
        if len(s) == 0:
            continue
        k = int((s == 2).sum())
        p = binomtest(k, len(s), b, alternative="greater").pvalue
        print(f"    {grp:16s} {k}/{len(s)} in Cluster 2 ({k/len(s):5.1%})   "
              f"binomial vs base rate p = {p:.3f}")
    g1 = T[(T.group == '1 reported GOF') & T[cc].notna()][cc]
    g2 = T[(T.group == '2 this study') & T[cc].notna()][cc]
    if len(g1) and len(g2):
        tab = [[int((g1 == 2).sum()), int((g1 == 1).sum())],
               [int((g2 == 2).sum()), int((g2 == 1).sum())]]
        print(f"    Group 1 vs Group 2: {tab}  Fisher p = {fisher_exact(tab)[1]:.3f}")

print("\n=== 5. mapping quality summary ===")
ok = T[T.JAK2_wt_ok]
print(f"  variants with a JAK1 position      {ok.JAK1_pos.notna().sum()}/{len(T)}")
print(f"  unanimous across 5 gap settings    {int(ok.unanimous.sum())}")
print(f"  NOT unanimous                      {int((~ok.unanimous.astype(bool)).sum())}")
print(f"  wild type conserved in JAK1        {int(ok.wt_conserved.sum())}")
print(f"  self-substitution in JAK1          {int(ok.is_self_sub.sum())}")
print(f"  local identity < 0.25 (unreliable) {int((ok.local_id_11 < 0.25).sum())}")
print(f"  with a cluster label               {int(ok.new_cluster.notna().sum())}")

# ---- 6. the same test, restricted to mappings that can be trusted ----
print("\n=== 6. restricted to trustworthy mappings ===")
print("   filters: wild type conserved AND local identity >= 0.25 AND unanimous across gap settings")
good = T[(T.wt_conserved == True) & (T.local_id_11 >= 0.25)
         & (T.unanimous == True) & T.new_cluster.notna()]
print(good[["group", "JAK2", "JAK1_equivalent", "EV1_cluster", "new_cluster",
            "alphamissense", "polyphen2_humvar_prob"]].to_string(index=False))
for lbl, cc, b in (("EV1", "EV1_cluster", ev_base), ("new", "new_cluster", base)):
    for grp in ("1 reported GOF", "2 this study"):
        s = good[good.group == grp][cc]
        if len(s) == 0:
            continue
        k = int((s == 2).sum())
        p = binomtest(k, len(s), b, alternative="greater").pvalue
        print(f"    {lbl} {grp:16s} {k}/{len(s)} in Cluster 2 ({k/len(s):4.0%})   p = {p:.3f}")
print("   NOTE: these filters were chosen after seeing that half the mappings were")
print("   non-conserved, so this is a post-hoc subgroup of 6 - suggestive, not established.")

# ---- 7. how do the known GOF variants score, as a set? ----
print("\n=== 7. do the predictors recognise the known GOF variants? ===")
am_all = feat["alphamissense"].dropna()
g1 = T[(T.group == "1 reported GOF") & T.alphamissense.notna()]
print(f"  median AlphaMissense, the {len(g1)} known GOF equivalents: {g1.alphamissense.median():.3f}")
print(f"  median AlphaMissense, all {len(am_all):,} JAK1 substitutions:  {am_all.median():.3f}")
print(f"  below AlphaMissense's own 0.34 benign cutoff: "
      f"{int((g1.alphamissense < 0.34).sum())}/{len(g1)}")
print(f"  median PolyPhen-2 HumVar: {g1.polyphen2_humvar_prob.median():.3f}; "
      f"above 0.93: {int((g1.polyphen2_humvar_prob > 0.93).sum())}/{len(g1)}")
print("\n  per variant, with percentile within all JAK1 substitutions:")
for _, r in g1.sort_values("alphamissense").iterrows():
    print(f"    {r.JAK2:7s} -> {r.JAK1_equivalent:8s} AlphaMissense {r.alphamissense:.4f} "
          f"= {(am_all < r.alphamissense).mean():5.1%} pct   PolyPhen-2 {r.polyphen2_humvar_prob:.3f}")

print("\n  Group 1 against Group 2 on each feature:")
mm = T[T.alphamissense.notna()]
for c in ("alphamissense", "esm1b", "polyphen2_humvar_prob", "foldx_ddg"):
    x = mm[mm.group == "1 reported GOF"][c].dropna()
    y = mm[mm.group == "2 this study"][c].dropna()
    if len(x) > 2 and len(y) > 2:
        print(f"    {c:24s} G1 median {x.median():8.3f}   G2 median {y.median():8.3f}   "
              f"Mann-Whitney p = {mannwhitneyu(x, y).pvalue:.3f}")

print("\n=== 8. Group 2 on its own, in the order given ===")
g2 = T[T.group == "2 this study"].copy()           # GROUP2's own order is preserved throughout
g2cols = ["JAK2", "JAK1_pos", "JAK1_wt", "JAK1_equivalent", "wt_conserved", "is_self_sub",
          "is_nonsense", "local_id_11", "gaps_11", "unanimous", "positions_seen",
          "domain(JAK1)", "EV1_cluster", "new_cluster", "alphamissense", "esm1b",
          "polyphen2_humvar_prob", "sift", "cadd_phred", "clinpred", "blosum62", "foldx_ddg"]
print(g2[g2cols].to_string(index=False))
g2[g2cols].to_csv(HERE / "jak2_group2_to_jak1.csv", index=False)

T.to_csv(HERE / "jak2_groups_to_jak1.csv", index=False)
print("\nwrote jak2_groups_to_jak1.csv and jak2_group2_to_jak1.csv")
