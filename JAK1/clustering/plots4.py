import json, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":9,"axes.spines.top":False,"axes.spines.right":False,
 "figure.dpi":130,"savefig.bbox":"tight","axes.grid":True,"grid.alpha":.25,"grid.linewidth":.5})
S=json.load(open("stats.json"))
# pooled vs stratified OR
fig,axes=plt.subplots(1,2,figsize=(11,4.1))
ax=axes[0]
names=["paper","rebuilt"]; w=.36; x=np.arange(2)
ax.bar(x-w/2,[S["gnomad_strat"][n]["pooled_or"] for n in names],w,color="#999",label="pooled (confounded)")
ax.bar(x+w/2,[S["gnomad_strat"][n]["mh_or"] for n in names],w,color="#1a7a3c",label="Mantel–Haenszel (stratified)")
for i,n in enumerate(names):
    ax.text(i-w/2,S["gnomad_strat"][n]["pooled_or"]+.05,f'{S["gnomad_strat"][n]["pooled_or"]:.2f}',ha="center",fontsize=8.5)
    ax.text(i+w/2,S["gnomad_strat"][n]["mh_or"]+.05,f'{S["gnomad_strat"][n]["mh_or"]:.2f}',ha="center",fontweight="bold",fontsize=8.5)
ax.axhline(1,color="#999",ls="--",lw=1)
ax.set_xticks(x); ax.set_xticklabels(["Paper (EV1)","Rebuilt"]); ax.set_ylabel("odds ratio, C1 vs C2 observed in gnomAD")
ax.legend(frameon=False,fontsize=8,loc="upper center",bbox_to_anchor=(.5,-.12),ncol=2)
ax.set_title("Pooling inflates the depletion",fontsize=10)
# ARI on external strata
ax=axes[1]
E=S["strat_external"]
cols={"all variants":"#555","observed in gnomAD":"#1a7a3c","absent from gnomAD":"#b02020",
      "high coverage (≥10 feats)":"#1f5fa8","low coverage (≤8 feats)":"#d95f0e"}
nm=[e["name"] for e in E]; vv=[e["ari"] for e in E]
y=np.arange(len(nm))[::-1]
ax.barh(y,vv,color=[cols.get(n,"#777") for n in nm],height=.6)
for i,e in enumerate(E): ax.text(e["ari"]+.01,y[i],f'{e["ari"]:.3f}  (n={e["n"]:,})',va="center",fontsize=8.3)
ax.set_yticks(y); ax.set_yticklabels(nm,fontsize=8.4); ax.set_xlim(0,.88)
ax.set_xlabel("ARI vs the paper's clustering")
ax.set_title("Stratified on external variables only",fontsize=10)
fig.tight_layout(); fig.savefig("figs/gnomad_strat.png"); print("  figs/gnomad_strat.png")
