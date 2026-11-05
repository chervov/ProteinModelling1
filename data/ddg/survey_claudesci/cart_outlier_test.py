"""Does cartesian_ddg avoid the 4-residue outlier tail seen in the dual-state protocol?
Same 600 variants, same protein, same structure family - only the protocol differs."""
import pandas as pd, numpy as np, json, time, multiprocessing as mp
OFFSET=849   # JH1 construct starts at UniProt 849
AA3=dict(A="ALA",R="ARG",N="ASN",D="ASP",C="CYS",E="GLU",Q="GLN",G="GLY",H="HIS",I="ILE",
         L="LEU",K="LYS",M="MET",F="PHE",P="PRO",S="SER",T="THR",W="TRP",Y="TYR",V="VAL")

def work(chunk):
    import pyrosetta
    pyrosetta.init("-score:weights ref2015_cart -ex1 -ex2 -mute all -fa_max_dis 9.0 -constant_seed -jran 7")
    from pyrosetta import pose_from_pdb
    from pyrosetta.rosetta.protocols.simple_moves import MutateResidue
    from pyrosetta.rosetta.core.pack.task import TaskFactory
    from pyrosetta.rosetta.core.pack.task.operation import RestrictToRepacking,PreventRepacking,IncludeCurrent
    from pyrosetta.rosetta.core.select.residue_selector import ResidueIndexSelector,NeighborhoodResidueSelector
    from pyrosetta.rosetta.protocols.minimization_packing import PackRotamersMover,MinMover
    from pyrosetta.rosetta.core.kinematics import MoveMap
    from pyrosetta.rosetta.core.scoring import ScoreType
    sf=pyrosetta.create_score_function("ref2015_cart")
    base=pose_from_pdb("JH1_relaxed.pdb")
    def relax_site(pose,resi):
        tgt=ResidueIndexSelector(str(resi)); keep=NeighborhoodResidueSelector(tgt,6.0,True).apply(pose)
        tf=TaskFactory(); tf.push_back(RestrictToRepacking()); tf.push_back(IncludeCurrent())
        pr=PreventRepacking()
        for i in range(1,pose.total_residue()+1):
            if not keep[i]: pr.include_residue(i)
        tf.push_back(pr)
        PackRotamersMover(sf,tf.create_task_and_apply_taskoperations(pose)).apply(pose)
        ms=NeighborhoodResidueSelector(tgt,10.0,True).apply(pose); mm=MoveMap()
        for i in range(1,pose.total_residue()+1):
            if ms[i]: mm.set_chi(i,True); mm.set_bb(i,True)
        mv=MinMover(mm,sf,"lbfgs_armijo_nonmonotone",1e-6,True); mv.cartesian(True); mv.max_iter(2000)
        mv.apply(pose); return sf(pose)
    out=[]
    for rec in chunk:
        resi=rec["pos"]-OFFSET+1
        try:
            if base.residue(resi).name1()!=rec["wt"]:
                out.append({**rec,"err":"wt mismatch"}); continue
            wt=base.clone(); ew=relax_site(wt,resi)
            mu=base.clone(); MutateResidue(resi,AA3[rec["alt_aa"]]).apply(mu); em=relax_site(mu,resi)
            W=wt.energies().total_energies(); M=mu.energies().total_energies()
            cb=(M[ScoreType.cart_bonded]-W[ScoreType.cart_bonded])*sf.get_weight(ScoreType.cart_bonded)
            rep=(M[ScoreType.fa_rep]-W[ScoreType.fa_rep])*sf.get_weight(ScoreType.fa_rep)
            out.append({**rec,"cart_ddg":round(em-ew,3),"d_cart_bonded":round(cb,2),"d_fa_rep":round(rep,2)})
        except Exception as e:
            out.append({**rec,"err":f"{type(e).__name__}:{str(e)[:60]}"})
    return out

if __name__=="__main__":
    S=pd.read_csv("outlier_sample.csv").to_dict("records")
    chunks=[S[i::8] for i in range(8)]
    t0=time.time()
    with mp.Pool(8) as pool: res=sum(pool.map(work,chunks),[])
    dt=time.time()-t0
    pd.DataFrame(res).to_csv("cart_outlier_result.csv",index=False)
    ok=[r for r in res if "cart_ddg" in r]
    print(f"DONE {len(ok)}/{len(res)} in {dt/60:.1f} min  ({dt/max(len(ok),1):.2f} s/variant wall, 8 cores)")
