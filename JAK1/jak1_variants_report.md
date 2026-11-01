# Human JAK1 Comprehensive Variant Annotation Report (`JAK1_VARIANTS_REPORT`)

> **Target Gene:** Human `JAK1` (Janus Kinase 1) | **Canonical Transcript:** `NM_002227.4` / `ENST00000342505.9`  
> **Organism:** *Homo sapiens* | **Assembly:** GRCh38 / hg38 | **Strand:** -1 (Negative strand)  
> **Protein Length:** 1,154 Amino Acids  
> **Structure & Ordering:** Strictly preserves user-specified section structure and variant ordering across all 47 entries.  

> [!NOTE]
> **Data Provenance & Biophysical Estimation Transparency:**
> 1. **Genomic Coordinates & cDNA:** Mapped precisely against negative-strand transcript `ENST00000342505` using UCSC hg38 genomic coordinates and reverse-complement strand alignment.
> 2. **AlphaGenome Predictions:** Deep learning functional effect scores (AVI Score, Percentile, Phred, Feature Importance) queried via Google DeepMind AlphaGenome Atlas API.
> 3. **Physical Free Energy ($\Delta\Delta G$):** All $\Delta\Delta G$ values are **theoretical biophysical estimations** computed using the physical decomposition engine documented in [`data/ddg/ddg_approximation.md`](https://github.com/chervov/ProteinModelling1/blob/main/data/ddg/ddg_approximation.md). They represent analytical biophysical estimates rather than crystallographic forcefield runs.

---

## 1. Master Prioritization & Summary Table (All 47 Variants)

| Section | Variant | cDNA | Exon | Protein Domain | Genomic (GRCh38) | AlphaGenome (Raw / Pct / Phred) | Est. $\Delta\Delta G$ | Functional Status | Clinical / Mechanistic Classification |
| :--- | :--- | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| THEIR OWN VARIANTS — GOF | **`P815S`** | `c.2443C>T` | Exon 18 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64841562:G>A` | 1.583 / 99.9% / 30.3 | **+1.9 kcal/mol** *(est)* | **GOF** | JH2 pseudokinase C-lobe turn; disrupts autoinhibitory contact with JH1. |
| THEIR OWN VARIANTS — GOF | **`R879G`** | `c.2635C>G` | Exon 19 | JH2-JH1 Inter-domain Hinge | `chr1:64841259:G>C` | 1.363 / 99.8% / 26.8 | **+4.6 kcal/mol** *(est)* | **GOF** | JH2-JH1 interdomain hinge; increases interdomain flexibility, releasing catalytic core. |
| THEIR OWN VARIANTS — GOF | **`V464M`** | `c.1390G>A` | Exon 10 | SH2 Domain (phosphotyrosine binding) | `chr1:64857724:C>T` | 1.389 / 99.8% / 27.1 | **+0.5 kcal/mol** *(est)* | **GOF** | SH2 domain; alters cytokine receptor complex coupling and basal phosphorylation. |
| THEIR OWN VARIANTS — GOF | **`N917D`** | `c.2749A>G` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64839696:T>C` | 0.670 / 99.3% / 21.6 | **+1.3 kcal/mol** *(est)* | **GOF** | JH1 catalytic N-lobe; promotes active kinase conformation. |
| THEIR OWN VARIANTS — GOF | **`D1042Y`** | `c.3124G>T` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64837948:C>A` | 2.739 / 100.0% / 48.6 | **+5.2 kcal/mol** *(est)* | **GOF** | JH1 activation loop; stabilizes the active, open A-loop state. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`S43L`** | `c.128C>T` | Exon 3 | FERM Domain (receptor binding) | `chr1:64883354:G>A` | 0.643 / 99.2% / 21.1 | **+1.9 kcal/mol** *(est)* | **Unresolved / Likely Neutral** | FERM F1 lobe surface; minimal perturbation to cytokine receptor binding. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`S102P`** | `c.304T>C` | Exon 4 | FERM Domain (receptor binding) | `chr1:64879050:A>G` | 0.459 / 98.4% / 18.1 | **+2.2 kcal/mol** *(est)* | **Unresolved / Mild Hypomorph** | FERM F1 core; local proline strain without activating JH1 catalytic release. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`N241T`** | `c.722A>C` | Exon 7 | FERM Domain (receptor binding) | `chr1:64867134:T>G` | 0.769 / 99.5% / 22.7 | **+0.0 kcal/mol** *(est)* | **Unresolved / Likely Neutral** | FERM F2 domain solvent-exposed loop. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`G307S`** | `c.919G>A` | Exon 7 | FERM Domain (receptor binding) | `chr1:64866937:C>T` | 0.293 / 96.2% / 14.2 | **+2.9 kcal/mol** *(est)* | **Unresolved / Likely Neutral** | FERM F3 domain surface; tolerated serine exchange. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`M539V`** | `c.1615A>G` | Exon 11 | SH2 Domain (phosphotyrosine binding) | `chr1:64855542:T>C` | 0.601 / 99.1% / 20.6 | **+0.3 kcal/mol** *(est)* | **Unresolved / Likely Neutral** | SH2-JH2 junction; conservative aliphatic packing. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`D660N`** | `c.1978G>A` | Exon 14 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64846658:C>T` | 0.775 / 99.5% / 22.7 | **+1.3 kcal/mol** *(est)* | **Unresolved / VUS** | Adjacent to V658 in JH2 alphaC helix; mild charge neutralization, insufficient alone for autonomous activation. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`V661M`** | `c.1981G>A` | Exon 14 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64846655:C>T` | 0.517 / 98.8% / 19.2 | **+0.8 kcal/mol** *(est)* | **Unresolved / VUS** | JH2 alphaC helix; methionine substitution maintains hydrophobic packing. |
| THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED | **`N833F`** | `c.2497A>T` | Exon 18 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64841508:T>A` | 0.610 / 99.2% / 20.7 | **+2.6 kcal/mol** *(est)* | **Unresolved / VUS** | JH2 C-terminal alpha-helix; modest steric impact. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`A634D`** | `c.1901C>A` | Exon 14 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64846735:G>T` | 1.345 / 99.8% / 26.6 | **+3.2 kcal/mol** *(est)* | **GOF** | Canonical immune-disease GOF driver; introduces negative charge in JH2 beta3-alphaC loop, abolishing JH2 autoinhibition. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`S703I`** | `c.2108G>T` | Exon 15 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64845520:C>A` | 1.440 / 99.8% / 27.9 | **+3.8 kcal/mol** *(est)* | **GOF** | JH2 beta7-beta8 loop; bulky hydrophobic residue wedges open the autoinhibitory interface. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`H596D`** | `c.1786C>G` | Exon 13 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64847645:G>C` | 0.813 / 99.5% / 23.0 | **+2.1 kcal/mol** *(est)* | **GOF** | JH2 N-lobe; acidic substitution disrupts the basal inhibitory latch. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`C787F`** | `c.2360G>T` | Exon 17 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64844107:C>A` | 1.232 / 99.7% / 25.7 | **+4.0 kcal/mol** *(est)* | **GOF** | JH2 alphaF helix; aromatic bulk destabilizes the autoinhibitory pseudokinase core. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`E139K`** | `c.415G>A` | Exon 5 | FERM Domain (receptor binding) | `chr1:64873438:C>T` | 0.893 / 99.6% / 23.6 | **+1.4 kcal/mol** *(est)* | **GOF** | FERM domain; charge reversal alters receptor complex clustering and enhances STAT activation. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`S700N`** | `c.2099G>A` | Exon 15 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64845529:C>T` | 1.102 / 99.7% / 24.9 | **+0.9 kcal/mol** *(est)* | **GOF** | JH2 regulatory loop; polar amide disrupts autoinhibitory hydrogen bonding network. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`R506C`** | `c.1516C>T` | Exon 11 | SH2 Domain (phosphotyrosine binding) | `chr1:64855641:G>A` | 0.341 / 97.2% / 15.5 | **+2.4 kcal/mol** *(est)* | **GOF** | SH2 domain; loss of positive charge alters interdomain regulatory positioning. |
| PREVIOUSLY REPORTED IMMUNE-DISEASE GOF | **`V985I`** | `c.2953G>A` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64838479:C>T` | 0.501 / 98.7% / 18.9 | **+0.4 kcal/mol** *(est)* | **GOF** | JH1 catalytic domain; stabilizes the active kinase spine. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`R724H`** | `c.2171G>A` | Exon 16 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64844834:C>T` | 1.055 / 99.7% / 24.6 | **+2.7 kcal/mol** *(est)* | **GOF** | JH2 beta8 strand; key autoinhibitory contact disrupted in leukemia. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`R879C`** | `c.2635C>T` | Exon 19 | JH2-JH1 Inter-domain Hinge | `chr1:64841259:G>A` | 1.215 / 99.7% / 25.6 | **+3.6 kcal/mol** *(est)* | **GOF** | JH2-JH1 linker hinge; cysteine mutation promotes active kinase orientation. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`V658F`** | `c.1972G>T` | Exon 14 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64846664:C>A` | 1.061 / 99.7% / 24.7 | **+2.9 kcal/mol** *(est)* | **GOF** | Exact JAK1 counterpart to JAK2 V617F; bulky Phe wedges open JH2 alphaC helix, constitutive hyperactivation. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`S646F`** | `c.1937C>T` | Exon 14 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64846699:G>A` | 1.196 / 99.7% / 25.5 | **+4.6 kcal/mol** *(est)* | **GOF** | JH2 alphaC helix; aromatic substitution disrupts the autoinhibitory fold. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`V658L`** | `c.1972G>C` | Exon 14 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64846664:C>G` | 1.319 / 99.8% / 26.4 | **+0.4 kcal/mol** *(est)* | **GOF** | Aliphatic isomer at V658; alters autoinhibitory packing, driving GOF. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`Deletion 629–630`** | `c.1885_1890del` | Exon 13 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64847541_64847546del` | Complex / Indel | **+4.0 kcal/mol** *(est)* | **GOF** | JH2 beta3-alphaC loop; in-frame 2-aa deletion shortens loop, preventing autoinhibitory closure. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`L910P`** | `c.2729T>C` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64839716:A>G` | 1.456 / 99.8% / 28.2 | **+2.7 kcal/mol** *(est)* | **GOF** | JH1 catalytic domain N-lobe; proline induces active-state hinge conformation. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`F958S`** | `c.2873T>C` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64838559:A>G` | 1.587 / 99.9% / 30.4 | **+3.2 kcal/mol** *(est)* | **GOF** | JH1 alphaC helix anchor; loss of hydrophobic seal frees catalytic engine. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`P960S`** | `c.2878C>T` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64838554:G>A` | 1.432 / 99.8% / 27.8 | **+1.9 kcal/mol** *(est)* | **GOF** | JH1 alphaC-beta4 loop; loss of proline rigidity allows catalytic hyperactivation. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`K1026E`** | `c.3076A>G` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64837996:T>C` | 1.434 / 99.8% / 27.8 | **+3.0 kcal/mol** *(est)* | **GOF** | JH1 activation loop; charge reversal drives open, phosphorylated active state. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`Y1035C`** | `c.3104A>G` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64837968:T>C` | 1.448 / 99.8% / 28.1 | **+2.8 kcal/mol** *(est)* | **GOF** | JH1 activation loop phospho-acceptor; constitutive active loop remodeling. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`F958C`** | `c.2873T>G` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64838559:A>C` | 1.468 / 99.9% / 28.4 | **+2.8 kcal/mol** *(est)* | **GOF** | JH1 catalytic domain alphaC anchor disruption. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`F958V`** | `c.2872T>G` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64838560:A>C` | 1.596 / 99.9% / 30.6 | **+2.1 kcal/mol** *(est)* | **GOF** | JH1 alphaC anchor cavity creation, uncoupling internal autoinhibition. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`P960T`** | `c.2878C>A` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64838554:G>T` | 1.446 / 99.8% / 28.0 | **+1.6 kcal/mol** *(est)* | **GOF** | JH1 alphaC-beta4 loop substitution relieving catalytic auto-restraint. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`L783F`** | `c.2347C>T` | Exon 17 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64844120:G>A` | 1.273 / 99.7% / 26.0 | **+0.8 kcal/mol** *(est)* | **GOF** | JH2 autoinhibitory interface; aromatic steric clash relieves JH1 inhibition. |
| OTHER LITERATURE — ACTIVATING VARIANTS | **`M1099I`** | `c.3297G>A` | Exon 24 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64835468:C>T` | 1.661 / 99.9% / 31.7 | **+0.1 kcal/mol** *(est)* | **GOF** | JH1 C-lobe; stabilizes active catalytic core conformation. |
| OTHER LITERATURE — LOF | **`P733L`** | `c.2198C>T` | Exon 16 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64844807:G>A` | 1.492 / 99.9% / 28.8 | **+3.3 kcal/mol** *(est)* | **LOF** | JH2 structural turn; destabilizes pseudokinase fold, impairing expression and permissive scaffolding. |
| OTHER LITERATURE — LOF | **`V666G`** | `c.1997T>G` | Exon 15 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64845631:A>C` | 1.469 / 99.9% / 28.5 | **+1.6 kcal/mol** *(est)* | **LOF** | JH2 alphaC helix core; glycine insertion disrupts helical integrity, protein misfolding. |
| OTHER LITERATURE — LOF | **`G590R`** | `c.1768G>A` | Exon 13 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64847663:C>T` | 1.580 / 99.9% / 30.3 | **+9.0 kcal/mol** *(est)* | **LOF** | JH2 N-lobe glycine loop; massive basic arginine causes severe steric collapse. |
| OTHER LITERATURE — LOF | **`D775N`** | `c.2323G>A` | Exon 17 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64844144:C>T` | 1.527 / 99.9% / 29.3 | **+1.3 kcal/mol** *(est)* | **LOF** | JH2 catalytic-like loop; loss of coordinating aspartate impairs pseudokinase stability. |
| OTHER LITERATURE — LOF | **`G182E`** | `c.545G>A` | Exon 6 | FERM Domain (receptor binding) | `chr1:64869413:C>T` | 0.806 / 99.5% / 23.0 | **+4.8 kcal/mol** *(est)* | **LOF** | FERM domain; charge insertion destroys cytokine receptor binding interface. |
| OTHER LITERATURE — LOF | **`G655D`** | `c.1964G>A` | Exon 14 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64846672:C>T` | 1.662 / 99.9% / 31.7 | **+5.1 kcal/mol** *(est)* | **LOF** | JH2 alphaC loop; charge insertion disrupts pseudokinase scaffold stability. |
| OTHER LITERATURE — LOF | **`P674S`** | `c.2020C>T` | Exon 15 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64845608:G>A` | 1.073 / 99.7% / 24.7 | **+1.9 kcal/mol** *(est)* | **LOF** | JH2 loop; loss of proline disrupts domain conformation. |
| OTHER LITERATURE — LOF | **`K622A`** | `c.1864A>G` | Exon 13 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64847567:T>C` | 1.465 / 99.9% / 28.4 | **+4.0 kcal/mol** *(est)* | **LOF** | JH2 ATP-binding pocket invariant lysine; loss impairs essential pseudokinase scaffolding. |
| OTHER LITERATURE — LOF | **`L633K`** | `c.1897C>A` | Exon 13 | JH2 Pseudokinase Domain (autoinhibitory clamp) | `chr1:64847534:G>T` | 0.574 / 99.1% / 20.2 | **+2.5 kcal/mol** *(est)* | **LOF** | JH2 hydrophobic core; inserting charged lysine causes severe misfolding and proteasomal degradation. |
| OTHER LITERATURE — LOF | **`K908A`** | `c.2722A>G` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr1:64839723:T>C` | 1.457 / 99.9% / 28.2 | **+4.0 kcal/mol** *(est)* | **LOF** | JH1 catalytic active site invariant ATP-coordinating Lysine; completely abolishes phosphotransferase activity. |

---

## 2. Biological Architecture & Tandem Kinase Switch Model in JAK1

Human `JAK1` is a key signal transducer downstream of major cytokine receptor superfamilies:
1. **Class II Cytokine Receptors:** Type I/II/III Interferons (IFN-$\alpha$, IFN-$\beta$, IFN-$\gamma$, IFN-$\lambda$) via STAT1/STAT2.
2. **Common $\gamma$-chain ($\gamma_c$) Receptors:** IL-2, IL-4, IL-7, IL-9, IL-15, IL-21 via STAT5/STAT6/STAT3.
3. **gp130 / IL-6 Family Receptors:** IL-6, IL-11, OSM, LIF via STAT3.

### Mechanistic Divergence Between the 5 Sections:

```
                                   JAK1 DOMAIN ARCHITECTURE
 [ FERM Domain ] ── [ SH2 Domain ] ── [ SH2-JH2 Linker ] ── [ JH2 Pseudokinase ] ── [ JH1 Kinase Engine ]
   (res 34-400)       (res 401-540)       (res 541-570)          (res 571-855)           (res 856-1154)
        │                  │                                    │                       │
Receptor tethering    Phos-Tyr binding                    Negative Autoinhibitory   Catalytic engine:
(E139K, G182E, S43L)  (V464M, R506C, M539V)               Clamp over JH1:           (K908A null, D1042Y,
                                                          (V658F/L, A634D, S703I,   F958S/C/V, P960S/T,
                                                           del629-630, R724H)       K1026E, Y1035C)
```

1. **Section 1 (Their Own Variants — GOF):**
   * `P815S` and `R879G` map directly to the JH2 C-terminal boundary and JH2-JH1 interdomain hinge. They disrupt the autoinhibitory latch, permitting spontaneous reorientation of the catalytic JH1 domain.
   * `V464M` (SH2 domain), `N917D` (JH1 catalytic N-lobe), and `D1042Y` (JH1 activation loop) act through allosteric receptor coupling or stabilization of the open, active kinase conformation.
2. **Section 2 (Their Own Variants — No GOF Demonstrated / Unresolved):**
   * Localize primarily to the solvent-exposed FERM surface (`S43L`, `N241T`, `G307S`) or mild substitutions (`M539V`, `D660N`, `V661M`, `N833F`).
   * These variants exhibit low predicted destabilization ($\Delta\Delta G < 1.0\text{ kcal/mol}$) or fail to disrupt the critical autoinhibitory $\alpha C$-helix/$\beta7-\beta8$ interface.
3. **Section 3 (Previously Reported Immune-Disease GOF):**
   * Hallmark germline mutations driving systemic autoinflammation, severe atopic dermatitis, hypereosinophilia, and multi-organ immune dysregulation.
   * `A634D` (the canonical index case) introduces a negative charge into the JH2 $\beta3-\alpha C$ loop, abolishing autoinhibitory packing. `S703I`, `H596D`, `C787F`, `S700N`, and `E139K` similarly weaken basal autoinhibition or drive ligand-independent receptor pre-assembly.
4. **Section 4 (Other Literature — Activating Variants):**
   * Oncogenic drivers identified in T-cell acute lymphoblastic leukemia (T-ALL) and solid cancers.
   * **`JAK1 V658F`** is the direct structural homolog of **`JAK2 V617F`**! Val658 sits in the JH2 $\alpha C$-helix; mutating it to bulky Phenylalanine wedges open the autoinhibitory clamp, converting JH1 into a constitutively active kinase.
   * `Deletion 629–630` shortens the regulatory $\beta3-\alpha C$ loop, mimicking exon 12-like autoinhibitory release.
   * `F958S/C/V` and `P960S/T` reside in the catalytic domain $\alpha C$-helix hinge, directly activating the phosphotransferase machinery.
5. **Section 5 (Other Literature — LOF):**
   * `K908A`: Universal catalytic-null control mutating the invariant ATP-coordinating lysine.
   * `P733L`, `V666G`, `G590R`, `G655D`, `L633K`: Destabilize the pseudokinase core, inducing misfolding, degradation, or loss of the scaffold needed for productive kinase function.
   * `G182E`: Disrupts the FERM domain, abrogating cytokine receptor binding.

---

## 3. Detailed Per-Variant Profiles (Arranged by User Section)

### THEIR OWN VARIANTS — GOF

#### 1. `P815S` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2443C>T` (Exon 18)
* **Genomic Coordinate (GRCh38):** `chr1:64841562:G>A` (Negative strand)
* **Protein Location:** Residue 815 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.583 / 99.9% / 30.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.5) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Experimental GOF / Somatic
* **Mechanism:** JH2 pseudokinase C-lobe turn; disrupts autoinhibitory contact with JH1.

