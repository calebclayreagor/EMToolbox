import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Hematologic/Giustacchini2017_Hematologic-1"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Giustacchini2017_Hematologic-1"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=14,alpha=.85,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('CML malignant manifold — samples',size=7)
ax.text(.5,-.12,'Giustacchini et al., 2017',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated Giustacchini samples.pdf, legend removed | corr=%.3f"%np.corrcoef(xl[:,0],a.obs['t'].values)[0,1])
