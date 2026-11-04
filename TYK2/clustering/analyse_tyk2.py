"""Statistics for the ELEVEN-feature TYK2 clustering (v2), including the dual-state ddG.

A copy of analyse.py pointed at tyk2_clustering_v2.csv and writing stats_with_ddg.json.
The v1 files are left untouched.
"""
import csv, json, math, pathlib
import numpy as np, pandas as pd
from scipy import stats as sps
C = pathlib.Path("/Users/chervov/ProteinModelling1/TYK2/clustering")
SEQ = open("TYK2_P29597_1187aa.txt").read().splitlines()[1]
NAMES = ["esm1b","alphamissense","cadd","foldx","sift","polyphen2","blosum62","clinpred",
         "ddg_closed","ddg_open","ddg_delta"]
LAB = {"ddg_closed":"ddG closed","ddg_open":"ddG open","ddg_delta":"ddG delta",
     "esm1b":"ESM-1b","alphamissense":"AlphaMissense","cadd":"CADD","foldx":"FoldX ddG",
       "sift":"SIFT","polyphen2":"PolyPhen-2 HumVar","blosum62":"BLOSUM62","clinpred":"ClinPred"}
# +1 = larger means more damaging
# ddG here is dG_WT - dG_mut, so NEGATIVE = destabilising: negate for the damaging direction
SIGN = {"ddg_closed":-1,"ddg_open":-1,"ddg_delta":-1,"esm1b":-1,"alphamissense":1,"cadd":1,"foldx":1,"sift":-1,"polyphen2":1,
        "blosum62":-1,"clinpred":1}

df = pd.read_csv(C/"tyk2_clustering_v1.csv")
gn = pd.read_csv(C/"tyk2_gnomad.csv").set_index("variant")
cv = pd.read_csv(C/"tyk2_clinvar.csv").set_index("variant")
df["in_gnomad"] = df.variant.map(gn.in_gnomad).fillna(0).astype(int)
df["gnomad_af"] = df.variant.map(gn.gnomad_af)
df["clinvar"]   = df.variant.map(cv.clinvar_significance)
df["stars"]     = df.variant.map(cv.clinvar_stars)
cl = df.cluster.to_numpy(); X = df[NAMES].to_numpy(float)
dbn = ~np.isnan(X[:, NAMES.index("cadd")])
ncov = (~np.isnan(X)).sum(1)
S = {"n": len(df), "sizes": [int((cl==1).sum()), int((cl==2).sum())]}

# which cluster is damaging? by AlphaMissense
am = X[:, NAMES.index("alphamissense")]
dam = 2 if np.nanmedian(am[cl==2]) > np.nanmedian(am[cl==1]) else 1
S["damaging_cluster"] = int(dam)
print(f"cluster sizes C1 {S['sizes'][0]:,} C2 {S['sizes'][1]:,}; damaging = C{dam}")

# ---- per-feature means by cluster (what the report is asked to show) ----
S["means"] = {}
for i, n in enumerate(NAMES):
    v = X[:, i]
    row = {}
    for c in (1, 2):
        m = (cl == c) & ~np.isnan(v)
        row[f"c{c}_mean"]   = round(float(v[m].mean()), 4)
        row[f"c{c}_median"] = round(float(np.median(v[m])), 4)
        row[f"c{c}_sd"]     = round(float(v[m].std()), 4)
        row[f"c{c}_n"]      = int(m.sum())
    a, b = v[(cl==1)&~np.isnan(v)], v[(cl==2)&~np.isnan(v)]
    row["diff"] = round(row["c2_mean"] - row["c1_mean"], 4)
    # Cohen's d, and a rank test that does not assume normality
    sp = math.sqrt(((len(a)-1)*a.std(ddof=1)**2 + (len(b)-1)*b.std(ddof=1)**2)/(len(a)+len(b)-2))
    row["cohens_d"] = round(float((b.mean()-a.mean())/sp), 3) if sp else None
    row["mwu_p"] = float(sps.mannwhitneyu(a, b).pvalue)
    # AUC for separating the damaging cluster
    s = SIGN[n]*v; m = ~np.isnan(s)
    y = (cl[m] == dam).astype(int); r = sps.rankdata(s[m]); n1 = y.sum()
    row["auc"] = round(float((r[y==1].sum()-n1*(n1+1)/2)/(n1*(len(y)-n1))), 4)
    row["coverage"] = round(100*np.isfinite(v).mean(), 1)
    S["means"][n] = row
    print(f"  {LAB[n]:<20} C1 {row['c1_mean']:>9.3f}  C2 {row['c2_mean']:>9.3f}  "
          f"d={row['cohens_d']:>6}  AUC={row['auc']:.3f}")

