"""JH2-JH1 interface residues, all-atom heavy-atom contacts."""
import json, math, os
from collections import defaultdict
AA3={"ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLN":"Q","GLU":"E","GLY":"G","HIS":"H",
     "ILE":"I","LEU":"L","LYS":"K","MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W",
     "TYR":"Y","VAL":"V","MSE":"M"}
def atoms(path, chain=None):
    out=defaultdict(list)
    if path.endswith(".cif"):
        hdr,rows,inl=[],[],False
        for ln in open(path):
            if ln.startswith("_atom_site."): hdr.append(ln.strip().split(".")[1]); inl=True; continue
            if inl:
                if ln.startswith(("#","loop_","_")) or not ln.strip():
                    if rows: break
                    continue
                rows.append(ln.split())
        ix={k:i for i,k in enumerate(hdr)}
        for f in rows:
            if len(f)<len(hdr): continue
            el=f[ix.get("type_symbol",0)]
            if el=="H": continue
            if chain and f[ix.get("auth_asym_id",ix["label_asym_id"])]!=chain: continue
            try: n=int(f[ix.get("auth_seq_id",ix["label_seq_id"])])
            except Exception: continue
            out[n].append((float(f[ix["Cartn_x"]]),float(f[ix["Cartn_y"]]),float(f[ix["Cartn_z"]]),
                           f[ix["label_atom_id"]].strip('"'), AA3.get(f[ix["label_comp_id"]],"X")))
        return out
    for ln in open(path):
        if not ln.startswith(("ATOM","HETATM")): continue
        if ln[76:78].strip()=="H": continue
        if chain and ln[21]!=chain: continue
        if ln[16] not in " A": continue
        try: n=int(ln[22:26])
        except ValueError: continue
        out[n].append((float(ln[30:38]),float(ln[38:46]),float(ln[46:54]),
                       ln[12:16].strip(), AA3.get(ln[17:20].strip(),"X")))
    return out

def iface(at, A, B, cut=5.0):
    a=[p for p in at if A[0]<=p<=A[1]]; b=[p for p in at if B[0]<=p<=B[1]]
    ia,ib,pairs=set(),set(),[]
    c2=cut*cut
    for p in a:
        for q in b:
            hit=False
            for x1,y1,z1,_,_ in at[p]:
                for x2,y2,z2,_,_ in at[q]:
                    if (x1-x2)**2+(y1-y2)**2+(z1-z2)**2<=c2: hit=True; break
                if hit: break
            if hit: ia.add(p); ib.add(q); pairs.append((p,q))
    return sorted(ia), sorted(ib), pairs

JOBS=[("TYK2 4OLI","/Users/chervov/top10/st/P29597_4OLI.pdb",None,(589,875),(897,1176)),
      ("JAK1 ma-l9b1f (Jeanpierre closed)","/Users/chervov/top10/st/P23458_ma-l9b1f.cif",None,(583,855),(875,1153)),
      ("JAK1 ma-a1sai (Jeanpierre open)","/Users/chervov/top10/st/P23458_ma-a1sai.cif",None,(583,855),(875,1153))]
res={}
for lab,path,ch,A,B in JOBS:
    at=atoms(path,ch)
    ia,ib,pr=iface(at,A,B)
    rng=(min(at),max(at)) if at else (0,0)
    print(f"{lab}: residues {rng[0]}-{rng[1]} ({len(at)} modelled)")
    print(f"   JH2 side ({A[0]}-{A[1]}): {len(ia)} interface residues")
    print(f"   JH1 side ({B[0]}-{B[1]}): {len(ib)} interface residues")
    print(f"   {len(pr)} residue-residue contacts at <5 A heavy atom")
    res[lab]={"jh2":ia,"jh1":ib,"n_pairs":len(pr),"modelled":sorted(at)}
json.dump(res, open("/Users/chervov/.claude/jobs/e920d48f/tmp/j2/ifaces.json","w"))
print()
for k,v in res.items():
    print(k, "JH2:", v["jh2"])
    print(k, "JH1:", v["jh1"])
