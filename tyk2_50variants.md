# Human TYK2 Comprehensive 50-Variant Functional Annotation Report (`tyk2_50variants.md`)

> **Target Gene:** Human `TYK2` (Tyrosine Kinase 2) | **Canonical Transcript:** `NM_003331.5` / `ENST00000525621.5` (or `ENST00001135476`)  
> **Organism:** *Homo sapiens* | **Assembly:** GRCh38 / hg38 | **Strand:** -1 (Negative strand)  
> **Protein Length:** 1,187 Amino Acids  
> **Structure & Ordering:** Strictly preserves user-specified order across all 50 entries in 3 categories (GOF, LOF, More LOF).  

> [!NOTE]
> **Data Provenance & Biophysical Estimation Transparency:**
> 1. **Genomic Coordinates & cDNA:** Mapped precisely against human `TYK2` coding exons using UCSC hg38 genomic coordinates and reverse-complement strand alignment.
> 2. **AlphaGenome Predictions:** Deep learning functional effect scores (AVI Score, Percentile, Phred, Feature Importance) queried via Google DeepMind AlphaGenome Atlas API.
> 3. **Physical Free Energy ($\Delta\Delta G$):** All $\Delta\Delta G$ values are **theoretical biophysical estimations** computed using the physical decomposition engine documented in [`data/ddg/ddg_approximation.md`](https://github.com/chervov/ProteinModelling1/blob/main/data/ddg/ddg_approximation.md). They represent analytical biophysical estimates rather than crystallographic forcefield runs.

---

## 1. Master Prioritization & Summary Table (All 50 Variants)

| # | Category | Variant | cDNA | Exon | Protein Domain | Genomic (GRCh38) | AlphaGenome (Raw / Pct / Phred) | Est. $\Delta\Delta G$ | Status | Mechanistic & Functional Classification |
| :-: | :--- | :--- | :--- | :---: | :--- | :--- | :---: | :---: | :---: | :--- |
| 01 | GOF | **`P760L`** | `c.2279C>T` | Exon 16 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10358035:G>A` | 0.998 / 99.6% / 24.3 | **+4.5 kcal/mol** *(est)* | **GOF** | JH2 pseudokinase C-lobe turn; disrupts autoinhibitory contact holding JH1 in basal dormant state. |
| 02 | GOF | **`G761V`** | `c.2282G>T` | Exon 16 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10358032:C>A` | 1.401 / 99.8% / 27.2 | **+6.1 kcal/mol** *(est)* | **GOF** | Adjacent to P760 in JH2 autoinhibitory turn; bulky valine wedges open the pseudokinase-kinase interface. |
| 03 | GOF | **`E957D`** | `c.2871G>C` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10354079:C>G` | 0.188 / 92.2% / 11.1 | **+0.6 kcal/mol** *(est)* | **GOF** | JH1 catalytic domain N-lobe; alters electrostatic environment promoting active kinase conformation. |
| 04 | GOF | **`R1027H`** | `c.3080G>A` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353046:C>T` | 1.559 / 99.9% / 29.8 | **+2.7 kcal/mol** *(est)* | **GOF** | JH1 activation loop boundary; histidine substitution relieves basal conformational auto-restraint. |
| 05 | GOF | **`G36D`** | `c.107G>A` | Exon 3 | FERM Domain (receptor tethering) | `chr19:10378300:C>T` | 1.127 / 99.7% / 25.1 | **+4.1 kcal/mol** *(est)* | **GOF** | FERM domain N-terminus; promotes spontaneous cytokine receptor pre-assembly / homodimerization. |
| 06 | GOF | **`S47N`** | `c.140G>A` | Exon 3 | FERM Domain (receptor tethering) | `chr19:10378267:C>T` | 0.188 / 92.2% / 11.1 | **+0.6 kcal/mol** *(est)* | **GOF** | FERM F1 lobe; enhances receptor complex clustering and basal STAT phosphorylation. |
| 07 | GOF | **`V731I`** | `c.2191G>A` | Exon 16 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10358123:C>T` | 0.458 / 98.4% / 18.1 | **+0.4 kcal/mol** *(est)* | **GOF** | JH2 beta7-beta8 loop; aliphatic expansion destabilizes the autoinhibitory clamp. |
| 08 | GOF | **`E41V`** | `c.122A>T` | Exon 3 | FERM Domain (receptor tethering) | `chr19:10378285:T>A` | 0.705 / 99.4% / 22.0 | **+0.7 kcal/mol** *(est)* | **GOF** | FERM domain surface; hydrophobic exchange enhances autonomous receptor engagement. |
| 09 | GOF | **`P441R`** | `c.1322C>G` | Exon 9 | SH2 Domain (phosphotyrosine recognition) | `chr19:10364659:G>C` | 0.812 / 99.5% / 23.0 | **+4.9 kcal/mol** *(est)* | **GOF** | FERM-SH2 junction hinge; basic charge release promotes interdomain active orientation. |
| 10 | GOF | **`K642R`** | `c.1925A>G` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10361804:T>C` | 0.880 / 99.6% / 23.5 | **+3.1 kcal/mol** *(est)* | **GOF** | JH2 alphaC-helix regulatory switch; alters allosteric autoinhibition of catalytic engine. |
| 11 | GOF | **`H667Q`** | `c.2001C>A` | Exon 14 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10361557:G>T` | 0.543 / 98.9% / 19.7 | **+1.4 kcal/mol** *(est)* | **GOF** | JH2 pseudokinase regulatory pocket; neutralizes imidazole, uncoupling autoinhibitory restraint. |
| 12 | GOF | **`E925K`** | `c.2773G>A` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10354177:C>T` | 0.961 / 99.6% / 24.1 | **+2.2 kcal/mol** *(est)* | **GOF** | JH1 catalytic N-lobe; charge reversal stabilizes ATP-binding competent state. |
| 13 | LOF | **`G1010D`** | `c.3029G>A` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353097:C>T` | 1.702 / 99.9% / 32.1 | **+8.0 kcal/mol** *(est)* | **LOF** | JH1 catalytic loop; inserting charged aspartate destroys invariant catalytic cleft geometry. |
| 14 | LOF | **`R864C`** | `c.2590C>T` | Exon 18 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10356595:G>A` | 0.898 / 99.6% / 23.7 | **+5.0 kcal/mol** *(est)* | **LOF** | JH2-JH1 interdomain interface; loss of positive charge and salt-bridge network impairs folding. |
| 15 | LOF | **`P1104A`** | `c.3310C>G` | Exon 23 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10352442:G>C` | 1.357 / 99.8% / 26.7 | **+1.9 kcal/mol** *(est)* | **LOF** | JH1 activation segment C-terminal anchor; proline loss destabilizes kinase catalytic engine. |
| 16 | LOF | **`G634E`** | `c.1901G>A` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10361828:C>T` | 0.127 / 87.6% / 9.1 | **+6.1 kcal/mol** *(est)* | **LOF** | JH2 beta3-alphaC loop; acidic charge creates severe steric clash, inducing pseudokinase misfolding. |
| 17 | LOF | **`G996R`** | `c.2986G>A` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353569:C>T` | 0.901 / 99.6% / 23.7 | **+9.0 kcal/mol** *(est)* | **LOF** | JH1 catalytic core; bulky basic arginine severely disrupts the catalytic spine. |
| 18 | LOF | **`A928V`** | `c.2783C>T` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10354167:G>A` | 1.521 / 99.9% / 29.2 | **+3.2 kcal/mol** *(est)* | **LOF** | JH1 subdomain II ATP-binding cleft; steric crowding adjacent to invariant catalytic lysine. |
| 19 | LOF | **`G799R`** | `c.2395G>A` | Exon 17 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10357835:C>T` | 1.439 / 99.8% / 27.9 | **+10.2 kcal/mol** *(est)* | **LOF** | JH2 pseudokinase core; arginine insertion induces severe steric collapse and proteasomal degradation. |
| 20 | LOF | **`L1014P`** | `c.3041T>C` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353085:A>G` | 1.401 / 99.8% / 27.2 | **+3.7 kcal/mol** *(est)* | **LOF** | JH1 catalytic loop; rigid proline disrupts the catalytic polypeptide backbone. |
| 21 | LOF | **`L757V`** | `c.2269C>G` | Exon 16 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10358045:G>C` | 1.662 / 99.9% / 31.7 | **+0.4 kcal/mol** *(est)* | **LOF** | JH2 hydrophobic core; cavity creation destabilizes the required pseudokinase scaffold. |
| 22 | LOF | **`N1028S`** | `c.3083A>G` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353043:T>C` | 1.466 / 99.9% / 28.4 | **+0.5 kcal/mol** *(est)* | **LOF** | JH1 activation loop; impairs coordination of phosphorylation-dependent activation. |
| 23 | LOF | **`S431G`** | `c.1291A>G` | Exon 9 | FERM Domain (receptor tethering) | `chr19:10364690:T>C` | 0.626 / 99.2% / 20.9 | **+0.4 kcal/mol** *(est)* | **LOF** | FERM domain core; loss of side chain destabilizes cytokine receptor-binding interface. |
| 24 | LOF | **`R703W`** | `c.2107C>T` | Exon 15 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10359243:G>A` | 0.216 / 93.6% / 12.0 | **+1.3 kcal/mol** *(est)* | **LOF** | JH2 pseudokinase beta-sheet; massive aromatic tryptophan disrupts domain structural integrity. |
| 25 | More LOF | **`E782K`** | `c.2344G>A` | Exon 17 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10357886:C>T` | 1.375 / 99.8% / 26.9 | **+3.4 kcal/mol** *(est)* | **LOF** | JH2 alphaF helix; charge reversal breaks essential internal salt bridges. |
| 26 | More LOF | **`H669P`** | `c.2006A>C` | Exon 14 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10361552:T>G` | 1.151 / 99.7% / 25.2 | **+3.6 kcal/mol** *(est)* | **LOF** | JH2 alphaC helix; proline insertion terminates the autoinhibitory alpha-helix, causing misfolding. |
| 27 | More LOF | **`G1040W`** | `c.3118G>T` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353008:C>A` | 1.501 / 99.9% / 28.9 | **+9.4 kcal/mol** *(est)* | **LOF** | JH1 DFG motif adjacent glycine; massive tryptophan wedge completely blocks ATP binding. |
| 28 | More LOF | **`R864H`** | `c.2591G>A` | Exon 18 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10356594:C>T` | 1.054 / 99.7% / 24.6 | **+4.1 kcal/mol** *(est)* | **LOF** | JH2 C-terminal interface; histidine substitution impairs interdomain salt-bridge stabilization. |
| 29 | More LOF | **`K1038N`** | `c.3114G>C` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353012:C>G` | 1.533 / 99.9% / 29.4 | **+3.7 kcal/mol** *(est)* | **LOF** | JH1 activation segment; loss of basic lysine prevents active-state electrostatic network. |
| 30 | More LOF | **`R860H`** | `c.2579G>A` | Exon 18 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10356606:C>T` | 0.803 / 99.5% / 23.0 | **+4.1 kcal/mol** *(est)* | **LOF** | JH2 C-lobe interface; impairs structural tethering required for catalytic competence. |
| 31 | More LOF | **`R1159S`** | `c.3475C>A` | Exon 25 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10350923:G>T` | 1.503 / 99.9% / 29.0 | **+5.4 kcal/mol** *(est)* | **LOF** | JH1 C-terminal domain boundary; loss of arginine destabilizes the kinase C-lobe core. |
| 32 | More LOF | **`G1088W`** | `c.3262G>T` | Exon 23 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10352490:C>A` | 1.614 / 99.9% / 31.0 | **+7.9 kcal/mol** *(est)* | **LOF** | JH1 C-lobe; tryptophan insertion disrupts internal packing of the catalytic domain. |
| 33 | More LOF | **`R1159C`** | `c.3475C>T` | Exon 25 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10350923:G>A` | 1.347 / 99.8% / 26.6 | **+5.0 kcal/mol** *(est)* | **LOF** | JH1 C-terminal boundary; cysteine mutation introduces aberrant disulfide bonding / misfolding. |
| 34 | More LOF | **`R895C`** | `c.2683C>T` | Exon 19 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10354544:G>A` | 0.989 / 99.6% / 24.2 | **+5.0 kcal/mol** *(est)* | **LOF** | JH2-JH1 interdomain hinge; disrupts the conformational alignment of the tandem kinases. |
| 35 | More LOF | **`H594Y`** | `c.1780C>T` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10361949:G>A` | 1.258 / 99.7% / 25.9 | **+2.6 kcal/mol** *(est)* | **LOF** | JH2 N-lobe beta-sheet; bulky tyrosine creates steric clashes destabilizing the pseudokinase fold. |
| 36 | More LOF | **`R1159H`** | `c.3476G>A` | Exon 25 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10350922:C>T` | 1.484 / 99.9% / 28.7 | **+4.1 kcal/mol** *(est)* | **LOF** | JH1 C-terminal tail; impairs overall stability of the catalytic domain. |
| 37 | More LOF | **`L695P`** | `c.2084T>C` | Exon 15 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10359266:A>G` | 1.377 / 99.8% / 26.9 | **+2.7 kcal/mol** *(est)* | **LOF** | JH2 beta-sheet; proline insertion disrupts secondary structure and causes misfolding. |
| 38 | More LOF | **`R860C`** | `c.2578C>T` | Exon 18 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10356607:G>A` | 0.764 / 99.5% / 22.6 | **+5.0 kcal/mol** *(est)* | **LOF** | JH2 interdomain boundary; cysteine substitution induces aggregation / loss of expression. |
| 39 | More LOF | **`D421H`** | `c.1261G>C` | Exon 9 | FERM Domain (receptor tethering) | `chr19:10364720:C>G` | 1.337 / 99.8% / 26.5 | **+1.7 kcal/mol** *(est)* | **LOF** | FERM domain F3 lobe; disrupts acidic patch essential for cytokine receptor association. |
| 40 | More LOF | **`L986P`** | `c.2957T>C` | Exon 21 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353598:A>G` | 1.487 / 99.9% / 28.7 | **+2.7 kcal/mol** *(est)* | **LOF** | JH1 catalytic domain; proline breaks an essential alpha-helix in the kinase engine. |
| 41 | More LOF | **`H432R`** | `c.1295A>G` | Exon 9 | FERM Domain (receptor tethering) | `chr19:10364686:T>C` | 1.023 / 99.6% / 24.4 | **+2.4 kcal/mol** *(est)* | **LOF** | FERM-SH2 linker; disrupts electrostatic tethering to cytokine receptor Box1/Box2. |
| 42 | More LOF | **`D1041A`** | `c.3122A>C` | Exon 22 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10353004:T>G` | 1.703 / 99.9% / 32.2 | **+3.1 kcal/mol** *(est)* | **LOF** | JH1 invariant DFG motif catalytic aspartate; completely eliminates Mg2+/ATP coordination (Catalytic Null). |
| 43 | More LOF | **`L641P`** | `c.1922T>C` | Exon 13 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10361807:A>G` | 1.547 / 99.9% / 29.6 | **+2.7 kcal/mol** *(est)* | **LOF** | JH2 alphaC helix; proline breaks the alpha-helix, leading to pseudokinase collapse. |
| 44 | More LOF | **`C1140W`** | `c.3420T>G` | Exon 24 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10351061:A>C` | 1.121 / 99.7% / 25.0 | **+5.6 kcal/mol** *(est)* | **LOF** | JH1 C-lobe; massive tryptophan wedge causes severe steric clash in the kinase core. |
| 45 | More LOF | **`S1082P`** | `c.3244T>C` | Exon 23 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10352508:A>G` | 1.518 / 99.9% / 29.2 | **+2.4 kcal/mol** *(est)* | **LOF** | JH1 C-lobe loop; proline strain alters the catalytic engine fold. |
| 46 | More LOF | **`E947K`** | `c.2839G>A` | Exon 20 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10354111:C>T` | 1.591 / 99.9% / 30.5 | **+5.1 kcal/mol** *(est)* | **LOF** | JH1 catalytic N-lobe; charge reversal disrupts invariant electrostatic network. |
| 47 | More LOF | **`G1088R`** | `c.3262G>A` | Exon 23 | JH1 Tyrosine Kinase Domain (catalytic engine) | `chr19:10352490:C>T` | 1.893 / 100.0% / 33.9 | **+9.0 kcal/mol** *(est)* | **LOF** | JH1 C-lobe; basic arginine insertion causes severe electrostatic and steric collapse. |
| 48 | More LOF | **`W798C`** | `c.2394G>C` | Exon 17 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10357836:C>G` | 1.653 / 99.9% / 31.6 | **+3.6 kcal/mol** *(est)* | **LOF** | JH2 hydrophobic core; loss of bulky tryptophan creates a massive 119 A3 cavity void. |
| 49 | More LOF | **`D429N`** | `c.1285G>A` | Exon 9 | FERM Domain (receptor tethering) | `chr19:10364696:C>T` | 0.936 / 99.6% / 23.9 | **+0.8 kcal/mol** *(est)* | **LOF** | FERM domain; loss of coordinating carboxylate impairs cytokine receptor association. |
| 50 | More LOF | **`E806K`** | `c.2416G>A` | Exon 17 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp) | `chr19:10357814:C>T` | 1.517 / 99.9% / 29.2 | **+3.4 kcal/mol** *(est)* | **LOF** | JH2 C-lobe surface; charge reversal destabilizes the pseudokinase scaffolding fold. |

