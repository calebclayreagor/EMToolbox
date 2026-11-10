import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, RED, GREY
NB='/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Rendeiro2020_Hematologic-3'
F='/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Rendeiro2020_Hematologic-3'
gates=[('Gate 1 — mixing & continuity', 'NO-GO', '#c0392b', 'Unintegrated iLISI 1.0 of 7 (complete per-patient segregation); Leiden clusters 99.3% patient-pure; patient identity 99.5% kNN-predictable. Mixing appears only when Harmony is forced (θ≥3), collapsing patient centroids rather than revealing a shared axis. Per-patient archipelago — no continuous, sample-mixed malignant manifold exists to fit.'), ('Gate 2 — module geography', 'NA', '#888888', 'Not evaluated — gate chain stops at the Gate 1 NO-GO (§6).'), ('Gate 3 — hub cross-repression', 'NA', '#888888', 'Not evaluated — branching-only; no trajectory fit.')]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset='Chronic Lymphocytic Leukemia (Rendeiro et al., 2020), 10x — 18,657 malignant cells · 7 samples / 4 patients.'
verdict='Pattern does NOT reproduce. The malignant compartment is a set of independent per-patient CLL clones, not a continuous developmental manifold. NO-GO at Gate 1; no trajectory, no bifurcation. Descriptive EMT-TF overlay: ZEB2 (12.4%), ZEB1 (3.8%).'
params=[('Sample threshold', '≥100 cells → 7 of 11 samples (18,657 cells); largest multiplicative count gap 1012→80 (12.6×)'), ('n_pcs', '20 (scree elbow at 6, floored to atlas robust range)'), ('Integration', 'Harmony on sample, swept 0→5; protocol-default θ=2 shown; higher over-integrates'), ('Island removal', 'none (disconnected components are whole patients, not noise)'), ('Geometry', 'NA (no trajectory); manifold not sample-mixed; Gate 1 NO-GO'), ('EMT-TFs', 'ZEB2 (12.4%), ZEB1 (3.8%); SNAI2/TWIST/FOXC2/PRRX2 absent')]
build_summary(os.path.join(NB,"summary.pdf"),'Rendeiro 2020 Chronic Lymphocytic Leukemia — analysis summary',gates,panels,dataset,verdict,params,run_label='run 4 of 6')
print("built")
