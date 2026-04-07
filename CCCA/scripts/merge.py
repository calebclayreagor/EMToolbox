#%%
import os
import pandas as pd
import anndata as ad
from load import load_CCCA_adata

pth = os.path.join('..', '..', 'data')
pth_in = os.path.join(pth, 'unzip', 'CCCA')
pth_feat = os.path.join(pth, 'features', 'biomart')
pth_out = os.path.join(pth, 'cancer', 'CCCA')

# datasets summary (CCCA)
summary_df = pd.read_csv(os.path.join(pth, 'CCCA_summary.csv'), sep = '\t')
title = summary_df.Title.str.replace(' et al. ', '')
cat = summary_df.Category.str.replace(r'[ /]', '-', regex = True)
summary_df['Name'] = 'Data_' + title + '_' + cat

# dataset features (+ others)
g = pd.read_csv(os.path.join(pth_feat, 'union.csv')).hsapiens
g = pd.concat((g, pd.Series(['TWIST2', 'ZEB1', 'ZEB2'])))
g = g.sort_values().reset_index(drop = True)

# preprocessing
def preprocess(adata: ad.AnnData) -> ad.AnnData:
    if 'cell_type' not in adata.obs.columns:
        adata.obs['cell_type'] = 'Malignant'
    if 'celltype' in adata.obs.columns:
        adata.obs['celltype_orig'] = adata.obs.celltype.copy()
    adata.obs['celltype'] = adata.obs.cell_type.copy()

    # keep dset features
    adata = adata[:, adata.var_names.isin(g)].copy()
    return adata

# prepare datasets
adata_dict = dict()
for ix in summary_df.index:
    name_ix = summary_df.loc[ix].Name
    dirname = os.path.join(pth_in, name_ix)
    if os.path.exists(dirname):
        for dirpth, subdir, _ in os.walk(dirname):
            if len(subdir) == 0:
                adata = load_CCCA_adata(dirpth)
                adata = preprocess(adata)
                for col in summary_df.columns:
                    adata.obs[col] = summary_df.loc[ix, col]
                adata_dict[dirpth] = adata
    else:
        print(f'WARNING: The directory {dirname} does not exist!')

# merge datasets
adata = ad.concat(adata_dict,
                  join = 'outer',
                  merge = 'same',
                  label = 'source')
adata.obs_names_make_unique()
adata.obs = adata.obs.astype(str)

# save malignant cells
adata = adata[adata.obs.celltype == 'Malignant'].copy()
adata.write(os.path.join(pth_out, 'malignant.h5ad'))

#%%
