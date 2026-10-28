# PTPN2 haploinsufficiency (Jeanpierre et al. 2024) — what can be said about the six variants

*Written 28 October 2026. Analysis of the variants in Jeanpierre, Cognard, Tusseau, Riller, …,
Rieux-Laucat, Belot & Mathieu, "Haploinsufficiency in PTPN2 leads to early-onset systemic
autoimmunity from Evans syndrome to lupus", **J Exp Med 2024, 221(9):e20232337**, PMID
[39028869](https://pubmed.ncbi.nlm.nih.gov/39028869/), PMCID PMC11259789. Variants and functional
results read from the Europe PMC full text; ΔΔG and predictor values computed here from
`external_data/` resources.*

**Same first author as the JAK1 conformational paper this project reproduces, same lab (Institut
Imagine / Rieux-Laucat), and PTPN2 is a direct negative regulator of JAK1 and JAK3.**

---

## 0. The headline

**The six variants do not share one mechanism, and the two missense variants are mechanistic
opposites.** Both ΔΔG methods agree, and they disagree with AlphaMissense in exactly the informative
way:

| variant | FoldX ΔΔG | ThermoMPNN ΔΔG | buried? | AlphaMissense | mechanism implied |
|---|--:|--:|---|--:|---|
| **Y126N** | **+4.59** (87th pct) | **+2.27** (90th pct) | **RASA 0** | 0.997 | **destabilisation → loss of protein** |
| **C216S** | +0.71 (43rd pct) | **−1.32** (**0th pct**) | RASA 0.03 | 0.999 | **catalytic ablation of a stable protein** |

**C216S is the single least destabilising substitution in the entire PTPN2 protein by ThermoMPNN**
(ΔΔG −1.32, i.e. mildly stabilising) — while AlphaMissense calls it 0.9987 pathogenic. That
maximal disagreement is the signal: the protein folds perfectly and does nothing, because **C216 is
the catalytic cysteine** (UniProt P17706, Active site 216, "Phosphocysteine intermediate").

So "haploinsufficiency" — reduced functional dosage — is the right label for most of the series but
**not for C216S**, which produces a full complement of stable, catalytically dead protein. The
distinction matters for therapy: a dosage problem and a dead-enzyme problem respond differently to
anything that raises expression.

---

## 1. The six variants

Six heterozygous germline variants in six families; all absent from gnomAD.

| family | patient | cDNA | protein | type | position vs domain | inheritance |
|---|---|---|---|---|---|---|
| A | A1 + **A2 (father, asymptomatic)** | c.1209delT | **p.Phe403Leufs\*25** | frameshift | C-terminal tail, **TC48 only** | paternal |
| B | B1 | c.293G>A | **p.Trp98\*** | nonsense | inside PTP domain | **paternal, asymptomatic** |
| C | C1 | c.866G>A | **p.Trp289Ter** | nonsense | **just past** PTP domain | unknown |
| D | D1 | c.70-2A>T | **p.Glu24Metfs\*20** | splice → frameshift | very N-terminal | likely **de novo** |
| E | E1 | c.376T>A | **p.Tyr126Asn** | **missense** | PTP domain, **fully buried** | unknown |
| F | F1 | c.647G>C | **p.Cys216Ser** | **missense** | **catalytic cysteine** | **paternal, asymptomatic** |

Phenotypes: lupus with renal, cutaneous, haematological and hepatic involvement (A1); Evans
syndrome (B1, C1, F1); ITP (D1); common variable immune deficiency (E1); autoimmune neutropenia and
Hashimoto thyroiditis.

**Three of six were inherited from an asymptomatic father** (A1, B1, F1) — autosomal dominant with
incomplete penetrance, which the paper states.

### Domain boundary note

The paper says "except for patient A1 (F403Lfs\*25), all mutations were located in the catalytic
domain". **UniProt annotates the phosphatase domain as 5–275**, which places **W289 outside it.** The
discrepancy is a boundary convention (PTP domains are often drawn to ~300), but it matters for
W289\* specifically — see §2.3.

---

## 2. Four mechanisms, not one

### 2.1 Y126N — destabilisation, i.e. real haploinsufficiency

| | |
|---|---|
| FoldX ΔΔG | **+4.59 kcal/mol**, 87th percentile of all 7,163 PTPN2 variants |
| ThermoMPNN ΔΔG | **+2.27 kcal/mol**, 90th percentile |
| ESM-1v | −14.34, 82nd percentile most-damaging |
| AlphaMissense | 0.9968, pathogenic |
| relative solvent accessibility | **0.00 — completely buried** |
| pLDDT | 98.21 |

Two independent ΔΔG methods, one physics-based (FoldX on AlphaFold) and one trained on experimental
ΔG (ThermoMPNN), both put this in the top ~10% most destabilising substitutions in the protein. A
buried tyrosine replaced by asparagine — losing an aromatic ring and introducing a polar amide in a
closed packing environment — is the canonical destabilising substitution.

**This is the variant for which "haploinsufficiency" is literally correct:** the allele produces
less folded protein. The paper notes Y126 is conserved across PTPN2 orthologs, which is consistent.

### 2.2 C216S — catalytic ablation, not haploinsufficiency

| | |
|---|---|
| FoldX ΔΔG | +0.71 kcal/mol, 43rd percentile — **unremarkable** |
| ThermoMPNN ΔΔG | **−1.32 kcal/mol, 0th percentile — the least destabilising substitution in the protein** |
| ESM-1v | −10.37, 58th percentile |
| AlphaMissense | **0.9987, pathogenic** |
| RASA / pLDDT | 0.03 / 98.1 |

**C216 is the catalytic nucleophile.** Cys→Ser is near-isosteric — serine is the same size with
oxygen for sulphur — so it costs essentially nothing structurally while removing the thiolate that
performs the phosphoryl transfer. This is the standard catalytically-dead PTP mutant used throughout
the phosphatase field.

The consequences worth stating:

1. **The allele makes a full amount of stable protein that cannot work.** Functionally that is loss of 50% of activity, as haploinsufficiency would be — but mechanistically it is not reduced dosage, and the mutant protein is still present to occupy substrates and complexes. A dominant-negative contribution cannot be excluded on these data.
2. **It is the cleanest possible illustration of why ΔΔG is a mechanism channel and not a pathogenicity score** (`external_data/ddg_study.md` §0, §6.1). Rank the six variants by ΔΔG and C216S looks benign; rank by AlphaMissense and it is maximally pathogenic. **Neither is wrong — the disagreement is the finding.** A variant with near-zero ΔΔG and near-1.0 AlphaMissense is a functional-site variant by elimination.
3. The paper reports C216S inherited from an **asymptomatic father**, so even complete catalytic ablation of one allele is not sufficient for disease.

A related precedent the paper cites: a previously reported PTPN2 variant substituting **the same cysteine by glycine**, associated with Crohn's disease. Cys→Gly would be both catalytically dead *and* destabilising, so the two are not equivalent.

### 2.3 W289* — the truncated protein is functional; the loss must be NMD

This is the most interesting of the truncations and the paper's own data make the point.

UniProt places the PTP domain at **5–275**, so a stop at **289 leaves the entire catalytic domain
intact** and removes only the C-terminal regulatory tail. And that tail is **autoinhibitory** — the
paper states PTPN2 "exists in an inactive basal state due to the folding of its C-terminal domain"
over the active site, consistent with
[Nat Commun 2021](https://www.nature.com/articles/s41467-021-27633-6), which showed by NMR/SAXS/XL-MS
that the disordered tail autoinhibits by steric bulk and is displaced by the Integrin-α1 tail.

So W289* should produce a **tail-less, constitutively more active phosphatase** — and the paper's
functional data say exactly that: STAT1 phosphorylation "was decreased following expression of PTPN2
WT or W289\* mutants", i.e. **W289\* behaved like wild type**, while F403Lfs\*25, Y126N and C216S
failed to suppress.

**Therefore the disease mechanism for patient C1 cannot be a defective protein.** It has to be
dosage — nonsense-mediated decay of the transcript, so little or no protein is made. The protein
that *would* be made is competent. This is the one variant in the series for which "haploinsufficiency"
is the only available explanation, and it is also the one whose protein product is not loss-of-function.

**Testable:** if NMD is the mechanism, W289* transcript should be reduced in patient cells and
restored by a translation-inhibitor NMD block (cycloheximide or puromycin). I did not find that
experiment in the paper.

### 2.4 F403Lfs*25 — isoform-specific mislocalisation, not loss of catalysis

PTPN2 has two isoforms sharing the catalytic domain and differing in the C-terminal tail:

- **TC48**, 415 aa, canonical, ER-localised — its last **34 hydrophobic residues (≈382–415) mask the nuclear localisation signal** and direct the protein to the ER
- **TC45**, 387 aa, shuttles between nucleus and cytoplasm

**Residue 403 exists only in TC48.** A frameshift at 403 cannot affect TC45 at all, and it falls
squarely inside the hydrophobic NLS-masking segment.

Prediction: normal catalysis, abnormal localisation. The paper's own result: *"we failed to identify
a decreased phosphatase activity for the F403Lfs\*25 variant in vitro, while its activity was reduced
in the luciferase assay and in the Jurkat model"* — catalytically fine, non-functional in cells.
That is a trafficking/compartment defect, and the structural reading explains it.

Two consequences:

1. **Family A's genotype is TC48-selective.** Their TC45 is entirely wild type. If TC45 carries most JAK/STAT regulation — it is the nuclear/cytoplasmic isoform — family A should be the mildest, and indeed the carrier father A2 is asymptomatic while A1 has the most severe phenotype in the series (lupus with renal involvement). That is worth reconciling.
2. It is the only variant in the set that is **not** a dosage or catalytic defect, so grouping it under haploinsufficiency obscures its mechanism.

### 2.5 W98* and E24Mfs*20 — straightforward dosage

W98* truncates inside the catalytic domain (5–275); E24Mfs*20 arises from a canonical splice-acceptor
loss (c.70-2A>T) and terminates 20 codons later. Both destroy the domain and both are early enough
for NMD. These are unambiguous haploinsufficiency. E24Mfs*20 is the likely *de novo* case.

---

## 3. Summary table

| variant | protein made? | folds? | catalytic? | localised? | mechanism |
|---|---|---|---|---|---|
| E24Mfs*20 | no (NMD) | — | — | — | **dosage** |
| W98* | no (NMD) | — | — | — | **dosage** |
| **W289\*** | **reduced (NMD)** | **yes** | **yes — behaves as WT** | yes | **dosage only** |
| **Y126N** | yes | **no — ΔΔG +4.6 / +2.3, buried** | — | — | **destabilisation** |
| **C216S** | **yes, fully stable** | **yes** | **no — nucleophile removed** | yes | **catalytic ablation** |
| **F403Lfs\*25** | yes (**TC48 only**) | yes | **yes — normal in vitro** | **no** | **mislocalisation** |

---

## 4. What this adds, and what it does not

**Adds.** The paper establishes PTPN2 haploinsufficiency as a disease entity and shows all six
variants cause loss of regulatory function — that is not in question. What the computational data
add is that **the route to loss differs per variant**, in ways that are predictable and that the
paper's own functional assays corroborate:

- Y126N is destabilising and C216S is not — and this was predictable before any assay, from two independent ΔΔG methods agreeing
- C216S/AlphaMissense disagreement identifies a functional-site variant with no structural cost
- W289* and F403Lfs*25 are explained by where they fall relative to the catalytic domain and the TC48 tail respectively

**Does not add.** No claim here is a substitute for experiment. Specifically:

- ΔΔG is a weak predictor in general — ρ ≈ 0.26–0.28 against DMS data (`external_data/ddg_study.md` §5). Y126N's result is credible because two methods agree, the residue is fully buried (RASA 0), the model is confident (pLDDT 98) and the substitution type is canonical — not because any single number is reliable.
- **Protein abundance in patient cells was not extracted from the paper here.** If the paper reports western blots per variant, Y126N should show reduced PTPN2 and C216S should not. That is the direct test of this analysis and it should be checked against their Fig. 2 before any of this is relied on.
- No modelling of the C-terminal tail was done. The tail is disordered, so ΔΔG is undefined there and all four truncating/frameshift variants are outside what these resources can score.

---

## 5. Relevance to this project

1. **PTPN2 has one folded domain** (PTP, 5–275 of 415) and therefore **no inter-domain open/closed state** — see `twostate_vs_floppy.md` §4.4. Its regulation is tail-on-domain, which is a different problem from JAK's domain-on-domain arrangement. Modelling its conformations the way we model JAK is not applicable.
2. **The phosphatase that *is* a JAK-like two-state system is SHP2/PTPN11**, and `twostate_vs_floppy.md` §4.4 shows it is missing from the `more_proteins/` screen despite 119 SWISS-MODEL structures — along with SHP1/PTPN6, which was screened and recorded `n_parents = 0`.
3. **This is a worked example of the ΔΔG framing we argued for.** `external_data/ddg_study.md` recommends reporting ΔΔG as a mechanism channel beside AlphaMissense rather than as a competing pathogenicity score. PTPN2 C216S is what that looks like in practice: both numbers correct, the disagreement diagnostic.
4. The same group's JAK1 and PTPN2 papers are two halves of one pathway — JAK1/JAK3 and their phosphatase. A combined variant-interpretation framework across both would be a natural extension.

---

## 6. Provenance

| value | source |
|---|---|
| variants, phenotypes, inheritance, functional results | Europe PMC full text of PMC11259789 |
| FoldX ΔΔG, pLDDT | `external_data/protvar_foldx_*` — EBI ProtVar, FoldX v5 on AlphaFold2, 208,792,558 rows; PTPN2 subset 7,163 variants |
| ThermoMPNN ΔΔG, ESM-1v, AlphaMissense, RASA, secondary structure | Liao & Lehner 2026, Zenodo 18386427, `P17706_merged.csv`, 7,885 rows |
| domain boundaries, active site | UniProt P17706 |
| tail autoinhibition mechanism | [Nat Commun 2021](https://www.nature.com/articles/s41467-021-27633-6) |
| JAK1/JAK3 vs JAK2 specificity | [FEBS J review](https://febs.onlinelibrary.wiley.com/doi/10.1111/j.1742-4658.2012.08563.x) |

Percentiles are within PTPN2's own variant distribution (FoldX median +0.99 kcal/mol, IQR
+0.08…+2.84; ThermoMPNN median +0.62; ESM-1v median −9.29).
