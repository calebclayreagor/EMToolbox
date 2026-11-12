# `deposit/`: data deposit

Processed and derived objects underlying the analyses in the EMToolbox repository
(https://github.com/calebclayreagor/EMToolbox), published as a single archive alongside the
code.

**200 data files · 118.6 GB** (57.1 GB zipped)

## Use

Download `deposit.zip` into a clone of EMToolbox and extract it at the repository root
(`EMToolbox/`):

```bash
unzip -o deposit.zip && rm deposit.zip
```

## Contents

| directory | files | contents | produced by |
|---|---|---|---|
| `data/cancer/vertebrate/CCCA/claude/` | 186 · 110 GB | One `processed.h5ad` per run, under `<Category>/<Dataset>[-N]/`; malignant cells from 3CA datasets | `mesencontext/claude/<Category>/<Dataset>[-N]/01_preprocessing.ipynb` |
| `data/cancer/vertebrate/CCCA/pancan/` | 1 · 1.2 GB | `malignant.h5ad` — malignant cells pooled across 3CA datasets | `mesencontext/scripts/merge.py` |
| `data/cancer/vertebrate/CCCA/Puram2017_Head-and-Neck/` | 1 · 183 MB | `signatures.h5ad` — HNSCC malignant cells scored for the Gast, pSom and Crest e-EMT signatures | `mesencontext/Puram2017_Head-and-Neck/03_signatures.ipynb` |
| `data/cancer/invertebrate/` | 3 · 607 MB | `signatures.h5ad` for `drosophila/`, `holigactis/`, `marenaria/` | `invertebrate/drosophila/03_signatures.ipynb`; `invertebrate/{holigactis,marenaria}/notebooks/02_signatures.ipynb` |
| `data/development/processed/` | 3 · 1.8 GB | QC'd, integrated developmental datasets (`GSE162534`, `GSE229103`, `rRNAModifications`) | `development/<dataset>/preprocessing.ipynb` |
| `data/development/trajectories/` | 3 · 1.1 GB | `scFates` trajectories, one per dataset in `data/development/processed/` | `development/<dataset>/trajectory.ipynb` |
| `data/development/modeling/` | 1 · 3.7 GB | `mesencoder.h5ad` — merged developmental reference carrying the MesenCoder latent embedding in `obsm['X_mesencoder']` | `mesencoder/prediction.py` |
| `data/ref/CELLxGENE/` | 1 · 82 MB | `070526.csv` — mean and scaled expression per tissue × cell type × gene, for 238 genes in normal human data | CELLxGENE Discover, downloaded 2026-07-05 |
| `mesencoder/checkpoints/` | 1 · 387 KB | `epoch=09.ckpt` — trained MesenCoder weights, the checkpoint used to produce `mesencoder.h5ad` | `mesencoder/training.py` |

`.h5ad` `X` holds log1p of per-cell-normalised expression, not raw counts; the loader and its
normalisation rules are described in Supplementary Methods §4. Dataset scope and per-disease
counts are in Supplementary Table 6, and the per-run analysis log — including the run index
that forms the `-N` directory suffix — is Supplementary Table 7.

## Scope

Every data asset in EMToolbox is either included here or derived from what is, with one
exception: the neuroblastoma data under `data/cancer/vertebrate/NB/` derives from material
that has not been publicly deposited and is available on request. Source data under
`data/unzip/` is not redistributed; see `data/unzip/README.md` for each dataset's origin and
acquisition date.
