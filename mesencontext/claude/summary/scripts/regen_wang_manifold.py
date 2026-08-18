import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Brain/Wang2019_Brain-7"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Brain/Wang2019_Brain-7"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
xu=a.obsm['X_umap']; t=a.obs['t'].values
G=a.uns['graph']; Fn=np.asarray(G['F']); Bc=np.asarray(G['B']); ii,jj=np.where(np.triu(Bc>0))
xlo,xhi=np.percentile(xu[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xu[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
fig,ax=plt.subplots(figsize=(3.5,1.5))
sca=ax.scatter(xu[:,0],xu[:,1],c=t,cmap='cividis',s=6,alpha=.6,rasterized=True)
for aa,bb in zip(ii,jj):
    ax.plot([Fn[0,aa],Fn[0,bb]],[Fn[1,aa],Fn[1,bb]],'-',color='crimson',lw=1.2,zorder=5)
ax.scatter(Fn[0],Fn[1],c='crimson',s=8,zorder=6)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py); ax.axis('off')
ax.set_title('Pseudotime',size=7.5)
cb=plt.colorbar(sca,ax=ax,fraction=0.035,pad=0.02); cb.ax.tick_params(labelsize=5); cb.set_label('pseudotime',size=6)
ax.text(.5,-.14,'Wang et al., 2019',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"manifold.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated manifold.pdf in house wide-strip (3.5,1.5), curve overlaid")
