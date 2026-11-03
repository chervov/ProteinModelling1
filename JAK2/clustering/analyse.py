"""Statistics for the JAK2 v1 clustering report."""
import csv, json, math, pathlib
import numpy as np, pandas as pd
from scipy import stats as sps
C = pathlib.Path("/Users/chervov/ProteinModelling1/JAK2/clustering")
SEQ = open("JAK2_O60674_1132aa.txt").read().splitlines()[1]
NAMES = ["esm1b","alphamissense","cadd","foldx","sift","polyphen2","blosum62","clinpred"]
LAB = {"esm1b":"ESM-1b","alphamissense":"AlphaMissense","cadd":"CADD","foldx":"FoldX ddG",
       "sift":"SIFT","polyphen2":"PolyPhen-2 HumVar","blosum62":"BLOSUM62","clinpred":"ClinPred"}
# +1 = larger means more damaging
SIGN = {"esm1b":-1,"alphamissense":1,"cadd":1,"foldx":1,"sift":-1,"polyphen2":1,
        "blosum62":-1,"clinpred":1}

df = pd.read_csv(C/"jak2_clustering_v1.csv")
gn = pd.read_csv(C/"jak2_gnomad.csv").set_index("variant")
cv = pd.read_csv(C/"jak2_clinvar.csv").set_index("variant")
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
DOM=[("FERM",37,380),("SH2",401,482),("JH2 pseudokinase",545,809),("JH1 kinase",849,1124)]
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

# ---- the 28-variant literature panel ---------------------------------------
# Three groups as supplied: previously reported GOF, the four newly selected,
# and those identified in the study. The last two overlap on four variants;
# the grouping is kept as given rather than de-duplicated.
PANEL=[("GOF variants previously reported",
        "T108A Y317H H345L H608N L611S V617I V617F V625F E846D R867Q T875N S755R R938Q R1063H".split()),
       ("New selected 4 variants", "V1110E G571R V578I L805I".split()),
       ("Variants identified in this study",
        "P37A F240V H380Y R426X C427R G571R V578I L805I I1065T V1110E".split())]
# damaging-direction thresholds, as specified. (light, intense) - None = no second tier.
# FoldX and BLOSUM62 have no published cutoff of this kind, so they are shown unhighlighted.
THR={"esm1b":("lt",-7.5,None),"alphamissense":("gt",0.564,None),"polyphen2":("ge",0.447,0.909),
     "sift":("le",0.05,None),"clinpred":("ge",0.5,None),"cadd":("ge",25.0,30.0)}
S["panel_thresholds"]={k:{"op":o,"light":a,"intense":b} for k,(o,a,b) in THR.items()}
dmap=dict((nm,(a,b)) for nm,a,b in DOM)
def domain_of(q):
    for nm,a,b in DOM:
        if a<=q<=b: return nm
    return "linker / other"
idx=df.set_index("variant")
S["panel"]=[]
for gname,vs in PANEL:
    rows=[]
    for v in vs:
        if v[-1]=="X":
            rows.append({"variant":v,"note":"nonsense (p.Arg426*) - outside the missense universe"})
            continue
        r=idx.loc[v]; q=int(r.pos)
        assert SEQ[q-1]==v[0], f"{v} does not match O60674"
        rows.append({"variant":v,"pos":q,"domain":domain_of(q),"cluster":int(r.cluster),
                     "gnomad":bool(r.in_gnomad),
                     "feat":{n:(None if pd.isna(r[n]) else float(r[n])) for n in NAMES}})
    S["panel"].append({"group":gname,"rows":rows})
npanel=sum(len(g["rows"]) for g in S["panel"])
nmiss=sum(1 for g in S["panel"] for x in g["rows"] if "note" in x)
print(f"\npanel: {npanel} listed, {npanel-nmiss} with features, {nmiss} excluded")
for g in S["panel"]:
    dd=sum(1 for x in g["rows"] if x.get("cluster")==dam)
    nn=sum(1 for x in g["rows"] if "cluster" in x)
    print(f"   {g['group']:<36}{dd}/{nn} in the damaging cluster")

np.save("X.npy",X); np.save("cl.npy",cl); np.save("ing.npy",ing); np.save("ncov.npy",ncov)
np.save("pos.npy",pos)
df.to_csv("merged.csv",index=False)
json.dump(S,open("stats.json","w"),indent=1)
print("\nwrote stats.json")
