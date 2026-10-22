# Variant clustering: reproducing the Jeanpierre/Debeaupuis pipeline across the JAK family

Regenerated 2026-10-22 19:40. Source data under `/Users/chervov/orianne_tyk2`; generator is
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
| ddG closed (PyRosetta) | 0% | **done** - reproduces their medians, AUC 0.770 on their clusters |
| ddG open (PyRosetta) | 0% | **done** - AUC 0.767 |
| **ddG open - closed** | 0% | **done - and it carries no signal: AUC 0.504, p=0.89** |
| AlphaMissense | 70.3% | **100%** - source release, keyed on UniProt (section 57) |
| SIFT | 43.7% | 33% |
| PolyPhen-2 | 43.7% | 32% |
| BLOSUM62 | 43.7% | **100%** - computed locally |
| ClinPred | 85.8% | 96% of the SNV subset |
| CADD | - | **0% - licence-restricted in dbNSFP** |
| MutFunc | 92.1% | not attempted |

**Why dbNSFP coverage caps at ~33%**: it is keyed on *genomic* variants, so it holds only
substitutions reachable by a single nucleotide change. This is why **V678F - this project's
headline TYK2 variant - has no PolyPhen, SIFT or REVEL score**. ESM-1b and BLOSUM62 score
protein sequence directly and have no such limit.

**AlphaMissense is no longer in that group.** Its scores are now taken from the source release
(`AlphaMissense_aa_substitutions.tsv.gz`), which is keyed on UniProt accession and protein-level
substitution, giving **100% coverage for all four JAKs** - including V678F (0.254) and H582W
(0.345), both of which it calls benign. The paper's reported 70.3% missingness is an artefact of
joining through genomic coordinates, not a property of AlphaMissense. The cross-check against our
earlier dbNSFP extraction also exposed a defect in that extraction - 290-531 values per column
carried on substitutions needing two or three nucleotide changes, which cannot have a dbNSFP row -
now blanked. See `mutation_analysis.md` section 57.

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
| AlphaMissense | 0.859 | 0.607 | 0.879 | 0.745 | 0.815 |
| ESM-1b | 0.796 | 0.589 | 0.823 | 0.708 | 0.766 |
| REVEL | 0.856 | 0.587 | 0.805 | 0.693 | 0.762 |
| SIFT | 0.760 | 0.579 | 0.787 | 0.681 | 0.743 |
| PolyPhen-2 | 0.748 | 0.583 | 0.759 | 0.667 | 0.741 |
| BLOSUM62 | 0.616 | 0.546 | 0.642 | 0.595 | 0.618 |
| **combined (CV)** | **0.859** | **0.605** | **0.877** | **0.742** | **0.812** |

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

## Dual-state ddG: the key feature, tested and negative

The distinctive component of the pipeline is **ddG_open - ddG_closed**, a conformational-
preference estimate rather than a stability estimate. It has now been computed two independent
ways. The protocol was first verified against PyRosetta's own published ddG tutorial (PagP set):
Pearson **0.3590** against their 0.3590768, and **0.6712** against their 0.6720891 excluding
proline - agreement to four decimals, so what follows is a result about the feature.

### Test 1 - JAK1, their models, their clusters

500 variants from Dataset EV1, 250 from each cluster, scored on the
**Jeanpierre open and closed models themselves**. Their structures, their variants, their
labels - no confound left. Values clipped to [-10, 10] as the paper does.

| feature | median their C1 | median their C2 | AUC vs their labels | p |
|---|--:|--:|--:|--:|
| ddG_closed | -1.64 | -6.34 | 0.770 | 6.29e-26 |
| ddG_open | -1.82 | -6.60 | 0.767 | 2.35e-25 |
| **ddG_open - ddG_closed** | +0.00 | +0.00 | **0.504** | 0.891 |
| *paper's reported medians* | *-2.05* | *-6.36* | *-* | *-* |

ddG_closed reproduces their published medians to within 0.4 kcal/mol and separates their
clusters well. Their headline feature does not separate them at all. The reason is visible in
one number: **closed and open correlate at r = 0.822**, so the subtraction cancels the
signal and leaves repack residual.

### Test 2 - TYK2, a matched pair of AlphaFold 3 models

The objection to test 1 is that the two JAK1 reference models were not built the same way, so
a real difference could be swamped by model-to-model inconsistency. Two TYK2 structures were
generated on the AF3 server as a **matched pair** and the 4OLI interface variants rescored.

- baseline score gap between states: **271 REU** (old mismatched pair 1048, Jeanpierre JAK1 181)
- Pearson r, ddG_closed vs ddG_open: **0.526**
- within +/-10 in both states: **67%**

Better-conditioned by every measure, and it does not help:

| feature | rho abundance | rho IFN-a 1 U | rho IFN-a 100 U | AUC vs IFN-a 1 U |
|---|--:|--:|--:|--:|
| ddG_closed | -0.025 | +0.052 | +0.119 | 0.520 |
| ddG_open | -0.025 | +0.070 | +0.150 | 0.523 |
| **ddG_open - ddG_closed** | -0.027 | +0.016 | +0.019 | 0.476 |
| AlphaMissense (reference) | -0.453 | -0.053 | -0.164 | 0.544 |

Here the two states correlate only weakly, so the difference keeps its magnitude - but the
decorrelation comes from the models differing in ways unrelated to the substitution, so what
it keeps is noise. **The feature fails at both ends of the same axis**: too correlated and the
subtraction cancels the signal, too decorrelated and it measures model discrepancy. No
intermediate regime escapes this.

### What this says about the paper

Not that their clusters are wrong - something narrower. Their clustering is recovered by the
**stability** term, which we reproduce closely; the **conformational** term they built the
pipeline around contributes nothing to it, and neither term predicts measured phenotype in the
TYK2 DMS. Their clusters also track the consensus of four sequence predictors (ClinPred 0.946,
PolyPhen 0.943, REVEL 0.901, ESM-1b 0.892) - but all four were **inputs** to the clustering, so
those figures measure feature weight, not external validation. Silhouette is **0.098** and our
reproduction agrees with their labels on **65.3%** of variants, *below* the **65.5%** a
majority-class classifier achieves (ARI 0.087).

Full detail, including the protocol verification and a correction to an earlier wrong diagnosis,
is in `mutation_analysis.md` sections 56-57.

