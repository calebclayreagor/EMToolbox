#%%
import os, glob
import numpy as np
import pandas as pd
from pybiomart import Server

pth = os.path.join('..', '..', 'data', 'features')
pth_out = os.path.join(pth, 'biomart')
server = Server(host = 'http://www.ensembl.org', use_cache = False)
mart = server.marts['ENSEMBL_MART_ENSEMBL']
attr = {
    'external_gene_name'                         : 'mmusculus',
    'hsapiens_homolog_associated_gene_name'      : 'hsapiens',
    'dmelanogaster_homolog_associated_gene_name' : 'dmelanogaster'}

# dataset features
feat_fn = sorted(glob.glob(os.path.join(pth, '*.txt')))
get_src = lambda fn: os.path.split(fn)[1].replace('.txt', '')
feat_dict = {get_src(fn) : fn for fn in feat_fn}

# homologs map (many-to-many)
df = (mart.datasets['mmusculus_gene_ensembl']
      .query(attributes = list(attr.keys())))
df.columns = list(attr.values())
df = df.dropna().sort_values(list(attr.values()))

# feature homologs
for src, fn in feat_dict.items():
    features = np.loadtxt(fn, dtype = str)
    msk = df.mmusculus.isin(features)
    feat_dict[src] = df.loc[msk].copy()
    fn_out = os.path.join(pth_out, f'{src}.csv')
    feat_dict[src].to_csv(fn_out, index = False)

# features union
df_out = (pd.concat(feat_dict.values(), ignore_index = True)
          .drop_duplicates().sort_values(list(attr.values())))
df_out.to_csv(os.path.join(pth_out, 'union.csv'), index = False)

#%%