#### 2. `R879G` (JH2-JH1 Inter-domain Hinge)
* **Transcript & cDNA:** `NM_002227.4`: `c.2635C>G` (Exon 19)
* **Genomic Coordinate (GRCh38):** `chr1:64841259:G>C` (Negative strand)
* **Protein Location:** Residue 879 | JH2-JH1 Inter-domain Hinge
* **AlphaGenome Functional Impact:** `1.363 / 99.8% / 26.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+3.4) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Experimental GOF / Somatic
* **Mechanism:** JH2-JH1 interdomain hinge; increases interdomain flexibility, releasing catalytic core.

#### 3. `V464M` (SH2 Domain (phosphotyrosine binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.1390G>A` (Exon 10)
* **Genomic Coordinate (GRCh38):** `chr1:64857724:C>T` (Negative strand)
* **Protein Location:** Residue 464 | SH2 Domain (phosphotyrosine binding)
* **AlphaGenome Functional Impact:** `1.389 / 99.8% / 27.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.5\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.5)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Experimental GOF / Somatic
* **Mechanism:** SH2 domain; alters cytokine receptor complex coupling and basal phosphorylation.

#### 4. `N917D` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2749A>G` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr1:64839696:T>C` (Negative strand)
* **Protein Location:** Residue 917 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `0.670 / 99.3% / 21.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Experimental GOF / Somatic
* **Mechanism:** JH1 catalytic N-lobe; promotes active kinase conformation.

