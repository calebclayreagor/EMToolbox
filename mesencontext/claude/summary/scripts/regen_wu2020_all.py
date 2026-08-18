import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Hematologic/Wu2020_Hematologic-3"
F_="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Hematologic/Wu2020_Hematologic-3"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
g=a.uns['graph']; Fc=np.asarray(g['F']); B=np.asarray(g['B']); root=int(np.asarray(g['root']))
xy=a.obsm['X_umap']; xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
FS=(3.5,1.5); CITE='Wu et al., 2020'
def frame(ax):
    ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
    ax.invert_yaxis()  # pseudotime already left->right on raw x (corr +0.97); drop invert_xaxis
def cite(ax): ax.text(.5,-.12,CITE,ha='center',transform=ax.transAxes,size=6)

# 1) samples, no legend
fig,ax=plt.subplots(figsize=FS)
sc.pl.umap(a,color='sample',size=6,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
frame(ax); ax.set_title('AML malignant manifold — samples',size=7); cite(ax)
fig.savefig(os.path.join(F_,"samples.pdf"),bbox_inches='tight'); plt.close(fig)

# 2) manifold: pseudotime + curve + lime root
fig,ax=plt.subplots(figsize=FS)
sc.pl.umap(a,color='t',cmap='cividis',size=8,colorbar_loc=None,frameon=False,show=False,ax=ax)
for i in range(Fc.shape[1]):
    for j in range(i+1,Fc.shape[1]):
        if B[i,j]>0: ax.plot([Fc[0,i],Fc[0,j]],[Fc[1,i],Fc[1,j]],'-',color='crimson',lw=1.3,zorder=5)
ax.scatter(Fc[0],Fc[1],c='white',edgecolors='crimson',s=14,zorder=6)
ax.scatter(Fc[0,root],Fc[1,root],c='lime',edgecolors='k',s=50,zorder=7)
frame(ax); ax.set_title('Pseudotime',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"manifold.pdf"),bbox_inches='tight'); plt.close(fig)

# 3) signatures (raw, plasma), no celltype overlay
for key,short,title in [('Gast','Gast','Gastrulation Signature'),('pSom','pSom','Somitogenesis Signature'),('Crest','Crest','Neural Crest Signature')]:
    fig,ax=plt.subplots(figsize=FS)
    sc.pl.umap(a,color=key,cmap='plasma',alpha=.5,size=8,colorbar_loc=None,frameon=False,show=False,ax=ax)
    frame(ax); ax.set_title(title,size=7.5); cite(ax)
    fig.savefig(os.path.join(F_,short+"_signature.pdf"),bbox_inches='tight'); plt.close(fig)

# 4) expression: single-gene ZEB2 (blue), 75th-pctile-among-expressers threshold
def _vec(gene):
    x=a[:,gene].X; return np.asarray(x.todense()).ravel() if hasattr(x,'todense') else np.asarray(x).ravel()
gene='ZEB2'; v=_vec(gene); pos=v[v>0]; thr=float(np.quantile(pos,0.75)) if pos.size else 0.0
sel=v>thr
fig,ax=plt.subplots(figsize=FS)
sc.pl.umap(a,size=8,alpha=.4,frameon=False,show=False,ax=ax,na_color='lightgray')
sc.pl.umap(a[sel].copy(),na_color='tab:blue',size=8,alpha=.7,frameon=False,show=False,ax=ax)
frame(ax)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color='tab:blue',label=f'{gene} (5.1%)')],
          frameon=False,loc='upper right',fontsize=5,handletextpad=.2,borderaxespad=0.2)
ax.set_title('EMT-TF Expression  ZEB2',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated all 6 Wu2020 panels at house (3.5,1.5)")
