"""Modules-stage manuscript output for Ji2020_Skin (Gate-3 statistic panel).

Reuses the ACCEPTED run-9 05_modules recipe VERBATIM: Gast OR pSom (union) genes
on the hub cells, per-gene Pearson vs each module score, mutual correlation of the
two gene-wise vectors = the Gate-3 cross-repression r. Display only, no h5ad (§6).

This step is a SCATTER (per-gene Gast-corr vs pSom-corr), not a UMAP, so the
embedding conventions (Basal-top orientation, (5,5), s=15) do not apply; it keeps
run-9's own scatter conventions: (3.5,3.5), s=25, alpha=0.6, Gast/pSom/Both colour
dict, adjustText gene labels, Gate-3 r annotation. Axis labels/title are kept (a
scatter is unreadable without them).

Reads : DATA/signatures.h5ad
Writes: FIG/modules.pdf
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd, scanpy as sc, matplotlib.pyplot as plt
from scipy.stats import pearsonr
from adjustText import adjust_text
import _common as C

FEAT = "/home/caleb/EMToolbox/data/features/biomart"
adata = sc.read_h5ad(os.path.join(C.DATA, "signatures.h5ad"))
print("loaded signatures subset:", adata.shape)

c_dict = {'Gast': plt.cm.tab20c(12), 'pSom': plt.cm.tab20c(8), 'Both': 'darkgrey'}

# ---- run-9 05_modules, VERBATIM ----
get_feat = lambda p: pd.read_csv(p).hsapiens
gast = get_feat(os.path.join(FEAT, 'GSE162534.csv'))
psom = get_feat(os.path.join(FEAT, 'GSE229103.csv'))
g = pd.merge(gast, psom, 'outer').hsapiens.drop_duplicates()
g = g.loc[g.isin(adata.var_names)]
print('union genes on manifold:', g.size)

msk = adata.obs['hub'].values
adata_plt = adata[msk, g.tolist()].copy()
print('hub cells:', int(msk.sum()))

X = pd.DataFrame(np.asarray(adata_plt.X.todense()) if hasattr(adata_plt.X, 'todense')
                 else np.asarray(adata_plt.X), index=adata_plt.obs_names, columns=g)
X = X.loc[:, (X.nunique(axis=0) > 1)].copy()
R = pd.DataFrame(index=X.columns)
mod1 = adata_plt.obs.GSE162534.values[:, None]   # Gast
mod2 = adata_plt.obs.GSE229103.values[:, None]   # pSom
R['Gast'] = pearsonr(X, mod1, axis=0).statistic
R['pSom'] = pearsonr(X, mod2, axis=0).statistic
rank = R.abs().sum(axis=1).rank(ascending=False)
R = R.loc[rank.sort_values().index].copy()

ix = R.index
msk_dict = {'Gast': ix.isin(gast) & ~ix.isin(psom),
            'pSom': ~ix.isin(gast) & ix.isin(psom),
            'Both': ix.isin(gast) & ix.isin(psom)}
for mod, m in msk_dict.items():
    R.loc[m, 'Module'] = mod
    print(mod, int(m.sum()))
R['Module'] = pd.Categorical(R.Module, list(reversed(list(msk_dict.keys()))), ordered=True)

# Gate-3 statistic: module mutual correlation (excluding Both genes)
rval = np.corrcoef(*R.loc[~msk_dict['Both'], ['Gast', 'pSom']].values.T)[0, 1].round(2)
print('Gate-3 r =', rval)

# ---- modules.pdf: scatter (run-9 scatter conventions) ----
fig, ax = plt.subplots(figsize=(3.5, 3.5))
for mod, sdf in R.groupby('Module', observed=True):
    sdf.plot(kind='scatter', x='Gast', y='pSom', color=c_dict[mod], label=mod,
             s=25, alpha=.6, linewidth=0, ax=ax)
ax.axvline(0, color='k', lw=1, ls='--', zorder=0)
ax.axhline(0, color='k', lw=1, ls='--', zorder=0)
xlim = abs(np.asarray(ax.get_xlim())).max(); ylim = abs(np.asarray(ax.get_ylim())).max()
ax.set_xlim(-xlim, xlim); ax.set_ylim(-ylim, ylim)
# Gast (x) ticks fixed at 0.1 interval capped at +/-0.2 (data reaches ~0.28 but no
# 0.3 tick); pSom (y) at 0.1 interval. Limits unchanged, so all points still shown.
from matplotlib.ticker import MultipleLocator
ax.set_xticks([-.2, -.1, 0, .1, .2])
ax.yaxis.set_major_locator(MultipleLocator(0.1))

n, texts = 30, []   # top-N genes by combined |corr| labelled (run-9 used 20)
for i in R.head(n).index:
    xi = R.loc[i].Gast; yi = R.loc[i].pSom
    texts.append(ax.text(xi, yi, i, fontsize=5.75, fontstyle='italic'))
adjust_text(texts=texts)

ax.legend(title='Module', loc='lower left', title_fontsize=7.5, handlelength=1,
          handletextpad=.5, borderaxespad=.65, fontsize=7.5, reverse=True)
ax.text(.99, .01, r'$r=$' + f'{rval}', transform=ax.transAxes,
        fontsize=10, color='tab:red', ha='right', va='bottom')
ax.set_title('Basal Population')
ax.set_xlabel(r'Gast Correlation ($r$)'); ax.set_ylabel(r'pSom Correlation ($r$)')
fig.savefig(os.path.join(C.FIG, "modules.pdf"), bbox_inches='tight', dpi=300)
plt.close(fig)
print(f"wrote {C.FIG}/modules.pdf")