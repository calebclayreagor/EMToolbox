#%%
import os
import numpy as np
import pandas as pd
from itertools import combinations

pth = os.path.join('..', '..', 'data')
pth_in = os.path.join(pth, 'ref', 'CELLxGENE')
pth_out = os.path.join(pth, 'results', 'tx', 'discovery', 'safety')

# load CZ CELLxGENE pseudobulk -> cell type max expression
fn = os.path.join(pth_in, 'pbulk.csv')
df = pd.read_csv(fn, index_col = [0, 1])
df_max = df.max(axis = 0).rename('Expression').to_frame()
df_idxmax = pd.DataFrame(
    data = df.idxmax(axis = 0).to_frame()[0].tolist(),
    index = df_max.index, columns = df.index.names)
df_single = df_max.join(df_idxmax)

# gene pair max expression
g = list(combinations(df_single.index, 2))
df_pair = df_single.reindex(np.array(g).ravel())
expr_arr = df_pair.Expression.values.reshape(-1, 2)
ix = np.arange(len(g)) * 2 + expr_arr.argmax(axis = 1)
df_pair = df_pair.iloc[ix].reset_index(names = 'Gene')
df_pair.index = pd.MultiIndex.from_tuples(g)

# save results
df_single.to_csv(os.path.join(pth_out, 'single.csv'))
df_pair.to_csv(os.path.join(pth_out, 'pair.csv'))

#%%
