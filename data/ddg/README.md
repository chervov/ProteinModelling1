# JAK2 variant ΔΔG — results, method and how to rerun

**Protein: JAK2 only — UniProt O60674, 1,132 aa.** Not JAK1/JAK3/TYK2. Every position below was
verified against the canonical O60674 sequence before any number was computed.

Compiled 29 October 2026.

## Files

| file | contents |
|---|---|
| `jak2_variants_ddg.csv` | the 25 input lines → ΔΔG, percentile, interpretation flags |
| `compute_jak2_ddg.py` | reproduces the table from scratch for any JAK2 variant list |
| `jak2_ddg.png` | three-panel figure |

Rerun for a different list:

```bash
python compute_jak2_ddg.py --variants "V617F,S755R,R867Q"
python compute_jak2_ddg.py --variants-file my_variants.txt --out out.csv
```

## Two input lines could not be given a ΔΔG, and were not guessed

**`R426X` — nonsense.** A stop codon has no folded mutant state, so ΔΔG is undefined. Reported as
undefined rather than approximated. (Its functional consequence is presumably loss of everything
C-terminal to residue 426, i.e. both kinase domains — a truncation question, not a stability one.)

**`R755S` — wild-type mismatch.** Position 755 in O60674 is **S**, not R. The nearest arginines are
761 and 769, and UniProt lists no JAK2 isoform that would shift the numbering. PubMed has **0 hits**
for `JAK2 "R755S"` and **1** for `JAK2 "S755R"` — PMID 24398328, *Germ-line JAK2 mutations in the
kinase domain are responsible for hereditary thrombocytosis*, which also reports **R867Q** from the
same list. The input is therefore almost certainly a wt/mut transposition. **Both forms appear in
the table**: `R755S` flagged as a mismatch with no value, and `S755R` computed. Decide which you meant.

## Method

ΔΔG came from two independent precomputed saturation-mutagenesis tables, not from new inference —
both already cover the **complete 1,132 × 19 = 21,508** JAK2 substitution set:

| source | method | file |
|---|---|---|
| ThermoMPNN | graph network on an AlphaFold2 model | `external_data/thermompnn_jak_src.csv` (21,508 JAK2 rows) |
| ProtVar (EBI) | FoldX v5.0 on AlphaFold2 models | `external_data/protvar_foldx_jak_src.csv` (20,349 JAK2 rows) |

**Sign convention: positive = destabilising** in both, verified empirically rather than assumed.

`P37A` has no FoldX value — ProtVar omits some low-confidence positions despite its README claiming
a pLDDT > 70 filter is the only exclusion. Its pLDDT is 57.6, the lowest in this set.

## How to read these numbers — the floors matter more than the values

- **±0.5 kcal/mol** is the experimental noise floor for ΔΔG measurements.
- **±0.69 kcal/mol** is ThermoMPNN's own antisymmetry bias, measured on Ssym in this project:
  mean δ = ΔΔG(A→B) + ΔΔG(B→A) = +0.69 where thermodynamics requires 0. Below this, the **sign** of
  a prediction is not meaningful.
- Accuracy ceiling: on 386 held-out human measurements ThermoMPNN reached r = +0.517 and FoldX
  +0.388 (see `external_data/ddg_benchmark_local.md`). These are weak predictors by construction.

**61% of the 23 computed variants fall inside the 0.5 kcal/mol floor; 65% inside the antisymmetry
bias.** Most of this list is, individually, not interpretable from ΔΔG.

## The headline result

Measured against **JAK2's own distribution** — the only meaningful reference, since "1.4 kcal/mol"
means nothing without knowing what an average JAK2 variant does:

| | ΔΔG (kcal/mol) |
|---|--:|
| all 21,508 JAK2 substitutions, median | **0.74** |
| these 23 variants, median | **0.34** |
| these 23 variants, median percentile | **33rd** |

**This variant set is *less* destabilising than a typical JAK2 missense variant.** V617F — the
canonical MPN driver — sits at the **37th percentile** (+0.43 ThermoMPNN, +0.64 FoldX), below
JAK2's median. GOF-reported and this-study variants are indistinguishable (medians 0.39 vs 0.21,
Mann–Whitney p = 0.59).

**That is the expected signature of gain-of-function, and it is a result rather than a failure.**
Activating mutations work by *releasing autoinhibition* — for JAK2, by disrupting the JH2
pseudokinase domain's restraint of JH1 — not by unfolding the protein. The published position is
consistent: dominant-negative and gain-of-function variants are far milder than loss-of-function and
close to benign in |ΔΔG| ([10.1038/s41467-022-31686-6](https://doi.org/10.1038/s41467-022-31686-6)),
and ΔΔG is a weak pathogenicity classifier overall (best AUC ≈ 0.66,
[10.1038/s41598-020-72404-w](https://doi.org/10.1038/s41598-020-72404-w)).

**So: do not use these ΔΔG values to rank these variants for pathogenicity.** They answer "does this
mutation destabilise the fold?", and for most of this list the answer is no.

## What does stand out

Four variants clear both floors and both methods agree they are destabilising:

| variant | group | domain | ThermoMPNN | FoldX | percentile |
|---|---|---|--:|--:|--:|
| **I1065T** | this study | Protein kinase 2 (JH1) | 2.32 | 3.15 | 88th |
| **Y317H** | reported GOF | FERM | 1.68 | 2.61 | 77th |
| **V625F** | reported GOF | Protein kinase 1 (JH2) | 1.42 | 5.33 | 71st |
| **G571R** | this study | Protein kinase 1 (JH2) | 1.15 | 2.44 | 63rd |

`E846D` reaches 1.39 on ThermoMPNN but **−0.76** on FoldX — the methods disagree on sign, so it
should not be called either way. It also sits in the JH2–JH1 linker, outside any annotated domain.

## Caveats

1. Both tables are built on **AlphaFold2 monomer models** of JAK2. No full-length experimental JAK2
   structure exists; the closest is the cryo-EM JAK1 dimer (7T6F/8EWY). So these values describe an
   isolated monomer in one modelled conformation, not JAK2 on a receptor.
2. ΔΔG here is **native-state fold stability**, which is not the mechanism for most of this list.
3. Inter-domain interface positions are extrapolation: no published benchmark measures ΔΔG accuracy
   as a function of domain count or interface location — see `external_data/ddg_literature.md`.
4. The two methods correlate at only r = +0.67 across these 23 variants, and at +0.58 across 386
   held-out human measurements. Where they disagree, neither is authoritative.
