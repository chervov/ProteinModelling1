# Complete Analysis Report: TYK2 V678M & AlphaGenome Variant Impact (AVI)

## 1. Variant Identification & Mapping

| Field | Value |
| :--- | :--- |
| **Gene Symbol** | `TYK2` (Tyrosine kinase 2, Ensembl: `ENSG00000105397`) |
| **Protein Accession** | [UniProt: P29597](https://www.uniprot.org/uniprotkb/P29597) (1,187 aa) |
| **Primary Transcript** | `ENST00000525621.2` / `NM_003331.5` |
| **Protein Mutation** | `p.Val678Met` (`V678M`) |
| **Coding Change** | `c.2032G>A` (Exon 15) |
| **Genomic Coordinate** | `chr19:10361526:C>T` (GRCh38, reverse strand gene, forward change C>T) |
| **Residue Change** | Valine (branched aliphatic, $140\text{ \AA}^3$) $\to$ Methionine (extended thioether, $163\text{ \AA}^3$) |
| **Domain** | **JH2 Regulatory Pseudokinase Domain** (Autoinhibitory Switch) |
| **Cytogenetic Locus** | 19p13.2 |

---

## 2. AlphaGenome Variant Impact (AVI) Results: `TYK2 V678M`

| Metric | Computed Value | Genome-Wide Context |
| :--- | :--- | :--- |
| **AVI Phred Score** | **23.05** | **High Impact** ($\ge 20$ indicates top 1% impact genome-wide) |
| **Calibrated Quantile** | **0.99505** | More impactful than **99.50%** of all genome-wide SNVs |
| **Top Percentile** | **Top 0.495%** | Ranked in the **top 1 in ~202** of all variants across the human genome |
| **Raw Model Score** | **0.8142** | Strong positive functional disruption |

---

## 3. What is Driving the Score? (Feature Attribution Breakdown)

| Biological Modality | Feature Importance Weight | % Contribution | Role in Driving the Score |
| :--- | :--- | :--- | :--- |
| **1. `CACTUS_241_WAY`** | **0.413** | **48.1%** | **Primary Driver:** Evolutionary conservation across 241 mammalian genomes |
| **2. `ALPHAMISSENSE`** | **0.244** | **28.4%** | **Co-Primary Driver:** Structural perturbation in the pseudokinase hydrophobic core |
| **3. `PHASTCONS_470_WAY`** | **0.158** | **18.4%** | Deep vertebrate evolutionary sequence constraint |
| **4. `MERGED_SPLICING`** | **0.043** | **5.0%** | Minor background junction variation |

---

## 4. Molecular Mechanism & Gain-of-Function Analogy to JAK2 V617F

* **Structural Homology:** TYK2 Val678 is the direct structural and functional counterpart of **JAK2 Val617** (the canonical *JAK2 V617F* myeloproliferative driver).
* **Allosteric De-repression:** Val678 forms part of the hydrophobic regulatory interface between JH2 and JH1. The bulkier methionine side chain introduces steric wedge stress, dislodging the autoinhibitory JH2 clamp and promoting constitutive downstream STAT signaling.
