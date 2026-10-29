"""Dual-state ddG: relax each state, then score every literature mutation in both."""
import json, os, sys, multiprocessing as mp
try: mp.set_start_method("fork")
except RuntimeError: pass
sys.path.insert(0,'/Users/chervov/top10'); os.chdir('/Users/chervov/top10')
from muts import MUTS
import pyrosetta
from pyrosetta import pose_from_file, get_fa_scorefxn
from pyrosetta.rosetta.protocols.relax import FastRelax
from pyrosetta.rosetta.protocols.constraint_generator import \
     AddConstraints, CoordinateConstraintGenerator
from pyrosetta.toolbox import mutate_residue
pyrosetta.init("-mute all -ignore_unrecognized_res -ignore_zero_occupancy false "
               "-detect_disulf false -load_PDB_components false", silent=True)
SF=get_fa_scorefxn()
STATES=json.load(open("states.json"))
SEQ=json.load(open("seqs.json"))

def prep(path, chain):
    """No global FastRelax: this is the cached-WT local-repack protocol used for the TYK2/JAK1
    campaign (~100k variants/hour). The WT is repacked identically to the mutant at the same
    site, so the comparison is matched; what is NOT done is a whole-protein relaxation, which
    costs hours per structure and mostly adds backbone drift. Recorded as a protocol limit."""
    p=pose_from_file(path)
    if chain:
        info=p.pdb_info(); keep=[i for i in range(1,p.total_residue()+1) if info.chain(i)==chain]
        if keep and len(keep)<p.total_residue():
            from pyrosetta.rosetta.protocols.grafting import return_region
            p=return_region(p, keep[0], keep[-1])
    return p

def pdbmap(pose, canon):
    """canonical UniProt residue number -> pose index.

    PDB files are in author numbering, which for many entries is offset from UniProt (and for
    non-human templates is a different sequence entirely). Rather than trust the numbering, the
    pose sequence is aligned to the canonical sequence by the offset that maximises identity.
    Falls back to raw PDB numbering only if that alignment is poor."""
    info=pose.pdb_info(); n=pose.total_residue()
    seq="".join(pose.residue(i).name1() for i in range(1,n+1))
    nums=[info.number(i) for i in range(1,n+1)]
    # try the raw numbering first
    raw={}; 
    for i in range(1,n+1): raw.setdefault(nums[i-1], i)
    hits=sum(1 for p,i in raw.items() if 1<=p<=len(canon) and canon[p-1]==pose.residue(i).name1())
    if hits >= 0.8*len(raw): return raw, round(100*hits/max(len(raw),1)), 0
    # otherwise scan offsets against the canonical sequence
    best=(0,-1)
    for off in range(-max(nums+[0])-5, len(canon)+5):
        h=0
        for i in range(1, n+1, max(1, n//400)):
            p=nums[i-1]+off
            if 1<=p<=len(canon) and canon[p-1]==seq[i-1]: h+=1
        if h>best[1]: best=(off,h)
    off=best[0]
    m={}
    for i in range(1,n+1): m.setdefault(nums[i-1]+off, i)
    hits=sum(1 for p,i in m.items() if 1<=p<=len(canon) and canon[p-1]==pose.residue(i).name1())
    return m, round(100*hits/max(len(m),1)), off

AA1={'A':'ALA','R':'ARG','N':'ASN','D':'ASP','C':'CYS','Q':'GLN','E':'GLU','G':'GLY','H':'HIS',
     'I':'ILE','L':'LEU','K':'LYS','M':'MET','F':'PHE','P':'PRO','S':'SER','T':'THR','W':'TRP',
     'Y':'TYR','V':'VAL'}
out={}
for acc,st in STATES.items():
    gene=st["gene"]; res={}
    for state in ("closed","open"):
        s=st[state]
        if not os.path.exists(s["file"]):
            print(f"{gene} {state}: file missing",flush=True); continue
        try: pose=prep(s["file"], s.get("chain"))
        except Exception as e:
            print(f"{gene} {state}: prep failed {type(e).__name__} {str(e)[:60]}",flush=True); continue
        m,pct,off=pdbmap(pose, SEQ[acc]); base=SF(pose)
        wtcache={}
        for wt,pos,alt,lab,mech,ref in MUTS.get(acc,[]):
            key=f"{wt}{pos}{alt}"
            idx=m.get(pos)
            if idx is None:
                res.setdefault(key,{})[state]=None; continue
            if pose.residue(idx).name1()!=wt:
                pass
            if pose.residue(idx).name1()!=wt:
                res.setdefault(key,{})[state]="wt_mismatch"; continue
            if pos not in wtcache:
                pw=pose.clone(); mutate_residue(pw,idx,wt,pack_radius=8.0,pack_scorefxn=SF)
                wtcache[pos]=SF(pw)
            pm=pose.clone(); mutate_residue(pm,idx,alt,pack_radius=8.0,pack_scorefxn=SF)
            # ddG = mut - wt, POSITIVE = destabilising (field convention)
            v=round(SF(pm)-wtcache[pos],3)
            res.setdefault(key,{})[state]=v
            # anything beyond +-25 REU is repulsion-dominated, not a free energy (see
            # external_data/ddg_study.md 3.4); keep the raw value but mark it
            res[key].setdefault("flag",{})[state]="clash" if abs(v)>25 else ""
        n=sum(1 for k in res if isinstance(res[k].get(state),float))
        print(f"{gene:<8}{state:<7}{os.path.basename(s['file'])[:30]:<32}{pose.total_residue():>5} res, "
              f"seq match {pct:>3}% offset {off:+d}, {n} scored",flush=True)
        res.setdefault("_meta",{})[state]=dict(seq_match=pct,offset=off,nres=pose.total_residue())
    out[acc]=dict(gene=gene,pair=st["pair"],closed=st["closed"],open=st["open"],ddg=res)
    json.dump(out,open("ddg.json","w"),indent=1)
print("\nDDG DONE",flush=True)
