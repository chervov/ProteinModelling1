# JAK3 Y581C: equivalent positions in JAK1, JAK2 and TYK2

Alignment as in [`jak2_priority_variants_paralogs.md`](../jak2_priority_variants_paralogs.md) (BLOSUM62 global alignment; map in [`jak_alignment_position_map.csv`](../jak_alignment_position_map.csv)). Data retrieved 24-25 Oct 2026.

## Alignment

```
JAK3  EAASLMSQVSYRHLVLLHGVC   (Y581 = centre)
JAK2  EAASMMSKLSHKHLVLNYGVC   (H606)
JAK1  EAASMMRQVSHKHIVYLYGVC   (H647)
TYK2  ETASLMSQVSHTHLAFVHGVC   (H667)
```

JAK3 is the only family member with Tyr here; JAK1, JAK2 and TYK2 all have His. The residue sits in the JH2 N-lobe just after the alphaC helix (UniProt JAK2 helix 591-603), in the 604-609 loop that a JAK2 modelling study links to H606 side-chain contacts with L604/L609.

## JAK3 Y581C itself

| Evidence | Value | Reading |
|---|---|---|
| AlphaMissense | 0.10 | likely benign |
| EVE | 0.12 | benign |
| REVEL / CADD | 0.37 / 22.2 | uncertain / tolerated |
| ESM1b | -5.2 | tolerated (threshold -7.5) |
| SIFT / PolyPhen-2 HVAR / MetaRNN | 0.001 / 0.917 / 0.77 | damaging |
| Conservation (phyloP 100 vertebrates) | 4.5 | moderately conserved |
| Position mean AlphaMissense (19 substitutions) | 0.47 | moderately constrained |
| ClinVar / OncoKB / CIViC | - | not reported |
| gnomAD v4 | site seen, allele count 0 | no carriers |
| Tumours (cBioPortal, COSMIC) | none | not reported |
| Other JAK3 variants at 581 | Y581H, Y581S (gnomAD, 1 allele each); Y581* | |
| Nearby JAK3 | **R582W** likely pathogenic (T-B+ SCID, loss of function); Q578* likely pathogenic | adjacent residue is critical for function |

## Equivalent positions

| Gene | Residue | Same substitution (AlphaMissense) | Position mean AlphaMissense | Reported variants and literature |
|---|---|---|---|---|
| JAK2 | H606 | H606C (0.16) | 0.47 | H606Q: ClinVar uncertain, gnomAD 112 alleles, 2 tumours; modelled to disrupt the 604-609 loop. Neighbour **K607N** is an activating JAK2 variant reported in AML (UniProt natural variant) |
| JAK1 | H647 | H647C (0.62) | 0.89 | **H647Y** - JAK1 His mutated to JAK3's Tyr - is listed among JH2 mutations associated with acute leukaemias, next to A634D, V658F and R724H (review table, PMC7813639) |
| TYK2 | H667 | H667C (0.40) | 0.75 | **Deep mutational scan:** every substitution lowers IFN-alpha signalling (-1.74 to -0.13; position among the ~10% least tolerant in TYK2, rank 118/1187). H667C is the mildest (-0.13 +- 0.28, not different from WT); most changes also lower abundance (H667C -0.21) |

## Predictor scores for the homologous variants

### Same substitution (to Cys) at each equivalent residue

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK3 | Y581C | 0.10 (LB) | 0.37 | 22.2 | 0.001 | 0.917 | 0.77 | -5.2 | 0.12 | - |
| JAK2 | H606C | 0.16 (LB) | - | - | - | - | - | - | - | - |
| JAK1 | H647C | 0.62 (LP) | - | - | - | - | - | - | - | - |
| TYK2 | H667C | 0.40 (amb) | - | - | - | - | - | - | - | -0.13 +- 0.28 |

dbNSFP scores (REVEL, CADD, SIFT, PolyPhen-2, MetaRNN, ESM1b, EVE) exist only for changes reachable by one DNA letter; His to Cys needs two, so only AlphaMissense (all 19 substitutions) and the TYK2 deep mutational scan cover them. AlphaMissense classes: LP likely pathogenic (> 0.564), amb ambiguous, LB likely benign (< 0.34).

### Variants reported at the equivalent positions (ClinVar, gnomAD, cBioPortal, literature)

