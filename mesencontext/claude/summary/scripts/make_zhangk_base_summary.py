import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Kidney/Zhang2021_Kidney"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Kidney/Zhang2021_Kidney"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "7/8 samples (\u2265369 cells, dominant 710\u2192192 cliff) intermix on one continuous manifold: iLISI 1.00\u21923.17, "
  "single kNN component (0 detached) at every \u03b8; no patient-private island (kNN-purity 4.6\u00d7 vs 4.5\u00d7, no standoff)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single developmental axis: pSom-high origin \u2192 neural-crest terminus. Crest\u2194pSom spatially anti-correlated "
  "(r=\u22120.91); Crest rises along pseudotime (\u03c1=+0.48, high-decile pt 0.72 = terminal); joint pSom&Crest enrichment "
  "0.26 (<1 = inverse gradient, not a co-expression hub). No Gast/pSom arms, no bifurcation. Crest terminal, no "
  "inversion flag."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Not tested \u2014 no bifurcation and no hub to run 04_correlation/05_modules on (branching-only gate)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Clear-cell renal cell carcinoma (Zhang et al., 2021), 10x \u2014 8 patients / 11,410 malignant load; "
 "11,218 across 7 samples (\u2265369 cells) enter the manifold.")
verdict=("Pattern reproduces (non-branching). Gate 1 GO, Gate 2 GO, Gate 3 NA: RCC malignant cells form one "
 "continuous developmental axis \u2014 posterior-somitogenesis origin \u2192 neural-crest terminus, Crest inverse "
 "gradient. EMT programme is root-loaded: ZEB2 (24% det.) concentrates at the pSom origin; no terminus EMT-TF.")
params=[
 ("Min cells/sample","\u2265369 (geom-mean cliff; keeps 7/8)"),
 ("Island removal","none (kNN-purity, no standoff)"),
 ("Root","tip 0 = pSom-high / Crest-low origin"),
 ("Geometry","non-branching (curve 2 tips 0 forks)"),
 ("Subtypes","3CA meta-programs (mp_top)"),
 ("Integration","Harmony on sample, \u03b8=10, 30 it"),
 ("Trajectory","scFates curve N=20, \u03bb=0.3, \u03bc=100"),
 ("n_pcs","20 (10x precedent; scree top-heavy)"),
 ("Signatures","score_genes, union control pool"),
 ("EMT-TFs","ZEB2 (root) / SNAI2, root-loaded"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Zhang 2021 RCC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
