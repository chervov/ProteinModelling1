"""Two-cluster split per protein, gnomAD enrichment, and where the literature mutations land."""
import json, os, sys, csv, urllib.request, collections
import numpy as np
sys.path.insert(0,'/Users/chervov/top10'); os.chdir('/Users/chervov/top10')
sys.path.insert(0,'/Users/chervov/analysis1')
from muts import MUTS
from ten import TEN
FEAT="/Users/chervov/analysis1/feat"
A1=json.load(open("/Users/chervov/analysis1/results.json"))

def load(acc):
    F={}
    for fn,cols in ((f"{acc}.foldx.csv",[("foldx","foldx_ddg")]),):
        p=f"{FEAT}/{fn}"
        if os.path.exists(p):
            for r in csv.DictReader(open(p)):
                try: F[(int(r["pos"]),r["alt"])]={"foldx":float(r["foldx_ddg"])}
                except ValueError: pass
    p=f"{FEAT}/{acc}.tmpnn.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: k=(int(r["new_position"]),r["mutation"].strip())
            except (ValueError,KeyError): continue
            d=F.setdefault(k,{})
            for nm,c in (("tmpnn","ddG_pred"),("esm1v","ESM1v_all_variants"),("am","am_pathogenicity")):
                try: d[nm]=float(r[c])
                except (ValueError,KeyError,TypeError): pass
    p=f"{FEAT}/{acc}.dbnsfp.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: k=(int(r["pos"]),r["alt"])
            except (ValueError,KeyError): continue
            d=F.setdefault(k,{})
            for c in ("revel","cadd","sift","polyphen","metarnn","vest4","primateai","provean"):
                if r.get(c):
                    try: d[c]=float(r[c])
                    except ValueError: pass
    return F
SIGN={"am":1,"esm1v":-1,"foldx":1,"tmpnn":1,"revel":1,"cadd":1,"sift":-1,"polyphen":1,
      "metarnn":1,"vest4":1,"primateai":1,"provean":-1}
LAB={"am":"AlphaMissense","esm1v":"ESM-1v","foldx":"FoldX ΔΔG","tmpnn":"ThermoMPNN ΔΔG",
     "revel":"REVEL","cadd":"CADD","sift":"SIFT","polyphen":"PolyPhen-2","metarnn":"MetaRNN",
     "vest4":"VEST4","primateai":"PrimateAI","provean":"PROVEAN"}
def km2(Z):
    rng=np.random.default_rng(0); C=Z[rng.choice(len(Z),2,replace=False)]
    lab=np.zeros(len(Z),dtype=int)
    for _ in range(200):
        d=((Z[:,None,:]-C[None,:,:])**2).sum(2); new=d.argmin(1)
        if _>0 and (new==lab).all(): break
        lab=new
        for k in (0,1):
            if (lab==k).any(): C[k]=Z[lab==k].mean(0)
    if Z[lab==1].mean()<Z[lab==0].mean(): lab=1-lab
    return lab
def gnomad(gene):
    q=("query($g:String!){gene(gene_symbol:$g,reference_genome:GRCh38){variants(dataset:gnomad_r4)"
       "{consequence hgvsp exome{af} genome{af}}}}")
    AA3={"Ala":"A","Arg":"R","Asn":"N","Asp":"D","Cys":"C","Gln":"Q","Glu":"E","Gly":"G","His":"H",
         "Ile":"I","Leu":"L","Lys":"K","Met":"M","Phe":"F","Pro":"P","Ser":"S","Thr":"T","Trp":"W",
         "Tyr":"Y","Val":"V","Ter":"*"}
    body=json.dumps({"query":q,"variables":{"g":gene}}).encode()
    r=urllib.request.Request("https://gnomad.broadinstitute.org/api",data=body,
        headers={"Content-Type":"application/json","User-Agent":"research-script"})
    out={}
    try: d=json.load(urllib.request.urlopen(r,timeout=300))
    except Exception: return out
    for v in (d["data"]["gene"]["variants"] or []):
        if v.get("consequence")!="missense_variant": continue
        h=(v.get("hgvsp") or "")
        if not h.startswith("p."): continue
        b=h[2:]; wt3,rest=b[:3],b[3:]
        pos="".join(c for c in rest if c.isdigit()); alt3=rest[len(pos):]
        if not pos or wt3 not in AA3 or alt3 not in AA3: continue
        af=(v.get("exome") or {}).get("af") or (v.get("genome") or {}).get("af")
        k=(int(pos),AA3[alt3])
        if af is not None and (k not in out or af>out[k]): out[k]=af
    return out
RES={}
for gene,acc,_ in TEN:
    F=load(acc); gn=gnomad(gene)
    for tag,want in (("rich",list(SIGN)),("full",["am","esm1v","foldx","tmpnn"])):
        keys=[k for k in want if sum(1 for v in F.values() if v.get(k) is not None)>200]
        if len(keys)<2: continue
        rows=[(k,v) for k,v in F.items() if all(v.get(x) is not None for x in keys)]
        if len(rows)<200: continue
        X=np.array([[SIGN[x]*v[x] for x in keys] for _,v in rows],float)
        Z=np.nan_to_num((X-X.mean(0))/(X.std(0)+1e-9))
        lab=km2(Z)
        ing=np.array([1 if k in gn else 0 for k,_ in rows])
        d=RES.setdefault(acc,{}); 
        d[tag]=dict(n=len(rows),keys=[LAB[x] for x in keys],
            sizes=[int((lab==0).sum()),int((lab==1).sum())],
            means={str(c):{LAB[x]:round(float(X[lab==c,i].mean()),3) for i,x in enumerate(keys)} for c in (0,1)},
            gnomad_frac=[round(float(ing[lab==0].mean()),4),round(float(ing[lab==1].mean()),4)],
            gnomad_n=[int(ing[lab==0].sum()),int(ing[lab==1].sum())])
        if tag=="rich":
            idx={k:i for i,(k,_) in enumerate(rows)}
            assign={}
            for wt,pos,alt,l,m,r in MUTS.get(acc,[]):
                i=idx.get((pos,alt))
                assign[f"{wt}{pos}{alt}"]=int(lab[i]) if i is not None else None
            d["mut_cluster"]=assign
    rr=RES.get(acc,{}).get("rich",{})
    gf=rr.get("gnomad_frac")
    print(f"{gene:<8}{rr.get('n',0):>6,} variants, {len(rr.get('keys',[]))} feats, "
          f"clusters {rr.get('sizes')}, gnomAD {100*gf[0]:.1f}% vs {100*gf[1]:.1f}% "
          f"({gf[0]/gf[1]:.1f}x depletion)" if gf and gf[1]>0 else f"{gene}: no depletion",flush=True)
json.dump(RES,open("clusters.json","w"),indent=1)
print("\nclusters.json written")
