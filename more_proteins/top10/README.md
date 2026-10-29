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
scripts/rep10.py    builds the HTML
```

Structure files (`af/`, `st/`, `pae/`, 78 MB) are not committed; `gather.py` refetches them.
Everything else needed to rebuild the reports is in `data/`.
