import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from scipy.stats import spearmanr
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Prostate/Dong2020_Prostate-5"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Dong2020_Prostate-5"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
# --- display-only left->right orientation: negate X_umap x so pseudotime increases left->right ---
a.obsm['X_umap']=a.obsm['X_umap'].copy(); a.obsm['X_umap'][:,0]*=-1
t=a.obs['t'].values
print("post-flip corr(x,t)=%.3f"%np.corrcoef(a.obsm['X_umap'][:,0],t)[0,1])
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
def frame(ax):
    ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
def cite(ax,y=-.12): ax.text(.5,y,'Dong et al., 2020',ha='center',transform=ax.transAxes,size=6)
HS=(3.5,1.5)
# ---------- samples (no legend) ----------
fig,ax=plt.subplots(figsize=HS)
sc.pl.umap(a,color='sample',size=8,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend();
if lg: lg.remove()
frame(ax); ax.set_title('Prostate malignant manifold — samples',size=7.5); cite(ax)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# ---------- manifold: sub (developmental) cividis t + curve + red root + celltype labels ----------
sub=a[a.obs.compartment=='Developmental'].copy()
R=sub.obsm['X_R']; node=(R.T @ sub.obsm['X_umap'])/R.sum(0)[:,None]
B=np.asarray(a.uns['graph']['B']); root=int(np.asarray(a.uns['graph']['root']))
edges=[(i,j) for i in range(len(node)) for j in range(i+1,len(node)) if B[i,j]>0]
fig,ax=plt.subplots(figsize=HS)
sc.pl.umap(sub,color='t',cmap='cividis',size=10,colorbar_loc=None,frameon=False,show=False,ax=ax)
for i,j in edges: ax.plot([node[i,0],node[j,0]],[node[i,1],node[j,1]],'-k',lw=1.2,zorder=10)
ax.scatter(node[:,0],node[:,1],c='w',edgecolor='k',s=10,zorder=11)
ax.scatter(node[root,0],node[root,1],c='red',edgecolor='k',s=55,zorder=12)
sc.pl.umap(sub,color='celltype',size=10,alpha=0,legend_loc='on data',legend_fontsize=5,legend_fontoutline=1,frameon=False,show=False,ax=ax)
frame(ax); ax.set_title('Pseudotime',size=7.5); cite(ax)
fig.savefig(os.path.join(F,"manifold.pdf"),bbox_inches='tight'); plt.close(fig)
# ---------- signatures (plasma, GSE keys) ----------
for key,fn,title in [('GSE162534','Gast_signature','Gastrulation Signature'),
                     ('GSE229103','pSom_signature','Somitogenesis Signature'),
                     ('rRNAModifications','Crest_signature','Neural Crest Signature')]:
    fig,ax=plt.subplots(figsize=HS)
    sc.pl.umap(a,color=key,cmap='plasma',alpha=.7,size=8,colorbar_loc=None,frameon=False,show=False,ax=ax)
    sc.pl.umap(a,color='celltype',size=8,alpha=0,legend_loc='on data',legend_fontsize=5,legend_fontoutline=1,frameon=False,show=False,ax=ax)
    frame(ax); ax.set_title(title,size=7.5); cite(ax)
    fig.savefig(os.path.join(F,fn+".pdf"),bbox_inches='tight'); plt.close(fig)
# ---------- EMT (SOX9 blue / TWIST1 red categorical, median-among-expressers thr) ----------
g_plt={}
for g,c in [('SOX9','tab:blue'),('TWIST1','tab:red')]:
    v=a[:,g].X.toarray().ravel(); thr=float(np.quantile(v[v>0],0.5)); g_plt[g]=(c,thr)
fig,ax=plt.subplots(figsize=HS)
sc.pl.umap(a,size=8,alpha=.35,frameon=False,show=False,ax=ax,na_color='lightgray')
for var,(c,thr) in g_plt.items():
    ap=a[a[:,var].X.toarray().ravel()>thr].copy()
    sc.pl.umap(ap,na_color=c,size=8,alpha=.8,frameon=False,show=False,ax=ax)
frame(ax); ax.set_title('EMT-TF Expression   SOX9 (early) · TWIST1 (late)',size=7.5); cite(ax)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated all 6 panels house-strip, left->right")
