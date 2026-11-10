import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from scipy.stats import spearmanr
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Prostate/Chen2021_Prostate"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Prostate/Chen2021_Prostate"
a=sc.read_h5ad(os.path.join(D,"manifold.h5ad"))   # base signatures.h5ad absent; same log-norm X + X_umap_lin
print("X max (log-norm check): %.2f"%float(a.X.max()))
a.obsm['X_umap']=a.obsm['X_umap_lin']
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
def _vec(g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
genes=['TWIST1','FOXC1']; colors={'TWIST1':'tab:blue','FOXC1':'tab:red'}   # house hues, no orange
thr={g:(float(np.quantile(_vec(g)[_vec(g)>0],0.75)) if (_vec(g)>0).any() else 0.0) for g in genes}
sel={g:_vec(g)>thr[g] for g in genes}
order=sorted(genes,key=lambda g:-int(sel[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=30,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[sel[g]].copy(),na_color=colors[g],size=30,alpha=.85,frameon=False,show=False,ax=ax)
ax.set_title('EMT-TF Expression   TWIST1 \u00b7 FOXC1 (both root-enriched)',size=7.5)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.text(.5,-.14,'Chen et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
for g in genes:
    v=_vec(g); print(f"{g}: expr_frac={(v>0).mean():.2f} -> house sel_frac={sel[g].mean():.3f} (was {(v>0).mean():.2f}) | rho(t)={spearmanr(a.obs['t'].values,v)[0]:.3f}")
