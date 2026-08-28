"""Manifold-stage manuscript outputs for Ji2020_Skin.

Reuses the ACCEPTED run-9 02_manifold pipeline (data-driven Basal-tip root,
pseudotime seed, hub definition, milestone-renaming logic) with two researcher-
steered modifications, neither of which changes the run-9 branch topology
(3 tips: Basal/Differentiated/Mixed + 1 Basal fork, Basal root, Basal hub):
  1. input cell set = run-9 subset with the seeded res=1.0 Leiden spur cluster
     + TSK removed;
  2. PPT parameters re-tuned for the smoother manifold requested on the subset:
     Nodes=250, ppt_lambda=20000, ppt_sigma=0.5 (vs run-9 40/700/0.8). Chosen
     from a full N/lambda/sigma search (low-sigma + high-lambda regime): sharpest
     Basal-root gradient while holding the 3-tip topology.
The tree is refit over the FROZEN run-9 X_umap (no re-embedding).

Reads : DATA/processed.h5ad  (preprocessing-stage subset)
Writes: DATA/manifold.h5ad   (subset + PPT tree + pseudotime + milestones; §6 schema)
        FIG/manifold.pdf      (scFates trajectory spine, pseudotime cividis)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ['R_HOME'] = sys.exec_prefix + '/lib/R/'
import numpy as np, pandas as pd, scanpy as sc, scFates as scf, matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke
import _common as C

os.makedirs(C.DATA, exist_ok=True); os.makedirs(C.FIG, exist_ok=True)
adata = sc.read_h5ad(os.path.join(C.DATA, "processed.h5ad"))
print("loaded processed subset:", adata.shape)

# ---- run-9 02_manifold recipe; PPT params steered for the smoother subset fit ----
# fit the principal tree. Params re-tuned from a full search (Option C): low sigma
# sharpens the Basal root, high lambda holds the 3-tip topology against Mixed budding.
scf.tl.tree(adata, method='ppt', Nodes=250, ppt_lambda=20000, ppt_sigma=0.5,
            use_rep='X_umap', seed=1, plot=False, basis='umap')

# root at the Basal tip (COL17A1+/TP63+ progenitor keratinocytes = developmental
# origin); pick the Basal-annotated tip programmatically (data-driven, no hardcoded id)
B = adata.uns['graph']['B']; deg = (B > 0).sum(0)
F = adata.uns['graph']['F']; Resp = adata.obsm['X_R']
tips = np.where(deg == 1)[0]; forks = np.where(deg > 2)[0]
ct = adata.obs['celltype'].values
node_ct = np.array([pd.Series(Resp[:, n]).groupby(ct).sum().idxmax() for n in range(F.shape[1])])
root_tip = int([t for t in tips if node_ct[t] == 'Basal'][0])
print('tips', [(int(t), node_ct[t]) for t in tips])
print('forks', [(int(f), node_ct[f]) for f in forks])
print('root (Basal tip) =', root_tip)
scf.tl.root(adata, root_tip)
scf.tl.pseudotime(adata, n_jobs=4, seed=1)

# pseudotime smoothness check (adjacent-kNN correlation of t; ~1 = smooth monotone)
A = (adata.obsp['connectivities'] > 0).astype(int); ii, jj = A.nonzero()
sm = float(np.corrcoef(adata.obs['t'].values[ii], adata.obs['t'].values[jj])[0, 1])
print('pseudotime smoothness r =', round(sm, 3))

# Gate-3 hub = the Basal root compartment (fate-decision zone), stored for 04-05
adata.obs['hub'] = (adata.obs['celltype'] == 'Basal').values
print('hub (Basal) cells =', int(adata.obs['hub'].sum()))

# name milestones by biology, keeping labels unique (run-9 logic)
cats = list(adata.obs['milestones'].cat.categories); fork_ids = set(int(x) for x in forks)
base = {}
for n in cats:
    ni = int(n)
    base[n] = ('Basal_root' if ni == root_tip else 'Fork' if ni in fork_ids else str(node_ct[ni]))
cnt = {}; uniq = {}
for n in cats:
    b = base[n]; tot = list(base.values()).count(b); cnt[b] = cnt.get(b, 0) + 1
    uniq[n] = b if tot == 1 else f'{b}_{cnt[b]}'
scf.tl.rename_milestones(adata, new=uniq)
print('milestones:', list(adata.obs['milestones'].cat.categories))

adata.write(os.path.join(C.DATA, "manifold.h5ad"))
print(f"wrote {C.DATA}/manifold.h5ad  shape={adata.shape}")

# ---- manifold.pdf: scFates trajectory spine (per reference trajectories.pdf convention) ----
# Grey cells + fitted PPT spine coloured by pseudotime (cividis) with node dots at the
# tips/fork. scf.pl.trajectory places nodes by projecting the cell embedding through the
# soft-assignment responsibility (proj = embT·R / sum R), so pointing the basis at our
# frozen oriented coords makes the spine follow the locked orientation automatically.
adata.obsm['X_ori'] = np.asarray(C.oriented_umap(adata))
R = adata.obsm['X_R']
proj = (np.dot(adata.obsm['X_ori'].T, R) / R.sum(axis=0)).T   # principal-node coords, oriented frame
tips = list(adata.uns['graph']['tips'])
ct = adata.obs['celltype']
# leaf label = dominant celltype among each tip's highest-responsibility cells (data-driven)
tip_lab = {t: ct.iloc[np.argsort(R[:, t])[::-1][:200]].value_counts().idxmax() for t in tips}
top_tip = tips[int(np.argmax([proj[t, 1] for t in tips]))]      # topmost tip -> label ABOVE its leaf
PAD = 0.060 * np.ptp(adata.obsm['X_ori'][:, 1])                 # consistent vertical label pad

fig, ax = plt.subplots(figsize=C.FIGSIZE)
# grey base cells behind the spine — samples-panel marker size (smaller tier), so the
# faint background doesn't compete with the spine. scf.pl.trajectory's own `size` scales
# via scanpy and doesn't match ax.scatter, so we draw the cells and let scf draw the spine.
xy = adata.obsm['X_ori']
ax.scatter(xy[:, 0], xy[:, 1], s=C.SAMPLES_POINT_SIZE, linewidths=0, color='lightgrey',
           alpha=.5, rasterized=False, zorder=0)
scf.pl.trajectory(adata, basis='ori', color_seg='t', cmap_seg='cividis',
                  alpha=0, frameon=False, show=False, ax=ax, rasterized=False)  # spine only (cells hidden)
ax.set_title('')
C.frame(ax, xy)   # identical framing to every other panel (aspect='auto', 5x5 box)
for t in tips:
    x, y = proj[t]
    dy, va = (PAD, 'bottom') if t == top_tip else (-PAD, 'top')
    ax.text(x, y + dy, tip_lab[t], size=C.LABEL_SIZE, weight='bold', ha='center', va=va,
            path_effects=[withStroke(linewidth=2, foreground='white')], zorder=1000)
fig.savefig(os.path.join(C.FIG, "manifold.pdf"), bbox_inches='tight', dpi=300)
plt.close(fig)
print(f"wrote {C.FIG}/manifold.pdf")
