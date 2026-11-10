import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Hematologic/Rendeiro2020_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Rendeiro2020_Hematologic"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
a.obsm['X_umap']=a.obsm['X_umap_lin']   # root-left (+0.92)
xl=a.obsm['X_umap']; xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
# samples (no legend; base had a 7-sample legend)
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=10,alpha=.8,frameon=False,show=False,ax=ax)
lg=ax.get_legend()
if lg is not None: lg.remove()
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title('CLL malignant manifold \u2014 samples',size=7.5)
ax.text(.5,-.12,'Rendeiro et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
# expression ZEB2 blue / ZEB1 red (house; base used blue/orange), top-quartile among expressers
def _vec(g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
tf1,tf2='ZEB2','ZEB1'; colors={tf1:'tab:blue',tf2:'tab:red'}
thr={g:(float(np.quantile(_vec(g)[_vec(g)>0],0.75)) if (_vec(g)>0).any() else 0.0) for g in [tf1,tf2]}
sel={g:_vec(g)>thr[g] for g in [tf1,tf2]}
order=sorted([tf1,tf2],key=lambda g:-int(sel[g].sum()))
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=30,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[sel[g]].copy(),na_color=colors[g],size=30,alpha=.8,frameon=False,show=False,ax=ax)
ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
ax.set_title(f'EMT-TF Expression   {tf1} \u00b7 {tf2}  (both early-skewed)',size=7.5)
ax.text(.5,-.14,'Rendeiro et al., 2020',ha='center',transform=ax.transAxes,size=6)
fig.savefig(os.path.join(F,'expression.pdf'),bbox_inches='tight'); plt.close(fig)
print("regen Rendeiro samples(no legend) + expression(ZEB2 blue/ZEB1 red) | corr=%.3f"%np.corrcoef(xl[:,0],a.obs['t'].values)[0,1])
