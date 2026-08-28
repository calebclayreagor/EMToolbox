"""Signatures-stage manuscript outputs for Ji2020_Skin.

Reuses the ACCEPTED run-9 03_signatures scoring VERBATIM: sc.tl.score_genes for
each embryonic module (Gast/pSom/Crest) against the shared `union` control pool
(ctrl_as_ref=False, gene_pool=union, random_state=1234). Re-scored on the
manuscript subset so the scores are self-consistent with the modified cell set;
no method or parameter changed. RAW per-cell scores are shown in the deliverable
(smoothing is analysis-only and misleads as a deliverable — 04_test.md).

Reads : DATA/manifold.h5ad   (subset + Option-C tree/pseudotime)
Writes: DATA/signatures.h5ad (subset + module scores; §6 schema)
        FIG/{Gast,pSom,Crest}_signature.pdf   (plasma, locked display config)
        FIG/colorbars/{Gast,pSom,Crest}_colorbar.pdf  (external colorbars)
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import glob
import numpy as np, pandas as pd, scanpy as sc, matplotlib.pyplot as plt
import _common as C

FEAT = "/home/caleb/EMToolbox/data/features/biomart"
CB   = os.path.join(C.FIG, "colorbars")
os.makedirs(C.DATA, exist_ok=True); os.makedirs(CB, exist_ok=True)

adata = sc.read_h5ad(os.path.join(C.DATA, "manifold.h5ad"))
print("loaded manifold subset:", adata.shape)

# ---- run-9 03_signatures scoring, VERBATIM ----
feat_fn = sorted(glob.glob(os.path.join(FEAT, '*.csv')))
get_src  = lambda fn: os.path.split(fn)[1].replace('.csv', '')
get_feat = lambda fn: pd.read_csv(fn).hsapiens.drop_duplicates()
feat_dict = {get_src(fn): get_feat(fn) for fn in feat_fn}

msk_ref = feat_dict['union'].isin(adata.var_names)
g_ref = feat_dict['union'].loc[msk_ref].copy()
for src, df_src in feat_dict.items():
    if src != 'union':
        g = df_src.loc[df_src.isin(adata.var_names)].copy()
        sc.tl.score_genes(adata, gene_list=g, score_name=src,
                          ctrl_as_ref=False, gene_pool=g_ref, random_state=1234)
        print('scored', src, 'genes recovered:', g.size, '/ ref pool', g_ref.size)

adata.write(os.path.join(C.DATA, "signatures.h5ad"))
print(f"wrote {C.DATA}/signatures.h5ad  shape={adata.shape}")

# ---- signature panels: plasma, RAW scores, locked display config ----
# module-key -> (deliverable filename stem, colorbar label)
# per-panel colorbar ticks with display range clamped to the outer ticks, so the
# bar begins/ends exactly on a labelled tick (no unlabelled slivers). vmin/vmax is
# display-only (clamps a few outlier cells at the colormap extremes; scores unchanged).
panels = [('GSE162534', 'Gast', 'Gast', [-0.2, -0.1, 0, 0.1, 0.2], -0.2, 0.2),
          ('GSE229103', 'pSom', 'pSom', [-0.2, -0.1, 0, 0.1, 0.2, 0.3], -0.2, 0.3),
          ('rRNAModifications', 'Crest', 'Crest', [-0.2, -0.1, 0, 0.1, 0.2], -0.2, 0.2)]
xy = C.oriented_umap(adata)          # frozen orientation carried forward, Basal-top
mask = np.ones(adata.n_obs, bool)
for key, stem, lbl, ticks, vmin, vmax in panels:
    v = adata.obs[key].values
    o = C.zsort(v)                                 # highest score on top (scanpy sort_order)
    fig, ax = plt.subplots(figsize=C.FIGSIZE)
    sca = ax.scatter(xy[o, 0], xy[o, 1], c=v[o], cmap='plasma', alpha=.5, vmin=vmin, vmax=vmax,
                     s=C.POINT_SIZE, linewidths=0, rasterized=False)
    C.celltype_labels(ax, xy, adata, mask)
    C.frame(ax, xy)
    fig.savefig(os.path.join(C.FIG, f"{stem}_signature.pdf"), bbox_inches='tight', dpi=300)
    plt.close(fig)
    # external colorbar (house style: narrow standalone axes, alpha=1 solids)
    fcb = plt.figure(figsize=(.66, 1)); cax = fcb.add_axes([.35, .05, .3, .9])
    cb = plt.colorbar(sca, cax=cax); cb.ax.tick_params(which='both', size=0)
    cb.set_label(f'{lbl}\nSignature')
    cb.set_ticks(ticks, labels=ticks)   # range == outer ticks, so every tick lands
    cb.solids.set_alpha(1)
    fcb.savefig(os.path.join(CB, f"{stem}_colorbar.pdf"), bbox_inches='tight')
    plt.close(fcb)
    print(f"wrote {stem}_signature.pdf + colorbar  (score range {v.min():.3f}..{v.max():.3f})")
print("done")