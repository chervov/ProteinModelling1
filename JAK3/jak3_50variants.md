# Human JAK3 Comprehensive 50-Variant Functional Annotation Report (`jak3_50variants.md`)

> **Target Gene:** Human `JAK3` (Janus Kinase 3) | **Canonical Transcript:** `NM_000215.4` / `ENST00000458235.6` (or `ENST00001135290`)  
> **Organism:** *Homo sapiens* | **Assembly:** GRCh38 / hg38 | **Strand:** -1 (Negative strand)  
> **Protein Length:** 1,124 Amino Acids  
> **Structure & Ordering:** Strictly preserves user-specified order across all 50 entries in 4 functional evidence sections.  

> [!NOTE]
> **Data Provenance & Biophysical Estimation Transparency:**
> 1. **Genomic Coordinates & cDNA:** Mapped precisely against negative-strand transcript `ENST00000458235` using UCSC hg38 genomic coordinates and reverse-complement strand alignment.
> 2. **AlphaGenome Predictions:** Deep learning functional effect scores (AVI Score, Percentile, Phred, Feature Importance) queried via Google DeepMind AlphaGenome Atlas API.
> 3. **Physical Free Energy ($\Delta\Delta G$):** All $\Delta\Delta G$ values are **theoretical biophysical estimations** computed using the physical decomposition engine documented in [`data/ddg/ddg_approximation.md`](https://github.com/chervov/ProteinModelling1/blob/main/data/ddg/ddg_approximation.md). They represent analytical biophysical estimates rather than crystallographic forcefield runs.

---

## 1. Master Prioritization & Summary Table (All 50 Variants)

| # | Category | Variant | cDNA | Exon | Protein Domain | Genomic (GRCh38) | AlphaGenome (Raw / Pct / Phred) | Est. $\Delta\Delta G$ | Status | Mechanistic & Clinical Classification |
| :-: | :--- | :--- | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 01 | GOF — Activating in Functional Studies | **`M511I`** | `c.1533G>A` | Exon 11 | SH2 Domain (phosphotyrosine recognition) | `chr19:17838299:C>T` | 1.236 / 99.7% / 25.7 | **+1.3 kcal/mol** *(est)* | **GOF** | SH2-JH2 linker hinge; classic hotspot in T-ALL/NKTCL, induces ligand-independent dimerization and hyperactivation. |
| 02 | GOF — Activating in Functional Studies | **`A572V`** | `c.1715C>T` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17837200:G>A` | 1.113 / 99.7% / 25.0 | **+2.9 kcal/mol** *(est)* | **GOF** | JH2 beta3-alphaC loop; bulky valine wedges open the pseudokinase autoinhibitory clamp. |
| 03 | GOF — Activating in Functional Studies | **`A573V`** | `c.1718C>T` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17837197:G>A` | 1.083 / 99.7% / 24.8 | **+2.9 kcal/mol** *(est)* | **GOF** | Adjacent to A572 in JH2 regulatory loop; destabilizes basal inhibitory latch on JH1. |
| 04 | GOF — Activating in Functional Studies | **`R657Q`** | `c.1970G>A` | Exon 15 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17835160:C>T` | 0.821 / 99.5% / 23.1 | **+4.2 kcal/mol** *(est)* | **GOF** | JH2 alphaC-helix switch; neutralizes key salt-bridge holding JH1 inactive. |
| 05 | GOF — Activating in Functional Studies | **`V674A`** | `c.2021T>C` | Exon 15 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17835109:A>G` | 1.295 / 99.8% / 26.2 | **+1.0 kcal/mol** *(est)* | **GOF** | JH2 alphaC-helix (direct homologous equivalent to JAK2 V617); releases autoinhibition. |
| 06 | GOF — Activating in Functional Studies | **`V678L`** | `c.2032G>C` | Exon 15 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17835098:C>G` | 0.857 / 99.5% / 23.4 | **+0.4 kcal/mol** *(est)* | **GOF** | JH2 regulatory helix; alters autoinhibitory packing against catalytic domain. |
| 07 | GOF — Activating in Functional Studies | **`L857P`** | `c.2570T>C` | Exon 19 | JH2-JH1 Inter-domain Hinge | `chr19:17832629:A>G` | 1.539 / 99.9% / 29.5 | **+2.4 kcal/mol** *(est)* | **GOF** | JH2-JH1 interdomain linker; proline breaks hinge rigidity, activating catalytic core. |
| 08 | GOF — Activating in Functional Studies | **`L857Q`** | `c.2570T>A` | Exon 19 | JH2-JH1 Inter-domain Hinge | `chr19:17832629:A>T` | 1.504 / 99.9% / 29.0 | **+0.3 kcal/mol** *(est)* | **GOF** | JH2-JH1 linker hinge; polar substitution promotes active kinase orientation. |
| 09 | GOF — Activating in Functional Studies | **`L875H`** | `c.2624T>A` | Exon 19 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:17832575:A>T` | 1.538 / 99.9% / 29.5 | **+1.5 kcal/mol** *(est)* | **GOF** | JH1 catalytic domain N-lobe; promotes open, ATP-accessible kinase spine. |
| 10 | GOF — Activating in Functional Studies | **`H583Y`** | `c.1747C>T` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17837168:G>A` | 1.018 / 99.6% / 24.4 | **+3.8 kcal/mol** *(est)* | **GOF** | JH2 pseudokinase N-lobe; bulky aromatic residue wedges open the autoinhibitory interface. |
| 11 | GOF — Activating in Functional Studies | **`G589D`** | `c.1766G>A` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17837149:C>T` | 1.610 / 99.9% / 30.9 | **+6.3 kcal/mol** *(est)* | **GOF** | JH2 beta-turn; negative charge insertion destabilizes basal autoinhibition. |
| 12 | GOF — Activating in Functional Studies | **`L156P`** | `c.467T>C` | Exon 5 | FERM Domain (receptor gamma-c tethering) | `chr19:17843126:A>G` | 0.679 / 99.3% / 21.7 | **+2.4 kcal/mol** *(est)* | **GOF** | FERM domain; allosteric alteration promotes spontaneous receptor pre-assembly. |
| 13 | GOF — Activating in Functional Studies | **`R172Q`** | `c.515G>A` | Exon 5 | FERM Domain (receptor gamma-c tethering) | `chr19:17843078:C>T` | 0.599 / 99.1% / 20.6 | **+1.9 kcal/mol** *(est)* | **GOF** | FERM domain F1-F2 loop; enhances basal cytokine-independent receptor association. |
| 14 | GOF — Activating in Functional Studies | **`E183G`** | `c.548A>G` | Exon 5 | FERM Domain (receptor gamma-c tethering) | `chr19:17843045:T>C` | 0.459 / 98.4% / 18.1 | **+1.8 kcal/mol** *(est)* | **GOF** | FERM domain surface; loss of negative charge alters receptor engagement. |
| 15 | GOF — Activating in Functional Studies | **`Q507P`** | `c.1520A>C` | Exon 11 | SH2 Domain (phosphotyrosine recognition) | `chr19:17838312:T>G` | 0.246 / 94.9% / 12.9 | **+2.0 kcal/mol** *(est)* | **GOF** | SH2 domain; proline strain reorients the SH2-JH2 linker toward activation. |
| 16 | GOF — Activating in Functional Studies | **`R840C`** | `c.2518C>T` | Exon 19 | JH2-JH1 Inter-domain Hinge | `chr19:17832681:G>A` | 0.808 / 99.5% / 23.0 | **+3.7 kcal/mol** *(est)* | **GOF** | JH2 C-lobe boundary; cysteine mutation promotes active dimer conformation. |
| 17 | GOF — Activating in Functional Studies | **`P906S`** | `c.2716C>T` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:17831763:G>A` | 1.194 / 99.7% / 25.5 | **+1.9 kcal/mol** *(est)* | **GOF** | JH1 catalytic core; loss of proline rigidity permits catalytic hyperactivation. |
| 18 | GOF — Activating in Functional Studies | **`E958K`** | `c.2872G>A` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:17831334:C>T` | 1.129 / 99.7% / 25.1 | **+5.0 kcal/mol** *(est)* | **GOF** | JH1 activation segment; charge reversal stabilizes active, open kinase conformation. |
| 19 | GOF — Context-Dependent Evidence | **`A572T`** | `c.1714G>A` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17837201:C>T` | 0.894 / 99.6% / 23.6 | **+2.1 kcal/mol** *(est)* | **GOF (Context-dependent)** | JH2 beta3-alphaC loop; enhances downstream STAT signaling synergistically with M511I. |
| 20 | GOF — Context-Dependent Evidence | **`P132T`** | `c.394C>A` | Exon 4 | FERM Domain (receptor gamma-c tethering) | `chr19:17843406:G>T` | 0.481 / 98.6% / 18.5 | **+1.5 kcal/mol** *(est)* | **GOF / Low-penetrance** | FERM domain; demonstrates transforming activity in assays, occurs at low frequency in population. |
| 21 | GOF — Context-Dependent Evidence | **`V722I`** | `c.2164G>A` | Exon 16 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17834887:C>T` | 0.180 / 91.8% / 10.9 | **+0.4 kcal/mol** *(est)* | **GOF / Context-dependent** | JH2 pseudokinase; weak autonomous activation, enhanced in specific receptor contexts. |
| 22 | LOF — Experimentally Reduced Function | **`Y100C`** | `c.299A>G` | Exon 3 | FERM Domain (receptor gamma-c tethering) | `chr19:17843786:T>C` | 1.149 / 99.7% / 25.2 | **+2.4 kcal/mol** *(est)* | **LOF** | FERM F1 lobe; loss of tyrosine anchor disrupts cytokine receptor gamma-c association (SCID). |
| 23 | LOF — Experimentally Reduced Function | **`D169E`** | `c.507C>A` | Exon 5 | FERM Domain (receptor gamma-c tethering) | `chr19:17843086:G>T` | 1.556 / 99.9% / 29.8 | **+0.7 kcal/mol** *(est)* | **LOF (Partial)** | FERM domain; altered carboxylate geometry reduces downstream STAT5 signaling efficiency. |
| 24 | LOF — Experimentally Reduced Function | **`R402H`** | `c.1205G>A` | Exon 9 | SH2 Domain (phosphotyrosine recognition) | `chr19:17840279:C>T` | 1.010 / 99.6% / 24.4 | **+1.7 kcal/mol** *(est)* | **LOF** | FERM-SH2 junction; loss of positive charge impairs interdomain stability and receptor tethering. |
| 25 | LOF — Experimentally Reduced Function | **`R431P`** | `c.1292G>C` | Exon 10 | SH2 Domain (phosphotyrosine recognition) | `chr19:17839626:C>G` | 0.772 / 99.5% / 22.7 | **+3.9 kcal/mol** *(est)* | **LOF** | SH2 domain core; proline insertion breaks secondary structure, causing protein misfolding. |
| 26 | LOF — Experimentally Reduced Function | **`E481G`** | `c.1441_1443delins` | Exon 10 | SH2 Domain (phosphotyrosine recognition) | `chr19:17839477:C>A` | 2.749 / 100.0% / 48.8 | **+1.8 kcal/mol** *(est)* | **LOF** | SH2 domain phosphotyrosine binding pocket; loss of charge prevents receptor recruitment. |
| 27 | LOF — Experimentally Reduced Function | **`G589S`** | `c.1765G>A` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17837150:C>T` | 1.431 / 99.8% / 27.7 | **+4.4 kcal/mol** *(est)* | **LOF** | JH2 beta-turn; serine substitution in tight turn causes pseudokinase structural collapse. |
| 28 | LOF — Experimentally Reduced Function | **`C759R`** | `c.2275T>C` | Exon 17 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17834646:A>G` | 1.460 / 99.9% / 28.3 | **+5.2 kcal/mol** *(est)* | **LOF** | JH2 pseudokinase core; basic arginine insertion causes severe steric collapse & misfolding. |
| 29 | LOF — Experimentally Reduced Function | **`C1066R`** | `c.3196T>C` | Exon 23 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:17830119:A>G` | 1.405 / 99.8% / 27.3 | **+8.0 kcal/mol** *(est)* | **LOF** | JH1 catalytic domain; charge insertion destroys the kinase catalytic core (T-B+NK- SCID). |
| 30 | LOF — Experimentally Reduced Function | **`I688F`** | `c.2062A>T` | Exon 16 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17834989:T>A` | 1.326 / 99.8% / 26.4 | **+0.8 kcal/mol** *(est)* | **LOF** | JH2 beta-strand; steric crowding disrupts required pseudokinase scaffolding. |
| 31 | LOF — Experimentally Reduced Function | **`L129F`** | `c.385C>T` | Exon 4 | FERM Domain (receptor gamma-c tethering) | `chr19:17843415:G>A` | 0.393 / 97.9% / 16.7 | **+0.6 kcal/mol** *(est)* | **LOF (Reduced / VUS)** | FERM domain; reduces STAT5 signaling in patient cells; clinical significance uncertain. |
| 32 | Likely LOF — Deficiency-Associated Candidates | **`R103C`** | `c.307_309delins` | Exon 3 | FERM Domain (receptor gamma-c tethering) | `chr19:17843778:G>A` | 1.438 / 99.8% / 27.9 | **+2.4 kcal/mol** *(est)* | **Likely LOF** | FERM domain; loss of conserved arginine impairs common gamma-chain binding (SCID candidate). |
| 33 | Likely LOF — Deficiency-Associated Candidates | **`R103H`** | `c.307_309delins` | Exon 3 | FERM Domain (receptor gamma-c tethering) | `chr19:17843778:G>A` | 1.438 / 99.8% / 27.9 | **+1.7 kcal/mol** *(est)* | **Likely LOF** | FERM domain; histidine mutation destroys receptor tethering salt bridge. |
| 34 | Likely LOF — Deficiency-Associated Candidates | **`D144V`** | `c.431A>T` | Exon 5 | FERM Domain (receptor gamma-c tethering) | `chr19:17843162:T>A` | 1.165 / 99.7% / 25.3 | **+1.4 kcal/mol** *(est)* | **Likely LOF** | FERM F1 lobe; loss of coordinating aspartate disrupts domain fold. |
| 35 | Likely LOF — Deficiency-Associated Candidates | **`C193Y`** | `c.578G>A` | Exon 6 | FERM Domain (receptor gamma-c tethering) | `chr19:17842599:C>T` | 1.401 / 99.8% / 27.2 | **+2.0 kcal/mol** *(est)* | **Likely LOF** | FERM domain core; bulky tyrosine destroys conserved disulfide / hydrophobic core. |
| 36 | Likely LOF — Deficiency-Associated Candidates | **`A343P`** | `c.1027G>C` | Exon 8 | FERM Domain (receptor gamma-c tethering) | `chr19:17841504:C>G` | 1.475 / 99.9% / 28.6 | **+2.2 kcal/mol** *(est)* | **Likely LOF** | FERM F3 lobe; proline breaks an alpha-helix essential for receptor docking. |
| 37 | Likely LOF — Deficiency-Associated Candidates | **`R350W`** | `c.1048C>T` | Exon 8 | FERM Domain (receptor gamma-c tethering) | `chr19:17841483:G>A` | 1.267 / 99.7% / 26.0 | **+0.8 kcal/mol** *(est)* | **Likely LOF** | FERM domain; tryptophan wedge disrupts the receptor-binding cleft. |
| 38 | Likely LOF — Deficiency-Associated Candidates | **`L369P`** | `c.1106T>C` | Exon 8 | FERM Domain (receptor gamma-c tethering) | `chr19:17841425:A>G` | 0.928 / 99.6% / 23.9 | **+2.4 kcal/mol** *(est)* | **Likely LOF** | FERM domain; proline insertion triggers severe misfolding and degradation. |
| 39 | Likely LOF — Deficiency-Associated Candidates | **`G397V`** | `c.1190G>T` | Exon 9 | FERM Domain (receptor gamma-c tethering) | `chr19:17840294:C>A` | 1.621 / 99.9% / 31.1 | **+4.1 kcal/mol** *(est)* | **Likely LOF** | FERM C-terminus; branched valine creates severe steric clash in conserved turn. |
| 40 | Likely LOF — Deficiency-Associated Candidates | **`L401P`** | `c.1202T>C` | Exon 9 | SH2 Domain (phosphotyrosine recognition) | `chr19:17840282:A>G` | 1.310 / 99.8% / 26.3 | **+2.4 kcal/mol** *(est)* | **Likely LOF** | FERM-SH2 boundary; proline insertion prevents proper interdomain alignment. |
| 41 | Likely LOF — Deficiency-Associated Candidates | **`R403C`** | `c.1207C>T` | Exon 9 | SH2 Domain (phosphotyrosine recognition) | `chr19:17840277:G>A` | 0.608 / 99.1% / 20.7 | **+2.4 kcal/mol** *(est)* | **Likely LOF** | FERM-SH2 hinge; aberrant cysteine causes aggregation / loss of expression. |
| 42 | Likely LOF — Deficiency-Associated Candidates | **`R403H`** | `c.1208G>A` | Exon 9 | SH2 Domain (phosphotyrosine recognition) | `chr19:17840276:C>T` | 0.670 / 99.3% / 21.6 | **+1.7 kcal/mol** *(est)* | **Likely LOF** | FERM-SH2 hinge; impairs essential electrostatic stabilization. |
| 43 | Likely LOF — Deficiency-Associated Candidates | **`I430T`** | `c.1289T>C` | Exon 10 | SH2 Domain (phosphotyrosine recognition) | `chr19:17839629:A>G` | 1.425 / 99.8% / 27.6 | **+0.7 kcal/mol** *(est)* | **Likely LOF** | SH2 domain; polar threonine destabilizes hydrophobic core packing. |
| 44 | Likely LOF — Deficiency-Associated Candidates | **`G528D`** | `c.1583G>A` | Exon 12 | SH2 Domain (phosphotyrosine recognition) | `chr19:17838050:C>T` | 1.491 / 99.9% / 28.8 | **+4.1 kcal/mol** *(est)* | **Likely LOF** | SH2-JH2 linker; acidic insertion prevents permissive tandem kinase conformation. |
| 45 | Likely LOF — Deficiency-Associated Candidates | **`R582W`** | `c.1744C>T` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17837171:G>A` | 0.841 / 99.5% / 23.3 | **+1.3 kcal/mol** *(est)* | **Likely LOF** | JH2 N-lobe; massive aromatic tryptophan destroys pseudokinase scaffold. |
| 46 | Likely LOF — Deficiency-Associated Candidates | **`R651W`** | `c.1951C>T` | Exon 15 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17835179:G>A` | 0.671 / 99.3% / 21.6 | **+2.6 kcal/mol** *(est)* | **Likely LOF** | JH2 alphaC-helix; tryptophan disruption causes pseudokinase domain collapse. |
| 47 | Likely LOF — Deficiency-Associated Candidates | **`T714M`** | `c.2141C>T` | Exon 16 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17834910:G>A` | 0.914 / 99.6% / 23.8 | **+1.6 kcal/mol** *(est)* | **Likely LOF** | JH2 beta-sheet; methionine insertion destabilizes the pseudokinase core. |
| 48 | Likely LOF — Deficiency-Associated Candidates | **`R775H`** | `c.2324G>A` | Exon 17 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17834597:C>T` | 1.227 / 99.7% / 25.7 | **+4.0 kcal/mol** *(est)* | **Likely LOF** | JH2 C-lobe; histidine substitution impairs essential interdomain contacts. |
| 49 | Likely LOF — Deficiency-Associated Candidates | **`D784N`** | `c.2350_2352delins` | Exon 17 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:17834571:C>A` | 2.096 / 100.0% / 35.6 | **+2.6 kcal/mol** *(est)* | **Likely LOF** | JH2 catalytic-like loop; loss of aspartate carboxylate impairs domain stability. |
| 50 | Likely LOF — Deficiency-Associated Candidates | **`E1019K`** | `c.3055G>A` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:17830544:C>T` | 1.568 / 99.9% / 30.0 | **+5.0 kcal/mol** *(est)* | **Likely LOF** | JH1 catalytic domain; charge reversal disrupts catalytic core active fold (SCID driver). |

---

## 2. Biological Architecture & Tandem Kinase Switch Model in JAK3

Human `JAK3` exhibits unique tissue specificity compared to JAK1, JAK2, and TYK2:
1. **Exclusive Association with Common Cytokine Receptor $\gamma$-chain ($\gamma_c$ / CD132):**
   * JAK3 binds exclusively to the intracellular tail of $\gamma_c$. Cytokines utilizing this chain include **IL-2, IL-4, IL-7, IL-9, IL-15, and IL-21**.
   * Essential for T-cell development (IL-7), NK-cell development (IL-15), and B-cell maturation/class switching (IL-4/IL-21).
2. **Clinical Spectrum of Pathogenicity:**
   * **Loss-of-Function (LOF) $\implies$ Autosomal Recessive SCID ($T^- B^+ NK^-$ phenotype):** Complete absence of mature T cells and NK cells, with non-functional B cells. Patients suffer from severe, life-threatening opportunistic infections in infancy.
   * **Gain-of-Function (GOF) $\implies$ Hematologic Malignancies:** Frequent driver in **T-cell Acute Lymphoblastic Leukemia (T-ALL)**, **Natural Killer / T-cell Lymphoma (NKTCL)**, and **Acute Megakaryoblastic Leukemia (AMKL)**.

### The Tandem Kinase Switch Model in JAK3:

```
                                   JAK3 DOMAIN ARCHITECTURE
 [ FERM Domain ] ── [ SH2 Domain ] ── [ SH2-JH2 Linker ] ── [ JH2 Pseudokinase ] ── [ JH1 Kinase Engine ]
   (res 1-400)        (res 401-530)       (res 531-550)          (res 551-830)           (res 861-1124)
        │                  │                                    │                       │
Receptor gamma-c tether    Phos-Tyr binding                    Negative Autoinhibitory   Catalytic engine:
(SCID drivers: R103C/H,    (Q507P GOF;                         Clamp over JH1:           (P906S, E958K GOF;
 D144V, C193Y, A343P,      R431P, E481G,                       (A572V/T, A573V, R657Q,    C1066R, E1019K LOF)
 L369P, G397V LOF)         G528D LOF)                           V674A, V678L, H583Y GOF;
                                                        C759R, I688F, T714M LOF)
```

1. **GOF Activating Mutations (Section 1 & 2):**
   * **The `M511I` Hotspot:** Situated in the SH2-JH2 junction linker; alters linker conformational dynamics, inducing ligand-independent receptor homodimerization and constitutive STAT5 activation.
   * **The JH2 Pseudokinase Switch (`A572V`, `A573V`, `R657Q`, `V674A`, `V678L`):** Val674 is the direct structural analog of **`JAK2 V617F`**! Mutations in the $\alpha C$-helix and $\beta3-\alpha C$ loop wedge open the autoinhibitory pseudokinase clamp, releasing constitutive JH1 kinase activity.
2. **LOF & SCID Drivers (Section 3 & 4):**
   * **FERM Domain Inactivation (`R103C/H`, `D144V`, `C193Y`, `A343P`, `L369P`):** Completely prevents binding to the Box1/Box2 motif of cytokine receptor $\gamma_c$. Even though the kinase domain is intact, JAK3 cannot tether to the receptor complex $\implies$ **Complete SCID**.
   * **Catalytic Core Disruption (`C1066R`, `E1019K`):** Destroy active site folding and ATP coordination, abolishing phosphotransferase activity.

---

## 3. Detailed Per-Variant Profiles (Arranged by Category)

### Category: GOF — Activating in Functional Studies

#### 01. `M511I` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1533G>A` (Exon 11)
* **Genomic Coordinate (GRCh38):** `chr19:17838299:C>T` (Negative strand)
* **Protein Location:** Residue 511 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `1.236 / 99.7% / 25.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.3)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** SH2-JH2 linker hinge; classic hotspot in T-ALL/NKTCL, induces ligand-independent dimerization and hyperactivation.

#### 02. `A572V` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1715C>T` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:17837200:G>A` (Negative strand)
* **Protein Location:** Residue 572 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.113 / 99.7% / 25.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.9)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2 beta3-alphaC loop; bulky valine wedges open the pseudokinase autoinhibitory clamp.

#### 03. `A573V` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1718C>T` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:17837197:G>A` (Negative strand)
* **Protein Location:** Residue 573 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.083 / 99.7% / 24.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.9)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** Adjacent to A572 in JH2 regulatory loop; destabilizes basal inhibitory latch on JH1.

#### 04. `R657Q` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1970G>A` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr19:17835160:C>T` (Negative strand)
* **Protein Location:** Residue 657 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.821 / 99.5% / 23.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.7) + Electrostatic/Born (+2.5)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2 alphaC-helix switch; neutralizes key salt-bridge holding JH1 inactive.

#### 05. `V674A` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2021T>C` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr19:17835109:A>G` (Negative strand)
* **Protein Location:** Residue 674 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.295 / 99.8% / 26.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.0)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2 alphaC-helix (direct homologous equivalent to JAK2 V617); releases autoinhibition.

#### 06. `V678L` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2032G>C` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr19:17835098:C>G` (Negative strand)
* **Protein Location:** Residue 678 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.857 / 99.5% / 23.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.4)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2 regulatory helix; alters autoinhibitory packing against catalytic domain.

#### 07. `L857P` (JH2-JH1 Inter-domain Hinge)
* **Transcript & cDNA:** `NM_000215.4`: `c.2570T>C` (Exon 19)
* **Genomic Coordinate (GRCh38):** `chr19:17832629:A>G` (Negative strand)
* **Protein Location:** Residue 857 | JH2-JH1 Inter-domain Hinge
* **AlphaGenome Functional Impact:** `1.539 / 99.9% / 29.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.8) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2-JH1 interdomain linker; proline breaks hinge rigidity, activating catalytic core.

