import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Pal2021_Breast"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Pal2021_Breast"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Mixing + continuity judged on the regenerated embedding. iLISI 1.0 \u2192 4.96 of 22 samples (Harmony \u03b8=10); "
  "one continuous connected component (11 speck cells removed). A proliferation compartment (76% cycling, 14,165 "
  "cells) is resolved before the GO \u2192 the trajectory is scoped to the low-cycling developmental Body "
  "(45,191 cells)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "No Gast/pSom two-arm hub; a single embryonic axis runs pSom-high (origin) \u2192 Crest-high (terminus). Smoothed "
  "pSom vs Crest r=\u22120.93; joint pSom&Crest enrichment 0.23 (<1, inverse gradient). Crest terminal (high-decile "
  "pseudotime 0.92); Gast weak and flat."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Branching-only gate \u2192 not applicable (single linear axis, no bifurcation to test for cross-repression)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Breast cancer (Pal et al., 2021), 10x \u2014 45 samples / 305,224 cells (master scope); 59,356 malignant "
 "cells (22 samples). Trajectory scoped to the low-cycling developmental Body (45,191 cells; 14,165-cell cycling "
 "compartment excluded).")
verdict=("The embryonic pattern reproduces as the NON-BRANCHING case \u2014 one continuous, sample-integrated "
 "malignant manifold carrying a single somitogenesis\u2192neural-crest developmental axis, with no Gast/pSom "
 "bifurcation. Gate 1 GO / Gate 2 GO / Gate 3 NA. EMT-TFs PRRX2 (strongest root) & FOXC1 (most expressed, 16%) "
 "\u2014 all detected factors origin-enriched (no terminus factor). Module strength Gast \u03bc=\u22120.007 \u00b7 "
 "pSom \u03bc=+0.036 \u00b7 Crest \u03bc=\u22120.034 \u2192 Linear-pSom/Crest.")
params=[
 ("Min-cell threshold","\u226512 (geom-mean of 56\u21923 cliff, ratio 18.67); keeps 22 of 26"),
 ("Integration","Harmony on sample, \u03b8=10 (swept 2/5/10); n_pcs=20, spread=1.3, 3733 overdispersed"),
 ("Sub-region scoping","Leiden res=0.15 \u2192 2 lobes; Cycling lobe (76% cycling) excluded"),
 ("Geometry","Non-branching curve (scFates N=20 \u03bb=0.3); 2 tips, 0 forks, fold-free (SA 2.98)"),
 ("Root node","curve tip 0 \u2014 pSom/Gast-high, Crest-low, 9% cycling; pt vs prolif \u03c1=+0.01"),
 ("EMT-TFs","PRRX2 (strongest root) & FOXC1 (16%) \u2014 all detected origin-enriched; VIM excluded"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Pal 2021 Breast \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
