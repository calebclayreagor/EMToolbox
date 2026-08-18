import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from scipy.stats import spearmanr
import pandas as pd
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Kidney/Bi2021_Kidney"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Kidney/Bi2021_Kidney"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']
t=a.obs['t'].values; tn=(t-t.min())/(t.max()-t.min())
panel=['SNAI1','SNAI2','ZEB1','ZEB2','TWIST1','TWIST2','FOXC1','FOXC2','PRRX1','PRRX2']
present=[g for g in panel if g in a.var_names]
X=a[:,present].X; X=X.toarray() if hasattr(X,'toarray') else np.asarray(X)
rows=[(g,(X[:,j]>0).mean(),spearmanr(tn,X[:,j])[0]) for j,g in enumerate(present)]
df=pd.DataFrame(rows,columns=['TF','frac','rho'])
ok=df[df.frac>0.03]
# strongest by |rho| among detected (matches notebook's monotone branch selection)
strong=ok.iloc[ok.rho.abs().values.argmax()]
g=strong.TF; dirn='origin' if strong.rho<0 else 'terminus'
def _vec(gn):
    x=a[:,gn].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
v=_vec(g); pos=v[v>0]; thr=float(np.quantile(pos,0.75)) if pos.size else np.inf
sel=v>thr
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
col='tab:blue' if dirn=='origin' else 'tab:red'   # origin marker -> blue, terminus -> red
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=30,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
sc.pl.umap(a[sel].copy(),na_color=col,size=30,alpha=.85,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title(f'EMT-TF Expression   {g} ({dirn} marker)',size=7.5)
ax.text(.5,-.14,'Bi et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print(f"regenerated expression.pdf | {g}: {(v>0).mean()*100:.0f}% expr, rho={strong.rho:+.2f}, {dirn}, {int(sel.sum())} shown")
