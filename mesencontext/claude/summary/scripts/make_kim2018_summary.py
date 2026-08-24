import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Breast/Kim2018_Breast"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Breast/Kim2018_Breast"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Harmony (\u03b8=10) on sample: same-sample neighbour fraction 0.99\u21920.40; iLISI 3.89 of 9 samples; continuity "
  "confirmed off the independent PCA-harmony graph (1 connected component), 0 islands."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Single axis: pSom-high origin \u2192 Gast/Crest-high terminus. Organized Gast\u2194pSom cross-repression (smoothed "
  "r=\u22120.84); Crest a terminal gradient. FLAG: Crest enriches the Gast pole (inversion) \u2014 passes anyway."),
 ("Gate 3 — cross-repression","NA",GREY,
  "No bifurcation (curve: 2 tips, 0 forks) \u2014 branching-only Gate 3 not applicable."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Triple-negative breast cancer (Kim et al., 2018), Nanogrid \u2014 2,263 malignant cells across 9 samples "
 "(9/16 kept at \u2265100-cell floor). Non-branching Linear-pSom/Crest.")
verdict=("The embryonic-program pattern reproduces as a non-branching linear axis: a single continuous, "
 "sample-integrated manifold from a pSom-high developmental origin to a Gast/Crest-high terminus, with organized "
 "Gast\u2194pSom cross-repression and Crest as a terminal gradient enriched on the Gast pole (inversion flag). No "
 "bifurcation \u2192 Gate 3 NA. EMT-TF expression (FOXC1, SNAI2) concentrates at the root/origin end; no EMT-TF marks "
 "the terminus in this dataset.")
params=[
 ("Min-cell threshold","\u2265100 (floor coincides with real 52\u2192100 inflection) \u2192 9/16, 2,263 cells"),
 ("Embedding","HVG=536; PCA50; Harmony \u03b8=10 (TNBC patient batch); n_pcs=20, spread=1.3"),
 ("Trajectory","scFates curve (non-branching), N=20, \u03bb=0.3, \u03bc=100; fold-free (2.98)"),
 ("Root","pSom-high/Crest-low developmental origin (Crest is late)"),
 ("Geometry","Linear-pSom/Crest (raw Gast \u22120.009, pSom +0.040, Crest \u22120.085)"),
 ("EMT-TFs","FOXC1 (65%, \u03c1=\u22120.41) + SNAI2 (\u03c1=\u22120.23); BOTH root/origin-enriched, none terminal"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Kim 2018 TNBC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
