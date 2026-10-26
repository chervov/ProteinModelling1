# Mean ddG by target amino acid (the substituted-in residue)

*TYK2: 22,536 variants on the matched AF3 pair. JAK1: 21,926 on the Jeanpierre pair.*
*Sign convention ddG = dG_WT - dG_mut, so **negative = destabilizing**.*

**Raw values are not free energies.** 26.9% of TYK2 values fall below -10 and the minimum is
-3048; these are steric-clash penalties from inserting a side chain into a rigid backbone, not
thermodynamic quantities. Only the *ordering* is meaningful. Both raw and clipped columns are
given so the clipping is visible rather than silent.

## TYK2

| target | | n | raw mean | raw median | raw min | % < -10 | clipped mean | clipped SD | clipped open | open-closed | vol A^3 | hydropathy |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **P** | Pro | 1,105 | -177.6 | -190.05 | -783 | 87% | -9.05 | 2.83 | -8.97 | +0.079 | 113 | -1.6 |
| **W** | Trp | 1,163 | -172.4 | -7.04 | -3048 | 45% | -6.45 | 3.73 | -6.32 | +0.131 | 228 | -0.9 |
| **F** | Phe | 1,140 | -124.4 | -5.31 | -2902 | 41% | -5.59 | 4.28 | -5.35 | +0.236 | 190 | +2.8 |
| **I** | Ile | 1,145 | -46.1 | -6.05 | -2091 | 43% | -5.57 | 4.51 | -5.29 | +0.281 | 167 | +4.5 |
| **Y** | Tyr | 1,152 | -158.9 | -5.59 | -2608 | 42% | -5.55 | 4.40 | -5.31 | +0.244 | 194 | -1.3 |
| **V** | Val | 1,112 | -26.2 | -4.94 | -1376 | 38% | -5.18 | 4.48 | -4.97 | +0.215 | 140 | +4.2 |
| **R** | Arg | 1,100 | -58.5 | -4.68 | -2568 | 34% | -5.11 | 4.38 | -4.79 | +0.317 | 173 | -4.5 |
| **G** | Gly | 1,096 | -3.8 | -4.31 | -19 | 11% | -4.63 | 3.59 | -4.53 | +0.103 | 60 | -0.4 |
| **H** | His | 1,136 | -46.4 | -3.62 | -2463 | 30% | -4.58 | 4.35 | -4.39 | +0.188 | 153 | -3.2 |
| **L** | Leu | 1,049 | -47.5 | -3.58 | -1995 | 34% | -4.58 | 4.63 | -4.27 | +0.310 | 167 | +3.8 |
| **K** | Lys | 1,141 | -34.5 | -4.06 | -2430 | 32% | -4.49 | 4.72 | -4.14 | +0.342 | 169 | -3.9 |
| **M** | Met | 1,161 | -25.5 | -3.31 | -2295 | 21% | -4.25 | 3.94 | -4.05 | +0.202 | 163 | +1.9 |
| **C** | Cys | 1,155 | -8.9 | -3.63 | -733 | 7% | -3.99 | 3.27 | -3.91 | +0.075 | 108 | +2.5 |
| **D** | Asp | 1,131 | -9.7 | -3.49 | -1098 | 11% | -3.88 | 4.03 | -3.75 | +0.120 | 111 | -3.5 |
| **E** | Glu | 1,101 | -18.5 | -3.29 | -1801 | 19% | -3.85 | 4.42 | -3.59 | +0.260 | 138 | -3.5 |
| **Q** | Gln | 1,135 | -21.8 | -2.59 | -2202 | 16% | -3.54 | 4.24 | -3.29 | +0.242 | 144 | -3.5 |
| **T** | Thr | 1,139 | -10.8 | -3.02 | -922 | 12% | -3.53 | 3.92 | -3.35 | +0.180 | 116 | -0.7 |
| **N** | Asn | 1,161 | -10.8 | -2.68 | -1473 | 7% | -3.12 | 3.77 | -3.01 | +0.112 | 114 | -3.5 |
| **S** | Ser | 1,110 | -3.7 | -2.00 | -329 | 4% | -2.60 | 3.58 | -2.49 | +0.106 | 89 | -0.8 |
| **A** | Ala | 1,104 | -3.3 | -1.91 | -258 | 4% | -2.50 | 3.57 | -2.44 | +0.061 | 89 | +1.8 |

## JAK1

