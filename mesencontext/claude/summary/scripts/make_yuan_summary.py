import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Yuan2018_Brain"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Yuan2018_Brain"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "8 samples intermix per-neighbourhood (iLISI 1.0\u21924.08/8) on one continuous manifold (single kNN component, 0 "
  "islands); no per-patient archipelago."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Gast/pSom co-vary (r=+0.23) and both oppose Crest (\u22120.66 / \u22120.75): one developmental axis, Crest an inverse "
  "terminal gradient. Non-branching case."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation (curve: 2 tips, 0 forks, fold-free across params) \u2192 not tested."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("High-grade glioma (Yuan et al., 2018), microwell array-based platform (UMI counts) \u2014 20,080 malignant "
 "cells (8/8 samples); embryonic-program cell-state analysis.")
verdict=("The embryonic-program pattern reproduces as the non-branching case: a single continuous "
 "gastrulation/somitogenesis \u2192 neural-crest developmental axis, rooted at the Gast/pSom-high pole with Crest as an "
 "inverse terminal gradient. No Gast\u2013pSom bifurcation (Gate 3 NA). Linear-pSom/Crest geometry (pSom \u03bc=+0.035 "
 "globally strongest).")
params=[
 ("Min-cell threshold","\u2265100 floor (largest gap 2012\u2192598, r=3.36); 8/8, 20,080 cells"),
 ("Genes / embedding","729 overdispersed (GAM); n_pcs=20; Harmony \u03b8=10"),
 ("Islands removed","0 (single connected kNN component)"),
 ("Geometry","Non-branching; scFates curve N=20, \u03bb=0.3, \u03bc=100 (2 tips, 0 forks)"),
 ("Root","curve tip 0 = Gast/pSom-high, Crest-low (Crest is late)"),
 ("Module means (raw)","pSom \u03bc=+0.035 globally strongest (Linear-pSom/Crest)"),
 ("EMT-TFs","ZEB1 (14%, root) \u00b7 PRRX1 (9%, terminus); Snail/Twist/FoxC near-absent"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Yuan 2018 high-grade glioma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