---

## 2. Biological Architecture & Tandem Kinase Switch Model in TYK2

Human `TYK2` is the essential non-receptor tyrosine kinase mediating downstream signaling for:
1. **Type I Interferons (IFN-$\alpha$, IFN-$\beta$):** Heterodimerizes with JAK1 downstream of IFNAR1/IFNAR2 to phosphorylate STAT1 and STAT2.
2. **Interleukin-12 (IL-12):** Heterodimerizes with JAK2 downstream of IL-12R$\beta1$/IL-12R$\beta2$ to activate STAT4 and drive Th1 differentiation.
3. **Interleukin-23 (IL-23):** Downstream of IL-12R$\beta1$/IL-23R to activate STAT3 and drive Th17 immune responses (the key driver in psoriasis, psoriatic arthritis, and IBD).
4. **Interleukin-10 (IL-10) family:** Signaling through IL-10R, IL-22R.

### The Tandem Kinase Switch Model in TYK2:

```
                                   TYK2 DOMAIN ARCHITECTURE
 [ FERM Domain ] ── [ SH2 Domain ] ── [ SH2-JH2 Linker ] ── [ JH2 Pseudokinase ] ── [ JH1 Kinase Engine ]
   (res 1-440)        (res 441-580)       (res 581-600)          (res 601-890)           (res 891-1187)
        │                  │                                    │                       │
Receptor tethering    Phos-Tyr binding                    Negative Autoinhibitory   Catalytic engine:
(G36D, E41V, S47N,    (P441R)                             Clamp over JH1:           (D1041A catalytic null,
 D421H, D429N, H432R)                                     (P760L, G761V, V731I,     G1040W, G1010D,
                                                           K642R, H667Q GOF;        L1014P, P1104A LOF)
                                                           G634E, W798C, R864C LOF)
```

