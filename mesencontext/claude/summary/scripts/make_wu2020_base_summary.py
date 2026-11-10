import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Wu2020_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Wu2020_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Harmony \u03b8=10 on sample (iLISI 9.37 of 23.63 ceiling climbs to \u03b8=10, drops at \u03b8=20). After removing 20 "
  "cells in 17 detached specks, all 96,881 cells form ONE connected component: samples intermix per-neighbourhood "
  "on a single continuous manifold. Judged on the regenerated embedding, not a scalar alone."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single Gast/pSom-high \u2192 Crest-high developmental axis. Organized Gast\u2194pSom cross-repression (smoothed "
  "r=\u22120.68); Crest opposes Gast (r=\u22120.67), co-varies weakly with pSom (r=+0.11) and rises to the terminus "
  "(Crest-high decile at pseudotime 0.82; Spearman \u03c1=+0.43). No Gast/pSom co-expression hub and no opposing "
  "Gast arm \u2014 non-branching, not a bifurcation. Crest terminal, not on the Gast arm (no inversion flag)."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Branching-only. The manifold does not bifurcate \u2014 the diagnostic tree fit shows no Gast/pSom co-expression "
  "hub and no opposing Gast arm (both non-root tips are pSom-high / Crest-low), and the committed curve is "
  "fork-free. There is no hub population to test, so Gate 3 does not apply."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Acute myeloid leukemia (Wu et al., 2020), Microwell-seq \u2014 96,881 malignant cells (36 samples); single "
 "low-cycling body (cycling fraction 0.001).")
verdict=("The embryonic-program pattern reproduces in a NON-BRANCHING form: one continuous, sample-integrated AML "
 "manifold carrying a single Gastrulation/Somitogenesis-high \u2192 Neural-crest-high developmental axis with "
 "organized Gast\u2194pSom cross-repression (r=\u22120.68) and a terminal Crest gradient. No bifurcation, so Gate 3 is "
 "NA. Gate 1 & 2 GO; geometry Linear-pSom/Crest. EMT-TF ZEB2 (5.1%) is the sole detectable canonical factor.")
params=[
 ("Min-cell threshold","100 (floor; no dominant cliff) \u2192 36/38 samples, 96,901 cells (dropped P18, P13)"),
 ("Integration","Harmony \u03b8=10, n_pcs=20, k=30, spread=1.3 (iLISI peaks \u03b8=10, falls \u03b8=20); 443 overdispersed"),
 ("Island removal","20 cells / 17 specks (UMAP radius graph 6\u00d7 median NN) \u2192 96,881"),
 ("Geometry","Non-branching curve N=20, fold-free (SA 2.90); |corr(t, DC1)|=0.91"),
 ("Root","curve tip at Gast/pSom-high, Crest-low pole; pt vs cycling \u03c1=\u22120.07"),
 ("Module means (raw)","pSom +0.007 > Gast +0.002 > Crest \u22120.004 (Linear-pSom/Crest)"),
 ("EMT-TF readout","ZEB2 (5.1%) \u2014 sole detectable canonical EMT-TF; broad panel below floor/absent"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Wu 2020 AML \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
