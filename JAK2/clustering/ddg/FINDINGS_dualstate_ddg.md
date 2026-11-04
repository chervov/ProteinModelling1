# The dual-state ΔΔG features: results, and why `ddg_delta` should not be used

Run completed 4 November 2026. PyRosetta on **both** model pairs: 21,508 substitutions × 2 pairs
= **43,016 ΔΔG pairs, 100% coverage**, 43 min per pair at ~30,000 variants/h.
Raw: `data/ddg/ddg_JAK2P{1,2}_all.json`. Features built from **pair 1** (the untemplated pair).

## 1. The headline: `ddg_delta` is inert, and it is not reproducible

| feature | AUC vs the clustering | pair 1 ↔ pair 2 correlation |
|---|--:|--:|
| `ddg_closed` | 0.713 | **r = 0.893**, ρ = 0.928 |
| `ddg_open` | 0.717 | **r = 0.870**, ρ = 0.906 |
| **`ddg_delta`** | **0.499** | **r = 0.074**, ρ = 0.155 |

Two independent facts, and together they settle the question:

- **AUC 0.499 is exactly chance.** On JAK1 the same feature scored 0.4966. Two proteins, two
  independent model sets, the same answer: the conformational difference term carries no signal
  about which cluster a variant belongs to.
- **The pair-1/pair-2 correlation of 0.074 is the stronger result**, and it is what the second
  pair was computed for. `ddg_closed` and `ddg_open` reproduce well across two different model
  pairs (r ≈ 0.88), so the ΔΔG calculation itself is stable. **Their difference does not.**

The reason is visible in the numbers: the closed and open ΔΔG values are nearly identical for
almost every variant (median `delta` = −0.003 on pair 1). The two states differ only in where JH1
sits, and ΔΔG is local — so for the vast majority of positions, nothing about the residue's
environment changes between states. `delta` is therefore a difference of two large, strongly
correlated numbers, which is the classic recipe for a quantity dominated by numerical noise. That
noise does not reproduce between model pairs, and r = 0.074 measures exactly that.

**Recommendation: do not use `ddg_delta` as a feature.** Not because it is weak, but because it is
not measuring a property of the protein. `ddg_closed` and `ddg_open` are legitimate — though note
they are 0.713 and 0.717 and correlate with each other almost perfectly, so they are effectively
one feature, a general destabilisation term that FoldX (0.742) already supplies.

## 2. v2 clustering: the three features change almost nothing

| | v1 (8 features) | v2 (11 features) |
|---|---|---|
| C1 tolerant / C2 damaging | 7,746 / 13,762 | 7,910 / 13,598 |
| iterations | 13 | 10 |
| gnomAD pooled OR | 1.96 | 1.97 |

**v1 and v2 agree on 99.11% of variants, ARI 0.9644** — only 192 of 21,508 move. The external
gnomAD validation is unchanged to two decimal places.

This is the JAK1 result again: there, dropping the three ΔΔG features *improved* agreement with
the published clustering (ARI 0.484 → 0.492). Adding them here neither helps nor hurts.

**So `jak2_clustering_v1_wo_ddg_oc` was not missing anything important.** That is worth stating
plainly, because the whole dual-state structural effort — the model inventory, the pair selection,
the PAE analysis, two PyRosetta runs — was undertaken to fill a gap that turns out not to matter
for the clustering.

## 3. Full per-feature ranking (v2)

| feature | coverage | C1 mean | C2 mean | AUC |
|---|--:|--:|--:|--:|
| PolyPhen-2 | 100% | 0.22 | 0.91 | 0.964 |
| CADD | 31.1% | 16.95 | 27.27 | 0.955 |
| ClinPred | 31.1% | 0.60 | 0.97 | 0.951 |
| AlphaMissense | 100% | 0.23 | 0.78 | 0.942 |
| ESM-1b | 100% | −6.17 | −12.47 | 0.921 |
| SIFT | 31.1% | 0.33 | 0.04 | 0.898 |
| FoldX | 94.6% | 0.64 | 2.95 | 0.742 |
| `ddg_open` | 100% | −17.97 | −76.09 | 0.717 |
| `ddg_closed` | 100% | −19.27 | −75.74 | 0.713 |
| BLOSUM62 | 100% | −0.82 | −1.71 | 0.665 |
| **`ddg_delta`** | **100%** | **1.30** | **−0.36** | **0.499** |

AUCs are circular — these are the features the clustering was built from. They rank the features
against each other, they do not validate the result.

Sign convention: `ddG = dG_WT − dG_mut`, **negative = destabilising** (opposite to FoldX).
AUC is computed on the damaging direction, so `ddg_*` is negated first.

## 4. What this does not say

- **It does not say the closed state is wrong.** The two closed models agree to 1.53 Å and the
  ΔΔG values computed on them correlate at r = 0.89. The structures are fine; the *difference*
  feature is the problem.
- **It does not rule out a conformational signal in principle.** A difference term restricted to
  the residues whose environment actually changes between states — the JH1–JH2 and JH1–FERM
  interfaces — might carry signal that a protein-wide difference drowns. That is a different
  feature from the one the paper specifies, and it has not been tested.
- **It inherits the PAE caveat.** AlphaFold's FERM–JH1 PAE is 21.0 Å against a 31 Å ceiling, so
  the interface residues — exactly the ones where a difference could be real — sit in the least
  certain part of the model.

## Reproduce

```bash
cd ~/ddg_jak2 && python3 worker.py && python3 collect_jak2.py
cd JAK2/clustering && python3 cluster_jak2_v2.py
```
