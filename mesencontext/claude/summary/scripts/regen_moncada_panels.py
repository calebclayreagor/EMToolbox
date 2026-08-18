import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Pancreas/Moncada2020_Pancreas"
F="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Pancreas/Moncada2020_Pancreas"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
# samples, no legend
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=16,alpha=.85,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('PDAC malignant manifold — samples',size=7)
ax.text(.5,-.12,'Moncada et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# expression: FOXC1 blue / SNAI2 red (both root), top-decile threshold, inline legend
def _vec(g):
    x=a[:,g].X; return np.asarray(x.todense()).ravel() if hasattr(x,'todense') else np.asarray(x).ravel()
sel=['FOXC1','SNAI2']; colors={'FOXC1':'tab:blue','SNAI2':'tab:red'}; thr={}
for g in sel:
    v=_vec(g); pos=v[v>0]; thr[g]=float(np.quantile(pos,0.90)) if pos.size else 0.0
seln={g:_vec(g)>thr[g] for g in sel}
order=sorted(sel,key=lambda g:-int(seln[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=16,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[seln[g]].copy(),na_color=colors[g],size=16,alpha=.85,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[g],label=g) for g in sel],
          frameon=False,loc='upper right',fontsize=5,handletextpad=.2,borderaxespad=0.2)
ax.set_title('EMT-TF Expression  FOXC1 · SNAI2',size=7.5)
ax.text(.5,-.12,'Moncada et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated Moncada samples + expression at house strip")