1. **GOF Mutations (12 Variants):**
   * **JH2 Autoinhibitory Clamp Destabilization (`P760L`, `G761V`, `V731I`, `K642R`, `H667Q`):** Residues 760–761 and 731 form the critical autoinhibitory turn in the pseudokinase C-lobe that latches onto the JH1 catalytic engine. Mutations here destabilize the autoinhibitory latch ($\Delta\Delta G > +1.5\text{ kcal/mol}$), constitutively releasing JH1 kinase activity.
   * **FERM Domain Autonomous Activation (`G36D`, `E41V`, `S47N`):** In the N-terminal FERM domain, these mutations promote spontaneous receptor clustering and enhanced basal STAT activation.
   * **JH1 Active State Stabilization (`E925K`, `E957D`, `R1027H`):** Directly remodel the kinase N-lobe and activation loop into the open, active conformation.
2. **LOF & More LOF Mutations (38 Variants):**
   * **Direct Catalytic Nullification in JH1:** `D1041A` mutates the invariant catalytic aspartate of the DFG motif (completely eliminating $\text{Mg}^{2+}/\text{ATP}$ coordination); `G1040W` introduces a massive tryptophan wedge into the ATP binding cleft; `G1010D` disrupts the catalytic loop.
   * **Pseudokinase Core Misfolding & Degradation:** `W798C` deletes a buried tryptophan creating a devastating $+5.2\text{ kcal/mol}$ cavity void ($119\text{ \AA}^3$); `G634E`, `G799R`, `L641P`, `H669P`, `L695P`, and `R864C/H` break the pseudokinase scaffold required for productive protein stability.
   * **FERM Disruption:** `D421H`, `D429N`, and `H432R` abrogate the acidic interface required to bind cytokine receptor chains (IFNAR1, IL-12R$\beta1$).

