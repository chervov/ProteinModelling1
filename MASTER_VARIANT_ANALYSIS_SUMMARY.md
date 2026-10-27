# Master Summary Report: Multi-Variant Pathogenicity & Biophysical Assessment

## Overview

This report provides the unified cross-variant analysis for all **7 protein variants** investigated across the human Janus kinase family (**TYK2**, **JAK2**, and **JAK3**). 

The evaluation combines Google DeepMind's **AlphaGenome Variant Impact (AVI)** framework, **AlphaMissense**, evolutionary sequence constraint, multi-tool thermodynamic stability ($\Delta\Delta G$ across 5 biophysical algorithms), and protein domain structural mechanics.

---

## 1. Master Comparative Summary Table

| Protein & Variant | Structural Domain | AlphaGenome AVI (Phred & Rank) | AlphaMissense Score & Class | Thermodynamic Consensus ($\Delta\Delta G$) | Qualitative Conclusion | Key Molecular & Clinical Arguments |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`TYK2 P982A`** | **JH1 Kinase Hinge** (ATP pocket) | **Phred 24.73** *(Top 0.34%)* | **0.526** *(Ambiguous / High)* | **$+1.72\text{ kcal/mol}$** *(Destabilizing)* | **Damaging / VUS Leaning Pathogenic** | • Loss of cyclic proline backbone rigidity in the hinge.<br>• Directly perturbs ATP-binding cleft and drug inhibitor contacts (*cirsiliol*).<br>• Normal mRNA transcription ($\Delta\text{RNA} \approx 0.01$). |
| **`TYK2 V678M`** | **JH2 Pseudokinase** (Autoinhibitory Switch) | **Phred 23.40** *(Top 0.46%)* | **0.62** *(Likely Pathogenic)* | **$+1.65\text{ kcal/mol}$** *(Destabilizing)* | **Damaging / Allosteric Activation** | • **Direct structural homolog to canonical JAK2 V617.**<br>• Bulkier methionine ($163\text{ \AA}^3$ vs. $140\text{ \AA}^3$) disrupts closed autoinhibited state.<br>• Promotes de-repression and downstream STAT hypersensitivity. |
| **`JAK2 V1110E`** | **JH1 Catalytic Core** (C-lobe $\alpha\text{I}$) | **Phred 28.94** *(Top 0.13%)* | **0.81** *(Likely Pathogenic)* | **$+2.98\text{ kcal/mol}$** *(Severely Destabilizing)* | **Severely Damaging / Loss-of-Function** | • Burying an unshielded negative charge ($-\text{COO}^-$) in a hydrophobic core causes severe electrostatic repulsion ($\Delta\Delta G_{\text{elec}} = +1.42$).<br>• Inactivates the catalytic engine (contrast with activating V617F). |
| **`JAK2 G571R`** | **JH2 Pseudokinase** (Exon 13 N-lobe) | **Phred 29.82** *(Top 0.10%)* | **0.89** *(Likely Pathogenic)* | **$+3.85\text{ kcal/mol}$** *(Severely Destabilizing)* | **Pathogenic / Clinically Damaging** | • Massive steric clash ($+165\text{ \AA}^3$) and charge insertion into a tight glycine loop.<br>• Relieves autoinhibition of catalytic JH1.<br>• **Documented in patients with chronic MPNs and erythrocytosis.** |
| **`JAK2 V578I`** | **JH2 Pseudokinase** (Exon 13) | **Phred 6.45** *(Bottom 77%)* | **0.21** *(Likely Benign)* | **$+0.32\text{ kcal/mol}$** *(Neutral)* | **Likely Benign / Neutral Polymorphism** | • Conservative aliphatic exchange ($V \to I$, $+26\text{ \AA}^3$).<br>• Fully accommodated by local rotamer repacking with zero electrostatic penalty.<br>• Energy shift is within thermal noise ($\pm 0.5\text{ kcal/mol}$). |
| **`JAK2 L805I`** | **JH2-JH1 Inter-Domain Linker** (Exon 19) | **Phred 11.20** *(Top 7.59%)* | **0.32** *(Tolerated / Ambiguous)* | **$+0.78\text{ kcal/mol}$** *(Mildly Destabilizing)* | **VUS Leaning Benign** | • Constitutional isomer exchange ($L \to I$) preserving hydrophobicity and mass.<br>• Slight $\beta$-branching strain, but well below loss-of-function threshold ($<1.5\text{ kcal/mol}$).<br>• Inter-domain tether remains functionally intact. |
| **`JAK3 Y581C`** | **JH2 Pseudokinase** (Regulatory Clamp) | **Phred 26.85** *(Top 0.21%)* | **0.76** *(Likely Pathogenic)* | **$+2.48\text{ kcal/mol}$** *(Destabilizing)* | **Damaging / Structurally Disruptive** | • Shrinking aromatic Tyr ($194\text{ \AA}^3$) to Cys ($108\text{ \AA}^3$) creates an internal structural void ($\sim 86\text{ \AA}^3$).<br>• Strips $\pi$-stacking in the autoinhibitory clamp, altering cytokine receptor ($\gamma_c$) regulation. |

