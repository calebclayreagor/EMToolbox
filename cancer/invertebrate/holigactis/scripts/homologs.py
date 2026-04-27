#%%
import os, glob
import pandas as pd

pth = os.path.join('..', '..', '..', '..', 'data')
pth_feat = os.path.join(pth, 'features')
pth_bm = os.path.join(pth_feat, 'biomart')
pth_fb = os.path.join(pth, 'ref', 'flybase')
pth_ortho = os.path.join(pth, 'results', 'orthofinder')
pth_out = os.path.join(pth_feat, 'orthofinder', 'holigactis')
names = {'Drosophila_melanogaster' : 'dmelanogaster',
         'Hydra_oligactis'         : 'holigactis'}

# drosophila genes: flybase ID -> gene symbol (map)
fn = 'fbgn_fbtr_fbpp_expanded_fb_2026_01.tsv'
g_dict = (pd.read_csv(os.path.join(pth_fb, fn),
                      skiprows = 4, skipfooter = 1,
                      engine = 'python', sep = '\t')
          .set_index('gene_ID').gene_symbol.to_dict())

# dataset features
feat_fn = sorted(glob.glob(os.path.join(pth_bm, '*.csv')))
get_src = lambda fn: os.path.split(fn)[1].replace('.csv', '')
feat_dict = {get_src(fn) : fn for fn in feat_fn}

# homologs map (many-to-many)
fn = 'Drosophila_melanogaster__v__Hydra_oligactis.tsv'
df = pd.read_csv(os.path.join(pth_ortho, fn), sep = '\t')
for name, colname in names.items():
    df[colname] = df[name].str.split(', ')
    df = df.explode(colname)
    if colname == 'dmelanogaster':
        df[colname] = df[colname].map(g_dict)
df = (df[list(names.values())].dropna()
      .sort_values(list(names.values())))

# feature homologs
for src, fn in feat_dict.items():
    features = pd.read_csv(fn).dmelanogaster
    msk = df.dmelanogaster.isin(features)
    feat_dict[src] = df.loc[msk].copy()
    fn_out = os.path.join(pth_out, f'{src}.csv')
    feat_dict[src].to_csv(fn_out, index = False)

#%%
