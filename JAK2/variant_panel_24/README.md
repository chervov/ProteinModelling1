# JAK2 — 24-variant panel: predictors, databases, AlphaGenome AVI, and JH2–JH1 interface mapping

Two groups as supplied: 14 previously reported GOF variants, 10 identified in the current study.
Master table: [`JAK2_24_variants_full.csv`](JAK2_24_variants_full.csv) — 82 columns, section headers
and a blank row separating the groups.

## Three corrections made while building this

1. **`R755S` cannot exist.** Position 755 of O60674 / NP_004963.1 (the two are byte-identical, 1132 aa)
   is **Ser**, context `GTTLWEICSGGDKPL-S755-ALDSQRKLQ`; the nearest Arg are 761 and 769.
   The variant is **S755R**, a transposition — confirmed by ClinVar `NM_004972.4:c.2265T>A (p.Ser755Arg)`
   and by Marty et al., *Blood* 2014;123:1372–83 (PMID 24398328), which reports **S755R in cis with
   R938Q** in a hereditary-thrombocytosis family and **R867Q** in a second family. R938Q and R867Q are both
   in this list, so the list draws on that paper. An earlier guess of R683S was wrong and is retracted.
2. **R1063H is labelled a prior GOF but ClinVar calls it Benign/Likely benign**, with 8,630 gnomAD alleles
   and 46 homozygotes. Worth re-checking against the source.
3. **V617F's gnomAD AF of 2.93e-4 with 17 homozygotes** is somatic clonal haematopoiesis leaking into
   gnomAD, not germline tolerance.

## AlphaGenome Variant Impact (AVI)

Scored with the GDM `alphagenome-variant-impact-score` skill against GRCh38. Coordinates were taken from
dbNSFP `hg38`, and hg19≡hg38 was **verified per variant** for JAK2 rather than assumed. Where a protein
change is reachable by more than one SNV (E846D, S755R) the ClinVar-matching codon change was used.
Raw tool output: [`alphagenome_avi_raw_output.md`](alphagenome_avi_raw_output.md).

Phred = −10·log10(quantile); Phred 20 ≈ top 1% of all genome-wide SNVs.

| Variant | Group | GRCh38 | HGVS c. | AVI Phred | Percentile | Top modality | Predictors | Interface |
|---|---|---|---|---|---|---|---|---|
| **T108A** | prior GOF | `chr9:5029878:A>G` | c.322A>G | **14.34** | Top 3.68% | PhastCons 470 | 1/20 (5%) | 0/6 |
| **Y317H** | prior GOF | `chr9:5055681:T>C` | c.949T>C | **22.58** | Top 0.55% | Cactus | 13/19 (68%) | 0/6 |
| **H345L** | prior GOF | `chr9:5055766:A>T` | c.1034A>T | **21.08** | Top 0.78% | Cactus | 2/9 (22%) | 0/6 |
| **H608N** | prior GOF | `chr9:5073743:C>A` | c.1822C>A | **23.74** | Top 0.42% | Cactus | 7/9 (78%) | 0/6 |
| **L611S** | prior GOF | `chr9:5073753:T>C` | c.1832T>C | **25.45** | Top 0.28% | AlphaMissense | 9/9 (100%) | 3/6 |
| **V617I** | prior GOF | `chr9:5073770:G>A` | c.1849G>A | **23.01** | Top 0.50% | Cactus | 14/20 (70%) | 0/6 |
| **V617F** | prior GOF | `chr9:5073770:G>T` | c.1849G>T | **24.19** | Top 0.38% | Cactus | 16/19 (84%) | 0/6 |
| **V625F** | prior GOF | `chr9:5077461:G>T` | c.1873G>T | **44.61** | Top 0.003463% | Splicing | 19/20 (95%) | 0/6 |
| **E846D** | prior GOF | `chr9:5081828:G>C` | c.2538G>C | **20.88** | Top 0.82% | AlphaMissense | 10/18 (56%) | 0/6 |
| **R867Q** | prior GOF | `chr9:5089702:G>A` | c.2600G>A | **23.98** | Top 0.40% | Cactus | 17/21 (81%) | 3/6 |
| **T875N** | prior GOF | `chr9:5089726:C>A` | c.2624C>A | **28.8** | Top 0.13% | AlphaMissense | 19/21 (90%) | 4/6 |
| **S755R** | prior GOF | `chr9:5080362:T>A` | c.2265T>A | **22.76** | Top 0.53% | AlphaMissense | 8/19 (42%) | 0/6 |
| **R938Q** | prior GOF | `chr9:5090497:G>A` | c.2813G>A | **26.29** | Top 0.23% | AlphaMissense | 19/21 (90%) | 0/6 |
| **R1063H** | prior GOF | `chr9:5126343:G>A` | c.3188G>A | **22.38** | Top 0.58% | Cactus | 6/20 (30%) | 0/6 |
| **P37A** | this study | `chr9:5022096:C>G` | c.109C>G | **15.38** | Top 2.90% | PhastCons 470 | 3/20 (15%) | 0/6 |
| **F240V** | this study | `chr9:5054666:T>G` | c.718T>G | **25.83** | Top 0.26% | AlphaMissense | 5/9 (56%) | 0/6 |
| **H380Y** | this study | `chr9:5064964:C>T` | c.1138C>T | **23.44** | Top 0.45% | Cactus | 17/20 (85%) | 0/6 |
| **R426X** | this study | `chr9:5066739:C>T` | c.1276C>T | **46.82** | Top 0.00208% | Protein Termination | 2/2 (100%) | 0/6 |
| **C427R** | this study | `chr9:5066742:T>C` | c.1279T>C | **23.08** | Top 0.49% | Cactus | 8/20 (40%) | 0/6 |
| **G571R** | this study | `chr9:5072561:G>C` | c.1711G>C | **23.6** | Top 0.44% | Cactus | 17/20 (85%) | 0/6 |
| **V578I** | this study | `chr9:5072582:G>A` | c.1732G>A | **23.43** | Top 0.45% | Cactus | 17/20 (85%) | 0/6 |
| **L805I** | this study | `chr9:5080662:C>A` | c.2413C>A | **23.02** | Top 0.50% | Cactus | 12/20 (60%) | 0/6 |
| **I1065T** | this study | `chr9:5126349:T>C` | c.3194T>C | **24.36** | Top 0.37% | Cactus | 18/21 (86%) | 0/6 |
| **V1110E** | this study | `chr9:5126721:T>A` | c.3329T>A | **22.67** | Top 0.54% | Cactus | 8/20 (40%) | 0/6 |