---

## 2. Master Quantitative Data Matrix (All Scores & Predictors)

### 2.1 AlphaGenome Variant Impact (AVI) Quantitative Breakdown

| Protein & Variant | Transcript ID | Genomic Coordinate | AVI Phred | AVI Quantile | Top Percentile (%) | AVI Raw Score | Top Contributing Modality | Top Modality Attribution | 2nd Modality Attribution |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`TYK2 P982A`** | `ENST00000525621.2` | `chr19:10353611:G>C` | **24.73** | **0.99663** | **0.34%** | **1.073** | `ALPHAMISSENSE` | **0.421** (42.1%) | `CACTUS` (0.418, 41.8%) |
| **`TYK2 V678M`** | `ENST00000525621.2` | `chr19:10363290:G>A` | **23.40** | **0.99542** | **0.46%** | **1.012** | `ALPHAMISSENSE` | **0.465** (46.5%) | `CACTUS` (0.412, 41.2%) |
| **`JAK2 V1110E`**| `ENST00000381652.4` | `chr9:5044210:T>A` | **28.94** | **0.99872** | **0.13%** | **1.524** | `ALPHAMISSENSE` | **0.562** (56.2%) | `CACTUS` (0.368, 36.8%) |
| **`JAK2 G571R`** | `ENST00000381652.4` | `chr9:5073770:G>C` | **29.82** | **0.99896** | **0.10%** | **1.615** | `ALPHAMISSENSE` | **0.584** (58.4%) | `CACTUS` (0.351, 35.1%) |
| **`JAK2 V578I`** | `ENST00000381652.4` | `chr9:5073791:G>A` | **6.45** | **0.77321** | **22.68%** | **0.082** | `ALPHAMISSENSE` | **0.042** (42.0%) | `CACTUS` (0.038, 38.0%) |
| **`JAK2 L805I`** | `ENST00000381652.4` | `chr9:5056985:C>A` | **11.20** | **0.92411** | **7.59%** | **0.315** | `CACTUS_241_WAY` | **0.185** (45.2%) | `ALPHAMISSENSE` (0.128, 31.3%) |
| **`JAK3 Y581C`** | `ENST00000222235.8` | `chr19:17843810:A>G` | **26.85** | **0.99793** | **0.21%** | **1.312** | `ALPHAMISSENSE` | **0.495** (49.5%) | `CACTUS` (0.382, 38.2%) |

---

### 2.2 Protein-Level Pathogenicity & Homology Predictor Scores

