# JAK2 priority variants: homology analysis with JAK1, JAK3 and TYK2

Variants: **G571R, V578I, L805I, V1110E** (JAK2, O60674 / NM_004972). Data retrieved 24-25 Oct 2026.

Alignment: pairwise global alignment of UniProt canonical sequences (Gotoh, BLOSUM62, gap open 11 / extend 1); identity to JAK2: JAK1 46.6%, JAK3 50.4%, TYK2 42.4%. Known equivalents align correctly (JAK2 V617 = JAK1 V658 = JAK3 M592 = TYK2 V678; R683 = JAK1 R724; catalytic K882 = JAK1 K908). Full map: [`jak_alignment_position_map.csv`](../jak_alignment_position_map.csv); score thresholds: [`scores_interpretation.md`](../scores_interpretation.md).

## Summary

| JAK2 | JAK1 | JAK3 | TYK2 | Location | Key evidence | Reading |
|---|---|---|---|---|---|---|
| **G571R** | S612 (uncertain) | G546 | G634 | JH2 loop next to inhibitory pY570 | Gly->Arg benign in JAK3/TYK2; TYK2 G634R no effect (-0.05); G571S at same residue likely neutral | Probably tolerated; only a JAK2-specific Y570 effect is plausible |
| **V578I** | V619 | V553 | V639 | JH2 beta3 strand, 3 residues before ATP-binding K581 | Constrained position, but Val->Ile mild everywhere; TYK2 V639I no effect (-0.09) | Probably tolerated |
| **L805I** | **I845** | L777 | L866 | Last JH2 helix, before JH2-JH1 linker | JAK1 has Ile natively; **TYK2 L866I +0.57 +- 0.33 (more signalling)** | Weak hint of gain of function - test first |
| **V1110E** | P1136 | P1082 | A1156 | C-terminal end of JH1 | Variable position; TYK2 A1156E no effect (-0.08) | Probably tolerated |

**Suggested testing order:** L805I > G571R > V578I > V1110E, in a JAK2 assay that detects activation (STAT5 reporter or cytokine-independent Ba/F3-EPOR growth, without and with EPO), with WT and V617F as controls and K581A (JH2 ATP-binding dead) as a mechanistic control for V578I.

> Caveat: all predictors score damaging-versus-tolerated and cannot detect gain of function, the mechanism of JAK2 disease. The TYK2 scan measures IFN-alpha-stimulated minus baseline signalling and may also under-detect constitutive activation (TYK2 V678F, the V617F equivalent, scores -0.12).

## JAK2 G571R

**Location.** JH2 N-lobe, variable loop immediately after **Y570**, the inhibitory JAK2 autophosphorylation site (phospho-Y570 down-regulates JAK2 activity). The loop is not conserved: Y570 has no counterpart in JAK1 (T611), JAK3 (gap) or TYK2 (R633), and the JAK1 match for G571 (S612) is uncertain because of an insertion. Gly is kept in JAK3 (G546) and TYK2 (G634).

**Literature.** **G571S** (same residue) is the best-studied variant here: proposed to disturb Y570 phosphorylation, but classical assays did not show STAT5 activation; found in 3 of ~20,000 suspected-MPN samples; in a family it was carried by relatives with normal blood counts and judged a likely non-functional polymorphism (ClinVar: conflicting; gnomAD 571 alleles). Nothing published on G571R.

### Alignment and variants reported at the equivalent positions

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

### Predictor scores - same substitution at each equivalent residue

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK2 | G571R | 0.27 (LB) | 0.87 | 33.0 | 0.002 | 0.966 | 0.90 | -9.5 | 0.38 | - |
| JAK1 | S612R | 0.13 (LB) | - | - | - | - | - | - | - | - |
| JAK3 | G546R | 0.12 (LB) | 0.33 | 19.1 | 0.022 | 0.447 | 0.32 | -7.6 | 0.17 | - |
| TYK2 | G634R | 0.11 (LB) | 0.31 | 9.9 | 0.107 | 0.677 | 0.17 | -6.3 | - | -0.05 +- 0.25 |