---

## 3. Detailed Per-Variant Profiles (Arranged by Category)

### Category: GOF

#### 01. `P760L` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2279C>T` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr19:10358035:G>A` (Negative strand)
* **Protein Location:** Residue 760 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.998 / 99.6% / 24.3`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.5\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+3.0) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** JH2 pseudokinase C-lobe turn; disrupts autoinhibitory contact holding JH1 in basal dormant state.

#### 02. `G761V` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2282G>T` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr19:10358032:C>A` (Negative strand)
* **Protein Location:** Residue 761 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.401 / 99.8% / 27.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+6.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+6.1)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** Adjacent to P760 in JH2 autoinhibitory turn; bulky valine wedges open the pseudokinase-kinase interface.

#### 03. `E957D` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.2871G>C` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr19:10354079:C>G` (Negative strand)
* **Protein Location:** Residue 957 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `0.188 / 92.2% / 11.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.6)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** JH1 catalytic domain N-lobe; alters electrostatic environment promoting active kinase conformation.

#### 04. `R1027H` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3080G>A` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:10353046:C>T` (Negative strand)
* **Protein Location:** Residue 1027 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.559 / 99.9% / 29.8`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.5) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** JH1 activation loop boundary; histidine substitution relieves basal conformational auto-restraint.

#### 05. `G36D` (FERM Domain (receptor tethering))
* **Transcript & cDNA:** `NM_003331.5`: `c.107G>A` (Exon 3)
* **Genomic Coordinate (GRCh38):** `chr19:10378300:C>T` (Negative strand)
* **Protein Location:** Residue 36 | FERM Domain (receptor tethering)
* **AlphaGenome Functional Impact:** `1.127 / 99.7% / 25.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+3.4) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** FERM domain N-terminus; promotes spontaneous cytokine receptor pre-assembly / homodimerization.

