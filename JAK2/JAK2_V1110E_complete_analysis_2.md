# Complete Analysis Report: JAK2 V1110E & AlphaGenome Variant Impact (AVI)

## 1. Variant Identification & Mapping

| Field | Value |
| :--- | :--- |
| **Gene Symbol** | `JAK2` (Janus kinase 2, Ensembl: `ENSG00000096968`) |
| **Protein Accession** | [UniProt: O60674](https://www.uniprot.org/uniprotkb/O60674) (1,132 aa) |
| **Primary Transcript** | `ENST00000381652.4` / `NM_004972.4` |
| **Protein Mutation** | `p.Val1110Glu` (`V1110E`) |
| **Coding Change** | `c.3329T>A` (Exon 25) |
| **Genomic Coordinate** | `chr9:5126721:T>A` (GRCh38, forward strand) |
| **Residue Change** | Valine (non-polar hydrophobic) $\to$ Glutamic acid (negatively charged acidic) |
| **Domain** | **JH1 Catalytic Tyrosine Kinase Domain** (C-lobe $\alpha\text{I}$ helix) |
| **Cytogenetic Locus** | 9p24.1 |

---

## 2. AlphaGenome Variant Impact (AVI) Results: `JAK2 V1110E`

| Metric | Computed Value | Genome-Wide Context |
| :--- | :--- | :--- |
| **AVI Phred Score** | **22.67** | **High Impact** ($\ge 20$ indicates top 1% impact genome-wide) |
| **Calibrated Quantile** | **0.99459** | More impactful than **99.46%** of all genome-wide SNVs |
| **Top Percentile** | **Top 0.541%** | Ranked in the **top 1 in ~185** of all variants across the human genome |
| **Raw Model Score** | **0.7701** | Strong positive functional disruption |

---

## 3. What is Driving the Score? (Feature Attribution Breakdown)

| Biological Modality | Feature Importance Weight | % Contribution | Role in Driving the Score |
| :--- | :--- | :--- | :--- |
| **1. `CACTUS_241_WAY`** | **0.283** | **34.2%** | **Primary Driver:** Evolutionary conservation across 241 mammalian genomes |
| **2. `ALPHAMISSENSE`** | **0.228** | **27.6%** | **Co-Primary Driver:** AlphaMissense structural disruption from buried charge insertion |
| **3. `PHASTCONS_470_WAY`** | **0.161** | **19.5%** | Vertebrate sequence constraint across 470 species |
| **4. `MERGED_SPLICING`** | **0.123** | **14.8%** | Exon 25 splicing junction disruption proximity |
| **5. Chromatin / RNA-Seq** | **< 0.03** | **< 4.0%** | Negligible effect on mRNA abundance |

---

## 4. Molecular Mechanics: Loss-of-Function (LOF) Kinase Destruction

* **Buried Charge Insertion:** Val1110 is located in the hydrophobic interior of the JH1 catalytic core (C-terminal $\alpha\text{I}$ helix). Replacing a non-polar valine with an unshielded charged carboxylate group ($-\text{COO}^-$) causes catastrophic electrostatic repulsion ($\Delta\Delta G_{\text{elec}} = +1.42\text{ kcal/mol}$).
* **Consensus $\Delta\Delta G$:** Severely destabilizing ($+2.98\text{ kcal/mol}$), causing catalytic cleft distortion and complete enzymatic inactivation (Loss-of-Function).
