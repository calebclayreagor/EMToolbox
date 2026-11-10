import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Head-and-Neck/Chen2020_Head-and-Neck-1"; F="/home/caleb/EMToolbox/figures/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-1"
a=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
# --- samples: single sample-colored UMAP, legend-free, house strip ---
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=20,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('NPC malignant manifold \u2014 samples',size=7.5)
ax.text(.5,-.12,'Chen et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# --- expression: reference categorical overlay, top-2 detected TFs on grey ---
full=a.raw.to_adata(); full.obsm['X_umap']=a.obsm['X_umap']
pairs=[('PRRX1','tab:blue'),('SNAI2','tab:red')]
fig,ax=plt.subplots(figsize=(3.5,1.5))
ax.scatter(xy[:,0],xy[:,1],s=5,c='lightgrey',linewidths=0,rasterized=True)
hand=[]
for g,col in pairs:
    v=np.asarray(full[:,g].X.todense()).ravel()
    pos=v[v>0]; thr=float(np.quantile(pos,0.75)) if pos.size else np.inf  # dataset-specific: matches Chen final (regen_chen5)
    sel=v>=thr
    ax.scatter(xy[sel,0],xy[sel,1],s=6,c=col,linewidths=0,rasterized=True)
    hand.append(Line2D([0],[0],marker='o',color='w',markerfacecolor=col,markersize=4,label=g))
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py); ax.axis('off')
ax.legend(handles=hand,loc='upper right',frameon=False,fontsize=5,handletextpad=.2)
ax.set_title('EMT-TF expression',size=7.5)
ax.text(.5,-.08,'Chen et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regen samples+expression | PRRX1/SNAI2 0.75-among-pos (dataset-specific) overlay")
