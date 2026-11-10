import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Hematologic/Liu2021_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Liu2021_Hematologic"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))   # raw==lin (root-left, +0.948); base samples had a 15-sample legend
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=8,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg is not None: lg.remove()   # 15 samples -> no legend (final convention)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('MM malignant manifold \u2014 samples',size=7.5)
ax.text(.5,-.12,'Liu et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
print("regen Liu samples no legend | corr=%.3f | nsamp=%d"%(np.corrcoef(xy[:,0],a.obs['t'].values)[0,1], a.obs['sample'].nunique()))