### Two variants separate sharply from the rest

- **V625F — Phred 44.61, top 0.0035%, driven by Splicing.** chr9:5077461 is the **10th base of exon 15**
  (exon 15 = 5077452–5077580), inside the acceptor-proximal window. AlphaGenome attributes the impact to
  splicing rather than to the amino-acid change. No other missense variant in the panel behaves this way.
  This is a testable, previously unflagged mechanism for V625F and does not come from any of the 21
  protein-level predictors.
- **R426X — Phred 46.82, top 0.0021%, Protein Termination.** Correct and expected: a stop-gain at residue
  426 of 1132 removes both kinase domains. The 21-predictor panel cannot score it (2/21).

### What carries the signal elsewhere

For the remaining 22, the top modality is **Cactus (deep conservation)** or **AlphaMissense** in every case,
with regulatory tracks (DNASE, ATAC, ChIP, CAGE) contributing <0.02. That is expected for coding variants and
means **AVI adds little beyond AlphaMissense plus conservation for this panel** — its value here was finding
the one variant whose mechanism is not protein-level at all. AlphaGenome would add more on non-coding JAK2
variants (promoter, enhancer, deep intronic), none of which are in this list.

### AVI does not rank the known drivers highest

V617F sits at Phred 24.19 — below T875N (28.80), R938Q (26.29), F240V (25.83) and L611S (25.45). The two
lowest are T108A (14.34) and P37A (15.38), both FERM-domain and both low on every other measure too. As with
the 21-predictor count, **AVI is a damage detector and does not see gain of function**; it should be read
alongside the interface columns, not instead of them.

## JH2–JH1 interface mapping

Each variant was mapped onto TYK2 and JAK1 by global BLOSUM62 alignment (42.4% and 46.6% identity;
validated on V617→V678/V658, F595→Y656/F636, Y1008→Y1055/Y1035) and tested against **six** independent
interface definitions: the 4OLI TYK2 crystal, the Shan JAK2 and JAK1 models (`Shan2014JAK1JAK2/`, native
numbering, 99.7% sequence match), the Jeanpierre closed and open JAK1 models, AlphaFold JAK2, and our own
JAK2 closed model.

| At the interface in | Variants |
|---|---|
| 4 of 6 models | **T875N** |
| 3 of 6 models | **L611S**, **R867Q** |
| 0 of 6 models | all 21 others, including V617F, V617I, V625F, S755R, R938Q and **every Group 2 variant** |

**No variant touches the open-state interface.** Closest Group 2 approaches: G571R 1 residue away, V578I 2.

### A caveat about AlphaFold that matters beyond this table

Expressed in JAK2 numbering, the crystal and all three physics/homology models agree on the JH2–JH1 contact
surface (overlaps 17–27 residues, Jaccard 0.31–0.67). **AlphaFold JAK2 shares only 4–5 residues with each of
them** (Jaccard 0.06–0.07), placing JH2–JH1 on a different surface entirely (JH2 549–556/631–640/708–714 versus
602–607/666–687). For the JAK2 inter-domain arrangement the AlphaFold model should **not** be used as the
closed state; the Shan JAK2 model should, being native-numbered, 4OLI-consistent and carrying 42 contacts.

## Is there an AVI threshold for pathogenicity? No — and here is why it matters

