import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Hematologic/Rendeiro2020_Hematologic-5"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Rendeiro2020_Hematologic-5"
a=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
def frame(ax):
    ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
    ax.invert_yaxis(); ax.invert_xaxis()
# samples, no legend
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=10,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
frame(ax); ax.set_title('CLL malignant manifold — samples',size=7)
ax.text(.5,-.12,'Rendeiro et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# expression, categorical any-expresser, ZEB2 blue / ZEB1 red, inline legend
def _vec(g):
    x=a[:,g].X; return np.asarray(x.todense()).ravel() if hasattr(x,'todense') else np.asarray(x).ravel()
colors={'ZEB2':'tab:blue','ZEB1':'tab:red'}; shown=['ZEB2','ZEB1']
sel={g:_vec(g)>0 for g in shown}
stats={g:100*sel[g].mean() for g in shown}
order=sorted(shown,key=lambda g:-int(sel[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=8,alpha=.4,frameon=False,show=False,ax=ax,na_color='lightgrey')
for g in order:
    sc.pl.umap(a[sel[g]].copy(),na_color=colors[g],size=8,alpha=.7,frameon=False,show=False,ax=ax)
frame(ax)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[g],label=f'{g} ({stats[g]:.1f}%)') for g in shown],
          frameon=False,loc='upper right',fontsize=5,handletextpad=.2,borderaxespad=0.2)
ax.set_title('EMT-TF Expression  ZEB2 · ZEB1',size=7.5)
ax.text(.5,-.12,'Rendeiro et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated Rendeiro samples + expression at house strip")
