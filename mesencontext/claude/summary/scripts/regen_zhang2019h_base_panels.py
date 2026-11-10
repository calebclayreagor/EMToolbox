import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Hematologic/Zhang2019_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Zhang2019_Hematologic"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']   # root-left (+0.98)
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
# samples (no legend; base had a 4-sample legend)
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=8,alpha=.85,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg is not None: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('Follicular lymphoma malignant manifold \u2014 samples',size=6.5)
ax.text(.5,-.12,'Zhang et al., 2019',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
# expression ZEB2 blue (earlier) / ZEB1 red (terminus), top-quartile; legend INLINE (base used external bbox -> 2.34)
def _vec(g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
lo_tf,hi_tf='ZEB2','ZEB1'; colors={lo_tf:'tab:blue',hi_tf:'tab:red'}
lab={lo_tf:f'{lo_tf} (earlier)',hi_tf:f'{hi_tf} (terminus)'}
thr={g:(float(np.quantile(_vec(g)[_vec(g)>0],0.75)) if (_vec(g)>0).any() else 0.0) for g in [lo_tf,hi_tf]}
sel={g:_vec(g)>thr[g] for g in [lo_tf,hi_tf]}
order=sorted([lo_tf,hi_tf],key=lambda g:-int(sel[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=30,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[sel[g]].copy(),na_color=colors[g],size=30,alpha=.8,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[lo_tf],label=lab[lo_tf]),
                   Line2D([],[],marker='o',ls='',color=colors[hi_tf],label=lab[hi_tf])],
          frameon=False, loc='lower right', fontsize=6)
ax.set_title('EMT-TF Expression',size=7.5)
ax.text(.5,-.14,'Zhang et al., 2019',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'expression.pdf'),bbox_inches='tight'); plt.close(fig)
print("regen Zhang2019H samples(no legend) + expression(inline legend) | corr=%.3f"%np.corrcoef(xl[:,0],a.obs['t'].values)[0,1])
