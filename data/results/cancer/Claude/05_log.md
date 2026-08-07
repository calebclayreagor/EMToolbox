# CCCA Meta-Atlas Run Ledger

Running scorecard — one row per analyzed dataset, reflecting its **last attempt**. Rows are added as
datasets are run and finalized (verdicts entered by the expert). Per-run provenance (cell counts,
params, subtypes, gate mechanics) lives in `analysis_log.csv`, joined on `JoinKey`.

| Analysis Order | Title | Category | Disease | JoinKey | Set | Run start | Run end | Science | Deliverables | Expert interaction | Manifold geometry | Gast μ | pSom μ | Crest μ | Gate 1 | Gate 2 | Gate 3 | Hub r | Attempts |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Puram et al. 2017 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Puram2017_Head-and-Neck | train | — | — | Success | Success | Teacher | Branching | −0.103 | −0.018 | +0.297 | GO | GO | GO | −0.47 | 1 |
| 2 | Kürten et al. 2021 | Head and Neck | Head and Neck Squamous Cell Carcinoma | Data_Kürten2021_Head-and-Neck | eval | 2026-07-27 15:08 | 2026-07-27 22:10 | Success | Success | Tutor | Linear | +0.019 | +0.045 | −0.003 | GO | GO | — | — | 1 |
| 3 | Chen et al. 2020 | Head and Neck | Nasopharyngeal Carcinoma | Data_Chen2020_Head-and-Neck | test | 2026-07-29 13:19 | 2026-07-29 14:47 | Success | Failure | Reviewer | Linear | −0.015 | +0.002 | −0.007 | GO | GO | — | — | 7 |
| 4 | Bischoff et al. 2021 | Lung | Lung Adenocarcinoma | Data_Bischoff2021_Lung | test | 2026-07-29 22:24 | 2026-07-29 23:47 | Success | Failure | Reviewer | Linear | −0.037 | +0.057 | −0.032 | GO | GO | — | — | 3 |
| 5 | Sun et al. 2021 | Liver/Biliary | Hepatocellular Carcinoma | Data_Sun2021_Liver-Biliary | test | 2026-07-30 00:05 | 2026-07-30 01:23 | Success | Failure | Reviewer | Linear | −0.012 | +0.059 | −0.032 | GO | GO | — | — | 1 |
| 6 | Bi et al. 2021 ¹ | Kidney | Renal Cell Carcinoma | Data_Bi2021_Kidney | test | 2026-07-30 05:04 | 2026-07-30 05:48 | Success | Failure | Judge | Linear | −0.012 | +0.030 | −0.029 | GO | GO | — | — | 1 |
| 7 | Jansky et al. 2021 ² | Neuroendocrine | Neuroblastoma | Data_Jansky2021_Neuroendocrine | test | 2026-07-30 13:07 | 2026-07-30 15:08 | Success | Failure | Judge | Linear | +0.004 | +0.017 | −0.013 | GO | GO | — | — | 1 |
| 8 | Tirosh et al. 2016 ³ | Skin | Melanoma | Data_Tirosh2016_Skin | test | 2026-08-05 22:04 | 2026-08-05 22:49 | Success | Success | Judge | Linear | −0.507 | −0.068 | +0.149 | GO | GO | — | — | 2 |
| 9 | Peng et al. 2019 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Peng2019_Pancreas | test | 2026-08-05 15:19 | 2026-08-05 16:00 | Failure | Failure | Judge | — | −0.047 | +0.098 | −0.055 | — | — | — | — | 2 |
| 10 | Chen et al. 2021 | Prostate | Prostate Cancer | Data_Chen2021_Prostate | test | 2026-08-05 20:26 | 2026-08-05 21:15 | Success | Failure | Judge | Linear | +0.004 | +0.036 | −0.069 | GO | GO | — | — | 2 |
| 11 | Lee et al. 2020 ⁴ | Colorectal | Colorectal Carcinoma | Data_Lee2020_Colorectal | test | 2026-07-30 20:15 | 2026-07-30 21:51 | Success | Success | Judge | Linear | −0.025 | +0.091 | −0.021 | GO | GO | — | — | 1 |
| 12 | Wang et al. 2019 | Brain | Glioblastoma | Data_Wang2019_Brain | test | 2026-08-05 22:04 | 2026-08-05 23:02 | Failure | Failure | Judge | — | −0.003 | +0.008 | −0.007 | — | — | — | — | 2 |
| 13 | Wu et al. 2021 ‡ | Breast | Breast Cancer | Data_Wu2021_Breast | test | 2026-07-31 00:32 | 2026-07-31 03:03 | Success | Failure | Judge | Linear | −0.025 | +0.029 | −0.034 | GO | GO | — | — | 1 |
| 14 | Zhang et al. 2022 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Zhang2022_Ovarian | test | 2026-07-31 03:15 | 2026-07-31 13:56 | Success | Failure | Judge | Linear | −0.006 | +0.051 | −0.012 | GO | GO | — | — | 1 |
| 15 | Zhou et al. 2020 † | Sarcoma | Osteosarcoma | Data_Zhou2020_Sarcoma | test | 2026-07-31 14:00 | 2026-07-31 16:14 | Success | Success | Judge | Linear | −0.039 | +0.083 | −0.046 | GO | GO | — | — | 1 |
| 16 | Kim et al. 2020 | Lung | Lung Adenocarcinoma | Data_Kim2020_Lung | test | 2026-08-05 22:04 | 2026-08-05 22:41 | Failure | Success | Judge | — | −0.040 | +0.056 | −0.027 | — | — | — | — | 2 |
| 17 | Steele et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Steele2020_Pancreas | test | 2026-07-31 17:35 | 2026-07-31 18:33 | Success | Success | Judge | Linear | −0.042 | +0.077 | −0.047 | GO | GO | — | — | 1 |
| 18 | Song et al. 2022 | Prostate | Prostate Cancer | Data_Song2022_Prostate | test | 2026-07-31 18:37 | 2026-07-31 19:43 | Success | Failure | Judge | Linear | −0.013 | +0.025 | −0.022 | GO | GO | — | — | 1 |
| 19 | Ji et al. 2020 | Skin | Skin Squamous Cell Carcinoma | Data_Ji2020_Skin | test | 2026-07-31 20:16 | 2026-07-31 22:01 | Success | Failure | Judge | Linear | −0.032 | +0.042 | +0.023 | GO | GO | — | — | 1 |
| 20 | Lin et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Lin2020_Pancreas | test | 2026-08-01 15:13 | 2026-08-01 16:27 | Success | Failure | Judge | Linear | −0.008 | +0.046 | −0.006 | GO | GO | — | — | 1 |
| 21 | Qian et al. 2020 | Lung | Lung Cancer | Data_Qian2020_Lung | test | 2026-08-01 17:17 | 2026-08-01 18:10 | Success | Success | Judge | Linear | −0.027 | +0.091 | −0.037 | GO | GO | — | — | 1 |
| 22 | Obradovic et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Obradovic2021_Kidney | test | 2026-08-05 22:04 | 2026-08-05 22:38 | Failure | Failure | Judge | — | +0.024 | +0.099 | −0.075 | — | — | — | — | 2 |
| 23 | Venteicher et al. 2017 | Brain | IDH-Mutant Astrocytoma | Data_Venteicher2017_Brain | test | 2026-08-02 00:23 | 2026-08-02 01:06 | Success | Success | Judge | Linear | −0.068 | +0.211 | −0.150 | GO | GO | — | — | 1 |
| 24 | Olbrecht et al. 2021 | Ovarian | High-Grade Serous Tubo-Ovarian Cancer | Data_Olbrecht2021_Ovarian | test | 2026-08-05 16:54 | 2026-08-05 17:25 | Failure | Failure | Judge | — | +0.029 | +0.077 | −0.020 | — | — | — | — | 2 |
| 25 | Geistlinger et al. 2020 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Geistlinger2020_Ovarian | test | 2026-08-05 22:04 | 2026-08-05 22:52 | Success | Failure | Judge | Linear | +0.170 | +0.432 | −0.345 | GO | GO | — | — | 2 |
| 26 | Laughney et al. 2020 | Lung | Lung Cancer | Data_Laughney2020_Lung | test | 2026-08-02 03:27 | 2026-08-02 15:58 | Success | Success | Judge | Linear | −0.032 | +0.063 | −0.029 | GO | GO | — | — | 1 |
| 27 | Zhang et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Zhang2021_Kidney | test | 2026-08-05 22:04 | 2026-08-05 22:54 | Failure | Success | Judge | — | −0.034 | +0.085 | −0.060 | — | — | — | — | 2 |
| 28 | Zilionis et al. 2019 | Lung | Non-Small Cell Lung Cancer | Data_Zilionis2019_Lung | test | 2026-08-05 16:54 | 2026-08-05 17:30 | Failure | Failure | Judge | — | −0.009 | +0.039 | −0.022 | — | — | — | — | 2 |
| 29 | Choudhury et al. 2022 | Brain | Meningioma | Data_Choudhury2022_Brain | test | 2026-08-02 18:21 | 2026-08-02 21:46 | Success | Failure | Judge | — | — | — | — | NO-GO | — | — | — | 1 |
| 30 | Dong et al. 2020 | Prostate | Prostate Cancer | Data_Dong2020_Prostate | test | 2026-08-05 20:26 | 2026-08-05 21:05 | Failure | Failure | Judge | — | — | — | — | — | — | — | — | 2 |
| 31 | Jerby-Arnon et al. 2018 ⁵ | Skin | Melanoma | Data_Jerby-Arnon2018_Skin | test | 2026-08-02 23:05 | 2026-08-03 00:08 | Success | Success | Judge | Linear | −0.492 | −0.139 | +0.201 | GO | GO | — | — | 1 |
| 32 | Biermann et al. 2022 | Skin | Metastatic Melanoma | Data_Biermann2022_Skin | test | 2026-08-03 00:52 | 2026-08-03 03:12 | Success | Success | Judge | Linear | −0.050 | −0.024 | +0.045 | GO | GO | — | — | 1 |
| 33 | Maynard et al. 2020 | Lung | Lung Cancer | Data_Maynard2020_Lung | test | 2026-08-03 03:33 | 2026-08-03 12:29 | Success | Success | Judge | Linear | −0.130 | +0.210 | +0.076 | GO | GO | — | — | 1 |
| 34 | Xing et al. 2021 | Lung | Lung Cancer | Data_Xing2021_Lung | test | 2026-08-03 12:39 | 2026-08-03 13:43 | Success | Failure | Judge | Linear | −0.022 | +0.053 | −0.024 | GO | GO | — | — | 1 |
| 35 | Chan et al. 2021 ⁶ | Lung | Lung Cancer | Data_Chan2021_Lung | test | 2026-08-05 20:26 | 2026-08-05 21:54 | Failure | Success | Judge | — | +0.036 | +0.111 | −0.080 | — | — | — | — | 2 |
| 35 | Galen et al. 2019 | Hematologic | Acute Myeloid Leukemia | Data_Galen2019_Hematologic | test | 2026-08-03 14:21 | 2026-08-03 15:22 | Success | Failure | Judge | Linear | −0.012 | +0.008 | −0.004 | GO | GO | — | — | 1 |
| 35 | Gao et al. 2021 | Breast | Breast Cancer | Data_Gao2021_Breast | test | 2026-08-05 20:26 | 2026-08-05 21:18 | Failure | Failure | Judge | — | — | — | — | — | — | — | — | 2 |
| 35 | Hwang et al. 2022 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Hwang2022_Pancreas | test | 2026-08-05 20:26 | 2026-08-05 22:03 | Failure | Failure | Judge | — | −0.004 | −0.002 | +0.003 | — | — | — | — | 2 |
| 35 | Izar et al. 2020 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Izar2020_Ovarian | test | 2026-08-03 14:21 | 2026-08-03 15:03 | Success | Success | Judge | Linear | −0.154 | +0.250 | +0.041 | GO | GO | — | — | 1 |
| 35 | Jerby-Arnon et al. 2021 | Sarcoma | Synovial Sarcoma | Data_Jerby-Arnon2021_Sarcoma | test | 2026-08-05 15:19 | 2026-08-05 16:13 | Success | Failure | Judge | Linear | −0.089 | +0.323 | +0.038 | GO | GO | — | — | 2 |
| 35 | Kildisiute et al. 2021 | Neuroendocrine | Neuroblastoma | Data_Kildisiute2021_Neuroendocrine | test | 2026-08-05 15:19 | 2026-08-05 15:52 | Success | Failure | Judge | — | — | — | — | NO-GO | — | — | — | 2 |
| 35 | Krishna et al. 2021 | Kidney | Renal Cell Carcinoma | Data_Krishna2021_Kidney | test | 2026-08-03 14:21 | 2026-08-03 15:03 | Success | Failure | Judge | Linear | −0.039 | +0.044 | −0.042 | GO | GO | — | — | 1 |
| 35 | Neftel et al. 2019 | Brain | Glioblastoma | Data_Neftel2019_Brain | test | 2026-08-03 14:21 | 2026-08-03 15:25 | Success | Success | Judge | Linear | +0.017 | +0.072 | −0.047 | GO | GO | — | — | 1 |
| 35 | Pelka et al. 2021 | Colorectal | Colorectal Cancer | Data_Pelka2021_Colorectal | test | 2026-08-03 14:21 | 2026-08-03 18:12 | Success | Failure | Judge | Linear | −0.014 | +0.033 | −0.017 | GO | GO | — | — | 1 |
| 36 | Olalekan et al. 2021 ⁷ | Ovarian | Ovarian Cancer | Data_Olalekan2021_Ovarian | test | 2026-08-03 19:57 | 2026-08-03 20:21 | Success | Success | Judge | Linear | +0.018 | +0.027 | −0.028 | GO | GO | — | — | 1 |
| 36 | Young et al. 2018 | Kidney | Kidney Cancer | Data_Young2018_Kidney | test | 2026-08-05 15:19 | 2026-08-05 15:52 | Success | Failure | Judge | — | — | — | — | NO-GO | — | — | — | 2 |
| 36 | He et al. 2021 | Prostate | Metastatic Prostate Cancer | Data_He2021_Prostate | test | 2026-08-03 19:57 | 2026-08-04 13:22 | Success | Success | Judge | Linear | −0.302 | +0.055 | +0.046 | GO | GO | — | — | 1 |
| 36 | Qian et al. 2020 | Breast | Breast Cancer | Data_Qian2020_Breast | test | 2026-08-05 20:26 | 2026-08-05 21:48 | Failure | Failure | Judge | — | −0.020 | +0.031 | +0.013 | — | — | — | — | 2 |
| 36 | Paulson et al. 2020 | Skin | Merkel Cell Carcinoma | Data_Paulson2020_Skin | test | 2026-08-03 19:57 | 2026-08-03 20:31 | Success | Failure | Judge | Linear | +0.037 | +0.051 | −0.006 | GO | GO | — | — | 1 |
| 36 | Yuan et al. 2018 | Brain | High-Grade Glioma | Data_Yuan2018_Brain | test | 2026-08-03 19:57 | 2026-08-03 20:29 | Success | Failure | Judge | Linear | +0.019 | +0.035 | −0.045 | GO | GO | — | — | 1 |
| 36 | Gojo et al. 2020 | Brain | Pediatric Ependymoma | Data_Gojo2020_Brain | test | 2026-08-03 19:57 | 2026-08-04 13:22 | Success | Success | Judge | Linear | +0.116 | +0.329 | +0.003 | GO | GO | — | — | 1 |
| 36 | Raghavan et al. 2021 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Raghavan2021_Pancreas | test | 2026-08-05 16:54 | 2026-08-05 17:41 | Failure | Success | Judge | — | −0.011 | +0.072 | −0.024 | — | — | — | — | 2 |
| 36 | Cohen et al. 2021 | Hematologic | Multiple Myeloma | Data_Cohen2021_Hematologic | test | 2026-08-05 15:19 | 2026-08-05 16:31 | Failure | Failure | Judge | — | −0.022 | +0.014 | +0.001 | — | — | — | — | 2 |
| 36 | Dong et al. 2020 | Neuroendocrine | Neuroblastoma | Data_Dong2020_Neuroendocrine | test | 2026-08-03 19:57 | 2026-08-03 21:10 | Success | Failure | Judge | Linear | +0.100 | +0.232 | −0.000 | GO | GO | — | — | 1 |
| 37 | Couturier et al. 2020⁸ | Brain | Glioblastoma | Data_Couturier2020_Brain | test | 2026-08-04 14:02 | 2026-08-04 15:51 | Success | Failure | Judge | Linear | +0.004 | +0.077 | −0.044 | GO | GO | — | — | 1 |
| 37 | Filbin et al. 2018 | Brain | Pediatric H3-K27M Mutant Glioma | Data_Filbin2018_Brain | test | 2026-08-05 16:54 | 2026-08-05 17:50 | Failure | Success | Judge | — | +0.019 | +0.205 | +0.117 | — | — | — | — | 2 |
| 37 | Gaiti et al. 2019 | Hematologic | Chronic Lymphocytic Leukemia | Data_Gaiti2019_Hematologic | test | 2026-08-04 14:02 | 2026-08-04 15:29 | Success | Failure | Judge | Linear | −0.084 | −0.010 | +0.102 | GO | GO | — | — | 1 |
| 37 | Liu et al. 2021 | Hematologic | Multiple Myeloma | Data_Liu2021_Hematologic | test | 2026-08-05 15:19 | 2026-08-05 16:20 | Success | Failure | Judge | — | — | — | — | NO-GO | — | — | — | 2 |
| 37 | Nath et al. 2021 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Nath2021_Ovarian | test | 2026-08-04 14:02 | 2026-08-04 15:36 | Success | Failure | Judge | Linear | −0.004 | +0.058 | −0.010 | GO | GO | — | — | 1 |
| 37 | Pal et al. 2021 | Breast | Breast Cancer | Data_Pal2021_Breast | test | 2026-08-05 15:19 | 2026-08-05 16:53 | Failure | Failure | Judge | — | −0.007 | +0.036 | −0.034 | — | — | — | — | 2 |
| 37 | Zhang et al. 2019 | Ovarian | High-Grade Serous Ovarian Carcinoma | Data_Zhang2019_Ovarian | test | 2026-08-04 14:02 | 2026-08-04 15:07 | Success | Success | Judge | Linear | −0.011 | +0.042 | −0.034 | GO | GO | — | — | 1 |
| 37 | Li et al. 2017 | Colorectal | Colorectal Carcinoma | Data_Li2017_Colorectal | test | 2026-08-04 15:54 | 2026-08-04 16:20 | Success | Success | Judge | Linear | −0.096 | +0.112 | +0.008 | GO | GO | — | — | 1 |
| 37 | Tirosh et al. 2016 | Brain | IDH-Mutant Oligodendroglioma | Data_Tirosh2016_Brain | test | 2026-08-04 15:54 | 2026-08-04 16:20 | Success | Failure | Judge | Linear | −0.042 | +0.160 | −0.201 | GO | GO | — | — | 1 |
| 37 | Bassez et al. 2021 | Breast | Breast Cancer | Data_Bassez2021_Breast | test | 2026-08-05 16:54 | 2026-08-05 18:44 | Failure | Failure | Judge | — | −0.014 | +0.022 | −0.005 | — | — | — | — | 2 |
| 37 | Caron et al. 2020 | Hematologic | Acute Lymphoblastic Leukemia | Data_Caron2020_Hematologic | test | 2026-08-05 16:54 | 2026-08-05 17:52 | Failure | Failure | Judge | — | −0.017 | +0.000 | −0.010 | — | — | — | — | 2 |
| 37 | Griffiths et al. 2021 | Breast | Breast Cancer | Data_Griffiths2021_Breast | test | 2026-08-05 16:54 | 2026-08-05 20:25 | Failure | Success | Judge | — | −0.019 | −0.053 | +0.023 | — | — | — | — | 2 |
| 37 | Hovestadt et al. 2019 | Brain | Medulloblastoma | Data_Hovestadt2019_Brain | test | 2026-08-04 16:41 | 2026-08-04 17:16 | Success | Failure | Judge | Linear | −0.043 | +0.186 | +0.026 | GO | GO | — | — | 1 |
| 37 | Ledergor et al. 2018 | Hematologic | Multiple Myeloma | Data_Ledergor2018_Hematologic | test | 2026-08-05 16:54 | 2026-08-05 17:49 | Success | Success | Judge | Linear | −0.029 | +0.015 | +0.004 | GO | GO | — | — | 2 |
| 37 | Nam et al. 2019 | Hematologic | Myeloproliferative Neoplasms | Data_Nam2019_Hematologic | test | 2026-08-04 16:41 | 2026-08-04 17:36 | Success | Success | Judge | Linear | −0.036 | +0.008 | +0.009 | GO | GO | — | — | 1 |
| 37 | Qian et al. 2020 | Ovarian | Ovarian Cancer | Data_Qian2020_Ovarian | test | 2026-08-05 16:54 | 2026-08-05 17:28 | Success | Failure | Judge | Linear | +0.044 | +0.065 | −0.019 | GO | GO | — | — | 2 |
| 37 | Rendeiro et al. 2020 | Hematologic | Chronic Lymphocytic Leukemia | Data_Rendeiro2020_Hematologic | test | 2026-08-05 20:26 | 2026-08-05 21:06 | Failure | Success | Judge | — | −0.017 | +0.005 | +0.007 | — | — | — | — | 2 |
| 37 | Roider et al. 2020 | Hematologic | B-Cell Lymphoma | Data_Roider2020_Hematologic | test | 2026-08-04 16:41 | 2026-08-04 17:21 | Success | Failure | Judge | Linear | −0.027 | +0.002 | +0.005 | GO | GO | — | — | 1 |
| 37 | Wu et al. 2020 | Hematologic | Acute Myeloid Leukemia | Data_Wu2020_Hematologic | test | 2026-08-05 22:04 | 2026-08-05 23:47 | Failure | Failure | Judge | — | +0.002 | +0.007 | −0.004 | — | — | — | — | 2 |
| 37 | Chung et al. 2017 | Breast | Breast Cancer | Data_Chung2017_Breast | test | 2026-08-04 22:59 | 2026-08-05 01:42 | Success | Success | Judge | Linear | −0.276 | +0.124 | −0.074 | GO | GO | — | — | 1 |
| 37 | Darmanis et al. 2017 | Brain | Glioblastoma | Data_Darmanis2017_Brain | test | 2026-08-05 15:47 | 2026-08-05 15:56 | Success | Failure | Judge | Linear | +0.010 | +0.099 | +0.041 | GO | GO | — | — | 2 |
| 37 | Giustacchini et al. 2017 | Hematologic | Chronic Myeloid Leukemia | Data_Giustacchini2017_Hematologic | test | 2026-08-05 20:26 | 2026-08-05 20:49 | Success | Success | Judge | Linear | −0.093 | +0.049 | −0.033 | GO | GO | — | — | 2 |
| 37 | Gulati et al. 2020 | Breast | Breast Cancer | Data_Gulati2020_Breast | test | 2026-08-05 22:04 | 2026-08-05 22:25 | Success | Failure | Judge | — | −0.067 | +0.098 | −0.056 | GO | NO-GO | — | — | 2 |
| 37 | Karaayvas et al. 2018 | Breast | Breast Cancer | Data_Karaayvas2018_Breast | test | 2026-08-05 15:47 | 2026-08-05 16:00 | Success | Success | Judge | — | −0.220 | +0.106 | −0.067 | GO | NO-GO | — | — | 2 |
| 37 | Kim et al. 2018 | Breast | Triple-Negative Breast Cancer | Data_Kim2018_Breast | test | 2026-08-04 22:23 | 2026-08-04 23:39 | Success | Failure | Judge | Linear | −0.009 | +0.040 | −0.085 | GO | GO | — | — | 1 |
| 37 | Li et al. 2019 | Skin | Melanoma | Data_Li2019_Skin | test | 2026-08-05 22:04 | 2026-08-05 22:43 | Failure | Failure | Judge | — | −0.015 | +0.016 | −0.002 | — | — | — | — | 2 |
| 37 | Moncada et al. 2020 | Pancreas | Pancreatic Ductal Adenocarcinoma | Data_Moncada2020_Pancreas | test | 2026-08-04 22:55 | 2026-08-05 01:42 | Success | Success | Judge | Linear | −0.011 | +0.115 | −0.064 | GO | GO | — | — | 1 |
| 37 | Shih et al. 2018 | Ovarian | Ovarian Cancer | Data_Shih2018_Ovarian | test | 2026-08-04 22:23 | 2026-08-04 23:15 | Success | Success | Judge | Linear | −0.013 | +0.065 | −0.035 | GO | GO | — | — | 1 |
| 37 | Song et al. 2019 | Lung | Non-Small Cell Lung Cancer | Data_Song2019_Lung | test | 2026-08-04 22:23 | 2026-08-04 23:04 | Success | Success | Judge | Linear | −0.013 | +0.080 | −0.052 | GO | GO | — | — | 1 |
| 37 | Steen et al. 2021 | Hematologic | Diffuse Large B-Cell Lymphoma | Data_Steen2021_Hematologic | test | 2026-08-04 22:23 | 2026-08-05 01:11 | Success | Failure | Judge | Linear | −0.066 | −0.010 | +0.043 | GO | GO | — | — | 1 |
| 37 | Yost et al. 2019 | Skin | Skin Carcinoma | Data_Yost2019_Skin | test | 2026-08-04 22:23 | 2026-08-04 22:54 | Success | Success | Judge | Linear | −0.015 | +0.046 | −0.011 | GO | GO | — | — | 1 |
| 37 | Zhang et al. 2019 | Hematologic | Follicular Lymphoma | Data_Zhang2019_Hematologic | test | 2026-08-05 20:26 | 2026-08-05 20:52 | Failure | Failure | Judge | — | +0.012 | +0.006 | +0.009 | — | — | — | — | 2 |