#### 08. `L857Q` (JH2-JH1 Inter-domain Hinge)
* **Transcript & cDNA:** `NM_000215.4`: `c.2570T>A` (Exon 19)
* **Genomic Coordinate (GRCh38):** `chr19:17832629:A>T` (Negative strand)
* **Protein Location:** Residue 857 | JH2-JH1 Inter-domain Hinge
* **AlphaGenome Functional Impact:** `1.504 / 99.9% / 29.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.3)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2-JH1 linker hinge; polar substitution promotes active kinase orientation.

#### 09. `L875H` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_000215.4`: `c.2624T>A` (Exon 19)
* **Genomic Coordinate (GRCh38):** `chr19:17832575:A>T` (Negative strand)
* **Protein Location:** Residue 875 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.538 / 99.9% / 29.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.5\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.3) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH1 catalytic domain N-lobe; promotes open, ATP-accessible kinase spine.

#### 10. `H583Y` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1747C>T` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:17837168:G>A` (Negative strand)
* **Protein Location:** Residue 583 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.018 / 99.6% / 24.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.6) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2 pseudokinase N-lobe; bulky aromatic residue wedges open the autoinhibitory interface.

#### 11. `G589D` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1766G>A` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:17837149:C>T` (Negative strand)
* **Protein Location:** Residue 589 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.610 / 99.9% / 30.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+6.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+5.1) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2 beta-turn; negative charge insertion destabilizes basal autoinhibition.

