# Variant clustering: reproducing the Jeanpierre/Debeaupuis pipeline across the JAK family

Regenerated 2026-10-22 18:25. Source data under `/Users/chervov/orianne_tyk2`; generator is
`analysis/make_clustering_report.py`. Companion detail lives in `mutation_analysis.md` sections 51-52.

## The method being reproduced

Jeanpierre, Debeaupuis et al., *EMBO Molecular Medicine* 2025, 17:3275-3299 - the source of the
Jeanpierre open/closed JAK1 models used as references throughout this project. They scored 21,926
JAK1 missense variants on 11 features and clustered them.

**Thermodynamic convention (Appendix S3), which is inverted from Rosetta's native sign:**

> ddG_m = dG_WT - dG_m. If ddG_m < 0 the mutation is **destabilizing**; if > 0, **stabilizing**.
>
> ddG_open,m > ddG_closed,m corresponds to stronger stabilization (or weaker destabilization) of
> the open versus closed state, **leading to more open configurations in mutants**.

So the pipeline's distinctive feature is **ddG_open - ddG_closed**: a conformational-preference
estimate, not a stability estimate. Clustering is **semi-supervised K-means on Gower distance**,
seeded with 10 labelled variants; Gower is used because it handles missing features natively.

### Their 11 features, with the missingness they report

| feature | missing (paper, JAK1) | available to us |
|---|--:|---|
| ESM-1b | 0% | **100%** - files supplied, verified against UniProt |
| ddG closed (PyRosetta) | 0% | in progress |
| ddG open (PyRosetta) | 0% | in progress |
| **ddG open - closed** | 0% | **in progress - the key feature** |
| AlphaMissense | 70.3% | 33% (dbNSFP) |
| SIFT | 43.7% | 33% |
| PolyPhen-2 | 43.7% | 32% |
| BLOSUM62 | 43.7% | **100%** - computed locally |
| ClinPred | 85.8% | 96% of the SNV subset |
| CADD | - | **0% - licence-restricted in dbNSFP** |
| MutFunc | 92.1% | not attempted |

**Why coverage caps at ~33%**: dbNSFP is keyed on *genomic* variants, so it holds only
substitutions reachable by a single nucleotide change. This is why **V678F - this project's
headline TYK2 variant - has no PolyPhen, SIFT, REVEL or AlphaMissense score at all**. ESM-1b
scores protein sequence directly and has no such limit.

## Data: what it is, how it was obtained, how complete it is

Every number in this document traces to one of the following. Access dates are 2026-10-22.

### 1. Deep mutational scan - the ground truth

| | |
|---|---|
| what | >23,000 single amino-acid substitutions across TYK2, assayed for IFN-alpha signalling and protein abundance |
| source | MaveDB, `urn:mavedb:00001270-a` (signalling) and `urn:mavedb:00001271-a-1` (abundance) |
| how | downloaded as score CSVs; parsed from the `hgvs_pro` column (`p.Xaa###Yaa`) |
| system | HEK293T with all endogenous TYK2 knocked out by CRISPR, STAT2 + IRF9 restored by piggyBac |
| signalling assay | barcoded luciferase under an 8x ISRE promoter, doxycycline-inducible TYK2; IFN-alpha 2a at 1, 10 or 100 U/mL; RNA harvested at 6 h |
| abundance assay | VAMP-seq: N-terminal **GFP**-tagged TYK2 with a co-transcriptional **BFP** normalisation control, FACS-sorted into four quartile bins on the GFP:BFP ratio |
| replication | biological triplicate; signalling libraries amplified in duplicate per replicate |
| completeness | signalling 23,737 of 23,740 possible variants (>99.9%); abundance 23,716 (>99.9%) |
| **we hold** | **1 U/mL (22,536), 100 U/mL (22,536), abundance (22,516)** after restricting to missense with parseable HGVS |
| **not downloaded** | the **10 U/mL** arm and the inhibitor arms (BMS-986202, NDI-034858) - available, never pulled |

