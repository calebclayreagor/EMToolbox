import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Filbin2018_Brain"; F="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Filbin2018_Brain"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Malignant structure is sample-mixed AND continuous. iLISI 1.00\u21923.81 of 6 samples after Harmony(\u03b8=10); "
  "one connected component on the independent Harmony-PCA graph (no islands removed). Gast is not "
  "proliferation-confounded (prolif\u2013Gast \u03c1=+0.09)."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Non-branching embryonic axis. Gast/pSom co-localise (joint enrichment 1.54; spatial r=+0.61) as one "
  "developmental origin; Crest is an inverse terminal gradient (pSom&Crest joint 0.22; Crest-high decile "
  "pseudotime 0.99). No Gast/pSom hub diverging into two arms \u2014 GO (non-branching)."),
 ("Gate 3 \u2014 cross-repression","NA",GREY,
  "Not applicable \u2014 no bifurcation. A single principal curve (2 tips, 0 forks) fits the manifold, so there is "
  "no branch point at which to test mutual Gast\u2194pSom cross-repression."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pediatric H3-K27M mutant glioma (Filbin et al., 2018), SmartSeq2; 2,259 malignant cells across 6 "
 "samples (all kept, \u2265100 floor). One continuous non-branching manifold.")
verdict=("Pattern reproduces (non-branching). One continuous gastrulation/somitogenesis \u2192 neural-crest axis, "
 "rooted at the Gast/pSom-high origin; Crest a terminal inverse gradient. G1 GO \u00b7 G2 GO \u00b7 G3 NA \u2014 "
 "Linear-pSom/Crest.")
params=[
 ("Min-cell threshold","\u2265100 floor \u2192 all 6 samples kept (2,259 cells); 141\u2013667 smooth, no cliff"),
 ("Integration","Harmony on sample, \u03b8=10, n_pcs=20; patient batch 0.96, plateaus by \u03b8=5"),
 ("Geometry","scFates curve, Nodes=20 \u2014 non-branching (2 tips, 0 forks; self-approach 2.97)"),
 ("Root node","Gast/pSom-high, Crest-low tip 2 \u2014 developmental origin; non-cycling"),
 ("Islands removed","0 \u2014 single connected component (UMAP + Harmony-PCA graph)"),
 ("EMT-TFs shown","SNAI2 (early) \u00b7 ZEB2 (late) \u2014 best-demarcating pair; ZEB1/ZEB2/PRRX1 broad"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Filbin 2018 pediatric H3-K27M glioma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