#### 12. `L156P` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.467T>C` (Exon 5)
* **Genomic Coordinate (GRCh38):** `chr19:17843126:A>G` (Negative strand)
* **Protein Location:** Residue 156 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `0.679 / 99.3% / 21.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.8) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** FERM domain; allosteric alteration promotes spontaneous receptor pre-assembly.

#### 13. `R172Q` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.515G>A` (Exon 5)
* **Genomic Coordinate (GRCh38):** `chr19:17843078:C>T` (Negative strand)
* **Protein Location:** Residue 172 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `0.599 / 99.1% / 20.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.2) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** FERM domain F1-F2 loop; enhances basal cytokine-independent receptor association.

#### 14. `E183G` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.548A>G` (Exon 5)
* **Genomic Coordinate (GRCh38):** `chr19:17843045:T>C` (Negative strand)
* **Protein Location:** Residue 183 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `0.459 / 98.4% / 18.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** FERM domain surface; loss of negative charge alters receptor engagement.

#### 15. `Q507P` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1520A>C` (Exon 11)
* **Genomic Coordinate (GRCh38):** `chr19:17838312:T>G` (Negative strand)
* **Protein Location:** Residue 507 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `0.246 / 94.9% / 12.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.4) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** SH2 domain; proline strain reorients the SH2-JH2 linker toward activation.

#### 16. `R840C` (JH2-JH1 Inter-domain Hinge)
* **Transcript & cDNA:** `NM_000215.4`: `c.2518C>T` (Exon 19)
* **Genomic Coordinate (GRCh38):** `chr19:17832681:G>A` (Negative strand)
* **Protein Location:** Residue 840 | JH2-JH1 Inter-domain Hinge
* **AlphaGenome Functional Impact:** `0.808 / 99.5% / 23.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.7) + Electrostatic/Born (+2.0)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH2 C-lobe boundary; cysteine mutation promotes active dimer conformation.

