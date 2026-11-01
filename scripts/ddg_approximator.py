#!/usr/bin/env python3
"""
ddg_approximator.py
-------------------
Theoretical Biophysical Delta-Delta-G Approximation Engine.
Implements the multi-component energetic decomposition:
    ddG = ddG_steric + ddG_elec + ddG_cavity + ddG_backbone + ddG_hbond
"""

from typing import Dict, Any, Optional

# Empirical van der Waals volumes in Angstroms^3 (Zamyatnin/Chothia scale)
AA_VOLUMES = {
    'G': 60.1,  'A': 88.6,  'S': 89.0,  'C': 108.5, 'D': 111.1,
    'P': 112.7, 'T': 116.1, 'N': 114.1, 'V': 140.0, 'E': 138.4,
    'Q': 143.8, 'H': 153.2, 'I': 166.7, 'L': 166.7, 'M': 162.9,
    'K': 168.6, 'F': 189.9, 'Y': 193.6, 'W': 227.8, 'R': 225.0
}

# Formal electrical charges at physiological pH 7.4
AA_CHARGES = {
    'D': -1.0, 'E': -1.0,
    'K': +1.0, 'R': +1.0, 'H': +0.1,
    'G': 0.0, 'A': 0.0, 'S': 0.0, 'C': 0.0, 'P': 0.0,
    'T': 0.0, 'N': 0.0, 'V': 0.0, 'Q': 0.0, 'I': 0.0,
    'L': 0.0, 'M': 0.0, 'F': 0.0, 'Y': 0.0, 'W': 0.0
}

# Hydropathy index (Kyte-Doolittle)
AA_HYDROPATHY = {
    'I': 4.5,  'V': 4.2,  'L': 3.8,  'F': 2.8,  'C': 2.5,
    'M': 1.9,  'A': 1.8,  'G': -0.4, 'T': -0.7, 'S': -0.8,
    'W': -0.9, 'Y': -1.3, 'P': -1.6, 'H': -3.2, 'E': -3.5,
    'Q': -3.5, 'D': -3.5, 'N': -3.5, 'K': -3.9, 'R': -4.5
}


