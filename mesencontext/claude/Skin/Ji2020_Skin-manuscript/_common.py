"""Shared config + helpers for the Ji2020_Skin manuscript panels.

Visualization/science decisions locked with the researcher (see running list):
  - cluster removal: seeded Leiden res=1.0 (igraph, random_state=0) cluster '4'
    (Basal-root spur) + celltype 'TSK'. The seed makes the label reproducible;
    no derived rule.
  - orientation: a single FROZEN transform M (ORIENT_M) put the Basal root at the
    TOP; computed once from the approved Option-C tree, then applied at preprocessing
    and carried forward as obsm['X_umap_oriented'] so every panel shares it exactly.
  - aspect: square (5,5) axes box, aspect='auto' (data fills the box; not true
    UMAP geometry — the researcher wants literal 5x5 axes, not equal data units).
  - per-cell point size: trajectory-stage panels s=30 (manifold/signatures/
    correlation/expression); samples panel s=15 (smaller tier, mirrors Puram 120 vs 180).
  - celltype labels: size 12, bold, white outline (matches the trajectory-spine leaf labels).

All reads are from the FROZEN run-9 h5ads (read-only). Per-step artifacts are
kept separate (processed.h5ad / manifold.h5ad / ...) — step boundaries are not
blurred.
"""
import os, sys
os.environ['R_HOME'] = sys.exec_prefix + '/lib/R/'
import numpy as np, pandas as pd, scanpy as sc
from matplotlib.patheffects import withStroke

SRC   = "/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Skin/Ji2020_Skin-9"
DATA  = "/home/caleb/EMToolbox/data/cancer/vertebrate/CCCA/claude/Skin/Ji2020_Skin-manuscript"
FIG   = "/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Ji2020_Skin-manuscript"

FIGSIZE    = (5, 5)
POINT_SIZE = 30          # per-cell scatter size for the trajectory-stage panels
                         # (manifold, signatures, correlation, expression)
SAMPLES_POINT_SIZE = 15  # samples/integration panel — smaller tier (mirrors Puram's
                         # 120 vs 180 two-tier: samples smaller than trajectory panels)
LABEL_SIZE = 12
REMOVE_LEIDEN_R1 = "4"   # Basal-root spur (seeded res=1.0 label)
REMOVE_CELLTYPE  = "TSK" # tumor-specific keratinocyte terminal readout


def leiden_r1(a):
    """Seeded res=1.0 Leiden (the reproducible basis for cluster removal)."""
    sc.tl.leiden(a, resolution=1.0, key_added='leiden_r1', flavor='igraph',
                 n_iterations=2, directed=False, random_state=0)
    return a.obs['leiden_r1']


def keep_mask(a):
    """Boolean mask of retained cells: drop spur cluster + TSK celltype."""
    if 'leiden_r1' not in a.obs:
        leiden_r1(a)
    return ((a.obs['leiden_r1'] != REMOVE_LEIDEN_R1) &
            (a.obs['celltype'] != REMOVE_CELLTYPE)).values


# Canonical display orientation, FROZEN once (Basal root at TOP, arms fanning down).
# Derived a single time from the approved Option-C tree (root->tips angular bisector,
# then axis-swap) and hard-frozen here as a constant transform: oriented = X_umap @ M.T.
# Fixing it at the start of the chain and carrying `X_umap_oriented` forward through
# every h5ad guarantees ALL panels share one orientation (no per-object re-derivation,
# no drift). An orientation is a one-time design choice, like POINT_SIZE / FIGSIZE.
ORIENT_M = np.array([[ 0.87813381,  0.4784151 ],
                     [-0.4784151 ,  0.87813381]])


def orient(a):
    """Apply the frozen transform, STORE it as obsm['X_umap_oriented'], and return it.
    Called once at the start of the chain (preprocessing); carried forward in obsm."""
    a.obsm['X_umap_oriented'] = a.obsm['X_umap'] @ ORIENT_M.T
    return a.obsm['X_umap_oriented']


def oriented_umap(a):
    """Basal-top oriented coords: the stored obsm['X_umap_oriented'] if present
    (carried forward from preprocessing), else the frozen transform applied fresh."""
    if 'X_umap_oriented' in a.obsm:
        return a.obsm['X_umap_oriented']
    return a.obsm['X_umap'] @ ORIENT_M.T


def zsort(v, negatives_on_top=False):
    """Draw-order index for a continuous scatter (matches scanpy sort_order=True):
    plot the emphasized value LAST so it sits on top. Default = highest on top
    (signatures, pseudotime); negatives_on_top=True puts the most-negative last
    (correlation, where the cross-repression signal is the strong negative)."""
    import numpy as _np
    order = _np.argsort(_np.asarray(v))            # ascending -> highest last (on top)
    return order[::-1] if negatives_on_top else order  # descending -> most-negative last


def celltype_labels(ax, xy, a, mask):
    for c in a.obs['celltype'].cat.categories:
        if c == REMOVE_CELLTYPE:
            continue
        m = (a.obs['celltype'] == c).values & mask
        if m.sum():
            ax.text(xy[m, 0].mean(), xy[m, 1].mean(), c, size=LABEL_SIZE,
                    weight='bold', ha='center', va='center',
                    path_effects=[withStroke(linewidth=1.4, foreground='white')])


def frame(ax, xy_sub):
    xlo, xhi = xy_sub[:, 0].min(), xy_sub[:, 0].max()
    ylo, yhi = xy_sub[:, 1].min(), xy_sub[:, 1].max()
    xpad = (xhi - xlo) * .06; ypad = (yhi - ylo) * .06
    ax.set_xlim(xlo - xpad, xhi + xpad); ax.set_ylim(ylo - ypad, yhi + ypad)
    ax.set_aspect('auto'); ax.axis('off')   # fill the square (5,5) axes box (not true geometry)