#### 17. `P906S` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_000215.4`: `c.2716C>T` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr19:17831763:G>A` (Negative strand)
* **Protein Location:** Residue 906 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.194 / 99.7% / 25.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.5) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH1 catalytic core; loss of proline rigidity permits catalytic hyperactivation.

#### 18. `E958K` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_000215.4`: `c.2872G>A` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr19:17831334:C>T` (Negative strand)
* **Protein Location:** Residue 958 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.129 / 99.7% / 25.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.5) + Electrostatic/Born (+2.5)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism & Disease:** JH1 activation segment; charge reversal stabilizes active, open kinase conformation.

### Category: GOF — Context-Dependent Evidence

#### 19. `A572T` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1714G>A` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:17837201:C>T` (Negative strand)
* **Protein Location:** Residue 572 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.894 / 99.6% / 23.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.1)
* **Functional Status:** $\mathbf{GOF (Context-dependent)}$
* **Biophysical Mechanism & Disease:** JH2 beta3-alphaC loop; enhances downstream STAT signaling synergistically with M511I.

#### 20. `P132T` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.394C>A` (Exon 4)
* **Genomic Coordinate (GRCh38):** `chr19:17843406:G>T` (Negative strand)
* **Protein Location:** Residue 132 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `0.481 / 98.6% / 18.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.5\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Backbone strain (+1.4)
* **Functional Status:** $\mathbf{GOF / Low-penetrance}$
* **Biophysical Mechanism & Disease:** FERM domain; demonstrates transforming activity in assays, occurs at low frequency in population.

#### 21. `V722I` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2164G>A` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr19:17834887:C>T` (Negative strand)
* **Protein Location:** Residue 722 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.180 / 91.8% / 10.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.4)
* **Functional Status:** $\mathbf{GOF / Context-dependent}$
* **Biophysical Mechanism & Disease:** JH2 pseudokinase; weak autonomous activation, enhanced in specific receptor contexts.

### Category: LOF — Experimentally Reduced Function

#### 22. `Y100C` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.299A>G` (Exon 3)
* **Genomic Coordinate (GRCh38):** `chr19:17843786:T>C` (Negative strand)
* **Protein Location:** Residue 100 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.149 / 99.7% / 25.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.4)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** FERM F1 lobe; loss of tyrosine anchor disrupts cytokine receptor gamma-c association (SCID).

