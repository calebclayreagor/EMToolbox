#%%
import os, glob
import numpy as np
import pandas as pd
from pybiomart import Server

pth = os.path.join('..', '..', 'data', 'features')
pth_out = os.path.join(pth, 'biomart')
server = Server(host = 'http://www.ensembl.org')
mart = server.marts['ENSEMBL_MART_ENSEMBL']

# dataset features
feat_fn = sorted(glob.glob(os.path.join(pth, '*.txt')))
get_src = lambda fn: os.path.split(fn)[1].replace('.txt', '')
feat_dict = {get_src(fn) : fn for fn in feat_fn}

# homologs (1-to-1 deterministic map)
attr = ['external_gene_name', 'hsapiens_homolog_associated_gene_name']
df = mart.datasets['mmusculus_gene_ensembl'].query(attributes = attr)
df.columns = ['mmusculus', 'hsapiens']
df = (df.dropna().sort_values(['mmusculus', 'hsapiens'])
      .drop_duplicates(subset = ['mmusculus'], keep = 'first')
      .drop_duplicates(subset = ['hsapiens'], keep = 'first')
      .sort_values('mmusculus'))

# feature homologs
for src, fn in feat_dict.items():
    features = np.loadtxt(fn, dtype = str)
    msk = df.mmusculus.isin(features)
    feat_dict[src] = df.loc[msk].copy()
    fn_out = os.path.join(pth_out, f'{src}.csv')
    feat_dict[src].to_csv(fn_out, index = False)

#%%
