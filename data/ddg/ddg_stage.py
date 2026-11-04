"""Stage 2: Park 2016 cartesian ddG with the Frenz et al. 2020 modifications.

Per mutation and for the wild type:
  repack all residues with any atom within 6 A of the target, minimize those
  side chains plus the backbone of sequence-adjacent residues in Cartesian space,
  score with ref2015_cart.
Iterate until the two lowest energies agree within 1 REU, or 5 iterations
(Frenz et al. convergence rule), then take the LOWEST energy -- not the mean.
ddG = min(E_mutant) - min(E_wildtype).  Positive = destabilising.
Units are REU; ref2015 is calibrated so 1 REU ~ 1 kcal/mol and the source
benchmark applies no conversion factor.
"""
import os, sys, json, time, multiprocessing as mp

CONSTRUCTS = {"FERM_SH2": 20, "JH2_JH1": 545}   # construct -> first UniProt residue
SHELL, MIN_SHELL, MAXIT, CONV = 6.0, 10.0, 5, 1.0

def setup(pdb, seed):
    import pyrosetta
    pyrosetta.init(f"-score:weights ref2015_cart -ex1 -ex2 -mute all "
                   f"-fa_max_dis 9.0 -constant_seed -jran {seed}")
    return pyrosetta

def relax_site(pose, resi, pyrosetta, sf):
    """repack + cartesian-minimize the 6 A shell around resi; return score"""
    from pyrosetta.rosetta.core.pack.task import TaskFactory
    from pyrosetta.rosetta.core.pack.task.operation import (
        RestrictToRepacking, PreventRepacking, IncludeCurrent)
    from pyrosetta.rosetta.core.select.residue_selector import (
        ResidueIndexSelector, NeighborhoodResidueSelector)
    from pyrosetta.rosetta.protocols.minimization_packing import PackRotamersMover, MinMover
    from pyrosetta.rosetta.core.kinematics import MoveMap

    tgt = ResidueIndexSelector(str(resi))
    shell = NeighborhoodResidueSelector(tgt, SHELL, True)
    keep = shell.apply(pose)

    tf = TaskFactory(); tf.push_back(RestrictToRepacking()); tf.push_back(IncludeCurrent())
    prevent = PreventRepacking()
    for i in range(1, pose.total_residue() + 1):
        if not keep[i]:
            prevent.include_residue(i)
    tf.push_back(prevent)
    PackRotamersMover(sf, tf.create_task_and_apply_taskoperations(pose)).apply(pose)

    # Cartesian minimization must free backbone DOFs across the whole shell:
    # with only i+/-1 free, cart_bonded strain from MutateResidue cannot relax
    # and dominates the score (measured: 58.7 of 69.8 REU for V625F).
    mmsel = NeighborhoodResidueSelector(tgt, MIN_SHELL, True).apply(pose)
    mm = MoveMap()
    for i in range(1, pose.total_residue() + 1):
        if mmsel[i]:
            mm.set_chi(i, True); mm.set_bb(i, True)
    mv = MinMover(mm, sf, "lbfgs_armijo_nonmonotone", 1e-6, True)
    mv.cartesian(True); mv.max_iter(2000); mv.apply(pose)
    return sf(pose)

def converged_min(make_pose, resi, pyrosetta, sf):
    es, poses = [], []
    for it in range(MAXIT):
        p = make_pose()
        es.append(relax_site(p, resi, pyrosetta, sf)); poses.append(p)
        if len(es) >= 2 and abs(sorted(es)[0] - sorted(es)[1]) < CONV:
            break
    i = es.index(min(es))
    return min(es), len(es), poses[i]

def run_variant(args):
    variant, construct, pdb, offset, seed = args
    import pyrosetta
    pr = setup(pdb, seed)
    from pyrosetta import pose_from_pdb
    from pyrosetta.rosetta.protocols.simple_moves import MutateResidue
    AA3 = dict(A="ALA",R="ARG",N="ASN",D="ASP",C="CYS",E="GLU",Q="GLN",G="GLY",H="HIS",
               I="ILE",L="LEU",K="LYS",M="MET",F="PHE",P="PRO",S="SER",T="THR",
               W="TRP",Y="TYR",V="VAL")
    wt, pos, mt = variant[0], int(variant[1:-1]), variant[-1]
    resi = pos - offset + 1
    sf = pr.create_score_function("ref2015_cart")
    base = pose_from_pdb(pdb)
    obs = base.residue(resi).name1()
    if obs != wt:
        return {"variant": variant, "error": f"wt mismatch: pose has {obs}, expected {wt}"}
    t0 = time.time()
    from pyrosetta.rosetta.core.scoring import ScoreType
    e_wt, n_wt, p_wt = converged_min(lambda: base.clone(), resi, pr, sf)
    def mutant():
        p = base.clone(); MutateResidue(resi, AA3[mt]).apply(p); return p
    e_mt, n_mt, p_mt = converged_min(mutant, resi, pr, sf)
    W, M = p_wt.energies().total_energies(), p_mt.energies().total_energies()
    def dterm(st): return (M[st] - W[st]) * sf.get_weight(st)
    cb, rep = dterm(ScoreType.cart_bonded), dterm(ScoreType.fa_rep)
    ddg = e_mt - e_wt
    r = {"variant": variant, "construct": construct, "pose_resi": resi,
         "E_wt_REU": round(e_wt, 3), "E_mut_REU": round(e_mt, 3),
         "rosetta_cart_ddg": round(ddg, 3),
         "d_cart_bonded": round(cb, 2), "d_fa_rep": round(rep, 2),
         "frac_cart_bonded": round(cb / ddg, 2) if abs(ddg) > 1e-6 else None,
         "iters_wt": n_wt, "iters_mut": n_mt, "minutes": round((time.time()-t0)/60, 2)}
    print(json.dumps(r), flush=True)
    return r

if __name__ == "__main__":
    import pandas as pd
    plan = pd.read_csv("jak2_rosetta_plan.csv")
    best = {c: json.load(open(f"best_{c}.json"))["pdb"] for c in CONSTRUCTS}
    jobs = [(r.variant, r.construct, best[r.construct], CONSTRUCTS[r.construct], 100 + i)
            for i, r in enumerate(plan.itertuples()) if r.construct in best]
    print(f"{len(jobs)} variants on 8 cores", flush=True)
    t0 = time.time()
    with mp.Pool(8) as pool:
        res = pool.map(run_variant, jobs)
    json.dump(res, open("rosetta_ddg.json", "w"), indent=1)
    ok = [r for r in res if "error" not in r]
    print(f"\n{len(ok)}/{len(res)} succeeded in {(time.time()-t0)/60:.1f} min")