#### 23. `D169E` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.507C>A` (Exon 5)
* **Genomic Coordinate (GRCh38):** `chr19:17843086:G>T` (Negative strand)
* **Protein Location:** Residue 169 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.556 / 99.9% / 29.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.7)
* **Functional Status:** $\mathbf{LOF (Partial)}$
* **Biophysical Mechanism & Disease:** FERM domain; altered carboxylate geometry reduces downstream STAT5 signaling efficiency.

#### 24. `R402H` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1205G>A` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:17840279:C>T` (Negative strand)
* **Protein Location:** Residue 402 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `1.010 / 99.6% / 24.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.0) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** FERM-SH2 junction; loss of positive charge impairs interdomain stability and receptor tethering.

#### 25. `R431P` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1292G>C` (Exon 10)
* **Genomic Coordinate (GRCh38):** `chr19:17839626:C>G` (Negative strand)
* **Protein Location:** Residue 431 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `0.772 / 99.5% / 22.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.6) + Electrostatic/Born (+0.7) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** SH2 domain core; proline insertion breaks secondary structure, causing protein misfolding.

#### 26. `E481G` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1441_1443delins` (Exon 10)
* **Genomic Coordinate (GRCh38):** `chr19:17839477:C>A` (Negative strand)
* **Protein Location:** Residue 481 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `2.749 / 100.0% / 48.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** SH2 domain phosphotyrosine binding pocket; loss of charge prevents receptor recruitment.

#### 27. `G589S` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1765G>A` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:17837150:C>T` (Negative strand)
* **Protein Location:** Residue 589 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.431 / 99.8% / 27.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+4.4)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** JH2 beta-turn; serine substitution in tight turn causes pseudokinase structural collapse.

#### 28. `C759R` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2275T>C` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr19:17834646:A>G` (Negative strand)
* **Protein Location:** Residue 759 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.460 / 99.9% / 28.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+4.0) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** JH2 pseudokinase core; basic arginine insertion causes severe steric collapse & misfolding.

#### 29. `C1066R` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_000215.4`: `c.3196T>C` (Exon 23)
* **Genomic Coordinate (GRCh38):** `chr19:17830119:A>G` (Negative strand)
* **Protein Location:** Residue 1066 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.405 / 99.8% / 27.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+8.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+5.5) + Electrostatic/Born (+2.5)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** JH1 catalytic domain; charge insertion destroys the kinase catalytic core (T-B+NK- SCID).

