# CCCA Meta-Atlas Run Ledger

Running scorecard — one row per analyzed dataset, reflecting its **last attempt**. Rows are added as
datasets are run and finalized (verdicts entered by the expert). Per-run provenance (cell counts,
params, subtypes, gate mechanics) lives in `analysis_log.csv`, joined on `JoinKey`.

| Title | Category | Disease | JoinKey | Set | Run start | Run end | Science | Deliverables | Expert interaction | Manifold geometry | Gast μ | pSom μ | Crest μ | Gate 1 | Gate 2 | Gate 3 | Hub r | Attempts |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Puram et al. 2017 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Puram2017_Head-and-Neck | train | — | — | Success | Success | Teacher | Branching | −0.103 | −0.018 | +0.297 | GO | GO | GO | −0.47 | 1 |
| Kürten et al. 2021 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Kürten2021_Head-and-Neck | eval | 2026-07-27 15:08 | 2026-07-27 22:10 | Success | Success | Tutor | Linear-pSom/Crest | +0.019 | +0.045 | −0.003 | GO | GO | — | — | 1 |
| Chen et al. 2020 | Head and Neck | Nasopharyngeal Carcinoma | Data_Chen2020_Head-and-Neck | test | 2026-07-29 13:19 | 2026-07-29 14:47 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.015 | +0.002 | −0.007 | GO | GO | — | — | 7 |
| Bischoff et al. 2021 | Lung | Lung Adenocarcinoma | Data_Bischoff2021_Lung | test | 2026-07-29 22:24 | 2026-07-29 23:47 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.037 | +0.057 | −0.032 | GO | GO | — | — | 3 |
| Sun et al. 2021 | Liver/Biliary | Hepatocellular Carcinoma | Data_Sun2021_Liver-Biliary | test | 2026-07-30 00:05 | 2026-07-30 01:23 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.012 | +0.059 | −0.032 | GO | GO | — | — | 1 |
| Bi et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Bi2021_Kidney | test | 2026-07-30 05:04 | 2026-07-30 05:48 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.012 | +0.030 | −0.029 | GO | GO | — | — | 1 |
| Jansky et al. 2021 | Neuroendocrine | Neuroblastoma | Data_Jansky2021_Neuroendocrine | test | 2026-07-30 13:07 | 2026-07-30 15:08 | Success | Failure | Reviewer | Linear-pSom/Crest | +0.004 | +0.017 | −0.013 | GO | GO | — | — | 1 |
| Tirosh et al. 2016 | Skin | Melanoma | Data_Tirosh2016_Skin | test | 2026-07-30 15:40 | 2026-07-30 17:04 | Failure | Failure | Reviewer | — | −0.507 | −0.068 | +0.149 | — | — | — | — | 1 |
| Peng et al. 2019 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Peng2019_Pancreas | test | 2026-07-30 17:06 | 2026-07-30 18:33 | Failure | Failure | Reviewer | — | −0.047 | +0.097 | −0.055 | — | — | — | — | 1 |
| Chen et al. 2021 | Prostate | Prostate Cancer | Data_Chen2021_Prostate | test | 2026-07-30 18:48 | 2026-07-30 19:37 | Failure | Failure | Reviewer | — | +0.004 | +0.036 | −0.069 | — | — | — | — | 1 |
| Lee et al. 2020 | Colorectal | Colorectal Carcinoma | Data_Lee2020_Colorectal | test | 2026-07-30 20:15 | 2026-07-30 21:51 | Success | Success | Reviewer | Linear-pSom/Crest | −0.025 | +0.091 | −0.021 | GO | GO | — | — | 1 |
| Wang et al. 2019 | Brain | Glioblastoma | Data_Wang2019_Brain | test | 2026-07-30 21:57 | 2026-07-31 00:26 | Failure | Failure | Reviewer | — | −0.002 | +0.008 | −0.007 | — | — | — | — | 1 |
| Wu et al. 2021 ‡ | Breast | Breast Cancer | Data_Wu2021_Breast | test | 2026-07-31 00:32 | 2026-07-31 03:03 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.025 | +0.029 | −0.034 | GO | GO | — | — | 1 |

**Legend.**
- **Set** — train (calibration, HNSCC) · eval (supervised, HNSCC) · test (autonomous, other).
- **Science / Deliverables** — Success / Failure. Science = correct gate call reached by correct
  reasoning. Deliverables = §6 outputs match the binding reference (set, location, style, `summary.pdf` layout).
- **Expert interaction** — Teacher (calibrated the protocol) · Tutor (steered step-by-step) ·
  Reviewer (autonomous run, audited after the fact) · Judge (outcome adjudicated, no steering).
- **Manifold geometry** — Branching (Gast/pSom hub → pSom arm + Gast arm, cross-repression; Crest a
  terminal readout at the arm tips) · Linear (collapsed
  bifurcation, single axis), split by global module strength: **Linear-pSom/Crest** = pSom and/or Crest
  globally stronger than Gast, **Linear-Gast** = Gast globally stronger than pSom/Crest.
- **Gast μ · pSom μ · Crest μ** — mean `score_genes` module score across all malignant cells (the metric
  that defines the Linear split).
- **Gate 1 · Gate 2 · Gate 3** — GO / NO-GO. Gate 3 is branching-only.
- **Hub r** — Gast↔pSom cross-repression Pearson; branching only.
- **Attempts** — number of runs to reach this finalized row.

- **‡ Wu et al. 2021** — the agent identified an ambiguity in the non-branching definition, which did
  not say whether Gast/pSom cross-repression is disqualifying. The expert then
  updated the definition (`01_task.md` §1–2) to include the cross-repression case — organized
  cross-repression with a terminal Crest gradient counts as non-branching. Agent-identified,
  expert-ratified.
