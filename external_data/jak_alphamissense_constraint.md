# JAK family missense constraint — AlphaMissense on identical footing

How many possible missense variants in each JAK kinase are predicted damaging, measured the
same way for all four genes. Retrieved 2 November 2026.

**Why this file exists.** The per-gene tables in `external_data/<GENE>/` were assembled from
different source sets — JAK1's from a narrower one, the others including the deep mutational scans
and the full observed sets. Counting AlphaMissense classes in those tables therefore compares
sampling schemes, not genes. This file recomputes the split over **every SNV-reachable substitution
in each coding sequence**, with no selection by what has been observed in patients.

## Result

| gene | aa | substitutions | **likely benign** | ambiguous | **likely pathogenic** | mean AlphaMissense |
|---|--:|--:|--:|--:|--:|--:|
| **JAK1** | 1,154 | 6,867 | 46.1% | 11.4% | **42.6%** | 0.496 |
| **JAK2** | 1,132 | 6,691 | 51.8% | 10.7% | **37.5%** | 0.449 |
| **JAK3** | 1,124 | 6,602 | 59.4% | 11.7% | **28.9%** | 0.380 |
| **TYK2** | 1,187 | 6,981 | 63.1% | 10.7% | **26.2%** | 0.352 |
| *human proteome* | | *71M* | *57%* | *11%* | *32%* | |

Classes are AlphaMissense's published cutoffs: likely benign < 0.34, ambiguous, likely pathogenic
> 0.564. Proteome-wide figures from [Cheng et al., *Science* 2023](https://pubmed.ncbi.nlm.nih.gov/37733863/).

**Ordering: JAK1 > JAK2 > JAK3 > TYK2.** JAK1 and JAK2 are more constrained than an average human
protein; JAK3 and TYK2 less so. That matches what is known clinically — TYK2 tolerates loss of
function in humans (the common P1104A hypomorph), JAK3 loss causes SCID only biallelically with
unaffected carriers, while JAK1 and JAK2 are essential. It also matches the independent coding-region
AVI means in [`jak_family_avi_locus.md`](jak_family_avi_locus.md) (JAK1 0.856, JAK2 0.862, JAK3 0.677,
TYK2 0.607).

### This supersedes any count taken from the per-gene tables

Counting the same `AlphaMissense class` column inside the tables gives, for JAK1, **21.8%** likely
pathogenic — against **42.6%** here. JAK1 appeared to be the *least* constrained of the four and is
in fact the *most*. The cause is sampling: a table weighted toward variants seen in people is
enriched for variants that are tolerated, because that is why they were seen. Do not read
constraint off those tables.

## Coverage, and why these percentages are lower bounds

Only **31%** of possible substitutions are reachable by a single nucleotide change (6,602–6,981 of
~21,500 per gene); the rest need two or three changes in one codon and have no SNV to score.

Those reachable substitutions are **chemically more conservative**, by a wide margin:

| gene | BLOSUM62, reachable | BLOSUM62, unreachable |
|---|--:|--:|
| JAK1 | **−0.542** | −1.763 |
| JAK2 | **−0.528** | −1.774 |
| JAK3 | **−0.696** | −1.740 |
| TYK2 | **−0.686** | −1.754 |

A consistent gap of ~1.2 BLOSUM units. Single-base changes reach the similar amino acids; the
drastic ones mostly require multiple changes. **So the pathogenic fractions above understate the
true figure over all ~21,500 substitutions.** The same ceiling applies to dbNSFP, gnomAD and the
AlphaGenome Atlas — any SNV-indexed resource. Only predictors that work directly in protein space
(AlphaMissense's own full release, ESM1b) cover the complete set.

## Two checks performed

**AlphaMissense is exactly constant per amino-acid substitution.** Across ~2,767 substitutions
reachable by more than one codon change, the largest within-substitution spread is **0.000000**. It
is a pure protein-level score, so aggregating by `max` over codon changes (as
`external_data/JAK2/jak2_cds_avi_protein.csv` does for AVI) loses nothing for this feature.

**Zero reference mismatches in 41,409 CDS SNVs** across the four genes. JAK1, JAK3 and TYK2 are on
the minus strand, so every base had to be complemented before codon translation; every one matched
the Ensembl CDS. This is the strand handling validated directly.

## Context: predicted versus known

| gene | predicted likely pathogenic | **ClinVar pathogenic** | ClinVar benign | ClinVar VUS |
|---|--:|--:|--:|--:|
| JAK1 | ~2,900 | **3** | 8 | 361 |
| JAK2 | ~2,500 | **7** | 14 | 300 |
| JAK3 | ~1,900 | **22** | 21 | 319 |
| TYK2 | ~1,800 | **2** | 21 | 443 |

Roughly **90–95% of classified JAK variants are of uncertain significance**, and the predicted count
exceeds the known count by two to three orders of magnitude. AlphaMissense's own paper reports the
same globally: of the 4M+ missense variants observed in humans, only 2% carry an expert annotation.

**And the predicted-pathogenic set is a predicted *loss-of-function* set.** JAK2 V617F — the driver
in ~95% of polycythaemia vera — scores **0.334**, classed *likely benign*, at the 55th percentile of
JAK2. The activating variants that matter clinically for JAK2 sit inside the predicted-benign
majority, not the pathogenic third. These counts answer "how many substitutions would damage the
protein", which is not the same question as "how many cause disease".

## Files

| file | contents |
|---|---|
| [`jak_alphamissense_reachable.csv`](jak_alphamissense_reachable.csv) | 27,141 rows: every SNV-reachable substitution in the four genes with its AlphaMissense score |
| [`jak_alphamissense_summary.csv`](jak_alphamissense_summary.csv) | the summary table above |
| [`jak_alphamissense.py`](jak_alphamissense.py) | reproduces all of it, including both checks |

Method: AlphaMissense is one of the 18 features in the Atlas `AVI_SCORE_MODEL_FEATURES` scorer, so
one `query_interval` per coding exon returns it for every CDS SNV — about 8 seconds per gene.
Consequences come from local codon translation against the Ensembl CDS sequence, strand-aware.

**Non-commercial use only** per the AlphaGenome terms; not validated for clinical use.