# ---- gnomAD enrichment, pooled and stratified (the JAK1 lesson) ----
ing = df.in_gnomad.to_numpy()
def fisher(mask=None):
    m = np.ones(len(cl), bool) if mask is None else mask
    a=int(((cl==1)&(ing==1)&m).sum()); b=int(((cl==1)&(ing==0)&m).sum())
    c=int(((cl==2)&(ing==1)&m).sum()); d=int(((cl==2)&(ing==0)&m).sum())
    orr,p = sps.fisher_exact([[a,b],[c,d]])
    return dict(c1_obs=a,c1_n=a+b,c2_obs=c,c2_n=c+d,
                c1_pct=round(100*a/max(a+b,1),2), c2_pct=round(100*c/max(c+d,1),2),
                odds_ratio=round(orr,2), p=float(p))
S["gnomad_pooled"] = fisher()
num=den=0; strata={}
for nm, m in (("dbNSFP-defined",dbn),("dbNSFP-missing",~dbn)):
    t = fisher(m); strata[nm]=t
    a,b,c,d = t["c1_obs"],t["c1_n"]-t["c1_obs"],t["c2_obs"],t["c2_n"]-t["c2_obs"]
    n_=a+b+c+d
    if n_: num += a*d/n_; den += b*c/n_
S["gnomad_strata"]=strata
S["gnomad_mh_or"]=round(num/den,2) if den else None
print(f"\ngnomAD: pooled OR {S['gnomad_pooled']['odds_ratio']} "
      f"(C1 {S['gnomad_pooled']['c1_pct']}% vs C2 {S['gnomad_pooled']['c2_pct']}%, "
      f"p={S['gnomad_pooled']['p']:.1e})  ->  Mantel-Haenszel OR {S['gnomad_mh_or']}")
S["gnomad_confound"]={"pct_gnomad_in_dbnsfp":round(100*dbn[ing==1].mean(),1),
  "pct_all_dbnsfp":round(100*dbn.mean(),1),
  "pct_C1_dbnsfp":round(100*dbn[cl==1].mean(),1),"pct_C2_dbnsfp":round(100*dbn[cl==2].mean(),1)}

# ---- ClinVar spot check ----
path={"Pathogenic","Likely pathogenic","Pathogenic/Likely pathogenic"}
ben={"Benign","Likely benign","Benign/Likely benign"}
S["clinvar"]={"pathogenic":[],"benign":[]}
for v,c,sig in zip(df.variant, cl, df.clinvar):
    if sig in path: S["clinvar"]["pathogenic"].append([v,int(c)])
    elif sig in ben: S["clinvar"]["benign"].append([v,int(c)])
p_ok=sum(1 for _,c in S["clinvar"]["pathogenic"] if c==dam)
b_ok=sum(1 for _,c in S["clinvar"]["benign"] if c!=dam)
S["clinvar"]["correct"]=[p_ok,len(S["clinvar"]["pathogenic"]),b_ok,len(S["clinvar"]["benign"])]
print(f"ClinVar: {p_ok}/{len(S['clinvar']['pathogenic'])} pathogenic in the damaging cluster, "
      f"{b_ok}/{len(S['clinvar']['benign'])} benign in the tolerant one")

# ---- domains, coverage ----
DOM=[("FERM",26,431),("SH2",450,529),("JH2 pseudokinase",589,875),("JH1 kinase",897,1176)]
S["domains"]=[]
pos=df.pos.to_numpy()
for nm,a,b in DOM+[("linker / other",0,0)]:
    m=((pos>=a)&(pos<=b)) if b else ~np.any([[(pos>=x)&(pos<=y)] for _,x,y in DOM],axis=0)[0]
    if m.sum()==0: continue
    S["domains"].append({"domain":nm,"n":int(m.sum()),
        "pct_damaging":round(100*(cl[m]==dam).mean(),1),
        "pct_gnomad":round(100*ing[m].mean(),2)})
S["cov_table"]=[{"k":int(k),"n":int((ncov==k).sum()),
                 "pct_damaging":round(100*(cl[ncov==k]==dam).mean(),1)} for k in sorted(set(ncov))]

# ---- feature-feature correlation ------------------------------------------
# Oriented so that + always means "more damaging", otherwise ESM-1b and SIFT would
# show spurious negative correlations with everything else purely by sign convention.
SIGN={"ddg_closed":-1,"ddg_open":-1,"ddg_delta":-1,"esm1b":-1,"alphamissense":1,"cadd":1,"foldx":1,"sift":-1,"polyphen2":1,
      "blosum62":-1,"clinpred":1}
Xo = X*np.array([SIGN[n] for n in NAMES])
k=len(NAMES)
rho=np.full((k,k),np.nan); pairn=np.zeros((k,k),dtype=int)
for i in range(k):
    for j in range(k):
        m=~np.isnan(Xo[:,i])&~np.isnan(Xo[:,j]); pairn[i,j]=m.sum()
        if m.sum()>50: rho[i,j]=sps.spearmanr(Xo[m,i],Xo[m,j]).statistic
