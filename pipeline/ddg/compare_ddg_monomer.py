"""Run Rosetta's OWN ddG protocol (ddGMover = ddg_monomer / Kellogg et al. 2011) on the
variants where the pipeline reports thousands. ddGMover ramps the repulsive term and minimises
with coordinate constraints, which is exactly what the repack-only protocol lacks.

Rosetta convention here: POSITIVE = destabilising (opposite of the paper's sign).
"""
import json, time, traceback
import pyrosetta
from pyrosetta import pose_from_pdb, get_fa_scorefxn
from pyrosetta.rosetta.protocols.ddg import ddGMover
from pyrosetta.rosetta.utility import vector1_core_chemical_AA
from pyrosetta.rosetta.core.chemical import aa_from_oneletter_code

pyrosetta.init("-mute all -ex1 -ex2aro -ignore_unrecognized_res "
               "-ignore_zero_occupancy false -detect_disulf false")
sfxn = get_fa_scorefxn()
pose = pose_from_pdb("/tmp/ddg/TYK2_relaxed_closed.pdb")
n = pose.total_residue()
print(f"pose {n} residues, {sfxn(pose):.1f} REU", flush=True)

# pipeline values, for the comparison
PIPE = {("G", 746, "W"): -2988.6, ("G", 746, "A"): -228.8, ("G", 801, "W"): -3047.9,
        ("H", 667, "F"): -17.8, ("R", 775, "A"): 1.5}

def kellogg(position, alt, iterations=3):
    muts = vector1_core_chemical_AA(n)
    for i in range(1, n + 1):
        muts[i] = pose.residue(i).aa()
    muts[position] = aa_from_oneletter_code(alt)
    mover = ddGMover(sfxn, sfxn, muts)
    mover.set_min_cst(True)        # minimise with coordinate constraints (ddg_monomer row 16)
    mover.set_min(True)            # take the lowest of the decoys
    mover.set_mean(False)
    mover.restrict_to_nbrs(True)   # only repack/minimise the neighbourhood
    mover.num_iterations(iterations)
    work = pose.clone()
    t0 = time.time()
    mover.apply(work)
    return mover.ddG(), time.time() - t0

out = []
for (wt, pos, alt), pipe in PIPE.items():
    try:
        value, secs = kellogg(pos, alt)
        rec = {"variant": f"{wt}{pos}{alt}", "pipeline_ddg": pipe,
               "kellogg_REU": round(value, 2),
               "kellogg_kcal": round(value / 2.94, 2),   # documented REU -> kcal/mol factor
               "seconds": round(secs)}
        out.append(rec)
        print(json.dumps(rec), flush=True)
        json.dump(out, open("/tmp/ddg/kellogg.json", "w"), indent=1)
    except Exception:
        print(f"{wt}{pos}{alt} FAILED\n{traceback.format_exc()}", flush=True)
json.dump(out, open("/tmp/ddg/kellogg.json", "w"), indent=1)
print("KELLOGG_DONE", len(out), flush=True)
