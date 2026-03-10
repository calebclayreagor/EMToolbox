#%%
import os, glob
import numpy as np
import pandas as pd
import scanpy as sc
import anndata as ad
from scipy.stats import gmean
np.random.seed(1)

pth = os.path.join('..', '..', 'data')
pth_in = os.path.join(pth, 'processed')
pth_traj = os.path.join(pth, 'trajectories')
pth_feat = os.path.join(pth, 'features', 'biomart')
pth_out = os.path.join(pth, 'modeling', 'inputs')

# load datasets, trajectories, features
adata_fn = sorted(glob.glob(os.path.join(pth_in, '*.h5ad')))
traj_fn = sorted(glob.glob(os.path.join(pth_traj, '*.h5ad')))
get_src = lambda fn: os.path.split(fn)[1].replace('.h5ad', '')
adata_dict = {get_src(fn) : sc.read_h5ad(fn) for fn in adata_fn}
traj_dict = {get_src(fn) : sc.read_h5ad(fn) for fn in traj_fn}
g = pd.read_csv(os.path.join(pth_feat, 'union.csv')).mmusculus

# train/val split
train_frac = .8
for src in adata_dict:
    adata = adata_dict[src].copy()
    traj = traj_dict[src].copy()

    # keep trajectory, features
    msk_traj = adata.obs_names.isin(traj.obs_names)
    msk_var = adata.var_names.isin(g)
    adata = adata[msk_traj, msk_var].copy()
    traj = traj[adata.obs_names].copy()
    adata.obsm['X_umap'] = traj.obsm['X_umap'].copy()
    adata.obs['t'] = traj.obs.t.copy()

    # keep celltypes
    n = adata.obs.groupby('celltype', observed = True).size()
    keep = n.loc[(n / adata.n_obs) > .01].index
    adata = adata[adata.obs.celltype.isin(keep)].copy()

    # training split (celltype stratified)
    train_ix = (adata.obs
                .groupby('celltype', observed = True)
                .sample(frac = train_frac).index)
    adata.obs['training'] = adata.obs_names.isin(train_ix)
    adata_dict[src] = adata.copy()

# merge datasets
adata = ad.concat(adata_dict,
                  join = 'outer',
                  merge = 'same',
                  label = 'source')
adata.obs_names_make_unique()
adata.obs = adata.obs.astype(str)

# training weights (celltype, source)
for col in ('celltype', 'source'):
    col_size = adata.obs.groupby(col).size()
    col_weight = 1 / adata.obs[col].map(col_size)
    adata.obs[f'weight_{col}'] = col_weight
weight = adata.obs[['weight_celltype', 'weight_source']]
weight = gmean(weight.values, axis = 1)
weight /= weight.mean()
adata.obs['weight'] = weight

# save dataset
adata.write(os.path.join(pth_out, 'development.h5ad'))

#%%
