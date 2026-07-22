#%%
import os
import pandas as pd

tissue_blacklist = [
    'embryo',
    'yolk sac',
    'placenta']

celltype_blacklist = [
    'aggregated',
    'cell',
    'cell in vitro',
    'malignant cell',
    'neoplastic cell',
    'abnormal cell',
    'primordial germ cell',
    'male germ cell',
    'spermatogonium',
    'spermatocyte',
    'spermatid',
    'oocyte',
    'fetal cardiomyocyte',
    'fetal pre-type II pneumocyte',
    'hepatoblast',
    'embryonic blood vessel endothelial progenitor cell',
    'pluripotent stem cell',
    'neuroepithelial stem cell',
    'neural stem cell',
    'epithelial fate stem cell',
    'cord blood hematopoietic stem cell',
    'neural crest cell',
    'premigratory neural crest cell',
    'migratory enteric neural crest cell',
    'neurectodermal cell',
    'neuroplacodal cell',
    'radial glial cell',
    'forebrain radial glial cell',
    'glioblast',
    'glioblast (sensu Vertebrata)',
    'forebrain neuroblast',
    'neuroblast (sensu Vertebrata)',
    'neuroblast (sensu Nematoda and Protostomia)',
    'Cajal-Retzius cell',
    'cerebellar granule cell precursor',
    'mesodermal cell',
    'mesenchymal lymphangioblast',
    'vascular lymphangioblast',
    'precursor cell',
    'neural cell',
    'neuronal receptor cell',
    'stem cell',
    'somatic stem cell',
    'progenitor cell',
    'hematopoietic precursor cell',
    'muscle precursor cell',
    'Schwann cell precursor',
    'differentiation-committed oligodendrocyte precursor',
    'oligodendrocyte precursor cell',
    'neural progenitor cell',
    'retinal progenitor cell',
    'glial cell',
    'blood cell',
    'CL:4047053',
    'hematopoietic stem cell',
    'hematopoietic cell',
    'mesenchymal stem cell',
    'skeletal muscle satellite cell']

# load CZ CELLxGENE gene expression (dset features)
pth = os.path.join('..', '..', 'data', 'ref', 'CELLxGENE')
df = pd.read_csv(os.path.join(pth, '070526.csv'), skiprows = 9)

# filter embryonic/fetal tissues+cell types
msk_tissue = ~df['Tissue'].isin(tissue_blacklist)
msk_celltype = ~df['Cell Type'].isin(celltype_blacklist)
msk_ncell = (df['Cell Count'] > 50)
df = df.loc[msk_tissue & msk_celltype & msk_ncell].copy()

# save results
df = df.pivot(index = ('Tissue', 'Cell Type'),
              columns = 'Gene Symbol',
              values = 'Expression').fillna(0.)
df.to_csv(os.path.join(pth, 'pbulk.csv'))

#%%
