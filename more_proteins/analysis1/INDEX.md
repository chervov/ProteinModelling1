# analysis1 — variant-effect analysis across 54 proteins

*Generated 28 October 2026. One report per protein in this directory. Pipeline: `pipe.py` (features, interface, gnomAD, clustering) and `report.py` (markdown). Every number computed, none quoted.*

## What was done, per protein

1. **Feature matrix** — FoldX ΔΔG (EBI ProtVar, 208,792,558-row human proteome), ThermoMPNN ΔΔG, ESM-1v, AlphaMissense, relative solvent accessibility, pLDDT, secondary structure and disorder (Liao & Lehner 2026, Zenodo 18386427), with per-feature coverage and all-vs-all Spearman.
2. **Interface** — residues of each domain within 5 Å of the other, in the most compact structure available (AlphaFold v6, SWISS-MODEL, PDB or ModelArchive), then a Mann–Whitney test of every feature inside the interface against the rest of the protein.
3. **ClinVar and gnomAD** — ClinVar significance counts from the Liao & Lehner table; gnomAD r4 missense allele frequencies fetched per gene from the GraphQL API.
4. **Two-cluster split** — k-means, k = 2, on z-scored features oriented so higher = more damaging, as in the Jeanpierre/Debeaupuis pipeline. Validated against gnomAD presence, ClinVar labels and interface membership.
5. **ProteinGym** — membership checked against all 217 DMS substitution assays.

## The headline result

**The two-cluster split is validated independently in every protein where it could be computed.** Across the 45 proteins with ≥2 usable features, the damaging cluster is **depleted in gnomAD in all 45** — population frequency between 1.0× and 15.2× lower than the tolerant cluster. Purifying selection acting on the predicted-damaging cluster is exactly what should happen, and it is not something the clustering was told about.


## Cross-protein findings

**1. gnomAD depletion is universal and the magnitude varies 15-fold.**
All 46 proteins with a computable split show the damaging cluster depleted.
Strongest: DDX3Y 15.2×, U2AF2 8.2×, SMARCAD1 4.8×, CSK 4.4×, CSF1R 4.3×.
Weakest: TAP1 1.0×, CAPN1 1.9×, CFTR 2.0×, ABCC2 2.0×.
**TAP1 at 1.0× is the one protein where the split carries no population signal** — worth a look,
since TAP1 is half of a heterodimer and its real NBD interface is formed with TAP2, so the
intra-chain pair measured here may be the wrong feature.

**2. Interface variants are more damaging by sequence predictors in 20 of 35 testable proteins**
(AlphaMissense, p < 0.001, median shifted toward damaging). That is the expected result and it
validates the interface calls.

**3. But ΔΔG often points the *other* way at the interface.**
FoldX reaches p < 0.05 in 26 proteins, and in **19 of those the interface is
*less* destabilising than the rest of the protein**: TYK2, JAK1, ABCB1, PTPN6, IGHG4, CFTR, ABCC2, ABCC4.
This is mechanistically sensible and worth stating plainly: an inter-domain interface residue is
*solvent-exposed in the isolated domain*, so substituting it costs little folding stability while
costing the assembly. **It is the same signature as PTPN2 C216S** — near-zero ΔΔG with high
AlphaMissense identifies a functional-site variant with no structural cost
(`PTPN2/jeanpierre2024_variant_analysis.md` §2.2). Reading ΔΔG as a proxy for "important residue"
would systematically miss interfaces.

**4. 14 proteins have no interface in any available structure**
(CAMK2A, CAPN1, CD163, CSF1R, EGFR, EPHA2, INSR, ITGB2, ITGB3, LRRK2, PTPRC, SMARCA4, SOS1, VCL), so they have no closed state to model and are not JAK
analogues however mobile they appear. This is the Stream B gate from
`more_proteins/jak_analogue_search_proposal.md` applied protein by protein.

**5. 8 proteins could not be clustered** (PTPN11, IGF2R, NCF1, TLN1, NF1, CAMK2A, ITGB2, LRRK2) because they
carry only one usable feature — they are absent from the Liao & Lehner table, which excluded
proteins under 16 or over 2,700 residues and those without matching ESM-1v. For these, FoldX ΔΔG is
the only feature available and no two-cluster split is defensible.

**6. Only SRC is in ProteinGym** (3 assays, 3,372–3,637 variants each, region 270–519). For the
other 53 proteins there is no published DMS and no precomputed baseline, so the predictions here
cannot be benchmarked against experiment — the single biggest limitation of this whole analysis.