| Gene | Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | TYK2 DMS signalling |
|---|---|---|---|---|---|---|---|---|---|---|
| JAK3 | Y581H | 0.08 (LB) | 0.10 | 6.6 | 1.000 | 0.008 | 0.05 | -0.6 | 0.03 | - |
| JAK3 | Y581S | 0.16 (LB) | 0.31 | 23.2 | 0.001 | 0.617 | 0.70 | -5.6 | 0.10 | - |
| JAK2 | H606Q | 0.49 (amb) | 0.34 | 26.9 | 0.001 | 0.541 | 0.94 | -7.2 | 0.72 | - |
| JAK2 | H606D | 0.46 (amb) | 0.37 | 27.4 | 0.002 | 0.541 | 0.95 | -7.0 | 0.54 | - |
| JAK2 | H606L | 0.35 (amb) | 0.59 | 24.1 | 0.001 | 0.160 | 0.95 | -10.9 | 0.76 | - |
| JAK2 | H606Y | 0.08 (LB) | 0.24 | 18.7 | 0.291 | 0.003 | 0.72 | -5.6 | 0.18 | - |
| JAK1 | H647Y | 0.52 (amb) | 0.51 | 25.5 | 0.059 | 0.996 | 0.92 | -6.5 | - | - |
| JAK1 | H647N | 0.68 (LP) | 0.47 | 29.8 | 0.001 | 0.995 | 0.98 | -6.4 | - | - |
| JAK1 | H647P | 0.88 (LP) | 0.68 | 27.9 | 0.001 | 0.999 | 0.98 | -10.9 | - | - |
| TYK2 | H667Q | 0.85 (LP) | 0.47 | 23.8 | 0.001 | 0.996 | 0.97 | -6.3 | - | -0.36 +- 0.26 |
| TYK2 | H667N | 0.37 (amb) | 0.70 | 28.5 | 0.002 | 0.994 | 0.98 | -9.7 | - | -0.31 +- 0.21 |
| TYK2 | H667Y | 0.25 (LB) | 0.70 | 25.0 | 0.067 | 0.997 | 0.97 | -5.6 | - | -1.44 +- 0.24 |

Thresholds (damaging): AlphaMissense > 0.564, REVEL >= 0.644, CADD >= 25, SIFT <= 0.05, PolyPhen-2 > 0.909, MetaRNN > 0.5, ESM1b < -7.5, EVE > 0.5; TYK2 DMS negative = loss of signalling. See [`scores_interpretation.md`](../scores_interpretation.md).

**What the table shows**

- **His to Tyr (JAK3's native residue) at the paralog positions:** JAK2 H606Y and TYK2 H667Y are called *likely benign* by AlphaMissense, yet **TYK2 H667Y is a strong loss of function in the deep mutational scan (-1.44 +- 0.24)**; JAK1 H647Y (ambiguous, 0.52) is reported in acute leukaemia. Predictors therefore miss the measured effects at this position in both directions.
- **The scan and the predictors disagree for TYK2 in general:** H667Q is LP by AlphaMissense and mildly reduced in the scan (-0.36), H667N is ambiguous by AlphaMissense and similarly reduced (-0.31).
- **JAK3 Y581C is predicted mild by AlphaMissense, EVE and ESM1b** but damaging by SIFT, PolyPhen-2 and MetaRNN; the most conservative-looking change at this site (Y581H, back to the family consensus) is predicted benign by all tools.
- **AlphaMissense scores the His to Cys change higher in JAK1 (0.62) and TYK2 (0.40) than in JAK3 (0.10),** in line with JAK3 already deviating from the family consensus here.
## Interpretation

1. **No direct evidence on Y581C.** It is not in ClinVar, cancer databases or the literature, and has no carriers in gnomAD.
2. **Predictors are split** (AlphaMissense, EVE, ESM1b, REVEL: benign-to-uncertain; SIFT, PolyPhen-2, MetaRNN: damaging). Note that AlphaMissense rates the equivalent His-to-Cys change as more damaging in JAK1 (0.62) and TYK2 (0.40) than in JAK3 (0.10), consistent with JAK3 already deviating from the family consensus here.
3. **The position is functionally important in the family, in both directions:**
   - loss of function: TYK2 His667 is required for signalling (DMS), and the adjacent JAK3 R582W causes SCID;
   - gain of function: JAK1 H647Y and JAK2 K607N are leukaemia-associated JH2 variants, i.e. this loop can relieve JH2 autoinhibition.
4. **Cys is the mildest substitution at the TYK2 equivalent**, and JAK3 natively carries Tyr (not the His that TYK2 needs), so a strong loss-of-function effect is not expected; a subtle regulatory effect (either direction) cannot be excluded.
5. **Suggested test:** JAK3 Y581C in a gamma-chain cytokine reporter (e.g. IL-2/STAT5 in Ba/F3 or HEK293 with IL2RB/IL2RG), with and without cytokine, alongside WT, R582W (loss-of-function control) and A572V or M511I (gain-of-function controls).

Sources: ClinVar, gnomAD v4, cBioPortal, AlphaFold DB (AlphaMissense), dbNSFP via myvariant.info, MaveDB (TYK2 DMS, urn:mavedb:00001270-a-6 / 00001271-a-1), UniProt; [BMC Struct Biol 2009, JAK2 exon 13-15 modelling](https://bmcstructbiol.biomedcentral.com/articles/10.1186/1472-6807-9-58/figures/8); [JH2 mutation review table (PMC7813639)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7813639/table/T1); [JAK3 JH2 ATP binding and oncogenic mutants (PMC6287396)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6287396/).
