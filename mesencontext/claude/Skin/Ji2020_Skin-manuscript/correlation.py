"""Correlation-stage manuscript output for Ji2020_Skin (Gate-3 evidence panel).

Reuses the ACCEPTED run-9 04_correlation recipe VERBATIM: Gast XOR pSom genes on
the hub cells, equal-frequency pseudotime windows (~100 cells), per-window Pearson
of each gene vs each module, correlation of those two gene-wise vectors per window,
then kNN-graph smoothing. Hub = adata.obs['hub'] (the Basal fate-decision
compartment, carried from the manifold step). Display only — no h5ad (§6).

Reads : DATA/signatures.h5ad
Writes: FIG/correlation.pdf                (Spectral +/-0.5 hub overlay on grey)
        FIG/colorbars/R_colorbar.pdf       (external colorbar, inverted like run-9)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd, scanpy as sc, matplotlib.pyplot as plt
from scipy.stats import pearsonr
import _common as C

FEAT = "/home/caleb/EMToolbox/data/features/biomart"
CB   = os.path.join(C.FIG, "colorbars"); os.makedirs(CB, exist_ok=True)

adata = sc.read_h5ad(os.path.join(C.DATA, "signatures.h5ad"))
print("loaded signatures subset:", adata.shape)

# ---- run-9 04_correlation, VERBATIM ----
get_feat = lambda p: set(pd.read_csv(p).hsapiens)
gast = get_feat(os.path.join(FEAT, 'GSE162534.csv'))
psom = get_feat(os.path.join(FEAT, 'GSE229103.csv'))
g = pd.Series(list(gast ^ psom)); g = g.loc[g.isin(adata.var_names)]
print('XOR genes on manifold:', g.size)

msk = adata.obs['hub'].values
adata_corr = adata[msk, g.tolist()].copy()
print('hub cells:', int(msk.sum()))

n_cells = 100; t = adata_corr.obs.t
n_bins = max(2, t.size // n_cells)
t_bin = pd.qcut(t, q=n_bins, duplicates='drop'); adata_corr.obs['t_bin'] = t_bin
grp = adata_corr.obs.groupby('t_bin', observed=True)
print('windows:', t_bin.cat.categories.size, '| per-window:', grp.size().min(), '-', grp.size().max())

r_dict = {}
for b, sdf_bin in grp:
    adata_bin = adata_corr[sdf_bin.index].copy()
    X = pd.DataFrame(np.asarray(adata_bin.X.todense()) if hasattr(adata_bin.X, 'todense')
                     else np.asarray(adata_bin.X), index=sdf_bin.index, columns=g)
    X = X.loc[:, (X.nunique(axis=0) > 1)].copy()
    mod1 = sdf_bin.GSE162534.values[:, None]   # Gast
    mod2 = sdf_bin.GSE229103.values[:, None]   # pSom
    aa = pearsonr(X, mod1, axis=0).statistic
    bb = pearsonr(X, mod2, axis=0).statistic
    r_dict[b] = np.corrcoef(aa, bb)[0, 1]

A = adata_corr.obsp['connectivities']
R = t_bin.map(r_dict).astype(float)
R_sm = (A @ R) / A.sum(axis=1).A1
adata_corr.obs['correlation'] = R_sm
print('mean windowed r:', round(float(np.nanmean(list(r_dict.values()))), 3))

# ---- correlation.pdf: hub overlay (Spectral) on grey manifold, locked config ----
# scale set to the data range (R_sm spans ~-0.31..0.26); +/-0.3 symmetric keeps zero
# at the diverging-colormap midpoint so colour sign == correlation sign.
xy = C.oriented_umap(adata)          # frozen orientation carried forward, Basal-top
xy_hub = xy[msk]
vlim = .3
fig, ax = plt.subplots(figsize=C.FIGSIZE)
ax.scatter(xy[:, 0], xy[:, 1], s=C.POINT_SIZE, linewidths=0, color='lightgrey',
           alpha=.5, rasterized=True)
Rv = np.asarray(R_sm)
o = C.zsort(Rv, negatives_on_top=True)   # strongest cross-repression (negative) on top
sca = ax.scatter(xy_hub[o, 0], xy_hub[o, 1], c=Rv[o], cmap='Spectral',
                 vmin=-vlim, vmax=vlim, s=C.POINT_SIZE, linewidths=0, alpha=.5, rasterized=True)
C.celltype_labels(ax, xy, adata, np.ones(adata.n_obs, bool))
C.frame(ax, xy)
fig.savefig(os.path.join(C.FIG, "correlation.pdf"), bbox_inches='tight', dpi=300)
plt.close(fig)

# external colorbar (house style, inverted axis as in run-9)
fcb = plt.figure(figsize=(.66, 1)); cax = fcb.add_axes([.35, .05, .3, .9])
cb = plt.colorbar(sca, cax=cax); cb.ax.tick_params(which='both', size=0)
cb.set_label('Pearson\nCorrelation'); cb.ax.invert_yaxis()
ticks = np.asarray([-.3, -.15, 0, .15, .3]); cb.set_ticks(ticks, labels=ticks)
cb.solids.set_alpha(1)
fcb.savefig(os.path.join(CB, 'R_colorbar.pdf'), bbox_inches='tight'); plt.close(fcb)
print(f"wrote {C.FIG}/correlation.pdf + colorbars/R_colorbar.pdf")
print("done")