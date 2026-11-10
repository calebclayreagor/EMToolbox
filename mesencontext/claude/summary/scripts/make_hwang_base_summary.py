import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY, RED
NB="/home/caleb/EMToolbox/mesencontext/claude/Pancreas/Hwang2022_Pancreas"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Hwang2022_Pancreas"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "38 retained patients intermix on one continuous manifold (same-sample neighbour fraction 0.96\u21920.20 across "
  "the \u03b8 sweep, near the mixing floor); radius-graph leaves one connected component."),
 ("Gate 2 \u2014 module geography","NO-GO",RED,
  "Pattern ABSENT. Three mutually-exclusive territories, not a hub\u2192arms axis: all modules pairwise "
  "anti-correlated (Gast/pSom \u22120.33, pSom/Crest \u22120.39, Gast/Crest \u22120.30) and no two co-occur (all "
  "joint-high enrichments depleted \u2192 no convergence hub). Crest mid-axis (decile pt 0.50), NOT terminal."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not branching and Gate 2 NO-GO \u2014 cross-repression test not applicable."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pancreatic ductal adenocarcinoma (Hwang et al., 2022), 10x; 64,538 malignant cells across 38/43 samples "
 "(\u226514-cell threshold). Whole malignant manifold; cell cycle flat across lobes.")
verdict=("Embryonic pattern does NOT reproduce (Gate 1 GO / Gate 2 NO-GO / Gate 3 NA). Modules resolve into three "
 "exclusive non-developmental territories with no terminal Crest readout \u2014 the Peng2019 same-PDAC NO-GO "
 "signature; territories track EMT-III / G2-M / classical states, not one developmental axis.")
params=[
 ("Min cells/sample","14 (mult-gap 24\u21929, ratio 2.67; 38/43)"),
 ("Scope","whole manifold (cell cycle flat)"),
 ("Root node","Gast-high tip (developmental origin)"),
 ("Integration","Harmony \u03b8=10 on sample; n_pcs=20"),
 ("Trajectory","scFates curve N=20 (PPT rejected)"),
 ("EMT-TFs","PRRX2 (early) \u00b7 FOXC1 (late)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Hwang 2022 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
