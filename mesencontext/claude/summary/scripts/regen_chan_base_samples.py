import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Lung/Chan2021_Lung"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Chan2021_Lung"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']   # base samples was raw (+0.472); lin is root-left (+0.696), matches other panels
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=6,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg is not None: lg.remove()   # Chan convention: 24 samples -> no legend
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('SCLC malignant manifold \u2014 samples',size=7.5)
ax.text(.5,-.12,'Chan et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
print("regen Chan samples on lin, no legend | corr=%.3f | nsamp=%d"%(np.corrcoef(xl[:,0],a.obs['t'].values)[0,1], a.obs['sample'].nunique()))
