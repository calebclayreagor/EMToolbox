import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Pancreas/Hwang2022_Pancreas-3"
F_="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Hwang2022_Pancreas-3"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
t=a.obs['t'].values
# original panels: raw scatter + invert_xaxis, raw corr(x,t)=+0.677 -> displayed origin-RIGHT.
# house left->right: negate x (origin-left) and DON'T invert_x. keep invert_y for vertical convention.
xy=a.obsm['X_umap'].copy()  # raw already origin-left (corr +0.677); drop the notebook's invert_xaxis
print("display corr(x,t)=%.3f"%np.corrcoef(xy[:,0],t)[0,1])
xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
def frame(ax):
    ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(yhi+py,ylo-py)  # invert_y via reversed ylim
    ax.axis('off')
def cite(ax,y=-.12): ax.text(.5,y,'Hwang et al., 2022',ha='center',transform=ax.transAxes,size=6)
HS=(3.5,1.5)
# samples (no legend)
fig,ax=plt.subplots(figsize=HS)
a.obsm['X_umap']=xy
sc.pl.umap(a,color='sample',size=6,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg: lg.remove()
frame(ax); ax.set_title('PDAC malignant manifold — samples',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# manifold: cividis t + crimson curve (F x-negated)
Fc=np.asarray(a.uns['graph']['F']).copy(); B=np.asarray(a.uns['graph']['B']); root=int(np.asarray(a.uns['graph']['root']))
fig,ax=plt.subplots(figsize=HS)
ax.scatter(xy[:,0],xy[:,1],c=t,cmap='cividis',s=2,linewidths=0,rasterized=True)
ii,jj=np.where(np.triu(B>0))
for i,j in zip(ii,jj): ax.plot([Fc[0,i],Fc[0,j]],[Fc[1,i],Fc[1,j]],'-',color='crimson',lw=1.0,zorder=3)
ax.scatter(Fc[0],Fc[1],s=6,color='crimson',zorder=4)
frame(ax); ax.set_title('Pseudotime',size=7.5); cite(ax,-.08)
fig.savefig(os.path.join(F_,"manifold.pdf"),bbox_inches='tight'); plt.close(fig)
# signatures plasma (raw scatter, p2-98 clip)
for k,fn,title in [('Gast','Gast_signature','Gastrulation Signature'),
                   ('pSom','pSom_signature','Somitogenesis Signature'),
                   ('Crest','Crest_signature','Neural Crest Signature')]:
    v=a.obs[k].values; lo,hi=np.percentile(v,[2,98])
    fig,ax=plt.subplots(figsize=HS)
    ax.scatter(xy[:,0],xy[:,1],c=v,cmap='plasma',vmin=lo,vmax=hi,s=2,alpha=.5,linewidths=0,rasterized=True)
    frame(ax); ax.set_title(title,size=7.5); cite(ax,-.08)
    fig.savefig(os.path.join(F_,fn+".pdf"),bbox_inches='tight'); plt.close(fig)
# EMT FOXC1(blue)/ZEB1(red)
def _vec(g): x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
early_tf,late_tf='FOXC1','ZEB1'; colors={early_tf:'tab:blue',late_tf:'tab:red'}
thr={g:(float(np.quantile(_vec(g)[_vec(g)>0],0.75)) if (_vec(g)>0).any() else 0.0) for g in [early_tf,late_tf]}
sel={g:_vec(g)>thr[g] for g in [early_tf,late_tf]}
order=sorted([early_tf,late_tf],key=lambda g:-int(sel[g].sum()))
fig,ax=plt.subplots(figsize=HS)
ax.scatter(xy[:,0],xy[:,1],c='lightgray',s=6,alpha=.3,linewidths=0,rasterized=True)
for g in order:
    m=sel[g]; ax.scatter(xy[m,0],xy[m,1],c=colors[g],s=6,alpha=.85,linewidths=0,rasterized=True)
frame(ax); ax.set_title('EMT-TF Expression   FOXC1 (blue) · ZEB1 (red)',size=7.5); cite(ax)
fig.savefig(os.path.join(F_,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regenerated all 6 panels house-strip, left->right")
