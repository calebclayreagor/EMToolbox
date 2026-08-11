# CCCA Meta-Atlas Run Ledger

Running scorecard — one row per analyzed dataset, reflecting its **last attempt**. Rows are added as
datasets are run and finalized (verdicts entered by the expert). Per-run provenance (cell counts,
params, subtypes, gate mechanics) lives in `analysis_log.csv`, joined on `JoinKey`.

| Title | Category | Disease | JoinKey | Run start | Run end | Expert interaction | Manifold geometry | Gate 1 | Gate 2 | Gate 3 | Hub r | Attempts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Puram et al. 2017 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Puram2017_Head-and-Neck | — | — | Teacher | Branching | GO | GO | GO | −0.47 | 1 |
| Kürten et al. 2021 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Kürten2021_Head-and-Neck | 2026-07-27 15:08 | 2026-07-27 22:10 | Tutor | Linear | GO | GO | — | — | 1 |
| Chen et al. 2020 | Head and Neck | Nasopharyngeal Carcinoma | Data_Chen2020_Head-and-Neck | 2026-07-29 13:19 | 2026-07-29 14:47 | Reviewer | Linear | GO | GO | — | — | 7 |
| Bischoff et al. 2021 | Lung | Lung Adenocarcinoma | Data_Bischoff2021_Lung | 2026-07-29 22:24 | 2026-07-29 23:47 | Reviewer | Linear | GO | GO | — | — | 3 |
| Sun et al. 2021 | Liver/Biliary | Hepatocellular Carcinoma | Data_Sun2021_Liver-Biliary | 2026-07-30 00:05 | 2026-07-30 01:23 | Reviewer | Linear | GO | GO | — | — | 1 |
| Bi et al. 2021 ¹ | Kidney | Renal Cell Carcinoma | Data_Bi2021_Kidney | 2026-07-30 05:04 | 2026-07-30 05:48 | Judge | Linear | GO | GO | — | — | 1 |
| Jansky et al. 2021 ² | Neuroendocrine | Neuroblastoma | Data_Jansky2021_Neuroendocrine | 2026-07-30 13:07 | 2026-07-30 15:08 | Judge | Linear | GO | GO | — | — | 1 |
| Tirosh et al. 2016 ³ | Skin | Melanoma | Data_Tirosh2016_Skin | 2026-08-05 22:04 | 2026-08-05 22:49 | Judge | Linear | GO | GO | — | — | 2 |
| Peng et al. 2019 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Peng2019_Pancreas | 2026-08-06 21:22 | 2026-08-06 22:52 | Judge | Linear | GO | GO | — | — | 3 |
| Chen et al. 2021 | Prostate | Prostate Cancer | Data_Chen2021_Prostate | 2026-08-05 20:26 | 2026-08-05 21:15 | Judge | Linear | GO | GO | — | — | 2 |
| Lee et al. 2020 ⁴ | Colorectal | Colorectal Carcinoma | Data_Lee2020_Colorectal | 2026-07-30 20:15 | 2026-07-30 21:51 | Judge | Linear | GO | GO | — | — | 1 |
| Wang et al. 2019 | Brain | Glioblastoma | Data_Wang2019_Brain | 2026-08-08 15:20 | 2026-08-08 17:28 | Judge | — | GO | NO-GO | — | — | 8 |
| Wu et al. 2021 ‡ | Breast | Breast Cancer | Data_Wu2021_Breast | 2026-07-31 00:32 | 2026-07-31 03:03 | Judge | Linear | GO | GO | — | — | 1 |
| Zhang et al. 2022 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Zhang2022_Ovarian | 2026-07-31 03:15 | 2026-07-31 13:56 | Judge | Linear | GO | GO | — | — | 1 |
| Zhou et al. 2020 † | Sarcoma | Osteosarcoma | Data_Zhou2020_Sarcoma | 2026-07-31 14:00 | 2026-07-31 16:14 | Judge | Linear | GO | GO | — | — | 1 |
| Kim et al. 2020 | Lung | Lung Adenocarcinoma | Data_Kim2020_Lung | 2026-08-06 21:22 | 2026-08-06 21:56 | Judge | Linear | GO | GO | — | — | 3 |
| Steele et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Steele2020_Pancreas | 2026-07-31 17:35 | 2026-07-31 18:33 | Judge | Linear | GO | GO | — | — | 1 |
| Song et al. 2022 | Prostate | Prostate Cancer | Data_Song2022_Prostate | 2026-07-31 18:37 | 2026-07-31 19:43 | Judge | Linear | GO | GO | — | — | 1 |
| Ji et al. 2020 | Skin | Skin Squamous Cell Carcinoma | Data_Ji2020_Skin | 2026-07-31 20:16 | 2026-07-31 22:01 | Judge | Branching | GO | GO | GO | −0.41 | 10 |
| Lin et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Lin2020_Pancreas | 2026-08-01 15:13 | 2026-08-01 16:27 | Judge | Linear | GO | GO | — | — | 1 |
| Qian et al. 2020 | Lung | Lung Cancer | Data_Qian2020_Lung | 2026-08-01 17:17 | 2026-08-01 18:10 | Judge | Linear | GO | GO | — | — | 1 |
| Obradovic et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Obradovic2021_Kidney | 2026-08-08 15:20 | 2026-08-08 17:51 | Judge | Linear | GO | GO | — | — | 1 |
| Venteicher et al. 2017 | Brain | IDH-Mutant Astrocytoma | Data_Venteicher2017_Brain | 2026-08-02 00:23 | 2026-08-02 01:06 | Judge | Linear | GO | GO | — | — | 1 |
| Olbrecht et al. 2021 | Ovarian | High-Grade Serous Tubo-Ovarian Cancer | Data_Olbrecht2021_Ovarian | 2026-08-08 15:20 | 2026-08-08 19:48 | Judge | Linear | GO | GO | — | — | 2 |
| Geistlinger et al. 2020 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Geistlinger2020_Ovarian | 2026-08-05 22:04 | 2026-08-05 22:52 | Judge | Linear | GO | GO | — | — | 2 |
| Laughney et al. 2020 | Lung | Lung Cancer | Data_Laughney2020_Lung | 2026-08-02 03:27 | 2026-08-02 15:58 | Judge | Linear | GO | GO | — | — | 1 |
| Zhang et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Zhang2021_Kidney | 2026-08-07 05:53 | 2026-08-07 07:05 | Judge | Linear | GO | GO | — | — | 4 |
| Zilionis et al. 2019 | Lung | Non-Small Cell Lung Cancer | Data_Zilionis2019_Lung | 2026-08-07 23:43 | 2026-08-08 03:09 | Judge | — | GO | NO-GO | — | — | 6 |
| Choudhury et al. 2022 | Brain | Meningioma | Data_Choudhury2022_Brain | 2026-08-02 18:21 | 2026-08-02 21:46 | Judge | — | NO-GO | — | — | — | 1 |
| Dong et al. 2020 | Prostate | Prostate Cancer | Data_Dong2020_Prostate | 2026-08-07 23:43 | 2026-08-08 02:44 | Judge | Linear | GO | GO | — | — | 6 |
| Jerby-Arnon et al. 2018 ⁵ | Skin | Melanoma | Data_Jerby-Arnon2018_Skin | 2026-08-02 23:05 | 2026-08-03 00:08 | Judge | Linear | GO | GO | — | — | 1 |
| Biermann et al. 2022 | Skin | Metastatic Melanoma | Data_Biermann2022_Skin | 2026-08-03 00:52 | 2026-08-03 03:12 | Judge | Linear | GO | GO | — | — | 1 |
| Maynard et al. 2020 | Lung | Lung Cancer | Data_Maynard2020_Lung | 2026-08-03 03:33 | 2026-08-03 12:29 | Judge | Linear | GO | GO | — | — | 1 |
| Xing et al. 2021 | Lung | Lung Cancer | Data_Xing2021_Lung | 2026-08-03 12:39 | 2026-08-03 13:43 | Judge | Linear | GO | GO | — | — | 1 |
| Chan et al. 2021 ⁶ | Lung | Lung Cancer | Data_Chan2021_Lung | 2026-08-07 05:53 | 2026-08-07 07:45 | Judge | Linear | GO | GO | — | — | 4 |
| Galen et al. 2019 | Hematologic | Acute Myeloid Leukemia | Data_Galen2019_Hematologic | 2026-08-03 14:21 | 2026-08-03 15:22 | Judge | Linear | GO | GO | — | — | 1 |
| Gao et al. 2021 | Breast | Breast Cancer | Data_Gao2021_Breast | 2026-08-07 05:53 | 2026-08-07 06:44 | Judge | — | NO-GO | — | — | — | 4 |
| Hwang et al. 2022 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Hwang2022_Pancreas | 2026-08-07 05:53 | 2026-08-07 10:09 | Judge | — | GO | NO-GO | — | — | 4 |
| Izar et al. 2020 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Izar2020_Ovarian | 2026-08-03 14:21 | 2026-08-03 15:03 | Judge | Linear | GO | GO | — | — | 1 |
| Jerby-Arnon et al. 2021 | Sarcoma | Synovial Sarcoma | Data_Jerby-Arnon2021_Sarcoma | 2026-08-05 15:19 | 2026-08-05 16:13 | Judge | Linear | GO | GO | — | — | 2 |
| Kildisiute et al. 2021 | Neuroendocrine | Neuroblastoma | Data_Kildisiute2021_Neuroendocrine | 2026-08-05 15:19 | 2026-08-05 15:52 | Judge | — | NO-GO | — | — | — | 2 |
| Krishna et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Krishna2021_Kidney | 2026-08-03 14:21 | 2026-08-03 15:03 | Judge | Linear | GO | GO | — | — | 1 |
| Neftel et al. 2019 | Brain | Glioblastoma | Data_Neftel2019_Brain | 2026-08-03 14:21 | 2026-08-03 15:25 | Judge | Linear | GO | GO | — | — | 1 |
| Pelka et al. 2021 | Colorectal | Colorectal Cancer | Data_Pelka2021_Colorectal | 2026-08-03 14:21 | 2026-08-03 18:12 | Judge | Linear | GO | GO | — | — | 1 |
| Olalekan et al. 2021 ⁷ | Ovarian | Ovarian Cancer | Data_Olalekan2021_Ovarian | 2026-08-03 19:57 | 2026-08-03 20:21 | Judge | Linear | GO | GO | — | — | 1 |
| Young et al. 2018 | Kidney | Kidney Cancer | Data_Young2018_Kidney | 2026-08-05 15:19 | 2026-08-05 15:52 | Judge | — | NO-GO | — | — | — | 2 |
| He et al. 2021 | Prostate | Metastatic Prostate Cancer | Data_He2021_Prostate | 2026-08-03 19:57 | 2026-08-04 13:22 | Judge | Linear | GO | GO | — | — | 1 |
| Qian et al. 2020 | Breast | Breast Cancer | Data_Qian2020_Breast | 2026-08-06 21:22 | 2026-08-06 22:36 | Judge | — | NO-GO | — | — | — | 3 |
| Paulson et al. 2020 | Skin | Merkel Cell Carcinoma | Data_Paulson2020_Skin | 2026-08-03 19:57 | 2026-08-03 20:31 | Judge | Linear | GO | GO | — | — | 1 |
| Yuan et al. 2018 | Brain | High-Grade Glioma | Data_Yuan2018_Brain | 2026-08-03 19:57 | 2026-08-03 20:29 | Judge | Linear | GO | GO | — | — | 1 |
| Gojo et al. 2020 | Brain | Pediatric Ependymoma | Data_Gojo2020_Brain | 2026-08-03 19:57 | 2026-08-04 13:22 | Judge | Linear | GO | GO | — | — | 1 |
| Raghavan et al. 2021 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Raghavan2021_Pancreas | 2026-08-07 18:53 | 2026-08-07 19:41 | Judge | Linear | GO | GO | — | — | 5 |
| Cohen et al. 2021 | Hematologic | Multiple Myeloma | Data_Cohen2021_Hematologic | 2026-08-06 21:22 | 2026-08-06 23:17 | Judge | Linear | GO | GO | — | — | 3 |
| Dong et al. 2020 | Neuroendocrine | Neuroblastoma | Data_Dong2020_Neuroendocrine | 2026-08-03 19:57 | 2026-08-03 21:10 | Judge | Linear | GO | GO | — | — | 1 |
| Couturier et al. 2020⁸ | Brain | Glioblastoma | Data_Couturier2020_Brain | 2026-08-04 14:02 | 2026-08-04 15:51 | Judge | Linear | GO | GO | — | — | 1 |
| Filbin et al. 2018 | Brain | Pediatric H3-K27M Mutant Glioma | Data_Filbin2018_Brain | 2026-08-09 00:54 | 2026-08-09 02:09 | Judge | Branching | GO | GO | GO | −0.34 | 10 |
| Gaiti et al. 2019 | Hematologic | Chronic Lymphocytic Leukemia | Data_Gaiti2019_Hematologic | 2026-08-04 14:02 | 2026-08-04 15:29 | Judge | Linear | GO | GO | — | — | 1 |
| Liu et al. 2021 | Hematologic | Multiple Myeloma | Data_Liu2021_Hematologic | 2026-08-05 15:19 | 2026-08-05 16:20 | Judge | — | NO-GO | — | — | — | 2 |
| Nath et al. 2021 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Nath2021_Ovarian | 2026-08-04 14:02 | 2026-08-04 15:36 | Judge | Linear | GO | GO | — | — | 1 |
| Pal et al. 2021 | Breast | Breast Cancer | Data_Pal2021_Breast | 2026-08-06 21:22 | 2026-08-07 04:24 | Judge | Linear | GO | GO | — | — | 3 |
| Zhang et al. 2019 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Zhang2019_Ovarian | 2026-08-04 14:02 | 2026-08-04 15:07 | Judge | Linear | GO | GO | — | — | 1 |
| Li et al. 2017 | Colorectal | Colorectal Carcinoma | Data_Li2017_Colorectal | 2026-08-04 15:54 | 2026-08-04 16:20 | Judge | Linear | GO | GO | — | — | 1 |
| Tirosh et al. 2016 | Brain | IDH-Mutant Oligodendroglioma | Data_Tirosh2016_Brain | 2026-08-04 15:54 | 2026-08-04 16:20 | Judge | Linear | GO | GO | — | — | 1 |
| Bassez et al. 2021 | Breast | Breast Cancer | Data_Bassez2021_Breast | 2026-08-07 23:43 | 2026-08-08 03:19 | Judge | Linear | GO | GO | — | — | 6 |
| Caron et al. 2020 | Hematologic | Acute Lymphoblastic Leukemia | Data_Caron2020_Hematologic | 2026-08-07 06:57 | 2026-08-07 10:40 | Judge | Linear | GO | GO | — | — | 4 |
| Griffiths et al. 2021 | Breast | Breast Cancer | Data_Griffiths2021_Breast | 2026-08-07 23:43 | 2026-08-08 04:38 | Judge | — | GO | NO-GO | — | — | 6 |
| Hovestadt et al. 2019 | Brain | Medulloblastoma | Data_Hovestadt2019_Brain | 2026-08-04 16:41 | 2026-08-04 17:16 | Judge | Linear | GO | GO | — | — | 1 |
| Ledergor et al. 2018 | Hematologic | Multiple Myeloma | Data_Ledergor2018_Hematologic | 2026-08-05 16:54 | 2026-08-05 17:49 | Judge | Linear | GO | GO | — | — | 2 |
| Nam et al. 2019 | Hematologic | Myeloproliferative Neoplasms | Data_Nam2019_Hematologic | 2026-08-04 16:41 | 2026-08-04 17:36 | Judge | Linear | GO | GO | — | — | 1 |
| Qian et al. 2020 | Ovarian | Ovarian Cancer | Data_Qian2020_Ovarian | 2026-08-05 16:54 | 2026-08-05 17:28 | Judge | Linear | GO | GO | — | — | 2 |
| Rendeiro et al. 2020 | Hematologic | Chronic Lymphocytic Leukemia | Data_Rendeiro2020_Hematologic | 2026-08-07 23:43 | 2026-08-08 02:43 | Judge | — | NO-GO | — | — | — | 6 |
| Roider et al. 2020 | Hematologic | B-Cell Lymphoma | Data_Roider2020_Hematologic | 2026-08-04 16:41 | 2026-08-04 17:21 | Judge | Linear | GO | GO | — | — | 1 |
| Wu et al. 2020 | Hematologic | Acute Myeloid Leukemia | Data_Wu2020_Hematologic | 2026-08-07 07:47 | 2026-08-07 10:40 | Judge | — | GO | NO-GO | — | — | 4 |
| Chung et al. 2017 | Breast | Breast Cancer | Data_Chung2017_Breast | 2026-08-04 22:59 | 2026-08-05 01:42 | Judge | Linear | GO | GO | — | — | 1 |
| Darmanis et al. 2017 | Brain | Glioblastoma | Data_Darmanis2017_Brain | 2026-08-05 15:47 | 2026-08-05 15:56 | Judge | Linear | GO | GO | — | — | 2 |
| Giustacchini et al. 2017 | Hematologic | Chronic Myeloid Leukemia | Data_Giustacchini2017_Hematologic | 2026-08-05 20:26 | 2026-08-05 20:49 | Judge | Linear | GO | GO | — | — | 2 |
| Gulati et al. 2020 | Breast | Breast Cancer | Data_Gulati2020_Breast | 2026-08-05 22:04 | 2026-08-05 22:25 | Judge | — | GO | NO-GO | — | — | 2 |
| Karaayvas et al. 2018 | Breast | Breast Cancer | Data_Karaayvas2018_Breast | 2026-08-05 15:47 | 2026-08-05 16:00 | Judge | — | GO | NO-GO | — | — | 2 |
| Kim et al. 2018 | Breast | Triple-Negative Breast Cancer | Data_Kim2018_Breast | 2026-08-04 22:23 | 2026-08-04 23:39 | Judge | Linear | GO | GO | — | — | 1 |
| Li et al. 2019 | Skin | Melanoma | Data_Li2019_Skin | 2026-08-07 09:21 | 2026-08-07 10:40 | Judge | — | NO-GO | — | — | — | 4 |
| Moncada et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Moncada2020_Pancreas | 2026-08-04 22:55 | 2026-08-05 01:42 | Judge | Linear | GO | GO | — | — | 1 |
| Shih et al. 2018 | Ovarian | Ovarian Cancer | Data_Shih2018_Ovarian | 2026-08-04 22:23 | 2026-08-04 23:15 | Judge | Linear | GO | GO | — | — | 1 |
| Song et al. 2019 | Lung | Non-Small Cell Lung Cancer | Data_Song2019_Lung | 2026-08-04 22:23 | 2026-08-04 23:04 | Judge | Linear | GO | GO | — | — | 1 |
| Steen et al. 2021 | Hematologic | Diffuse Large B-Cell Lymphoma | Data_Steen2021_Hematologic | 2026-08-04 22:23 | 2026-08-05 01:11 | Judge | Linear | GO | GO | — | — | 1 |
| Yost et al. 2019 | Skin | Skin Carcinoma | Data_Yost2019_Skin | 2026-08-04 22:23 | 2026-08-04 22:54 | Judge | Linear | GO | GO | — | — | 1 |
| Zhang et al. 2019 | Hematologic | Follicular Lymphoma | Data_Zhang2019_Hematologic | 2026-08-07 23:43 | 2026-08-08 02:19 | Judge | — | GO | NO-GO | — | — | 6 |

