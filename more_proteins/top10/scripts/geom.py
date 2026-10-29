"""All-pairs inter-domain geometry for every structure of every target."""
import json, os, sys, itertools, gzip
import numpy as np
from scipy.spatial import cKDTree
sys.path.insert(0,'/Users/chervov/top10'); os.chdir('/Users/chervov/top10')
META=json.load(open("meta.json"))
SEQ={}

def read_struct(path, chain=None):
    """heavy atoms + CA + bfactor by residue. Handles PDB and mmCIF."""
    heavy={}; ca={}; bf={}
    if path.endswith(".cif"):
        # minimal mmCIF atom_site parser
        cols=[]; rows=[]; inloop=False
        for L in open(path,errors="replace"):
            if L.startswith("_atom_site."):
                cols.append(L.strip().split(".")[1]); inloop=True; continue
            if inloop:
                if L.startswith("#") or L.startswith("loop_") or L.startswith("_"):
                    if rows: break
                    continue
                p=L.split()
                if len(p)<len(cols): continue
                rows.append(p)
        if not cols: return heavy,ca,bf
        ix={c:i for i,c in enumerate(cols)}
        need=("label_atom_id","Cartn_x","Cartn_y","Cartn_z","label_seq_id","type_symbol")
        if not all(n in ix for n in need): return heavy,ca,bf
        cid=ix.get("auth_asym_id") or ix.get("label_asym_id")
        first=None
        for p in rows:
            ch=p[cid] if cid is not None else "A"
            if first is None: first=ch
            if ch!=first: continue
            if p[ix["type_symbol"]]=="H": continue
            try: r=int(p[ix["label_seq_id"]])
            except ValueError: continue
            xyz=(float(p[ix["Cartn_x"]]),float(p[ix["Cartn_y"]]),float(p[ix["Cartn_z"]]))
            heavy.setdefault(r,[]).append(xyz)
            if p[ix["label_atom_id"]].strip('"')=="CA":
                ca[r]=xyz
                try: bf[r]=float(p[ix["B_iso_or_equiv"]]) if "B_iso_or_equiv" in ix else 0.0
                except ValueError: bf[r]=0.0
        return heavy,ca,bf
    first=None
    for L in open(path,errors="replace"):
        if not L.startswith("ATOM"): continue
        ch=L[21]
        if first is None: first=chain or ch
        if ch!=first: continue
        el=(L[76:78].strip() or L[12:16].strip()[0])
        if el=="H": continue
        try: r=int(L[22:26])
        except ValueError: continue
        xyz=(float(L[30:38]),float(L[38:46]),float(L[46:54]))
        heavy.setdefault(r,[]).append(xyz)
        if L[12:16].strip()=="CA":
            ca[r]=xyz
            try: bf[r]=float(L[60:66])
            except ValueError: bf[r]=0.0
    return heavy,ca,bf

def pairgeom(heavy, da, db, minfrac=0.35):
    ra=[r for r in range(da[1],da[2]+1) if r in heavy]
    rb=[r for r in range(db[1],db[2]+1) if r in heavy]
    la=da[2]-da[1]+1; lb=db[2]-db[1]+1
    if len(ra)<minfrac*la or len(rb)<minfrac*lb: return None
    A=np.array([c for r in ra for c in heavy[r]]); B=np.array([c for r in rb for c in heavy[r]])
    ia=[r for r in ra for _ in heavy[r]]; ib=[r for r in rb for _ in heavy[r]]
    pr=cKDTree(A).query_ball_tree(cKDTree(B),5.0)
    rp={(ia[i],ib[j]) for i,js in enumerate(pr) for j in js}
    return dict(dist=round(float(np.linalg.norm(A.mean(0)-B.mean(0))),1),contacts=len(rp),
                cov=[round(100*len(ra)/la),round(100*len(rb)/lb)],
                resA=sorted({x for x,_ in rp}), resB=sorted({y for _,y in rp}))

for acc,rec in META.items():
    doms=rec["domains"]; G=[]
    for s in rec["structures"]:
        p=s["file"]
        if not os.path.exists(p): continue
        heavy,ca,bf=read_struct(p, s.get("chain"))
        if not heavy: s["parse"]="failed"; continue
        row=dict(label=s["label"],kind=s["kind"],identity=s.get("identity"),src=s["src"],
                 nres=len(ca), plddt_med=round(float(np.median(list(bf.values()))),1) if bf else None,
                 pairs={})
        for (na,a1,a2),(nb,b1,b2) in itertools.combinations(doms,2):
            g=pairgeom(heavy,(na,a1,a2),(nb,b1,b2))
            if g: row["pairs"][f"{na}|{nb}"]=g
        G.append(row)
    rec["geom_all"]=G
    # which pairs move, across structures
    allpairs=sorted({k for r in G for k in r["pairs"]})
    mv={}
    for k in allpairs:
        ds=[(r["label"],r["pairs"][k]["dist"],r["pairs"][k]["contacts"]) for r in G if k in r["pairs"]]
        if len(ds)<2: continue
        d=[x[1] for x in ds]; c=[x[2] for x in ds]
        mv[k]=dict(n=len(ds),dmin=min(d),dmax=max(d),spread=round(max(d)-min(d),1),
                   cmin=min(c),cmax=max(c),
                   at_min=[x[0] for x in ds if x[1]==min(d)][0],
                   at_max=[x[0] for x in ds if x[1]==max(d)][0])
    rec["movement"]=mv
    top=sorted(mv.items(),key=lambda kv:-kv[1]["spread"])[:3]
    print(f"{rec['gene']:<8}{len(G)} structures, {len(allpairs)} domain pairs; biggest movers: "
          +"; ".join(f"{k.replace('|','↔')} {v['spread']:.0f}A (n={v['n']}, contacts {v['cmin']}-{v['cmax']})"
                     for k,v in top),flush=True)
json.dump(META,open("meta.json","w"),indent=1)
print("\nmeta.json updated with geom_all + movement")
