# New predictors and ΔΔG benchmarks — what was downloaded, and how useful each is

*Written 27 October 2026. Follow-up to [`../more_data.md`](../more_data.md), which surveyed public
ΔΔG and variant-effect resources. That survey identified ten population-free structural predictors
absent from our matrix, and the ABYSSAL repository was then analysed on request. This folder holds
what could actually be obtained.*

---

## 1. The headline

**Only 3 of the 10 new structural predictors ship precomputed scores. Of those, one covers our
proteins.** The other seven require running the model, which for 22,536 TYK2 variants is a GPU job,
not a download.

| predictor | precomputed available? | covers our proteins? | obtained |
|---|---|---|---|
| **COSMIS** | **yes** — GitHub | **yes, all five** | **✅ `cosmis_jak_src.tsv`** |
| Envision | yes — Shiny app, manual click | unknown | no |
| CPT | yes — GitHub `transfer_proteome` | unknown | no |
| SSEmb | no | — | code only |
| SaProt | no | — | code only |
| ProSST | no | — | code only |
| VenusREM | no | — | code only |
| ProtSSN | no | — | code only |
| S3F | no | — | code only |
| RSALOR | no | — | code only |

Plus the **ABYSSAL** ΔΔG benchmark suite, which is the more valuable find of the two.

---

## 2. COSMIS — obtained, all five proteins