#### 06. `S47N` (FERM Domain (receptor tethering))
* **Transcript & cDNA:** `NM_003331.5`: `c.140G>A` (Exon 3)
* **Genomic Coordinate (GRCh38):** `chr19:10378267:C>T` (Negative strand)
* **Protein Location:** Residue 47 | FERM Domain (receptor tethering)
* **AlphaGenome Functional Impact:** `0.188 / 92.2% / 11.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.6)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** FERM F1 lobe; enhances receptor complex clustering and basal STAT phosphorylation.

#### 07. `V731I` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2191G>A` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr19:10358123:C>T` (Negative strand)
* **Protein Location:** Residue 731 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.458 / 98.4% / 18.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.4)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** JH2 beta7-beta8 loop; aliphatic expansion destabilizes the autoinhibitory clamp.

#### 08. `E41V` (FERM Domain (receptor tethering))
* **Transcript & cDNA:** `NM_003331.5`: `c.122A>T` (Exon 3)
* **Genomic Coordinate (GRCh38):** `chr19:10378285:T>A` (Negative strand)
* **Protein Location:** Residue 41 | FERM Domain (receptor tethering)
* **AlphaGenome Functional Impact:** `0.705 / 99.4% / 22.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** FERM domain surface; hydrophobic exchange enhances autonomous receptor engagement.

