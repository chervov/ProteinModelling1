# Functional Impact & GOF / LOF Prediction Algorithm for Tandem Kinases

## 1. Executive Summary & Core Principle

> [!IMPORTANT]
> **Implementation Note:**
> In the current pipeline, AlphaGenome AVI scores and Ensembl coordinates are queried live via API. The $\Delta\Delta G$ values used in the decision rules represent **theoretical biophysical estimations** parameterized from structural literature and electrostatic rules, rather than local executions of FoldX or Rosetta.


Determining whether a genetic variant produces a **Gain-of-Function (GOF)**, **Loss-of-Function (LOF)**, or **Neutral** phenotype is one of the most critical challenges in variant interpretation. 

Standard machine learning tools (e.g., **AlphaMissense**, **SIFT**, **PolyPhen-2**) and thermodynamic forcefields (e.g., **FoldX**, **Rosetta**) are trained to detect **structural disruption** or **evolutionary conservation**. **They cannot inherently differentiate between activation and inactivation** because:
* A mutation that destabilizes an active site causes **Loss-of-Function (LOF)**.
* A mutation that destabilizes an autoinhibitory contact surface causes **Gain-of-Function (GOF)**.

In multi-domain signaling kinases like **JAK2**, **TYK2**, and **JAK3**, the functional outcome is governed by the **Tandem Kinase Allosteric Switch Model**. This document specifies the exact algorithmic framework used to deduce functional status by coupling genomic and structural data.

---

## 2. Mathematical Formalization of the Deduction Algorithm

Let a variant be defined by the tuple:
$$V = (G, p, \text{WT}, \text{Mut}, C_{\text{genomic}})$$

where $G$ is the gene symbol, $p$ is the amino acid position, $\text{WT}$ is the wild-type residue, $\text{Mut}$ is the mutant residue, and $C_{\text{genomic}}$ is the verified genomic coordinate.

### Inputs to the Classifier:
1. **Domain Assignment:** $D(p) \in \{\text{FERM}, \text{SH2-like}, \text{JH2 Pseudokinase}, \text{JH1 Catalytic}, \text{Linker}\}$
2. **AlphaGenome Variant Impact:**
   - Calibrated Phred score: $\Phi_{\text{AVI}} \in [0, 60]$
   - Calibrated Quantile: $Q_{\text{AVI}} \in [0, 1]$
   - Feature Attribution Vector: $\vec{F}_{\text{AVI}} = [f_{\text{Cactus}}, f_{\text{PhastCons}}, f_{\text{AM}}, f_{\text{Splice}}, f_{\text{Term}}, \dots]$
3. **Protein Pathogenicity Score:**
   - AlphaMissense prediction: $S_{\text{AM}} \in [0, 1]$
4. **Biophysical Thermodynamic Stability:**
   - Consensus Free Energy Change: $\Delta\Delta G_{\text{consensus}} = \Delta G_{\text{mut}} - \Delta G_{\text{wt}}$ ($\text{kcal/mol}$)
5. **Mutation Modality:**
   - $M \in \{\text{Missense}, \text{Nonsense (Stop)}, \text{Synonymous}, \text{Frameshift}\}$

---

## 3. Decision Logic & Pseudocode

```python
def classify_functional_status(variant, domain, mutation_type, avi_phred, am_score, ddg_mean, features):
    # Rule 1: Premature Protein Termination (Nonsense / Null)
    if mutation_type == "Nonsense" or features.get("PROTEIN_TERMINATION", 0) > 0.5:
        if domain in ["FERM", "SH2-like", "JH2 Pseudokinase", "Linker"]:
            return {
                "status": "Complete Loss-of-Function (Null / NMD)",
                "mechanism": "Premature termination codon deletes downstream regulatory and catalytic domains, triggering nonsense-mediated decay (NMD)."
            }
        elif domain == "JH1 Catalytic":
            return {
                "status": "Loss-of-Function (Truncation)",
                "mechanism": "Premature truncation of the catalytic kinase engine eliminates enzymatic activity."
            }

    # Rule 2: Energetically Neutral / Tolerated Polymorphism
    if ddg_mean < 0.8 and am_score < 0.34 and avi_phred < 20.0:
        return {
            "status": "Neutral / Wild-Type",
            "mechanism": "Conservative substitution fully accommodated without altering domain stability or regulatory interfaces."
        }

    # Rule 3: JH2 Pseudokinase Domain (The Autoinhibitory Switch)
    if domain == "JH2 Pseudokinase":
        # Check if the mutation disrupts the autoinhibitory clamp
        if ddg_mean >= 1.5 or avi_phred >= 20.0 or am_score >= 0.50:
            # High conservation + structural destabilization in JH2 relieves the negative clamp
            return {
                "status": "Gain-of-Function (GOF)",
                "mechanism": "Destabilizes the autoinhibitory JH2-JH1 contact interface, relieving the regulatory clamp and conferring constitutive catalytic activity on JH1."
            }
        else:
            return {
                "status": "Neutral / Near-WT",
                "mechanism": "Conservative exchange in JH2 preserved in the hydrophobic core; autoinhibitory clamp remains intact."
            }

    # Rule 4: JH1 Catalytic Kinase Domain (The Enzymatic Engine)
    if domain == "JH1 Catalytic":
        if ddg_mean >= 1.5 or am_score >= 0.56 or avi_phred >= 20.0:
            return {
                "status": "Loss-of-Function (LOF)",
                "mechanism": "Structural or electrostatic disruption of the catalytic kinase core impairs ATP binding, cleft dynamics, or substrate phosphotransfer."
            }
        else:
            return {
                "status": "Neutral / Tolerated",
                "mechanism": "Surface or conservative exchange in JH1 that preserves catalytic active site geometry."
            }

    # Rule 5: FERM Domain (Receptor Tethering & Chaperoning)
    if domain == "FERM":
        if ddg_mean >= 2.0 or am_score >= 0.56:
            return {
                "status": "Loss-of-Function (LOF)",
                "mechanism": "Destabilizes the FERM fold, impairing cytokine receptor association and reducing cell surface trafficking."
            }
        else:
            return {
                "status": "Loss-of-Function (Hypomorph) / VUS",
                "mechanism": "Mild conformational loosening at the receptor binding surface causing suboptimal receptor coupling."
            }

    # Rule 6: SH2-like Domain (Structural Inter-domain Node)
    if domain == "SH2-like":
        if ddg_mean >= 2.0 or am_score >= 0.56:
            return {
                "status": "Loss-of-Function (LOF)",
                "mechanism": "Disrupts the structural integrity of the SH2 fold and perturbs inter-domain linker connectivity."
            }
        else:
            return {
                "status": "Neutral / Near-WT",
                "mechanism": "Tolerated substitution in the SH2 domain."
            }

    # Default fallback
    return {"status": "Variant of Uncertain Significance (VUS)", "mechanism": "Unclassified."}
```

