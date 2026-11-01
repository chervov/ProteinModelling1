"""
gof_lof_classifier.py
---------------------
Deterministic decision classifier for inferring Gain-of-Function (GOF),
Loss-of-Function (LOF), or Neutral status for mutations in multi-domain
kinases (JAK2, TYK2, JAK3).
"""

from typing import Dict, Any

# JAK2 domain boundaries (canonical transcript ENST00000381652, 1,132 aa)
JAK2_DOMAINS = [
    {"name": "FERM Domain (F1 lobe)", "start": 37, "end": 120, "type": "FERM"},
    {"name": "FERM Domain (F2 lobe)", "start": 121, "end": 260, "type": "FERM"},
    {"name": "FERM Domain (F3 lobe)", "start": 261, "end": 380, "type": "FERM"},
    {"name": "SH2-like Domain", "start": 381, "end": 535, "type": "SH2"},
    {"name": "JH2 Pseudokinase Domain", "start": 536, "end": 812, "type": "JH2"},
    {"name": "JH2-JH1 Linker", "start": 813, "end": 839, "type": "LINKER"},
    {"name": "JH1 Catalytic Kinase Domain", "start": 840, "end": 1132, "type": "JH1"},
]

def get_jak2_domain(pos: int) -> Dict[str, str]:
    for d in JAK2_DOMAINS:
        if d["start"] <= pos <= d["end"]:
            return d
    return {"name": "Unannotated / Terminus", "type": "OTHER"}

def classify_variant(
    aa_pos: int,
    wt: str,
    mut: str,
    avi_phred: float,
    am_score: float,
    ddg_mean: float,
    features: Dict[str, float] = None
) -> Dict[str, Any]:
    """
    Classifies a variant into GOF, LOF, Complete Null (NMD), or Neutral.
    """
    if features is None:
        features = {}

    domain_info = get_jak2_domain(aa_pos)
    d_type = domain_info["type"]
    d_name = domain_info["name"]

    # Rule 1: Premature stop / Nonsense mutation
    if mut in ["X", "*", "Ter"] or features.get("PROTEIN_TERMINATION", 0.0) > 0.5:
        if d_type in ["FERM", "SH2", "JH2", "LINKER"]:
            return {
                "status": "Complete Loss-of-Function (Null / NMD)",
                "category": "LOF_NULL",
                "domain": d_name,
                "mechanism": "Premature termination codon terminates translation, deleting regulatory JH2 and catalytic JH1 domains; triggers NMD.",
                "clinical_impact": "Total absence of functional kinase; autosomal recessive severe disease / null phenotype."
            }
        else:
            return {
                "status": "Loss-of-Function (Truncation)",
                "category": "LOF",
                "domain": d_name,
                "mechanism": "Premature truncation of the catalytic core destroys kinase enzymatic activity.",
                "clinical_impact": "Severe catalytic loss-of-function."
            }

    # Rule 2: Energetically Neutral / Tolerated Polymorphism
    if ddg_mean < 0.8 and am_score < 0.30:
        return {
            "status": "Neutral / Wild-Type",
            "category": "NEUTRAL",
            "domain": d_name,
            "mechanism": "Conservative aliphatic or surface exchange accommodated within thermal fluctuations (<0.8 kcal/mol); zero active site or clamp perturbation.",
            "clinical_impact": "Normal physiological kinase regulation; benign population polymorphism."
        }

    # Rule 3: JH2 Pseudokinase Domain (The Autoinhibitory Switch)
    if d_type == "JH2":
        if ddg_mean >= 1.5 or avi_phred >= 20.0 or am_score >= 0.50:
            return {
                "status": "Gain-of-Function (GOF)",
                "category": "GOF",
                "domain": d_name,
                "mechanism": "Disrupts the autoinhibitory JH2 pseudokinase clamp holding JH1 shut, conferring constitutive catalytic firing while leaving the JH1 engine intact.",
                "clinical_impact": "Hyperactive downstream STAT phosphorylation; driver in chronic myeloproliferative neoplasms (MPNs) and erythrocytosis."
            }
        else:
            return {
                "status": "Neutral / Near-WT",
                "category": "NEUTRAL",
                "domain": d_name,
                "mechanism": "Minor perturbation in the JH2 hydrophobic core; regulatory clamp remains intact.",
                "clinical_impact": "Baseline kinase signaling; tolerated variant."
            }

    # Rule 4: JH1 Catalytic Kinase Core (The Enzymatic Engine)
    if d_type == "JH1":
        if ddg_mean >= 1.5 or am_score >= 0.50 or avi_phred >= 20.0:
            return {
                "status": "Loss-of-Function (LOF)",
                "category": "LOF",
                "domain": d_name,
                "mechanism": "Destabilizes catalytic core geometry, active site electrostatics, or substrate binding cleft, destroying kinase activity.",
                "clinical_impact": "Enzymatic kinase inactivation; loss of downstream signaling."
            }
        else:
            return {
                "status": "Neutral / Tolerated",
                "category": "NEUTRAL",
                "domain": d_name,
                "mechanism": "Surface exchange outside catalytic active site loops.",
                "clinical_impact": "Preserved kinase function."
            }

    # Rule 5: FERM Domain (Receptor Anchoring & Chaperoning)
    if d_type == "FERM":
        if ddg_mean >= 2.0 or am_score >= 0.50:
            return {
                "status": "Loss-of-Function (LOF)",
                "category": "LOF",
                "domain": d_name,
                "mechanism": "Destabilizes the FERM fold, impairing cytokine receptor association and reducing cell surface trafficking.",
                "clinical_impact": "Reduced cytokine sensitivity and signaling impairment."
            }
        else:
            return {
                "status": "Loss-of-Function (Hypomorph)",
                "category": "LOF_HYPOMORPH",
                "domain": d_name,
                "mechanism": "Mild conformational loosening at the receptor binding surface causing suboptimal receptor coupling.",
                "clinical_impact": "Blunted cytokine receptor response."
            }

    # Rule 6: SH2-like Domain
    if d_type == "SH2":
        if ddg_mean >= 2.0 or am_score >= 0.50:
            return {
                "status": "Loss-of-Function (LOF)",
                "category": "LOF",
                "domain": d_name,
                "mechanism": "Misfolds the SH2 module and disrupts inter-domain linker connectivity to JH2.",
                "clinical_impact": "Structural impairment of kinase activation."
            }
        else:
            return {
                "status": "Neutral / Near-WT",
                "category": "NEUTRAL",
                "domain": d_name,
                "mechanism": "Tolerated substitution in the SH2 domain.",
                "clinical_impact": "Baseline signaling."
            }

    # Fallback
    return {
        "status": "VUS",
        "category": "VUS",
        "domain": d_name,
        "mechanism": "Unclassified structural effect.",
        "clinical_impact": "Uncertain significance."
    }
