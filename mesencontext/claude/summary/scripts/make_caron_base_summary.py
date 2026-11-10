import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Hematologic/Caron2020_Hematologic"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Hematologic/Caron2020_Hematologic"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "Malignant manifold is sample-mixed AND continuous. 8 patients across 3 genetic ALL groups (ETV6-RUNX1 Pre-B, "
  "high-hyperdiploid B-ALL, Pre-T) merge on ONE connected component after Harmony (\u03b8=10) on sample. iLISI "
  "1.00\u21924.71 of 8. Leiden split is proliferation (cycling 0.87 vs 0.06), not B-vs-T lineage; 0 islands removed."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Embryonic pattern present as organized cross-repression, NOT a convergence hub. Gast & pSom sit at opposite "
  "poles (smoothed r=\u22120.45; joint-high enrichment 0.81<1); Crest is an inverse/terminal gradient (pSom\u2013Crest "
  "r=\u22120.72). Root Gast-high (\u03c1=\u22120.72 vs pseudotime) \u2192 terminus Crest-high (\u03c1=+0.33). No bifurcation."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Not evaluated \u2014 non-branching topology (principal curve, 2 tips, 0 forks, fold-free). No tree node-clusters, "
  "so no mutual Gast\u2013pSom cross-repression test applies. Terminates at the expression step."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Pediatric acute lymphoblastic leukemia (Caron et al., 2020), 10x \u2014 8 malignant samples / 25,788 "
 "cells across 3 genetic ALL groups (ETV6-RUNX1 Pre-B, high-hyperdiploid B-ALL, Pre-T).")
verdict=("Pattern reproduces as the NON-BRANCHING case: a single embryonic axis with organized Gast\u2013pSom "
 "cross-repression (r=\u22120.45) and an inverse terminal neural-crest gradient \u2014 a strict linear subset of the "
 "Puram hub-and-spoke, with no bifurcation. Root Gast/pSom-high \u2192 terminus Crest-high. Gate 1 GO / Gate 2 GO / "
 "Gate 3 NA. EMT-TFs ZEB2 (root) \u2192 ZEB1 (terminus).")
params=[
 ("Min-cell threshold","floor 100 (no dominant cliff; all 8 samples \u22651585) \u2192 8/8 kept, 25,788 cells"),
 ("Integration","Harmony on sample, \u03b8=10 (same-sample nbr frac 0.999\u21920.272; 3 genetic ALL groups)"),
 ("Embedding","PCA 50\u219220 on X_pca_harmony, k=30, spread=1.3, seed=1; radius-graph 0 removed"),
 ("Geometry","principal CURVE (scFates EPG N=20 \u03bb=0.3 \u03bc=100); PPT over-forks a dense blob; curve fold-free"),
 ("Root","curve tip 0 (Gast/pSom-high, Crest-low) \u2014 never Crest (late) or a cycling state"),
 ("Modules","score_genes union control pool (Gast 66/81, pSom 77/98, Crest 93/104); RAW per-cell scores"),
 ("EMT-TFs (>3%)","ZEB2 (40.6%), ZEB1 (8.9%), SNAI1 (6.8%); overlay pair ZEB2\u2192ZEB1"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Caron 2020 Pediatric ALL \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
