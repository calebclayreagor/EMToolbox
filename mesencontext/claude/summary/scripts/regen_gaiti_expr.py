import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Hematologic/Gaiti2019_Hematologic"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Gaiti2019_Hematologic"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']
other_tf, term_tf = 'PRRX1', 'ZEB2'   # least-terminal / terminus (from summary)
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
def _vec(g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
thr={}
for g in [other_tf,term_tf]:
    v=_vec(g); pos=v[v>0]; thr[g]=float(np.quantile(pos,0.75)) if pos.size else 0.0
sel={g:_vec(g)>thr[g] for g in [other_tf,term_tf]}
order=sorted([other_tf,term_tf], key=lambda g:-int(sel[g].sum()))
colors={other_tf:'tab:blue', term_tf:'tab:red'}
labs={other_tf:f'{other_tf} (least-terminal)', term_tf:f'{term_tf} (terminus)'}
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=30,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    ap=a[sel[g]].copy()
    sc.pl.umap(ap,na_color=colors[g],size=30,alpha=.85,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
# inline legend (upper right, inside axes) so the panel is not widened
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[g],label=labs[g]) for g in [other_tf,term_tf]],
          frameon=False, loc='upper right', fontsize=5, handletextpad=.2, borderaxespad=0.2)
ax.set_title('EMT-TF Expression (all panel TFs skew terminal)', size=7.5)
ax.text(.5,-.14,'Gaiti et al., 2019', ha='center', transform=ax.transAxes, size=6)
fig.savefig(os.path.join(F,'expression.pdf'), bbox_inches='tight'); plt.close(fig)
import pypdfium2 as pdfium
im=pdfium.PdfDocument(os.path.join(F,'expression.pdf'))[0].render(scale=2.0).to_pil()
print("regenerated expression.pdf inline legend | aspect=%.2f"%(im.size[0]/im.size[1]))
