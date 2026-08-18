import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
D="/home/caleb/MesenCoder/data/cancer/vertebrate/CCCA/Claude/Breast/Griffiths2021_Breast-5"
F_="/home/caleb/MesenCoder/figures/cancer/vertebrate/CCCA/Claude/Breast/Griffiths2021_Breast-5"
CB=os.path.join(F_,"colorbars")
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
proc=sc.read_h5ad(os.path.join(D,"processed.h5ad"))
g=a.uns['graph']; Fc=np.asarray(g['F']); B=np.asarray(g['B']); root=int(np.asarray(g['root']))
FS=(3.5,1.5); CITE='Griffiths et al., 2021'
def frame(ax):
    ax.invert_yaxis(); ax.invert_xaxis()
def cite(ax):
    ax.text(.5,-.12,CITE,ha='center',transform=ax.transAxes,size=6)

# 1) samples (processed, no legend)
fig,ax=plt.subplots(figsize=FS)
sc.pl.umap(proc,color='sample',size=6,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
frame(ax); ax.set_title('Breast Cancer Samples',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"samples.pdf"),bbox_inches='tight'); plt.close(fig)

# 2) manifold: pseudotime + fitted curve + root
fig,ax=plt.subplots(figsize=FS)
sc.pl.umap(a,color='t',cmap='cividis',size=10,colorbar_loc=None,frameon=False,show=False,ax=ax)
for i in range(B.shape[0]):
    for j in range(i+1,B.shape[1]):
        if B[i,j]>0: ax.plot([Fc[0,i],Fc[0,j]],[Fc[1,i],Fc[1,j]],'-',color='#d1495b',lw=1.4,zorder=10)
ax.scatter(Fc[0,root],Fc[1,root],c='lime',s=60,edgecolor='k',lw=.5,zorder=11)
frame(ax); ax.set_title('Pseudotime',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"manifold.pdf"),bbox_inches='tight'); plt.close(fig)

# 3) signatures
for key,short,title in [('Gast','Gast','Gastrulation Signature'),('pSom','pSom','Somitogenesis Signature'),('Crest','Crest','Neural Crest Signature')]:
    v=a.obs[key]; vmin,vmax=np.percentile(v,2),np.percentile(v,98)
    fig,ax=plt.subplots(figsize=FS)
    sc.pl.umap(a,color=key,cmap='plasma',alpha=.5,size=10,colorbar_loc=None,frameon=False,show=False,ax=ax,vmin=vmin,vmax=vmax)
    frame(ax); ax.set_title(title,size=7.5); cite(ax)
    fig.savefig(os.path.join(F_,short+"_signature.pdf"),bbox_inches='tight'); plt.close(fig)

# 4) expression: ZEB1 blue / ZEB2 red, median-nz threshold, inline legend
def _vec(gene):
    x=a[:,gene].X; return np.asarray(x.todense()).ravel() if hasattr(x,'todense') else np.asarray(x).ravel()
genes=['ZEB1','ZEB2']; colors={'ZEB1':'tab:blue','ZEB2':'tab:red'}; thr={}
for gene in genes:
    x=_vec(gene); nz=x[x>0]; thr[gene]=float(np.quantile(nz,0.5)) if nz.size else 0.0
sel={gene:_vec(gene)>thr[gene] for gene in genes}
order=sorted(genes,key=lambda gg:-int(sel[gg].sum()))
fig,ax=plt.subplots(figsize=FS)
sc.pl.umap(a,size=10,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for gene in order:
    sc.pl.umap(a[sel[gene]].copy(),na_color=colors[gene],size=10,alpha=.7,frameon=False,show=False,ax=ax)
frame(ax)
ax.legend(handles=[Line2D([],[],marker='o',ls='',color=colors[gene],label=gene) for gene in genes],
          frameon=False,loc='upper right',fontsize=5,handletextpad=.2,borderaxespad=0.2)
ax.set_title('EMT-TF Expression  ZEB1 · ZEB2',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated all 6 Griffiths panels at house (3.5,1.5)")
