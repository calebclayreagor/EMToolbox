import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Sarcoma/Jerby-Arnon2021_Sarcoma"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Sarcoma/Jerby-Arnon2021_Sarcoma"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']   # base samples was raw (root-right, -0.67); lin is root-left (+0.70)
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=30,alpha=.8,frameon=False,show=False,ax=ax)
h,l=ax.get_legend_handles_labels()
ax.legend(h,l,ncol=1,frameon=False,loc='center left',bbox_to_anchor=(1.02,.5),handletextpad=.2,labelspacing=.25,fontsize=5.5,title='sample',title_fontsize=6)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('SynSarc malignant manifold \u2014 samples (10x)',size=7.5)
ax.text(.5,-.12,'Jerby-Arnon et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
print("regen JA2021 samples on lin | corr=%.3f | nsamp=%d"%(np.corrcoef(xl[:,0],a.obs['t'].values)[0,1], a.obs['sample'].nunique()))