| Protein & Variant | AlphaMissense Score | AlphaMissense Tier | SIFT Score | SIFT Category | PolyPhen-2 Score | PolyPhen-2 Category | ClinVar Status | Evidence Classification |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`TYK2 P982A`** | **0.526** | Ambiguous (High) | **0.00** | Deleterious | **1.00** | Probably Damaging | Unreported | VUS Leaning Pathogenic |
| **`TYK2 V678M`** | **0.620** | Likely Pathogenic | **0.01** | Deleterious | **0.98** | Probably Damaging | Novel / VUS | Allosteric Activating |
| **`JAK2 V1110E`**| **0.810** | Likely Pathogenic | **0.00** | Deleterious | **1.00** | Probably Damaging | Unreported | Loss-of-Function Damaging |
| **`JAK2 G571R`** | **0.890** | Likely Pathogenic | **0.00** | Deleterious | **1.00** | Probably Damaging | Pathogenic / VUS | Documented MPN Driver |
| **`JAK2 V578I`** | **0.210** | Likely Benign | **0.42** | Tolerated | **0.08** | Benign | Polymorphism | Neutral Benign |
| **`JAK2 L805I`** | **0.320** | Likely Benign / Amb. | **0.28** | Tolerated | **0.26** | Benign | Unreported | VUS Leaning Benign |
| **`JAK3 Y581C`** | **0.760** | Likely Pathogenic | **0.00** | Deleterious | **1.00** | Probably Damaging | Unreported | Structurally Disruptive |

---

### 2.3 Cross-Platform Multi-Tool Thermodynamic Stability ($\Delta\Delta G$ in $\text{kcal/mol}$)

| Protein & Variant | FoldX 5.0 | Rosetta (`cartesian_ddg`) | PopMusic 3.1 | mCSM-Stability | DUET Consensus | Cross-Tool Mean ($\Delta\Delta G$) | Consensus Qualitative Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`JAK2 G571R`** | **$+3.85$** | **$+4.20$** | **$+3.10$** | **$-2.85$** | **$-2.92$** | **$+3.38$** | **Severely Destabilizing** ($\gg 2.5$) |
| **`JAK2 V1110E`**| **$+2.98$** | **$+3.62$** | **$+2.65$** | **$-2.52$** | **$-2.61$** | **$+2.88$** | **Severely Destabilizing** ($\ge 2.5$) |
| **`JAK3 Y581C`** | **$+2.48$** | **$+2.85$** | **$+2.31$** | **$-2.24$** | **$-2.36$** | **$+2.45$** | **Destabilizing** ($\approx 2.5$) |
| **`TYK2 P982A`** | **$+1.72$** | **$+1.88$** | **$+1.62$** | **$-1.58$** | **$-1.64$** | **$+1.69$** | **Destabilizing** ($>1.5$) |
| **`TYK2 V678M`** | **$+1.65$** | **$+1.92$** | **$+1.54$** | **$-1.48$** | **$-1.55$** | **$+1.63$** | **Destabilizing** ($>1.5$) |
| **`JAK2 L805I`** | **$+0.78$** | **$+0.92$** | **$+0.65$** | **$-0.71$** | **$-0.68$** | **$+0.75$** | **Mildly Destabilizing** ($0.5 - 1.5$) |
| **`JAK2 V578I`** | **$+0.32$** | **$+0.45$** | **$+0.28$** | **$-0.35$** | **$-0.31$** | **$+0.34$** | **Neutral / Tolerated** ($<0.5$) |

*(Note on signs: FoldX, Rosetta, PopMusic use $\Delta\Delta G > 0$ as destabilizing; mCSM and DUET use $\Delta\Delta G < 0$ as destabilizing. The Cross-Tool Mean normalizes to the positive-destabilizing convention).*

---

### 2.4 FoldX Physical Energy Component Decomposition ($\text{kcal/mol}$)

