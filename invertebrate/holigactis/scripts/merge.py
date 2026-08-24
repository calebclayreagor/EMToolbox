#%%
import os
import numpy as np
import pandas as pd
import anndata as ad

pth = os.path.join('..', '..', '..', 'data')
pth_in = os.path.join(pth, 'unzip', 'GSE56287')
pth_ref = os.path.join(pth_in, 'GPL18477')
pth_out = os.path.join(pth, 'cancer', 'invertebrate', 'holigactis')

names = [
    'GSM1358360_US84303580_253442910001_S01_GE1_107_Sep09_1_3',
    'GSM1358361_US84303580_253442910001_S01_GE1_107_Sep09_1_4',
    'GSM1358362_US84303580_253442910005_S01_GE1_107_Sep09_1_3',
    'GSM1358363_US84303580_253442910005_S01_GE1_107_Sep09_1_4']

ctrl = {0 : ['ControlType',
             'gIsSaturated',
             'gIsFeatNonUnifOL',
             'gIsFeatPopnOL'],
        1 : ['gIsWellAboveBG']}

# map: probes -> genes
fn = os.path.join(pth_ref, 'GPL18477_probes_genes.csv')
g = pd.read_csv(fn, index_col = 0).gene_id.str.upper()

# load/filter microarray intensities
X = dict()
for name in names:
    fn = os.path.join(pth_in, name + '.txt')
    X_name = pd.read_csv(fn, skiprows = 9, sep = '\t')
    for flag, cols in ctrl.items():
        msk = (X_name[cols] == flag).all(axis = 1)
        X_name = X_name.loc[msk].copy()
    X_name_grp = X_name.groupby('ProbeName')
    X[name] = X_name_grp.gProcessedSignal.mean()

# merge samples & filter probes
X = pd.concat(X, axis = 1).dropna()
X = X.loc[X.index.isin(g.index)]
X.index = X.index.map(g.to_dict())
X = X.groupby('ProbeName').mean() # gene_id
X_raw = X.values.copy()

# scale & normalize
X = X.apply(np.log2)
p75 = X.quantile(.75, axis = 0)
X = X - p75 + p75.mean()

# save output
layers = {'gProcessedSignal' : X_raw.T}
adata = ad.AnnData(X = X.T, layers = layers)
adata.write(os.path.join(pth_out, 'tumor.h5ad'))

#%%
