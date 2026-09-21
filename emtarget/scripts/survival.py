import numpy as np
import anndata as ad
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from typing import Tuple

# survival analysis wrapper function
def fit_survival(adata: ad.AnnData,
                 stratify_by: str,
                 cancer_type: str,
                 survival_type: str,
                 q_low: float = .33,
                 q_high: float = .66,
                 n_tests: int | None = None,
                 title: str | None = None,
                 ylabel: str | None = None,
                 **kwargs
                 ) -> Tuple[plt.Axes, float] | None:

    # select cancer type
    col = 'cancer type abbreviation'
    msk = (adata.obs[col] == cancer_type)
    adata = adata[msk].copy()
    df = adata.obs.copy()

    # deduplicate patients
    survival_type_time = survival_type + '.time'
    agg_dict = {survival_type      : 'first',
                survival_type_time : 'first',
                stratify_by        : 'mean'}
    cols = list(agg_dict.keys())
    df[cols] = df[cols].astype(float)
    df = df.groupby('_PATIENT').agg(agg_dict).dropna(subset = cols)
    df[survival_type_time] /= 365.

    if not df.empty:
        # stratify patients
        X = df[stratify_by].copy()
        df_low = df.loc[X < X.quantile(q_low)]
        df_high = df.loc[X > X.quantile(q_high)]

        if not df_low.empty and not df_high.empty:
            # plot survival
            _, ax = plt.subplots(1, 1, **kwargs)
            kmf = KaplanMeierFitter()
            for label, _df_ in (('Low', df_low), ('High', df_high)):
                kmf.fit(_df_[survival_type_time], _df_[survival_type], label = label)
                ax = kmf.plot_survival_function(ax = ax)

            # significance
            res = logrank_test(df_low[survival_type_time],
                               df_high[survival_type_time],
                               df_low[survival_type],
                               df_high[survival_type])
            pval = res.p_value
            if n_tests is not None:
                pval = min(pval * n_tests, 1.)

            # axes ticks/labels
            yticks = np.arange(0, 1.1, .2)
            yticklabels = (yticks * 100).astype(int)
            ax.set_yticks(yticks, yticklabels)
            ax.set_ylim(yticks[0] - .03, yticks[-1] + .03)
            if ylabel is None: ylabel = survival_type
            ax.set_ylabel(f'{ylabel} (%)')
            ax.set_xlabel('Years')

            # legend/title/pval
            leg = ax.legend(loc = 'lower left', frameon = False)
            leg.set_title(stratify_by)
            if title is None: title = cancer_type
            ax.set_title(title)
            ax.text(.975, .95, fr'$p =$ {pval:.2g}', transform = ax.transAxes,
                    bbox = {'boxstyle' : 'round', 'fc' : 'w', 'ec' : 'gray'},
                    ha = 'right', va = 'top')
            return ax, pval