---

## 4. Origin & Methodology for Thermodynamic Stability ($\Delta\Delta G$)

### What $\Delta\Delta G$ Measures:
$$\Delta\Delta G = \Delta G_{\text{mutant}} - \Delta G_{\text{wild-type}}$$
* In **FoldX**, **Rosetta**, and **PopMusic**: $\Delta\Delta G > 0$ indicates **destabilization** (the mutant is less stable than WT). A threshold of $\Delta\Delta G \ge 1.5\text{ kcal/mol}$ is typically destabilizing; $\ge 2.5\text{ kcal/mol}$ is severely destabilizing.
* In **mCSM** and **DUET**: $\Delta\Delta G < 0$ indicates **destabilization**.

### Where Are $\Delta\Delta G$ Values Sourced?
In molecular modeling workflows, $\Delta\Delta G$ values are derived from two primary modalities:

1. **Local Physical Simulation Suites:**
   * **FoldX 5.0:** Employs an empirical physical forcefield parameterizing van der Waals clashes ($\Delta\Delta G_{\text{vdw}}$), electrostatic interactions ($\Delta\Delta G_{\text{elec}}$), hydrogen bonding ($\Delta\Delta G_{\text{hbond}}$), and solvation free energy. Evaluated on high-resolution crystal structures (e.g., PDB `4IVA` for JAK2 JH2–JH1 tandem kinase, or AlphaFold model `AF-O60674-F1`).
   * **Rosetta `cartesian_ddg`:** Implements full-atom Monte Carlo conformational sampling with Cartesian energy minimization using the `ref2015` scoring function.

2. **Web Services & Structural Knowledgebases:**
   * **DUET / mCSM Web Server** (*University of Melbourne / BioSig*): Uses graph-based structural signatures and machine-learning consensus to estimate stability changes from PDB coordinates.
   * **PopMusic 3.1** (*Université Libre de Bruxelles*): Uses statistical knowledge-based torsional potentials derived from known protein structures.
   * **Pre-computed Parameterization / Literature Benchmarks:** In rapid variant screening pipelines, standard biophysical penalties are calibrated based on established structural rules:
     * Burying a charged carboxylate ($-\text{COO}^-$) in a hydrophobic core: $+1.2\text{ to }+1.5\text{ kcal/mol}$ electrostatic penalty.
     * Introducing a bulky, branched Arginine into a tight Glycine turn: $+2.2\text{ to }+2.8\text{ kcal/mol}$ van der Waals steric clash.
     * Conservative aliphatic swaps ($V \leftrightarrow I$, $L \leftrightarrow I$): $+0.2\text{ to }+0.7\text{ kcal/mol}$ (within thermal noise $k_B T \approx 0.6\text{ kcal/mol}$).

---

## 5. Domain Architecture of Human JAK2

Human JAK2 consists of **1,132 amino acids** structured into four major functional units:

| Domain | Residues | Primary Structural Role | Primary Mutation Consequence |
| :--- | :--- | :--- | :--- |
| **FERM Domain** | 37–380 | Receptor anchoring (EPOR, TPOR, G-CSFR) & chaperone | Destabilization $\implies$ **LOF** (Loss of receptor binding) |
| **SH2-like Domain** | 381–535 | Structural linker between FERM and kinase modules | Destabilization $\implies$ **LOF / Null** (Misfolding / NMD) |
| **JH2 Pseudokinase** | 536–812 | Autoinhibitory clamp keeping JH1 in inactive conformation | Destabilization $\implies$ **GOF** (Constitutive activation) |
| **JH1 Catalytic Core** | 840–1132 | Catalytic tyrosine kinase (ATP binding & phosphotransfer) | Destabilization $\implies$ **LOF** (Enzymatic inactivation) |
