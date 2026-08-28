"""Preprocessing-stage manuscript outputs for Ji2020_Skin. FIRST link in the chain.

Reads : run-9 processed.h5ad  (the §6 preprocessing artifact — this step's declared
        input; nothing downstream is read, so provenance flows strictly forward)
Writes: DATA/processed.h5ad   - run-9 processed SUBSET to retained cells (seeded
        res=1.0 Leiden spur cluster + TSK removed). The canonical display orientation
        is FIXED HERE (obsm['X_umap_oriented'] = X_umap @ ORIENT_M.T) and carried
        forward by every later step, so all panels share one orientation. No
        trajectory/pseudotime added here (step boundary kept clean).
        FIG/samples.pdf       - sample-coloured manifold (Gate-1 integration view),
        locked config (5x5, equal aspect, s=15), drawn from the stored oriented coords.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd, scanpy as sc, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import _common as C

os.makedirs(C.DATA, exist_ok=True); os.makedirs(C.FIG, exist_ok=True)

# --- read the run-9 preprocessing artifact; subset by the seeded-Leiden removal ---
P = sc.read_h5ad(os.path.join(C.SRC, "processed.h5ad"))
C.leiden_r1(P)                       # seeded res=1.0 Leiden = reproducible removal basis
mask = C.keep_mask(P)
Psub = P[mask].copy()
Psub.obs['leiden_r1'] = P.obs['leiden_r1'][mask].values   # removal-basis provenance
print(f"kept {int(mask.sum())} / {P.n_obs}  (removed {int((~mask).sum())}: "
      f"spur cluster {C.REMOVE_LEIDEN_R1} + {C.REMOVE_CELLTYPE})")

# --- FIX the display orientation once, store it, carry forward ---
C.orient(Psub)                       # writes Psub.obsm['X_umap_oriented']
Psub.write(os.path.join(C.DATA, "processed.h5ad"))
print(f"wrote {C.DATA}/processed.h5ad  shape={Psub.shape}")

# --- samples.pdf (from the stored oriented coords) ---
xy = C.oriented_umap(Psub)
samp = Psub.obs['sample'].astype('category'); cats = samp.cat.categories
fig, ax = plt.subplots(figsize=C.FIGSIZE)
for i, sm in enumerate(cats):
    m = (samp == sm).values
    ax.scatter(xy[m, 0], xy[m, 1], s=C.SAMPLES_POINT_SIZE, linewidths=0,
               color=plt.cm.tab20(i % 20), rasterized=False)
ax.legend(handles=[Line2D([0], [0], marker='o', color='w',
          markerfacecolor=plt.cm.tab20(i % 20), markersize=7, label=sm)
          for i, sm in enumerate(cats)],
          frameon=False, loc='lower left', fontsize=8, ncol=2,
          handletextpad=.2, columnspacing=.8)
C.frame(ax, xy)
fig.savefig(os.path.join(C.FIG, "samples.pdf"), bbox_inches='tight', dpi=300)
plt.close(fig)
print(f"wrote {C.FIG}/samples.pdf")