**Legend.**
- **Expert interaction** — Teacher (calibrated the protocol) · Tutor (steered step-by-step) ·
  Reviewer (autonomous run, audited after the fact) · Judge (outcome adjudicated, no steering).
- **Manifold geometry** — Branching (Gast/pSom hub → pSom arm + Gast arm, cross-repression; Crest a
  terminal readout at the arm tips) · Linear (collapsed bifurcation, single continuous axis).
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

**Scope corrections.** **Ireland et al. 2020 (Lung, SCLC)** — removed (row + both `analysis_log.csv`
rows + all deliverables), dropping the atlas from 87 to 86 rows. It is a cross-species composite (mouse
RPM GEM time-course + human sample), so it is not validly in scope.

**Prompt Evolution.** The autonomous **Judge** runs shared one initiating prompt that
set only the regime — scientific instruction stayed in the spec files (except the branching re-runs, item 12, which carried scientific steering in the prompt and via debrief). Its substantive edits are
numbered below; each carries a superscript on the table row where it first appears (re-run waves
overwrite existing rows, so carry none). Operational
guardrails (do-not-interrupt, no new packages/environments) are omitted.

1. **Baseline regime** — named dataset; no-feedback mandate; post-hoc independent-auditor contract.
   The seed paragraph, carried verbatim thereafter.
