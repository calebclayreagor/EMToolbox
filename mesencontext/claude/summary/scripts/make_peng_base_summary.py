import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY, RED
NB="/home/caleb/EMToolbox/mesencontext/claude/Pancreas/Peng2019_Pancreas"; F="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Peng2019_Pancreas"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "16/16 samples (\u2265100 cells) intermix on one continuous manifold; no per-sample islands (0 detached cells "
  "removed). Median iLISI 4.33 = 57% of the proportional-mixing maximum (7.53); neighbour graph is a single "
  "connected component."),
 ("Gate 2 \u2014 module geography","NO-GO",RED,
  "The three module-high territories sit at three separate UMAP corners (triangle, angles 44/95/42\u00b0 \u2014 not "
  "a Gast/pSom body flowing to a Crest terminus). Gast & pSom are spatially mutually exclusive: joint-high 0.8% "
  "vs 6.2% expected if independent (enrichment 0.13, <1), so there is no co-expression hub and no co-varying "
  "body. Along the rooted axis Gast (\u03c1=\u22120.56) and pSom (\u03c1=+0.11) move in opposite directions and Crest "
  "is flat (\u03c1=+0.10; high-decile pseudotime 0.70, mid-axis, not terminal). The anti-correlation holds at every "
  "clustering scale (sub-region sweep). Neither GO pattern \u2014 branching hub nor non-branching Gast/pSom overlap "
  "\u2014 is present."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "No bifurcation (single non-branching axis); Gate 3 is not evaluated."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pancreatic ductal adenocarcinoma (Peng et al., 2019), 10x \u2014 16 patients / 27,953 cells (master "
 "scope); malignant only: 7,945 load, all 7,945 enter the trajectory (one Leiden lobe, no subtypes).")
verdict=("Pattern does not reproduce \u2014 Gate 2 NO-GO. The embryonic modules are present (pSom mean +0.10, "
 "strongest in the atlas) but resolved into three mutually-exclusive territories, not a Gast/pSom hub or "
 "co-varying body; no bifurcation, no terminal Crest. The smoothed Gast~pSom = \u22120.41 reflects two separate "
 "corners, not cross-repression within a shared hub.")
params=[
 ("Min cells/sample","\u2265 100 (keeps 16/16)"),
 ("Island removal","UMAP radius-graph (\u22120 cells)"),
 ("Root","tip max(Gast+pSom\u2212Crest)"),
 ("Integration","Harmony on sample, \u03b8=10, 30 it"),
 ("Trajectory","ElPiGraph curve N=20 \u03bc=50 \u03bb=0.3"),
 ("Geometry","non-branching blob; 1 lobe, no subtypes"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Peng 2019 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