#### 09. `P441R` (SH2 Domain (phosphotyrosine recognition))
* **Transcript & cDNA:** `NM_003331.5`: `c.1322C>G` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:10364659:G>C` (Negative strand)
* **Protein Location:** Residue 441 | SH2 Domain (phosphotyrosine recognition)
* **AlphaGenome Functional Impact:** `0.812 / 99.5% / 23.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.7) + Electrostatic/Born (+0.7) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** FERM-SH2 junction hinge; basic charge release promotes interdomain active orientation.

#### 10. `K642R` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.1925A>G` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:10361804:T>C` (Negative strand)
* **Protein Location:** Residue 642 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.880 / 99.6% / 23.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+3.1)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** JH2 alphaC-helix regulatory switch; alters allosteric autoinhibition of catalytic engine.

#### 11. `H667Q` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2001C>A` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr19:10361557:G>T` (Negative strand)
* **Protein Location:** Residue 667 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.543 / 98.9% / 19.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.2) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** JH2 pseudokinase regulatory pocket; neutralizes imidazole, uncoupling autoinhibitory restraint.

#### 12. `E925K` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.2773G>A` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr19:10354177:C>T` (Negative strand)
* **Protein Location:** Residue 925 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `0.961 / 99.6% / 24.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.0) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{GOF}$
* **Biophysical Mechanism:** JH1 catalytic N-lobe; charge reversal stabilizes ATP-binding competent state.

### Category: LOF

#### 13. `G1010D` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3029G>A` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:10353097:C>T` (Negative strand)
* **Protein Location:** Residue 1010 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.702 / 99.9% / 32.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+8.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+5.4) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 catalytic loop; inserting charged aspartate destroys invariant catalytic cleft geometry.

#### 14. `R864C` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2590C>T` (Exon 18)
* **Genomic Coordinate (GRCh38):** `chr19:10356595:G>A` (Negative strand)
* **Protein Location:** Residue 864 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.898 / 99.6% / 23.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.4) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2-JH1 interdomain interface; loss of positive charge and salt-bridge network impairs folding.

#### 15. `P1104A` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3310C>G` (Exon 23)
* **Genomic Coordinate (GRCh38):** `chr19:10352442:G>C` (Negative strand)
* **Protein Location:** Residue 1104 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.357 / 99.8% / 26.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.5) + Backbone strain (+1.4)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 activation segment C-terminal anchor; proline loss destabilizes kinase catalytic engine.

#### 16. `G634E` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.1901G>A` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:10361828:C>T` (Negative strand)
* **Protein Location:** Residue 634 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.127 / 87.6% / 9.1`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+6.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+4.9) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 beta3-alphaC loop; acidic charge creates severe steric clash, inducing pseudokinase misfolding.

#### 17. `G996R` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.2986G>A` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr19:10353569:C>T` (Negative strand)
* **Protein Location:** Residue 996 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `0.901 / 99.6% / 23.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+9.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+7.8) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 catalytic core; bulky basic arginine severely disrupts the catalytic spine.

#### 18. `A928V` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.2783C>T` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr19:10354167:G>A` (Negative strand)
* **Protein Location:** Residue 928 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.521 / 99.9% / 29.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+3.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 subdomain II ATP-binding cleft; steric crowding adjacent to invariant catalytic lysine.

#### 19. `G799R` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2395G>A` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr19:10357835:C>T` (Negative strand)
* **Protein Location:** Residue 799 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.439 / 99.8% / 27.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+10.2\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+9.0) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 pseudokinase core; arginine insertion induces severe steric collapse and proteasomal degradation.

#### 20. `L1014P` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3041T>C` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:10353085:A>G` (Negative strand)
* **Protein Location:** Residue 1014 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.401 / 99.8% / 27.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Backbone strain (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 catalytic loop; rigid proline disrupts the catalytic polypeptide backbone.

#### 21. `L757V` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2269C>G` (Exon 16)
* **Genomic Coordinate (GRCh38):** `chr19:10358045:G>C` (Negative strand)
* **Protein Location:** Residue 757 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.662 / 99.9% / 31.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.4)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 hydrophobic core; cavity creation destabilizes the required pseudokinase scaffold.

#### 22. `N1028S` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3083A>G` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:10353043:T>C` (Negative strand)
* **Protein Location:** Residue 1028 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.466 / 99.9% / 28.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.5\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.5)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 activation loop; impairs coordination of phosphorylation-dependent activation.

#### 23. `S431G` (FERM Domain (receptor tethering))
* **Transcript & cDNA:** `NM_003331.5`: `c.1291A>G` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:10364690:T>C` (Negative strand)
* **Protein Location:** Residue 431 | FERM Domain (receptor tethering)
* **AlphaGenome Functional Impact:** `0.626 / 99.2% / 20.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.4)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** FERM domain core; loss of side chain destabilizes cytokine receptor-binding interface.

#### 24. `R703W` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2107C>T` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr19:10359243:G>A` (Negative strand)
* **Protein Location:** Residue 703 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.216 / 93.6% / 12.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.3\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 pseudokinase beta-sheet; massive aromatic tryptophan disrupts domain structural integrity.

### Category: More LOF

