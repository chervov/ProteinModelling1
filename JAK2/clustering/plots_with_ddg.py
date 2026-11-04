import json, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.size":9,"axes.spines.top":False,"axes.spines.right":False,
 "figure.dpi":130,"savefig.bbox":"tight","axes.grid":True,"grid.alpha":.25,"grid.linewidth":.5})
import os; os.makedirs("figs_with_ddg",exist_ok=True)
C1,C2="#2f7bbf","#c0392b"
NAMES=["esm1b","alphamissense","cadd","foldx","sift","polyphen2","blosum62","clinpred",
       "ddg_closed","ddg_open","ddg_delta"]
LAB={"ddg_closed":"ddG closed","ddg_open":"ddG open","ddg_delta":"ddG delta",
     "esm1b":"ESM-1b","alphamissense":"AlphaMissense","cadd":"CADD","foldx":"FoldX ddG",
     "sift":"SIFT","polyphen2":"PolyPhen-2","blosum62":"BLOSUM62","clinpred":"ClinPred"}
S=json.load(open("stats_with_ddg.json")); X=np.load("X_wd.npy"); cl=np.load("cl_wd.npy")
ing=np.load("ing_wd.npy"); ncov=np.load("ncov_wd.npy"); pos=np.load("pos_wd.npy")
sv=lambda f,n:(f.savefig(f"figs_with_ddg/{n}.png"),plt.close(f),print("  figs_with_ddg/"+n+".png"))

from matplotlib.colors import LinearSegmentedColormap
rho=np.load("corr_rho_wd.npy"); pairn=np.load("corr_n_wd.npy")

# 0 correlation heatmap + the pairwise n it rests on
fig,axes=plt.subplots(1,2,figsize=(13.2,5.6),gridspec_kw={"width_ratios":[1,1]})
cmap=LinearSegmentedColormap.from_list("bwr2",["#2166ac","#f7f7f7","#b2182b"])
k=len(NAMES); labs=[LAB[n] for n in NAMES]
ax=axes[0]
im=ax.imshow(rho,cmap=cmap,vmin=-1,vmax=1)
for i in range(k):
    for j in range(k):
        if not np.isnan(rho[i,j]):
            ax.text(j,i,f"{rho[i,j]:.2f}",ha="center",va="center",fontsize=7,
                    color="white" if abs(rho[i,j])>.55 else "#333")
ax.set_title("Spearman $\\rho$, all oriented so + = more damaging",fontsize=10)
fig.colorbar(im,ax=ax,shrink=.78,label="$\\rho$")
ax=axes[1]
nlog=np.log10(np.maximum(pairn,1))
im2=ax.imshow(nlog,cmap="YlGnBu",vmin=3.5,vmax=np.log10(21508))
for i in range(k):
    for j in range(k):
        v=pairn[i,j]
        ax.text(j,i,f"{v/1000:.1f}k",ha="center",va="center",fontsize=7,
                color="white" if nlog[i,j]>4.15 else "#333")
ax.set_title("variants with BOTH features present",fontsize=10)
cb=fig.colorbar(im2,ax=ax,shrink=.78,label="n (log scale)")
cb.set_ticks([np.log10(x) for x in (6335,10000,21508)]); cb.set_ticklabels(["6.3k","10k","21.5k"])
for ax in axes:
    ax.set_xticks(range(k)); ax.set_xticklabels(labs,rotation=45,ha="right")
    ax.set_yticks(range(k)); ax.set_yticklabels(labs); ax.grid(False)
sv(fig,"corr")

# 1 standardised cluster means - the headline "how do clusters differ" figure
fig,ax=plt.subplots(figsize=(8.6,5.8))
z1,z2=[],[]
for i,n in enumerate(NAMES):
    v=X[:,i]; m=~np.isnan(v); mu,sd=v[m].mean(),v[m].std()
    z1.append((v[(cl==1)&m].mean()-mu)/sd); z2.append((v[(cl==2)&m].mean()-mu)/sd)
y=np.arange(len(NAMES)); w=.38
ax.barh(y+w/2,z1,w,color=C1,label="C1 tolerant")
ax.barh(y-w/2,z2,w,color=C2,label="C2 damaging")
ax.axvline(0,color="#777",lw=1)
ax.set_yticks(y); ax.set_yticklabels([LAB[n] for n in NAMES]); ax.invert_yaxis()
ax.set_xlabel("cluster mean, in standard deviations from the overall mean")
ax.legend(frameon=False,loc="upper center",bbox_to_anchor=(.5,-.13),ncol=2)
ax.set_title("How the two clusters differ on each feature",fontsize=10.5)
sv(fig,"cluster_means")

# 2 distributions
fig,axes=plt.subplots(3,4,figsize=(13,8.2))   # 11 features now, not 8
for i,n in enumerate(NAMES):
    ax=axes.flat[i]; v=X[:,i]; m=~np.isnan(v)
    lo,hi=np.nanpercentile(v,[0.5,99.5]); b=np.linspace(lo,hi,45)
    ax.hist(v[m&(cl==1)],bins=b,color=C1,alpha=.72,density=True,label="C1")
    ax.hist(v[m&(cl==2)],bins=b,color=C2,alpha=.62,density=True,label="C2")
    ax.set_title(f"{LAB[n]} ({S['means'][n]['coverage']:.0f}% cov)",fontsize=9)
    ax.set_yticks([])
