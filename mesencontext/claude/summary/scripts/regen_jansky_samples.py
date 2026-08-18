import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Neuroendocrine/Jansky2021_Neuroendocrine"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Neuroendocrine/Jansky2021_Neuroendocrine"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']   # oriented layout, matches all other panels
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=30,alpha=.8,frameon=False,show=False,ax=ax)
h,l=ax.get_legend_handles_labels()
ax.legend(h,l,ncol=1,frameon=False,loc='center left',bbox_to_anchor=(1.02,.5),
          handletextpad=.2,labelspacing=.25,fontsize=4.5,title='sample',title_fontsize=5)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Neuroblastoma malignant manifold — samples',size=7.5)
ax.text(.5,-.14,'Jansky et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated samples.pdf on X_umap_lin | corr(x,t)=%.3f (origin-left, matches other panels)"%np.corrcoef(xl[:,0],a.obs['t'].values)[0,1])
