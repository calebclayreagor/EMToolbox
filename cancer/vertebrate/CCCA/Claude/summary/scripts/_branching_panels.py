"""Shared branching-panel regenerator (strip aspect, bisector root-left, per-cell).

Regenerates the 6 embedding strips + correlation panel for a branching dataset,
reading the FROZEN signatures.h5ad and writing (3.5,1.5) house-strip PDFs into the
deliverable FIGURES tree. Rotation = angular bisector of the root->tip unit vectors,
so the trajectory root is the left anchor and both terminal tips fan right.

Science is untouched: every value is re-derived from the frozen h5ad; only the
display (rotation, aspect, per-cell coloring) is regenerated.

Usage (from a per-dataset regen_<name>.py):
    from _branching_panels import regen_branching
    regen_branching(DATA_DIR, FIG_DIR, title_prefix, emt=[('PRRX1','tab:blue'),('ZEB1','tab:red')],
                    emt_q=0.80, hub_celltype='Mixed', samples_title='... samples')
"""
import os, numpy as np, pandas as pd, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patheffects import withStroke
from scipy.stats import pearsonr

FEAT = "/home/caleb/MesenCoder/data/features/biomart"


def _bisector_rotation(a):
    """Rigid rotation matrix aligning the root->tips angular bisector with +x."""
    g = a.uns['graph']; B = np.asarray(g['B']); F = np.asarray(g['F'])
    Fp = F.T if F.shape[0] == 2 else F
    deg = (B > 0).sum(0); tips = np.where(deg == 1)[0]
    root = int(np.asarray(g['root']).ravel()[0])
    term = [int(t) for t in tips if int(t) != root]
    dirs = [(Fp[t] - Fp[root]) / np.linalg.norm(Fp[t] - Fp[root]) for t in term]
    axis = np.sum(dirs, 0); axis /= np.linalg.norm(axis)
    ang = np.arctan2(axis[1], axis[0]); c, s = np.cos(-ang), np.sin(-ang)
    return np.array([[c, -s], [s, c]])


def _dense(a, gene):
    x = a[:, gene].X
    return x.toarray().ravel() if hasattr(x, 'toarray') else np.asarray(x).ravel()


