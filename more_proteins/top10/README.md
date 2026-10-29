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
scripts/rep10.py    builds the HTML
```

Structure files (`af/`, `st/`, `pae/`, 78 MB) are not committed; `gather.py` refetches them.
Everything else needed to rebuild the reports is in `data/`.
