import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Sarcoma/Zhou2020_Sarcoma"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Sarcoma/Zhou2020_Sarcoma"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=30,alpha=.8,frameon=False,show=False,ax=ax)
leg=ax.get_legend()
if leg is not None: leg.remove()   # legend removed so cloud fills panel (matches other panels)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Osteosarcoma malignant manifold — samples',size=7.5)
ax.text(.5,-.12,'Zhou et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated samples.pdf on X_umap_lin, legend removed | corr(x,t)=%.3f"%np.corrcoef(xl[:,0],a.obs['t'].values)[0,1])
