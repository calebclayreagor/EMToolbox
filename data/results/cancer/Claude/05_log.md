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