2. **Agent-chosen dataset** — dataset choice delegated to the agent; deliverables first named as the
   recurring weak spot.
3. **Learn from the log** — reuse deliverable templates from prior *successful* runs, especially `summary.pdf`.
4. **Science + deliverables** — the flagged weak spot widened from deliverables to include science;
   this became the canonical template for the single-dataset runs that followed.
5. **Content steer** (one run only) — the sole nudge on *what* to analyze: pick a low-pSom dataset.
   The next run reverted to item 4, unmarked.
6. **Batch delegation / scale-up** — the item-4 template plus one instruction: select 10 datasets and
   delegate the identical autonomous instructions to 10 subagents, reviewed together. First multi-dataset
   run.
7. **Delegate self-check** — item 6 plus one clause: the delegating agent may also check its subagents'
   science + deliverables accuracy. Second batch.
8. **Full scale-up** — item 7 unchanged in regime, scope widened from "10 new" to "all remaining in-scope
   datasets": the final batch, 33 subagents delegated the identical instructions and reviewed together.
9. **Science-fail re-run (`-1`)** — item-8 regime plus one directive: re-analyze every first-run science failure,
   hinting most were bad Gate 1/2 GO calls or missed branching.
10. **Science-fail re-run (`-3`)** — item-9 regime re-applied to the datasets still failing science.
   Dispatch instructions added strict attention to Gate 1 integration and Gate 2
   module geography, cycling-lobe scoping, pseudotime-curve rooting and fold-freeness, and
   deliverable/biology-visualization fidelity.
11. **Science-fail re-run (`-5`)** — item-10 regime, dispatch retargeted from pseudotime rooting/fold-freeness
   to which region the trajectory is scoped on. Several Gate 2 GOs flipped to NO-GO. This exposed a gap in
   the protocol order: `02_manifold` fits the pseudotime before Gate 2 tests the modules, so the fitted
   trajectory does not depend on the embryonic modules being present.
12. **Targeted content steer** — for the last runs of the bifurcating datasets (Filbin, Ji), the item-11 regime
   was narrowed with scientific steering toward a branching outcome (in-prompt and via debrief; see header).
