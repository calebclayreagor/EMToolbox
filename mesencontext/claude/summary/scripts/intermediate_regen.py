"""Reusable house-style panel regen for intermediate-run standardization.
regen6 = GO 6-panel set (samples/pseudotime/Gast/pSom/Crest/expression) from signatures.h5ad.
regen2 = NO-GO 2-panel set (samples/expression) from processed.h5ad.
Orientation: uses X_umap_lin if present and better pt-correlated, else raw X_umap.
EMT pair auto-derived from canonical TFs by pseudotime position, or caller-specified."""
import os, numpy as np, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D

CANON=['SNAI1','SNAI2','ZEB1','ZEB2','TWIST1','TWIST2','FOXC1','FOXC2','PRRX1','PRRX2']

def _vec(a,g):
    x=a[:,g].X; return x.toarray().ravel() if hasattr(x,'toarray') else np.asarray(x).ravel()

def _orient(a):
    xl=a.obsm.get('X_umap_lin')
    if xl is not None: return xl
    return a.obsm['X_umap']

def _lims(xy):
    xlo,xhi=np.percentile(xy[:,0],[0.3,99.7]); ylo,yhi=np.percentile(xy[:,1],[0.3,99.7])
    return xlo,xhi,ylo,yhi,(xhi-xlo)*.05,(yhi-ylo)*.08

def _emt_pair(a, src, genes=None):
    """Return (early_tf, late_tf) by pseudotime position among detectable (>3%) canonical TFs."""
    if genes and len(genes)>=2: return genes[0],genes[1]
    t=a.obs['t'].values if 't' in a.obs else None
    cand=[g for g in CANON if g in src.var_names and (_vec(src,g)>0).mean()>0.03]
    if len(cand)<2: cand=[g for g in CANON if g in src.var_names][:2]
    if t is None or len(cand)<2: return (cand+['',''])[0],(cand+['',''])[1]
    mpt={}
    for g in cand:
        v=_vec(src,g); m=v>np.quantile(v[v>0],0.75) if (v>0).any() else v>0
        mpt[g]=t[m].mean() if m.any() else np.nan
    sg=sorted([g for g in cand if not np.isnan(mpt[g])], key=lambda g:mpt[g])
    return sg[0],sg[-1]

def regen6(D,F,cite,samples_title,emt_genes=None,emt_label='early/late'):
    os.makedirs(os.path.join(F,'colorbars'),exist_ok=True)
    a=sc.read_h5ad(os.path.join(D,'signatures.h5ad'))
    a.obsm['X_umap']=_orient(a)
    # enforce root-left house convention: low pseudotime on the left (corr(x,t) >= 0)
    if 't' in a.obs:
        _t=a.obs['t'].values
        if np.corrcoef(a.obsm['X_umap'][:,0], _t)[0,1] < 0:
            a.obsm['X_umap']=a.obsm['X_umap']*np.array([-1.0,1.0])
    xy=a.obsm['X_umap']
    xlo,xhi,ylo,yhi,px,py=_lims(xy)
    def setlim(ax): ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
    def cite_(ax): ax.text(.5,-.12,cite,ha='center',transform=ax.transAxes,size=6)
    # samples
    fig,ax=plt.subplots(figsize=(3.5,1.5))
    sc.pl.umap(a,color='sample',size=12,alpha=.8,frameon=False,show=False,ax=ax)
    lg=ax.get_legend();
    if lg: lg.remove()
    setlim(ax); ax.set_title(samples_title,size=7.5); cite_(ax)
    fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
    # manifold (pseudotime)
    fig,ax=plt.subplots(figsize=(3.5,1.5))
    sc.pl.umap(a,color='t',cmap='cividis',size=12,alpha=.85,colorbar_loc='right',frameon=False,show=False,ax=ax,title='Pseudotime')
    setlim(ax); cite_(ax)
    fig.savefig(os.path.join(F,'manifold.pdf'),bbox_inches='tight'); plt.close(fig)
    # signatures
    titles={'Gast':'Gastrulation Signature','pSom':'Somitogenesis Signature','Crest':'Neural Crest Signature'}
    for mkey in ['Gast','pSom','Crest']:
        if mkey not in a.obs: continue
        fig,ax=plt.subplots(figsize=(3.5,1.5))
        sc.pl.umap(a,color=mkey,cmap='plasma',alpha=.7,size=12,colorbar_loc=None,frameon=False,show=False,ax=ax,title=titles[mkey])
        setlim(ax); cite_(ax)
        fig.savefig(os.path.join(F,f'{mkey}_signature.pdf'),bbox_inches='tight'); plt.close(fig)
        lo,hi=float(a.obs[mkey].min()),float(a.obs[mkey].max()); ticks=np.round(np.linspace(lo,hi,5),3)
        fcb=plt.figure(figsize=(.66,1)); cax=fcb.add_axes([.35,.05,.3,.9])
        import matplotlib as mpl
        cb=mpl.colorbar.ColorbarBase(cax,cmap=plt.get_cmap('plasma'),norm=mpl.colors.Normalize(lo,hi))
        cb.set_ticks(ticks); cb.ax.tick_params(labelsize=5)
        fcb.savefig(os.path.join(F,'colorbars',f'{mkey}_colorbar.pdf'),bbox_inches='tight'); plt.close(fcb)
    # expression
    full=a.raw.to_adata() if a.raw is not None else a
    full.obsm['X_umap']=a.obsm['X_umap']
    e,l=_emt_pair(a,full,emt_genes); colors={e:'tab:blue',l:'tab:red'}
    thr={g:(float(np.quantile(_vec(full,g)[_vec(full,g)>0],0.75)) if (_vec(full,g)>0).any() else 0.0) for g in [e,l]}
    sel={g:_vec(full,g)>thr[g] for g in [e,l]}
    order=sorted([e,l],key=lambda g:-int(sel[g].sum()))
    fig,ax=plt.subplots(figsize=(3.5,1.5))
    ax.scatter(xy[:,0],xy[:,1],s=6,c='lightgrey',linewidths=0,rasterized=True)
    for g in order: ax.scatter(xy[sel[g],0],xy[sel[g],1],s=7,c=colors[g],linewidths=0,rasterized=True)
    setlim(ax); ax.axis('off')
    ax.legend(handles=[Line2D([0],[0],marker='o',ls='',color=colors[e],label=f'{e}'),
                       Line2D([0],[0],marker='o',ls='',color=colors[l],label=f'{l}')],
              loc='upper right',frameon=False,fontsize=5,handletextpad=.2)
    ttl=f'EMT-TF Expression   {e} \u00b7 {l}' if emt_label=='plain' else f'EMT-TF Expression   {e} ({emt_label.split("/")[0]}) \u00b7 {l} ({emt_label.split("/")[-1]})'
    ax.set_title(ttl,size=7.5); cite_(ax)
    fig.savefig(os.path.join(F,'expression.pdf'),bbox_inches='tight'); plt.close(fig)
    return (e,l)

