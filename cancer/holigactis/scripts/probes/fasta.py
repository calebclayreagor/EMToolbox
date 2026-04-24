#%%
import os, csv
import pandas as pd

pth = os.path.join('..', '..', '..', '..', 'data', 'unzip', 'GSE56287')
df = (pd.read_csv(os.path.join(pth, 'GPL18477_annotation.txt'),
                  skiprows = 9, index_col = 3, sep = '\t')
                  .SEQUENCE.dropna().drop_duplicates())
df.index = '>' + df.index; df = df.index + '\n' + df
df.to_csv(os.path.join(pth, 'GPL18477_probes.fasta'),
          index = False, header = False,
          quoting = csv.QUOTE_NONE, escapechar = ' ')

#%%