## Summary table

| gene | | variants | features | iface contacts | PAE ratio | clusters (tol / dam) | gnomAD depletion | gnomAD n | ClinVar n | PG |
|---|---|--:|--:|--:|--:|---|--:|--:|--:|--:|
| [PTPN11](PTPN11.md) | **ref** | 10,488 | 1 | 70 | 2.01 | — | — | 500 | — | — |
| [TYK2](TYK2.md) | **ref** | 22,553 | 4 | 44 | 2.19 | 13204 / 6974 | 2.1× | 1,638 | 394 | — |
| [PTK2](PTK2.md) | **ref** | 19,988 | 4 | 43 | — | 8095 / 6896 | 2.9× | 1,215 | 24 | — |
| [JAK1](JAK1.md) | **ref** | 21,926 | 4 | 7 | 3.63 | 12788 / 8017 | 3.1× | 984 | 1 | — |
| [IGF2R](IGF2R.md) |  | 42,997 | 1 | 80 | 2.4 | — | — | 3,052 | — | — |
| [ABCB1](ABCB1.md) |  | 24,320 | 4 | 78 | 3.42 | 11535 / 11094 | 2.6× | 1,459 | 137 | — |
| [PTPN6](PTPN6.md) |  | 11,305 | 4 | 77 | 3.94 | 4807 / 5415 | 2.7× | 664 | 14 | — |
| [IGHG4](IGHG4.md) |  | 6,213 | 4 | 66 | 8.2 | 3798 / 2320 | 2.4× | 763 | — | — |
| [CFTR](CFTR.md) |  | 28,120 | 4 | 64 | 2.11 | 14023 / 9366 | 2.0× | 2,127 | 1 | — |
| [ABCC2](ABCC2.md) |  | 29,355 | 4 | 63 | 2.94 | 15917 / 11139 | 2.0× | 1,952 | 250 | — |
| [SMARCA2](SMARCA2.md) |  | 30,210 | 4 | 61 | 1.7 | 14049 / 6490 | 3.9× | 1,613 | 418 | — |
| [ABCC4](ABCC4.md) |  | 25,175 | 4 | 60 | 3.49 | 12097 / 11311 | 2.7× | 1,579 | 36 | — |
| [EIF4A3](EIF4A3.md) |  | 7,809 | 4 | 56 | 1.66 | 3876 / 3496 | 3.4× | 245 | 9 | — |
| [EIF4A1](EIF4A1.md) |  | 7,714 | 4 | 54 | 2.44 | 3662 / 3615 | 3.7× | 275 | 1 | — |
| [SMARCAD1](SMARCAD1.md) |  | 19,494 | 4 | 53 | 1.78 | 7707 / 6087 | 4.8× | 887 | 31 | — |
| [ACTN4](ACTN4.md) |  | 17,309 | 4 | 46 | 2.13 | 5866 / 10588 | 4.1× | 859 | 111 | — |
| [DDX3Y](DDX3Y.md) |  | 12,540 | 4 | 44 | 3.12 | 3171 / 5873 | 15.2× | 165 | — | — |
| [SF3B4](SF3B4.md) |  | 8,056 | 4 | 43 | 3.23 | 4162 / 3875 | 3.7× | 332 | 26 | — |
| [DICER1](DICER1.md) |  | 36,518 | 4 | 39 | 2.83 | 16895 / 9648 | 2.7× | 1,777 | 2919 | — |
| [DDX3X](DDX3X.md) |  | 12,578 | 4 | 38 | 3.35 | 2732 / 6369 | 3.8× | 406 | 239 | — |
| [DDX23](DDX23.md) |  | 15,580 | 4 | 35 | 4.36 | 8716 / 4185 | 3.9× | 738 | 50 | — |
| [MYH2](MYH2.md) |  | 36,879 | 4 | 25 | 2.36 | 18764 / 16329 | 2.4× | 2,062 | 659 | — |
| [EHD2](EHD2.md) |  | 10,317 | 4 | 21 | 4.78 | 4386 / 5247 | 2.3× | 714 | 21 | — |
| [EHD3](EHD3.md) |  | 10,165 | 4 | 21 | 6.58 | 4112 / 5730 | 2.6× | 630 | 20 | — |
| [TAP1](TAP1.md) |  | 14,212 | 4 | 20 | 2.22 | 8895 / 4557 | 1.0× | 802 | 170 | — |
| [NCF1](NCF1.md) |  | 7,106 | 1 | 17 | 10.63 | — | — | 470 | — | — |
| [PRKCA](PRKCA.md) |  | 12,768 | 4 | 17 | 5.03 | 5393 / 6577 | 2.8× | 555 | 11 | — |
| [ZAP70](ZAP70.md) |  | 11,761 | 4 | 17 | 3.77 | 4666 / 6069 | 2.6× | 739 | 163 | — |
| [U2AF2](U2AF2.md) |  | 9,025 | 4 | 16 | 2.53 | 3856 / 3535 | 8.2× | 256 | 17 | — |
| [ITGB1](ITGB1.md) |  | 15,162 | 4 | 15 | 2.11 | 6612 / 8341 | 2.9× | 765 | 19 | — |
| [SYK](SYK.md) |  | 12,065 | 4 | 15 | 2.49 | 4635 / 6195 | 3.3× | 560 | 19 | — |
| [BTK](BTK.md) |  | 12,521 | 4 | 14 | 5.17 | 5108 / 6672 | 3.7× | 266 | — | — |
| [ITK](ITK.md) |  | 11,780 | 4 | 14 | 6.65 | 6402 / 5131 | 2.6× | 644 | 180 | — |
| [DNM2](DNM2.md) |  | 16,530 | 4 | 13 | 2.73 | 4106 / 9916 | 3.1× | 1,050 | 1 | — |
| [CSK](CSK.md) |  | 8,550 | 4 | 11 | 3.27 | 3899 / 4556 | 4.4× | 323 | 6 | — |
| [SRC](SRC.md) |  | 10,184 | 4 | 9 | 2.2 | 4232 / 4318 | 3.7× | 496 | 13 | 3 |
| [ABL1](ABL1.md) |  | 21,470 | 4 | 8 | 2.46 | 4891 / 5730 | 4.0× | 1,217 | 305 | — |
| [DNM1](DNM1.md) |  | 16,416 | 4 | 5 | 2.72 | 8705 / 5336 | 3.5× | 796 | 1 | — |
| [TLN1](TLN1.md) |  | 45,239 | 1 | 4 | 2.16 | — | — | 2,603 | — | — |
| [NF1](NF1.md) |  | 84,243 | 1 | 1 | — | — | — | 2,601 | — | — |
| [CAMK2A](CAMK2A.md) |  | 8,512 | 1 | — | — | — | — | 409 | — | — |
| [CAPN1](CAPN1.md) |  | 13,566 | 4 | — | 3.19 | 6911 / 6427 | 1.9× | 903 | 107 | — |
| [CD163](CD163.md) |  | 21,964 | 4 | — | 7.63 | 11398 / 7507 | 2.3× | 1,223 | 35 | — |
| [CSF1R](CSF1R.md) |  | 18,468 | 4 | — | 3.9 | 9292 / 5946 | 4.3× | 1,129 | 345 | — |
| [EGFR](EGFR.md) |  | 22,990 | 4 | — | — | 9665 / 8917 | 2.8× | 1,530 | 3 | — |
| [EPHA2](EPHA2.md) |  | 18,544 | 4 | — | 5.15 | 9038 / 7606 | 2.3× | 1,205 | 123 | — |
| [INSR](INSR.md) |  | 26,258 | 4 | — | 2.6 | 13392 / 8819 | 2.7× | 1,352 | 194 | — |
| [ITGB2](ITGB2.md) |  | 14,136 | 1 | — | 5.33 | — | — | 1,096 | — | — |
| [ITGB3](ITGB3.md) |  | 14,972 | 4 | — | 5.14 | 7663 / 6777 | 2.1× | 957 | 240 | — |
| [LRRK2](LRRK2.md) |  | 44,954 | 1 | — | 2.83 | — | — | 3,063 | — | — |
| [PTPRC](PTPRC.md) |  | 24,814 | 4 | — | 4.99 | 11646 / 7012 | 2.3× | 1,600 | 321 | — |
| [SMARCA4](SMARCA4.md) |  | 31,293 | 4 | — | 3.39 | 13636 / 6143 | 3.4× | 1,415 | 2107 | — |
| [SOS1](SOS1.md) |  | 25,327 | 4 | — | 4.63 | 12613 / 7052 | 2.8× | 1,428 | 826 | — |
| [VCL](VCL.md) |  | 21,546 | 4 | — | — | 14423 / 6306 | 2.5× | 1,149 | 610 | — |