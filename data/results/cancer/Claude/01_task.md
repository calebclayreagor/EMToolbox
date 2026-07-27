# CCCA Meta-Atlas Cell-State Analysis — Task Save Point

**Status:** design phase. Settled: biology, gates, scope, environment, deliverables, annotation,
log schema. No datasets analyzed yet.

## 0. Overview

Re-run a six-step single-cell analysis — hand-built on Puram2017 (head & neck) — across every
in-scope CCCA / 3CA dataset, one per subdirectory.

**Question:** do malignant cells recapitulate embryonic-development programs? Score three modules
(Gast, pSom, Crest) on malignant cells, fit a cell-state trajectory, and use three go/no-go gates
to decide whether the expected pattern — a Gast/pSom hub diverging into two arms with
cross-repression — reproduces.

**Role:** this is **not** a fixed pipeline; nearly every parameter is dataset-dependent. Act as the
**analyst** — make the same *kinds* of judgment calls made for Puram2017, grounded in the data and
biology. The Puram2017 notebooks are the **protocol** (§3), not values to copy.

**Scope:** `CCCA_summary.csv` (§4) is authoritative. The on-disk folder set is a superset — folders
not in the summary are out of scope; do not analyze them.

## 1. Biology

Hypothesis: malignant cells recapitulate **embryonic-development gene programs**; EMT transitions
mirror developmental bifurcations. Modules (read the `hsapiens` column, drop NaN/dupes):

- **Gast** — gastrulation (`GSE162534.csv`)
- **pSom** — posterior somitogenesis (`GSE229103.csv`)
- **Crest** — neural crest (`rRNAModifications.csv` — filename historical; contents are neural crest)
- **union** — control pool for `score_genes` (`union.csv`)

**Expected pattern (from Puram2017):** a **hub** where Gast+pSom co-express **diverges** into a
pSom-leaning arm and a Gast-leaning arm. **Crest** is high at the arm tips (terminal readout),
enriched on the pSom arm. **Gast↔pSom is the cross-repression axis** — opposite directions out of
the hub; mutual exclusivity is the bifurcation signature. Crest is a terminal readout, **not** on
that axis. Hub module correlation in Puram ≈ **−0.49**. Module→arm assignment is **data-driven** —
read it off the scores, not off subtype names.

**Not every dataset bifurcates.** In the **non-branching case**, Gast and pSom **fully overlap**
with Crest as an inverse/terminal gradient — the programs are present but not resolved into two
competing arms. This is a real outcome, not a failure: it **passes Gate 2**, has no bifurcation for
Gate 3, and is reported as such — distinct from a no-go where the pattern is absent.

## 2. The three GO/NO-GO gates (the crux)

Gates are **scientific** (is the phenomenon present?), not parameter-quality checks. Parameter
tuning is the agent's means to answer them honestly — never something the researcher gates on;
judged visually.

- **Gate 1 (01→02):** after Harmony on `sample` + DR, is the malignant structure both **mixed**
  (sample-integrated) and **continuous** (connected gradient)? NO-GO if it clusters by sample or
  breaks into disconnected islands — don't force a trajectory.
- **Gate 2 (03→04):** does the embryonic module pattern appear — a Gast/pSom hub diverging into two
  arms, Crest high at tips (ideally pSom arm)? The **non-branching case** (Gast/pSom fully overlap,
  Crest an inverse gradient; §1) still **passes** but has no bifurcation for Gate 3. **Flag** (pass
  anyway) if Crest enriches the **Gast** arm — an inversion.
- **Gate 3 (04→05, branching only):** do tree node-clusters show **mutual Gast↔pSom negative
  correlation** (competitive cross-repression)? Crest not tested. No branching / no anti-correlation
  → NO-GO on step 05.

**The EMT-TF expression step is unconditional** — always produced as the final notebook, outside the
gate chain (numbered 06 only when all gates pass; renumbered after an earlier no-go — see §6).