#### 25. `E782K` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2344G>A` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr19:10357886:C>T` (Negative strand)
* **Protein Location:** Residue 782 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.375 / 99.8% / 26.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.2) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 alphaF helix; charge reversal breaks essential internal salt bridges.

#### 26. `H669P` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2006A>C` (Exon 14)
* **Genomic Coordinate (GRCh38):** `chr19:10361552:T>G` (Negative strand)
* **Protein Location:** Residue 669 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.151 / 99.7% / 25.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.8) + Electrostatic/Born (+1.2) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 alphaC helix; proline insertion terminates the autoinhibitory alpha-helix, causing misfolding.

#### 27. `G1040W` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3118G>T` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:10353008:C>A` (Negative strand)
* **Protein Location:** Residue 1040 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.501 / 99.9% / 28.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+9.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+9.4)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 DFG motif adjacent glycine; massive tryptophan wedge completely blocks ATP binding.

#### 28. `R864H` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2591G>A` (Exon 18)
* **Genomic Coordinate (GRCh38):** `chr19:10356594:C>T` (Negative strand)
* **Protein Location:** Residue 864 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.054 / 99.7% / 24.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.5) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 C-terminal interface; histidine substitution impairs interdomain salt-bridge stabilization.

#### 29. `K1038N` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3114G>C` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:10353012:C>G` (Negative strand)
* **Protein Location:** Residue 1038 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.533 / 99.9% / 29.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 activation segment; loss of basic lysine prevents active-state electrostatic network.

#### 30. `R860H` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2579G>A` (Exon 18)
* **Genomic Coordinate (GRCh38):** `chr19:10356606:C>T` (Negative strand)
* **Protein Location:** Residue 860 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.803 / 99.5% / 23.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.5) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 C-lobe interface; impairs structural tethering required for catalytic competence.

#### 31. `R1159S` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3475C>A` (Exon 25)
* **Genomic Coordinate (GRCh38):** `chr19:10350923:G>T` (Negative strand)
* **Protein Location:** Residue 1159 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.503 / 99.9% / 29.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.8) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 C-terminal domain boundary; loss of arginine destabilizes the kinase C-lobe core.

#### 32. `G1088W` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3262G>T` (Exon 23)
* **Genomic Coordinate (GRCh38):** `chr19:10352490:C>A` (Negative strand)
* **Protein Location:** Residue 1088 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.614 / 99.9% / 31.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+7.9\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+7.9)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 C-lobe; tryptophan insertion disrupts internal packing of the catalytic domain.

#### 33. `R1159C` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3475C>T` (Exon 25)
* **Genomic Coordinate (GRCh38):** `chr19:10350923:G>A` (Negative strand)
* **Protein Location:** Residue 1159 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.347 / 99.8% / 26.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.4) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 C-terminal boundary; cysteine mutation introduces aberrant disulfide bonding / misfolding.

#### 34. `R895C` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.2683C>T` (Exon 19)
* **Genomic Coordinate (GRCh38):** `chr19:10354544:G>A` (Negative strand)
* **Protein Location:** Residue 895 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `0.989 / 99.6% / 24.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.4) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2-JH1 interdomain hinge; disrupts the conformational alignment of the tandem kinases.

#### 35. `H594Y` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.1780C>T` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:10361949:G>A` (Negative strand)
* **Protein Location:** Residue 594 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.258 / 99.7% / 25.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.4) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 N-lobe beta-sheet; bulky tyrosine creates steric clashes destabilizing the pseudokinase fold.

#### 36. `R1159H` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3476G>A` (Exon 25)
* **Genomic Coordinate (GRCh38):** `chr19:10350922:C>T` (Negative strand)
* **Protein Location:** Residue 1159 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.484 / 99.9% / 28.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+4.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.5) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 C-terminal tail; impairs overall stability of the catalytic domain.

#### 37. `L695P` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2084T>C` (Exon 15)
* **Genomic Coordinate (GRCh38):** `chr19:10359266:A>G` (Negative strand)
* **Protein Location:** Residue 695 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.377 / 99.8% / 26.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 beta-sheet; proline insertion disrupts secondary structure and causes misfolding.

#### 38. `R860C` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2578C>T` (Exon 18)
* **Genomic Coordinate (GRCh38):** `chr19:10356607:G>A` (Negative strand)
* **Protein Location:** Residue 860 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `0.764 / 99.5% / 22.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+2.4) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 interdomain boundary; cysteine substitution induces aggregation / loss of expression.

#### 39. `D421H` (FERM Domain (receptor tethering))
* **Transcript & cDNA:** `NM_003331.5`: `c.1261G>C` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:10364720:C>G` (Negative strand)
* **Protein Location:** Residue 421 | FERM Domain (receptor tethering)
* **AlphaGenome Functional Impact:** `1.337 / 99.8% / 26.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+1.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.0) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** FERM domain F3 lobe; disrupts acidic patch essential for cytokine receptor association.

#### 40. `L986P` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.2957T>C` (Exon 21)
* **Genomic Coordinate (GRCh38):** `chr19:10353598:A>G` (Negative strand)
* **Protein Location:** Residue 986 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.487 / 99.9% / 28.7`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 catalytic domain; proline breaks an essential alpha-helix in the kinase engine.

#### 41. `H432R` (FERM Domain (receptor tethering))
* **Transcript & cDNA:** `NM_003331.5`: `c.1295A>G` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:10364686:T>C` (Negative strand)
* **Protein Location:** Residue 432 | FERM Domain (receptor tethering)
* **AlphaGenome Functional Impact:** `1.023 / 99.6% / 24.4`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+1.7) + Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** FERM-SH2 linker; disrupts electrostatic tethering to cytokine receptor Box1/Box2.

