# JAK2 priority variants mapped to JAK1, JAK3 and TYK2

Pairwise global alignment of the UniProt canonical sequences (JAK2 O60674 vs JAK1 P23458, JAK3 P52333, TYK2 P29597; Gotoh algorithm, BLOSUM62, gap open 11 / extend 1). Identity to JAK2: JAK1 46.6%, JAK3 50.4%, TYK2 42.4%.
Sanity check - known equivalent residues align: JAK2 V617 = JAK1 V658 = JAK3 M592 = TYK2 V678; JAK2 R683 = JAK1 R724 = JAK3 R657 = TYK2 R744; catalytic K882 = JAK1 K908 = JAK3 K855 = TYK2 K930.
Full position map: [`jak_alignment_position_map.csv`](jak_alignment_position_map.csv) (one row per JAK2 residue). Sequences: [`jak_sequences.fasta`](jak_sequences.fasta).

## Summary

| JAK2 | JAK1 | JAK3 | TYK2 | Region | Paralog evidence | Reading |
|---|---|---|---|---|---|---|
| **G571R** | S612 (uncertain) | G546 | G634 | Variable loop, JH2 N-lobe (gapped alignment) | Equivalent Gly->Arg scores benign in JAK3/TYK2 (AlphaMissense 0.12 / 0.11); TYK2 DMS G634R -0.05 +- 0.25 (no effect); TYK2 G634E is ClinVar likely benign (gnomAD AC 123) | Position tolerates change across the family; older tools' "damaging" call is not supported |
| **V578I** | V619 | V553 | V639 | Conserved strand `EVLLKVLD` | Val conserved in all four; Ile mild everywhere (AlphaMissense 0.20-0.36); TYK2 DMS V639I -0.09 +- 0.27 | Probably tolerated |
| **L805I** | **I845** | L777 | L866 | Conserved helix at the end of JH2 (`RAIIRDLNSL`) | JAK1 naturally has Ile here; TYK2 DMS L866I **+0.57 +- 0.33** (highest at that position, ~top 5% of the scan = more signalling) | Only variant with a hint of gain of function (weak, ~1.7 SE) - first candidate for testing |
| **V1110E** | P1136 | P1082 | A1156 | Variable, C-terminal end of JH1 | Not conserved (Pro/Pro/Ala); TYK2 DMS A1156E -0.08 +- 0.35 | Probably tolerated |

DMS = TYK2 deep mutational scan, IFN-alpha signalling (MaveDB urn:mavedb:00001270-a-6; negative = loss of function). See [`scores_interpretation.md`](scores_interpretation.md) for score thresholds. Variant counts below come from ClinVar, gnomAD v4 (AC = allele count) and cBioPortal; tumour-database counts from licensed sources are not shown.

## Details per variant

Alignment windows show 6 residues either side; `-` = gap. "Position mean AlphaMissense" averages all 19 substitutions at that residue (high = constrained position).
### JAK2 G571R

```
JAK2  REVGDYGQLHETE  (centre = 571)
JAK1  MDYKDTSEEKKIK  (centre = 612)
JAK3  HEVVD-GEARKTE  (centre = 546)
TYK2  RVEGDRGQ--ELR  (centre = 634)
```

| Gene | Residue | Same substitution | AlphaMissense (same subst.) | Position mean AlphaMissense | Variants reported at this position |
|---|---|---|---|---|---|
| JAK2 | G571 | G571R | 0.27 | 0.35 | **G571R** (gnomAD AC 1)<br>**G571S** (ClinVar Conflicting classifications of pathogenicity; gnomAD AC 571; cBio 11)<br>**G571A** (gnomAD AC 1)<br>**G571C** (gnomAD AC 1)<br>**G571D** (cBio 1)<br>**G571Vfs*10** (gnomAD AC 1) |
| JAK1 | S612 | S612R | 0.13 | 0.09 | **S612A** (cBio 2)<br>**S612F** (cBio 2) |
| JAK3 | G546 | G546R | 0.12 | 0.21 | **G546E** (gnomAD AC 6)<br>**G546R** (gnomAD AC 1; cBio 1)<br>**G546W** (gnomAD AC 1) |
| TYK2 | G634 | G634R | 0.11 | 0.14 | **G634E** (ClinVar Likely benign; gnomAD AC 123)<br>**G634A** (gnomAD AC 22)<br>**G634W** (gnomAD AC 1) DMS signalling: same substitution -0.05 +- 0.25; range at position -2.44 to 0.67. |

