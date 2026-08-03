# CCCA Meta-Atlas Run Ledger

Running scorecard — one row per analyzed dataset, reflecting its **last attempt**. Rows are added as
datasets are run and finalized (verdicts entered by the expert). Per-run provenance (cell counts,
params, subtypes, gate mechanics) lives in `analysis_log.csv`, joined on `JoinKey`.

| Analysis Order | Title | Category | Disease | JoinKey | Set | Run start | Run end | Science | Deliverables | Expert interaction | Manifold geometry | Gast μ | pSom μ | Crest μ | Gate 1 | Gate 2 | Gate 3 | Hub r | Attempts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Puram et al. 2017 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Puram2017_Head-and-Neck | train | — | — | Success | Success | Teacher | Branching | −0.103 | −0.018 | +0.297 | GO | GO | GO | −0.47 | 1 |
| 2 | Kürten et al. 2021 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Kürten2021_Head-and-Neck | eval | 2026-07-27 15:08 | 2026-07-27 22:10 | Success | Success | Tutor | Linear-pSom/Crest | +0.019 | +0.045 | −0.003 | GO | GO | — | — | 1 |
| 3 | Chen et al. 2020 | Head and Neck | Nasopharyngeal Carcinoma | Data_Chen2020_Head-and-Neck | test | 2026-07-29 13:19 | 2026-07-29 14:47 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.015 | +0.002 | −0.007 | GO | GO | — | — | 7 |
| 4 | Bischoff et al. 2021 | Lung | Lung Adenocarcinoma | Data_Bischoff2021_Lung | test | 2026-07-29 22:24 | 2026-07-29 23:47 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.037 | +0.057 | −0.032 | GO | GO | — | — | 3 |
| 5 | Sun et al. 2021 | Liver/Biliary | Hepatocellular Carcinoma | Data_Sun2021_Liver-Biliary | test | 2026-07-30 00:05 | 2026-07-30 01:23 | Success | Failure | Reviewer | Linear-pSom/Crest | −0.012 | +0.059 | −0.032 | GO | GO | — | — | 1 |
| 6 | Bi et al. 2021 ¹ | Kidney | Renal Cell Carcinoma | Data_Bi2021_Kidney | test | 2026-07-30 05:04 | 2026-07-30 05:48 | Success | Failure | Judge | Linear-pSom/Crest | −0.012 | +0.030 | −0.029 | GO | GO | — | — | 1 |
| 7 | Jansky et al. 2021 ² | Neuroendocrine | Neuroblastoma | Data_Jansky2021_Neuroendocrine | test | 2026-07-30 13:07 | 2026-07-30 15:08 | Success | Failure | Judge | Linear-pSom/Crest | +0.004 | +0.017 | −0.013 | GO | GO | — | — | 1 |
| 8 | Tirosh et al. 2016 ³ | Skin | Melanoma | Data_Tirosh2016_Skin | test | 2026-07-30 15:40 | 2026-07-30 17:04 | Failure | Failure | Judge | — | −0.507 | −0.068 | +0.149 | — | — | — | — | 1 |
| 9 | Peng et al. 2019 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Peng2019_Pancreas | test | 2026-07-30 17:06 | 2026-07-30 18:33 | Failure | Failure | Judge | — | −0.047 | +0.097 | −0.055 | — | — | — | — | 1 |
| 10 | Chen et al. 2021 | Prostate | Prostate Cancer | Data_Chen2021_Prostate | test | 2026-07-30 18:48 | 2026-07-30 19:37 | Failure | Failure | Judge | — | +0.004 | +0.036 | −0.069 | — | — | — | — | 1 |
| 11 | Lee et al. 2020 ⁴ | Colorectal | Colorectal Carcinoma | Data_Lee2020_Colorectal | test | 2026-07-30 20:15 | 2026-07-30 21:51 | Success | Success | Judge | Linear-pSom/Crest | −0.025 | +0.091 | −0.021 | GO | GO | — | — | 1 |
| 12 | Wang et al. 2019 | Brain | Glioblastoma | Data_Wang2019_Brain | test | 2026-07-30 21:57 | 2026-07-31 00:26 | Failure | Failure | Judge | — | −0.002 | +0.008 | −0.007 | — | — | — | — | 1 |
| 13 | Wu et al. 2021 ‡ | Breast | Breast Cancer | Data_Wu2021_Breast | test | 2026-07-31 00:32 | 2026-07-31 03:03 | Success | Failure | Judge | Linear-pSom/Crest | −0.025 | +0.029 | −0.034 | GO | GO | — | — | 1 |
| 14 | Zhang et al. 2022 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Zhang2022_Ovarian | test | 2026-07-31 03:15 | 2026-07-31 13:56 | Success | Failure | Judge | Linear-pSom/Crest | −0.006 | +0.051 | −0.012 | GO | GO | — | — | 1 |
| 15 | Zhou et al. 2020 † | Sarcoma | Osteosarcoma | Data_Zhou2020_Sarcoma | test | 2026-07-31 14:00 | 2026-07-31 16:14 | Success | Success | Judge | Linear-pSom/Crest | −0.039 | +0.083 | −0.046 | GO | GO | — | — | 1 |
| 16 | Kim et al. 2020 | Lung | Lung Adenocarcinoma | Data_Kim2020_Lung | test | 2026-07-31 16:35 | 2026-07-31 17:32 | Failure | Success | Judge | — | −0.040 | +0.056 | −0.027 | — | — | — | — | 1 |
| 17 | Steele et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Steele2020_Pancreas | test | 2026-07-31 17:35 | 2026-07-31 18:33 | Success | Success | Judge | Linear-pSom/Crest | −0.042 | +0.077 | −0.047 | GO | GO | — | — | 1 |
| 18 | Song et al. 2022 | Prostate | Prostate Cancer | Data_Song2022_Prostate | test | 2026-07-31 18:37 | 2026-07-31 19:43 | Success | Failure | Judge | Linear-pSom/Crest | −0.013 | +0.025 | −0.022 | GO | GO | — | — | 1 |
| 19 | Ji et al. 2020 | Skin | Skin Squamous Cell Carcinoma | Data_Ji2020_Skin | test | 2026-07-31 20:16 | 2026-07-31 22:01 | Success | Failure | Judge | Linear-pSom/Crest | −0.032 | +0.042 | +0.023 | GO | GO | — | — | 1 |
| 20 | Lin et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Lin2020_Pancreas | test | 2026-08-01 15:13 | 2026-08-01 16:27 | Success | Failure | Judge | Linear-pSom/Crest | −0.008 | +0.046 | −0.006 | GO | GO | — | — | 1 |
| 21 | Qian et al. 2020 | Lung | Lung Cancer | Data_Qian2020_Lung | test | 2026-08-01 17:17 | 2026-08-01 18:10 | Success | Success | Judge | Linear-pSom/Crest | −0.027 | +0.091 | −0.037 | GO | GO | — | — | 1 |
| 22 | Obradovic et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Obradovic2021_Kidney | test | 2026-08-01 18:14 | 2026-08-02 00:18 | Failure | Success | Judge | — | +0.024 | +0.099 | −0.075 | — | — | — | — | 1 |
| 23 | Venteicher et al. 2017 | Brain | IDH-Mutant Astrocytoma | Data_Venteicher2017_Brain | test | 2026-08-02 00:23 | 2026-08-02 01:06 | Success | Success | Judge | Linear-pSom/Crest | −0.068 | +0.211 | −0.150 | GO | GO | — | — | 1 |
| 24 | Olbrecht et al. 2021 | Ovarian | High-Grade Serous Tubo-Ovarian Cancer | Data_Olbrecht2021_Ovarian | test | 2026-08-02 01:14 | 2026-08-02 02:06 | Failure | Failure | Judge | — | +0.029 | +0.077 | −0.020 | — | — | — | — | 1 |
| 25 | Geistlinger et al. 2020 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Geistlinger2020_Ovarian | test | 2026-08-02 02:29 | 2026-08-02 03:12 | Failure | Failure | Judge | — | +0.170 | +0.432 | −0.345 | — | — | — | — | 1 |
| 26 | Laughney et al. 2020 | Lung | Lung Cancer | Data_Laughney2020_Lung | test | 2026-08-02 03:27 | 2026-08-02 15:58 | Success | Success | Judge | Linear-pSom/Crest | −0.032 | +0.063 | −0.029 | GO | GO | — | — | 1 |
| 27 | Zhang et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Zhang2021_Kidney | test | 2026-08-02 16:07 | 2026-08-02 16:55 | Failure | Success | Judge | — | −0.034 | +0.085 | −0.060 | — | — | — | — | 1 |
| 28 | Zilionis et al. 2019 | Lung | Non-Small Cell Lung Cancer | Data_Zilionis2019_Lung | test | 2026-08-02 17:00 | 2026-08-02 20:12 | Failure | Failure | Judge | — | −0.009 | +0.039 | −0.022 | — | — | — | — | 1 |
| 29 | Choudhury et al. 2022 | Brain | Meningioma | Data_Choudhury2022_Brain | test | 2026-08-02 18:21 | 2026-08-02 21:46 | Success | Failure | Judge | — | — | — | — | NO-GO | — | — | — | 1 |
| 30 | Dong et al. 2020 | Prostate | Prostate Cancer | Data_Dong2020_Prostate | test | 2026-08-02 22:10 | 2026-08-02 22:57 | Failure | Success | Judge | — | +0.035 | +0.100 | −0.041 | — | — | — | — | 1 |
| 31 | Jerby-Arnon et al. 2018 ⁵ | Skin | Melanoma | Data_Jerby-Arnon2018_Skin | test | 2026-08-02 23:05 | 2026-08-03 00:08 | Success | Success | Judge | Linear-pSom/Crest | −0.492 | −0.139 | +0.201 | GO | GO | — | — | 1 |

**Legend.**
- **Analysis Order** — the sequence in which each dataset's verdict was reviewed and logged.
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
- **† Zhou et al. 2020** — both this run and Zhang 2022 struggled to keep orientation consistent across
  UMAPs, so the expert made it a binding criterion (`04_test.md`), which this run then met.

**Prompt Evolution.** The autonomous **Judge** runs shared one initiating prompt that
set only the regime — scientific instruction stayed in the spec files. Its substantive edits are
numbered below; each carries a superscript on the table row where it first appears. Operational
guardrails (do-not-interrupt, no new packages/environments) are omitted.

1. **Baseline regime** — named dataset; no-feedback mandate; post-hoc independent-auditor contract.
   The seed paragraph, carried verbatim thereafter.
2. **Agent-chosen dataset** — dataset choice delegated to the agent; deliverables first named as the
   recurring weak spot.
3. **Learn from the log** — reuse deliverable templates from prior *successful* runs, especially `summary.pdf`.
4. **Science + deliverables** — the flagged weak spot widened from deliverables to include science;
   this became the canonical template, unchanged through run 30.
5. **Content steer** — the sole nudge on *what* to analyze: pick a dataset with low pSom signature.
