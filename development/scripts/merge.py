#%%
import os, glob
import scanpy as sc
import anndata as ad

pth = os.path.join('..', '..', 'data', 'development')
pth_in = os.path.join(pth, 'processed')
pth_traj = os.path.join(pth, 'trajectories')
pth_out = os.path.join(pth, 'modeling')

# load datasets, trajectories
adata_fn = sorted(glob.glob(os.path.join(pth_in, '*.h5ad')))
traj_fn = sorted(glob.glob(os.path.join(pth_traj, '*.h5ad')))
get_src = lambda fn: os.path.split(fn)[1].replace('.h5ad', '')
adata_dict = {get_src(fn) : sc.read_h5ad(fn) for fn in adata_fn}
traj_dict = {get_src(fn) : sc.read_h5ad(fn) for fn in traj_fn}

# select trajectories
for src in adata_dict:
    adata = adata_dict[src].copy()
    traj = traj_dict[src].copy()
    msk = adata.obs_names.isin(traj.obs_names) 
    adata = adata[msk].copy()
    traj = traj[adata.obs_names].copy()

    # keep embedding, pseudotime
    X_traj = traj.obsm['X_umap'].copy()
    adata.obsm['X_umap_traj'] = X_traj
    adata.obs['t'] = traj.obs.t.copy()
    adata_dict[src] = adata.copy()

# merge datasets
adata = ad.concat(adata_dict,
                  join = 'outer',
                  merge = 'same',
                  label = 'source')
adata.obs_names_make_unique()
adata.obs = adata.obs.astype(str)

# save dataset
adata.write(os.path.join(pth_out, 'trajectories.h5ad'))

#%%
