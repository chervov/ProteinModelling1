# Top ten — deep conformational reports

Ten proteins selected from the 54 screened in [`../analysis1/`](../analysis1/), each carrying the full
Orianne-paper battery. Open [`index.html`](index.html), or any single report directly.

| Gene | UniProt | aa | Domains | Structures | Largest-moving pair | Spread Å | Muts | gnomAD depletion |
|---|---|---|---|---|---|---|---|---|
| **TYK2** | [P29597](https://www.uniprot.org/uniprotkb/P29597) | 1187 | 4 | 5 | FERM ↔ Protein kinase 2 | 54.5 | 6 | 1.3× |
| **JAK1** | [P23458](https://www.uniprot.org/uniprotkb/P23458) | 1154 | 4 | 5 | FERM ↔ Protein kinase 2 | 54.7 | 2 | 2.0× |
| **PTPN11** | [Q06124](https://www.uniprot.org/uniprotkb/Q06124) | 593 | 3 | 4 | SH2 1 ↔ Tyrosine-protein phosphatase | 16.2 | 6 | 1.6× |
| **SRC** | [P12931](https://www.uniprot.org/uniprotkb/P12931) | 536 | 3 | 6 | SH2 ↔ Protein kinase | 19.2 | 3 | 1.8× |
| **ABL1** | [P00519](https://www.uniprot.org/uniprotkb/P00519) | 1130 | 3 | 5 | SH2 ↔ Protein kinase | 21.5 | 6 | 2.2× |
| **BTK** | [Q06187](https://www.uniprot.org/uniprotkb/Q06187) | 659 | 4 | 9 | SH3 ↔ Protein kinase | 52.4 | 6 | 2.3× |
| **LRRK2** | [Q5S007](https://www.uniprot.org/uniprotkb/Q5S007) | 2527 | 3 | 5 | COR ↔ Protein kinase | 6.5 | 6 | 1.3× |
| **CFTR** | [P13569](https://www.uniprot.org/uniprotkb/P13569) | 1480 | 4 | 6 | ABC transporter 1 ↔ ABC transporter 2 | 20.0 | 7 | 1.0× |
| **ABCB1** | [P08183](https://www.uniprot.org/uniprotkb/P08183) | 1280 | 4 | 6 | ABC transporter 1 ↔ ABC transporter 2 | 34.2 | 5 | 1.3× |
| **DDX3X** | [O00571](https://www.uniprot.org/uniprotkb/O00571) | 662 | 2 | 3 | Helicase ATP-binding ↔ Helicase C-terminal | 19.0 | 4 | 3.7× |

## What each report contains

1. **Structures and 3D views** — every model drawn twice, coloured by domain and by pLDDT
   (AlphaFold), QMEANDisCo rescaled to the same range (SWISS-MODEL) or crystallographic
   B-factor (experimental). All coordinates renumbered into canonical UniProt positions by
   sequence alignment; the achieved identity is reported per model.
2. **Inter-domain geometry — all domain pairs, every structure.** Centroid distance and
   contact count for *every* ordered domain pair, so a pair that does not move is as visible
   as one that does, plus a per-pair movement summary across the structure set.
3. **PAE** — AlphaFold v6, block-averaged, with domain bars.
4. **Templates and homologs** — experimental structures of the protein itself, SWISS-MODEL
   models on homologous templates with identities, and the predicted models. The homolog
   templates are the only independent evidence that a pair can occupy more than one
   arrangement; a single predictor returns a single answer.
5. **Clustering and gnomAD enrichment** — unsupervised k=2 split of all possible missense
   variants on the predictor panel, with the observed-in-gnomAD rate per cluster.
6. **Literature mutations — full computation** — dual-state ΔΔG (closed and open) plus the
   fifteen-predictor panel, interface and pocket membership, burial, secondary structure.
7. **pLDDT at the mutated sites**, against the domain and chain medians.
8. **Proposed mechanism, mutation by mutation** — assembled from the computations, set beside
   what the literature says, with the disagreements stated.
9. **Literature review** — conformations, mutations, drugs and drug resistance, disease.
10. **Caveats.**

## Headline results

- The unsupervised damaging cluster is **depleted of gnomAD-observed variants in all ten**
  proteins, between 1.0× (CFTR) and 3.7× (DDX3X). The split uses no population data.
- The dual-state ΔΔG separates the mechanisms cleanly: **TYK2 V678F** destabilises the closed
  state by +15.50 REU while leaving the open state alone (−1.77), and **JAK1 V658F** does the
  same (+8.46 / −1.28) — both are the activating V617F-equivalent positions, and both come out
  as a loss of the compact state rather than a loss of folding. **PTPN11**'s GOF mutations sit
  at the N-SH2/PTP interface (4 of 6); **ABL1, BTK, SRC and LRRK2** resistance mutations sit in
  predicted drug pockets rather than at interfaces.
- Benign ABCB1 controls behave as controls (I261V +2.85/+3.42, N183S −1.16/−1.02).
- **LRRK2 is the weakest conformational case in the set**: its largest-moving pair spans only
  6.5 Å across five structures, against 52–55 Å for TYK2, JAK1 and BTK. It is included for its
  mutations and its drug programme, not as evidence of a two-state inter-domain switch, and its
  report should be read with that in mind.

## Caveats that travel with every number

1. **Some ΔΔG magnitudes are repulsion, not free energies.** The protocol repacks an 8 Å shell
   and applies **no global FastRelax** — that choice buys ~100k variants/hour instead of ~11
   minutes per structure. Any |ΔΔG| above 25 REU is flagged ⚠ and means "sterically impossible
   without backbone relaxation", not a measured energy. Affected: CFTR G85E (+1608),
   ABCB1 S893Y (+1530), PTPN11 A72V (+43).
2. **"Open" and "closed" here mean the inter-domain arrangement**, not the G-loop, not the
   DFG-in/out flip, not the phosphatase WPD loop. The LRRK2 G2019S call destabilises the
   *inter-domain* closed state, while the literature describes it stabilising the *intra-domain*
   closed kinase conformation — a different sense of the same word. See
   [`../../open_close/open_close_inf.md`](../../open_close/open_close_inf.md).
3. **The predictor panel is blind to gain of function.** Every member scores loss of function or
   loss of stability, so activating variants are systematically called benign, and are.
4. **dbNSFP indexes only single-nucleotide substitutions** (~69% of amino-acid changes), so some
   literature mutations — TYK2 V678F among them — have no clustering row although they are fully
   computed everywhere else.
5. ESM-1v and ThermoMPNN come from the Liao & Lehner proteome release, which covers 46 of the 54
   screened proteins; PTPN11 and LRRK2 are not in it, and take AlphaMissense from dbNSFP instead.

## Closest human sequence homologs

`phmmer` (HMMER 3.4) of each canonical sequence against all **20,431 reviewed human SwissProt**
entries, E ≤ 1e-3, the protein itself excluded. Produced by [`scripts/homol.py`](scripts/homol.py);
full tables in [`data/homologs.json`](data/homologs.json).

**How to read the numbers.** **Bit score** is the alignment score on a log₂ scale and is independent
of database size — it is the column to rank by. Above ~50 means real homology, above ~200 unambiguous
homology, above ~1000 at near-full coverage a close paralogue. **E-value** is how many hits this good
would be expected by chance among these 20,431 sequences; `0.0` means below floating-point resolution,
not zero evidence, and the value is not comparable across searches of differently sized databases.
**% identity** is counted over aligned columns only and **% similarity** adds conservative substitutions;
below roughly 25–30% identity — the *twilight zone* — identity alone no longer separates homology from
chance, which is precisely where bit score and E-value still do. **% query covered** is aligned columns
over the full query length: a high bit score at low coverage means **one shared domain matched, not the
whole protein**, so a kinase domain may be borrowed from such a hit but an inter-domain arrangement may not.

### TYK2 (P29597, 1187 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `JAK1` | [P23458](https://www.uniprot.org/uniprotkb/P23458) | **1095.7** | 0.0 | 47.5 | 68.3 | 1121 | 94.4 | Tyrosine-protein kinase JAK1 |
| 2 | `JAK2` | [O60674](https://www.uniprot.org/uniprotkb/O60674) | **799.8** | 4.4e-240 | 41.8 | 62.9 | 1036 | 87.3 | Tyrosine-protein kinase JAK2 |
| 3 | `JAK3` | [P52333](https://www.uniprot.org/uniprotkb/P52333) | **745.3** | 1.3e-223 | 42.5 | 61.8 | 1047 | 88.2 | Tyrosine-protein kinase JAK3 |
| 4 | `ACK1` | [Q07912](https://www.uniprot.org/uniprotkb/Q07912) | **165.8** | 1.2e-48 | 39.4 | 60.9 | 274 | 23.1 | Activated CDC42 kinase 1 |
| 5 | `ERBB4` | [Q15303](https://www.uniprot.org/uniprotkb/Q15303) | **157.6** | 3.3e-46 | 36.0 | 55.1 | 303 | 25.5 | Receptor tyrosine-protein kinase erbB- |
| 6 | `FAK2` | [Q14289](https://www.uniprot.org/uniprotkb/Q14289) | **154.3** | 3.3e-45 | 36.9 | 57.3 | 274 | 23.1 | Protein-tyrosine kinase 2-beta |
| 7 | `LYN` | [P07948](https://www.uniprot.org/uniprotkb/P07948) | **151.9** | 1.8e-44 | 34.9 | 57.2 | 292 | 24.6 | Tyrosine-protein kinase Lyn |
| 8 | `FAK1` | [Q05397](https://www.uniprot.org/uniprotkb/Q05397) | **151.2** | 3.0e-44 | 36.1 | 56.5 | 285 | 24.0 | Focal adhesion kinase 1 |
| 9 | `NTRK2` | [Q16620](https://www.uniprot.org/uniprotkb/Q16620) | **150.3** | 5.3e-44 | 38.9 | 59.6 | 275 | 23.2 | BDNF/NT-3 growth factors receptor |
| 10 | `KSYK` | [P43405](https://www.uniprot.org/uniprotkb/P43405) | **150.2** | 5.9e-44 | 36.8 | 56.4 | 266 | 22.4 | Tyrosine-protein kinase SYK |

### JAK1 (P23458, 1154 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `TYK2` | [P29597](https://www.uniprot.org/uniprotkb/P29597) | **1087.9** | 0.0 | 48.7 | 68.7 | 1097 | 95.1 | Non-receptor tyrosine-protein kinase T |
| 2 | `JAK2` | [O60674](https://www.uniprot.org/uniprotkb/O60674) | **966.0** | 2.5e-290 | 45.5 | 66.0 | 1103 | 95.6 | Tyrosine-protein kinase JAK2 |
| 3 | `JAK3` | [P52333](https://www.uniprot.org/uniprotkb/P52333) | **808.2** | 1.1e-242 | 43.1 | 63.4 | 1008 | 87.3 | Tyrosine-protein kinase JAK3 |
| 4 | `FRK` | [P42685](https://www.uniprot.org/uniprotkb/P42685) | **173.3** | 5.6e-51 | 38.1 | 61.2 | 281 | 24.4 | Tyrosine-protein kinase FRK |
| 5 | `ERBB4` | [Q15303](https://www.uniprot.org/uniprotkb/Q15303) | **163.4** | 5.6e-48 | 36.9 | 56.3 | 279 | 24.2 | Receptor tyrosine-protein kinase erbB- |
| 6 | `ACK1` | [Q07912](https://www.uniprot.org/uniprotkb/Q07912) | **160.4** | 4.4e-47 | 37.0 | 59.3 | 273 | 23.7 | Activated CDC42 kinase 1 |
| 7 | `ZAP70` | [P43403](https://www.uniprot.org/uniprotkb/P43403) | **155.2** | 1.6e-45 | 37.1 | 55.6 | 275 | 23.8 | Tyrosine-protein kinase ZAP-70 |
| 8 | `KSYK` | [P43405](https://www.uniprot.org/uniprotkb/P43405) | **153.7** | 4.8e-45 | 36.5 | 56.9 | 274 | 23.7 | Tyrosine-protein kinase SYK |
| 9 | `FGFR4` | [P22455](https://www.uniprot.org/uniprotkb/P22455) | **152.5** | 1.1e-44 | 37.1 | 59.5 | 321 | 27.8 | Fibroblast growth factor receptor 4 OS |
| 10 | `HCK` | [P08631](https://www.uniprot.org/uniprotkb/P08631) | **151.6** | 2.1e-44 | 33.8 | 57.5 | 287 | 24.9 | Tyrosine-protein kinase HCK |

### PTPN11 (Q06124, 593 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `PTN6` | [P29350](https://www.uniprot.org/uniprotkb/P29350) | **723.0** | 2.9e-217 | 58.3 | 76.4 | 547 | 92.2 | Tyrosine-protein phosphatase non-recep |
| 2 | `PTPRA` | [P18433](https://www.uniprot.org/uniprotkb/P18433) | **384.4** | 1.0e-114 | 38.9 | 60.8 | 579 | 97.6 | Receptor-type tyrosine-protein phospha |
| 3 | `PTPRD` | [P23468](https://www.uniprot.org/uniprotkb/P23468) | **370.2** | 2.0e-110 | 39.1 | 60.7 | 575 | 97.0 | Receptor-type tyrosine-protein phospha |
| 4 | `PTPRS` | [Q13332](https://www.uniprot.org/uniprotkb/Q13332) | **369.2** | 3.8e-110 | 41.0 | 61.7 | 525 | 88.5 | Receptor-type tyrosine-protein phospha |
| 5 | `PTPRF` | [P10586](https://www.uniprot.org/uniprotkb/P10586) | **361.0** | 1.2e-107 | 40.0 | 61.9 | 525 | 88.5 | Receptor-type tyrosine-protein phospha |
| 6 | `PTPRE` | [P23469](https://www.uniprot.org/uniprotkb/P23469) | **355.4** | 6.1e-106 | 38.2 | 59.0 | 586 | 98.8 | Receptor-type tyrosine-protein phospha |
| 7 | `PTPRT` | [O14522](https://www.uniprot.org/uniprotkb/O14522) | **292.4** | 7.1e-87 | 35.7 | 56.8 | 577 | 97.3 | Receptor-type tyrosine-protein phospha |
| 8 | `PTPRK` | [Q15262](https://www.uniprot.org/uniprotkb/Q15262) | **291.9** | 9.9e-87 | 37.0 | 57.9 | 541 | 91.2 | Receptor-type tyrosine-protein phospha |
| 9 | `PTPRM` | [P28827](https://www.uniprot.org/uniprotkb/P28827) | **279.1** | 7.9e-83 | 35.6 | 54.9 | 579 | 97.6 | Receptor-type tyrosine-protein phospha |
| 10 | `PTPRC` | [P08575](https://www.uniprot.org/uniprotkb/P08575) | **262.7** | 7.2e-78 | 33.4 | 58.5 | 545 | 91.9 | Receptor-type tyrosine-protein phospha |

### SRC (P12931, 536 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `YES` | [P07947](https://www.uniprot.org/uniprotkb/P07947) | **925.0** | 1.1e-278 | 78.0 | 88.0 | 510 | 95.1 | Tyrosine-protein kinase Yes |
| 2 | `FYN` | [P06241](https://www.uniprot.org/uniprotkb/P06241) | **836.6** | 7.2e-252 | 76.1 | 87.4 | 476 | 88.8 | Tyrosine-protein kinase Fyn |
| 3 | `FGR` | [P09769](https://www.uniprot.org/uniprotkb/P09769) | **798.9** | 2.0e-240 | 68.3 | 81.0 | 517 | 96.5 | Tyrosine-protein kinase Fgr |
| 4 | `HCK` | [P08631](https://www.uniprot.org/uniprotkb/P08631) | **653.1** | 2.9e-196 | 62.6 | 81.2 | 446 | 83.2 | Tyrosine-protein kinase HCK |
| 5 | `LCK` | [P06239](https://www.uniprot.org/uniprotkb/P06239) | **629.3** | 4.7e-189 | 59.9 | 78.4 | 454 | 84.7 | Tyrosine-protein kinase Lck |
| 6 | `LYN` | [P07948](https://www.uniprot.org/uniprotkb/P07948) | **622.2** | 6.8e-187 | 60.1 | 79.1 | 444 | 82.8 | Tyrosine-protein kinase Lyn |
| 7 | `BLK` | [P51451](https://www.uniprot.org/uniprotkb/P51451) | **614.5** | 1.5e-184 | 62.8 | 77.7 | 443 | 82.6 | Tyrosine-protein kinase Blk |
| 8 | `FRK` | [P42685](https://www.uniprot.org/uniprotkb/P42685) | **506.2** | 9.6e-152 | 53.8 | 74.2 | 446 | 83.2 | Tyrosine-protein kinase FRK |
| 9 | `PTK6` | [Q13882](https://www.uniprot.org/uniprotkb/Q13882) | **404.0** | 8.8e-121 | 46.7 | 65.6 | 439 | 81.9 | Protein-tyrosine kinase 6 |
| 10 | `ABL1` | [P00519](https://www.uniprot.org/uniprotkb/P00519) | **389.9** | 1.6e-116 | 44.3 | 66.9 | 447 | 83.4 | Tyrosine-protein kinase ABL1 |

### ABL1 (P00519, 1130 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `ABL2` | [P42684](https://www.uniprot.org/uniprotkb/P42684) | **1155.2** | 0.0 | 56.5 | 70.1 | 1105 | 97.8 | Tyrosine-protein kinase ABL2 |
| 2 | `FRK` | [P42685](https://www.uniprot.org/uniprotkb/P42685) | **402.7** | 3.8e-120 | 44.2 | 67.0 | 448 | 39.6 | Tyrosine-protein kinase FRK |
| 3 | `YES` | [P07947](https://www.uniprot.org/uniprotkb/P07947) | **396.0** | 4.0e-118 | 46.2 | 68.0 | 435 | 38.5 | Tyrosine-protein kinase Yes |
| 4 | `FYN` | [P06241](https://www.uniprot.org/uniprotkb/P06241) | **394.2** | 1.4e-117 | 45.3 | 67.8 | 435 | 38.5 | Tyrosine-protein kinase Fyn |
| 5 | `FGR` | [P09769](https://www.uniprot.org/uniprotkb/P09769) | **392.5** | 4.5e-117 | 45.0 | 66.7 | 444 | 39.3 | Tyrosine-protein kinase Fgr |
| 6 | `SRC` | [P12931](https://www.uniprot.org/uniprotkb/P12931) | **388.8** | 5.8e-116 | 44.9 | 67.3 | 443 | 39.2 | Proto-oncogene tyrosine-protein kinase |
| 7 | `LCK` | [P06239](https://www.uniprot.org/uniprotkb/P06239) | **383.3** | 2.6e-114 | 45.1 | 67.7 | 437 | 38.7 | Tyrosine-protein kinase Lck |
| 8 | `HCK` | [P08631](https://www.uniprot.org/uniprotkb/P08631) | **380.9** | 1.4e-113 | 44.7 | 67.4 | 436 | 38.6 | Tyrosine-protein kinase HCK |
| 9 | `LYN` | [P07948](https://www.uniprot.org/uniprotkb/P07948) | **367.0** | 2.2e-109 | 43.0 | 66.6 | 437 | 38.7 | Tyrosine-protein kinase Lyn |
| 10 | `BLK` | [P51451](https://www.uniprot.org/uniprotkb/P51451) | **359.6** | 3.7e-107 | 43.3 | 64.5 | 439 | 38.8 | Tyrosine-protein kinase Blk |

### BTK (Q06187, 659 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `TEC` | [P42680](https://www.uniprot.org/uniprotkb/P42680) | **772.8** | 2.6e-232 | 54.1 | 73.3 | 652 | 98.9 | Tyrosine-protein kinase Tec |
| 2 | `ITK` | [Q08881](https://www.uniprot.org/uniprotkb/Q08881) | **694.1** | 1.7e-208 | 50.3 | 69.9 | 652 | 98.9 | Tyrosine-protein kinase ITK/TSK |
| 3 | `BMX` | [P51813](https://www.uniprot.org/uniprotkb/P51813) | **689.0** | 5.9e-207 | 53.8 | 75.4 | 602 | 91.4 | Cytoplasmic tyrosine-protein kinase BM |
| 4 | `TXK` | [P42681](https://www.uniprot.org/uniprotkb/P42681) | **628.7** | 1.1e-188 | 56.0 | 77.0 | 466 | 70.7 | Tyrosine-protein kinase TXK |
| 5 | `ABL1` | [P00519](https://www.uniprot.org/uniprotkb/P00519) | **359.6** | 2.9e-107 | 42.0 | 63.8 | 436 | 66.2 | Tyrosine-protein kinase ABL1 |
| 6 | `ABL2` | [P42684](https://www.uniprot.org/uniprotkb/P42684) | **349.5** | 3.5e-104 | 41.7 | 62.3 | 432 | 65.6 | Tyrosine-protein kinase ABL2 |
| 7 | `LCK` | [P06239](https://www.uniprot.org/uniprotkb/P06239) | **349.1** | 4.3e-104 | 39.0 | 63.7 | 446 | 67.7 | Tyrosine-protein kinase Lck |
| 8 | `HCK` | [P08631](https://www.uniprot.org/uniprotkb/P08631) | **345.0** | 7.9e-103 | 40.1 | 63.1 | 439 | 66.6 | Tyrosine-protein kinase HCK |
| 9 | `LYN` | [P07948](https://www.uniprot.org/uniprotkb/P07948) | **342.7** | 3.8e-102 | 40.0 | 64.1 | 437 | 66.3 | Tyrosine-protein kinase Lyn |
| 10 | `BLK` | [P51451](https://www.uniprot.org/uniprotkb/P51451) | **341.8** | 7.0e-102 | 37.4 | 60.9 | 473 | 71.8 | Tyrosine-protein kinase Blk |

### LRRK2 (Q5S007, 2527 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `LRRK1` | [Q38SD2](https://www.uniprot.org/uniprotkb/Q38SD2) | **376.6** | 2.1e-112 | 29.5 | 55.6 | 1350 | 53.4 | Leucine-rich repeat serine/threonine-p |
| 2 | `SHOC2` | [Q9UQ13](https://www.uniprot.org/uniprotkb/Q9UQ13) | **97.2** | 3.7e-28 | 30.5 | 56.6 | 433 | 17.1 | Leucine-rich repeat protein SHOC-2 |
| 3 | `MFHA1` | [Q9Y4C4](https://www.uniprot.org/uniprotkb/Q9Y4C4) | **91.9** | 1.5e-26 | 29.7 | 54.3 | 488 | 19.3 | Malignant fibrous histiocytoma-amplifi |
| 4 | `M3K9` | [P80192](https://www.uniprot.org/uniprotkb/P80192) | **90.7** | 3.5e-26 | 34.0 | 59.9 | 262 | 10.4 | Mitogen-activated protein kinase kinas |
| 5 | `M3K7` | [O43318](https://www.uniprot.org/uniprotkb/O43318) | **88.9** | 1.2e-25 | 29.5 | 58.6 | 268 | 10.6 | Mitogen-activated protein kinase kinas |
| 6 | `MATK` | [P42679](https://www.uniprot.org/uniprotkb/P42679) | **87.0** | 4.4e-25 | 30.5 | 58.4 | 243 | 9.6 | Megakaryocyte-associated tyrosine-prot |
| 7 | `ERBIN` | [Q96RT1](https://www.uniprot.org/uniprotkb/Q96RT1) | **86.9** | 4.7e-25 | 27.5 | 54.2 | 530 | 21.0 | Erbin |
| 8 | `KS6A2` | [Q15349](https://www.uniprot.org/uniprotkb/Q15349) | **86.7** | 5.5e-25 | 31.7 | 57.4 | 378 | 15.0 | Ribosomal protein S6 kinase alpha-2 OS |
| 9 | `KS6A1` | [Q15418](https://www.uniprot.org/uniprotkb/Q15418) | **86.6** | 5.8e-25 | 31.9 | 56.7 | 386 | 15.3 | Ribosomal protein S6 kinase alpha-1 OS |
| 10 | `M3K10` | [Q02779](https://www.uniprot.org/uniprotkb/Q02779) | **86.6** | 6.0e-25 | 33.9 | 57.6 | 283 | 11.2 | Mitogen-activated protein kinase kinas |

### CFTR (P13569, 1480 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `MRP4` | [O15439](https://www.uniprot.org/uniprotkb/O15439) | **818.8** | 8.9e-246 | 36.4 | 63.7 | 1203 | 81.3 | ATP-binding cassette sub-family C memb |
| 2 | `MRP9` | [Q96J65](https://www.uniprot.org/uniprotkb/Q96J65) | **533.3** | 1.3e-159 | 28.3 | 56.6 | 1226 | 82.8 | ATP-binding cassette sub-family C memb |
| 3 | `MRP5` | [O15440](https://www.uniprot.org/uniprotkb/O15440) | **526.3** | 1.7e-157 | 29.1 | 59.0 | 1208 | 81.6 | ATP-binding cassette sub-family C memb |
| 4 | `MRP8` | [Q96J66](https://www.uniprot.org/uniprotkb/Q96J66) | **514.8** | 4.8e-154 | 29.5 | 56.4 | 1254 | 84.7 | ATP-binding cassette sub-family C memb |
| 5 | `MRP1` | [P33527](https://www.uniprot.org/uniprotkb/P33527) | **510.5** | 9.9e-153 | 29.8 | 57.3 | 1123 | 75.9 | ATP-binding cassette sub-family C memb |
| 6 | `MRP3` | [O15438](https://www.uniprot.org/uniprotkb/O15438) | **505.8** | 2.5e-151 | 29.7 | 59.4 | 1096 | 74.1 | ATP-binding cassette sub-family C memb |
| 7 | `MRP2` | [Q92887](https://www.uniprot.org/uniprotkb/Q92887) | **479.7** | 2.0e-143 | 30.5 | 58.7 | 1085 | 73.3 | ATP-binding cassette sub-family C memb |
| 8 | `ABCC9` | [O60706](https://www.uniprot.org/uniprotkb/O60706) | **453.5** | 1.5e-135 | 29.3 | 57.2 | 1265 | 85.5 | ATP-binding cassette sub-family C memb |
| 9 | `MRP7` | [Q5T3U5](https://www.uniprot.org/uniprotkb/Q5T3U5) | **447.0** | 1.4e-133 | 28.9 | 56.6 | 1087 | 73.4 | ATP-binding cassette sub-family C memb |
| 10 | `ABCC8` | [Q09428](https://www.uniprot.org/uniprotkb/Q09428) | **443.5** | 1.6e-132 | 29.9 | 57.7 | 1163 | 78.6 | ATP-binding cassette sub-family C memb |

### ABCB1 (P08183, 1280 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `MDR3` | [P21439](https://www.uniprot.org/uniprotkb/P21439) | **2141.9** | 0.0 | 76.6 | 89.5 | 1278 | 99.8 | Phosphatidylcholine translocator ABCB4 |
| 2 | `ABCB5` | [Q2M3G0](https://www.uniprot.org/uniprotkb/Q2M3G0) | **1559.8** | 0.0 | 55.4 | 79.5 | 1262 | 98.6 | ATP-binding cassette sub-family B memb |
| 3 | `ABCBB` | [O95342](https://www.uniprot.org/uniprotkb/O95342) | **1428.4** | 0.0 | 52.5 | 75.8 | 1269 | 99.1 | Bile salt export pump |
| 4 | `ABCBA` | [Q9NRK6](https://www.uniprot.org/uniprotkb/Q9NRK6) | **360.5** | 1.9e-107 | 38.2 | 62.6 | 524 | 40.9 | ATP-binding cassette sub-family B memb |
| 5 | `MITOS` | [Q9NUT2](https://www.uniprot.org/uniprotkb/Q9NUT2) | **341.9** | 8.0e-102 | 36.8 | 61.0 | 579 | 45.2 | Mitochondrial potassium channel ATP-bi |
| 6 | `ABCB9` | [Q9NP78](https://www.uniprot.org/uniprotkb/Q9NP78) | **327.5** | 1.8e-97 | 38.6 | 64.9 | 502 | 39.2 | ABC-type oligopeptide transporter ABCB |
| 7 | `TAP1` | [Q03518](https://www.uniprot.org/uniprotkb/Q03518) | **270.6** | 2.7e-80 | 34.4 | 60.3 | 517 | 40.4 | Antigen peptide transporter 1 |
| 8 | `MRP4` | [O15439](https://www.uniprot.org/uniprotkb/O15439) | **267.3** | 2.5e-79 | 25.5 | 50.1 | 1364 | 106.6 | ATP-binding cassette sub-family C memb |
| 9 | `TAP2` | [Q03519](https://www.uniprot.org/uniprotkb/Q03519) | **249.3** | 7.4e-74 | 35.0 | 61.7 | 491 | 38.4 | Antigen peptide transporter 2 |
| 10 | `ABCB6` | [Q9NP58](https://www.uniprot.org/uniprotkb/Q9NP58) | **238.2** | 1.6e-70 | 37.2 | 60.7 | 425 | 33.2 | ATP-binding cassette sub-family B memb |

### DDX3X (O00571, 662 aa)

| # | Entry | UniProt | Bit score | E-value | % id | % sim | Aligned cols | % query cov | Protein |
|---|---|---|---|---|---|---|---|---|---|
| 1 | `DDX3Y` | [O15523](https://www.uniprot.org/uniprotkb/O15523) | **1395.9** | 0.0 | 91.8 | 96.4 | 662 | 100.0 | ATP-dependent RNA helicase DDX3Y |
| 2 | `DDX4` | [Q9NQI0](https://www.uniprot.org/uniprotkb/Q9NQI0) | **485.6** | 2.8e-145 | 49.1 | 68.4 | 532 | 80.4 | Probable ATP-dependent RNA helicase DD |
| 3 | `DDX17` | [Q92841](https://www.uniprot.org/uniprotkb/Q92841) | **339.9** | 3.5e-101 | 42.6 | 63.5 | 474 | 71.6 | Probable ATP-dependent RNA helicase DD |
| 4 | `DDX5` | [P17844](https://www.uniprot.org/uniprotkb/P17844) | **339.1** | 5.9e-101 | 40.2 | 60.8 | 502 | 75.8 | Probable ATP-dependent RNA helicase DD |
| 5 | `DDX41` | [Q9UJV9](https://www.uniprot.org/uniprotkb/Q9UJV9) | **299.8** | 4.6e-89 | 39.0 | 61.9 | 431 | 65.1 | Probable ATP-dependent RNA helicase DD |
| 6 | `DDX46` | [Q7L014](https://www.uniprot.org/uniprotkb/Q7L014) | **297.6** | 2.2e-88 | 39.4 | 61.9 | 436 | 65.9 | Probable ATP-dependent RNA helicase DD |
| 7 | `DDX43` | [Q9NXZ2](https://www.uniprot.org/uniprotkb/Q9NXZ2) | **282.3** | 9.2e-84 | 39.8 | 62.2 | 394 | 59.5 | Probable ATP-dependent RNA helicase DD |
| 8 | `DDX23` | [Q9BUQ8](https://www.uniprot.org/uniprotkb/Q9BUQ8) | **275.3** | 1.2e-81 | 40.8 | 60.4 | 419 | 63.3 | Probable ATP-dependent RNA helicase DD |
| 9 | `DDX42` | [Q86XP3](https://www.uniprot.org/uniprotkb/Q86XP3) | **273.5** | 4.3e-81 | 35.5 | 58.3 | 521 | 78.7 | ATP-dependent RNA helicase DDX42 |
| 10 | `DDX53` | [Q86TM3](https://www.uniprot.org/uniprotkb/Q86TM3) | **253.1** | 6.5e-75 | 36.0 | 60.7 | 397 | 60.0 | Probable ATP-dependent RNA helicase DD |

### What the homolog tables say about this set

- **Four proteins have a near-twin**: ABCB1/MDR3 (76.6% id over 99.8% of the query), DDX3X/DDX3Y
  (91.8% over 100% — the Y-chromosome paralogue), SRC/YES (78.0% over 95.1%), TYK2/JAK1 (47.5%
  over 94.4%). For these, a homolog structure is a genuine substitute across the whole
  architecture, which is why the SWISS-MODEL template lineages in section 4 of each report span
  several domains.
- **ABL1 and BTK do not.** Their best non-family hits are SRC-family kinases at 39–66% query
  coverage: that is the kinase domain alone, with the SH3/SH2 module unmatched. A template taken
  from there carries no information about the inter-domain arrangement.
- **LRRK2 is the outlier.** Its only substantial homolog is LRRK1 at 29.5% identity over 53% of the
  query — twilight-zone identity, rescued only by a bit score of 376.6. Everything below it in the
  table is a single shared domain (a kinase domain, or leucine-rich repeats from SHOC2 and ERBIN).
  This is consistent with LRRK2 being the weakest conformational case in the set.
- **CFTR's homologs are all ABCC transporters** at 28–36% identity but 73–86% query coverage, so the
  whole ABC architecture is shared while the sequence is far diverged — the case where the bit score
  carries the signal that identity has lost.
- **PTPN11's closest relative, PTPN6/SHP1 at 58.3%**, is the protein with the same N-SH2-occludes-PTP
  autoinhibition, so its structures and its mutation literature transfer directly.
## Papers establishing the open/closed states, per protein

The benchmark for this project is the JAK set — four papers that between them report the inter-domain
arrangement experimentally and model the transition:

- **Shan / D. E. Shaw Research, JAK2 JH2-JH1** — Shan Y, Gnanasambandan K, Ungureanu D, Kim ET, Hammarén H, Yamashita K, Silvennoinen O, Shaw DE, Hubbard SR. *Molecular basis for pseudokinase-dependent autoinhibition of JAK2 tyrosine kinase.* **Nat Struct Mol Biol** 2014;21:579-84. doi:10.1038/nsmb.2849 · PMID 24918548
  <br>MD-derived model of the pseudokinase-kinase autoinhibitory interface; nearly all activating disease mutations map to it.
- **Ayaz / D. E. Shaw Research, FULL-LENGTH JAK2** — Ayaz P, Hammarén HM, Raivola J, Sharon D, Hubbard SR, Silvennoinen O, Shan Y, Shaw DE. *Structural models of full-length JAK2 kinase.* **bioRxiv**, posted 7 August 2019. doi:10.1101/727727 — **preprint, no peer-reviewed version noted**
  <br>Structural models of full-length JAK2 in active AND inactive forms from long-timescale MD - the four-domain arrangement, i.e. exactly our open/closed sense.
- **Lupardus, experimental TYK2** — Lupardus PJ, Ultsch M, Wallweber H, Bir Kohli P, Johnson AR, Eigenbrot C. *Structure of the pseudokinase-kinase domains from protein kinase TYK2 reveals a mechanism for Janus kinase (JAK) autoinhibition.* **Proc Natl Acad Sci U S A** 2014;111:8025-30. doi:10.1073/pnas.1401180111 · PMID 24843152
  <br>The 2.8 A JH2-JH1 crystal: the only experimental closed inter-domain state in the family.
- **Glassman, experimental full-length JAK** — Glassman CR, Tsutsumi N, Saxton RA, Lupardus PJ, Jude KM, Garcia KC. *Structure of a Janus kinase cytokine receptor complex reveals the basis for dimeric activation.* **Science** 2022;376:163-169. doi:10.1126/science.abn8933 · PMID 35271300
  <br>Cryo-EM of a JAK-cytokine-receptor complex: autoinhibited module and activated dimer.

Note that **Shan 2014 and Ayaz 2019 are two different D. E. Shaw Research papers**: the first models only
the JH2–JH1 pair, the second the complete FERM–SH2–JH2–JH1 arrangement in active *and* inactive forms,
which is the one that matches the inter-domain sense used throughout this project.

Below, five equivalents for each of the ten, graded by how directly they answer the question.
**Tier A** = reports or models two or more distinct inter-domain arrangements of that protein;
**Tier B** = one arrangement experimentally, or the transition approached indirectly.
Full records in [`data/conf_papers.json`](data/conf_papers.json).

### TYK2 (P29597)

1. **[A]** Lupardus PJ et al., *Proc Natl Acad Sci U S A* 2014;111:8025-30. [Structure of the pseudokinase-kinase domains from protein kinase TYK2 reveals a mechanism for Janus kinase (JAK) autoinhibition.](https://doi.org/10.1073/pnas.1401180111) · PMID 24843152
   <br>The 2.8 A crystal of the TYK2 JH2-JH1 module: the only experimental CLOSED inter-domain state anywhere in the JAK family. Our 4OLI.
2. **[B]** Wallweber HJ et al., *Nat Struct Mol Biol* 2014;21:443-8. [Structural basis of recognition of interferon-α receptor by tyrosine kinase 2.](https://doi.org/10.1038/nsmb.2807) · PMID 24704786
   <br>TYK2 FERM-SH2 bound to the IFNAR1 box1/box2 region - the other half of the architecture, fixing where the N-terminal module sits.
3. **[A]** Glassman CR et al., *Science* 2022;376:163-169. [Structure of a Janus kinase cytokine receptor complex reveals the basis for dimeric activation.](https://doi.org/10.1126/science.abn8933) · PMID 35271300
   <br>Full-length JAK on a receptor dimer by cryo-EM: the autoinhibited JH2-JH1 module docked against FERM-SH2, and the activated dimer. The architecture TYK2 is read onto.
4. **[B]** Wang J et al., *J Invest Dermatol* 2025;145:3158-3173. [A Triple-Action Inhibitory Mechanism of Allosteric TYK2-Specific Inhibitors.](https://doi.org/10.1016/j.jid.2025.04.025) · PMID 40378946
   <br>Allosteric TYK2-specific inhibitors acting by a triple mechanism; the drug works by holding the JH2-JH1 arrangement, so it is a conformational readout.
5. **[B]** Locke GA et al., *Methods Enzymol* 2022;667:685-727. [Identification and characterization of TYK2 pseudokinase domain stabilizers that allosterically inhibit TYK2 signaling.](https://doi.org/10.1016/bs.mie.2022.03.051) · PMID 35525559
   <br>Pseudokinase-domain STABILISERS that allosterically inhibit TYK2 - small molecules selected for locking the closed state.

### JAK1 (P23458)

1. **[A]** Glassman CR et al., *Science* 2022;376:163-169. [Structure of a Janus kinase cytokine receptor complex reveals the basis for dimeric activation.](https://doi.org/10.1126/science.abn8933) · PMID 35271300
   <br>Full-length JAK1 cryo-EM: the compact autoinhibited arrangement and the activated receptor-dimer arrangement side by side.
2. **[A]** Caveney NA et al., *Cell Rep* 2023;42:112201. [Structural basis of Janus kinase trans-activation.](https://doi.org/10.1016/j.celrep.2023.112201) · PMID 36867534
   <br>Structural basis of JAK trans-activation - the dimeric, activated JH1-JH1 arrangement that the closed state must give way to.
3. **[A]** Sun S et al., *Brief Bioinform* 2024;25:. [A novel approach to study multi-domain motions in JAK1's activation mechanism based on energy landscape.](https://doi.org/10.1093/bib/bbae079) · PMID 38446738
   <br>Multi-domain motions in JAK1 activation studied on an energy landscape: explicitly the open-vs-closed inter-domain question, computationally.
4. **[B]** Peng X et al., *Life (Basel)* 2025;15:. [Molecular Dynamics Simulation Analysis of JAK1 Initial Activation: Phosphorylation-Induced Conformational Dynamics and Domain Interactions.](https://doi.org/10.3390/life15081316) · PMID 40868963
   <br>MD of JAK1 initial activation: phosphorylation-induced conformational dynamics and inter-domain interactions.
5. **[B]** McNally R et al., *PLoS One* 2016;11:e0156218. [Crystal Structure of the FERM-SH2 Module of Human Jak2.](https://doi.org/10.1371/journal.pone.0156218) · PMID 27227461
   <br>Crystal structure of the JAK2 FERM-SH2 module - the evidence that FERM and SH2 move as one rigid block, which is why only FERM-vs-kinase moves.

### PTPN11 (Q06124)

1. **[A]** Hof P et al., *Cell* 1998;92:441-50. [Crystal structure of the tyrosine phosphatase SHP-2.](https://pubmed.ncbi.nlm.nih.gov/9491886/) · PMID 9491886
   <br>The founding autoinhibited crystal: N-SH2 inserted into the PTP catalytic cleft. The CLOSED state of this protein.
2. **[A]** Chen YN et al., *Nature* 2016;535:148-52. [Allosteric inhibition of SHP2 phosphatase inhibits cancers driven by receptor tyrosine kinases.](https://pubmed.ncbi.nlm.nih.gov/27362227/) · PMID 27362227
   <br>SHP099 binds a tunnel formed only where N-SH2, C-SH2 and PTP meet - an allosteric site that exists in the closed state and not the open one.
3. **[A]** Pádua RAP et al., *Nat Commun* 2018;9:4507. [Mechanism of activating mutations and allosteric drug inhibition of the phosphatase SHP2.](https://doi.org/10.1038/s41467-018-06814-w) · PMID 30375376
   <br>Mechanism of activating mutations AND allosteric drug inhibition: the open and closed states and the mutations that shift between them.
4. **[A]** LaRochelle JR et al., *Nat Commun* 2018;9:4508. [Structural reorganization of SHP2 by oncogenic mutations and implications for oncoprotein resistance to allosteric inhibition.](https://doi.org/10.1038/s41467-018-06823-9) · PMID 30375388
   <br>Structural reorganization by oncogenic mutations, and why an open-shifted oncoprotein resists an inhibitor that needs the closed state.
5. **[A]** Anselmi M et al., *Commun Biol* 2023;6:1289. [Atomistic ensemble of active SHP2 phosphatase.](https://doi.org/10.1038/s42003-023-05682-5) · PMID 38129686
   <br>An atomistic ensemble of the ACTIVE (open) phosphatase - the open state characterised in its own right rather than inferred.

### SRC (P12931)

1. **[B]** Xu W et al., *Nature* 1997;385:595-602. [Three-dimensional structure of the tyrosine kinase c-Src.](https://pubmed.ncbi.nlm.nih.gov/9024657/) · PMID 9024657
   <br>The first three-dimensional structure of c-Src: the assembled, autoinhibited SH3-SH2-kinase arrangement.
2. **[A]** Xu W et al., *Mol Cell* 1999;3:629-38. [Crystal structures of c-Src reveal features of its autoinhibitory mechanism.](https://pubmed.ncbi.nlm.nih.gov/10360179/) · PMID 10360179
   <br>Crystal structures of c-Src revealing the autoinhibitory mechanism - the SH3-SH2 clamp on the back of the kinase domain.
3. **[A]** Cowan-Jacob SW et al., *Structure* 2005;13:861-71. [The crystal structure of a c-Src complex in an active conformation suggests possible steps in c-Src activation.](https://pubmed.ncbi.nlm.nih.gov/15939018/) · PMID 15939018
   <br>An ACTIVE-conformation c-Src complex, with the proposed steps of activation: the second state, and the path between.
4. **[A]** Fajer M et al., *J Phys Chem B* 2017;121:3352-3363. [The Activation of c-Src Tyrosine Kinase: Conformational Transition Pathway and Free Energy Landscape.](https://doi.org/10.1021/acs.jpcb.6b08409) · PMID 27715044
   <br>The conformational transition pathway and free energy landscape of c-Src activation - the open/closed transition computed end to end.
5. **[A]** Boczek EE et al., *J Biol Chem* 2019;294:13186-13197. [Autophosphorylation activates c-Src kinase through global structural rearrangements.](https://doi.org/10.1074/jbc.RA119.008199) · PMID 31331936
   <br>Autophosphorylation activates c-Src through GLOBAL structural rearrangements - the inter-domain change measured, not the active site.

### ABL1 (P00519)

1. **[A]** Nagar B et al., *Cell* 2003;112:859-71. [Structural basis for the autoinhibition of c-Abl tyrosine kinase.](https://pubmed.ncbi.nlm.nih.gov/12654251/) · PMID 12654251
   <br>Structural basis for the autoinhibition of c-Abl: the assembled SH3-SH2-kinase clamp. The CLOSED state.
2. **[A]** Hantschel O et al., *Cell* 2003;112:845-57. [A myristoyl/phosphotyrosine switch regulates c-Abl.](https://pubmed.ncbi.nlm.nih.gov/12654250/) · PMID 12654250
   <br>The myristoyl/phosphotyrosine switch - the latch that holds the closed state, and what releasing it does.
3. **[A]** Nagar B et al., *Mol Cell* 2006;21:787-98. [Organization of the SH3-SH2 unit in active and inactive forms of the c-Abl tyrosine kinase.](https://pubmed.ncbi.nlm.nih.gov/16543148/) · PMID 16543148
   <br>Organization of the SH3-SH2 unit in ACTIVE AND INACTIVE forms of c-Abl: both inter-domain arrangements in one paper.
4. **[A]** Xie T et al., *Science* 2020;370:. [Conformational states dynamically populated by a kinase determine its function.](https://doi.org/10.1126/science.abc2754) · PMID 33004676
   <br>Conformational states dynamically populated by a kinase determine its function - the Abl state ensemble, not a single structure.
5. **[B]** de Buhr S et al., *Elife* 2023;12:. [Myristoyl's dual role in allosterically regulating and localizing Abl kinase.](https://doi.org/10.7554/eLife.85216) · PMID 37843155
   <br>The myristoyl group's dual role in allosterically regulating and localising Abl: simulations of the latched and unlatched arrangements.

### BTK (Q06187)

1. **[A]** Wang Q et al., *Elife* 2015;4:. [Autoinhibition of Bruton's tyrosine kinase (Btk) and activation by soluble inositol hexakisphosphate.](https://doi.org/10.7554/eLife.06074) · PMID 25699547
   <br>Autoinhibition of BTK and its activation by soluble IP6: the compact autoinhibited arrangement and what opens it.
2. **[A]** Wang Q et al., *Proc Natl Acad Sci U S A* 2019;116:9390-9399. [Structural mechanism for Bruton's tyrosine kinase activation at the cell membrane.](https://doi.org/10.1073/pnas.1819301116) · PMID 31019091
   <br>D. E. Shaw Research. Structural mechanism for BTK activation at the cell membrane - the full open/closed transition from long-timescale MD.
3. **[A]** Amatya N et al., *Proc Natl Acad Sci U S A* 2019;116:21539-21544. [Lipid-targeting pleckstrin homology domain turns its autoinhibitory face toward the TEC kinases.](https://doi.org/10.1073/pnas.1907566116) · PMID 31591208
   <br>The lipid-targeting PH domain turns its AUTOINHIBITORY face toward the TEC kinases - how the PH-TH module docks in the closed state.
4. **[A]** Joseph RE et al., *Elife* 2020;9:. [Differential impact of BTK active site inhibitors on the conformational state of full-length BTK.](https://doi.org/10.7554/eLife.60470) · PMID 33226337
   <br>Differential impact of active-site inhibitors on the conformational state of FULL-LENGTH BTK: drugs read out as open or closed.
5. **[A]** Joseph RE et al., *Elife* 2024;13:. [Impact of the clinically approved BTK inhibitors on the conformation of full-length BTK and analysis of the development of BTK resistance mutations in chronic lymphocytic leukemia.](https://doi.org/10.7554/eLife.95488) · PMID 39728925
   <br>The clinically approved BTK inhibitors against full-length BTK conformation, with the CLL resistance mutations - conformation and resistance in one study.

### LRRK2 (Q5S007)

1. **[A]** Deniston CK et al., *Nature* 2020;588:344-349. [Structure of LRRK2 in Parkinson's disease and model for microtubule interaction.](https://doi.org/10.1038/s41586-020-2673-2) · PMID 32814344
   <br>Cryo-EM of LRRK2 and a model for microtubule interaction: the first full inter-domain architecture.
2. **[A]** Watanabe R et al., *Cell* 2020;182:1508-1518.e16. [The In Situ Structure of Parkinson's Disease-Linked LRRK2.](https://doi.org/10.1016/j.cell.2020.08.004) · PMID 32783917
   <br>The IN SITU structure of LRRK2 inside cells - the arrangement as it actually occurs, including the filament form.
3. **[A]** Myasnikov A et al., *Cell* 2021;184:3519-3527.e10. [Structural analysis of the full-length human LRRK2.](https://doi.org/10.1016/j.cell.2021.05.004) · PMID 34107286
   <br>Structural analysis of full-length human LRRK2: the autoinhibited, closed inter-domain arrangement of the whole protein.
4. **[A]** Zhu H et al., *Science* 2023;382:1404-1411. [Rab29-dependent asymmetrical activation of leucine-rich repeat kinase 2.](https://doi.org/10.1126/science.adi9926) · PMID 38127736
   <br>Rab29-dependent ASYMMETRICAL activation - two different inter-domain arrangements within one assembly.
5. **[A]** Villagran Suarez A et al., *Cell* 2026;189:6460-6473.e7. [The structural basis for LRRK2's activation and autoinhibition.](https://doi.org/10.1016/j.cell.2026.07.027) · PMID 42575089
   <br>The structural basis for LRRK2's activation and autoinhibition: the open and closed states and the transition, 2026.

### CFTR (P13569)

1. **[B]** Zhang Z et al., *Cell* 2016;167:1586-1597.e9. [Atomic Structure of the Cystic Fibrosis Transmembrane Conductance Regulator.](https://doi.org/10.1016/j.cell.2016.11.014) · PMID 27912062
   <br>The first atomic structure of CFTR (zebrafish, dephosphorylated): the NBD-separated state.
2. **[A]** Liu F et al., *Cell* 2017;169:85-95.e8. [Molecular Structure of the Human CFTR Ion Channel.](https://doi.org/10.1016/j.cell.2017.02.024) · PMID 28340353
   <br>Molecular structure of the HUMAN CFTR ion channel in the dephosphorylated, NBD-separated state. Our 5UAK lineage.
3. **[A]** Zhang Z et al., *Cell* 2017;170:483-491.e8. [Conformational Changes of CFTR upon Phosphorylation and ATP Binding.](https://doi.org/10.1016/j.cell.2017.06.041) · PMID 28735752
   <br>Conformational changes of CFTR upon phosphorylation AND ATP binding - the NBD-separated and NBD-dimerised states in one study. Exactly our open/closed pair.
4. **[A]** Zhang Z et al., *Proc Natl Acad Sci U S A* 2018;115:12757-12762. [Molecular structure of the ATP-bound, phosphorylated human CFTR.](https://doi.org/10.1073/pnas.1815287115) · PMID 30459277
   <br>The ATP-bound, phosphorylated human CFTR: the NBD-dimerised CLOSED state at higher resolution. Our 6MSM lineage.
5. **[A]** Levring J et al., *Nature* 2023;616:606-614. [CFTR function, pathology and pharmacology at single-molecule resolution.](https://doi.org/10.1038/s41586-023-05854-7) · PMID 36949202
   <br>CFTR function, pathology and pharmacology at single-molecule resolution - the state occupancies measured one molecule at a time.

### ABCB1 (P08183)

1. **[A]** Alam A et al., *Proc Natl Acad Sci U S A* 2018;115:E1973-E1982. [Structure of a zosuquidar and UIC2-bound human-mouse chimeric ABCB1.](https://doi.org/10.1073/pnas.1717044115) · PMID 29440498
   <br>Zosuquidar- and UIC2-bound human-mouse chimeric ABCB1: an inhibitor-trapped inward-facing arrangement.
2. **[A]** Alam A et al., *Science* 2019;363:753-756. [Structural insight into substrate and inhibitor discrimination by human P-glycoprotein.](https://doi.org/10.1126/science.aav7102) · PMID 30765569
   <br>Structural insight into substrate and inhibitor discrimination by human P-glycoprotein - different NBD arrangements for different cargo.
3. **[A]** Kodan A et al., *Nat Commun* 2019;10:88. [Inward- and outward-facing X-ray crystal structures of homodimeric P-glycoprotein CmABCB1.](https://doi.org/10.1038/s41467-018-08007-x) · PMID 30622258
   <br>INWARD- AND OUTWARD-FACING X-ray structures of a homodimeric P-glycoprotein: both ends of the transport cycle in one paper.
4. **[A]** Nosol K et al., *Proc Natl Acad Sci U S A* 2020;117:26245-26253. [Cryo-EM structures reveal distinct mechanisms of inhibition of the human multidrug transporter ABCB1.](https://doi.org/10.1073/pnas.2010264117) · PMID 33020312
   <br>Cryo-EM structures revealing distinct mechanisms of inhibition of human ABCB1 - several distinct NBD arrangements.
5. **[A]** Kopcho N et al., *Sci Rep* 2019;9:15092. [Dynamics of ABC Transporter P-glycoprotein in Three Conformational States.](https://doi.org/10.1038/s41598-019-50578-2) · PMID 31641149
   <br>Dynamics of P-glycoprotein in THREE conformational states - the states characterised dynamically, not as static snapshots.

### DDX3X (O00571)

1. **[A]** Floor SN et al., *J Biol Chem* 2016;291:2412-21. [Autoinhibitory Interdomain Interactions and Subfamily-specific Extensions Redefine the Catalytic Core of the Human DEAD-box Protein DDX3.](https://doi.org/10.1074/jbc.M115.700625) · PMID 26598523
   <br>Autoinhibitory INTERDOMAIN interactions redefine the catalytic core of human DDX3 - the RecA1-RecA2 open/closed question stated directly.
2. **[A]** Epling LB et al., *J Mol Biol* 2015;427:1779-1796. [Cancer-associated mutants of RNA helicase DDX3X are defective in RNA-stimulated ATP hydrolysis.](https://doi.org/10.1016/j.jmb.2015.02.015) · PMID 25724843
   <br>Cancer-associated DDX3X mutants defective in RNA-stimulated ATP hydrolysis, with crystal structures: the mutations that break domain closure.
3. **[A]** Song H et al., *Nat Commun* 2019;10:3085. [The mechanism of RNA duplex recognition and unwinding by DEAD-box helicase DDX3X.](https://doi.org/10.1038/s41467-019-11083-2) · PMID 31300642
   <br>The mechanism of RNA duplex recognition and unwinding by DDX3X - the RNA-bound CLOSED state of the two RecA lobes.
4. **[B]** Moore AFT et al., *ACS Omega* 2021;6:12640-12646. [Interactions of the C-Terminal Truncated DEAD-Box Protein DDX3X With RNA and Nucleotide Substrates.](https://doi.org/10.1021/acsomega.1c00700) · PMID 34056415
   <br>C-terminally truncated DDX3X with RNA and nucleotide substrates: how ligand occupancy sets the inter-lobe arrangement.
5. **[A]** Ghosh P et al., *Hum Mol Genet* 2026;35:. [DDX3X syndrome mutations lock DDX3X-RNA conformational states to drive persistent pathological condensation and neuronal death.](https://doi.org/pii: ddag066. 10.1093/hmg/ddag066) · PMID 42497113
   <br>DDX3X syndrome mutations LOCK DDX3X-RNA conformational states - pathogenic variants acting by trapping one state. 2026.

## Reproducing

```
scripts/ten.py      the ten selected accessions
scripts/gather.py   AlphaFold v6 + PAE, experimental PDB/mmCIF, ModelArchive, SWISS-MODEL templates
scripts/geom.py     all-pairs inter-domain geometry -> meta.json
scripts/states.py   picks the closed and open member of the largest-moving pair -> states.json
scripts/muts.py     the literature mutation set, verified against canonical sequences
scripts/ddg.py      dual-state PyRosetta ddG, sequence-aligned numbering -> ddg.json
scripts/mutfeat.py  per-mutation predictors, pLDDT, pockets, interface -> mutfeat.json
scripts/clust.py    k=2 clustering + gnomAD r4 -> clusters.json
scripts/homol.py    phmmer vs reviewed human SwissProt -> homologs.json
scripts/confpapers.py  curated conformational-state literature, PubMed-verified -> conf_papers.json
scripts/rep10.py    builds the HTML
```

Structure files (`af/`, `st/`, `pae/`, 78 MB) are not committed; `gather.py` refetches them.
Everything else needed to rebuild the reports is in `data/`.