for j in range(len(NAMES), axes.size): axes.flat[j].set_visible(False)
axes.flat[0].legend(frameon=False,fontsize=8)
fig.suptitle("Feature distributions by cluster",fontsize=11,y=1.0); fig.tight_layout()
sv(fig,"distributions")

# 3 AUC
fig,ax=plt.subplots(figsize=(7.6,4.8))
order=sorted(NAMES,key=lambda n:-S["means"][n]["auc"])
ax.barh(range(len(order))[::-1],[S["means"][n]["auc"] for n in order],color="#1f5fa8",height=.62)
for i,n in enumerate(order):
    ax.text(S["means"][n]["auc"]+.004,len(order)-1-i,
            f"{S['means'][n]['auc']:.3f}  ({S['means'][n]['coverage']:.0f}%)",va="center",fontsize=8.4)
ax.axvline(.5,color="#999",ls="--",lw=1); ax.set_xlim(.5,1.04)
ax.set_yticks(range(len(order))[::-1]); ax.set_yticklabels([LAB[n] for n in order])
ax.set_xlabel("AUC for separating C2 (damaging)")
ax.set_title("Per-feature discrimination (circular: these features built the clustering)",fontsize=9.5)
sv(fig,"auc")

# 4 gnomAD enrichment, pooled vs stratified
fig,axes=plt.subplots(1,2,figsize=(10.4,4))
g=S["gnomad_pooled"]
b=axes[0].bar(["C1 tolerant","C2 damaging"],[g["c1_pct"],g["c2_pct"]],color=[C1,C2],width=.6)
for bb,v,o,t in zip(b,[g["c1_pct"],g["c2_pct"]],[g["c1_obs"],g["c2_obs"]],[g["c1_n"],g["c2_n"]]):
    axes[0].text(bb.get_x()+bb.get_width()/2,v+.15,f"{v:.2f}%",ha="center",fontweight="bold")
    axes[0].text(bb.get_x()+bb.get_width()/2,v/2,f"{o}/{t:,}",ha="center",color="white",fontsize=8)
axes[0].set_ylabel("% of cluster observed in gnomAD r4")
axes[0].set_title(f"Pooled: OR {g['odds_ratio']}, p = {g['p']:.1e}",fontsize=10)
ax=axes[1]
ax.bar([0,1],[g["odds_ratio"],S["gnomad_mh_or"]],color=["#999","#1a7a3c"],width=.5)
for i,v in enumerate([g["odds_ratio"],S["gnomad_mh_or"]]):
    ax.text(i,v+.03,f"{v}",ha="center",fontweight="bold")
ax.axhline(1,color="#999",ls="--",lw=1); ax.set_xticks([0,1])
ax.set_xticklabels(["pooled\n(confounded)","Mantel–Haenszel\n(stratified)"],fontsize=9)
ax.set_ylabel("odds ratio"); ax.set_title("Stratifying by dbNSFP reachability",fontsize=10)
fig.suptitle("gnomAD enrichment — no feature saw this data",fontsize=11,y=1.02)
fig.tight_layout(); sv(fig,"gnomad")

# 5 along the protein
fig,ax=plt.subplots(figsize=(11,3.3))
W=25; ctr=[];dmg=[];gno=[]
for a in range(1,1133,W):
    m=(pos>=a)&(pos<a+W)
    if m.sum()<5: continue
    ctr.append(a+W/2); dmg.append(100*(cl[m]==2).mean()); gno.append(100*ing[m].mean())
ax.fill_between(ctr,dmg,color=C2,alpha=.35); ax.plot(ctr,dmg,color=C2,lw=1.2)
ax2=ax.twinx(); ax2.plot(ctr,gno,color="#1a7a3c",lw=1.3); ax2.grid(False)
ax2.set_ylabel("% seen in gnomAD",color="#1a7a3c")
for s,e,nm in [(37,380,"FERM"),(401,482,"SH2"),(545,809,"JH2 pseudokinase"),(849,1124,"JH1 kinase")]:
    ax.axvspan(s,e,color="#999",alpha=.11)
    ax.text((s+e)/2,92,nm,ha="center",fontsize=7.6,color="#333",
            bbox=dict(fc="white",ec="none",alpha=.75,pad=1.5))
ax.axvline(617,color="#000",lw=.9,ls=":"); ax.text(617,5,"V617F",fontsize=7.5,rotation=90,va="bottom")
ax.set_xlim(1,1132); ax.set_ylim(0,100)
ax.set_xlabel("JAK2 residue"); ax.set_ylabel("% damaging",color=C2)
ax.set_title("Damaging fraction and gnomAD observation along JAK2 (25-residue windows)",fontsize=10,pad=12)
sv(fig,"along_protein")