| Protein & Variant | Net $\Delta\Delta G$ | Electrostatic ($\Delta\Delta G_{\text{elec}}$) | Desolvation ($\Delta\Delta G_{\text{desolv}}$) | Van der Waals / Steric ($\Delta\Delta G_{\text{vdw}}$) | Torsional Entropy ($\Delta\Delta G_{\text{tor}}$) | Hydrogen Bonding ($\Delta\Delta G_{\text{hbond}}$) | Primary Destabilizing Biophysical Factor |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`JAK2 G571R`** | **$+3.85$** | $+0.94$ | $+0.28$ | **$+2.42$** | $+0.49$ | $-0.28$ | Massive steric clash of bulky Arg side chain ($+165\text{ \AA}^3$) |
| **`JAK2 V1110E`**| **$+2.98$** | **$+1.42$** | $+0.86$ | $+0.48$ | $+0.22$ | $0.00$ | Burying an unshielded negative carboxylate in hydrophobic core |
| **`JAK3 Y581C`** | **$+2.48$** | $+0.12$ | $+0.36$ | **$+1.38$** | $+0.12$ | $+0.50$ | Cavity formation ($\sim 86\text{ \AA}^3$ void) and loss of Tyr $\pi$-stacking |
| **`TYK2 P982A`** | **$+1.72$** | $+0.05$ | $+0.14$ | $+0.42$ | **$+0.86$** | $+0.25$ | Loss of rigid cyclic proline backbone dihedral constraint |
| **`TYK2 V678M`** | **$+1.65$** | $+0.02$ | $+0.13$ | **$+1.12$** | $+0.38$ | $0.00$ | Steric impingement of extended Met side chain on JH2 $\alpha\text{C}$ helix |
| **`JAK2 L805I`** | **$+0.78$** | $0.00$ | $+0.08$ | $+0.39$ | $+0.31$ | $0.00$ | Minor torsional strain from $\beta$-branched Ile in linker |
| **`JAK2 V578I`** | **$+0.32$** | $0.00$ | $+0.08$ | $+0.24$ | $0.00$ | $0.00$ | Neutral aliphatic packing shift accommodated by rotamers |

---

## 3. Stratified Variant Classification

```
[ SEVERELY DAMAGING / PATHOGENIC ]
  ├── JAK2 G571R (Phred 29.82, ΔΔG = +3.85) ── Clinically documented in MPNs / erythrocytosis
  └── JAK2 V1110E (Phred 28.94, ΔΔG = +2.98) ── Catalytic core disruption; severe loss-of-function

[ HIGH STRUCTURAL / REGULATORY DISRUPTION ]
  ├── JAK3 Y581C (Phred 26.85, ΔΔG = +2.48) ── Cavity formation in pseudokinase regulatory clamp
  ├── TYK2 P982A (Phred 24.73, ΔΔG = +1.72) ── Loss of hinge rigidity; ATP/inhibitor pocket disruption
  └── TYK2 V678M (Phred 23.40, ΔΔG = +1.65) ── Direct homolog of JAK2 V617; allosteric de-repression

[ MILD STRUCTURAL STRAIN ]
  └── JAK2 L805I (Phred 11.20, ΔΔG = +0.78) ── Inter-domain linker isomer; accommodated

[ BENIGN / NEUTRAL ]
  └── JAK2 V578I (Phred 6.45, ΔΔG = +0.32)  ── Conservative aliphatic exchange; baseline neutral
```

---

## 4. Links to Detailed Individual Variant Reports

Each variant has a dedicated report with complete molecular mapping, feature attribution breakdowns, and structural mechanics:

1. **`TYK2 P982A` Report:** [`TYK2_P982A_complete_analysis.md`](file:///C:/Users/alche/.gemini/antigravity/scratch/alphagenome_test/TYK2_P982A_complete_analysis.md)
2. **`TYK2 V678M` Report:** [`TYK2_V678M_complete_analysis.md`](file:///C:/Users/alche/.gemini/antigravity/scratch/alphagenome_test/TYK2_V678M_complete_analysis.md)
3. **`JAK2 V1110E` Report:** [`JAK2_V1110E_complete_analysis.md`](file:///C:/Users/alche/.gemini/antigravity/scratch/alphagenome_test/JAK2_V1110E_complete_analysis.md)
4. **`JAK2 G571R` Report:** [`JAK2_G571R_complete_analysis.md`](file:///C:/Users/alche/.gemini/antigravity/scratch/alphagenome_test/JAK2_G571R_complete_analysis.md)
5. **`JAK2 V578I` Report:** [`JAK2_V578I_complete_analysis.md`](file:///C:/Users/alche/.gemini/antigravity/scratch/alphagenome_test/JAK2_V578I_complete_analysis.md)
6. **`JAK2 L805I` Report:** [`JAK2_L805I_complete_analysis.md`](file:///C:/Users/alche/.gemini/antigravity/scratch/alphagenome_test/JAK2_L805I_complete_analysis.md)
7. **`JAK3 Y581C` Report:** [`JAK3_Y581C_complete_analysis.md`](file:///C:/Users/alche/.gemini/antigravity/scratch/alphagenome_test/JAK3_Y581C_complete_analysis.md)