### JAK2 V578I

```
JAK2  QLHETEVLLKVLD  (centre = 578)
JAK1  EEKKIKVILKVLD  (centre = 619)
JAK3  EARKTEVLLKVMD  (centre = 553)
TYK2  Q--ELRVVLKVLD  (centre = 639)
```

| Gene | Residue | Same substitution | AlphaMissense (same subst.) | Position mean AlphaMissense | Variants reported at this position |
|---|---|---|---|---|---|
| JAK2 | V578 | V578I | 0.24 | 0.89 | **V578I** (gnomAD AC 1)<br>**V578F** (ClinVar Uncertain significance; gnomAD AC 2) |
| JAK1 | V619 | V619I | 0.36 | 0.93 | none |
| JAK3 | V553 | V553I | 0.20 | 0.83 | **V553fs** (ClinVar Likely pathogenic)<br>**V553M** (gnomAD AC 1) |
| TYK2 | V639 | V639I | 0.33 | 0.87 | none DMS signalling: same substitution -0.09 +- 0.27; range at position -2.47 to 0.67. |

### JAK2 L805I

```
JAK2  RAIIRDLNSLFTP  (centre = 805)
JAK1  RAIMRDINKLEEQ  (centre = 845)
JAK3  RAVIRDLNSLISS  (centre = 777)
TYK2  RTILRDLTRLQPH  (centre = 866)
```

| Gene | Residue | Same substitution | AlphaMissense (same subst.) | Position mean AlphaMissense | Variants reported at this position |
|---|---|---|---|---|---|
| JAK2 | L805 | L805I | 0.15 | 0.83 | **L805I** (gnomAD AC 15; cBio 1) |
| JAK1 | I845 | already I | - | 0.82 | **I845del** (cBio 2)<br>**I845V** (ClinVar Uncertain significance; gnomAD AC 12) |
| JAK3 | L777 | L777I | 0.11 | 0.80 | **L777F** (gnomAD AC 1)<br>**L777P** (gnomAD AC 2; cBio 1) |
| TYK2 | L866 | L866I | 0.11 | 0.70 | **L866F** (gnomAD AC 1) DMS signalling: same substitution 0.57 +- 0.33; range at position -2.79 to 0.57. |

### JAK2 V1110E

```
JAK2  ECWNNNVNQRPSF  (centre = 1110)
JAK1  KCWEFQPSNRTSF  (centre = 1136)
JAK3  LCWAPSPQDRPSF  (centre = 1082)
TYK2  NCWETEASFRPTF  (centre = 1156)
```

| Gene | Residue | Same substitution | AlphaMissense (same subst.) | Position mean AlphaMissense | Variants reported at this position |
|---|---|---|---|---|---|
| JAK2 | V1110 | V1110E | 0.29 | 0.23 | **V1110E** (requested variant)<br>**V1110I** (cBio 1)<br>**V1110L** (gnomAD AC 2; cBio 1) |
| JAK1 | P1136 | P1136E | 0.69 | 0.68 | **P1136S** (gnomAD AC 1) |
| JAK3 | P1082 | P1082E | 0.47 | 0.38 | **P1082L** (cBio 2)<br>**P1082T** (gnomAD AC 1) |
| TYK2 | A1156 | A1156E | 0.46 | 0.46 | **A1156V** (gnomAD AC 14; cBio 2) DMS signalling: same substitution -0.08 +- 0.35; range at position -2.31 to 0.34. |