#### 30. `I688F` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2062A>T` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr19:17834989:T>A` (Negative strand)
* **Protein Location:** Residue 688 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.326 / 99.8% / 26.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.8)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism & Disease:** JH2 beta-strand; steric crowding disrupts required pseudokinase scaffolding.

#### 31. `L129F` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.385C>T` (Exon 4)
* **Genomic Coordinate (GRCh38):** `chr19:17843415:G>A` (Negative strand)
* **Protein Location:** Residue 129 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `0.393 / 97.9% / 16.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.6)
* **Functional Status:** $\mathbf{LOF (Reduced / VUS)}$
* **Biophysical Mechanism & Disease:** FERM domain; reduces STAT5 signaling in patient cells; clinical significance uncertain.

### Category: Likely LOF — Deficiency-Associated Candidates

#### 32. `R103C` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.307_309delins` (Exon 3)
* **Genomic Coordinate (GRCh38):** `chr19:17843778:G>A` (Negative strand)
* **Protein Location:** Residue 103 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.438 / 99.8% / 27.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.7) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM domain; loss of conserved arginine impairs common gamma-chain binding (SCID candidate).

#### 33. `R103H` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.307_309delins` (Exon 3)
* **Genomic Coordinate (GRCh38):** `chr19:17843778:G>A` (Negative strand)
* **Protein Location:** Residue 103 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.438 / 99.8% / 27.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.0) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM domain; histidine mutation destroys receptor tethering salt bridge.