**Linchpin: identify the HUB** (Puram's "Mixed") — the Gast/pSom-overlap convergence population that
04–05 run on and Gate 3 tests. Identify by **role** (module-convergence zone at the trajectory
branch/root), not by name, and confirm it's the topological convergence point.

## 3. The 6-step protocol (source of truth: Puram2017 notebooks)

`.../CCCA/Puram2017_Head-and-Neck/{01..06}_*.ipynb` (READ-ONLY). Parameter values there are
**illustrative, not defaults to copy** — and the **in-notebook comments are illustrative of the
analytical judgment calls** the researcher made, the reasoning to emulate rather than transcribe.
I/O per step in §6.

1. **01_preprocessing** — load malignant cells → drop under-populated samples (per-dataset min-cell
   threshold) → filter genes → overdispersed selection → PCA → Harmony on `sample` → neighbors →
   UMAP → Leiden → drop detached clusters → re-cluster → annotate subtypes. **Annotation always uses
   both data-derived marker expression and the original publication's reported subtypes/markers**
   (cited in the log) — never one alone.
2. **02_manifold** — scFates PPT tree → biologically-motivated root → pseudotime → rename milestones.
3. **03_signatures** — `score_genes` for Gast/pSom/Crest with the union control pool → signature UMAPs.
4. **04_correlation** — Gast XOR pSom genes, hub cells → pseudotime-windowed module Pearson.
5. **05_modules** — Gast OR pSom genes, hub cells → per-gene module correlation → scatter, reports r.
6. **06_expression** — EMT-TF expression overlay; most informative TFs for that dataset.

Per-dataset notebooks are numbered **sequentially** — the expression step is always the *last*
notebook, so its number depends on how far the analysis ran (§6).

## 4. Data & code assets (source of truth)

- **Loader** `.../CCCA/scripts/load.py` — `load_CCCA_adata(datadir)` reads the matrix/gene/cell files
  in `datadir`, auto-detects normalization from the matrix filename (TPM/normalized pass through;
  counts normalized), always `log1p`, sets `celltype` (default 'Malignant'). **Point it at a
  bottom-level (leaf) dataset directory**, as `merge.py` does — it does not walk nested subdirs.
  `merge.py` also defines the folder-naming convention mapping summary rows → on-disk folders.
- **Scope list** `.../CCCA/Claude/CCCA_summary.csv` — TAB-sep; `Title, Category, Disease, Technology,
  Samples, Cells`; one row per in-scope dataset. **Authoritative.**
- **Input data** `.../data/unzip/CCCA/` — one folder per dataset (superset of scope). Layout varies
  (some datasets nest by technology; expression is a mix of counts and TPM). Resolve each dataset to
  its leaf matrix directory before loading; don't hardcode format counts.
- **Gene sets** `.../data/features/biomart/` — the four CSVs above.
- **Environment** — the existing `scFates` conda env (§5).

## 5. Directory access & environment

Grant **narrowly, one at a time**; grants apply to **new kernels only** — restart after each.

| Directory | Access | Role |
|---|---|---|
| `.../data/unzip/CCCA/` | **ro** | input dataset folders |
| `.../CCCA/scripts/` | **ro** | `load.py`, `merge.py` |
| `.../CCCA/Puram2017_Head-and-Neck/` | **ro** | reference notebooks 01–06 |
| `.../data/features/biomart/` | **ro** | gene sets |
| `.../CCCA/Claude/` | **rw** | notebooks, summary-CSV copy, cumulative log |
| `.../data/cancer/vertebrate/CCCA/Claude/` | **rw** | output h5ads |
| `.../figures/cancer/vertebrate/CCCA/Claude/` | **rw** | output figures (+ `colorbars/`) |

Not granted: `MesenCoder` root, `data` root — hence the summary CSV lives in the rw `Claude/`.

**Environment:** use the existing **`scFates`** conda env — **no recreation needed**. (Stack: python
3.11, r-base 4.3 + r-mgcv, rpy2, scanpy/scFates/harmonypy/leidenalg/anndata; scFates PPT → rpy2 →
r-mgcv, and notebook 01 sets `R_HOME` to the conda prefix.)

## 6. Deliverables & outputs

**Layout:** one dataset per subdir, partitioned by `Category`, replicated across three roots
(notebooks, h5ads, figures + `colorbars/`): `.../Claude/<Category>/<DatasetName>/NN_*.ipynb`
(`<DatasetName>` = folder name minus `Data_`). **Relative paths:** the `<Category>/` partition puts
notebooks two levels deeper than Puram — adapt the path logic; notebooks must run in place. **Keep
rw-directory outputs tidy and as brief as possible** — they live on the researcher's disk; don't
accumulate scratch or intermediate files.

| Step | Reads | h5ad | Figures |
|---|---|---|---|
| preprocessing | raw load | `processed.h5ad` | `samples.pdf` |
| manifold | `processed.h5ad` | `manifold.h5ad` | `manifold.pdf` |
| signatures | `manifold.h5ad` | `signatures.h5ad` | `{Gast,pSom,Crest}_signature.pdf` + colorbars |
| correlation | `signatures.h5ad` | — | `correlation.pdf`, `colorbars/R_colorbar.pdf` |
| modules | `signatures.h5ad` | — | `modules.pdf` |
| expression | `processed.h5ad` | — | `expression.pdf` |

**Stop at a no-go — do not create downstream notebooks** (not stubbed, not emptied). Notebook
numbers are **sequential**, so the unconditional expression step is always the *last* notebook,
renumbered to follow whatever preceded it:

- Gate 1 NO-GO → preprocessing (01) + expression (**02**)
- Gate 2 NO-GO → 01–03 + expression (**04**)
- Gate 3 NO-GO → 01–04 + expression (**05**)
- all gates pass → full 01–06 (expression = 06)

**Every dataset also produces, regardless of how far it ran:**

- **`summary.pdf`** — a **punchy** one-page executive summary (same register as this doc): dataset in
  one line (cancer type, platform, malignant-cell count); key parameter choices + rationale
  (min-cell threshold, root node, geometry); **the gate outcomes with reasoning for each go/no-go**;
  hub identity and r where applicable; a one-line verdict on whether the pattern reproduces. **Embeds
  the step figures** (the produced `.pdf`s) so the decisions are visible at a glance.
  - Update (7/24/26): format precisely to match the Puram2017 calibration-step output
- **one row in `.../CCCA/Claude/analysis_log.csv`** (TAB-sep) — the six `CCCA_summary.csv` columns
  verbatim (joins 1:1 to the master), then provenance (join key, cell counts through filtering,
  expression type, key embedding/trajectory params, clusters removed, subtypes + annotation source,
  geometry) and the gate readout (`gate1/2/3`, Crest-arm flag, hub r, EMT-TFs shown, status, notes).
