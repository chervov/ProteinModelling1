# Complete Analysis Report: JAK2 L805I & AlphaGenome Variant Impact (AVI)

## 1. Variant Identification & Mapping

| Field | Value |
| :--- | :--- |
| **Gene Symbol** | `JAK2` (Janus kinase 2, Ensembl: `ENSG00000096968`) |
| **Protein Accession** | [UniProt: O60674](https://www.uniprot.org/uniprotkb/O60674) (1,132 aa) |
| **Primary Transcript** | `ENST00000381652.4` / `NM_004972.4` |
| **Protein Mutation** | `p.Leu805Ile` (`L805I`) |
| **Coding Change** | `c.2413C>A` (Exon 19) |
| **Genomic Coordinate** | `chr9:5080662:C>A` (GRCh38, forward strand) |
| **Residue Change** | Leucine $\to$ Isoleucine (constitutional hydrophobic isomer) |
| **Domain** | **JH2-JH1 Inter-Domain Linker** (Exon 19) |
| **Cytogenetic Locus** | 9p24.1 |

---

## 2. AlphaGenome Variant Impact (AVI) Results: `JAK2 L805I`

| Metric | Computed Value | Genome-Wide Context |
| :--- | :--- | :--- |
| **AVI Phred Score** | **23.02** | **High Impact (Constraint)** ($\ge 20$ indicates top 1% impact genome-wide) |
| **Calibrated Quantile** | **0.99501** | More impactful than **99.50%** of all genome-wide SNVs |
| **Top Percentile** | **Top 0.499%** | Ranked in the **top 1 in ~200** of all variants across the human genome |
| **Raw Model Score** | **0.8100** | Strong positive functional constraint |

---

## 3. What is Driving the Score? (Feature Attribution Breakdown)

| Biological Modality | Feature Importance Weight | % Contribution | Role in Driving the Score |
| :--- | :--- | :--- | :--- |
| **1. `CACTUS_241_WAY`** | **0.531** | **62.2%** | **Dominant Driver:** Deep mammalian evolutionary constraint across 241 species |
| **2. `PHASTCONS_470_WAY`** | **0.148** | **17.3%** | Deep vertebrate evolutionary sequence constraint across 470 species |
| **3. `ALPHAMISSENSE`** | **0.119** | **14.0%** | Low structural impact (conservative isomer exchange, benign) |
| **4. `MERGED_SPLICING`** | **0.038** | **4.4%** | Minor background junction variation |

---

## 4. Multi-Predictor Protein Pathogenicity & Biophysical Assessment

| Predictor | Score / Value | Classification | Interpretation |
| :--- | :--- | :--- | :--- |
| **AlphaGenome (AVI)** | **Phred 23.02** | Top 0.50% | High score driven by cross-species mammalian conservation |
| **AlphaMissense** | **0.119** | **Likely Benign** | Conservative leucine-to-isoleucine isomer exchange |
| **FoldX $\Delta\Delta G$** | **$+0.78\text{ kcal/mol}$** | **Mildly Destabilizing / Tolerated** | Well below loss-of-function threshold ($<1.5\text{ kcal/mol}$) |
| **ClinVar** | *Unreported / VUS* | **VUS Leaning Benign** | Tolerated linker polymorphism |
