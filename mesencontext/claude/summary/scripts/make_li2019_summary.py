import sys, os
sys.path.insert(0,"/home/caleb/EMToolbox/mesencontext/claude/summary")
from build_summary import build_summary, GREEN, GREY
RED="#c0392b"
NB="/home/caleb/EMToolbox/mesencontext/claude/Skin/Li2019_Skin-3"
F ="/home/caleb/EMToolbox/figures/mesencontext/claude/Skin/Li2019_Skin-3"
gates=[
 ("Gate 1 — mixing & continuity","NO-GO",RED,
  "Harmony reaches near-maximal sample mixing (iLISI 1.00\u21921.78 of 3), but the malignant structure resolves into TWO "
  "density lobes that are transcriptomically disconnected \u2014 inter-cluster PAGA on the PCA-space graph \u2248 0.001 (~0), "
  "invariant across n_pcs 20/30 \u00d7 \u03b8 10/15, and stronger integration never merges them. Neither lobe reproduces the "
  "embryonic axis (in both, Gast/pSom ANTI-correlate rather than co-vary). A broken manifold with no cell-state "
  "continuum \u2014 a trajectory is not forced."),
 ("Gate 2 — module geography","N/A",GREY,
  "Not evaluated \u2014 Gate 1 NO-GO halts the chain before the signature step."),
 ("Gate 3 — cross-repression","N/A",GREY,
  "Not evaluated \u2014 branching-only; no trajectory fit."),
]
panels=[("Manifold — samples",os.path.join(F,"samples.pdf")),
        ("EMT-TF expression",os.path.join(F,"expression.pdf"))]
dataset=("Melanoma (Li et al., 2019), MARS-seq immunotherapy atlas \u2014 1,082 malignant cells across 3 tumours "
 "(3/20 clear the \u226556-cell threshold). Gate 1 NO-GO: two disconnected lobes.")
verdict=("The embryonic-program pattern does NOT reproduce in Li et al. 2019. The small malignant compartment (1,082 "
 "cells, 3 tumours) forms two transcriptomically disconnected lobes rather than one integrated, continuous cell-state "
 "manifold, and the Gast/pSom/Crest modules are salt-and-pepper with no coherent geography \u2014 Gast and pSom "
 "anti-correlate in each lobe instead of co-varying. Gate 1 is a NO-GO; Gates 2\u20133 are not evaluated. EMT-TFs "
 "(ZEB2, SNAI2) are reported unconditionally on the best-attempt embedding, without a pseudotime claim.")
params=[
 ("Malignant load","1,160 cells of 78,336 (MARS-seq atlas); Malignant subset only"),
 ("Sample threshold","\u226556 cells (largest gap 154\u219221, ratio 7.3) \u2192 p25/p21/p26, 1,082 cells"),
 ("Overdispersed genes","217 (scFates GAM); PCA n_pcs=20"),
 ("Integration","Harmony on sample \u03b8=10 (near-maximal iLISI; higher over-corrects, no merge)"),
 ("Continuity test","UMAP radius-graph lobes + PAGA on the PCA graph (layout-independent)"),
 ("EMT-TFs","ZEB2 (43%) + SNAI2 (27%), top-decile expressers; no pseudotime claim"),
 ("Geometry","none \u2014 trajectory not fit (Gate 1 NO-GO)"),
]
out=os.path.join(NB,"summary.pdf")
build_summary(out,"Li 2019 melanoma \u2014 analysis summary",gates,panels,dataset,verdict,params)
print("built",out)
