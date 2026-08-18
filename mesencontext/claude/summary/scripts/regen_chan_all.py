import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from scipy.stats import spearmanr
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Lung/Chan2021_Lung-3"
F_="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Lung/Chan2021_Lung-3"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
# stored X_umap(=lin) runs pseudotime right->left; negate x for house left->right (display only)
a.obsm['X_umap']=a.obsm['X_umap'].copy(); a.obsm['X_umap'][:,0]*=-1
t=a.obs['t'].values
print("post-flip corr(x,t)=%.3f"%np.corrcoef(a.obsm['X_umap'][:,0],t)[0,1])
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
HS=(3.5,1.5)
def frame(ax): ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
def cite(ax,y=-.12): ax.text(.5,y,'Chan et al., 2021',ha='center',transform=ax.transAxes,size=6)
# samples (no legend)
fig,ax=plt.subplots(figsize=HS)
sc.pl.umap(a,color='sample',size=6,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
frame(ax); ax.set_title('SCLC malignant manifold — samples',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# manifold: cividis t + curve F/B (F also x-negated)
g=a.uns['graph']; B=np.asarray(g['B']); Fc=np.asarray(g['F']).T.copy(); Fc[:,0]*=-1
fig,ax=plt.subplots(figsize=HS)
sc.pl.umap(a,color='t',cmap='cividis',size=6,colorbar_loc=None,frameon=False,show=False,ax=ax)
ii,jj=np.where(np.triu(B>0))
for i,j in zip(ii,jj): ax.plot([Fc[i,0],Fc[j,0]],[Fc[i,1],Fc[j,1]],'-',color='k',lw=1.0,zorder=5)
ax.scatter(Fc[:,0],Fc[:,1],s=7,color='k',zorder=6)
frame(ax); ax.set_title('Pseudotime',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"manifold.pdf"),bbox_inches='tight'); plt.close(fig)
# signatures plasma
for col,fn,title in [('Gast','Gast_signature','Gastrulation Signature'),
                     ('pSom','pSom_signature','Somitogenesis Signature'),
                     ('Crest','Crest_signature','Neural Crest Signature')]:
    fig,ax=plt.subplots(figsize=HS)
    sc.pl.umap(a,color=col,cmap='plasma',alpha=.6,size=6,colorbar_loc=None,frameon=False,show=False,ax=ax)
    frame(ax); ax.set_title(title,size=7.5); cite(ax)
    fig.savefig(os.path.join(F_,fn+".pdf"),bbox_inches='tight'); plt.close(fig)
# EMT: root_tf blue / term_tf red, 75th-pct-among-expressers thr
root_tf,term_tf='TWIST1','SNAI1'
tfs={root_tf:'tab:blue',term_tf:'tab:red'}
order=sorted(tfs, key=lambda gg:-(np.asarray(a[:,gg].X.todense()).ravel()>0).mean())
fig,ax=plt.subplots(figsize=HS)
sc.pl.umap(a,size=6,alpha=.35,frameon=False,show=False,ax=ax,na_color='lightgray')
for gg in order:
    x=np.asarray(a[:,gg].X.todense()).ravel(); expr=x[x>0]
    thr=np.quantile(expr,.75) if expr.size else np.inf
    sc.pl.umap(a[x>thr],na_color=tfs[gg],size=9,alpha=.7,frameon=False,show=False,ax=ax)
frame(ax); ax.set_title('EMT-TF Expression   TWIST1 (root) · SNAI1 (terminus)',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated all 6 panels house-strip, left->right")
