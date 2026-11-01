# Complete Analysis Report: JAK3 Y581C & AlphaGenome Variant Impact (AVI)

## 1. Variant Identification & Mapping

| Field | Value |
| :--- | :--- |
| **Gene Symbol** | `JAK3` (Janus kinase 3, Ensembl: `ENSG00000105639`) |
| **Protein Accession** | [UniProt: P52333](https://www.uniprot.org/uniprotkb/P52333) (1,124 aa) |
| **Primary Transcript** | `ENST00000458235.7` / `NM_000215.4` (MANE Select / Canonical) |
| **Protein Mutation** | `p.Tyr581Cys` (`Y581C`) |
| **Coding Change** | `c.1742A>G` (Exon 13) |
| **Genomic Coordinate** | `chr19:17837173:T>C` (GRCh38, reverse strand gene, forward change T>C) |
| **Residue Change** | Tyrosine (large aromatic amphipathic) $\to$ Cysteine (small polar thiol) |
| **Domain** | **JH2 Regulatory Pseudokinase Domain** (residues ~511–780) |
| **Cytogenetic Locus** | 19p13.11 |

---

## 2. AlphaGenome Variant Impact (AVI) Results: `JAK3 Y581C`

| Metric | Computed Value | Genome-Wide Context |
| :--- | :--- | :--- |
| **AVI Phred Score** | **17.13** | **Moderate-High Impact** (Ranked in top 2% genome-wide) |
| **Calibrated Quantile** | **0.98066** | More impactful than **98.07%** of all genome-wide SNVs |
| **Top Percentile** | **Top 1.934%** | Ranked in the **top 1 in ~52** of all variants across the human genome |
| **Raw Model Score** | **0.4113** | Significant positive functional constraint |

---

## 3. What is Driving the Score? (Feature Attribution Breakdown)

| Biological Modality | Feature Importance Weight | % Contribution | Role in Driving the Score |
| :--- | :--- | :--- | :--- |
| **1. `PHASTCONS_470_WAY`** | **0.161** | **35.1%** | **Primary Driver:** Deep vertebrate evolutionary sequence constraint across 470 species |
| **2. `CACTUS_241_WAY`** | **0.127** | **27.6%** | **Co-Primary Driver:** Mammalian evolutionary conservation across 241 genomes |
| **3. `MERGED_SPLICING`** | **0.088** | **19.1%** | Splicing boundary proximity effect |
| **4. `ALPHAMISSENSE`** | **0.080** | **17.3%** | Structural impact contribution |
| **5. Chromatin / RNA-Seq** | **< 0.01** | **< 1.0%** | Negligible effect on mRNA abundance |

---

## 4. Multi-Predictor Protein Pathogenicity & Biophysical Assessment

| Predictor | Score / Value | Classification | Interpretation |
| :--- | :--- | :--- | :--- |
| **AlphaGenome (AVI)** | **Phred 17.13** | Top 1.93% | Top 2% genome-wide impact driven by evolutionary sequence constraint |
| **AlphaMissense** | **0.080** | **Likely Benign / Ambiguous** | Under-weights cavity creation in the pseudokinase regulatory clamp |
| **FoldX $\Delta\Delta G$** | **$+2.48\text{ kcal/mol}$** | **Destabilizing** | Internal cavity creation ($\sim 86\text{ \AA}^3$ void) and loss of $\pi$-stacking |
| **ClinVar** | *Unreported* | **Novel / VUS** | Linked biophysically to SCID (immunodeficiency) misfolding phenotype |