**COntact Set MISsense tolerance.** Per-residue missense constraint computed from the 3D contact
set of each residue against gnomAD variation. Population-free in the AVE sense: no clinical labels.
Code and scores: [github.com/CapraLab/cosmis](https://github.com/CapraLab/cosmis).

Three precomputed files are published (AlphaFold 37.5 MB, PDB 18.2 MB, SWISS-MODEL 25.6 MB).
**Note a trap: our proteins are absent from the AlphaFold file** (7,020 UniProt ids, none of the
JAKs) and present only in the PDB and SWISS-MODEL files. Checking only the largest file would have
produced a false negative — as it did on the first attempt here.

`cosmis_jak_src.tsv` — 2,497 rows merged from the PDB and SWISS-MODEL sets:

| protein | UniProt | positions | residue range | median COSMIS | structure source |
|---|---|--:|---|--:|---|
| JAK1 | P23458 | 460 | 35–563 | −1.083 | PDB |
| JAK2 | O60674 | 471 | 36–514 | +0.188 | PDB |
| JAK3 | P52333 | 593 | 511–1103 | −1.058 | SWISS-MODEL |
| **TYK2** | P29597 | **537** | **579–1177** | −0.699 | PDB |
| SRC | P12931 | 436 | 86–536 | −1.700 | PDB |

Columns: `uniprot_id`, `enst_id`, `uniprot_pos`, `uniprot_aa`, `cosmis`, `cosmis_pvalue`, `cossyn`,
`str_source`. More negative COSMIS = more constrained, i.e. less tolerant of missense variation.

**The TYK2 coverage is well placed for us: residues 579–1177 is exactly the JH2+JH1 span of 4OLI**,
where all our interface, ΔΔG and DMS work sits. All 537 positions overlap our DMS.

### Tested against our data — and it is weak

Spearman, COSMIS per position against per-position means over 19 substitutions, n = 537:

| versus | ρ | p |
|---|--:|--:|
| DMS, IFN-α 1 U/mL | **+0.159** | 2.2 × 10⁻⁴ |
| DMS, IFN-α 100 U/mL | **+0.217** | 3.6 × 10⁻⁷ |
| DMS, abundance | **+0.139** | 1.3 × 10⁻³ |
| AlphaMissense | **−0.259** | 1.2 × 10⁻⁹ |

Signs are as expected (constrained positions → lower DMS scores → positive ρ; constrained →
higher AlphaMissense → negative ρ) and every p-value is significant on 537 positions. But **|ρ| of
0.14–0.26 is weak** — comparable to BLOSUM62's ρ = 0.07–0.15 against the same data and far below
AlphaMissense's ρ ≈ 0.45–0.49.

**Honest verdict: COSMIS adds a genuinely independent signal — population constraint from 3D
contact sets, correlating only −0.26 with AlphaMissense — but a weak one.** Its value is
independence, not strength. Whether weak-and-independent beats strong-and-redundant in combination
is an empirical question we have not tested. Note also that this is a *per-position* score: it
cannot distinguish substitutions at the same position, which is the same dilution problem that made
our position-averaged drug analysis miss V690P.

---

## 3. ABYSSAL — the more useful find

[github.com/ivankovlab/abyssal](https://github.com/ivankovlab/abyssal) — a **ΔΔG predictor trained
on the Tsuboyama ("Mega") dataset using ESM2 embeddings**.

> Pak, M. A., Dovidchenko, N. V., Sharma, S. M., & Ivankov, D. N. (2023). *New mega dataset combined
> with deep neural network makes a progress in predicting impact of mutation on protein stability.*
> [doi:10.1101/2022.12.31.522396](https://doi.org/10.1101/2022.12.31.522396)

Trained model: [zenodo 7886963](https://zenodo.org/record/7886963), `ddg_model_trained_on_mega.pt`,
**206 MB, CC-BY-4.0**. A [Colab notebook](https://colab.research.google.com/github/ivankovlab/abyssal/blob/colab/abyssal_predictor_colab.ipynb)
runs it, **GPU mode required**.

### Why it matters to us

**It is sequence-only.** Input is a `sequence` and a `mutation` column; the model computes ESM2
embeddings and predicts ΔΔG. No structure needed.

That has two consequences, pulling in opposite directions:

- **For**: it will predict ΔΔG for full-length JAK2 and JAK3 — the two proteins with no
  experimental variant data and no reliable structure — with no structure-preparation step and no
  PyRosetta. It is trained on 776k experimental measurements, which is more thermodynamic data than
  any structure-based method has seen.
- **Against**: being sequence-only, **it cannot produce a dual-state ΔΔG by construction.** It has
  no notion of open versus closed. So it cannot test the difference feature — it is a comparator for
  our *per-state* magnitudes only.

### What is actually in this folder

The repository's benchmark sets, which are the part worth having regardless of whether we run the
model. All are experimental ΔΔG with pH and temperature:

| file | rows | what it is |
|---|--:|---|
`holdout.tsv` | 5,321 | **Mega holdout set** — 5 WT constructs, `ddG_ML` plus full sequences |
`S669.tsv` | 669 | Pancotti et al. 2022, 94 PDB entries |
`S669_420.tsv` | 420 | S669 **minus proteins homologous to Mega** |
`S669_411.tsv` | 411 | S669_420 **minus proteins homologous to S2648** |
`S2648.tsv` | 2,648 | Dehouck et al. 2009, 113 PDB entries |
`S2648_2441.tsv` | 2,441 | S2648 minus proteins homologous to Mega |
`Ssym.tsv` | 342 | Pucci et al. 2018 — **forward and reverse mutation pairs** |
`Myoglobin.tsv` | — | Kepp 2015 |
`p53.tsv` | — | Pires et al. 2014 |

**The homology-filtered variants are the point.** `S669_411` is S669 with every protein similar to
*both* the Mega set and S2648 removed, using an all-against-all BLAST the repo ships
(`fasta_blast/`). That is a leakage control we have never applied to any of our ΔΔG evaluation —
our PyRosetta protocol has only ever been scored by rank correlation against a phenotype on the
same protein.

**`Ssym` is the sharpest test available.** It contains each mutation and its reverse, so a correct
ΔΔG predictor must be **antisymmetric**: ΔΔG(A→B) = −ΔΔG(B→A). A predictor that merely detects
"this position is important" scores near zero. Measured here, Ssym's experimental ΔΔG has median
+0.75 and mean +1.018 — not the 0 that perfect pairing would give, so the set is not perfectly
balanced, but it still isolates direction-sensitivity in a way no other set does.

**Running our PyRosetta protocol on Ssym is a half-day job and would tell us something we do not
know**: whether our ΔΔG has any antisymmetry at all, or is really a position-importance score
wearing thermodynamic units. Given the dual-state difference turned out to be noise, this is the
natural next diagnostic.

### Kinase content, for relevance

| set | kinase rows | which |
|---|--:|---|
`S669` | 56 | AMPK β1/β2, RAF, RIPK2, PIM1 |
`S2648_2441` | 44 | adenylate kinase, CDK4 inhibitor C, CDKN2A, CKS1, phosphoglycerate kinase |
`Ssym` | 3 | CDK4 inhibitor C |

**No JAK, no SRC, and no protein-tyrosine kinase domain in any benchmark set.** PIM1 and RAF are
serine/threonine kinases. So these sets calibrate a protocol in general, not on anything close to
our targets — the same limitation as Tsuboyama's SH3-only coverage.

### Caveats

- **No license on the ABYSSAL repository** (the *model* on Zenodo is CC-BY-4.0, the repo declares
  nothing). The datasets are redistributions of published sets from [ProDDG](https://ivankovlab.ru/proddg);
  cite the original papers, not this repo.
- **Small project**: 2 stars, 1 fork, last pushed 2023-09-13. The preprint DOI is a bioRxiv
  preprint; no journal version was checked for.
- GPU required for the Colab path. Under this project's standing rule, GPU work goes on molab, not
  Colab.

### Also worth knowing: ProDDG

[ivankovlab.ru/proddg](https://ivankovlab.ru/proddg) — the same group's **database of ΔΔG datasets
*and* predictors**. It is where all the benchmark sets above come from, and it is a more direct
index for our purposes than the AVE catalogue, which covers pathogenicity predictors rather than
stability ones. Not yet examined.

---

## 4. The seven that need running, ranked by what they would add

None has precomputed scores. If any is worth the compute, these two are:

1. **RSALOR** — [github.com/3BioCompBio/RSALOR](https://github.com/3BioCompBio/RSALOR). "Relative
   Solvent Accessibility × Log-Odds Ratio", **empirical, no machine learning**. It is essentially
   the product of two things we already have for TYK2 — per-residue RSA (`data/orianne/rsa_af3.json`)
   and MSA conservation. Cheapest to run, most interpretable, and the closest thing to a published
   baseline for "structure plus conservation" that our ΔΔG work should be beating.
2. **S3F** — [github.com/DeepGraphLearning/S3F](https://github.com/DeepGraphLearning/S3F).
   Sequence-Structure-**Surface**; adds a surface representation the others lack, which is the
   closest published analogue to our interface-burial analysis.

The remaining five (SSEmb, SaProt, ProSST, VenusREM, ProtSSN) are structure-aware protein language
models. They would likely rank well but are heavy, and being language models they correlate with
ESM1b, which is already in our matrix — less independent than they look.

---

## 5. Recommended order

1. **Run our PyRosetta protocol on `Ssym.tsv`** (342 rows, forward/reverse pairs) and check
   antisymmetry. Cheap, and it tests whether our ΔΔG is thermodynamic or just positional.
2. **Calibrate against `../SRC/src_sh3_experimental_ddG_Tsuboyama2023.csv`** (1,025 measured ΔΔG) —
   see `../more_data.md` §2, and mind the 1,140 unmeasurable variants.
3. **Add COSMIS to the predictor matrix** as an independent-but-weak feature, and test whether it
   adds anything over AlphaMissense in the grouped-by-position CV we already run.
4. **Run ABYSSAL on all four JAKs** (molab GPU). It is the only way to get a data-trained ΔΔG for
   JAK2 and JAK3, and it needs no structures.
5. **Run RSALOR on TYK2** as the honest baseline our structural features should beat.

## 6. Files here

| file | source | size |
|---|---|--:|
`cosmis_jak_src.tsv` | COSMIS PDB + SWISS-MODEL sets, our five proteins | 143 KB |
`holdout.tsv` | ABYSSAL / Mega holdout | 1.1 MB |
`S669.tsv`, `S669_420.tsv`, `S669_411.tsv` | ABYSSAL / Pancotti 2022 | 0.7 MB |
`S2648.tsv`, `S2648_2441.tsv` | ABYSSAL / Dehouck 2009 | 2.0 MB |
`Ssym.tsv` | ABYSSAL / Pucci 2018 | 150 KB |
`Myoglobin.tsv`, `p53.tsv` | ABYSSAL / Kepp 2015, Pires 2014 | 80 KB |

Not committed, too large: the COSMIS full files (`~/cosmis_dl/`, 81 MB), the ABYSSAL trained model
(206 MB, on Zenodo), the Tsuboyama archive (`~/tsuboyama/`, 1 GB).