def regen_branching(D, F, samples_title, emt, emt_q=0.80, hub_celltype='Mixed'):
    """D=data dir (frozen h5ads), F=figures dir (output). emt=[(gene,color),...]."""
    os.makedirs(F, exist_ok=True)
    a = sc.read_h5ad(os.path.join(D, "signatures.h5ad"))
    a.obsm['X_umap'] = a.obsm['X_umap'] @ _bisector_rotation(a).T
    xy = a.obsm['X_umap']
    xlo, xhi = xy[:, 0].min(), xy[:, 0].max()
    ylo, yhi = xy[:, 1].min(), xy[:, 1].max()
    xpad = (xhi - xlo) * .06; ypad = (yhi - ylo) * .10

    def lab(ax):
        for ct in a.obs['celltype'].cat.categories:
            m = (a.obs['celltype'] == ct).values
            if m.sum():
                ax.text(xy[m, 0].mean(), xy[m, 1].mean(), ct, size=6, weight='bold',
                        ha='center', va='center',
                        path_effects=[withStroke(linewidth=1.2, foreground='white')])

    def strip(fname, fn):
        fig, ax = plt.subplots(figsize=(3.5, 1.5)); fn(ax)
        ax.set_xlim(xlo - xpad, xhi + xpad); ax.set_ylim(ylo - ypad, yhi + ypad); ax.axis('off')
        fig.savefig(os.path.join(F, fname), bbox_inches='tight', dpi=300); plt.close(fig)

    def _samp(ax):
        for i, sm in enumerate(a.obs['sample'].astype('category').cat.categories):
            m = (a.obs['sample'] == sm).values
            ax.scatter(xy[m, 0], xy[m, 1], s=4, linewidths=0, alpha=.85,
                       color=plt.cm.tab20(i % 20), rasterized=True)
    strip("samples.pdf", _samp)
    strip("manifold.pdf", lambda ax: (ax.scatter(xy[:, 0], xy[:, 1], c=a.obs['t'].values,
                                                  cmap='cividis', s=4, linewidths=0, rasterized=True), lab(ax)))
    for key, fn in [('GSE162534', 'Gast_signature.pdf'), ('GSE229103', 'pSom_signature.pdf'),
                    ('rRNAModifications', 'Crest_signature.pdf')]:
        strip(fn, (lambda k: (lambda ax: (ax.scatter(xy[:, 0], xy[:, 1], c=a.obs[k].values,
              cmap='plasma', s=4, linewidths=0, alpha=.7, rasterized=True), lab(ax))))(key))

    # EMT-TF two-gene overlay (thresholded expressers on grey)
    def thr(gene, q=emt_q):
        x = _dense(a, gene); pos = x[x > 0]
        return np.quantile(pos, q) if pos.size else np.inf

    def _expr(ax):
        ax.scatter(xy[:, 0], xy[:, 1], s=4, linewidths=0, color='lightgrey', alpha=.5, rasterized=True)
        for gene, col in emt:
            v = _dense(a, gene); sel = v > thr(gene)
            ax.scatter(xy[sel, 0], xy[sel, 1], s=5, linewidths=0, color=col, alpha=.7, rasterized=True)
        lab(ax)
        ax.legend(handles=[Line2D([0], [0], marker='o', color='w', markerfacecolor=col,
                  markersize=5, label=g) for g, col in emt],
                  frameon=False, loc='lower right', fontsize=5)
    strip("expression.pdf", _expr)

    # correlation gradient on the hub celltype (kept as deliverable; omitted from summary embed)
    try:
        gf = lambda p: set(pd.read_csv(p).hsapiens.dropna())
        gast = gf(os.path.join(FEAT, 'GSE162534.csv')); psom = gf(os.path.join(FEAT, 'GSE229103.csv'))
        genes = pd.Series(list(gast ^ psom)); genes = genes[genes.isin(a.var_names)]
        hub = (a.obs['celltype'] == hub_celltype).values
        ac = a[hub, genes.tolist()].copy(); tt = ac.obs.t
        nb = max(3, tt.size // 60); tb = pd.cut(tt, bins=nb); ac.obs['t_bin'] = tb
        rd = {}
        for b, sdf in ac.obs.groupby('t_bin', observed=True):
            if len(sdf) < 3: rd[b] = np.nan; continue
            ab = ac[sdf.index].copy()
            X = pd.DataFrame(ab.X.toarray() if hasattr(ab.X, 'toarray') else np.asarray(ab.X),
                             index=sdf.index, columns=genes.tolist())
            X = X.loc[:, X.nunique(0) > 1]
            if X.shape[1] < 2: rd[b] = np.nan; continue
            r1 = pearsonr(X, sdf.GSE162534.values[:, None], axis=0).statistic
            r2 = pearsonr(X, sdf.GSE229103.values[:, None], axis=0).statistic
            rd[b] = np.corrcoef(r1, r2)[0, 1]
        A = ac.obsp['connectivities']; R = tb.map(rd).astype(float).fillna(0.0)
        Rsm = (A @ R.values) / np.asarray(A.sum(1)).ravel()
        corr = np.full(a.n_obs, np.nan); corr[np.where(hub)[0]] = Rsm

        def _corr(ax):
            ax.scatter(xy[:, 0], xy[:, 1], s=4, linewidths=0, color='lightgrey', alpha=.5, rasterized=True)
            m = ~np.isnan(corr)
            ax.scatter(xy[m, 0], xy[m, 1], c=corr[m], cmap='Spectral', vmin=-.5, vmax=.5,
                       s=4, linewidths=0, alpha=.85, rasterized=True)
            lab(ax)
        strip("correlation.pdf", _corr)
    except Exception as e:
        print("  [warn] correlation panel skipped:", e)
    print(f"  regenerated 6 strips + correlation into {F}")