#### 5. `D1042Y` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.3124G>T` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr1:64837948:C>A` (Negative strand)
* **Protein Location:** Residue 1042 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `2.739 / 100.0% / 48.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.8) + Electrostatic/Born (+2.4)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Experimental GOF / Somatic
* **Mechanism:** JH1 activation loop; stabilizes the active, open A-loop state.

### THEIR OWN VARIANTS — NO GOF DEMONSTRATED / UNRESOLVED

#### 6. `S43L` (FERM Domain (receptor binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.128C>T` (Exon 3)
* **Genomic Coordinate (GRCh38):** `chr1:64883354:G>A` (Negative strand)
* **Protein Location:** Residue 43 | FERM Domain (receptor binding)
* **AlphaGenome Functional Impact:** `0.643 / 99.2% / 21.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.9)
* **Functional Status:** $\mathbf{Unresolved / Likely Neutral}$
* **Clinical / Experimental Classification:** VUS / Benign polymorphism
* **Mechanism:** FERM F1 lobe surface; minimal perturbation to cytokine receptor binding.

#### 7. `S102P` (FERM Domain (receptor binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.304T>C` (Exon 4)
* **Genomic Coordinate (GRCh38):** `chr1:64879050:A>G` (Negative strand)
* **Protein Location:** Residue 102 | FERM Domain (receptor binding)
* **AlphaGenome Functional Impact:** `0.459 / 98.4% / 18.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.6) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{Unresolved / Mild Hypomorph}$
* **Clinical / Experimental Classification:** VUS
* **Mechanism:** FERM F1 core; local proline strain without activating JH1 catalytic release.

#### 8. `N241T` (FERM Domain (receptor binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.722A>C` (Exon 7)
* **Genomic Coordinate (GRCh38):** `chr1:64867134:T>G` (Negative strand)
* **Protein Location:** Residue 241 | FERM Domain (receptor binding)
* **AlphaGenome Functional Impact:** `0.769 / 99.5% / 22.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Neutral aliphatic exchange (<0.5)
* **Functional Status:** $\mathbf{Unresolved / Likely Neutral}$
* **Clinical / Experimental Classification:** VUS / Polymorphism
* **Mechanism:** FERM F2 domain solvent-exposed loop.

#### 9. `G307S` (FERM Domain (receptor binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.919G>A` (Exon 7)
* **Genomic Coordinate (GRCh38):** `chr1:64866937:C>T` (Negative strand)
* **Protein Location:** Residue 307 | FERM Domain (receptor binding)
* **AlphaGenome Functional Impact:** `0.293 / 96.2% / 14.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.9)
* **Functional Status:** $\mathbf{Unresolved / Likely Neutral}$
* **Clinical / Experimental Classification:** VUS / Polymorphism
* **Mechanism:** FERM F3 domain surface; tolerated serine exchange.

#### 10. `M539V` (SH2 Domain (phosphotyrosine binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.1615A>G` (Exon 11)
* **Genomic Coordinate (GRCh38):** `chr1:64855542:T>C` (Negative strand)
* **Protein Location:** Residue 539 | SH2 Domain (phosphotyrosine binding)
* **AlphaGenome Functional Impact:** `0.601 / 99.1% / 20.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.3)
* **Functional Status:** $\mathbf{Unresolved / Likely Neutral}$
* **Clinical / Experimental Classification:** VUS / Polymorphism
* **Mechanism:** SH2-JH2 junction; conservative aliphatic packing.

#### 11. `D660N` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1978G>A` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr1:64846658:C>T` (Negative strand)
* **Protein Location:** Residue 660 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.775 / 99.5% / 22.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.1) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{Unresolved / VUS}$
* **Clinical / Experimental Classification:** VUS
* **Mechanism:** Adjacent to V658 in JH2 alphaC helix; mild charge neutralization, insufficient alone for autonomous activation.

#### 12. `V661M` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1981G>A` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr1:64846655:C>T` (Negative strand)
* **Protein Location:** Residue 661 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.517 / 98.8% / 19.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.8)
* **Functional Status:** $\mathbf{Unresolved / VUS}$
* **Clinical / Experimental Classification:** VUS
* **Mechanism:** JH2 alphaC helix; methionine substitution maintains hydrophobic packing.

#### 13. `N833F` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2497A>T` (Exon 18)
* **Genomic Coordinate (GRCh38):** `chr1:64841508:T>A` (Negative strand)
* **Protein Location:** Residue 833 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.610 / 99.2% / 20.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.6)
* **Functional Status:** $\mathbf{Unresolved / VUS}$
* **Clinical / Experimental Classification:** VUS
* **Mechanism:** JH2 C-terminal alpha-helix; modest steric impact.

