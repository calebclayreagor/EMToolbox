"""Expression-stage manuscript output for Ji2020_Skin (EMT-TF panel, unconditional).

Reuses the run-9 06_expression recipe: un-regressed log-norm expression (via
load_CCCA_adata) aligned to the processed subset, drawn as a CATEGORICAL overlay of
thresholded expressers on a grey manifold (NOT a continuous colormap — 04_test flags
the continuous version as a deliverable failure). Researcher-steered TF pair: PRRX2 +
SNAI2 (PRRX2 replaces run-9's SOX9). Display only, no h5ad (§6).

Reads : DATA/processed.h5ad  (subset + frozen orientation) + un-regressed raw expression
Writes: FIG/expression.pdf
"""
import os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, scanpy as sc, matplotlib.pyplot as plt
import _common as C
sys.path.append("/home/caleb/EMToolbox/mesencontext")
from scripts.load import load_CCCA_adata

proc = sc.read_h5ad(os.path.join(C.DATA, "processed.h5ad"))
xy = C.oriented_umap(proc)           # frozen orientation carried from preprocessing
print("loaded processed subset:", proc.shape)

# un-regressed log-norm expression, aligned to the subset cells
raw = load_CCCA_adata("/home/caleb/EMToolbox/data/unzip/CCCA/Data_Ji2020_Skin")
raw = raw[proc.obs_names].copy()

# EMT-TF panel: (colour, display threshold). PRRX2 sparse -> lower thresh; SNAI2 as run-9.
# Order = draw order: SNAI2 (dense) first, PRRX2 (sparse) last so it plots ON TOP.
g_plt = {'SNAI2': ('tab:red', 1.05),
         'PRRX2': ('tab:blue', 0.65)}

fig, ax = plt.subplots(figsize=C.FIGSIZE)
ax.scatter(xy[:, 0], xy[:, 1], s=C.POINT_SIZE, linewidths=0, color='lightgrey',
           alpha=.5, rasterized=False)
for var, (col, thresh) in g_plt.items():
    v = np.asarray(raw[:, var].X.todense()).ravel()
    sel = v > thresh
    ax.scatter(xy[sel, 0], xy[sel, 1], s=C.POINT_SIZE, linewidths=0, color=col,
               alpha=.5, rasterized=False)
    print(f"{var}: {int(sel.sum())} expressers > {thresh}")
C.celltype_labels(ax, xy, proc, np.ones(proc.n_obs, bool))
C.frame(ax, xy)
fig.savefig(os.path.join(C.FIG, "expression.pdf"), bbox_inches='tight', dpi=300)
plt.close(fig)
print(f"wrote {C.FIG}/expression.pdf")