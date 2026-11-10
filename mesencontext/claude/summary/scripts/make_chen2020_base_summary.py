import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck"; F="/home/caleb/EMToolbox/figures/mesencontext/claude/Head-and-Neck/Chen2020_Head-and-Neck"
gates=[
 ("Gate 1 \u2014 mixing & continuity","NO-GO",RED,
  "Continuous (1 connected component, 100% of cells) BUT not mixed: across the integration-strength sweep "
  "73%\u219256%\u21921% of cells sit in patient-pure Leiden clusters (\u03b8=1/2/3); diff-sample neighbour fraction "
  "0.30 at \u03b8=2 vs 0.69 ceiling. The purest clusters (99% P11) are non-cycling genuine patient-private CNV "
  "states, not a shared axis. P11+P01 alone = 72% of cells. \u03b8=3 forces mixing only by over-integrating "
  "(a detached speck appears). Do not force a trajectory."),
 ("Gate 2 \u2014 module geography","NA",GREY,
  "Not evaluated \u2014 gate chain stops at Gate 1 NO-GO (no manifold / signatures / correlation / modules "
  "notebooks produced)."),
 ("Gate 3 \u2014 cross-repression","NA",GREY,
  "Not evaluated \u2014 no manifold, no hub."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("EBV-associated nasopharyngeal carcinoma (Chen et al., 2020), 10x; 3,674 malignant cells across 8 samples.")
verdict=("Pattern does NOT reproduce \u2014 Gate 1 NO-GO. The malignant compartment clusters by patient, not into "
 "a sample-integrated continuous manifold, so no trajectory is fit.")
params=[
 ("Min-cell threshold","62 (median-restricted spillover gap 107\u219236, \u00d72.97)"),
 ("Overdispersed genes","1,290 (GAM)"),
 ("n_pcs","6 (scree elbow)"),
 ("Integration","Harmony \u03b8=2 (balance of the \u03b8=1\u20133 sweep)"),
 ("Geometry","none \u2014 Gate 1 NO-GO, no trajectory"),
 ("EMT-TFs (descriptive, \u22653%)","PRRX1 62% \u00b7 SNAI2 24% \u00b7 FOXC1 13% \u00b7 ZEB2 13% \u00b7 ZEB1 7% \u00b7 TWIST2 6%; SNAI1/TWIST1 below floor"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Chen 2020 NPC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