| target | | n | raw mean | raw median | raw min | % < -10 | clipped mean | clipped SD | clipped open | open-closed | vol A^3 | hydropathy |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **P** | Pro | 1,102 | -177.3 | -188.53 | -780 | 88% | -9.11 | 2.82 | -9.16 | -0.058 | 113 | -1.6 |
| **W** | Trp | 1,139 | -202.2 | -7.95 | -2936 | 46% | -6.53 | 3.78 | -6.57 | -0.040 | 228 | -0.9 |
| **Y** | Tyr | 1,109 | -163.6 | -6.45 | -2441 | 45% | -5.85 | 4.33 | -5.88 | -0.030 | 194 | -1.3 |
| **F** | Phe | 1,110 | -126.6 | -5.83 | -2286 | 44% | -5.77 | 4.30 | -5.85 | -0.087 | 190 | +2.8 |
| **I** | Ile | 1,088 | -47.9 | -5.64 | -1665 | 42% | -5.45 | 4.57 | -5.84 | -0.395 | 167 | +4.5 |
| **V** | Val | 1,089 | -26.2 | -4.36 | -1119 | 36% | -5.02 | 4.51 | -5.37 | -0.346 | 140 | +4.2 |
| **R** | Arg | 1,097 | -60.3 | -4.22 | -2762 | 32% | -4.86 | 4.36 | -4.94 | -0.083 | 173 | -4.5 |
| **H** | His | 1,120 | -44.6 | -3.59 | -2118 | 30% | -4.58 | 4.40 | -4.69 | -0.113 | 153 | -3.2 |
| **K** | Lys | 1,050 | -37.6 | -4.14 | -2480 | 32% | -4.56 | 4.75 | -4.64 | -0.081 | 169 | -3.9 |
| **G** | Gly | 1,097 | -4.0 | -4.08 | -18 | 10% | -4.35 | 3.86 | -4.48 | -0.135 | 60 | -0.4 |
| **L** | Leu | 1,042 | -51.7 | -3.10 | -1663 | 32% | -4.34 | 4.71 | -4.58 | -0.237 | 167 | +3.8 |
| **M** | Met | 1,120 | -26.8 | -3.15 | -2128 | 21% | -4.12 | 4.14 | -4.28 | -0.162 | 163 | +1.9 |
| **D** | Asp | 1,089 | -9.3 | -3.43 | -778 | 12% | -3.74 | 4.18 | -3.93 | -0.191 | 111 | -3.5 |
| **E** | Glu | 1,059 | -16.8 | -3.09 | -1309 | 18% | -3.74 | 4.40 | -3.88 | -0.146 | 138 | -3.5 |
| **C** | Cys | 1,122 | -7.8 | -3.44 | -714 | 6% | -3.72 | 3.32 | -3.81 | -0.096 | 108 | +2.5 |
| **Q** | Gln | 1,113 | -20.4 | -2.45 | -1623 | 17% | -3.31 | 4.30 | -3.44 | -0.131 | 144 | -3.5 |
| **T** | Thr | 1,100 | -9.6 | -2.61 | -761 | 10% | -3.23 | 3.94 | -3.47 | -0.241 | 116 | -0.7 |
| **N** | Asn | 1,095 | -10.8 | -2.67 | -1112 | 8% | -3.05 | 3.90 | -3.17 | -0.126 | 114 | -3.5 |
| **S** | Ser | 1,081 | -3.5 | -1.91 | -359 | 3% | -2.38 | 3.69 | -2.49 | -0.116 | 89 | -0.8 |
| **A** | Ala | 1,104 | -2.9 | -1.83 | -245 | 3% | -2.18 | 3.61 | -2.26 | -0.080 | 89 | +1.8 |

---

## The 20 target residues fall into two groups

Sorting the raw means reveals a single dominant break, and it is the same in both proteins:

| protein | largest gap in the sorted means | next largest | k-means on the 20 means |
|---|---|---|---|
| TYK2 | **65.9** between F (−124.4) and R (−58.5) | 34.6 (Y–F) | **FPWY** \| rest |
| JAK1 | **66.4** between F (−126.6) and R (−60.3) | 37.0 (Y–F) | **FPWY** \| rest |

The gap after phenylalanine is roughly twice the next largest, and k-means on the 20 means recovers
the same four residues without being told where to cut. Two different proteins, scored on unrelated
structure pairs (AF3 for TYK2, Jeanpierre's models for JAK1), give the identical partition.

| group | residues | mean ddG_closed, TYK2 | volume range |
|---|---|--:|--:|
| **High** | **P, W, Y, F** | −124 to −178 | 113–228 Å³ |
| Low | A C D E G H I K L M N Q R S T V | −3 to −59 | 60–174 Å³ |

### It is one group formed by two different mechanisms

Three of the four are the largest aromatics — Trp 228 Å³, Tyr 194, Phe 190 — which is the steric
story: a bulky side chain cannot be accommodated in a fixed backbone, so `fa_rep` dominates
(measured directly in `conclusions_ddG_difference_feature.md` §9, where the extreme values are
~100% repulsive term).

**Proline is only 113 Å³** — smaller than arginine (173) or leucine (167), both of which sit
comfortably in the low group. It reaches the high group by a different route: it has no backbone
N–H to donate a hydrogen bond, and its ring locks φ near −60°, so it is incompatible with regular
secondary structure wherever it lands. That is why the volume correlation is **r = −0.62** across
all 20 residues but **−0.84 once proline is excluded** (§8.1 of the conclusions document).

The DMS agrees that proline is the worst destination residue experimentally — rank 1 of 20 on
abundance, on signalling, and on fraction loss-of-function — and the computed penalty tracks burial
as the mechanism predicts (median −221 buried, −47 very exposed, against −4.9 and −1.2 for alanine).

### Caveat: the split is a property of the raw values

On clipped values the boundary softens and the two proteins stop agreeing: k-means gives **FIPRVWY**
for TYK2 and **FIPWY** for JAK1. The clean partition describes **how often a substitution clashes
catastrophically**, not how bad a typical substitution is. Use it to reason about the clash tail,
not as a general damage classification.