**DeepMind publishes none.** The tool documents only a percentile ladder (Phred >=40/30/20/15/10 =
top 0.01/0.1/1/3.16/10% of all genome-wide SNVs) and uses `--min_phred 15.0` purely as a
candidate-prioritisation filter. The AlphaGenome paper sets no pathogenicity cutoff; its thresholds
concern regulatory effects. A third-party report
([VariantGrid issue 2561](https://github.com/SACGF/variantgrid/issues/2561)) states the authors
advise ranking-based prioritisation rather than hard cutoffs, which matches what the primary
documentation does and does not say.

**We tested whether a threshold works anyway.** Twelve ClinVar-benign JAK2 missense variants with
gnomAD AF > 1e-5 were scored as an in-gene background
([`JAK2_benign_AVI_background.csv`](JAK2_benign_AVI_background.csv)):

| set | n | min | median | max | mean |
|---|---|---|---|---|---|
| ClinVar-benign JAK2 missense | 12 | 15.22 | 21.08 | **24.17** | 20.61 |
| this panel (missense, excl. V625F/R426X) | 22 | 14.34 | 23.25 | 28.80 | 22.92 |

The ranges overlap almost completely. The best cutoff achievable on this data is Phred >= 20.88, at
**76% accuracy while falsely calling 6 of 12 known-benign variants pathogenic**. Benign Y1021F (24.17)
and L383V (24.14) are tied with V617F (24.19); benign R1063H (22.38) outranks nine panel variants.

The reason is structural: the genome-wide SNV distribution is dominated by non-coding positions, so
any missense change in a deeply conserved kinase lands in the top 1% by construction. A genome-wide
percentile cannot discriminate within a pre-selected set of conserved coding variants.

**Use AVI as a rank and a mechanism flag, not a classifier.** The two findings that survive without any
cutoff are the ones where the modality changes: V625F on Splicing and R426X on Protein Termination,
both far above the benign maximum. The `Above_benign_max_24.17` and `Vs_benign_median` columns in
[`JAK2_24_AVI_in_listed_order.csv`](JAK2_24_AVI_in_listed_order.csv) carry this calibration; only 8 of
24 clear the benign ceiling.

### Reading the conservation modalities

`PhastCons 470` (Zoonomia 470-way mammalian alignment) and `Cactus` (241-way) are both evolutionary
conservation, and both are properties of the **position**, not of the substitution - identical for all
three alternate alleles at a site. PhastCons is a two-state phylogenetic HMM giving the posterior
probability that a base lies inside a conserved element, so it borrows strength from neighbouring bases
and is smoothed along the sequence.

PhastCons 470 is the leading attribution for exactly two variants - **T108A (14.34, rank 24/24)** and
**P37A (15.38, rank 23/24)**, the two lowest in the panel. That is diagnostic: when the top modality is
PhastCons, no specific mechanism is driving the score, only weak regional conservation. Both are FERM
domain, both are at the bottom of every independent measure here, and both fall below the benign median
of 21.08. For T108A, listed as a previously reported GOF, this is a third independent line of evidence
pointing the other way.

## Files

| file | contents |
|---|---|
| [`JAK2_24_variants_full.csv`](JAK2_24_variants_full.csv) | master table, 82 columns, section headers + blank separator |
| [`JAK2_24_AVI_in_listed_order.csv`](JAK2_24_AVI_in_listed_order.csv) | compact view in the order supplied, with the benign calibration columns |
| [`JAK2_24_sorted_by_AVI.csv`](JAK2_24_sorted_by_AVI.csv) | same, ranked by AVI Phred descending |
| [`JAK2_benign_AVI_background.csv`](JAK2_benign_AVI_background.csv) | the 12 ClinVar-benign controls used to calibrate |
| [`JAK2_S755R.csv`](JAK2_S755R.csv) | the single corrected variant, full column set |
| [`alphagenome_avi_raw_output.md`](alphagenome_avi_raw_output.md) | raw AVI tool output incl. per-variant feature attributions |

## Provenance

- 18 of 24 variants were already covered by [`../../external_data/JAK2/jak2_variants_inf_predict_ext.csv`](../../external_data/JAK2/jak2_variants_inf_predict_ext.csv)
  (104 columns: ClinVar, gnomAD, cBioPortal, COSMIC, LOVD, DECIPHER, CIViC, DRUG, OMIM).
- 6 (H345L, H608N, L611S, F240V, R426X, S755R) were fetched live from dbNSFP via myvariant.info; none of the
  first five is in ClinVar, L611S and R426X are in COSMIC.
- Predictor thresholds follow the dbNSFP v4.1c README where the authors define one (PrimateAI 0.803,
  PROVEAN −2.5, BayesDel_addAF 0.0692655, LIST-S2 0.85, DEOGEN2 0.5, MutationAssessor 1.935, SIFT 0.05);
  ESM1b −7.5 and MVP 0.7 from their source papers; the rest are conventional midpoints and are marked as such.
- Scripts: `mkcsv.py` (table assembly), `align2.py` (cross-species mapping), `iface2.py` (interface contacts).