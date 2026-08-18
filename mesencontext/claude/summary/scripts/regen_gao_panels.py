import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Breast/Gao2021_Breast-3"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Gao2021_Breast-3"
a=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
def frame(ax): ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
# ---- samples (no legend), house strip ----
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=8,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
frame(ax); ax.set_title('Breast malignant manifold — samples',size=7.5)
ax.text(.5,-.12,'Gao et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# ---- expression: FOXC1(blue)/FOXC2(red), INLINE legend, same house strip ----
def _vec(g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
sel=['FOXC1','FOXC2']; colors={'FOXC1':'tab:blue','FOXC2':'tab:red'}
thr={g:(float(np.quantile(_vec(g)[_vec(g)>0],0.75)) if (_vec(g)>0).any() else 0.0) for g in sel}
seln={g:_vec(g)>thr[g] for g in sel}
order=sorted(sel,key=lambda g:-int(seln[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=8,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[seln[g]].copy(),na_color=colors[g],size=8,alpha=.85,frameon=False,show=False,ax=ax)
frame(ax)
ax.legend(handles=[Line2D([0],[0],marker='o',color='w',markerfacecolor=colors[g],markersize=4,label=g) for g in sel],
          loc='upper right', frameon=False, fontsize=6, handletextpad=.2, borderaxespad=.2)
ax.set_title('EMT-TF Expression   FOXC1 (blue) · FOXC2 (red)',size=7.5)
ax.text(.5,-.12,'Gao et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated samples + expression at matched house frame")