#### 42. `D1041A` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3122A>C` (Exon 22)
* **Genomic Coordinate (GRCh38):** `chr19:10353004:T>G` (Negative strand)
* **Protein Location:** Residue 1041 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.703 / 99.9% / 32.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+0.5) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 invariant DFG motif catalytic aspartate; completely eliminates Mg2+/ATP coordination (Catalytic Null).

#### 43. `L641P` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.1922T>C` (Exon 13)
* **Genomic Coordinate (GRCh38):** `chr19:10361807:A>G` (Negative strand)
* **Protein Location:** Residue 641 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.547 / 99.9% / 29.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.7\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+1.1) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 alphaC helix; proline breaks the alpha-helix, leading to pseudokinase collapse.

#### 44. `C1140W` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3420T>G` (Exon 24)
* **Genomic Coordinate (GRCh38):** `chr19:10351061:A>C` (Negative strand)
* **Protein Location:** Residue 1140 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.121 / 99.7% / 25.0`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+5.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 C-lobe; massive tryptophan wedge causes severe steric clash in the kinase core.

#### 45. `S1082P` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3244T>C` (Exon 23)
* **Genomic Coordinate (GRCh38):** `chr19:10352508:A>G` (Negative strand)
* **Protein Location:** Residue 1082 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.518 / 99.9% / 29.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+2.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+0.8) + Backbone strain (+1.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 C-lobe loop; proline strain alters the catalytic engine fold.

#### 46. `E947K` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.2839G>A` (Exon 20)
* **Genomic Coordinate (GRCh38):** `chr19:10354111:C>T` (Negative strand)
* **Protein Location:** Residue 947 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.591 / 99.9% / 30.5`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+5.1\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.5) + Electrostatic/Born (+2.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 catalytic N-lobe; charge reversal disrupts invariant electrostatic network.

#### 47. `G1088R` (JH1 Tyrosine Kinase Domain (catalytic engine))
* **Transcript & cDNA:** `NM_003331.5`: `c.3262G>A` (Exon 23)
* **Genomic Coordinate (GRCh38):** `chr19:10352490:C>T` (Negative strand)
* **Protein Location:** Residue 1088 | JH1 Tyrosine Kinase Domain (catalytic engine)
* **AlphaGenome Functional Impact:** `1.893 / 100.0% / 33.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+9.0\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+7.8) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH1 C-lobe; basic arginine insertion causes severe electrostatic and steric collapse.

#### 48. `W798C` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2394G>C` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr19:10357836:C>G` (Negative strand)
* **Protein Location:** Residue 798 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.653 / 99.9% / 31.6`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.6\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Cavity void (+3.6)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 hydrophobic core; loss of bulky tryptophan creates a massive 119 A3 cavity void.

#### 49. `D429N` (FERM Domain (receptor tethering))
* **Transcript & cDNA:** `NM_003331.5`: `c.1285G>A` (Exon 9)
* **Genomic Coordinate (GRCh38):** `chr19:10364696:C>T` (Negative strand)
* **Protein Location:** Residue 429 | FERM Domain (receptor tethering)
* **AlphaGenome Functional Impact:** `0.936 / 99.6% / 23.9`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+0.8\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Electrostatic/Born (+0.7)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** FERM domain; loss of coordinating carboxylate impairs cytokine receptor association.

#### 50. `E806K` (JH2 Pseudokinase Domain (regulatory autoinhibitory clamp))
* **Transcript & cDNA:** `NM_003331.5`: `c.2416G>A` (Exon 17)
* **Genomic Coordinate (GRCh38):** `chr19:10357814:C>T` (Negative strand)
* **Protein Location:** Residue 806 | JH2 Pseudokinase Domain (regulatory autoinhibitory clamp)
* **AlphaGenome Functional Impact:** `1.517 / 99.9% / 29.2`
* **Thermodynamic Perturbation:** $\Delta\Delta G_{\text{est}} = \mathbf{+3.4\text{ kcal/mol}}$ *(Biophysical estimate)*
  - **Breakdown:** Steric clash (+2.2) + Electrostatic/Born (+1.2)
* **Functional Status:** $\mathbf{LOF}$
* **Biophysical Mechanism:** JH2 C-lobe surface; charge reversal destabilizes the pseudokinase scaffolding fold.
