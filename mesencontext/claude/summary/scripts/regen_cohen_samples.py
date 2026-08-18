import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Hematologic/Cohen2021_Hematologic-2"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Cohen2021_Hematologic-2"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']   # left->right, no invert
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=6,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('MM malignant manifold — samples',size=7.5)
ax.text(.5,-.12,'Cohen et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated samples.pdf, legend + invert removed | corr(x,t)=%.3f"%np.corrcoef(xl[:,0],a.obs['t'].values)[0,1])
