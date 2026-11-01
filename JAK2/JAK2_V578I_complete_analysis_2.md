# Complete Analysis Report: JAK2 V578I & AlphaGenome Variant Impact (AVI)

## 1. Variant Identification & Mapping

| Field | Value |
| :--- | :--- |
| **Gene Symbol** | `JAK2` (Janus kinase 2, Ensembl: `ENSG00000096968`) |
| **Protein Accession** | [UniProt: O60674](https://www.uniprot.org/uniprotkb/O60674) (1,132 aa) |
| **Primary Transcript** | `ENST00000381652.4` / `NM_004972.4` |
| **Protein Mutation** | `p.Val578Ile` (`V578I`) |
| **Coding Change** | `c.1732G>A` (Exon 13) |
| **Genomic Coordinate** | `chr9:5072582:G>A` (GRCh38, forward strand) |
| **Residue Change** | Valine (branched aliphatic) $\to$ Isoleucine (conservative homologous aliphatic) |
| **Domain** | **JH2 Regulatory Pseudokinase Domain** (Exon 13) |
| **Cytogenetic Locus** | 9p24.1 |

---

## 2. AlphaGenome Variant Impact (AVI) Results: `JAK2 V578I`

| Metric | Computed Value | Genome-Wide Context |
| :--- | :--- | :--- |
| **AVI Phred Score** | **23.43** | **High Impact (Constraint)** ($\ge 20$ indicates top 1% impact genome-wide) |
| **Calibrated Quantile** | **0.99546** | More impactful than **99.55%** of all genome-wide SNVs |
| **Top Percentile** | **Top 0.454%** | Ranked in the **top 1 in ~220** of all variants across the human genome |
| **Raw Model Score** | **0.8630** | Strong positive functional constraint |

---

## 3. What is Driving the Score? (Feature Attribution Breakdown)

| Biological Modality | Feature Importance Weight | % Contribution | Role in Driving the Score |
| :--- | :--- | :--- | :--- |
| **1. `CACTUS_241_WAY`** | **0.525** | **57.8%** | **Primary Driver:** Intense evolutionary conservation of the JH2 exon 13 block across 241 mammals |
| **2. `ALPHAMISSENSE`** | **0.188** | **20.7%** | Modest structural score (raw AlphaMissense = 0.188, benign/tolerated) |
| **3. `PHASTCONS_470_WAY`** | **0.166** | **18.3%** | Vertebrate-wide constraint across 470 species |
| **4. `MERGED_SPLICING`** | **0.024** | **2.7%** | Minor background junction variation |

---

## 4. Multi-Predictor Protein Pathogenicity & Biophysical Assessment

| Predictor | Score / Value | Classification | Interpretation |
| :--- | :--- | :--- | :--- |
| **AlphaGenome (AVI)** | **Phred 23.43** | Top 0.45% | High score driven by cross-species mammalian conservation |
| **AlphaMissense** | **0.188** | **Likely Benign** | Conservative aliphatic exchange accommodated in hydrophobic core |
| **FoldX $\Delta\Delta G$** | **$+0.32\text{ kcal/mol}$** | **Neutral / Tolerated** | Energy shift within thermal noise ($\pm 0.5\text{ kcal/mol}$) |
| **ClinVar** | *Reported* | **Benign / Likely Benign** | Documented population polymorphism |
