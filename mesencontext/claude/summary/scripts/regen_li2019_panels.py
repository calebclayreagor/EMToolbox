import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Skin/Li2019_Skin-3"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Li2019_Skin-3"
a=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
# samples, no legend
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=12,alpha=.85,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Melanoma malignant manifold — samples\n(Gate 1 NO-GO: two disconnected lobes)',size=6.3)
ax.text(.5,-.14,'Li et al., 2019',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# expression: ZEB2 blue / SNAI2 red, top-decile threshold, inline legend
def _vec(g):
    x=a[:,g].X; return np.asarray(x.todense()).ravel() if hasattr(x,'todense') else np.asarray(x).ravel()
sel=['ZEB2','SNAI2']; colors={'ZEB2':'tab:blue','SNAI2':'tab:red'}; thr={}
for g in sel:
    v=_vec(g); pos=v[v>0]; thr[g]=float(np.quantile(pos,0.90)) if pos.size else 0.0
seln={g:_vec(g)>thr[g] for g in sel}
order=sorted(sel,key=lambda g:-int(seln[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=12,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[seln[g]].copy(),na_color=colors[g],size=12,alpha=.85,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[g],label=f'{g}') for g in sel],
          frameon=False,loc='upper right',fontsize=5,handletextpad=.2,borderaxespad=0.2)
ax.set_title('EMT-TF Expression  ZEB2 · SNAI2',size=7)
ax.text(.5,-.12,'Li et al., 2019',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated Li2019 samples + expression at house strip")