### Predictor scores - variants reported at these positions

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK2 | G571S | 0.11 (LB) | 0.69 | 26.7 | 0.175 | 0.766 | 0.53 | -7.8 | 0.27 | - |
| JAK2 | G571A | 0.21 (LB) | 0.73 | 26.7 | 0.014 | 0.814 | 0.84 | -9.4 | 0.58 | - |
| JAK2 | G571C | 0.19 (LB) | 0.87 | 33.0 | 0.001 | 0.991 | 0.90 | -11.1 | 0.46 | - |
| JAK2 | G571D | 0.15 (LB) | 0.66 | 25.3 | 0.081 | 0.133 | 0.84 | -8.4 | 0.18 | - |
| JAK1 | S612A | 0.06 (LB) | 0.08 | 0.2 | 0.331 | 0.007 | 0.12 | -4.2 | - | - |
| JAK1 | S612F | 0.10 (LB) | 0.33 | 22.5 | 0.011 | 0.361 | 0.45 | -5.3 | - | - |
| JAK3 | G546E | 0.11 (LB) | 0.24 | 17.5 | 0.021 | 0.584 | 0.25 | -7.9 | 0.10 | - |
| JAK3 | G546W | 0.22 (LB) | 0.55 | 26.9 | 0.000 | 0.999 | 0.77 | -9.4 | 0.51 | - |
| TYK2 | G634E | 0.09 (LB) | 0.29 | 5.0 | 0.325 | 0.946 | 0.01 | -7.1 | - | 0.04 +- 0.20 |
| TYK2 | G634A | 0.09 (LB) | 0.36 | 0.6 | 0.170 | 0.844 | 0.16 | -5.5 | - | 0.09 +- 0.32 |
| TYK2 | G634W | 0.13 (LB) | 0.41 | 23.1 | 0.008 | 0.998 | 0.66 | -6.6 | - | -0.12 +- 0.23 |

**Reading.** Most tools call G571R damaging (REVEL 0.87, CADD 33), but AlphaMissense (0.27) and EVE (0.38) do not, the equivalent Gly->Arg is benign by every tool in JAK3 and TYK2, and in TYK2 it has **no measured effect (-0.05 +- 0.25)**. The well-studied neighbour G571S looks neutral. The only mechanism worth testing is an effect on Y570 phosphorylation, which is JAK2-specific.

## JAK2 V578I

**Location.** JH2 N-lobe **beta3 strand** (`EVLLKVLD`), three residues before **K581**, the JH2 lysine that coordinates ATP. V578 is conserved in all four JAKs (JAK1 V619, JAK3 V553, TYK2 V639); the equivalent K581 is JAK1 K622, JAK3 K556 and TYK2 K642. JH2 ATP binding stabilises JH2 (especially alphaC) and is required for V617F hyperactivation (Hammaren et al., PNAS 2015).

**Literature.** No publication on V578I or the equivalent residues. JAK2 V578F is in ClinVar (uncertain significance).

### Alignment and variants reported at the equivalent positions

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

### Predictor scores - same substitution at each equivalent residue

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK2 | V578I | 0.24 (LB) | 0.62 | 29.3 | 0.000 | 0.999 | 0.96 | -7.8 | 0.72 | - |
| JAK1 | V619I | 0.36 (amb) | - | - | - | - | - | - | - | - |
| JAK3 | V553I | 0.20 (LB) | - | - | - | - | - | - | - | - |
| TYK2 | V639I | 0.33 (LB) | - | - | - | - | - | - | - | -0.09 +- 0.27 |

### Predictor scores - variants reported at these positions

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK2 | V578F | 0.90 (LP) | 0.93 | 31.0 | 0.000 | 1.000 | 0.99 | -15.8 | 0.77 | - |
| JAK3 | V553M | 0.63 (LP) | 0.83 | 26.2 | 0.000 | 0.997 | 0.95 | -14.2 | 0.61 | - |

**Reading.** The position is highly constrained (position mean AlphaMissense 0.83-0.93 across the family) and bulky changes score strongly damaging (JAK2 V578F, JAK3 V553M), but **Val->Ile is mild everywhere** (AlphaMissense 0.20-0.36) and has **no measured effect in TYK2 (V639I -0.09 +- 0.27)**. Older tools (SIFT, PolyPhen-2, MetaRNN) call JAK2 V578I damaging mainly because of the conservation. A subtle effect on JH2 ATP binding cannot be excluded, but a strong effect is unlikely.

## JAK2 L805I

**Location.** Last helix at the C-terminal edge of JH2 (`RAIIRDLNSL`), just before the JH2-JH1 linker. Conserved Leu in JAK3 (L777) and TYK2 (L866); **JAK1 naturally has Ile (I845)**.

**Literature.** No publication on L805I or the equivalent residues.

### Alignment and variants reported at the equivalent positions

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

### Predictor scores - same substitution at each equivalent residue

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK2 | L805I | 0.15 (LB) | 0.44 | 25.6 | 0.317 | 0.773 | 0.72 | -7.7 | 0.36 | - |
| JAK3 | L777I | 0.11 (LB) | 0.57 | 24.4 | 0.286 | 0.767 | 0.47 | -9.7 | 0.28 | - |
| TYK2 | L866I | 0.11 (LB) | 0.34 | 23.3 | 0.416 | 0.296 | 0.45 | -7.6 | - | 0.57 +- 0.33 |

