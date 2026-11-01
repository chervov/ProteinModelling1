"""
Biophysical Delta-Delta-G Approximator (DEPRECATED & RETRACTED)
=============================================================

WARNING / RETRACTION NOTICE (2026-11-01):
-----------------------------------------
This analytical approximation model has FAILED EMPIRICAL VALIDATION.
DO NOT USE THIS SCRIPT FOR VARIANT SCORING, RANKING, OR STABILITY PREDICTIONS.

Audit Findings:
1. Non-reproducible benchmark table: original claims did not match code execution.
2. Incapable of predicting stabilizing mutations (returns values >= 0.00 by construction).
3. Zero correlation (Spearman ~ 0) against experimental and established tools
   (ThermoMPNN, FoldX, mCSM, DDMut) on characterized JAK2 variants.
4. Operates without 3D structural coordinates; ignores backbone relaxation.
5. Contradicts crystallographic solvent accessibility (RSA) data.

Retained strictly for archival and pedagogical purposes.
For real stability predictions, use FoldX, Rosetta, ThermoMPNN, or DDMut.
"""

import sys

class BiophysicalDDGApproximator:
    def __init__(self):
        self.alpha = 0.040        # Steric clash coefficient (kcal/mol / A^3)
        self.kappa = 0.024        # Cavity coefficient (kcal/mol / A^3)
        self.gly_penalty = 2.42   # Glycine tight-turn disruption penalty
        self.born_penalty = 1.42  # Desolvation penalty for buried charges
        self.pro_penalty = 1.45   # Proline cyclic rigidity loss penalty

        # Empirical whole-residue volume scale (Zamyatnin, A^3)
        self.aa_volumes = {
            'G': 60.1,  'A': 88.6,  'S': 89.0,  'C': 108.5, 'D': 111.1,
            'P': 112.7, 'N': 114.1, 'T': 116.1, 'E': 138.4, 'V': 140.0,
            'Q': 143.8, 'H': 153.2, 'M': 162.9, 'I': 166.7, 'L': 166.7,
            'K': 168.6, 'F': 189.9, 'Y': 193.6, 'W': 227.8, 'R': 225.0
        }

        # Formal charges at pH 7.4
        self.aa_charges = {
            'D': -1.0, 'E': -1.0, 'K': 1.0, 'R': 1.0, 'H': 0.1,
            'G': 0.0, 'A': 0.0, 'S': 0.0, 'C': 0.0, 'P': 0.0,
            'N': 0.0, 'T': 0.0, 'V': 0.0, 'Q': 0.0, 'M': 0.0,
            'I': 0.0, 'L': 0.0, 'F': 0.0, 'Y': 0.0, 'W': 0.0
        }

    def compute_ddg(self, wt, mut, burial_index=0.8, is_tight_turn=False,
                    is_salt_bridge=False, is_catalytic_core=False,
                    is_autoinhibitory_switch=False):
        """
        DEPRECATED: Heuristic approximation of delta-delta-G.
        """
        wt = wt.upper()
        mut = mut.upper()

        v_wt = self.aa_volumes.get(wt, 140.0)
        v_mut = self.aa_volumes.get(mut, 140.0)
        delta_v = v_mut - v_wt

        q_wt = self.aa_charges.get(wt, 0.0)
        q_mut = self.aa_charges.get(mut, 0.0)
        delta_q = abs(q_mut) - abs(q_wt)

        # 1. Steric clash
        ddg_steric = 0.0
        if delta_v > 0:
            ddg_steric += self.alpha * delta_v * burial_index
            if is_autoinhibitory_switch:
                ddg_steric += 1.2

        if wt == 'G' and mut != 'G':
            ddg_steric += self.gly_penalty if is_tight_turn else 1.2

        # 2. Cavity creation
        ddg_cavity = 0.0
        if delta_v < 0:
            ddg_cavity += self.kappa * abs(delta_v) * burial_index
            if wt in ['F', 'Y', 'W'] and mut in ['A', 'V', 'G', 'S']:
                ddg_cavity += 1.1

        # 3. Electrostatics
        ddg_elec = 0.0
        if delta_q > 0:
            if burial_index > 0.5:
                ddg_elec += self.born_penalty * burial_index
            if is_catalytic_core:
                ddg_elec += 1.0

        if is_salt_bridge and abs(q_wt) > 0 and q_mut == 0:
            ddg_elec += 2.2

        # 4. Backbone strain / Proline
        ddg_backbone = 0.0
        if wt == 'P' and mut != 'P':
            ddg_backbone += self.pro_penalty
        elif wt != 'P' and mut == 'P':
            ddg_backbone += 1.8 if is_catalytic_core else 1.2

        # Aliphatic isomer mitigation
        if wt in ['V', 'I', 'L'] and mut in ['V', 'I', 'L']:
            ddg_steric = min(ddg_steric, 0.4)
            ddg_cavity = min(ddg_cavity, 0.4)

        ddg_total = ddg_steric + ddg_cavity + ddg_elec + ddg_backbone
        return {
            "wt": wt,
            "mut": mut,
            "delta_v": delta_v,
            "ddg_est": round(ddg_total, 2),
            "components": {
                "steric": round(ddg_steric, 2),
                "cavity": round(ddg_cavity, 2),
                "elec": round(ddg_elec, 2),
                "backbone": round(ddg_backbone, 2)
            }
        }

if __name__ == "__main__":
    print("=" * 80)
    print("WARNING: ddg_approximator.py is DEPRECATED and FAILED EMPIRICAL VALIDATION.")
    print("Do not use for ranking or stability predictions.")
    print("=" * 80)