Scale: 0 = wild type, **-0.352 = the nonsense median**, i.e. a dead protein. Abundance measures
steady-state protein per unit mRNA, so a low score means the protein is made and then degraded -
a proxy for folding stability, though a degron or aggregation would look the same.

### 2. ESM-1b - the evolutionary score

| | |
|---|---|
| what | protein language model log-odds, one file per JAK, supplied by the user |
| how | files in `~/Downloads`, named by UniProt accession |
| completeness | **100%** - every position x 20 amino acids, including self-substitutions scored 0.0 |
| verification | every WT residue in every row checked against the UniProt sequence: **100% match in all four genes** |
| identification | not labelled as ESM-1b in the files; identified by (a) score range and median matching the paper's reported ESM-1b cluster means, (b) JAK1 reducing to exactly 21,926 non-self variants, the paper's own count |

### 3. Sequence predictors - dbNSFP via MyVariant.info

| | |
|---|---|
| what | PolyPhen-2 (HDIV/HVAR), SIFT, REVEL, AlphaMissense, ClinPred |
| how | `myvariant.info/v1/query`, `q=dbnsfp.genename:<GENE>`, scrolled with `fetch_all` |
| raw hits | 9,481 records for TYK2, collapsing to 7,917 unique (position, alt) pairs |
| completeness | **~33% of all possible substitutions** |
| **why not more** | dbNSFP is keyed on **genomic** variants, so it contains only substitutions reachable by a **single nucleotide change**. Two-nucleotide substitutions are absent entirely - including **V678F**, this project's headline variant |
| ClinPred note | returned as a nested object `{pred, rankscore, score}`, not a bare float; the `score` field is used |

### 4. CADD - attempted and unavailable

Requested as `dbnsfp.cadd.phred` and `cadd.phred`; MyVariant returned **0 of 9,205** records with a
value. CADD is licence-restricted in the academic dbNSFP build. Obtaining it needs either the CADD
website (per-VCF submission) or the ~80 GB whole-genome score file. **This is one of only two
sequence-based pathogenicity scores the paper names**, so its absence is a real gap in the
reproduction, not a convenience omission.

### 5. Population and clinical databases

| source | field | TYK2 | JAK1 | JAK2 | JAK3 |
|---|---|--:|--:|--:|--:|
| gnomAD (exome, then genome) | `gnomad_exome.af.af` | 702 | 330 | 512 | 526 |
| ClinVar | `clinvar.rcv.clinical_significance` | 414 | 272 | 223 | 327 |

Both via the same MyVariant query, so both inherit the ~33% single-nucleotide ceiling. The paper
reported 289 JAK1 gnomAD variants; we retrieve 330, consistent with a later gnomAD release.

**ClinVar is not usable as ground truth for TYK2**: of 414 records, **381 (89%) are "Uncertain
significance"**, with only 12 Pathogenic, 1 Likely pathogenic, 8 Benign and 21 Likely benign. Only
2 pathogenic variants overlap the clustered set, so no pathogenic-enrichment test is possible.
This is precisely the gap the DMS fills.

### 6. Structures used for ddG

| state | source | FERM-JH1 | note |
|---|---|--:|---|
| closed | AlphaFold `AF-P29597-F1` | 39.7 A | the compact TYK2 model |
| open | our run `TYK2_20261022_010154/selected_open.pdb` | 93.4 A | wild type, template-free, 512/8192; 4.8 A from Jeanpierre's open JAK1 model |

The paper built both JAK1 states with a modified AlphaFold2. No experimental multi-domain TYK2
structure exists (`mutation_analysis.md` section 35), so the open state here is necessarily a
prediction - validated only by its 5-8 A agreement with cryo-EM **JAK1** 8EWY.

### 7. Derived locally, no external dependency

BLOSUM62 (Biopython), side-chain volume change (Zamyatnin), hydrophobicity change
(Kyte-Doolittle). **100% coverage**, instant.

## Provenance check on the ESM-1b files

