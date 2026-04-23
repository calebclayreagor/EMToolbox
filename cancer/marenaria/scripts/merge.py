#%%
import os
import pandas as pd
import anndata as ad
import scanpy as sc

pth = os.path.join('..', '..', '..', 'data')
pth_in = os.path.join(pth, 'unzip', 'MarBTN')
pth_out = os.path.join(pth, 'cancer', 'marenaria')

names = [
    '01-FFM-28E5',
    '02-FFM-28E6',
    '03-FFM-28E7',
    # '19-FFM-15G11',
    # '20-FFM-16G1',
    '04-FFM-28E5-ASW',
    '05-FFM-28E6-ASW',
    '06-FFM-28E7-ASW']

# load bulk RNA-seq counts
X = dict()
for name in names:
    fn = f'{name}_ReadsPerGene.out.tab'
    X[name] = pd.read_csv(
        os.path.join(pth_in, fn),
        index_col = 0, skiprows = 4,
        sep = '\t').iloc[:, 0]

# merge samples
X = pd.concat(X, axis = 1).T
adata = ad.AnnData(X = X)
adata.layers['counts'] = adata.X.copy()

# normalize & scale
sc.pp.normalize_total(adata)
sc.pp.log1p(adata)

# save output
adata.write(os.path.join(pth_out, 'MarBTN.h5ad'))

#%%
