import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Hematologic/Liu2021_Hematologic-1"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Liu2021_Hematologic-1"
a=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
# samples panel, house strip, no legend
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=8,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('MM malignant manifold — samples (Gate 1 NO-GO: patient-segregated)',size=6.3)
ax.text(.5,-.12,'Liu et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# expression panel, house strip, inline legend, ZEB1 blue / ZEB2 red, top-decile threshold
def _vec(g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
sel=['ZEB1','ZEB2']; thr={}
for g in sel:
    v=_vec(g); pos=v[v>0]; thr[g]=float(np.quantile(pos,0.90)) if pos.size else 0.0
seln={g:_vec(g)>thr[g] for g in sel}
colors={'ZEB1':'tab:blue','ZEB2':'tab:red'}
order=sorted(sel,key=lambda g:-int(seln[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=14,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[seln[g]].copy(),na_color=colors[g],size=14,alpha=.85,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[g],label=g) for g in sel],
          frameon=False,loc='upper right',fontsize=5,handletextpad=.2,borderaxespad=0.2)
ax.set_title('EMT-TF Expression  ZEB1 (blue) · ZEB2 (red)',size=7.0)
ax.text(.5,-.12,'Liu et al., 2021',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated Liu samples + expression (house strip, inline legend)")
