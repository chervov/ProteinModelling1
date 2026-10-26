# Report pack — JAK family conformational modelling and variant effects

*Updated 26 October 2026. Each file is the current version from the repository root; this folder is
a snapshot for reading and presenting.*

---

## Read in this order

| # | document | what it says |
|---|---|---|
| 1 | [`new_methods_summary20261023.md`](new_methods_summary20261023.md) | **the methods contribution** — two new controls (template, MSA depth) and what they unlock. Section 1 is one slide. |
| 2 | [`new_methods_mutations20261023.md`](new_methods_mutations20261023.md) | **mutation effects** found with those controls. Section 1 is one slide. |
| 3 | [`interface_effect.md`](interface_effect.md) | **the TYK2 JH2–JH1 interface effect** — abundance destroyed, signalling intact |
| 4 | [`conclusions_ddG_difference_feature.md`](conclusions_ddG_difference_feature.md) | **the ΔΔG negative** — the published pipeline's key feature does not work |
| 5 | [`predictor_correlation_matrix.md`](predictor_correlation_matrix.md) | **twelve features all-vs-all** — the predictors are one feature |
| 6 | [`dms_basic_statistics.md`](dms_basic_statistics.md) | the DMS dataset characterised: 11 arms, quality, batch structure |
| 7 | [`binding_sites_analysis.md`](binding_sites_analysis.md) | drug-response positions from the inhibitor arms |
| 8 | [`ddg_by_target_aa.md`](ddg_by_target_aa.md) | ΔΔG by substituted-in residue; the P/W/Y/F group |

---

## The five findings

**1. The closed form of TYK2 is unreachable without a template.** 0 of 89 template-free runs; 24 of
24 with the closed 4OLI template. The drug-target conformation is invisible to the standard method.

**2. MSA depth is a conformational dial with a sharp switch.** TYK2 goes from 8% open at 64
sequences to 96% at 96. States live in narrow windows — JAK1's active-dimer exists at 64 and is
gone by 128.

**3. Three mutations move the structure, in both directions.** V678F opens TYK2 (75% vs 8%,
Holm p = 0.0001), V678A opens it (62%), **P982A closes it** (54% vs 96%, Holm p = 0.034). JAK2
V617F — the textbook driver — loses the compact state entirely (0/16 vs 9/16, Holm p = 0.007).

**4. The published pipeline's distinctive feature does not work.** ΔΔG_open − ΔΔG_closed:
**AUC 0.499** against measured phenotype at n = 22,536, **0.495** against the paper's own cluster
labels, **+0.00 to +0.03** against every sequence predictor. A null control on two *identical*
structures behaves the same, which identifies the cause: the two states correlate at 0.82, so the
subtraction leaves repack residual. Single-state ΔΔG does work (AUC 0.733) but adds nothing over
AlphaMissense (ΔAUC ≤ 0.003).

**5. The TYK2 JH2–JH1 interface dissociates abundance from function.** 69% of interface variants
fall in the bottom abundance quartile (vs 38%) yet only 4.9% are loss-of-function (vs 15.3%). At
matched low abundance they signal at −0.071 against −0.792 for controls, p = 1e−44.

---

## What is not established

- **The mechanism of finding 5.** The conformational explanation predicted a shift in
  allosteric-inhibitor sensitivity. The test is **inconclusive**: two replicates of the same drug
  give p = 0.63 and p = 6.8e−05, and the effect (~0.08) sits below the assay's noise floor (~0.30).
  See `interface_effect.md` §10.
- **JAK2 and JAK3 conformations.** AlphaFold 2 and AlphaFold 3 both disagree with our pipeline —
  AF says JAK2 is open and JAK3 closed; our runs give the reverse. Neither side is validated.
  See `new_methods_summary20261023.md` §4.
- **The candidate new JAK3 form.** Unmatched against a five-structure reference panel at moderate
  MSA depth. A candidate, not a discovery.
- **Any effect measured on `ifn_1U`.** That arm has separation 0.56 and SD/SE = 1.06 — biological
  spread barely exceeds measurement error. Gain-of-function analysis rests on it.

---

## Corrections made during the work

Recorded because each changed a stated conclusion:

| what was claimed | what is true |
|---|---|
| templates force the closed state (59/59) | only *specified closed* templates do; AF3 opens JAK2 with and without templates — the **model**, not the template, is the variable |
| ΔΔG_closed predicts no measured phenotype | it reaches **AUC 0.733** at 100 U/mL; the pilot used an unrepresentative interface-only subset at the weaker dose |
| ΔΔG_closed is "the most valuable non-redundant feature" | it adds **≤0.003 AUC** over AlphaMissense against experimental data |
| the allosteric-drug test is a clean negative | **inconclusive** — the baselines were cross-batch, and the effect is below the noise floor |
| the predictor matrix (curated set) | **biased benign**; redone genome-wide, phenotype correlations are 0.06–0.08 higher |
| 65.3% clustering agreement with the paper | **below** the 65.5% majority-class baseline |

---

## Data and reproducibility

| | |
|---|---|
| TYK2 DMS, all 11 arms | `TYK2/DMS_Howard2026/` (Howard et al., *eLife* 2026) |
| ΔΔG, both proteins, 100% coverage | `data/ddg/` — 44,462 variants, TYK2 and JAK1 |
| genome-wide predictors incl. CADD, MetaRNN | `external_data/TYK2/tyk2_dbnsfp_genomewide.csv` — 7,195 variants |
| structures | `TYK2/af3/`, `JAK2/af3_*`, `JAK3/af3_notemplate/`, `AFDB/` |
| pipelines | `pipeline/ddg/`, `pipeline/dbnsfp/` |

The ΔΔG protocol is verified against PyRosetta's own published tutorial to four decimal places.
The published pipeline we reproduce is **not** reproducible as printed: its methods give only
*"estimated with PyRosetta 4"*, and its clustering script
([BioModels MODEL2507020001](https://www.ebi.ac.uk/biomodels/MODEL2507020001)) was never released.
Our reproduction is therefore an independent reimplementation, which matched their published
cluster medians to within 0.4 kcal/mol.