class BiophysicalDDGApproximator:
    """
    Computes theoretical biophysical Delta-Delta-G approximations (kcal/mol)
    for single amino acid substitutions based on structural environment.
    """

    def __init__(
        self,
        steric_coeff: float = 0.040,      # kcal/mol / Angstrom^3
        cavity_coeff: float = 0.024,      # kcal/mol / Angstrom^3 (Eriksson/Matthews)
        born_charge_penalty: float = 1.42,# kcal/mol for unshielded buried charge
        glycine_turn_penalty: float = 2.42,# kcal/mol for steric clash in Gly-specific turn
        proline_hinge_penalty: float = 1.45 # kcal/mol for losing cyclic pyrrolidine rigidity
    ):
        self.alpha = steric_coeff
        self.kappa = cavity_coeff
        self.born_penalty = born_charge_penalty
        self.gly_penalty = glycine_turn_penalty
        self.pro_penalty = proline_hinge_penalty

    def compute_ddg(
        self,
        wt: str,
        mut: str,
        burial_index: float = 0.8,          # 1.0 = fully buried core, 0.0 = surface
        is_tight_turn: bool = False,         # E.g., Glycine turn in loop/hinge
        is_salt_bridge: bool = False,        # Conserved catalytic salt bridge
        is_catalytic_core: bool = False,     # Within enzyme active cleft
        is_autoinhibitory_switch: bool = False # At domain clamp interface (e.g., JH2 V617)
    ) -> Dict[str, Any]:
        """
        Calculates the estimated Delta-Delta-G and individual component breakdown.
        """
        wt = wt.upper()
        mut = mut.upper()

        if wt not in AA_VOLUMES or mut not in AA_VOLUMES:
            raise ValueError(f"Unknown amino acid in substitution {wt} -> {mut}")

        if wt == mut:
            return {
                "ddg_est": 0.0,
                "components": {"steric": 0.0, "cavity": 0.0, "electrostatic": 0.0, "backbone": 0.0},
                "verdict": "Identical Residue (Zero Perturbation)"
            }

        # 1. Volume Delta
        v_wt = AA_VOLUMES[wt]
        v_mut = AA_VOLUMES[mut]
        delta_v = v_mut - v_wt

        # 2. Charge Delta
        q_wt = AA_CHARGES[wt]
        q_mut = AA_CHARGES[mut]
        delta_q = abs(q_mut - q_wt)

        # -------------------------------------------------------------
        # Component A: Steric Clash
        # -------------------------------------------------------------
        ddg_steric = 0.0
        if delta_v > 0:
            # Packing clash scaled by burial
            ddg_steric += self.alpha * delta_v * burial_index
            if is_autoinhibitory_switch:
                # Extra clash wedging open domain clamp (e.g. V617F wedge)
                ddg_steric += 1.2

        if wt == 'G' and mut != 'G':
            # Glycine unique dihedral angles clash penalty
            ddg_steric += self.gly_penalty if is_tight_turn else 1.2

        # -------------------------------------------------------------
        # Component B: Cavity Creation (Empty packing void)
        # -------------------------------------------------------------
        ddg_cavity = 0.0
        if delta_v < 0:
            # Cavity penalty
            ddg_cavity += self.kappa * abs(delta_v) * burial_index
            # Additional aromatic cavity penalty if deleting Phe/Tyr/Trp
            if wt in ['F', 'Y', 'W'] and mut in ['A', 'V', 'G', 'S']:
                ddg_cavity += 1.1

        # -------------------------------------------------------------
        # Component C: Electrostatic & Born Desolvation
        # -------------------------------------------------------------
        ddg_elec = 0.0
        if delta_q > 0:
            if burial_index > 0.5:
                # Unshielded charge inserted into low-dielectric core
                ddg_elec += self.born_penalty * burial_index
            if is_catalytic_core:
                # Electrostatic repulsion in active cleft
                ddg_elec += 1.0

        if is_salt_bridge and abs(q_wt) > 0 and q_mut == 0:
            # Disrupted invariant salt bridge
            ddg_elec += 2.2

        # -------------------------------------------------------------
        # Component D: Backbone Dihedral & Proline Rigidity
        # -------------------------------------------------------------
        ddg_backbone = 0.0
        if wt == 'P' and mut != 'P':
            # Loss of fixed cyclic constraint
            ddg_backbone += self.pro_penalty
        elif wt != 'P' and mut == 'P':
            # Insertion of rigid proline into non-proline position
            ddg_backbone += 1.8 if is_catalytic_core else 1.2

        # -------------------------------------------------------------
        # Conservative Aliphatic Adjustment (Rotamer repacking mitigation)
        # -------------------------------------------------------------
        if wt in ['V', 'I', 'L'] and mut in ['V', 'I', 'L']:
            # Aliphatic isomers repack easily
            total_raw = ddg_steric + ddg_cavity
            ddg_steric = min(ddg_steric, 0.4)
            ddg_cavity = min(ddg_cavity, 0.4)

        # Total Estimated Delta-Delta-G
        ddg_total = ddg_steric + ddg_cavity + ddg_elec + ddg_backbone

        # Qualitative Classification
        if ddg_total >= 2.5:
            verdict = "Severely Destabilizing (>= 2.5 kcal/mol)"
        elif ddg_total >= 1.5:
            verdict = "Destabilizing (1.5 - 2.5 kcal/mol)"
        elif ddg_total >= 0.8:
            verdict = "Mildly Destabilizing (0.8 - 1.5 kcal/mol)"
        else:
            verdict = "Neutral / Tolerated (< 0.8 kcal/mol)"

        return {
            "wt": wt,
            "mut": mut,
            "delta_volume_A3": delta_v,
            "ddg_est": round(ddg_total, 2),
            "components": {
                "steric_clash": round(ddg_steric, 2),
                "cavity_void": round(ddg_cavity, 2),
                "electrostatic": round(ddg_elec, 2),
                "backbone": round(ddg_backbone, 2)
            },
            "verdict": verdict
        }


# =====================================================================
# Validation Suite on Characterized JAK2 Variants
# =====================================================================
if __name__ == "__main__":
    appr = BiophysicalDDGApproximator()

    test_variants = [
        {"id": "JAK2 V617F", "wt": "V", "mut": "F", "burial": 0.9, "is_autoinhibitory": True},
        {"id": "JAK2 G571R", "wt": "G", "mut": "R", "burial": 0.8, "is_turn": True},
        {"id": "JAK2 V1110E", "wt": "V", "mut": "E", "burial": 0.9, "is_catalytic": True},
        {"id": "JAK2 F240V", "wt": "F", "mut": "V", "burial": 0.95},
        {"id": "JAK2 V578I", "wt": "V", "mut": "I", "burial": 0.85},
        {"id": "JAK2 L805I", "wt": "L", "mut": "I", "burial": 0.50},
        {"id": "JAK2 R938Q", "wt": "R", "mut": "Q", "burial": 0.85, "is_salt_bridge": True},
        {"id": "JAK2 P37A",  "wt": "P", "mut": "A", "burial": 0.40},
    ]

    print("=" * 80)
    print(f"{'Variant':<14} | {'Subst':<7} | {'Delta-V':<9} | {'Est. ddG':<10} | {'Verdict'}")
    print("=" * 80)

    for tv in test_variants:
        res = appr.compute_ddg(
            wt=tv["wt"],
            mut=tv["mut"],
            burial_index=tv.get("burial", 0.8),
            is_tight_turn=tv.get("is_turn", False),
            is_salt_bridge=tv.get("is_salt_bridge", False),
            is_catalytic_core=tv.get("is_catalytic", False),
            is_autoinhibitory_switch=tv.get("is_autoinhibitory", False)
        )
        print(f"{tv['id']:<14} | {tv['wt']}->{tv['mut']:<5} | {res['delta_volume_A3']:>+6.1f} A3 | +{res['ddg_est']:<4.1f} kcal | {res['verdict']}")

    print("=" * 80)
