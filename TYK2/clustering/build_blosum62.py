"""BLOSUM62 substitution scores for TYK2 — computed locally, not fetched.

BLOSUM62 is a 20x20 lookup table (Henikoff & Henikoff, PNAS 1992), so there is nothing to
download and nothing can be missing: every substitution has a score. It is the only feature in
the paper's eleven that is **position-blind** — every V->F in TYK2 scores -1 wherever it sits.

The matrix is taken from Biopython's `substitution_matrices`, which ships the NCBI table, and is
cross-checked against an independently written copy of the published matrix so a silent version
difference cannot pass. Self-substitutions would take the diagonal (a real value, A->A = 4) but
this directory's universe excludes them, so the file has no blanks and no diagonal entries.

Writes tyk2_blosum62.csv.
"""
import csv
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
ACC = "P29597"

# The published BLOSUM62, written out here so the Biopython value can be checked against an
# independent copy rather than trusted. Rows and columns in this order.
ORDER = "ARNDCQEGHILKMFPSTWYV"
REFERENCE = """
 4 -1 -2 -2  0 -1 -1  0 -2 -1 -1 -1 -1 -2 -1  1  0 -3 -2  0
-1  5  0 -2 -3  1  0 -2  0 -3 -2  2 -1 -3 -2 -1 -1 -3 -2 -3
-2  0  6  1 -3  0  0  0  1 -3 -3  0 -2 -3 -2  1  0 -4 -2 -3
-2 -2  1  6 -3  0  2 -1 -1 -3 -4 -1 -3 -3 -1  0 -1 -4 -3 -3
 0 -3 -3 -3  9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
-1  1  0  0 -3  5  2 -2  0 -3 -2  1  0 -3 -1  0 -1 -2 -1 -2
-1  0  0  2 -4  2  5 -2  0 -3 -3  1 -2 -3 -1  0 -1 -3 -2 -2
 0 -2  0 -1 -3 -2 -2  6 -2 -4 -4 -2 -3 -3 -2  0 -2 -2 -3 -3
-2  0  1 -1 -3  0  0 -2  8 -3 -3 -1 -2 -1 -2 -1 -2 -2  2 -3
-1 -3 -3 -3 -1 -3 -3 -4 -3  4  2 -3  1  0 -3 -2 -1 -3 -1  3
-1 -2 -3 -4 -1 -2 -3 -4 -3  2  4 -2  2  0 -3 -2 -1 -2 -1  1
-1  2  0 -1 -3  1  1 -2 -1 -3 -2  5 -1 -3 -1  0 -1 -3 -2 -2
-1 -1 -2 -3 -1  0 -2 -3 -2  1  2 -1  5  0 -2 -1 -1 -1 -1  1
-2 -3 -3 -3 -2 -3 -3 -3 -1  0  0 -3  0  6 -4 -2 -2  1  3 -1
-1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4  7 -1 -1 -4 -3 -2
 1 -1  1  0 -1  0  0  0 -1 -2 -2  0 -1 -2 -1  4  1 -3 -2 -2
 0 -1  0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1  1  5 -2 -2  0
-3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1  1 -4 -3 -2 11  2 -3
-2 -2 -2 -3 -2 -1 -2 -3  2 -1 -1 -2 -1  3 -3 -2 -2  2  7 -1
 0 -3 -3 -3 -1 -2 -2 -3 -3  3  1 -2  1 -1 -2 -2  0 -3 -1  4
"""


def reference_matrix():
    rows = [r.split() for r in REFERENCE.strip().splitlines()]
    return {(a, b): int(rows[i][j])
            for i, a in enumerate(ORDER) for j, b in enumerate(ORDER)}


def main():
    ref = reference_matrix()
    try:
        from Bio.Align import substitution_matrices
        bio = substitution_matrices.load("BLOSUM62")
        disagree = [(a, b) for a in ORDER for b in ORDER if int(bio[a][b]) != ref[(a, b)]]
        if disagree:
            sys.exit(f"Biopython BLOSUM62 differs from the published matrix at "
                     f"{len(disagree)} cells, e.g. {disagree[:5]}")
        print(f"matrix: Biopython agrees with the published BLOSUM62 at all "
              f"{len(ORDER)**2} cells")
        score = lambda w, a: int(bio[w][a])
    except ImportError:
        print("matrix: Biopython not available, using the embedded published matrix")
        score = lambda w, a: ref[(w, a)]

    seq = (HERE / f"TYK2_{ACC}_1187aa.txt").read_text().splitlines()[1]
    universe = [r["variant"] for r in csv.DictReader(open(HERE / "tyk2_variant_universe.csv"))]

    out = HERE / "tyk2_blosum62.csv"
    vals = []
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["index", "variant", "wt", "pos", "alt", "blosum62"])
        for i, v in enumerate(universe, 1):
            wt, pos, alt = v[0], int(v[1:-1]), v[-1]
            if seq[pos - 1] != wt:
                sys.exit(f"{v}: sequence has {seq[pos-1]} at {pos}")
            s = score(wt, alt)
            vals.append(s)
            w.writerow([i, v, wt, pos, alt, s])

    import collections
    dist = collections.Counter(vals)
    print(f"\nwrote {out.name}: {len(universe):,} rows in universe order, "
          f"{len(vals):,} populated (100.00%) - a lookup can never be missing")
    print(f"  range {min(vals)} .. {max(vals)}; lower = less conservative substitution")
    print("  distribution: " + "  ".join(f"{k}:{dist[k]:,}" for k in sorted(dist)))
    print(f"  position-blind: every V>F scores {score('V','F')} wherever it occurs "
          f"({sum(1 for v in universe if v[0]=='V' and v[-1]=='F'):,} of them in TYK2)")


if __name__ == "__main__":
    main()