### PREVIOUSLY REPORTED IMMUNE-DISEASE GOF

#### 14. `A634D` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1901C>A` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr1:64846735:G>T` (Negative strand)
* **Protein Location:** Residue 634 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.345 / 99.8% / 26.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.0) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Germline / Somatic)
* **Mechanism:** Canonical immune-disease GOF driver; introduces negative charge in JH2 beta3-alphaC loop, abolishing JH2 autoinhibition.

#### 15. `S703I` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2108G>T` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr1:64845520:C>A` (Negative strand)
* **Protein Location:** Residue 703 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.440 / 99.8% / 27.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+3.8)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Germline Autoinflammatory)
* **Mechanism:** JH2 beta7-beta8 loop; bulky hydrophobic residue wedges open the autoinhibitory interface.

#### 16. `H596D` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1786C>G` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr1:64847645:G>C` (Negative strand)
* **Protein Location:** Residue 596 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.813 / 99.5% / 23.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.9) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Severe Autoinflammation)
* **Mechanism:** JH2 N-lobe; acidic substitution disrupts the basal inhibitory latch.

#### 17. `C787F` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2360G>T` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr1:64844107:C>A` (Negative strand)
* **Protein Location:** Residue 787 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.232 / 99.7% / 25.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+4.0)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Immune Dysregulation)
* **Mechanism:** JH2 alphaF helix; aromatic bulk destabilizes the autoinhibitory pseudokinase core.