S["corr"]={"names":NAMES,"sign":SIGN,
           "rho":[[None if np.isnan(v) else round(float(v),3) for v in r] for r in rho],
           "pair_n":pairn.tolist()}
off=[(round(float(rho[i,j]),3),NAMES[i],NAMES[j]) for i in range(k) for j in range(i+1,k)
     if not np.isnan(rho[i,j])]
S["corr"]["highest"]=sorted(off,reverse=True)[:3]
S["corr"]["lowest"]=sorted(off)[:3]
S["corr"]["mean_abs"]=round(float(np.mean([abs(a) for a,_,_ in off])),3)
S["corr"]["min_pair_n"]=int(min(pairn[i,j] for i in range(k) for j in range(i+1,k)))
np.save("corr_rho_t.npy",rho); np.save("corr_n_t.npy",pairn)
print(f"\ncorrelation: mean |rho| over {len(off)} pairs = {S['corr']['mean_abs']}, "
      f"smallest pairwise n = {S['corr']['min_pair_n']:,}")
print("   highest:", ", ".join(f"{a} {b}/{c}" for a,b,c in S["corr"]["highest"]))
print("   lowest: ", ", ".join(f"{a} {b}/{c}" for a,b,c in S["corr"]["lowest"]))

# ---- DMS validation: TYK2's decisive advantage over JAK2 -------------------
# Howard et al. 2026 measured interferon signalling and protein abundance for essentially every
# TYK2 missense variant. Nothing in the clustering saw it, and it covers 22,536 variants against
# the 21 usable ClinVar labels JAK2 had to rely on.
dms = pd.read_csv(C/".."/"DMS_Howard2026"/"TYK2_DMS_Howard2026_all_arms.csv")
dms = dms[dms["class"] == "missense"].copy()
dms["variant"] = dms.wt + dms.pos.astype(str) + dms.alt
dms = dms[dms.variant.isin(set(df.variant))]
cl_by_v = dict(zip(df.variant, df.cluster))
dms["cluster"] = dms.variant.map(cl_by_v)
S["dms"] = {"n_overlap": int(len(dms)), "arms": {}}
for arm in ("ifn_1U", "ifn_10U", "ifn_100U", "abundance"):
    if arm not in dms: continue
    x = dms.dropna(subset=[arm])
    a = x[x.cluster == dam][arm].to_numpy(); b = x[x.cluster != dam][arm].to_numpy()
    # a LOW score means loss of function, so negate for the damaging direction
    auc = float(sps.mannwhitneyu(-a, -b).statistic / (len(a) * len(b)))
    S["dms"]["arms"][arm] = {"n": int(len(x)), "c1_mean": round(float(b.mean()), 4),
                             "c2_mean": round(float(a.mean()), 4), "auc": round(auc, 3),
                             "p": float(sps.mannwhitneyu(a, b).pvalue)}
print("\nDMS (Howard 2026), %d missense overlapping:" % len(dms))
for k, v in S["dms"]["arms"].items():
    print(f"   {k:<12} n={v['n']:,}  C1 {v['c1_mean']:+.3f}  C2 {v['c2_mean']:+.3f}  AUC {v['auc']:.3f}")

np.save("corr_rho_t.npy",rho); np.save("corr_n_t.npy",pairn)
print(f"\ncorrelation: mean |rho| over {len(off)} pairs = {S['corr']['mean_abs']}, "
      f"smallest pairwise n = {S['corr']['min_pair_n']:,}")
print("   highest:", ", ".join(f"{a} {b}/{c}" for a,b,c in S["corr"]["highest"]))
print("   lowest: ", ", ".join(f"{a} {b}/{c}" for a,b,c in S["corr"]["lowest"]))

# ---- predictor thresholds, kept for the report (no TYK2 variant panel yet) ----------
# damaging-direction cutoffs, as used in the JAK2 reports. FoldX and BLOSUM62 have no
# published cutoff of this kind and are shown unhighlighted.
THR={"esm1b":("lt",-7.5,None),"alphamissense":("gt",0.564,None),"polyphen2":("ge",0.447,0.909),
     "sift":("le",0.05,None),"clinpred":("ge",0.5,None),"cadd":("ge",25.0,30.0)}
S["panel_thresholds"]={k:{"op":o,"light":a,"intense":b} for k,(o,a,b) in THR.items()}

np.save("X_t.npy",X); np.save("cl_t.npy",cl); np.save("ing_t.npy",ing); np.save("ncov_t.npy",ncov)
np.save("pos_t.npy",pos)
df.to_csv("merged_tyk2.csv",index=False)
json.dump(S,open("stats_tyk2.json","w"),indent=1)
print("\nwrote stats_tyk2.json")
