# ΔΔG for human variants at scale — methods, data, and what I measured

*Compiled 28 October 2026. Three companion documents: this synthesis, the literature survey
([ddg_literature.md]({{artifact:559be41f-b7da-47a5-8e5f-ef56858d774c}}), 33 cited DOIs all resolved),
and the precomputed-resource audit
([ddg_precomputed_human.md]({{artifact:d4cc08ad-0b3d-42bb-a317-574c93ab10f4}})).
The earlier training-data memo (`external_data/ddg_precomputed.md`) is not repeated.*

---

## 0. The decision, up front

**Do not compute first — download first.** EBI's ProtVar already publishes FoldX ΔΔG for
**208,792,558 human missense variants** covering **20,173 of 20,431 reviewed human entries** and
**76.0% of all canonical human residues**, CC BY 4.0, keyed to UniProt accession and position. For
an arbitrary gene list, roughly three quarters of canonical missense variants already have a value.

Compute locally only for the missing quarter. I have that pipeline installed, validated and timed:
**ThermoMPNN at ~280 variants/s on one CPU core**, with measured accuracy of
**r = +0.517** on 386 held-out human measurements.

The harder truth from the literature: on genuinely unseen mutations the best predictors reach
**r ≈ 0.5–0.6**, not the 0.7–0.8 that method papers advertise, and experimental noise puts the
ceiling at r ≈ 0.7–0.8 anyway ([10.1093/bioinformatics/bty880](https://doi.org/10.1093/bioinformatics/bty880)).
Plan the project around a weak-but-real signal, not a precise one.

---

## 1. Precomputed human resources — verified

| resource | kind | proteins | variants | keyed to | status |
|---|---|--:|--:|---|---|
| **ProtVar FoldX** (EBI) | predicted, FoldX 5.0 on AF2 | 20,437 | **208.8M rows** | UniProt acc + pos | verified by full download, 1.5 GB gz |
| ProtVar per-gene bundles | predicted + ClinVar/gnomAD | 1,048 genes | ~3.9k/gene | GRCh38 + UniProt | verified (first member only) |
| ProtVar MAVE mirror | **experimental** | 537 human | 3.42M rows | MaveDB URN + offset | verified |
| Domainome Table 4 | predicted, homolog-averaged | 1,761 | 4.11M rows | UniProt acc + pos | verified, read in full |
| Domainome Table 2 | **experimental** aPCA | 434 | 546,537 missense | UniProt acc + pos | verified, read in full |
| ProteinGym substitutions | **experimental** DMS | 81 human | 329,664 human singles | mnemonic only | verified |
| Mega-scale human subset | **experimental** | 50 PDB domains | 46,955 rows (17.2%) | PDB only — needs SIFTS | verified |
| **RaSP human proteome** | predicted | 23,391 *(README)* | ~230M *(abstract)* | UniProt acc | **NOT verified — download blocked** |
| MAVISp | predicted consensus | unverified | unverified | UniProt acc | **NOT verified — host blocked** |

**On RaSP specifically:** its ERDA hosts were allowlisted on request and then reset the TLS
handshake reproducibly, under both `requests` and `curl`, TLS 1.2 and 1.3, IPv4 forced. Its
headline numbers come from the repository README and the eLife abstract, **not from the data**.
It is the only full-proteome alternative to ProtVar and the only one shipping a ready-made
gnomAD/ClinVar join, so it is worth retrying from an unrestricted network.

### Two traps in ProtVar worth knowing before you use it

1. **Its README is stale and contradicts the data.** The README claims only pLDDT > 70 is
   included; **34,838,191 rows (16.7%) are below 70**. Apply your own confidence filter.
2. **Overlapping AlphaFold fragments duplicate positions.** 10,989,614 position-fragment groups
   resolve to only 9,091,699 distinct positions — **17.3% are repeats**. Deduplicate before
   counting anything, or every per-protein statistic will be inflated.

---

## 2. Where the precomputed data runs out — and it is exactly your proteins

Coverage falls monotonically with protein length, then recovers:

| length | proteins | ProtVar residue coverage |
|---|--:|--:|
| ≤ 100 aa | 776 | 89.5% |
| 101–500 | 11,601 | 85.6% |
| 501–1,000 | 5,647 | 74.7% |
| **1,001–2,700** | **2,191** | **64.1%** |
| > 2,700 | 216 | 86.4% |

The **1,001–2,700 aa band is the worst served** — precisely the multi-domain band this project has
spent its time on. Above 2,700 aa coverage recovers because AlphaFold's overlapping fragment models
give dense coverage. The missing quarter is concentrated in **disordered regions and inter-domain
linkers**, which is where inter-domain interface variants sit.

Two further gaps: **non-canonical isoforms have no precomputed value in any resource verified
here**, and **membrane proteins are covered (82.7%, better than non-TM) but should not be trusted**
— FoldX on an AlphaFold monomer has no lipid. Note also that every large precomputed set is built on
AlphaFold2 **monomer** models, so none represents an inter-domain interface in a specific
conformational state.

---

## 3. What I installed, and how fast it actually runs

Measured on this machine (8 CPU cores, 16 GiB, **no GPU**), full saturation mutagenesis from an
AlphaFold model, wall-clock including model load:

| protein | length | variants | time | rate |
|---|--:|--:|--:|--:|
| Lysozyme C | 148 | 2,812 | 9.2 s | 305/s |
| TP53 | 393 | 7,467 | 15.9 s | 470/s |
| JAK1 | 1,154 | 21,926 | 65.1 s | 337/s |
| Fibronectin | 2,477 | 47,063 | 238.0 s | 198/s |

Across all 23 validation proteins: **269,458 variants in 16.0 min = 280 variants/s**
on one core. Scaling is linear in length at ~2.7 ms/variant plus ~2 s fixed overhead per protein.

**What this means for your next step.** The reviewed human proteome holds 216.9M possible canonical
missense variants. At the measured 280 variants/s that is **9.0 days single-core, or ~27 hours
across 8 cores** — so computing just the missing quarter (~52M variants) is **6.4 hours on 8
cores**. A gene list is a rounding error against that. Scale is not the obstacle, and no GPU is
needed.

### Package assessment

| tool | install | speed | support | verdict |
|---|---|---|---|---|
| **ThermoMPNN** | clone + torch, worked | 280 var/s sustained (198–470 per protein) | active, PNAS 2024, weights shipped | **recommended workhorse** |
| RaSP | clone, weights shipped | fast by design | eLife 2023, maintained | good second opinion; precomputed set blocked |
| ProteinMPNN log-odds | weights shipped | fastest | very active | zero-shot baseline, not calibrated kcal/mol |
| DDGun / DDGun3D | clone, needs MSA tooling | fast | stable | **the honesty baseline** — see §5 |
| FoldX | **licence required** | minutes/mutation | commercial | not installable here; is what ProtVar used |
| Rosetta `cartesian_ddg` | **licence + heavy** | ~hours/mutation | academic standard | infeasible at this scale |

Install friction worth recording: ThermoMPNN's `git clone` **fails in this sandbox** because the
repo contains a `.idea/` directory the filesystem refuses to create. The tarball route works. Its
scripts also need `analysis/` on `PYTHONPATH`, and `local.yaml` rewritten for `accel: "cpu"`.

---

## 4. What I measured, not quoted

I ran ThermoMPNN over all 23 human proteins in FireProtDB's **homology-filtered** split — genuinely
held out, >25% identity filtered — giving 386 experimental comparisons. All 386 joined with
wild-type residue agreement, confirming position registration.

![validation]({{artifact:0deca401-4ffb-49e0-a8ff-200343c30fc8}})

- **Overall: r = +0.517, Spearman +0.559, RMSE 1.47 kcal/mol** (n = 386). Both conventions agree
  that positive = destabilising, verified empirically rather than assumed.
- **Large proteins do not do worse.** ≥800 aa: r = +0.563, RMSE 1.28 (n = 32, 4 proteins).
  <800 aa: r = +0.490, RMSE 1.49 (n = 354). This is the only evidence I am aware of in this
  regime — the literature survey found **no benchmark at all** on large multi-domain proteins.
  Treat it as weak: 32 measurements over 4 proteins, dominated by fibronectin and tenascin, which
  are tandem-repeat proteins whose domains are small and largely independent. It hints the method
  does not collapse; it does not show interface variants are handled.
- **Skill collapses on stabilising mutations: r = +0.068, sign correct in only 43%** (n = 108),
  against r = +0.430 on destabilising ones. This independently reproduces Zheng et al.'s finding that
  *none* of 27 methods predicts stabilising mutations accurately
  ([10.1002/pro.4861](https://doi.org/10.1002/pro.4861)). **Do not use this pipeline to find
  stabilising mutations.**
- **Per-protein variance dwarfs the average**, from r = +0.93 to r = −0.14. The instructive failure
  is **α-1-antitrypsin (P01009): r = −0.137 over 45 measurements** — a serpin, *metastable by
  design*, so native-state ΔΔG is the wrong quantity for it. Carbonic anhydrase II gives RMSE
  3.69 kcal/mol. A global correlation hides proteins where ΔΔG is noise.

---

## 5. Best practice, as the evidence supports it

1. **Audit antisymmetry on your own proteins — it is free.** Score A→B and B→A and check the sum is
   near zero; it needs no experimental data
   ([10.1093/bioinformatics/bty340](https://doi.org/10.1093/bioinformatics/bty340)). Black-box ML
   methods fail badly here (AUTOMUTE ⟨δ⟩ = −0.99 kcal/mol), predicting "destabilising" both ways.
2. **Quote direct-only correlations.** S669's "total" column pools direct and reverse variants, so
   antisymmetric methods score higher automatically (PremPS 0.62 total vs 0.41 direct).
3. **Beat DDGun or justify the complexity.** DDGun is untrained and antisymmetric by construction
   and lands within ~0.04 Pearson of the best trained methods on S669. If a sophisticated pipeline
   cannot beat it on your data, the complexity buys nothing.
4. **Treat ±0.5 kcal/mol as noise**
   ([10.1186/s12859-021-04238-w](https://doi.org/10.1186/s12859-021-04238-w)).
5. **AlphaFold models are fine as input; pLDDT is not a ΔΔG proxy.** AF2-based predictions are
   comparable to experimental structures
   ([10.1038/s41594-022-00849-w](https://doi.org/10.1038/s41594-022-00849-w)); homology models
   degrade below 40% template identity. But mutation-induced pLDDT change does not correlate with
   ΔΔG ([10.1371/journal.pone.0282689](https://doi.org/10.1371/journal.pone.0282689)).
   **Circularity warning:** in 26 hereditary-cancer genes, stability predictors on AF2 structures
   gave pathogenicity AUROC 0.614–0.719 while the AF2 confidence score *alone* gave 0.852
   ([10.3389/fgene.2023.1052383](https://doi.org/10.3389/fgene.2023.1052383)) — an apparent ΔΔG
   signal can be a proxy for burial that pLDDT captures more directly.
6. **Use homology-aware splits if you ever train.** ProteinGym: a one-hot baseline scores 0.579 on
   random splits and **0.064** on contiguous ones.
7. **Don't bother with epistasis models for doubles.** Simple additive models match epistasis-aware
   predictors on most metrics ([10.1002/pro.70003](https://doi.org/10.1002/pro.70003)).

### If the goal is interpreting pathogenicity, read this first

ΔΔG is a **weak** classifier of pathogenicity — best AUC ≈ 0.66–0.68, FoldX top at 0.661
([10.1038/s41598-020-72404-w](https://doi.org/10.1038/s41598-020-72404-w)) — and all tested
stability predictors were inferior to dedicated variant-effect predictors. Three consequences:

- **Use |ΔΔG|, not signed ΔΔG**: strongly *stabilising* variants are also enriched in disease.
- **Compute on complexes where they exist**: monomer → full biological assembly raised pathogenic
  mean |ΔΔG| from 3.39 to 3.89 kcal/mol and AUC from 0.652 to 0.677
  ([10.1038/s41467-022-31686-6](https://doi.org/10.1038/s41467-022-31686-6)).
- **Accept a structural blind spot**: dominant-negative and gain-of-function variants are milder
  than loss-of-function and close to benign in magnitude, and account for **48% of phenotypes in
  dominant genes** ([10.1038/s41467-025-63234-3](https://doi.org/10.1038/s41467-025-63234-3)).
  ΔΔG is close to the wrong quantity for them.

**Report outputs as stability scores, not pathogenicity scores**, and keep a sequence-based
predictor alongside.

---

## 6. Recommended pipeline for the computation you asked for next

1. Download ProtVar's FoldX table (1.5 GB), **deduplicate AlphaFold fragments** and apply your own
   pLDDT filter. This answers ~76% of canonical variants with no compute at all.
2. Resolve your gene list to canonical UniProt accessions; flag non-canonical isoforms as
   out-of-scope-for-precomputed up front.
3. For uncovered positions, run ThermoMPNN on AlphaFold models — 6.4 h on 8 cores for the whole
   missing quarter of the proteome, far less for a gene list.
4. Run **DDGun as a baseline** and **the antisymmetry audit** on a sample of targets; if ThermoMPNN
   does not beat DDGun on your proteins, say so in the output rather than burying it.
5. Cross-check against Domainome Table 4 (independent, experiment-anchored kcal/mol) wherever it
   overlaps — 1,761 genes, though it covers a median 17.6% of a covered protein's residues and
   misses JAK1/2/3, TYK2, TP53, BRCA1, PTEN, CFTR and TTN entirely.
6. Emit per-variant confidence, not just a number: pLDDT at the site, whether the position sits in
   a domain or a linker, and whether |ΔΔG| clears the 0.5 kcal/mol noise floor.

---

## 7. What I could not verify

- **RaSP's human proteome** — download blocked at the TLS layer after allowlisting; counts are from
  README and abstract only.
- **MAVISp** — host blocked; access not requested since ProtVar supersedes it on scale.
- **ProtVar's distinct-variant count** — reported as a bound (172,724,083–172,742,281) because
  hashing ~173M keys exceeds this machine's memory; the two underlying full-file counts are exact.
- **ProtVar's 1,048-gene list** — not enumerated; the figure comes from the filename.
- **Mega-scale human fraction (17.2%)** — measured on the 298-domain ThermoMPNN split subset, not
  the full Zenodo release.
- **No quantified accuracy penalty for AlphaFold inputs exists in the literature** — the Akdel
  values live in a figure panel; "comparable to experimental structures" is the authors' wording.