**Legend.**
- **Analysis Order** — the sequence in which each dataset's first verdict was reviewed and logged.
- **Set** — train (calibration, HNSCC) · eval (supervised, HNSCC) · test (autonomous, other).
- **Science / Deliverables** — Success / Failure. Science = correct gate call reached by correct
  reasoning. Deliverables = §6 outputs match the binding reference (set, location, style, `summary.pdf` layout).
- **Expert interaction** — Teacher (calibrated the protocol) · Tutor (steered step-by-step) ·
  Reviewer (autonomous run, audited after the fact) · Judge (outcome adjudicated, no steering).
- **Manifold geometry** — Branching (Gast/pSom hub → pSom arm + Gast arm, cross-repression; Crest a
  terminal readout at the arm tips) · Linear (collapsed bifurcation, single continuous axis).
- **Gast μ · pSom μ · Crest μ** — mean `score_genes` module score across all malignant cells.
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
set only the regime — scientific instruction stayed in the spec files. Its substantive edits are
numbered below; each carries a superscript on the table row where it first appears. Operational
guardrails (do-not-interrupt, no new packages/environments) are omitted.

1. **Baseline regime** — named dataset; no-feedback mandate; post-hoc independent-auditor contract.
   The seed paragraph, carried verbatim thereafter.
