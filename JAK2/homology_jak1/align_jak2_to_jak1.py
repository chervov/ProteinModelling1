"""Map four JAK2 variants onto JAK1 by sequence alignment, two independent ways.

The repository already holds a JAK-family alignment position map; that is read and used, but a
fresh pairwise global alignment is also computed here so the two can be compared. An alignment
is an inference, not a fact, and a position mapping that only one method supports should not be
relied on.
"""
import pathlib

import pandas as pd
from Bio import Align
from Bio.Align import substitution_matrices

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent.parent                      # repository root, from JAK2/homology_jak1/
# inputs live in external_data/ in the repository; fall back to this directory if run standalone
EXT = ROOT / "external_data" if (ROOT / "external_data").is_dir() else HERE
VARIANTS = ["V1110E", "G571R", "V578I", "L805I", "V617F"]   # V617F included as the known control

seqs, name = {}, None
for line in (EXT / "jak_sequences.fasta").read_text().splitlines():
    if line.startswith(">"):
        name = line[1:].strip()
        seqs[name] = ""
    elif name:
        seqs[name] += line.strip()
for k, v in seqs.items():
    print(f"{k:5s} {len(v):5,} aa   starts {v[:12]}")

J2, J1 = seqs["JAK2"], seqs["JAK1"]

# ---- 1. the alignment map already in the repository ----------------------------
m = pd.read_csv(EXT / "jak_alignment_position_map.csv")
m = m[m.JAK2_pos.astype(str).str.isdigit()].copy()
m["JAK2_pos"] = m.JAK2_pos.astype(int)
repo = m.set_index("JAK2_pos")

# ---- 2. an independent pairwise global alignment --------------------------------
al = Align.PairwiseAligner(scoring="blastp")
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -11, -1
aln = al.align(J2, J1)[0]
print(f"\nindependent global alignment: score {aln.score:,.0f}")
pairs = {}                                   # JAK2 pos (1-based) -> JAK1 pos or None
i = j = 0
a2, a1 = str(aln[0]), str(aln[1])
ident = gaps = 0
for c2, c1 in zip(a2, a1):
    if c2 != "-":
        i += 1
    if c1 != "-":
        j += 1
    if c2 != "-":
        pairs[i] = j if c1 != "-" else None
        if c1 == "-":
            gaps += 1
        elif c1 == c2:
            ident += 1
print(f"  aligned length {len(a2):,}; JAK2 residues identical to JAK1: "
      f"{ident:,}/{len(J2):,} ({ident/len(J2):.1%}); JAK2 residues facing a gap: {gaps}")

# ---- 3. map the variants --------------------------------------------------------
rows = []
for v in VARIANTS:
    wt, pos, alt = v[0], int(v[1:-1]), v[-1]
    ok2 = J2[pos - 1] == wt
    p_ind = pairs.get(pos)
    r = repo.loc[pos] if pos in repo.index else None
    p_repo = (int(r.JAK1_pos) if r is not None and str(r.JAK1_pos).replace(".0", "").isdigit() else None)
    j1_ind = J1[p_ind - 1] if p_ind else None
    rows.append({
        "JAK2_variant": v,
        "JAK2_wt_ok": ok2,
        "repo_JAK1_pos": p_repo,
        "indep_JAK1_pos": p_ind,
        "agree": p_repo == p_ind,
        "JAK1_aa": j1_ind,
        "conserved": (j1_ind == wt) if j1_ind else None,
        "JAK1_equivalent": f"{j1_ind}{p_ind}{alt}" if j1_ind else None,
    })
out = pd.DataFrame(rows)
print("\n" + out.to_string(index=False))
out.to_csv(HERE / "jak2_to_jak1_mapping.csv", index=False)

# ---- 4. local sequence context, which is what makes a mapping believable --------
print("\nlocal context (JAK2 above, JAK1 below, +/- 10 residues around the aligned position)")
for v in VARIANTS:
    wt, pos, alt = v[0], int(v[1:-1]), v[-1]
    p = pairs.get(pos)
    if not p:
        print(f"\n{v}: aligns to a gap")
        continue
    # find the alignment column for this JAK2 position so both strings stay in register
    k = i2 = 0
    for k, c2 in enumerate(a2):
        if c2 != "-":
            i2 += 1
            if i2 == pos:
                break
    lo, hi = max(0, k - 10), k + 11
    bar = "".join("|" if x == y and x != "-" else " " for x, y in zip(a2[lo:hi], a1[lo:hi]))
    print(f"\n{v} -> JAK1 {J1[p-1]}{p}{alt}   (JAK2 {pos}, JAK1 {p})")
    print(f"  JAK2 {a2[lo:hi]}")
    print(f"       {bar}")
    print(f"  JAK1 {a1[lo:hi]}")
    print(f"       {' ' * (k - lo)}^")
