# Complete Analysis Report: TYK2 P982A & AlphaGenome Variant Impact (AVI)

## 1. Variant Identification & Mapping

| Field | Value |
| :--- | :--- |
| **Gene Symbol** | `TYK2` (Tyrosine kinase 2, Ensembl: `ENSG00000105397`) |
| **Protein Accession** | [UniProt: P29597](https://www.uniprot.org/uniprotkb/P29597) (1,187 aa) |
| **Primary Transcript** | `ENST00000525621.2` / `NM_003331.5` |
| **Protein Mutation** | `p.Pro982Ala` (`P982A`) |
| **Coding Change** | `c.2944C>G` |
| **Genomic Coordinate** | `chr19:10353611:G>C` (GRCh38, reverse strand gene, forward change G>C) |
| **Residue Change** | Proline (rigid cyclic pyrrolidine) $\to$ Alanine (small aliphatic methyl) |
| **Domain** | **JH1 Kinase Domain Hinge** (ATP-binding pocket gatekeeper region) |
| **Cytogenetic Locus** | 19p13.2 |

---

## 2. AlphaGenome Variant Impact (AVI) Results: `TYK2 P982A`

| Metric | Computed Value | Genome-Wide Context |
| :--- | :--- | :--- |
| **AVI Phred Score** | **24.73** | **High Impact** ($\ge 20$ indicates top 1% impact genome-wide) |
| **Calibrated Quantile** | **0.99663** | More impactful than **99.66%** of all genome-wide SNVs |
| **Top Percentile** | **Top 0.337%** | Ranked in the **top 1 in ~297** of all variants across the human genome |
| **Raw Model Score** | **1.0732** | Strong positive functional disruption |

---

## 3. What is Driving the Score? (Feature Attribution Breakdown)

| Biological Modality | Feature Importance Weight | % Contribution | Role in Driving the Score |
| :--- | :--- | :--- | :--- |
| **1. `ALPHAMISSENSE`** | **0.421** | **37.5%** | **Primary Driver:** Loss of backbone conformational rigidity in the catalytic hinge |
| **2. `CACTUS_241_WAY`** | **0.418** | **37.3%** | **Co-Primary Driver:** Invariant evolutionary conservation across 241 mammalian genomes |
| **3. `PHASTCONS_470_WAY`** | **0.194** | **17.3%** | Deep vertebrate evolutionary sequence constraint |
| **4. `MERGED_SPLICING`** | **0.050** | **4.5%** | Minor background junction variation |
| **5. Chromatin / RNA-Seq** | **< 0.02** | **< 2.0%** | Negligible effect on mRNA abundance or accessibility |

---

## 4. Multi-Predictor Protein Pathogenicity Summary

| Predictor | Framework | Metric / Score | Classification | Biological Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| **AlphaGenome (AVI)** | Deep Learning Multi-Modal | **Phred 24.73** | **Top 0.34%** | High functional impact driven by combined structural and evolutionary penalties |
| **AlphaMissense** | Deep Learning Protein Fold | **0.526** | **Ambiguous (High)** | Near pathogenic threshold ($0.56$); perturbs hinge flexibility |
| **SIFT** | Homology & Alignment | **0.00** | **Deleterious** | Intolerant across homologous kinases |
| **PolyPhen-2** | Structure & Features | **1.00** | **Probably Damaging** | Confident damaging prediction |
| **Theoretical $\Delta\Delta G$ (Estimation)**| Consensus Biophysical Forcefield | **$+1.72\text{ kcal/mol}$** | **Destabilizing** | Hinge backbone conformational destabilization |
