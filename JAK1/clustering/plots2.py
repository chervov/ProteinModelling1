import json, numpy as np, matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
plt.rcParams.update({"font.size":9,"axes.spines.top":False,"axes.spines.right":False,
  "figure.dpi":130,"savefig.bbox":"tight","axes.grid":True,"grid.alpha":.25,"grid.linewidth":.5})
C1,C2="#2f7bbf","#c0392b"
F=["esm1b","alphamissense","ddg_closed","ddg_open","ddg_delta","cadd","foldx","sift","polyphen2","blosum62","clinpred"]
X=np.load("X.npy"); pap=np.load("pap.npy"); reb=np.load("reb.npy")
ing=np.load("ing.npy"); ncov=np.load("ncov.npy")
am=X[:,F.index("alphamissense")]
agree=pap==reb
def save(f,n): f.savefig(f"figs/{n}.png"); plt.close(f); print("  figs/"+n+".png")
def ari(p,r):
    from collections import Counter
    n=len(p); c=Counter(zip(p,r)); a=Counter(p); b=Counter(r); C=lambda x:x*(x-1)/2
    idx=sum(C(v) for v in c.values()); ea=sum(C(v) for v in a.values()); eb=sum(C(v) for v in b.values())
    exp=ea*eb/C(n); mx=(ea+eb)/2
    return (idx-exp)/(mx-exp)

# 6 disagreement by coverage
fig,axes=plt.subplots(1,2,figsize=(10.4,4))
ks=sorted(set(ncov)); rate=[100*(~agree[ncov==k]).mean() for k in ks]; cnt=[(ncov==k).sum() for k in ks]
b=axes[0].bar([str(k) for k in ks],rate,color="#6a51a3",width=.6)
for bb,v,c in zip(b,rate,cnt):
    axes[0].text(bb.get_x()+bb.get_width()/2,v+.5,f"{v:.1f}%",ha="center",fontweight="bold",fontsize=8.5)
    axes[0].text(bb.get_x()+bb.get_width()/2,v/2,f"n={c:,}",ha="center",color="white",fontsize=7.5)
axes[0].set_xlabel("features present (of 11)"); axes[0].set_ylabel("% assigned differently")
axes[0].set_title("Disagreement rises as coverage falls",fontsize=10)
# band x coverage heat
bands=[(0,.25,"<0.25\nconf. tolerant"),(.25,.55,"0.25–0.55\nintermed.-low"),
       (.55,.80,"0.55–0.80\nintermed.-high"),(.80,1.01,"≥0.80\nconf. damaging")]
M=np.full((2,len(bands)),np.nan)
for j,(lo,hi,_) in enumerate(bands):
    sel=(~np.isnan(am))&(am>=lo)&(am<hi)
    for i,cs in enumerate([ncov<=8,ncov>=10]):
        m=sel&cs
        if m.sum()>30: M[i,j]=100*(~agree[m]).mean()
cmap=LinearSegmentedColormap.from_list("r",["#ffffff","#fdd49e","#e34a33","#7f0000"])
im=axes[1].imshow(M,cmap=cmap,vmin=0,vmax=40,aspect="auto")
axes[1].set_xticks(range(len(bands))); axes[1].set_xticklabels([b[2] for b in bands],fontsize=7.5)
axes[1].set_yticks([0,1]); axes[1].set_yticklabels(["≤8 features","≥10 features"]); axes[1].grid(False)
for i in range(2):
    for j in range(len(bands)):
        if not np.isnan(M[i,j]):
            axes[1].text(j,i,f"{M[i,j]:.1f}%",ha="center",va="center",fontweight="bold",
                         color="white" if M[i,j]>22 else "#222")
fig.colorbar(im,ax=axes[1],shrink=.85,label="% disagreement")
axes[1].set_title("Band and coverage are independent, and multiply",fontsize=10)
fig.tight_layout(); save(fig,"disagreement")

# 7 stratified ARI
subs=[("ALL (published headline)",np.ones(len(pap),bool)),
      ("high coverage (≥10 feats)",ncov>=10),
      ("confident AlphaMissense",(~np.isnan(am))&((am<.25)|(am>=.80))),
      ("BOTH high-cov & confident",(ncov>=10)&(~np.isnan(am))&((am<.25)|(am>=.80))),
      ("NEITHER (≤8 & intermediate)",(ncov<=8)&(~np.isnan(am))&(am>=.25)&(am<.80))]
names=[s[0] for s in subs]; vals=[ari(pap[m],reb[m]) for _,m in subs]; ns=[int(m.sum()) for _,m in subs]
fig,ax=plt.subplots(figsize=(8.4,4))
cols=["#555","#5b8fc9","#5b8fc9","#1a7a3c","#b02020"]
bb=ax.barh(range(len(names))[::-1],vals,color=cols,height=.6)
for i,(v,nn) in enumerate(zip(vals,ns)):
    ax.text(v+.012,len(names)-1-i,f"{v:.3f}   (n={nn:,})",va="center",fontsize=8.6,fontweight="bold")
ax.set_yticks(range(len(names))[::-1]); ax.set_yticklabels(names,fontsize=8.6)
ax.set_xlim(0,.95); ax.set_xlabel("Adjusted Rand Index vs the paper's EV1 clustering")
ax.set_title("The headline ARI averages two very different regimes",fontsize=10)
save(fig,"ari_strat")

# 8 gnomAD along the protein + cluster
fig,ax=plt.subplots(figsize=(11,3.4))
pos=np.array([int(v) for v in np.load("pos.npy")]) if False else None
import csv
rows=list(csv.DictReader(open("/Users/chervov/ProteinModelling1/JAK1/clustering/jak1_clustering_rebuilt.csv")))
P=np.array([int(r["pos"]) for r in rows])
W=25; edges=np.arange(1,1155+W,W)
fr_c2=[]; fr_gn=[]; ctr=[]
for a,b2 in zip(edges[:-1],edges[1:]):
    m=(P>=a)&(P<b2)
    if m.sum()==0: continue
    ctr.append((a+b2)/2); fr_c2.append(100*(pap[m]==2).mean()); fr_gn.append(100*ing[m].mean())
ax.fill_between(ctr,fr_c2,color=C2,alpha=.35,label="% damaging (paper C2)")
ax.plot(ctr,fr_c2,color=C2,lw=1.2)
ax2=ax.twinx(); ax2.plot(ctr,fr_gn,color="#1a7a3c",lw=1.4,label="% seen in gnomAD")
ax2.set_ylabel("% seen in gnomAD",color="#1a7a3c"); ax2.grid(False)
for s,e,nm in [(34,420,"FERM"),(439,544,"SH2"),(583,855,"JH2 pseudokinase"),(875,1153,"JH1 kinase")]:
    ax.axvspan(s,e,color="#999",alpha=.11)
    ax.text((s+e)/2,92,nm,ha="center",fontsize=7.8,color="#333",
            bbox=dict(fc="white",ec="none",alpha=.75,pad=1.5))
ax.set_xlim(1,1154); ax.set_ylim(0,100); ax.set_xlabel("JAK1 residue"); ax.set_ylabel("% damaging",color=C2)
ax.set_title("Damaging fraction and gnomAD observation along the protein (25-residue windows)",
             fontsize=10,pad=12)
save(fig,"along_protein")
