import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Brain/Choudhury2022_Brain"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Choudhury2022_Brain"
a=sc.read_h5ad(os.path.join(D,"processed.h5ad"))   # Gate 1 NO-GO: raw X_umap only (no trajectory/lin)
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.06
fig,ax=plt.subplots(figsize=(3.5,2.4))
sc.pl.umap(a,color='sample',size=8,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()   # legend removed so the cloud fills the panel (per-patient archipelago still visible by colour)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Meningioma malignant manifold — samples',size=8)
ax.text(.5,-.08,'Choudhury et al., 2022',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
im=1
print("regenerated samples.pdf (raw X_umap, legend removed)")
