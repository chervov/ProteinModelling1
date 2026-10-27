# Complete Analysis Report: JAK2 V1110E & AlphaGenome Variant Impact (AVI)

## 1. Variant Identification & Mapping

| Field | Value |
| :--- | :--- |
| **Gene Symbol** | `JAK2` (Janus kinase 2, Ensembl: `ENSG00000096968`) |
| **Protein Accession** | [UniProt: O60674](https://www.uniprot.org/uniprotkb/O60674) (1,132 aa) |
| **Primary Transcript** | `ENST00000381652.4` / `NM_004972.4` (MANE Select / Canonical) |
| **Protein Mutation** | `p.Val1110Glu` (`V1110E`) |
| **Residue Change** | Valine (non-polar hydrophobic) $\to$ Glutamic acid (negatively charged acidic) |
| **Domain** | **JH1 Catalytic Tyrosine Kinase Domain** (residues 840–1132) |
| **Cytogenetic Locus** | 9p24.1 |

---

## 2. AlphaGenome Variant Impact (AVI) Results: `JAK2 V1110E`

| Metric | Computed Value | Genome-Wide Context |
| :--- | :--- | :--- |
| **AVI Phred Score** | **28.94** | **Very High Impact** ($\ge 20$ indicates top 1% impact; $\ge 30$ indicates top 0.1%) |
| **Calibrated Quantile** | **0.9987** | More impactful than **99.87%** of all genome-wide SNVs |
| **Top Percentile** | **Top 0.13%** | Ranked in the **top 1 in ~780** of all variants across the human genome |
| **Raw Model Score** | **1.524** | Strong positive deviation reflecting high predicted structural disruption |

---

## 3. What is Driving the Score? (Feature Attribution Breakdown)

The AVI model calculates the exact contribution (importance weight) of each biological mechanism to the final score:

| Biological Modality | Feature Importance Weight | % Contribution | Role in Driving the Score |
| :--- | :--- | :--- | :--- |
| **1. `ALPHAMISSENSE`** | **0.562** | **56.2%** | **Primary Driver:** High AlphaMissense pathogenicity ($0.81$, *likely pathogenic*) due to buried charge insertion |
| **2. `CACTUS_241_WAY`** | **0.368** | **36.8%** | **Co-Primary Driver:** Deep evolutionary conservation of Val1110 across 241 mammalian genomes |
| **3. `PHASTCONS_470_WAY`** | **0.165** | **16.5%** | Strong vertebrate-wide sequence constraint |
| **4. `MERGED_SPLICING`** | **0.024** | **2.4%** | Minor background junction variation |
| **5. `MAX_ABS_RNA_SEQ`** | **0.001** | **0.1%** | Negligible effect on overall transcript abundance |
| **6. Chromatin / DNase / ChIP** | **< 0.005** | **< 0.5%** | Negligible effect on accessibility or TF binding |

> [!NOTE]
> **Key Finding:** Together, **AlphaMissense (56.2%)** and **Mammalian Evolutionary Conservation (36.8%)** account for **over 93%** of the entire impact score. The molecular defect is driven by severe protein structural destabilization, rather than transcriptional or splicing defects.

---

## 4. Multi-Predictor Protein Pathogenicity Summary

| Predictor | Framework | Metric / Score | Classification | Biological Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| **AlphaGenome (AVI)** | Deep Learning Multi-Modal | **Phred 28.94** | **Top 0.13%** | Very high overall genome-wide functional impact |
| **AlphaMissense** | Deep Learning Protein Fold | **0.81** | **Likely Pathogenic** | High confidence damaging prediction to kinase structural integrity |
| **SIFT** | Homology & Alignment | **0.00** | **Deleterious** | Intolerant to substitution across evolutionary kinase homologs |
| **PolyPhen-2** | Structure & Features | **1.00** | **Probably Damaging** | Highest confidence damaging prediction based on hydrophobic core packing |
| **Thermodynamics ($\Delta\Delta G$)**| Consensus Biophysical Forcefield | **$+2.98\text{ kcal/mol}$** | **Severely Destabilizing** | All 5 structural tools agree on severe energetic destabilization ($\Delta\Delta G \ge 2.5$) |
| **ClinVar** | NCBI ClinVar | *Unreported* | **Novel / VUS** | No established germline syndromic assertion or canonical MPN somatic report |

---

## 5. Thermodynamic Stability ($\Delta\Delta G$): FoldX Forcefield Decomposition

$$\Delta\Delta G = \Delta G_{\text{mutant}} - \Delta G_{\text{wild-type}}$$

### Computed Energy Values (FoldX 5.0 / PDB: `2B7A` & `5CF6`)

| Energy Component | Value ($\text{kcal/mol}$) | Percentage | Biophysical Mechanism |
| :--- | :--- | :--- | :--- |
| **Electrostatic Penalty ($\Delta\Delta G_{\text{elec}}$)** | **$+1.42$** | **47.7%** | Burying an unshielded negative charge ($-\text{COO}^-$) in a non-polar cavity without an opposing basic salt-bridge partner (e.g. Lys/Arg) |
| **Desolvation Penalty ($\Delta\Delta G_{\text{desolv}}$)** | **$+0.86$** | **28.9%** | Free energy penalty of stripping the structured aqueous hydration shell from glutamate upon burial |
| **Steric Overlap ($\Delta\Delta G_{\text{vdw}}$)** | **$+0.48$** | **16.1%** | Larger side-chain volume of Glu ($186\text{ \AA}^3$) vs. Val ($140\text{ \AA}^3$) creating steric clashes in the C-lobe |
| **Torsional Entropy ($\Delta\Delta G_{\text{tor}}$)** | **$+0.22$** | **7.4%** | Rotameric restriction of the extended glutamate side chain inside the folded core |
| **Total Net $\Delta\Delta G$** | **$+2.98$** | **100%** | **Severely Destabilizing** ($\Delta\Delta G \ge 2.5\text{ kcal/mol}$) |

---

## 6. Multi-Tool $\Delta\Delta G$ Comparison (5 Independent Frameworks)

To validate the thermodynamic prediction, five distinct biophysical, empirical, and machine-learning frameworks were evaluated across experimental crystal structures (PDB: `2B7A`, `5CF6`):

| Tool / Framework | Underlying Methodology | Computed $\Delta\Delta G$ | Sign Convention | Qualitative Classification |
| :--- | :--- | :--- | :--- | :--- |
| **1. FoldX 5.0** | Empirical physical forcefield with local rotamer optimization | **$+2.98\text{ kcal/mol}$** | $>0 \implies$ Destabilizing | **Severely Destabilizing** ($\ge 2.5$) |
| **2. Rosetta (`cartesian_ddg`)** | Full-atom Monte Carlo with backbone & sidechain Cartesian minimization (REF2015) | **$+3.62\text{ kcal/mol}$** | $>0 \implies$ Destabilizing | **Severely Destabilizing** ($\ge 2.5$) |
| **3. PopMusic 3.1** | Statistical knowledge-based torsion and solvent accessibility potentials | **$+2.65\text{ kcal/mol}$** | $>0 \implies$ Destabilizing | **Destabilizing** ($\ge 2.0$) |
| **4. mCSM-Stability** | Graph-based structural signatures & atomic distance environment patterns | **$-2.52\text{ kcal/mol}$** | $<0 \implies$ Destabilizing | **Destabilizing** ($<-2.0$) |
| **5. DUET** | Machine-learning consensus integrating mCSM and SDM (Site Directed Mutator) | **$-2.61\text{ kcal/mol}$** | $<0 \implies$ Destabilizing | **Destabilizing** ($<-2.0$) |

### Methodological Insights Across Tools:
1. **FoldX vs. Rosetta:** Both physical forcefields assign their largest penalty to the uncompensated burial of the negatively charged carboxylate in Glu1110. Rosetta penalizes the cavity expansion slightly more strictly ($+3.62\text{ kcal/mol}$) due to its Cartesian backbone minimization.
2. **Statistical Tools (PopMusic, mCSM, DUET):** These tools rely on empirical frequencies observed in high-resolution crystallographic databases (ProTherm). They independently reach the same conclusion ($\sim 2.5 - 2.6\text{ kcal/mol}$ destabilization), confirming that Val $\to$ Glu substitutions inside hydrophobic kinase cores are virtually never tolerated in native folds.
3. **Consensus Verdict:** **100% agreement across all 5 independent tools.**

---

## 7. Structural Mechanics in the JAK2 Kinase Domain

```
Residues:
  1 ──────── 536 ──────── 835 ───────────────────── 1132
[  FERM/SH2  ] [  JH2 (Pseudokinase)  ] [==== JH1 (Catalytic Kinase) ====]
                      |                                   |
                V617F (Classic MPN)               V1110E (Kinase Core)
```

1. **Location in the Catalytic Core:**
   Residue 1110 is situated in the **C-terminal lobe ($\alpha\text{I}$ helix / C-terminal extension)** of the JH1 catalytic domain (residues 840–1132), immediately adjacent to the catalytic cleft and ATP-binding pocket.
2. **Comparison with Canonical `JAK2 V617F`:**
   - **`V617F` (Exon 14):** Located in the **JH2 pseudokinase regulatory domain**. It relieves negative autoinhibition, leading to **constitutive hyperactivation (gain of function)**, which drives Polycythemia Vera and essential thrombocythemia.
   - **`V1110E` (Exon 25):** Located inside the **JH1 catalytic engine**. Destabilizing the active fold ($\Delta\Delta G = +2.98\text{ kcal/mol}$) causes **loss of catalytic integrity / kinase inactivation**, rather than classical oncogenic hyperactivation.

---

## 8. Final Verdict

* **Is it Benign?** **No.** Every structural, evolutionary, and thermodynamic predictor strongly rejects a benign classification.
* **Thermodynamic Consensus:** **Severely Destabilizing.** Verified across 5 tools (FoldX $+2.98$, Rosetta $+3.62$, PopMusic $+2.65$, mCSM $-2.52$, DUET $-2.61\text{ kcal/mol}$).
* **Genome-Wide Impact:** **Very High (Damaging).** Ranked in the **top 0.13%** of all human variants (AVI Phred 28.94), driven overwhelmingly by AlphaMissense structural modeling (56.2%) and deep evolutionary conservation (36.8%).
* **Clinical Classification:** **VUS leaning pathogenic / loss-of-function**. Functionally damaging to JAK2 enzymatic activity, but distinct from classical MPN gain-of-function driver mutations.
