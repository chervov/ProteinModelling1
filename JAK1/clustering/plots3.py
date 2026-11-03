import json, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":9,"axes.spines.top":False,"axes.spines.right":False,
  "figure.dpi":130,"savefig.bbox":"tight","axes.grid":True,"grid.alpha":.25,"grid.linewidth":.5})
LAB={"esm1b":"ESM-1b","alphamissense":"AlphaMissense","ddg_closed":"ddG closed","ddg_open":"ddG open",
     "ddg_delta":"ddG delta","cadd":"CADD","foldx":"FoldX ddG","sift":"SIFT","polyphen2":"PolyPhen-2",
     "blosum62":"BLOSUM62","clinpred":"ClinPred"}
S=json.load(open("stats.json")); A=S["auc_subsets"]
KA="all variants"; KD="dbNSFP-defined (all 11 features)"; KM="dbNSFP-missing (8 features)"
order=sorted(A, key=lambda f:-(A[f][KD] or 0))
fig,axes=plt.subplots(1,2,figsize=(12.6,4.9))
# left: all vs matched subset
y=np.arange(len(order)); w=.38
ax=axes[0]
ax.barh(y+w/2,[A[f][KA] for f in order],w,color="#888",label="all 21,926 variants")
ax.barh(y-w/2,[A[f][KD] for f in order],w,color="#1f5fa8",label="dbNSFP subset (n=6,873)")
ax.axvline(.5,color="#999",ls="--",lw=1); ax.set_xlim(.45,1.02)
ax.set_yticks(y); ax.set_yticklabels([LAB[f] for f in order],fontsize=8.6)
ax.invert_yaxis(); ax.set_xlabel("AUC vs the paper's clusters")
ax.set_title("Same variants for every feature",fontsize=10)
ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(.5,-.15),ncol=2)
# right: easy vs hard
ax=axes[1]
oo=[f for f in order if A[f][KM] is not None]
y=np.arange(len(oo))
ax.barh(y+w/2,[A[f][KD] for f in oo],w,color="#1a7a3c",label="dbNSFP-defined (easier)")
ax.barh(y-w/2,[A[f][KM] for f in oo],w,color="#b02020",label="dbNSFP-missing (harder)")
ax.axvline(.5,color="#999",ls="--",lw=1); ax.set_xlim(.45,1.02)
ax.set_yticks(y); ax.set_yticklabels([LAB[f] for f in oo],fontsize=8.6)
ax.invert_yaxis(); ax.set_xlabel("AUC vs the paper's clusters")
ax.set_title("The three 31.3% features cannot be scored on the harder half",fontsize=10)
ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(.5,-.15),ncol=2)
fig.suptitle("Per-feature AUC on matched subsets",fontsize=11,y=1.02)
fig.tight_layout(); fig.savefig("figs/auc_subsets.png"); print("  figs/auc_subsets.png")