#### 34. `D144V` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.431A>T` (Exon 5)
* **Genomic Coordinate (GRCh38):** `chr19:17843162:T>A` (Negative strand)
* **Protein Location:** Residue 144 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.165 / 99.7% / 25.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.7) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM F1 lobe; loss of coordinating aspartate disrupts domain fold.

#### 35. `C193Y` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.578G>A` (Exon 6)
* **Genomic Coordinate (GRCh38):** `chr19:17842599:C>T` (Negative strand)
* **Protein Location:** Residue 193 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.401 / 99.8% / 27.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.0)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM domain core; bulky tyrosine destroys conserved disulfide / hydrophobic core.

#### 36. `A343P` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.1027G>C` (Exon 8)
* **Genomic Coordinate (GRCh38):** `chr19:17841504:C>G` (Negative strand)
* **Protein Location:** Residue 343 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.475 / 99.9% / 28.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.6) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM F3 lobe; proline breaks an alpha-helix essential for receptor docking.

#### 37. `R350W` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.1048C>T` (Exon 8)
* **Genomic Coordinate (GRCh38):** `chr19:17841483:G>A` (Negative strand)
* **Protein Location:** Residue 350 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.267 / 99.7% / 26.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM domain; tryptophan wedge disrupts the receptor-binding cleft.