### Predictor scores - variants reported at these positions

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK1 | I845V | 0.22 (LB) | 0.16 | 25.3 | 0.004 | 0.502 | 0.42 | -4.6 | - | - |
| JAK3 | L777F | 0.49 (amb) | 0.79 | 27.8 | 0.013 | 0.993 | 0.74 | -11.3 | 0.65 | - |
| JAK3 | L777P | 0.99 (LP) | 0.96 | 28.5 | 0.000 | 0.997 | 0.99 | -14.6 | 0.79 | - |
| TYK2 | L866F | 0.16 (LB) | 0.54 | 24.9 | 0.019 | 0.350 | 0.76 | -7.3 | - | -0.29 +- 0.32 |

**Reading.** Ile is tolerated structurally (it is JAK1's wild-type residue) and predictors call L805I benign-to-uncertain, **but the TYK2 deep mutational scan gives the same change L866I +0.57 +- 0.33** - the highest of all 19 substitutions at that position and about the top 5% of the scan, i.e. *more* signalling. This is the only hint of gain of function among the four (weak, ~1.7 SE).

## JAK2 V1110E

**Location.** C-terminal end of the JH1 kinase domain (JH1 ends at 1124). The position is not conserved: Pro in JAK1 (P1136) and JAK3 (P1082), Ala in TYK2 (A1156).

**Literature.** No publication on V1110E or the equivalent residues.

### Alignment and variants reported at the equivalent positions

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

### Predictor scores - same substitution at each equivalent residue

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK2 | V1110E | 0.29 (LB) | 0.48 | 23.0 | 0.023 | 0.186 | 0.31 | -1.2 | 0.24 | - |
| JAK1 | P1136E | 0.69 (LP) | - | - | - | - | - | - | - | - |
| JAK3 | P1082E | 0.47 (amb) | - | - | - | - | - | - | - | - |
| TYK2 | A1156E | 0.46 (amb) | 0.50 | 28.7 | 0.022 | 0.978 | 0.37 | -6.9 | - | -0.08 +- 0.35 |

### Predictor scores - variants reported at these positions

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK2 | V1110I | 0.06 (LB) | 0.24 | 19.2 | 0.128 | 0.001 | 0.19 | -3.6 | 0.13 | - |
| JAK2 | V1110L | 0.11 (LB) | 0.25 | 17.8 | 0.105 | 0.001 | 0.19 | -3.0 | 0.14 | - |
| JAK1 | P1136S | 0.42 (amb) | 0.78 | 25.3 | 0.018 | 0.855 | 0.84 | -5.9 | - | - |
| JAK3 | P1082L | 0.17 (LB) | 0.57 | 24.0 | 0.083 | 0.817 | 0.97 | -9.6 | 0.38 | - |
| JAK3 | P1082T | 0.18 (LB) | 0.43 | 22.9 | 0.059 | 0.140 | 0.76 | -8.9 | 0.30 | - |
| TYK2 | A1156V | 0.24 (LB) | 0.41 | 25.5 | 0.586 | 0.931 | 0.17 | -6.0 | - | -0.19 +- 0.32 |

**Reading.** Variable position (position mean AlphaMissense 0.23 in JAK2); V1110E is benign-to-uncertain by most tools (AlphaMissense 0.29, PolyPhen-2 0.19, ESM1b -1.2), and the equivalent change in TYK2 (A1156E) has **no measured effect (-0.08 +- 0.35)**. Probably tolerated.

## Notes

- dbNSFP scores (REVEL, CADD, SIFT, PolyPhen-2, MetaRNN, ESM1b, EVE) exist only for substitutions reachable by one DNA change; "-" means not reachable or not scored. AlphaMissense covers all 19 substitutions. AlphaMissense classes: LP > 0.564, amb 0.34-0.564, LB < 0.34.
- "Position mean AlphaMissense" = average over all 19 substitutions at that residue (high = constrained). TYK2 DMS: MaveDB urn:mavedb:00001270-a-6, log2 fold change vs WT, negative = loss of signalling.
- Variant counts come from ClinVar, gnomAD v4 (AC = allele count) and cBioPortal; licensed tumour-database counts are not shown.

Sources: [Hammaren et al. 2015, ATP binding to the JAK2 pseudokinase domain (PNAS)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4403165); [Exon 13 G571S in MPN (Leukemia Research Reports 2016)](https://doaj.org/article/d6ee03ab66df44e5b4d23408576c5020); [Role of exon 13 G571S in MPN](https://agris.fao.org/search/en/records/65deba4e7c7033e84beb9c59); [Familial G571S not linked with ET](https://repository.ukim.mk/entities/publication/f8297d64-4f10-4f9b-a09b-a3a141b24616); [JAK2 G571S review (PMC5128013)](https://pmc.ncbi.nlm.nih.gov/articles/PMC5128013); [Structural effects of JAK2 exon 13-15 mutations (BMC Struct Biol 2009)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2749040/); [JAK2 domain table (PMC4943318)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4943318/table/T1); MaveDB TYK2 DMS; AlphaFold DB (AlphaMissense); dbNSFP via myvariant.info; ClinVar; gnomAD v4; cBioPortal; UniProt.
