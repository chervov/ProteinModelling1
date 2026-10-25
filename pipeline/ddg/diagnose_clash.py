"""Diagnose the TYK2 ddG magnitudes: reproduce the repo protocol, decompose the energy,
and test whether a more flexible protocol removes the extreme values.

Protocol A = pipeline/ddg/worker.py exactly: FastRelax(coord-constrained, 1 repeat) once per
structure, then mutate_residue(pack_radius=8.0), ddG = E(wt_repacked) - E(mut).  Negative =
destabilising (the paper's sign).
Protocol B = same, plus side-chain + backbone minimisation of the 8 A shell after mutation.
"""
import os, sys, json, time, urllib.request, traceback

W = "/tmp/ddg"
RAW = "https://raw.githubusercontent.com/chervov/ProteinModelling1/main/"
os.makedirs(W, exist_ok=True)

def log(*a):
    print(f"[{time.strftime('%H:%M:%S')}]", *a, flush=True)

import pyrosetta
from pyrosetta import pose_from_pdb, get_fa_scorefxn
from pyrosetta.toolbox import mutate_residue
from pyrosetta.rosetta.core.scoring import ScoreType
from pyrosetta.rosetta.protocols.relax import FastRelax
from pyrosetta.rosetta.protocols.constraint_generator import (
    CoordinateConstraintGenerator, AddConstraints)
from pyrosetta.rosetta.core.kinematics import MoveMap
from pyrosetta.rosetta.protocols.minimization_packing import MinMover

pyrosetta.init("-mute all -ex1 -ex2aro -ignore_unrecognized_res "
               "-ignore_zero_occupancy false -detect_disulf false")
SF = get_fa_scorefxn()

# ---------- structure: identical to the main run ----------
src = f"{W}/tyk2_af3_closed.pdb"
if not os.path.exists(src):
    urllib.request.urlretrieve(RAW + "TYK2/af3/tyk2_af3_closed.pdb", src)
cached = f"{W}/TYK2_relaxed_closed.pdb"
if os.path.exists(cached) and os.path.getsize(cached) > 100000:
    pose = pose_from_pdb(cached); log("loaded cached relax")
else:
    pose = pose_from_pdb(src)
    cg = CoordinateConstraintGenerator()
    ac = AddConstraints(); ac.add_generator(cg); ac.apply(pose)
    sf = SF.clone(); sf.set_weight(ScoreType.coordinate_constraint, 1.0)
    t0 = time.time(); FastRelax(sf, 1).apply(pose)
    log(f"relaxed in {time.time()-t0:.0f}s")
    pose.dump_pdb(cached)
log(f"{pose.total_residue()} residues, baseline {SF(pose):.1f} REU")

# per-residue energies of the relaxed WT: are there pre-existing hot spots?
SF(pose)
res_e = [(i, pose.energies().residue_total_energy(i)) for i in range(1, pose.total_residue() + 1)]
worst = sorted(res_e, key=lambda x: -x[1])[:8]
log("worst WT residue energies (REU):", [(i, round(e, 1)) for i, e in worst])

def terms(p):
    """Weighted score terms for a pose."""
    SF(p)
    tot = p.energies().total_energies()
    return {st.name: tot[st] * SF.get_weight(st)
            for st in SF.get_nonzero_weighted_scoretypes()}

def minimise_shell(p, pos):
    """Protocol B extra: minimise chi + bb of residues whose CA is within 8 A of pos."""
    mm = MoveMap()
    ca = p.residue(pos).xyz("CA")
    for i in range(1, p.total_residue() + 1):
        if p.residue(i).has("CA") and (p.residue(i).xyz("CA") - ca).norm() <= 8.0:
            mm.set_chi(i, True); mm.set_bb(i, True)
    MinMover(mm, SF, "lbfgs_armijo_nonmonotone", 0.01, True).apply(p)
    return p

# ---------- test set: extreme positions from the stored results, plus ordinary ones ----------
stored = json.load(urllib.request.urlopen(RAW + "data/ddg/ddg_TYK2_all.json", timeout=300))
by = {(r["pos"], r["alt"]): r for r in stored}
TESTS = [746, 964, 801, 667, 775]          # first three are the most extreme positions
ALTS = ["W", "F", "A", "G"]

rows = []
for pos in TESTS:
    wt = pose.residue(pos).name1()
    pw = pose.clone(); mutate_residue(pw, pos, wt, pack_radius=8.0)
    base = SF(pw); base_terms = terms(pw)
    for alt in ALTS:
        if alt == wt:
            continue
        try:
            pm = pose.clone(); mutate_residue(pm, pos, alt, pack_radius=8.0)
            a_ddg = base - SF(pm)                       # protocol A, paper sign
            mt = terms(pm)
            d_rep = mt.get("fa_rep", 0) - base_terms.get("fa_rep", 0)
            pb = minimise_shell(pm.clone(), pos)
            pwb = minimise_shell(pw.clone(), pos)
            b_ddg = SF(pwb) - SF(pb)                    # protocol B
            ref = by.get((pos, alt), {})
            rows.append(dict(pos=pos, wt=wt, alt=alt,
                             repo=ref.get("ddg_closed"), A=round(a_ddg, 1), B=round(b_ddg, 1),
                             d_fa_rep=round(d_rep, 1),
                             frac_rep=round(d_rep / max(abs(a_ddg), 1e-9), 2)))
            log(rows[-1])
        except Exception:
            log(f"{pos}{alt} FAILED\n{traceback.format_exc()}")
json.dump(rows, open(f"{W}/experiment.json", "w"), indent=1)
log("EXPERIMENT_DONE", len(rows), "variants")
