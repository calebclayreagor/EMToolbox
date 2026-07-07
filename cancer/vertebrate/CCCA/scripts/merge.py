#%%
import os
import pandas as pd
import anndata as ad
from load import load_CCCA_adata

pth = os.path.join('..', '..', '..', '..', 'data')
pth_in = os.path.join(pth, 'unzip', 'CCCA')
pth_feat = os.path.join(pth, 'features', 'biomart')
pth_out = os.path.join(pth, 'cancer', 'vertebrate', 'CCCA')

blacklist = [
    'nan',
    'Adenoma_specific_cell',
    'Serrated_specific_cells',
    'AML_progenitor_cell',
    'Proliferating_Cell',
    'Osteoblast_proli',
    'Undifferentiated',
    'TZBTB16']

# datasets summary (CCCA)
summary_df = pd.read_csv(os.path.join(pth, 'CCCA_summary.csv'), sep = '\t')
title = summary_df.Title.str.replace(' et al. ', '')
cat = summary_df.Category.str.replace(r'[ /]', '-', regex = True)
summary_df['Name'] = 'Data_' + title + '_' + cat

# dataset features (+ others)
g = pd.read_csv(os.path.join(pth_feat, 'union.csv')).hsapiens.drop_duplicates()
g = pd.concat((g, pd.Series(['SNAI1', 'TWIST2', 'FOXC1', 'ZEB1', 'ZEB2', 'PRRX2'])))
g = g.sort_values().reset_index(drop = True)

# preprocessing: keep dset features
def preprocess(adata: ad.AnnData) -> ad.AnnData:
    return adata[:, adata.var_names.isin(g)].copy()

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

# save malignant, normal cells
adata_cancer = adata[adata.obs.celltype == 'Malignant'].copy()
adata_normal = adata[adata.obs.celltype != 'Malignant'].copy()
msk_blacklist = adata_normal.obs.celltype.isin(blacklist)
adata_normal = adata_normal[~msk_blacklist].copy()
adata_cancer.write(os.path.join(pth_out, 'malignant.h5ad'))
adata_normal.write(os.path.join(pth_out, 'normal.h5ad'))

#%%
