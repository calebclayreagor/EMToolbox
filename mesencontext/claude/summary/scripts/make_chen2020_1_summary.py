import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, RED, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-1"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck-1"
gates=[
 ("Gate 1 \u2014 mixing & continuity","NO-GO",RED,
  "Continuous (1 connected component) but NOT sample-mixed: ~50% of cells in patient-pure clusters at \u03b8=2 "
  "(~90% at \u03b8=1), robust across n_pcs {15,20,30} \u2014 not the attempt-1 n_pcs=6 artifact. Purest clusters = "
  "non-cycling P11 (patient-private CNV). Only \u03b8=3 mixes, by over-integrating."),
 ("Gate 2 \u2014 module geography","NA",GREY,
  "Not evaluated \u2014 no sample-integrated continuous manifold on which to fit a trajectory / score module "
  "geography."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not evaluated \u2014 requires a branching trajectory with an identified hub, which Gate 1 precludes."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Nasopharyngeal carcinoma (Chen et al., 2020), 10x \u2014 14 patients / 71,896 cells (master scope); "
 "malignant only: 3,763 load \u2192 3,674 across 8 patients (\u226562 cells) enter the embedding.")
verdict=("Pattern does NOT reproduce \u2014 Gate 1 NO-GO. The malignant compartment is patient-segregated "
 "(inter-patient CNV heterogeneity), not a shared sample-integrated developmental manifold. No hub, no "
 "trajectory, no cross-repression axis to test. EMT-TFs shown for reference: PRRX1 / SNAI2 (FOXC/PRRX families; "
 "canonical SNAI1 & TWIST1 below the 3% detection floor).")
params=[
 ("Min cells/sample","62 (median-restricted gap; keeps 8/14)"),
 ("Genes","1,290 over-dispersed (GAM)"),
 ("n_pcs","20 (re-derived; K\u00fcrten 20 / Puram 40)"),
 ("Integration","Harmony on sample, \u03b8=2, 20 it"),
 ("Embedding","UMAP, Leiden res=0.5 \u2192 9 clusters"),
 ("Trajectory","none (Gate 1 NO-GO)"),
 ("EMT-TF panel","detection-gated \u22653%; PRRX1/SNAI2/FOXC1"),
 ("Geometry","patient-segregated (not a manifold)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Chen 2020 NPC \u2014 analysis summary",gates,panels,dataset,verdict,params,
              run_label="run 2 of 7")
print("built", os.path.join(NB,"summary.pdf"))