2. **Agent-chosen dataset** — dataset choice delegated to the agent; deliverables first named as the
   recurring weak spot.
3. **Learn from the log** — reuse deliverable templates from prior *successful* runs, especially `summary.pdf`.
4. **Science + deliverables** — the flagged weak spot widened from deliverables to include science;
   this became the canonical template, unchanged through run 30 and resumed for run 32.
5. **Content steer** (run 31 only) — the sole nudge on *what* to analyze: pick a low-pSom dataset.
   Run 32 reverted to item 4, unmarked.
6. **Batch delegation / scale-up** — the item-4 template plus one instruction: select 10 datasets and
   delegate the identical autonomous instructions to 10 subagents, reviewed together. First multi-dataset
   run; all ten share Analysis Order 35.
7. **Delegate self-check** — item 6 plus one clause: the delegating agent may also check its subagents'
   science + deliverables accuracy. Second batch (all ten share Analysis Order 36).
8. **Full scale-up** — item 7 unchanged in regime, scope widened from "10 new" to "all remaining in-scope
   datasets": the final batch, 33 subagents delegated the identical instructions and reviewed together
   (all share Analysis Order 37).
9. **Science-fail re-run** — item-8 regime plus one directive: re-analyze every first-run science failure,
   hinting most were bad Gate 1/2 GO calls or missed branching.