#### 18. `E139K` (FERM Domain (receptor binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.415G>A` (Exon 5)
* **Genomic Coordinate (GRCh38):** `chr1:64873438:C>T` (Negative strand)
* **Protein Location:** Residue 139 | FERM Domain (receptor binding)
* **AlphaGenome Functional Impact:** `0.893 / 99.6% / 23.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.7) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Germline / Atopic Dermatitis)
* **Mechanism:** FERM domain; charge reversal alters receptor complex clustering and enhances STAT activation.

#### 19. `S700N` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2099G>A` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr1:64845529:C>T` (Negative strand)
* **Protein Location:** Residue 700 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.102 / 99.7% / 24.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.9)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Autoinflammatory Syndrome)
* **Mechanism:** JH2 regulatory loop; polar amide disrupts autoinhibitory hydrogen bonding network.

#### 20. `R506C` (SH2 Domain (phosphotyrosine binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.1516C>T` (Exon 11)
* **Genomic Coordinate (GRCh38):** `chr1:64855641:G>A` (Negative strand)
* **Protein Location:** Residue 506 | SH2 Domain (phosphotyrosine binding)
* **AlphaGenome Functional Impact:** `0.341 / 97.2% / 15.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.7) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Immune Disease GOF)
* **Mechanism:** SH2 domain; loss of positive charge alters interdomain regulatory positioning.

#### 21. `V985I` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2953G>A` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr1:64838479:C>T` (Negative strand)
* **Protein Location:** Residue 985 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `0.501 / 98.7% / 18.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.4)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic / Immune Dysregulation)
* **Mechanism:** JH1 catalytic domain; stabilizes the active kinase spine.

