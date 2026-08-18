import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Breast/Qian2020_Breast-2"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Qian2020_Breast-2"
a=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.06
def frame(ax): ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
# samples (no legend)
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=10,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
frame(ax); ax.set_title('Breast malignant manifold — samples',size=7.5)
ax.text(.5,-.12,'Qian et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# expression SNAI2(blue)/FOXC1(red), upper-quartile, INLINE legend
def vec(g): x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
sel_g=['SNAI2','FOXC1']; colors={'SNAI2':'tab:blue','FOXC1':'tab:red'}
thr={g:(float(np.quantile(vec(g)[vec(g)>0],0.75)) if (vec(g)>0).any() else 0.0) for g in sel_g}
seln={g:vec(g)>thr[g] for g in sel_g}
order=sorted(sel_g,key=lambda g:-int(seln[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=10,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[seln[g]].copy(),na_color=colors[g],size=10,alpha=.85,frameon=False,show=False,ax=ax)
frame(ax)
ax.legend(handles=[Line2D([0],[0],marker='o',color='w',markerfacecolor=colors[g],markersize=4,label=g) for g in sel_g],
          loc='upper right', frameon=False, fontsize=6, handletextpad=.2, borderaxespad=.2)
ax.set_title('EMT-TF Expression   SNAI2 (blue) · FOXC1 (red)',size=7.5)
ax.text(.5,-.12,'Qian et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated samples + expression at matched house frame")