def regen2(D,F,cite,samples_title,emt_genes=None):
    """NO-GO 2-panel: samples (sample-colored, no legend) + expression (categorical overlay)."""
    a=sc.read_h5ad(os.path.join(D,'processed.h5ad'))
    xy=a.obsm['X_umap']; xlo,xhi,ylo,yhi,px,py=_lims(xy)
    def setlim(ax): ax.set_xlim(xlo-px,xhi+px); ax.set_ylim(ylo-py,yhi+py)
    def cite_(ax): ax.text(.5,-.12,cite,ha='center',transform=ax.transAxes,size=6)
    fig,ax=plt.subplots(figsize=(3.5,1.5))
    sc.pl.umap(a,color='sample',size=18,alpha=.8,frameon=False,show=False,ax=ax)
    lg=ax.get_legend()
    if lg: lg.remove()
    setlim(ax); ax.set_title(samples_title,size=7.5); cite_(ax)
    fig.savefig(os.path.join(F,'samples.pdf'),bbox_inches='tight'); plt.close(fig)
    full=a.raw.to_adata() if a.raw is not None else a; full.obsm['X_umap']=xy
    if emt_genes: genes=emt_genes[:2]
    else:
        det=[(g,(_vec(full,g)>0).mean()) for g in CANON if g in full.var_names]
        genes=[g for g,_ in sorted(det,key=lambda x:-x[1])[:2]]
    cols=['tab:blue','tab:red']
    fig,ax=plt.subplots(figsize=(3.5,1.5))
    ax.scatter(xy[:,0],xy[:,1],s=5,c='lightgrey',linewidths=0,rasterized=True)
    hand=[]
    for g,col in zip(genes,cols):
        v=_vec(full,g); pos=v[v>0]; thr=float(np.quantile(pos,0.75)) if pos.size else np.inf
        sel=v>=thr; ax.scatter(xy[sel,0],xy[sel,1],s=6,c=col,linewidths=0,rasterized=True)
        hand.append(Line2D([0],[0],marker='o',color='w',markerfacecolor=col,markersize=4,label=g))
    setlim(ax); ax.axis('off')
    ax.legend(handles=hand,loc='upper right',frameon=False,fontsize=5,handletextpad=.2)
    ax.set_title('EMT-TF expression',size=7.5); cite_(ax)
    fig.savefig(os.path.join(F,'expression.pdf'),bbox_inches='tight'); plt.close(fig)
    return tuple(genes)