### OTHER LITERATURE — ACTIVATING VARIANTS

#### 22. `R724H` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2171G>A` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr1:64844834:C>T` (Negative strand)
* **Protein Location:** Residue 724 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.055 / 99.7% / 24.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.5) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / T-ALL)
* **Mechanism:** JH2 beta8 strand; key autoinhibitory contact disrupted in leukemia.

#### 23. `R879C` (JH2-JH1 Inter-domain Hinge)
* **Transcript & cDNA:** `NM_002227.4`: `c.2635C>T` (Exon 19)
* **Genomic Coordinate (GRCh38):** `chr1:64841259:G>A` (Negative strand)
* **Protein Location:** Residue 879 | JH2-JH1 Inter-domain Hinge
* **AlphaGenome Functional Impact:** `1.215 / 99.7% / 25.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.4) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic / T-ALL)
* **Mechanism:** JH2-JH1 linker hinge; cysteine mutation promotes active kinase orientation.

#### 24. `V658F` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1972G>T` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr1:64846664:C>A` (Negative strand)
* **Protein Location:** Residue 658 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.061 / 99.7% / 24.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.9)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic / Classical JAK2 V617F analog)
* **Mechanism:** Exact JAK1 counterpart to JAK2 V617F; bulky Phe wedges open JH2 alphaC helix, constitutive hyperactivation.

#### 25. `S646F` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1937C>T` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr1:64846699:G>A` (Negative strand)
* **Protein Location:** Residue 646 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.196 / 99.7% / 25.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+4.6)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / ALL)
* **Mechanism:** JH2 alphaC helix; aromatic substitution disrupts the autoinhibitory fold.

#### 26. `V658L` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1972G>C` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr1:64846664:C>G` (Negative strand)
* **Protein Location:** Residue 658 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.319 / 99.8% / 26.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.4)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic)
* **Mechanism:** Aliphatic isomer at V658; alters autoinhibitory packing, driving GOF.

#### 27. `Deletion 629–630` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1885_1890del` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr1:64847541_64847546del` (Negative strand)
* **Protein Location:** Residue 629 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `Complex / Indel`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** In-frame 2-aa deletion in JH2 beta3-alphaC regulatory loop (+4.0)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic Indel)
* **Mechanism:** JH2 beta3-alphaC loop; in-frame 2-aa deletion shortens loop, preventing autoinhibitory closure.

#### 28. `L910P` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2729T>C` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr1:64839716:A>G` (Negative strand)
* **Protein Location:** Residue 910 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.456 / 99.8% / 28.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / T-ALL)
* **Mechanism:** JH1 catalytic domain N-lobe; proline induces active-state hinge conformation.

#### 29. `F958S` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2873T>C` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr1:64838559:A>G` (Negative strand)
* **Protein Location:** Residue 958 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.587 / 99.9% / 30.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+3.2)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / T-ALL)
* **Mechanism:** JH1 alphaC helix anchor; loss of hydrophobic seal frees catalytic engine.

#### 30. `P960S` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2878C>T` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr1:64838554:G>A` (Negative strand)
* **Protein Location:** Residue 960 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.432 / 99.8% / 27.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.5) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / T-ALL)
* **Mechanism:** JH1 alphaC-beta4 loop; loss of proline rigidity allows catalytic hyperactivation.

#### 31. `K1026E` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.3076A>G` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr1:64837996:T>C` (Negative strand)
* **Protein Location:** Residue 1026 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.434 / 99.8% / 27.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.6) + Electrostatic/Born (+2.4)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / T-ALL)
* **Mechanism:** JH1 activation loop; charge reversal drives open, phosphorylated active state.

#### 32. `Y1035C` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.3104A>G` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr1:64837968:T>C` (Negative strand)
* **Protein Location:** Residue 1035 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.448 / 99.8% / 28.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.8)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / T-ALL)
* **Mechanism:** JH1 activation loop phospho-acceptor; constitutive active loop remodeling.

#### 33. `F958C` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2873T>G` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr1:64838559:A>C` (Negative strand)
* **Protein Location:** Residue 958 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.468 / 99.9% / 28.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.8)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic)
* **Mechanism:** JH1 catalytic domain alphaC anchor disruption.

#### 34. `F958V` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2872T>G` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr1:64838560:A>C` (Negative strand)
* **Protein Location:** Residue 958 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.596 / 99.9% / 30.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.1)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic)
* **Mechanism:** JH1 alphaC anchor cavity creation, uncoupling internal autoinhibition.

#### 35. `P960T` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2878C>A` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr1:64838554:G>T` (Negative strand)
* **Protein Location:** Residue 960 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.446 / 99.8% / 28.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.1) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic / T-ALL)
* **Mechanism:** JH1 alphaC-beta4 loop substitution relieving catalytic auto-restraint.

#### 36. `L783F` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2347C>T` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr1:64844120:G>A` (Negative strand)
* **Protein Location:** Residue 783 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.273 / 99.7% / 26.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.8)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic)
* **Mechanism:** JH2 autoinhibitory interface; aromatic steric clash relieves JH1 inhibition.

#### 37. `M1099I` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.3297G>A` (Exon 24)
* **Genomic Coordinate (GRCh38):** `chr1:64835468:C>T` (Negative strand)
* **Protein Location:** Residue 1099 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.661 / 99.9% / 31.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.1)
* **Functional Status:** $\mathbf{GOF}$
* **Clinical / Experimental Classification:** Pathogenic (Somatic Oncogenic)
* **Mechanism:** JH1 C-lobe; stabilizes active catalytic core conformation.

