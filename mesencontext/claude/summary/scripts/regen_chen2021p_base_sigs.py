import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Prostate/Chen2021_Prostate"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Chen2021_Prostate"
CB=os.path.join(F,"colorbars"); os.makedirs(CB,exist_ok=True)
a=sc.read_h5ad(os.path.join(D,"manifold.h5ad"))   # has Gast/pSom/Crest + X_umap_lin (base signatures.h5ad absent)
a.obsm['X_umap']=a.obsm['X_umap_lin']
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
titles={'Gast':'Gastrulation Signature','pSom':'Somitogenesis Signature','Crest':'Neural Crest Signature'}
for m in ['Gast','pSom','Crest']:
    fig,ax=plt.subplots(figsize=(3.5,1.5))
    sc.pl.umap(a,color=m,cmap='plasma',alpha=.75,size=30,colorbar_loc=None,frameon=False,show=False,ax=ax,title=titles[m])
    ax.title.set_size(7.5); ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
    ax.text(.5,-.14,'Chen et al., 2021',ha='center',transform=ax.transAxes,size=6)
    fig.savefig(os.path.join(F,f"{m}_signature.pdf"),bbox_inches='tight')
    lo,hi=float(a.obs[m].min()),float(a.obs[m].max()); ticks=np.round(np.linspace(lo,hi,5),2)
    fcb=plt.figure(figsize=(.66,1)); cax=fcb.add_axes([.35,.05,.3,.9])
    cb=plt.colorbar(ax.collections[0],cax=cax); cb.ax.tick_params(which='both',size=0)
    cb.set_label(f'{m}\nSignature'); cb.set_ticks(ticks,labels=ticks); cb.solids.set_alpha(1)
    fcb.savefig(os.path.join(CB,f"{m}_colorbar.pdf"),bbox_inches='tight'); plt.close('all')
print("regen Chen signatures at plasma (house); scores unchanged")
