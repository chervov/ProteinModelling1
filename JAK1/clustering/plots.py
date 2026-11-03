import json, csv, os
import numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy import stats as sps
os.makedirs("figs",exist_ok=True)
plt.rcParams.update({"font.size":9,"axes.spines.top":False,"axes.spines.right":False,
                     "figure.dpi":130,"savefig.bbox":"tight","axes.grid":True,
                     "grid.alpha":.25,"grid.linewidth":.5})
C1,C2="#2f7bbf","#c0392b"          # tolerant, damaging
F=["esm1b","alphamissense","ddg_closed","ddg_open","ddg_delta","cadd","foldx","sift","polyphen2","blosum62","clinpred"]
LAB={"esm1b":"ESM-1b","alphamissense":"AlphaMissense","ddg_closed":"ddG closed","ddg_open":"ddG open",
     "ddg_delta":"ddG delta","cadd":"CADD","foldx":"FoldX ddG","sift":"SIFT","polyphen2":"PolyPhen-2",
     "blosum62":"BLOSUM62","clinpred":"ClinPred"}
X=np.load("X.npy"); pap=np.load("pap.npy"); reb=np.load("reb.npy")
ing=np.load("ing.npy"); gaf=np.load("gaf.npy"); ncov=np.load("ncov.npy")
S=json.load(open("stats.json"))
def save(fig,name): fig.savefig(f"figs/{name}.png"); plt.close(fig); print("  figs/"+name+".png")

# 1 histograms by paper cluster
fig,axes=plt.subplots(3,4,figsize=(13,7.5))
for i,f in enumerate(F):
    ax=axes.flat[i]; v=X[:,i]; m=~np.isnan(v)
    lo,hi=np.nanpercentile(v,[0.5,99.5]); b=np.linspace(lo,hi,45)
    ax.hist(v[m&(pap==1)],bins=b,color=C1,alpha=.72,label="C1 tolerant",density=True)
    ax.hist(v[m&(pap==2)],bins=b,color=C2,alpha=.62,label="C2 damaging",density=True)
    ax.set_title(f"{LAB[f]}  ({100*m.mean():.0f}% cov)",fontsize=9)
    ax.set_yticks([])
axes.flat[11].axis("off")
axes.flat[0].legend(fontsize=8,frameon=False)
fig.suptitle("Feature distributions by the paper's EV1 cluster",fontsize=11,y=1.00)
fig.tight_layout(); save(fig,"hist_by_cluster")

# 2 correlation matrix (oriented so + = more damaging)
SIGN={"esm1b":-1,"alphamissense":1,"ddg_closed":-1,"ddg_open":-1,"ddg_delta":-1,"cadd":1,
      "foldx":1,"sift":-1,"polyphen2":1,"blosum62":-1,"clinpred":1}
Xo=X*np.array([SIGN[f] for f in F])
k=len(F); M=np.full((k,k),np.nan)
for i in range(k):
    for j in range(k):
        m=~np.isnan(Xo[:,i])&~np.isnan(Xo[:,j])
        if m.sum()>50: M[i,j]=sps.spearmanr(Xo[m,i],Xo[m,j]).statistic
cmap=LinearSegmentedColormap.from_list("bwr2",["#2166ac","#f7f7f7","#b2182b"])
fig,ax=plt.subplots(figsize=(7.6,6.4))
im=ax.imshow(M,cmap=cmap,vmin=-1,vmax=1)
ax.set_xticks(range(k)); ax.set_xticklabels([LAB[f] for f in F],rotation=45,ha="right")
ax.set_yticks(range(k)); ax.set_yticklabels([LAB[f] for f in F]); ax.grid(False)
for i in range(k):
    for j in range(k):
        if not np.isnan(M[i,j]):
            ax.text(j,i,f"{M[i,j]:.2f}",ha="center",va="center",fontsize=6.6,
                    color="white" if abs(M[i,j])>.55 else "#333")
fig.colorbar(im,shrink=.8,label="Spearman ρ")
ax.set_title("Feature correlation (all oriented: + = more damaging)",fontsize=10)
save(fig,"corr")

# 3 AUC
fig,ax=plt.subplots(figsize=(8,4.4))
order=sorted(F,key=lambda f:-(S["auc"][f]["paper"] or 0))
y=np.arange(len(order)); w=.38
ax.barh(y+w/2,[S["auc"][f]["paper"] for f in order],w,color="#444",label="vs paper EV1")
ax.barh(y-w/2,[S["auc"][f]["rebuilt"] for f in order],w,color="#e08214",label="vs rebuilt")
ax.axvline(.5,color="#999",ls="--",lw=1)
ax.set_yticks(y); ax.set_yticklabels([f"{LAB[f]}  ({S['auc'][f]['cov']:.0f}%)" for f in order])
ax.set_xlim(.45,1.02); ax.set_xlabel("AUC for separating cluster 2 (damaging)")
ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(.5,-.15),ncol=2); ax.set_title("Per-feature discrimination",fontsize=10)
save(fig,"auc")

# 4 gnomAD enrichment
fig,axes=plt.subplots(1,2,figsize=(9.6,4),sharey=True)
for ax,(nm,lab) in zip(axes,[("paper","Paper (Dataset EV1)"),("rebuilt","Rebuilt clustering")]):
    g=S["gnomad"][nm]
    v=[g["1"]["frac"] if "1" in g else g[1]["frac"], g["2"]["frac"] if "2" in g else g[2]["frac"]]
    nn=[g["1"]["n"] if "1" in g else g[1]["n"], g["2"]["n"] if "2" in g else g[2]["n"]]
    gg=[g["1"]["gn"] if "1" in g else g[1]["gn"], g["2"]["gn"] if "2" in g else g[2]["gn"]]
    bars=ax.bar(["C1 tolerant","C2 damaging"],v,color=[C1,C2],width=.6)
    for b,val,a,t in zip(bars,v,gg,nn):
        ax.text(b.get_x()+b.get_width()/2,val+.12,f"{val:.2f}%",ha="center",fontweight="bold")
        ax.text(b.get_x()+b.get_width()/2,val/2,f"{a}/{t:,}",ha="center",color="white",fontsize=8)
    ax.set_title(f"{lab}\n{g['depletion_C2_vs_C1']}× depletion, p = {g['p']:.1e}",fontsize=9.5)
axes[0].set_ylabel("% of cluster observed in gnomAD r4")
fig.suptitle("gnomAD enrichment: the damaging cluster is depleted of observed variation",fontsize=11,y=1.02)
save(fig,"gnomad_enrich")

# 5 gnomAD by AF band
fig,ax=plt.subplots(figsize=(8,4))
bands=list(S["gnomad_by_af"].keys())
pv=[S["gnomad_by_af"][b]["pct_in_C2_paper"] for b in bands]
rv=[S["gnomad_by_af"][b]["pct_in_C2_rebuilt"] for b in bands]
x=np.arange(len(bands)); w=.38
ax.bar(x-w/2,pv,w,color="#444",label="paper EV1")
ax.bar(x+w/2,rv,w,color="#e08214",label="rebuilt")
for i,b in enumerate(bands): ax.text(i,max(pv[i],rv[i])+1.6,f"n={S['gnomad_by_af'][b]['n']:,}",ha="center",fontsize=7.5)
ax.set_xticks(x); ax.set_xticklabels(bands,fontsize=8.5)
ax.set_ylabel("% assigned to C2 (damaging)"); ax.legend(frameon=False)
ax.set_title("The commoner the variant in gnomAD, the less often it is called damaging",fontsize=10)
save(fig,"gnomad_af")