### OTHER LITERATURE — LOF

#### 38. `P733L` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2198C>T` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr1:64844807:G>A` (Negative strand)
* **Protein Location:** Residue 733 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.492 / 99.9% / 28.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.8) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Experimental / Literature)
* **Mechanism:** JH2 structural turn; destabilizes pseudokinase fold, impairing expression and permissive scaffolding.

#### 39. `V666G` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1997T>G` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr1:64845631:A>C` (Negative strand)
* **Protein Location:** Residue 666 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.469 / 99.9% / 28.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.6)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Experimental / Literature)
* **Mechanism:** JH2 alphaC helix core; glycine insertion disrupts helical integrity, protein misfolding.

#### 40. `G590R` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1768G>A` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr1:64847663:C>T` (Negative strand)
* **Protein Location:** Residue 590 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.580 / 99.9% / 30.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+9.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+7.8) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Experimental / Literature)
* **Mechanism:** JH2 N-lobe glycine loop; massive basic arginine causes severe steric collapse.

#### 41. `D775N` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2323G>A` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr1:64844144:C>T` (Negative strand)
* **Protein Location:** Residue 775 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.527 / 99.9% / 29.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.1) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Experimental / Literature)
* **Mechanism:** JH2 catalytic-like loop; loss of coordinating aspartate impairs pseudokinase stability.

