import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
D="/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Pancreas/Peng2019_Pancreas"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Peng2019_Pancreas"
CB=os.path.join(F,"colorbars"); os.makedirs(CB,exist_ok=True)
CITE="Peng et al., 2019"
a=sc.read_h5ad(os.path.join(D,"signatures.h5ad"))
xl=a.obsm['X_umap']                      # raw==lin (+0.86), already root-left
xlo,xhi=np.percentile(xl[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xl[:,1],[0.3,99.7])
px=(xhi-xlo)*.05; py=(yhi-ylo)*.08
def setlim(ax): ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
def cite(ax): ax.text(.5,-.14,CITE,ha='center',transform=ax.transAxes,size=6)
# samples (house strip, legend kept per Peng's final convention)
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='sample',size=14,alpha=.8,frameon=False,show=False,ax=ax,title='PDAC malignant manifold \u2014 samples')
h,l=ax.get_legend_handles_labels()
ax.legend(h,l,ncol=2,frameon=False,loc='center left',bbox_to_anchor=(1.02,.5),handletextpad=.2,labelspacing=.25,columnspacing=.6,fontsize=4.5,title='sample',title_fontsize=5)
ax.title.set_size(7.5); setlim(ax); cite(ax)
fig.savefig(os.path.join(F,"samples.pdf"),bbox_inches='tight'); plt.close(fig)
# pseudotime + curve
B=np.asarray(a.uns['graph']['B']); Fn=a.uns['graph']['F'].T
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,color='t',cmap='cividis',size=14,alpha=.85,colorbar_loc='right',frameon=False,show=False,ax=ax,title='Pseudotime')
ii,jj=np.where(np.triu(B>0))
for u,v in zip(ii,jj): ax.plot([Fn[u,0],Fn[v,0]],[Fn[u,1],Fn[v,1]],'-',c='k',lw=0.8,zorder=5)
ax.title.set_size(7.5); setlim(ax); cite(ax)
fig.savefig(os.path.join(F,"manifold.pdf"),bbox_inches='tight'); plt.close(fig)
# signatures (plasma + separate colorbars)
titles={'Gast':'Gastrulation Signature','pSom':'Somitogenesis Signature','Crest':'Neural Crest Signature'}
for m in ['Gast','pSom','Crest']:
    fig,ax=plt.subplots(figsize=(3.5,1.5))
    sc.pl.umap(a,color=m,cmap='plasma',alpha=.75,size=14,colorbar_loc=None,frameon=False,show=False,ax=ax,title=titles[m])
    ax.title.set_size(7.5); setlim(ax); cite(ax)
    fig.savefig(os.path.join(F,f"{m}_signature.pdf"),bbox_inches='tight')
    lo,hi=float(a.obs[m].min()),float(a.obs[m].max()); ticks=np.round(np.linspace(lo,hi,5),2)
    fcb=plt.figure(figsize=(.66,1)); cax=fcb.add_axes([.35,.05,.3,.9])
    cb=plt.colorbar(ax.collections[0],cax=cax); cb.ax.tick_params(which='both',size=0)
    cb.set_label(f'{m}\nSignature'); cb.set_ticks(ticks,labels=ticks); cb.solids.set_alpha(1)
    fcb.savefig(os.path.join(CB,f"{m}_colorbar.pdf"),bbox_inches='tight'); plt.close('all')
# expression (freeze first-run pair ZEB1 early -> SNAI2 late)
early_tf,late_tf='ZEB1','SNAI2'
def _vec(g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()
thr={g:(float(np.quantile(_vec(g)[_vec(g)>0],0.75)) if (_vec(g)>0).any() else 0.0) for g in [early_tf,late_tf]}
sel={g:_vec(g)>thr[g] for g in [early_tf,late_tf]}
order=sorted([early_tf,late_tf],key=lambda g:-int(sel[g].sum()))
colors={early_tf:'tab:blue',late_tf:'tab:red'}
fig,ax=plt.subplots(figsize=(3.5,1.5))
sc.pl.umap(a,size=14,alpha=.3,frameon=False,show=False,ax=ax,na_color='lightgray')
for g in order:
    sc.pl.umap(a[sel[g]].copy(),na_color=colors[g],size=14,alpha=.85,frameon=False,show=False,ax=ax)
ax.set_title(f'EMT-TF Expression   {early_tf} (early) \u00b7 {late_tf} (late)',size=7.5)
setlim(ax); cite(ax)
fig.savefig(os.path.join(F,"expression.pdf"),bbox_inches='tight'); plt.close(fig)
print("regen Peng strip | EMT %s->%s | corr=%.3f"%(early_tf,late_tf,np.corrcoef(xl[:,0],a.obs['t'].values)[0,1]))
