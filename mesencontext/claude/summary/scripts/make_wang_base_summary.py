import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Brain/Wang2019_Brain"
F="/home/caleb/EMToolbox/figures/mesencontext/claude/Brain/Wang2019_Brain"
gates=[
 ("Gate 1 \u2014 mixing & continuity","GO",GREEN,
  "7/10 samples (\u2265237 cells) intermix on one continuous manifold; no per-patient islands (16 detached cells "
  "removed); Harmony drops same-sample neighbour fraction 0.99\u21920.63, iLISI 1.01\u21922.00."),
 ("Gate 2 \u2014 module geography","GO (non-branching)",GREEN,
  "Single developmental axis, not a bifurcation: Gast & pSom co-vary weakly (r=+0.15), Crest is the inverse "
  "terminal gradient (vs pSom r=\u22120.87; Crest-high decile at pseudotime 0.86). No competing arms."),
 ("Gate 3 \u2014 hub cross-repression","NA",GREY,
  "Branching-only test. Non-branching manifold has no Gast/pSom hub bifurcation, so the mutual-exclusivity "
  "correlation is not defined here."),
]
panels=[("Manifold \u2014 samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Glioblastoma (Wang et al., 2019), 10x \u2014 10 patients / 16,317 cells (master scope); 9,916 malignant "
 "cells, 9,634 after thresholding thin samples and removing detached islands.")
verdict=("Pattern reproduces (non-branching). A single embryonic axis runs from a gastrulation/somitogenesis-high "
 "origin to a neural-crest-high terminus; pseudotime is developmental, not proliferative (cycle-score rho +0.02). "
 "EMT-TF axis ZEB1 (root) \u2192 PRRX1 (terminus).")
params=[
 ("Min cells/sample","\u2265237 (largest multiplicative gap; keeps 7/10)"),
 ("PC count","30 (chord-elbow 8 over-cuts \u2014 Chen2020 lesson)"),
 ("Integration","Harmony on sample, \u03b8=10 (mixing plateau)"),
 ("Island removal","UMAP radius-graph, \u221216 cells / 1 island"),
 ("Trajectory","scFates curve N=20 \u03bb=0.3 \u03bc=100 (fold-free, ratio 2.87)"),
 ("Root","curve tip 2 = pSom/Gast-high, Crest-low"),
 ("Subtypes","3CA meta-programs (Neftel: Astro / MES-Hypoxia / OPC) + Wang 2019"),
 ("Geometry","Linear-pSom/Crest (single axis; pSom strongest globally)"),
]
build_summary(os.path.join(NB,"summary.pdf"),"Wang 2019 Glioblastoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built", os.path.join(NB,"summary.pdf"))