| gene | UniProt | rows | positions | UniProt length | WT residue matches |
|---|---|--:|---|--:|---|
| JAK1 | P23458 | 23,080 | 1-1154 | 1,154 | 100% |
| JAK2 | O60674 | 22,640 | 1-1132 | 1,132 | 100% |
| JAK3 | P52333 | 22,480 | 1-1124 | 1,124 | 100% |
| TYK2 | P29597 | 23,740 | 1-1187 | 1,187 | 100% |

After dropping self-substitutions JAK1 gives **21,926** - exactly the count the paper reports,
confirming these files are the paper's own input rather than a lookalike.

## Clustering and gnomAD validation, all four JAKs

| gene | Cluster 1 | Cluster 2 | ESM-1b C1 | ESM-1b C2 | gnomAD in C1 | Fisher p |
|---|--:|--:|--:|--:|---|--:|
| JAK1 | 13,785 | 8,141 | -6.44 | -12.86 | 308/330 (93%) | 1.2e-37 |
| JAK2 | 10,962 | 10,546 | -6.91 | -13.53 | 440/512 (86%) | 2.3e-61 |
| JAK3 | 10,011 | 11,345 | -7.57 | -13.64 | 402/526 (76%) | 2.0e-42 |
| TYK2 | 11,498 | 11,055 | -7.35 | -13.79 | 554/702 (79%) | 2.4e-51 |
| *paper, JAK1* | *7,559* | *14,367* | *-4.47* | *-10.75* | *214/289 (74%)* | - |

The paper's central validation - common variants fall in the benign cluster - **reproduces in
every JAK**, at 76-93% against a ~50% background. Our cluster *sizes* differ from theirs
because the feature space differs: no CADD, no ddG yet, and dbNSFP at a third of their coverage.

## What the features actually predict, tested against the TYK2 deep mutational scan

TYK2 is the only JAK with a DMS (22,536 variants on signalling at two doses, 22,516 on
abundance), so the pipeline can be scored against measured phenotype - which the paper could
not do. Targets are the bottom decile of each assay; the combined model is cross-validated
with folds grouped by residue position so substitutions at one site cannot leak between folds.

| predictor | abundance | IFN-a 1 U/mL | IFN-a 100 U/mL | either dose | both doses |
|---|--:|--:|--:|--:|--:|
| ESM-1b | 0.796 | 0.589 | 0.823 | 0.708 | 0.765 |
| AlphaMissense | 0.848 | 0.579 | 0.834 | 0.699 | 0.787 |
| REVEL | 0.840 | 0.572 | 0.777 | 0.670 | 0.736 |
| SIFT | 0.739 | 0.579 | 0.765 | 0.670 | 0.724 |
| PolyPhen-2 | 0.732 | 0.573 | 0.746 | 0.654 | 0.727 |
| BLOSUM62 | 0.616 | 0.546 | 0.642 | 0.595 | 0.618 |
| **combined (CV)** | **0.876** | **0.593** | **0.872** | **0.726** | **0.836** |

**The dose matters more than the predictor.** At 100 U/mL the panel reaches 0.87, matching its
performance on abundance. At 1 U/mL it collapses to 0.60. The two doses correlate at only
rho = +0.52, so they are substantially different measurements: at saturating ligand the readout
is dominated by variants that simply broke the protein, which these tools detect well; at
limiting ligand the *activating* variants appear - V678M +0.561, V678I +0.520, H582W +1.339 -
and a tool trained to separate damaging from tolerated has no representation for a variant that
signals **more** than wild type.

**Consequence for the paper's application.** Its clinical premise is identifying
**gain-of-function** JAK1 variants. AUC 0.60 on the dose where gain of function is visible,
against 0.87 where it is not, is the quantitative reason a pathogenicity panel is the wrong
instrument for that question - and why the structural dual-state component is needed at all.

## Dual-state ddG

469 variants computed, both states, 3 repacks each.

- ddG_open - ddG_closed: median +1.13, range -691.84 to +1135.97
- repack SD (precision of a single ddG): median 0.00 kcal/mol

