import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Lung/Zilionis2019_Lung"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Lung/Zilionis2019_Lung"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "6/7 samples (\u2265131 cells) intermix on one continuous manifold with no per-patient / per-histology islands "
  "(radius-graph: 0 detached; iLISI median 1.00\u21923.35 of 6); both Leiden lobes carry all 6 samples and both "
  "histologies (LUAD+LUSC). Read on the embedding, not a scalar alone."),
 ("Gate 2 \u2014 module geography","GO (non-branching, Crest-flagged)",GREEN,
  "Single dominant Gast\u2192pSom axis: gastrulation high at the origin declines along pseudotime (\u03c1=\u22120.58) while "
  "somitogenesis rises to a terminal readout (\u03c1=+0.77; pSom-high decile mean pt 0.99). Strong Gast\u2194pSom "
  "cross-repression (smoothed r=\u22120.53, near Puram \u22120.49) but joint-high enrichment 0.73 < 1 \u2014 mutually "
  "exclusive, one axis not a co-expression hub. FLAG: Crest is globally depleted and weakly U-shaped (high at "
  "BOTH tips, lowest mid; t\u00b2>0, p<0.001) \u2014 not the reference terminal readout."),
 ("Gate 3 \u2014 hub mutual exclusivity","NA",GREY,
  "Single monotone axis \u2014 no bifurcation and no Gast/pSom co-expression hub, so there is no branch pair to test "
  "for mutual exclusivity (the Wu 2021 organised-cross-repression non-branching case)."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("NSCLC (Zilionis et al. 2019), inDrop \u2014 7 patients / 31,179 cells (master scope); malignant only: "
 "3,920 cells across 6 malignant-bearing samples (drop 1 sub-100 spillover sample, p2) enter preprocessing; "
 "the whole malignant manifold (no lobe scoping) enters the trajectory.")
verdict=("Non-branching pattern reproduces \u2014 Gate 1 GO, Gate 2 GO, Gate 3 NA. Zilionis\u2019s NSCLC malignant "
 "manifold is a single monotone gastrulation \u2192 somitogenesis axis with strong Gast\u2194pSom cross-repression "
 "(smoothed r=\u22120.53), but the decisive hub test shows the two are mutually exclusive (joint-high enrichment "
 "0.73 < 1), so it is one axis, not Puram\u2019s co-expression hub \u2014 no bifurcation, and Gate 3 has no hub to test. "
 "The two density lobes are NOT a proliferative split (6.4% cycling; both lobes low) nor histological nor "
 "single-patient; the axis is cell-cycle-free (survives non-cycling cells, r=\u22120.53) so the whole manifold is "
 "kept. EMT-TFs are weak & root/early-loaded: SNAI2 (root) \u2192 FOXC1 (terminus) chosen by data over Puram\u2019s "
 "pair, though end-separation is small (\u0394pt=0.02). Crest is the weak link: globally depleted and only shallowly "
 "U-shaped (high at both tips, not terminal) \u2014 flagged.")
params=[
 ("Min cells/sample","\u2265131 (dominant cliff 232\u219275, ratio 3.09; drops p2; 6/7)"),
 ("Integration","Harmony \u03b8=10; PCA50; n_pcs=20; spread=1.3"),
 ("Island removal","radius-graph 6\u00d7 median NN \u2014 0 removed"),
 ("Root node","Gast-high / pSom-low curve tip 2"),
 ("Geometry","non-branching single axis (curve 2 tips, 0 forks, fold-free)"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100 (ElPiGraph)"),
 ("Scope","whole manifold (no lobe scoping)"),
 ("EMT-TFs","SNAI2 (early) \u2192 FOXC1 (late), 3% floor"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Zilionis 2019 NSCLC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