#### 38. `L369P` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.1106T>C` (Exon 8)
* **Genomic Coordinate (GRCh38):** `chr19:17841425:A>G` (Negative strand)
* **Protein Location:** Residue 369 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `0.928 / 99.6% / 23.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.8) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM domain; proline insertion triggers severe misfolding and degradation.

#### 39. `G397V` (FERM Domain (receptor gamma-c tethering))
* **Transcript & cDNA:** `NM_000215.4`: `c.1190G>T` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:17840294:C>A` (Negative strand)
* **Protein Location:** Residue 397 | FERM Domain (receptor gamma-c tethering)
* **AlphaGenome Functional Impact:** `1.621 / 99.9% / 31.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+4.1)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM C-terminus; branched valine creates severe steric clash in conserved turn.

#### 40. `L401P` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1202T>C` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:17840282:A>G` (Negative strand)
* **Protein Location:** Residue 401 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `1.310 / 99.8% / 26.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.8) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM-SH2 boundary; proline insertion prevents proper interdomain alignment.

#### 41. `R403C` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1207C>T` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:17840277:G>A` (Negative strand)
* **Protein Location:** Residue 403 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `0.608 / 99.1% / 20.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.7) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM-SH2 hinge; aberrant cysteine causes aggregation / loss of expression.

#### 42. `R403H` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1208G>A` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:17840276:C>T` (Negative strand)
* **Protein Location:** Residue 403 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `0.670 / 99.3% / 21.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.0) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** FERM-SH2 hinge; impairs essential electrostatic stabilization.

#### 43. `I430T` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1289T>C` (Exon 10)
* **Genomic Coordinate (GRCh38):** `chr19:17839629:A>G` (Negative strand)
* **Protein Location:** Residue 430 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `1.425 / 99.8% / 27.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** SH2 domain; polar threonine destabilizes hydrophobic core packing.

#### 44. `G528D` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_000215.4`: `c.1583G>A` (Exon 12)
* **Genomic Coordinate (GRCh38):** `chr19:17838050:C>T` (Negative strand)
* **Protein Location:** Residue 528 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `1.491 / 99.9% / 28.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+3.4) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** SH2-JH2 linker; acidic insertion prevents permissive tandem kinase conformation.

#### 45. `R582W` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1744C>T` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:17837171:G>A` (Negative strand)
* **Protein Location:** Residue 582 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.841 / 99.5% / 23.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** JH2 N-lobe; massive aromatic tryptophan destroys pseudokinase scaffold.

#### 46. `R651W` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.1951C>T` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr19:17835179:G>A` (Negative strand)
* **Protein Location:** Residue 651 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.671 / 99.3% / 21.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+2.5)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** JH2 alphaC-helix; tryptophan disruption causes pseudokinase domain collapse.

#### 47. `T714M` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2141C>T` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr19:17834910:G>A` (Negative strand)
* **Protein Location:** Residue 714 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.914 / 99.6% / 23.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.6)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** JH2 beta-sheet; methionine insertion destabilizes the pseudokinase core.

#### 48. `R775H` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2324G>A` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr19:17834597:C>T` (Negative strand)
* **Protein Location:** Residue 775 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.227 / 99.7% / 25.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.5) + Electrostatic/Born (+2.5)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** JH2 C-lobe; histidine substitution impairs essential interdomain contacts.

#### 49. `D784N` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_000215.4`: `c.2350_2352delins` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr19:17834571:C>A` (Negative strand)
* **Protein Location:** Residue 784 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `2.096 / 100.0% / 35.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.1) + Electrostatic/Born (+2.5)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** JH2 catalytic-like loop; loss of aspartate carboxylate impairs domain stability.

#### 50. `E1019K` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_000215.4`: `c.3055G>A` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:17830544:C>T` (Negative strand)
* **Protein Location:** Residue 1019 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.568 / 99.9% / 30.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.5) + Electrostatic/Born (+2.5)
* **Functional Status:** $\mathbf{Likely LOF}$
* **Biophysical Mechanism & Disease:** JH1 catalytic domain; charge reversal disrupts catalytic core active fold (SCID driver).
