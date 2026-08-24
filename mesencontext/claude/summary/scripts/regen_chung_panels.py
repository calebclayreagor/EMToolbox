import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Breast/Chung2017_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Chung2017_Breast"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
# samples, no legend (sparse SmartSeq2, size larger)
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=22,alpha=.85,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Breast malignant manifold — samples',size=7)
ax.text(.5,-.12,'Chung et al., 2017',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# expression: FOXC1 blue (early/root) / SNAI1 red (late/terminus), inline legend
def _vec(g):
    x=a[:,g].X; return np.asarray(x.todense()).ravel() if hasattr(x,'todense') else np.asarray(x).ravel()
early,late='FOXC1','SNAI1'; thr={}
for g in [early,late]:
    v=_vec(g); pos=v[v>0]; thr[g]=float(np.quantile(pos,0.75)) if pos.size else 0.0
sel={g:_vec(g)>thr[g] for g in [early,late]}
colors={early:'tab:blue', late:'tab:red'}
order=sorted([early,late],key=lambda g:-int(sel[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=22,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[sel[g]].copy(),na_color=colors[g],size=22,alpha=.8,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[g],label=g) for g in [early,late]],
          frameon=False,loc='upper right',fontsize=5,handletextpad=.2,borderaxespad=0.2)
ax.set_title('EMT-TF Expression  FOXC1 · SNAI1',size=7.5)
ax.text(.5,-.12,'Chung et al., 2017',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated Chung samples + expression at house strip")
