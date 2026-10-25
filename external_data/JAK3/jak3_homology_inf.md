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

## Interpretation

1. **No direct evidence on Y581C.** It is not in ClinVar, cancer databases or the literature, and has no carriers in gnomAD.
2. **Predictors are split** (AlphaMissense, EVE, ESM1b, REVEL: benign-to-uncertain; SIFT, PolyPhen-2, MetaRNN: damaging). Note that AlphaMissense rates the equivalent His-to-Cys change as more damaging in JAK1 (0.62) and TYK2 (0.40) than in JAK3 (0.10), consistent with JAK3 already deviating from the family consensus here.
3. **The position is functionally important in the family, in both directions:**
   - loss of function: TYK2 His667 is required for signalling (DMS), and the adjacent JAK3 R582W causes SCID;
   - gain of function: JAK1 H647Y and JAK2 K607N are leukaemia-associated JH2 variants, i.e. this loop can relieve JH2 autoinhibition.
4. **Cys is the mildest substitution at the TYK2 equivalent**, and JAK3 natively carries Tyr (not the His that TYK2 needs), so a strong loss-of-function effect is not expected; a subtle regulatory effect (either direction) cannot be excluded.
5. **Suggested test:** JAK3 Y581C in a gamma-chain cytokine reporter (e.g. IL-2/STAT5 in Ba/F3 or HEK293 with IL2RB/IL2RG), with and without cytokine, alongside WT, R582W (loss-of-function control) and A572V or M511I (gain-of-function controls).

Sources: ClinVar, gnomAD v4, cBioPortal, AlphaFold DB (AlphaMissense), dbNSFP via myvariant.info, MaveDB (TYK2 DMS, urn:mavedb:00001270-a-6 / 00001271-a-1), UniProt; [BMC Struct Biol 2009, JAK2 exon 13-15 modelling](https://bmcstructbiol.biomedcentral.com/articles/10.1186/1472-6807-9-58/figures/8); [JH2 mutation review table (PMC7813639)](https://pmc.ncbi.nlm.nih.gov/articles/PMC7813639/table/T1); [JAK3 JH2 ATP binding and oncogenic mutants (PMC6287396)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6287396/).