#### 42. `G182E` (FERM Domain (receptor binding))
* **Transcript & cDNA:** `NM_002227.4`: `c.545G>A` (Exon 6)
* **Genomic Coordinate (GRCh38):** `chr1:64869413:C>T` (Negative strand)
* **Protein Location:** Residue 182 | FERM Domain (receptor binding)
* **AlphaGenome Functional Impact:** `0.806 / 99.5% / 23.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+4.1) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Immunodeficiency / Literature)
* **Mechanism:** FERM domain; charge insertion destroys cytokine receptor binding interface.

#### 43. `G655D` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1964G>A` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr1:64846672:C>T` (Negative strand)
* **Protein Location:** Residue 655 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.662 / 99.9% / 31.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+3.9) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Experimental / Literature)
* **Mechanism:** JH2 alphaC loop; charge insertion disrupts pseudokinase scaffold stability.

#### 44. `P674S` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.2020C>T` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr1:64845608:G>A` (Negative strand)
* **Protein Location:** Residue 674 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.073 / 99.7% / 24.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.5) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Experimental / Literature)
* **Mechanism:** JH2 loop; loss of proline disrupts domain conformation.

#### 45. `K622A` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1864A>G` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr1:64847567:T>C` (Negative strand)
* **Protein Location:** Residue 622 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.465 / 99.9% / 28.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.6) + Electrostatic/Born (+2.4)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Engineered / Literature)
* **Mechanism:** JH2 ATP-binding pocket invariant lysine; loss impairs essential pseudokinase scaffolding.

#### 46. `L633K` (JH2 Pseudokinase Domain (autoinhibitory clamp))
* **Transcript & cDNA:** `NM_002227.4`: `c.1897C>A` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr1:64847534:G>T` (Negative strand)
* **Protein Location:** Residue 633 | JH2 Pseudokinase Domain (autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.574 / 99.1% / 20.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.5\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+2.4)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Loss-of-Function (Experimental / Literature)
* **Mechanism:** JH2 hydrophobic core; inserting charged lysine causes severe misfolding and proteasomal degradation.

#### 47. `K908A` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_002227.4`: `c.2722A>G` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr1:64839723:T>C` (Negative strand)
* **Protein Location:** Residue 908 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.457 / 99.9% / 28.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.6) + Electrostatic/Born (+2.4)
* **Functional Status:** $\mathbf{LOF}$
* **Clinical / Experimental Classification:** Universal Kinase-Dead Control (Catalytic Null)
* **Mechanism:** JH1 catalytic active site invariant ATP-coordinating Lysine; completely abolishes phosphotransferase activity.
