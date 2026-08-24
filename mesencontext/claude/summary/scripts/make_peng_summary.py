import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
NB="/home/caleb/EMToolbox/mesencontext/claude/Pancreas/Peng2019_Pancreas-2"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Pancreas/Peng2019_Pancreas-2"
gates=[
 ("Gate 1 — mixing & continuity","GO",GREEN,
  "Pre-Harmony the 16 tumours form a per-patient archipelago (iLISI median 1.0 of 16, many detached islands). "
  "With Harmony on sample they intermix into one continuous mass \u2014 iLISI median 4.05, a single kNN-graph "
  "component, 0 detached cells. Both mixed and continuous. \u03b8=2 from a mixing+geometry sweep (mixing "
  "saturates by \u03b8=2; higher \u03b8 only collapses the developmental axis, aspect 1.37\u21921.05)."),
 ("Gate 2 — module geography","GO (non-branching)",GREEN,
  "Decided on geography, not means. Not a Puram hub-and-spoke: no Gast/pSom co-expression hub (interior "
  "Gast-XOR vs pSom-XOR r=+0.29, not \u22120.49) and a PPT tree over-fits the continuous cloud (26\u201343 forks, "
  "no clean Y). Non-branching case (\u00a71): organized Gast\u2194pSom cross-repression (spatial r=\u22120.53) with "
  "a terminal neural-crest gradient \u2014 pSom\u2194Crest r=\u22120.57 (GO range: Steele \u22120.68, Moncada \u22120.56), "
  "and on the origin-rooted pseudotime Crest is the latest/terminal module (\u03c1=+0.40). Crest opposes pSom "
  "more than Gast \u2014 no Gast-arm inversion (no flag)."),
 ("Gate 3 — hub cross-repression","NA",GREY,
  "Not applicable \u2014 the manifold is non-branching (principal curve, 2 tips / 0 forks, fold-free). With no "
  "bifurcation there is no Mixed-type hub and no branch pair to test for mutual Gast\u2194pSom exclusivity, so "
  "the branching-only 04_correlation / 05_modules notebooks are not produced (per the deliverable spec)."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("Pseudotime",os.path.join(F,"manifold.pdf")),
        ("Gastrulation",os.path.join(F,"Gast_signature.pdf")),
        ("Somitogenesis",os.path.join(F,"pSom_signature.pdf")),
        ("Neural Crest",os.path.join(F,"Crest_signature.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("PDAC (Peng et al., 2019), 10x \u2014 16 tumours / 27,953 cells (master scope); malignant only: 7,945 "
 "cells across all 16 samples (\u2265100-cell floor; the multiplicative count gap is only 2.31\u00d7, mid-distribution, "
 "so no clean spillover cliff). Whole malignant manifold (two density lobes, near-identical developmental means, "
 "not scoped).")
verdict=("Pattern reproduces in the non-branching form (Linear). One continuous, sample-integrated manifold (G1 GO) "
 "carrying organized Gast\u2194pSom cross-repression with a terminal neural-crest gradient (G2 GO): rooted at the "
 "gastrulation/somitogenesis-high origin, the developmental ordering is Gast \u2192 pSom \u2192 Crest-terminal, matching "
 "the passing same-tissue Steele/Moncada PDAC runs. It lacks Puram's hub-and-spoke bifurcation, so there is no hub "
 "to test (G3 NA). EMT-TFs ZEB1 (root-side) \u2192 SNAI2 (far end); canonical SNAI1/TWIST near the detection floor.")
params=[
 ("Sample threshold","\u2265100-cell floor (mult. gap 2.31\u00d7 < 4\u00d7 degenerate); 16/16 kept \u2192 7,945 cells"),
 ("Overdispersed genes","1,288 (scFates find_overdispersed); no sc.pp.scale before PCA"),
 ("Integration","Harmony on sample, \u03b8=2 (mixing saturates by \u03b8=2; higher collapses axis 1.37\u21921.05)"),
 ("Embedding","n_pcs=20, n_neighbors=30, UMAP spread=1.3; 0 islands removed; 1 component"),
 ("Geometry","Linear (non-branching) principal curve; no hub, organized cross-repression + terminal Crest"),
 ("Root","tip 0 = Gast/pSom-high, Crest-low origin; curve fold-free (ratio 2.98); Crest terminal on DPT"),
 ("Module means (raw)","Gast \u22120.047 \u00b7 pSom +0.098 \u00b7 Crest \u22120.055 (means match Steele PASS; geography decides)"),
 ("EMT-TFs shown","ZEB1 (8.8%) & SNAI2 (9.3%) \u2014 most end-separated expressed factors; VIM excluded (not a TF)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Peng 2019 PDAC \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
