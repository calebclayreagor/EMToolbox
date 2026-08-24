import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Prostate/Song2022_Prostate"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Song2022_Prostate"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=30,alpha=.8,frameon=False,show=False,ax=ax)
leg=ax.get_legend()
if leg is not None: leg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Prostate malignant manifold — samples',size=7.5)
ax.text(.5,-.12,'Song et al., 2022',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated samples.pdf, legend removed | corr(x,t)=%.3f"%np.corrcoef(xl[:,0],a.obs['t'].values)[0,1])
