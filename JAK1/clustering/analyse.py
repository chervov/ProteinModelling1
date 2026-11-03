"""Full EDA + cluster analysis for the JAK1 rebuild. Writes stats.json and figs/*.png."""
import csv, json, os, math
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy import stats as sps

R="/Users/chervov/ProteinModelling1/JAK1/clustering"
os.makedirs("figs", exist_ok=True)
F=["esm1b","alphamissense","ddg_closed","ddg_open","ddg_delta","cadd","foldx","sift","polyphen2","blosum62","clinpred"]
LAB={"esm1b":"ESM-1b","alphamissense":"AlphaMissense","ddg_closed":"ddG closed","ddg_open":"ddG open",
     "ddg_delta":"ddG delta","cadd":"CADD","foldx":"FoldX ddG","sift":"SIFT","polyphen2":"PolyPhen-2",
     "blosum62":"BLOSUM62","clinpred":"ClinPred"}
# orientation: +1 means larger = more damaging
# Rosetta ddG here is ddG = dG_WT - dG_mut, so NEGATIVE = destabilising (build_rosetta_ddg_jak1_info.md s2);
# FoldX is the opposite. Orient everything so + = more damaging.
SIGN={"esm1b":-1,"alphamissense":+1,"ddg_closed":-1,"ddg_open":-1,"ddg_delta":-1,"cadd":+1,
      "foldx":+1,"sift":-1,"polyphen2":+1,"blosum62":-1,"clinpred":+1}
num=lambda s:(float(s) if s not in ("","NA",None) else np.nan)

rows=list(csv.DictReader(open(f"{R}/jak1_clustering_rebuilt.csv")))
gn=json.load(open("jak1_gnomad.json"))
n=len(rows)
X=np.array([[num(r[f]) for f in F] for r in rows])
pap=np.array([int(float(r["cluster"])) for r in rows])
reb=np.array([int(float(r["my_cluster"])) for r in rows])
pos=np.array([int(r["pos"]) for r in rows]); alt=[r["alt"] for r in rows]
vid=[r["variant_id"] for r in rows]
ing=np.array([1 if f"{p}{a}" in gn else 0 for p,a in zip(pos,alt)])
gaf=np.array([gn.get(f"{p}{a}",{}).get("af",np.nan) for p,a in zip(pos,alt)])
ncov=(~np.isnan(X)).sum(1)
S={"n":n,"n_gnomad":int(ing.sum()),"gnomad_total":len(gn)}
print(f"rows {n} | gnomAD overlap {ing.sum()} of {len(gn)}")

# ---------- AUC ----------
def auc(score, lab, pos_label):
    m=~np.isnan(score)
    s=score[m]; y=(lab[m]==pos_label).astype(int)
    if y.sum()==0 or y.sum()==len(y): return np.nan,0
    r=sps.rankdata(s)
    n1=y.sum(); n0=len(y)-n1
    return ((r[y==1].sum()-n1*(n1+1)/2)/(n1*n0)), int(m.sum())
S["auc"]={}
for i,f in enumerate(F):
    a_p,np_=auc(SIGN[f]*X[:,i], pap, 2)
    a_r,nr=auc(SIGN[f]*X[:,i], reb, 2)
    S["auc"][f]={"paper":None if np.isnan(a_p) else round(a_p,4),
                 "rebuilt":None if np.isnan(a_r) else round(a_r,4),
                 "n":np_, "cov":round(100*np_/n,1)}
# gnomAD AUC: can a feature tell gnomAD-observed from not?
S["auc_gnomad"]={}
for i,f in enumerate(F):
    a,_=auc(SIGN[f]*X[:,i], ing+1, 1)   # pos_label=1 -> NOT in gnomad
    S["auc_gnomad"][f]=None if np.isnan(a) else round(a,4)

# ---------- gnomAD enrichment ----------
def enrich(lab,name):
    out={}
    for c in (1,2):
        m=lab==c
        out[c]={"n":int(m.sum()),"gn":int(ing[m].sum()),"frac":round(100*ing[m].mean(),2)}
    r=out[1]["frac"]/out[2]["frac"] if out[2]["frac"]>0 else float('nan')
    tab=np.array([[out[1]["gn"],out[1]["n"]-out[1]["gn"]],[out[2]["gn"],out[2]["n"]-out[2]["gn"]]])
    orr,p=sps.fisher_exact(tab)
    out["depletion_C2_vs_C1"]=round(r,2); out["odds_ratio"]=round(orr,2); out["p"]=float(p)
    S.setdefault("gnomad",{})[name]=out
    print(f"  {name}: C1 {out[1]['frac']}% ({out[1]['gn']}/{out[1]['n']}) vs C2 {out[2]['frac']}% "
          f"({out[2]['gn']}/{out[2]['n']})  -> {r:.2f}x, OR={orr:.2f}, p={p:.2e}")
print("gnomAD enrichment:")
enrich(pap,"paper"); enrich(reb,"rebuilt")
# by allele-frequency band
S["gnomad_by_af"]={}
for lo,hi,nm in [(0,1e-5,"AF < 1e-5"),(1e-5,1e-4,"1e-5 - 1e-4"),(1e-4,1e-3,"1e-4 - 1e-3"),(1e-3,1.1,"AF > 1e-3")]:
    m=(~np.isnan(gaf))&(gaf>=lo)&(gaf<hi)
    if m.sum()==0: continue
    S["gnomad_by_af"][nm]={"n":int(m.sum()),
        "pct_in_C2_paper":round(100*(pap[m]==2).mean(),1),
        "pct_in_C2_rebuilt":round(100*(reb[m]==2).mean(),1)}
S["gnomad_by_af"]["not in gnomAD"]={"n":int((ing==0).sum()),
    "pct_in_C2_paper":round(100*(pap[ing==0]==2).mean(),1),
    "pct_in_C2_rebuilt":round(100*(reb[ing==0]==2).mean(),1)}
json.dump(S, open("stats.json","w"), indent=1)
np.save("X.npy",X); np.save("pap.npy",pap); np.save("reb.npy",reb)
np.save("ing.npy",ing); np.save("gaf.npy",gaf); np.save("ncov.npy",ncov)
print("\nwrote stats.json + arrays")
