import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Breast/Bassez2021_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Bassez2021_Breast"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']   # root-left (+0.60); base samples had a 41-sample legend
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=6,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg is not None: lg.remove()   # 41 samples -> no legend (final convention)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Breast malignant-epithelial manifold \u2014 samples',size=6.5)
ax.text(.5,-.12,'Bassez et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
print("regen Bassez samples no legend | corr=%.3f | nsamp=%d"%(np.corrcoef(xl[:,0],a.obs['t'].values)[0,1], a.obs['sample'].nunique()))
